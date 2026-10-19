from pathlib import Path
import zipfile,json,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT.parent
archives=[]
def pack(dest,entries):
 with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p,arc in entries:z.write(p,arc)
 with zipfile.ZipFile(dest) as z:
  assert z.testzip() is None
  roots=sorted(set(n.split('/')[0] for n in z.namelist()))
  count=len(z.namelist())
 archives.append({'file':dest.name,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'entries':count,'roots':roots,'crc':'pass'})
c=ROOT/'collection/blueprint-06'
pack(OUT/'blueprint-06.zip',[(p,str(p.relative_to(c.parent))) for p in sorted(c.rglob('*')) if p.is_file() and not p.name.startswith('.')])
entries=[]
for p in sorted(ROOT.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(ROOT);parts=rel.parts
 if any(x in ['__pycache__','.DS_Store','node_modules'] for x in parts):continue
 if parts[0]=='renders' and (len(parts)<2 or parts[1]!='final'):continue
 if parts[0]=='comparisons' and (len(parts)<2 or parts[1]!='final'):continue
 if parts[0]=='review' and any('round' in x or x=='library-render' or x=='library-render-first' or x=='library-render-v1' for x in parts):continue
 entries.append((p,str(Path(ROOT.name)/rel)))
pack(OUT/'rhetis-blueprint-06-delivery.zip',entries)
(OUT/'rhetis-blueprint-06-archives.json').write_text(json.dumps(archives,indent=2));print(json.dumps(archives,indent=2))
