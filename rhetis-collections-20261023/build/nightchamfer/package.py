from pathlib import Path
from PIL import Image
import json,zipfile,hashlib,collections,shutil,fitz
O=Path('/workspace/output');C=O/'nightchamfer';R=O/'nightchamfer-review'
assert len(list((C/'elements').iterdir()))==56
assert {p.suffix for p in C.rglob('*')if p.is_file()}<={'.css','.json','.md','.html'}
imgs=[]
for p in sorted(R.rglob('*.png')):
 with Image.open(p)as im:size=im.size
 expected=(2560,720)if p.parent.name in ['compare-replica','compare-reassembled']else(1280,720)
 assert size==expected,(str(p),size)
 imgs.append({'file':str(p.relative_to(R)),'width':size[0],'height':size[1]})
assert len(list((R/'replica').glob('slide_*.png')))==18
assert len(list((R/'reassembled').glob('slide_*.png')))==18
for n in (C/'elements').iterdir():
 for mode in ['light','dark']:assert (R/'library/elements'/n.name/f'{mode}.png').exists()
pdf_counts={}
for f,expected_pages in [('replica/replica.pdf',18),('reassembled/reassembled.pdf',18),('library/library-light.pdf',172),('library/library-dark.pdf',172)]:
 assert(R/f).stat().st_size>1000
 with fitz.open(R/f)as doc:
  assert len(doc)==expected_pages,(f,len(doc));pdf_counts[f]=len(doc)
  assert all(abs(page.rect.width-1280)<.1 and abs(page.rect.height-720)<.1 for page in doc)

summary={'collection':'nightchamfer','build':'success','elements':56,'element_fixtures':len(list(C.glob('elements/*/fixtures/*.html'))),'foundation_fixtures':len(list(C.glob('foundation/fixtures/*.html'))),'source_images':18,'replica_pages':18,'reassembled_pages':18,'element_sheet_pngs':112,'png_count':len(imgs),'png_sizes':dict(collections.Counter(f"{i['width']}x{i['height']}"for i in imgs)),'pngs':imgs,'pdf_pages':pdf_counts,'collection_source_sha256':{str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(C.rglob('*'))if p.is_file()}}
(R/'build-verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
for name in ['nightchamfer','nightchamfer-review']:
 src=O/name;target=O/f'{name}.zip'
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
  for p in sorted(src.rglob('*')):
   if p.is_file():z.write(p,str(p.relative_to(O)))
 with zipfile.ZipFile(target)as z:assert z.testzip()is None;assert {n.split('/')[0]for n in z.namelist()}=={name}
 print(target.name,target.stat().st_size,hashlib.sha256(target.read_bytes()).hexdigest())
print('PNGs',len(imgs),summary['png_sizes'])
