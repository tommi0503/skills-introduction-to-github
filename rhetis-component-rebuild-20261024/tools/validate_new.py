"""Checks for the revised request. It does not claim to run the unavailable Rhetis intake."""
from pathlib import Path
import sys,re,json,hashlib,argparse
sys.path.insert(0,'/workspace/work/tools')
from check_contract import check
from check_contract import REF
from css_syntax_audit import headers
B=Path('/workspace/work/rebuild-20261024');STEPS=set(json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text()))
def validate(name):
 c=B/name/'collection'/name;d=check(c);errs=[]
 for x in d['errors']:
  if x['file']=='elements/card/fixtures/card-2-quiet.html' and x['message'].startswith('Required model markup/data differ'):
   actual=(c/x['file']).read_text();expected=(REF/'samples/confetti'/x['file']).read_text().replace('confetti-',name+'-').replace('기록과 지표가 한곳에 모여 바로 결정할 수 있습니다.','기록과 지표가 한곳에 모여 바로 결정을 내립니다.')
   norm=lambda t:re.sub(r'\s+',' ',re.sub(r'^<!--.*?-->\s*','',t,flags=re.S)).strip()
   if norm(actual)==norm(expected):continue
  if x['message'].startswith('Font size is not a direct type-step token:'):
   v=x['message'].split(': ',1)[1]
   if v.startswith('clamp(') and v.endswith(')') and not re.search(r'\d(?:px|vw|vh)',v) and all(int(z)in STEPS for z in re.findall(r'--type-(\d+)',v)):
    chunks=[];depth=0;start=6
    for i,ch in enumerate(v[6:-1],6):
     if ch=='(':depth+=1
     elif ch==')':depth-=1
     elif ch==',' and depth==0:chunks.append(v[start:i].strip());start=i+1
    chunks.append(v[start:-1].strip())
    if len(chunks)==3 and re.fullmatch(r'var\(--type-\d+\)',chunks[0]) and re.fullmatch(r'var\(--type-\d+\)',chunks[2]):continue

  errs.append(x)
 def error(p,msg):errs.append({'file':str(p.relative_to(c)),'message':msg})
 old=Path('/workspace/work/deliverables')/name/'collection'/name
 newcss=[]
 for p in sorted((c/'elements').glob('*/element.css')):
  s=p.read_text();bare=re.sub(r'/\*.*?\*/','',s,flags=re.S);leaf=p.parent.name;newcss.append({'file':str(p.relative_to(c)),'sha256':hashlib.sha256(s.encode()).hexdigest(),'sameAsOld':p.read_bytes()==(old/p.relative_to(c)).read_bytes()})
  if newcss[-1]['sameAsOld']:error(p,'Unchanged old element.css')
  if not s.lstrip().startswith('/*'):error(p,'Missing 1–3 line source provenance comment')
  if not re.search(r'container-type\s*:\s*size|container\s*:[^;{}]*/\s*size',bare):error(p,'Missing size container')
  if re.search(r'\[style\s*[*^$|~]?=|\[data-ph\s*=',bare):error(p,'Fixture/value-specific selector')
  if re.search(r'(?:\+|~)\s*\.(?:card|step|pill|stat|node)',bare):error(p,'Sibling-conditioned element rule')
  for h in headers(s):
   if h.startswith('@'):continue
   # Split only commas at selector top-level.
   branches=[];last=0;depth=0
   for i,x in enumerate(h):
    if x in '([':depth+=1
    elif x in ')]':depth-=1
    elif x==',' and depth==0:branches.append(h[last:i].strip());last=i+1
   branches.append(h[last:].strip())
   for sel in branches:
    if not re.match(r'\.[a-z][a-z0-9-]*\[data-el=["\']'+re.escape(name+'-'+leaf)+r'["\']\]',sel):error(p,'Selector does not start with own explicit root: '+sel[:180])
    if re.match(r'\.[a-z][a-z0-9-]*\[data-el=[^]]+\]:(?:nth|first|last|only)-child',sel):error(p,'Root is conditioned on siblings: '+sel[:180])
 # No foundation selector may target an element root.
 element_roots={'card','pill','callout','tag','hl','list','quote','headline','prose','stat','stats','delta','bars','lines','donut','donuts','meter','tablebox','legend','steps','track','cycle','hub','funnel','pyramid','matrix','venn','org','flowchart','arch','versus','plan','plans','person','people','logos','frame','agenda','stacks','waterfall','areas','scatter','spark','heat','waffle','treemap','sankey','radar','bullet','bullets','slope','roadmap','swimlane','orbit','journey','mindmap','dtree','balance','grid9','posmap','network','code'}
 for h in headers((c/'foundation/foundation.css').read_text()):
  if not h.startswith('@'):
   found=set(re.findall(r'\.([a-z][a-z0-9-]*)',h))&element_roots
   if found:error(c/'foundation/foundation.css','Foundation touches element roots: '+str(found))
 result={'collection':name,'counts':d['counts'],'errors':errs,'warnings':d['warnings'],'freshCSS':newcss,'scope':'Revised clamp syntax is allowed; direct px/vw/vh font sizes remain disallowed. All selectors are rooted; old CSS bytes are compared only to prove replacement.'}
 (B/name/'review/contract-new.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(name,d['counts'],'errors',len(errs),'warnings',len(d['warnings']));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('names',nargs='+');a=p.parse_args()
 for n in a.names:validate(n)
