from pathlib import Path
import re,json,zipfile,shutil,hashlib,os,sys,tempfile
from PIL import Image
import fitz
B=Path(__file__).resolve().parents[1];stage=Path(tempfile.mkdtemp(prefix='rhetis-enterprise-package-'));stage.mkdir(exist_ok=True);out=B/'downloads';out.mkdir(exist_ok=True)
collections=sys.argv[1:] or ['rise-block','cinder-pulse','current-fold','scanline-rise','halo-field','corner-signal','anchor-frame']
manifest=json.loads((out/'manifest.json').read_text()) if (out/'manifest.json').exists() else []
manifest=[r for r in manifest if r['collection'] not in collections]
for cid in collections:
 C=B/cid;R=B/(cid+'-review');S=stage/(cid+'-review')
 if not (R/'review-notes.md').exists():print('NOT READY',cid);continue
 if S.exists():shutil.rmtree(S)
 shutil.copytree(R,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc'));runtime=S/'runtime';runtime.mkdir(exist_ok=True);shutil.copytree(C,runtime/cid);shutil.copytree(B/'fonts',runtime/'fonts')
 issues=[]
 for f in sorted(R.rglob('*')):
  if f.suffix not in ['.html','.css'] or not f.is_file():continue
  dest=S/f.relative_to(R);s=f.read_text()
  def local(url):
   url=url.strip()
   if url.startswith(('data:','#','https://')):return url
   if url.startswith('http://127.0.0.1:8765/'):target=B/url.split(':8765/',1)[1]
   elif url.startswith('file://'):target=Path(url[7:])
   elif url.startswith('http://'):return url
   else:target=(f.parent/url).resolve()
   if '/workspace/work/ref/fonts/' in str(target):target=B/'fonts'/str(target).split('/fonts/',1)[1]
   if not target.exists():issues.append({'source':str(f.relative_to(R)),'url':url});return url
   if target.is_relative_to(R):new=S/target.relative_to(R)
   elif target.is_relative_to(C):new=runtime/cid/target.relative_to(C)
   elif target.is_relative_to(B/'fonts'):new=runtime/'fonts'/target.relative_to(B/'fonts')
   else:
    # Unusual local runtime dependencies are copied explicitly, never the workspace root.
    new=runtime/'extra'/target.name;new.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,new)
   return os.path.relpath(new,dest.parent)
  s=''.join(chunk if chunk.lower().startswith('<script') else re.sub(r'(href|src)=["\']([^"\']+)["\']',lambda m:m[1]+'="'+local(m[2])+'"',chunk) for chunk in re.split(r'(<script\b[^>]*>.*?</script>)',s,flags=re.S|re.I))
  s=re.sub(r'url\(["\']?([^\)"\']+)["\']?\)',lambda m:'url("'+local(m[1])+'")',s)
  dest.write_text(s)
 # Zip collection has exactly one top-level folder and only contract file types.
 for kind,root,zname,base in [('collection',C,cid+'.zip',C.parent),('review',S,cid+'-review.zip',S)]:
  files=sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
  if kind=='collection':assert all(p.suffix in ['.css','.json','.md','.html'] for p in files)
  zpath=out/zname
  with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
   for f in files:z.write(f,f.relative_to(base))
  with zipfile.ZipFile(zpath) as z:assert z.testzip() is None
  manifest.append({'collection':cid,'kind':kind,'file':zname,'bytes':zpath.stat().st_size,'sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),'files':len(files),'portable_missing_dependencies':issues})
 print(cid,'packaged',len(issues),'missing dependencies')
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));print('Archives',len(manifest))
