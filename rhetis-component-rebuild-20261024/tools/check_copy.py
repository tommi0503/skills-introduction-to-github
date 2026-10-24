"""Detect any six-character phrase copied from any frozen replica into a fixture."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,unicodedata,argparse
B=Path('/workspace/work/rebuild-20261024');O=Path('/workspace/work/deliverables')
class Text(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.parts=[]
 def handle_starttag(self,t,a):
  if t in ['script','style','title']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style','title']:self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip and s.strip():self.parts.append(s.strip())
def parts(p):
 d=Text();d.feed(p.read_text());return d.parts
def norm(s):return re.sub(r'[^\w가-힣]','',unicodedata.normalize('NFKC',s).lower())
def audit(name):
 source={}
 for n in ['nocturne','inflexion','diecut','afterglow','dockside','confluence']:
  for p in (O/n/'review/replica').glob('*.html'):
   for s in parts(p):
    z=norm(s)
    for i in range(len(z)-5):source.setdefault(z[i:i+6],{'collection':n,'page':p.stem,'sourceText':s[:180]})
 hits=[];files=0
 for p in sorted((B/name/'collection'/name/'elements').glob('*/fixtures/*.html')):
  files+=1
  for s in parts(p):
   z=norm(s);matches=list(dict.fromkeys(z[i:i+6] for i in range(len(z)-5) if z[i:i+6] in source))
   if matches:hits.append({'file':str(p.relative_to(B/name/'collection'/name)),'fixtureText':s,'matches':[{'phrase':a,**source[a]}for a in matches[:8]]})
 result={'collection':name,'fixturesChecked':files,'collisions':hits,'method':'NFKC/lowercase; punctuation and whitespace removed; contiguous six-character windows within each visible text node. The source corpus combines all six frozen replicas.'};(B/name/'review/copy-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(name,files,'fixtures','collisions',len(hits));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('names',nargs='+');a=p.parse_args()
 for n in a.names:audit(n)
