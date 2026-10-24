from pathlib import Path
from html.parser import HTMLParser
import re,json,argparse,unicodedata
ROOT=Path('/workspace/work/rebuild');SRC=Path('/workspace/work/delivery')
class Text(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.parts=[]
 def handle_starttag(self,t,a):
  if t in ['script','style','head']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style','head'] and self.skip:self.skip-=1
 def handle_data(self,s):
  if not self.skip and s.strip():self.parts.append(s)
def text(s):
 p=Text();p.feed(s);return p.parts
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKC',s).lower() if c.isalnum())
source={}
for f in SRC.glob('*/review/replica/slide_*.html'):
 for p in text(f.read_text()):
  s=norm(p)
  for i in range(max(0,len(s)-5)):
   key=s[i:i+6]
   if not key.isdigit():source.setdefault(key,[]).append(str(f.relative_to(SRC)))
a=argparse.ArgumentParser();a.add_argument('collection');a.add_argument('--leaf');v=a.parse_args();C=ROOT/v.collection/v.collection
fs=list((C/'elements'/v.leaf/'fixtures').glob('*.html')) if v.leaf else list(C.glob('elements/*/fixtures/*.html'))+list(C.glob('foundation/fixtures/*.html'));hits=[]
for f in fs:
 for p in text(f.read_text()):
  s=norm(p);keys={s[i:i+6] for i in range(max(0,len(s)-5)) if s[i:i+6] in source}
  company=bool(re.search(r'mirimedi|agency\s*miri|miri\s*company|미리컴퍼니|강미리|김미리',p,re.I))
  if keys or company:hits.append({'file':str(f.relative_to(C)),'text':p,'fragments':sorted(keys),'source':{k:sorted(set(source[k]))[:3] for k in sorted(keys)},'source_company':company})
out=ROOT/v.collection/'review/validation';out.mkdir(parents=True,exist_ok=True);dest=out/((v.leaf+'-' if v.leaf else '')+'copy-audit.json');dest.write_text(json.dumps({'fixtures':len(fs),'matches':hits},ensure_ascii=False,indent=2));print(v.collection,v.leaf or'all','fixtures',len(fs),'matched_fragments',sum(len(x['fragments']) for x in hits),'records',len(hits));print(json.dumps(hits[:12],ensure_ascii=False,indent=2))
