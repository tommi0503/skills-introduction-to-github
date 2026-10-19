"""Package final user outputs; exclude scratch, prior rounds and duplicate review screenshots."""
from pathlib import Path
import zipfile,hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1];DEST=ROOT.parent
def archive(name,files,base,top):
 target=DEST/name
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(set(files)):z.write(p,str(Path(top)/p.relative_to(base)))
 with zipfile.ZipFile(target) as z:
  assert z.testzip() is None
  roots={n.split('/')[0] for n in z.namelist()};assert roots=={top}
 return {'file':name,'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'files':len(files),'topLevel':top}
lib=ROOT/'collection/business-prism'
collection=archive('business-prism.zip',[p for p in lib.rglob('*') if p.is_file()],lib,'business-prism')
source=[]
for d in ['src','tools','assets','contract','collection','references']:
 source.extend(p for p in (ROOT/d).rglob('*') if p.is_file() and '__pycache__' not in str(p))
source.extend(ROOT/f for f in ['README.md','package.json','requirements.txt'])
sourceinfo=archive('rhetis-business-061-077-source.zip',source,ROOT,ROOT.name)
delivery=[]
for d in ['renders/final','renders/library','comparisons/final','previews','pdfs','collection']:
 delivery.extend(p for p in (ROOT/d).rglob('*') if p.is_file())
delivery.extend(p for p in (ROOT/'review').iterdir() if p.suffix in ['.md','.json'] and p.name not in ['archives.json','github-download-verification.json'])
delivery.extend([ROOT/'preview.html',ROOT/'README.md'])
deliveryinfo=archive('rhetis-business-061-077-deliverables.zip',delivery,ROOT,ROOT.name)
manifest={'archives':[collection,sourceinfo,deliveryinfo]}
(ROOT/'review/archives.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
