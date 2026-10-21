from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib,json
ROOT=Path(__file__).resolve().parent.parent
checks=json.loads((ROOT/'review/final-checks.json').read_text())
assert checks['status']=='passed','Finish review before packaging'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in p.parts for x in ['node_modules','__pycache__','.git']) and p.name!='file-manifest.json')
manifest={str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in files}
(ROOT/'file-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
files.append(ROOT/'file-manifest.json')
zip_path=ROOT.parent/(ROOT.name+'-complete.zip')
with ZipFile(zip_path,'w',ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,ROOT.name+'/'+str(p.relative_to(ROOT)))
with ZipFile(zip_path) as z:assert z.testzip() is None
result={'file':zip_path.name,'bytes':zip_path.stat().st_size,'sha256':sha(zip_path),'entries':len(files),'concepts':6,'designSlides':72,'wireframeSlides':72}
(ROOT.parent/(ROOT.name+'-downloads.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
