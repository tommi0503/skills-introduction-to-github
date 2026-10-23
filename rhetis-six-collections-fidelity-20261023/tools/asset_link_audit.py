"""Validate that the required standalone review sources resolve inside the review ZIP."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,json,argparse
def audit(root):
 errors=[];external=[];checked=0
 paths=[]
 for directory in ['replica','reassembled','library','assets']:
  paths.extend(p for p in (root/directory).rglob('*') if p.suffix in {'.html','.css'})
 if (root/'index.html').exists():paths.append(root/'index.html')
 for p in paths:
  text=p.read_text();urls=re.findall(r'''(?:src|href)\s*=\s*["']([^"']+)["']''',text) if p.suffix=='.html' else []
  urls+=re.findall(r'''url\(\s*["']?([^"')]+)["']?\s*\)''',text)
  for value in urls:
   if value.startswith(('#','data:','mailto:','tel:','javascript:')):continue
   url=urlsplit(value)
   if url.scheme or url.netloc:
    external.append({'file':str(p.relative_to(root)),'url':value});continue
   target=(p.parent/unquote(url.path)).resolve();checked+=1
   if not target.is_relative_to(root.resolve()):errors.append({'file':str(p.relative_to(root)),'url':value,'reason':'outside standalone review'})
   elif not target.exists():errors.append({'file':str(p.relative_to(root)),'url':value,'reason':'missing'})
 return {'checked':checked,'errors':errors,'external':external}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('root');p.add_argument('--out');a=p.parse_args();r=audit(Path(a.root).resolve())
 if a.out:Path(a.out).write_text(json.dumps(r,ensure_ascii=False,indent=2))
 print(json.dumps(r,ensure_ascii=False))
