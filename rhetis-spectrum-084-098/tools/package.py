"""Create deterministic deliverables and verify archive CRC, PNGs and checksums."""
from pathlib import Path
import hashlib,json,zipfile,io
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parent
OUTPUT=Path('/codex/browser/projectless/0022-files-mentioned-by-the-user-uploaded-file-pointe/output')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def include(p):
 rel=p.relative_to(ROOT);parts=rel.parts
 if '__pycache__'in parts or p.suffix=='.pyc':return False
 if parts[0]in ['renders','comparisons']and parts[1]!='final':return False
 # Assembly is checked against the replica pixel-by-pixel; avoid duplicating comparisons.
 if parts[:3]==('comparisons','final','assembly'):return False
 # Combined PDFs contain the same 109 vector pages; per-deck duplicates stay in source.
 if parts[0]=='pdfs'and len(parts)>2:return False
 return True
def pack(path,files):
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
  for p,name in files:z.write(p,name)
 with zipfile.ZipFile(path)as z:
  assert z.testzip()is None
  names=z.namelist();pngs=[];dimensions={}
  for n in names:
   if n.endswith('.png'):
    with Image.open(io.BytesIO(z.read(n)))as im:key=str(im.size[0])+'x'+str(im.size[1]);dimensions[key]=dimensions.get(key,0)+1
   if '/renders/final/'in n and n.endswith('.png'):
    with Image.open(io.BytesIO(z.read(n)))as im:assert im.size==(1280,720);pngs.append(n)
  return {'file':path.name,'bytes':path.stat().st_size,'sha256':sha(path),'entries':len(names),'topLevel':sorted({n.split('/')[0]for n in names}),'finalSlidePngs':len(pngs),'allPngDimensions':dimensions,'crcIntegrity':'passed'}
def main():
 final=json.loads((ROOT/'review/final-verification.json').read_text());assert final['success'],'Run verify first'
 c=ROOT/'collection/spectrum-brief';lib=REPO/'spectrum-brief.zip';delivery=REPO/'rhetis-spectrum-084-098-deliverables.zip'
 reports=[pack(lib,[(p,'spectrum-brief/'+str(p.relative_to(c)))for p in sorted(c.rglob('*'))if p.is_file()])]
 assert reports[0]['topLevel']==['spectrum-brief']
 fs=[(p,ROOT.name+'/'+str(p.relative_to(ROOT)))for p in sorted(ROOT.rglob('*'))if p.is_file()and include(p)]
 fs.append((lib,ROOT.name+'/spectrum-brief.zip'));reports.append(pack(delivery,fs))
 assert reports[1]['finalSlidePngs']==218
 if delivery.stat().st_size>99_000_000:raise RuntimeError('GitHub file limit: partition complete deliverable before uploading')
 out={'archives':reports};(REPO/'rhetis-spectrum-084-098-downloads.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
 import shutil
 try:
  OUTPUT.mkdir(parents=True,exist_ok=True)
  for p in [lib,delivery,REPO/'rhetis-spectrum-084-098-downloads.json']:shutil.copy2(p,OUTPUT/p.name)
  shutil.copy2(ROOT/'previews/overview.jpg',OUTPUT/'rhetis-spectrum-084-098-overview.jpg')
  for name in ['replica-all.pdf','assembly-all.pdf','replica-sheets.pdf','assembly-sheets.pdf']:shutil.copy2(ROOT/'pdfs'/name,OUTPUT/name)
 except OSError as e:
  print('Optional application output directory unavailable; verified deliverables remain in repository:',e)
 print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
