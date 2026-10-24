"""Additional six-character check across inline emphasis within the same semantic text block."""
from pathlib import Path
from html.parser import HTMLParser
import re,json,sys,unicodedata
B=Path('/workspace/work/rebuild-20261024');O=Path('/workspace/work/deliverables');NAMES=['nocturne','inflexion','diecut','afterglow','dockside','confluence']
class Blocks(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.stack=[];self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['style','script','title']:self.skip+=1
  if t in ['meta','link','br','hr','img','input']:return
  cls=set(dict(a).get('class','').split());block=t in ['p','h1','h2','h3','h4','li']or bool(cls&{'name','note','title','lead','kicker','bodycopy','heading','fig','kick'})
  if block:
   for x in self.stack:
    if x['block']:x['childBlock']=True
  self.stack.append({'tag':t,'block':block,'childBlock':False,'text':[]})
 def handle_endtag(self,t):
  if t in ['style','script','title']:self.skip=max(0,self.skip-1)
  if not self.stack:return
  match=next((i for i in range(len(self.stack)-1,-1,-1)if self.stack[i]['tag']==t),None)
  if match is None:return
  popped=self.stack[match:];self.stack=self.stack[:match]
  for x in popped:
   if x['block']and not x['childBlock']and ''.join(x['text']).strip():self.parts.append(''.join(x['text']).strip())
 def handle_data(self,s):
  if self.skip:return
  for x in self.stack:x['text'].append(s)
def blocks(p):
 d=Blocks();d.feed(p.read_text());return d.parts
def norm(s):return re.sub(r'[^\w가-힣]','',unicodedata.normalize('NFKC',s).lower())
src={}
for n in NAMES:
 for p in (O/n/'review/replica').glob('*.html'):
  for s in blocks(p):
   z=norm(s)
   for k in range(len(z)-5):src.setdefault(z[k:k+6],{'collection':n,'page':p.stem,'text':s})
for n in sys.argv[1:]:
 hits=[];fixtures=list((B/n/'collection'/n/'elements').glob('*/fixtures/*.html'))
 for p in fixtures:
  for s in blocks(p):
   z=norm(s);ks=list(dict.fromkeys(z[k:k+6]for k in range(len(z)-5)if z[k:k+6]in src))
   if ks:hits.append({'file':str(p.relative_to(B/n/'collection'/n)),'text':s,'matches':[{'phrase':k,**src[k]}for k in ks[:5]]})
 (B/n/'review/copy-block-audit.json').write_text(json.dumps({'collection':n,'fixtures':len(fixtures),'collisions':hits,'method':'Semantic paragraph/heading/name/note blocks; inline emphasis is concatenated, separate chart labels and fields are not.'},ensure_ascii=False,indent=2));print(n,'block collisions',len(hits))
