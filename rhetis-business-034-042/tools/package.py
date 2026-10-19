"""Package the collection as one top-level folder and the reviewed project separately."""
from pathlib import Path
import zipfile,json,hashlib
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parent

def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
def make():
 c=ROOT/'collection/business-spectrum';libzip=REPO/'business-spectrum.zip'
 with zipfile.ZipFile(libzip,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
  for p in sorted(c.rglob('*')):
   if p.is_file() and 'previews' not in p.relative_to(c).parts:z.write(p,'business-spectrum/'+str(p.relative_to(c)))
 full=REPO/'rhetis-business-034-042-deliverables.zip'
 with zipfile.ZipFile(full,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
  for p in sorted(ROOT.rglob('*')):
   if not p.is_file():continue
   rel=p.relative_to(ROOT);parts=rel.parts
   if '__pycache__'in parts or 'node_modules'in parts or rel.name=='AGENT-API.md':continue
   if parts[0]in ['renders','comparisons'] and len(parts)>1 and parts[1]not in ['final','library']:continue
   if parts[:3]==('collection','business-spectrum','previews'):continue
   if p.suffix=='.pyc':continue
   z.write(p,ROOT.name+'/'+str(rel))
  z.write(libzip,ROOT.name+'/business-spectrum.zip')
 results=[]
 for p in[libzip,full]:
  with zipfile.ZipFile(p)as z:
   bad=z.testzip();names=z.namelist();tops=sorted(set(n.split('/')[0]for n in names));pngs=sum(n.endswith('.png')for n in names)
  if bad:raise RuntimeError(bad)
  if p==libzip and tops!=['business-spectrum']:raise RuntimeError('Collection top-level folder mismatch')
  results.append({'file':p.name,'bytes':p.stat().st_size,'sha256':sha(p),'entries':len(names),'pngFiles':pngs,'topLevel':tops,'crcIntegrity':'passed'})
 manifest={'archives':results};(REPO/'rhetis-business-034-042-downloads.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));print(json.dumps(manifest,ensure_ascii=False,indent=2))
if __name__=='__main__':make()
