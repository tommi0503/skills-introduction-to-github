from pathlib import Path
from html.parser import HTMLParser
import re,json
BASE=Path('/workspace/output');NAMES=['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse']
class Node:
 def __init__(self,tag='',attrs=(),parent=None):self.tag=tag;self.attrs=dict(attrs);self.parent=parent;self.children=[];self.text=''
 def cls(self,c):return c in self.attrs.get('class','').split()
 def var(self,n):
  m=re.search(re.escape('--'+n)+r'\s*:\s*([-+.\d]+)',self.attrs.get('style',''));return float(m[1]) if m else None
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.root=Node();self.cur=self.root
 def handle_starttag(self,tag,attrs):
  node=Node(tag,attrs,self.cur);self.cur.children.append(node)
  if tag not in ['img','br','hr','input','meta','link','source','wbr']:self.cur=node
 def handle_endtag(self,tag):
  cur=self.cur
  while cur.parent is not None:
   if cur.tag==tag:self.cur=cur.parent;return
   cur=cur.parent
 def handle_data(self,data):self.cur.text+=data

def walk(node):
 yield node
 for c in node.children:yield from walk(c)
records=[]
for name in NAMES:
 issues=[];checked=0
 for kind in ['chart-waterfall','sankey','chart-stack']:
  for file in (BASE/name/'elements'/kind/'fixtures').glob('*.html'):
   p=Parser();p.feed(file.read_text());checked+=1
   if kind=='chart-waterfall':
    moves=[n for n in walk(p.root) if n.cls('move')];last=None
    for i,node in enumerate(moves):
     a,b=node.var('from'),node.var('to')
     if a is None or b is None:continue
     if i and node.cls('total') and last is not None and abs(b-last)>.01:issues.append({'fixture':str(file.relative_to(BASE/name)),'type':'waterfall total differs from preceding cumulative value','from_previous':last,'total':b})
     elif i and not node.cls('total') and last is not None and abs(a-last)>.01:issues.append({'fixture':str(file.relative_to(BASE/name)),'type':'waterfall cumulative discontinuity','from_previous':last,'from':a})
     label=next((c.text for c in node.children if c.tag=='b'),'');m=re.search(r'[-+]?\d[\d,.]*',label)
     if m:
      num=float(m[0].replace(',',''));expect=b if node.cls('total') else b-a
      if abs(num-expect)>.01:issues.append({'fixture':str(file.relative_to(BASE/name)),'type':'waterfall label differs from coordinates','label':num,'computed':expect})
     last=b
   if kind=='sankey':
    for node in walk(p.root):
     branches=[c for c in node.children if c.cls('branch')]
     if branches:
      vals=[b.var('v') for b in branches]
      if all(v is not None for v in vals) and abs(sum(vals)-100)>.01:issues.append({'fixture':str(file.relative_to(BASE/name)),'type':'sankey shares do not sum to 100','shares':vals})
 records.append({'collection':name,'fixtures_checked':checked,'issues':issues})
Path('/workspace/work/integration/data-audit.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
for r in records:print(r['collection'],r['fixtures_checked'],len(r['issues']),'data issues')
