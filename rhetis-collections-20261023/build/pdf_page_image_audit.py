"""Verify that each replica/reassembled PDF embeds the final page PNG pixels."""
from pathlib import Path
import json,sys,fitz,hashlib
from PIL import Image
BASE=Path('/workspace/output');WORK=Path('/workspace/work/integration')
names=sys.argv[1:] or ['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse'];records=[]
for name in names:
 errors=[];checks=[]
 for kind in ['replica','reassembled']:
  root=BASE/(name+'-review')/kind;pngs=sorted(root.glob('slide*.png'));doc=fitz.open(root/(kind+'.pdf'))
  if len(doc)!=len(pngs):errors.append(kind+' PDF page count differs from PNG count')
  for i,png in enumerate(pngs):
   if i>=len(doc):continue
   refs=doc.get_page_images(i)
   if len(refs)!=1:errors.append(f'{kind}/{i+1} expected one embedded slide image, found {len(refs)}');continue
   pix=fitz.Pixmap(doc,refs[0][0]);im=Image.frombytes('RGB' if pix.n==3 else 'RGBA',(pix.width,pix.height),pix.samples).convert('RGB')
   with Image.open(png) as original:expected=original.convert('RGB');same=im.size==expected.size and im.tobytes()==expected.tobytes()
   if not same:errors.append(f'{kind}/{png.name} embedded PDF pixels differ from final PNG')
   checks.append({'kind':kind,'page':i+1,'png':png.name,'pixels_match':same})
  doc.close()
 records.append({'collection':name,'errors':errors,'checks':checks});print(name,len(checks),'PDF page images',len(errors),'errors')
(WORK/'pdf-page-image-audit.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
