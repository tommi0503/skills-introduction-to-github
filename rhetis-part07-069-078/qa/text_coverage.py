from pathlib import Path
from html.parser import HTMLParser
import json,re
class Text(HTMLParser):
 def __init__(self):super().__init__();self.ignore=0;self.data=[]
 def handle_starttag(self,tag,attrs):
  if tag in ['style','script','title']:self.ignore+=1
 def handle_endtag(self,tag):
  if tag in ['style','script','title']:self.ignore=max(0,self.ignore-1)
 def handle_data(self,data):
  if not self.ignore:
   t=re.sub(r'\s+','',data)
   if t:self.data.append(t)
def texts(f):
 p=Text();p.feed(f.read_text());return p.data
base=Path('/workspace/work/rhetis-part07');reports={}
for k in ['vectorbox','seedmark','crossrail','meridian-deck','onboard-docket']:
 p=base/f'{k}-project';out=[]
 for f in sorted((p/'replica').glob('slide*.html')):
  g=p/'reassembled'/f.name
  if not g.exists():continue
  a,b=texts(f),texts(g);joined=''.join(b);missing=[t for t in a if t not in joined and len(t)>1];out.append({'page':f.name,'missingText':missing,'replicaTextN':len(a),'assemblyTextN':len(b),'missingChars':sum(map(len,missing))})
 reports[k]=out
 print(k)
 for x in sorted(out,key=lambda x:x['missingChars'],reverse=True)[:4]:print(x)
(base/'qa/text-coverage.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2))
