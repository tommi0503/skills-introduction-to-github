from pathlib import Path
from html.parser import HTMLParser
import re,json,collections,sys
BASE=Path('/workspace/output');REF=Path('/workspace/work/reference')
NAMES=['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse']
CONTRACTS=json.loads((REF/'contract/taxonomy.json').read_text())['contracts'];ROOTS={r:c['id'] for c in CONTRACTS for r in c['roots']}
GOLD={'card':['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone'],'callout':['callout','callout-icon','callout-stack'],'chart-area':['area-1','areas-2','areas-stacked-3','area-3pt'],'chart-bar':['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2'],'chart-donut':['donut','donuts-3','donuts-4','donut-0','donut-100'],'chart-line':['lines-12','lines-6','lines-3','lines-flat']}
VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class Parser(HTMLParser):
 def __init__(self,name):super().__init__();self.name=name;self.stack=[];self.errors=[];self.roots=[]
 def handle_starttag(self,t,a):
  d=dict(a);cl=d.get('class','').split();parent=self.stack[-1] if self.stack else None;owner=parent['owner'] if parent else None
  if not parent:self.roots.append((t,d))
  if parent and 'list' in parent['class'] and 'item' not in cl:self.errors.append('List direct child lacks .item: '+t+' '+str(cl))
  found=[(r,ROOTS[r]) for r in cl if r in ROOTS]
  if found:
   r,c=found[0]
   if not (r=='lines' and owner=='code.block@1'):
    if c!=owner and not d.get('data-el'):self.errors.append('Nested '+r+' lacks data-el')
    owner=c
  if d.get('data-el') and not d['data-el'].startswith(self.name+'-'):self.errors.append('Foreign data-el '+d['data-el'])
  if t not in VOID:self.stack.append({'owner':owner,'class':cl,'tag':t})
 def handle_endtag(self,t):
  if self.stack:self.stack.pop()
def audit(name):
 root=BASE/name;errors=[];exceptions=[];checked=0
 for d in (root/'elements').iterdir():
  seen=collections.defaultdict(list)
  for p in sorted((d/'fixtures').glob('*.html')):
   checked+=1;raw=p.read_text();s=re.sub(r'<!--.*?-->','',raw,flags=re.S).strip();seen[re.sub(r'\s+',' ',s)].append(p.name)
   if p.stem in GOLD.get(d.name,[]):exceptions.append(str(p.relative_to(root)));continue
   q=Parser(name);q.feed(s)
   if len(q.roots)!=1:q.errors.append('Expected exactly one top-level child')
   if q.roots:
    style=q.roots[0][1].get('style','');styles=dict(re.findall(r'(?:^|;)\s*([\w-]+)\s*:\s*([^;]+)',style))
    for key in styles:
     if key not in ['grid-column','grid-row'] and not key.startswith('--'):q.errors.append('Top-level non-grid property '+key)
    for key,expected in [('grid-column','1 / span 12'),('grid-row','1 / span 6')]:
     if re.sub(r'\s+','',styles.get(key,''))!=re.sub(r'\s+','',expected):q.errors.append('Top-level '+key+' must be '+expected)
   for e in q.errors:errors.append({'fixture':str(p.relative_to(root)),'error':e})
  for text,files in seen.items():
   if len(files)>1:errors.append({'element':d.name,'error':'Identical fixture markup and data','fixtures':files})
 return {'collection':name,'fixtures_checked':checked,'golden_fixtures_preserved':len(exceptions),'errors':errors}
reports=[audit(n) for n in (sys.argv[1:] or NAMES)]
Path('/workspace/work/integration/strict-fixture-audit.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2))
for r in reports:
 print(r['collection'],r['fixtures_checked'],len(r['errors']),'errors')
 for e in r['errors'][:20]:print(e)
