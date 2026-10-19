from pathlib import Path
import json,math,io
from PIL import Image,ImageDraw,ImageFont
import fitz
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'build/manifest.json').read_text());font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15);small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
for mode in ['replica','assembly']:
 doc=fitz.open();sheets=fitz.open();sheetpaths=[]
 for d in manifest:
  with fitz.open(ROOT/'pdfs'/mode/(d['id']+'.pdf')) as src:doc.insert_pdf(src)
  ids=[s['id'] for s in d['slides']]
  for off in range(0,len(ids),12):
   im=Image.new('RGB',(1280,720),'#e9edf5');dr=ImageDraw.Draw(im);dr.text((22,15),f'BLUEPRINT 06 / {mode.upper()} / DECK {d["id"]} / SHEET {off//12+1}',font=font,fill='#20315a')
   for i,sid in enumerate(ids[off:off+12]):
    x=22+(i%4)*315;y=56+(i//4)*218;thumb=Image.open(ROOT/'renders/final'/mode/d['id']/(sid+'.png')).convert('RGB').resize((291,164),Image.Resampling.LANCZOS);im.paste(thumb,(x,y));dr.text((x,y+172),d['id']+' / '+sid,font=small,fill='#35476e')
   out=ROOT/'sheets'/mode/f'{d["id"]}-{off//12+1:02}.png';out.parent.mkdir(parents=True,exist_ok=True);im.save(out);sheetpaths.append(out)
   pg=sheets.new_page(width=1280,height=720);raw=io.BytesIO();im.save(raw,format='JPEG',quality=94);pg.insert_image(pg.rect,stream=raw.getvalue())
 doc.save(ROOT/'pdfs'/(mode+'-all.pdf'),garbage=4,deflate=True);doc.close();sheets.save(ROOT/'pdfs'/(mode+'-sheets.pdf'),garbage=4,deflate=True);sheets.close()
 # Entire deck list in a compact JPG overview; original page dimensions are preserved in PNGs.
 w=1280;h=math.ceil(len(sheetpaths)/2)*420;overview=Image.new('RGB',(w,h),'#e9edf5');dr=ImageDraw.Draw(overview)
 for i,p in enumerate(sheetpaths):
  x=20+(i%2)*630;y=(i//2)*420+16;dr.text((x,y),f'{mode.upper()} / DECK-SHEET {p.stem}',font=font,fill='#20315a');thumb=Image.open(p).resize((610,343),Image.Resampling.LANCZOS);overview.paste(thumb,(x,y+30))
 overview.save(ROOT/(mode+'-overview.jpg'),quality=92)
print('Merged115-page PDFs and12-sheet PDFs per version; PNG sheets1280x720')
