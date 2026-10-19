from pathlib import Path
from PIL import Image,ImageDraw
import fitz,json,hashlib,math
P=Path(__file__).resolve().parents[1];A=P/'artifacts';(A/'sheets').mkdir(exist_ok=True)
# Export each deck and combined deck as native 1280×720 PDF pages, preserving vectors/text.
for mode in ['direct','assembled']:
 allpdf=fitz.open()
 for d in ['048','049','050','051','052','053']:
  file=A/mode/f'{d}.pdf';src=fitz.open(file);doc=fitz.open()
  for i in range(len(src)):
   page=doc.new_page(width=1280,height=720);page.show_pdf_page(page.rect,src,i)
  data=doc.tobytes(garbage=4,deflate=True);doc.close();src.close();file.write_bytes(data);doc=fitz.open(file);allpdf.insert_pdf(doc);doc.close()
  files=sorted((A/mode/d).glob('*.png'));canvas=Image.new('RGB',(1280,720),'#e9edf4');dr=ImageDraw.Draw(canvas);dr.text((24,15),f'{d} / {mode.upper()} / {len(files)} slides',fill='#22344b')
  cols=5;tw=232;th=130;gap=16
  for i,f in enumerate(files):
   im=Image.open(f);im.thumbnail((tw,th),Image.Resampling.LANCZOS);x=24+(i%cols)*(tw+gap);y=48+(i//cols)*132;canvas.paste(im,(x,y));dr.text((x+4,y+3),f.stem,fill='#69788e')
  canvas.save(A/'sheets'/f'{mode}-{d}.png')
 allpdf.save(A/f'{mode}-all-105.pdf',garbage=4,deflate=True);allpdf.close()
 sheet=fitz.open()
 for f in sorted((A/'sheets').glob(mode+'-*.png')):
  page=sheet.new_page(width=1280,height=720);page.insert_image(page.rect,filename=f)
 sheet.save(A/f'{mode}-contact-sheets.pdf',garbage=4,deflate=True);sheet.close()
# Library fixture sheets are also exactly 1280×720, one rendered fixture per page.
for mode in ['light','dark']:
 doc=fitz.open()
 for f in sorted((A/'library').glob(mode+'-*.png')):
  page=doc.new_page(width=1280,height=720);page.insert_image(page.rect,filename=f)
 doc.save(A/'library'/f'{mode}-sheet-native.pdf',garbage=4,deflate=True);doc.close()
 # The raw preview tool's paginated browser print is superseded by the native-page export.
 (A/'library'/f'{mode}-sheet.pdf').unlink(missing_ok=True)
# Overview contains all slides; use JPG so every delivered PNG remains native size.
images=[Image.open(A/'sheets'/f'direct-{d}.png') for d in ['048','049','050','051','052','053']];allim=Image.new('RGB',(1280,4320))
for i,im in enumerate(images):allim.paste(im,(0,i*720))
allim.save(A/'all-slides-preview.jpg',quality=90)
print('Exported native PDFs, 12 contact PNGs and overview')
