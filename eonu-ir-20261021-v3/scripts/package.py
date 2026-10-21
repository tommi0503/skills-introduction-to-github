from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT.parent/(ROOT.name+'-complete.zip')
def eligible(p):
    rel=p.relative_to(ROOT)
    return p.is_file() and not any(x in ('node_modules','__pycache__','.git') for x in rel.parts) and p.name!='.DS_Store'
files=sorted(p for p in ROOT.rglob('*') if eligible(p) and p.name!='file-manifest.json')
manifest={str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files}
(ROOT/'review'/'file-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
files=sorted(p for p in ROOT.rglob('*') if eligible(p))
with zipfile.ZipFile(ARCHIVE,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,arcname=ROOT.name+'/'+str(p.relative_to(ROOT)))
with zipfile.ZipFile(ARCHIVE) as z:
    assert z.testzip() is None
    for name,info in manifest.items():assert hashlib.sha256(z.read(ROOT.name+'/'+name)).hexdigest()==info['sha256']
record={'archive':ARCHIVE.name,'bytes':ARCHIVE.stat().st_size,'sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'files':len(files),'internalManifest':'review/file-manifest.json','crcCheck':'passed','perFileHashes':'passed'}
(ROOT.parent/(ROOT.name+'-downloads.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,indent=2))
