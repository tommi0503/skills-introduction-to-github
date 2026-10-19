"""Build full-deck PDF, navigable overview, and 9-up sheets from final renders."""
from pathlib import Path
import json,hashlib,html
from PIL import Image,ImageDraw,ImageFont
import fitz
ROOT=Path(__file__).resolve().parents[1]
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def main():
 manifest=json.loads((ROOT/'build/manifest.json').read_text());rows=[]
 for d in manifest:
  for s in d['slides']:rows.append(dict(deck=d['id'],deckTitle=d['title'],**s))
 (ROOT/'previews').mkdir(exist_ok=True)
 for mode in ['replica','assembly']:
  merged=fitz.open()
  for d in manifest:
   with fitz.open(ROOT/'pdfs'/mode/(d['id']+'.pdf'))as doc:merged.insert_pdf(doc)
  merged.save(ROOT/'pdfs'/(mode+'-all.pdf'),garbage=4,deflate=True);merged.close()
  sheets=[]
  for start in range(0,len(rows),9):
   current=rows[start:start+9];sheet=Image.new('RGB',(1980,1230),'#e9edee');draw=ImageDraw.Draw(sheet);font=ImageFont.truetype(FONT,18)
   draw.text((30,16),f'RHETIS / SPECTRUM BRIEF / {mode.upper()} / {start+1:03d} - {start+len(current):03d}',font=font,fill='#0c2738')
   for i,r in enumerate(current):
    x=30+(i%3)*650;y=62+(i//3)*385;im=Image.open(ROOT/'renders/final'/mode/r['deck']/(r['id']+'.png'));im=im.resize((630,354),Image.Resampling.LANCZOS);sheet.paste(im,(x,y));draw.text((x,y+356),r['deck']+' / '+r['id'],font=font,fill='#365762')
   dest=ROOT/'previews'/mode/f'sheet-{start//9+1:02d}.jpg';dest.parent.mkdir(exist_ok=True);sheet.save(dest,quality=91,optimize=True);sheets.append(dest)
  doc=fitz.open()
  for f in sheets:
   p=doc.new_page(width=990,height=615);p.insert_image(p.rect,filename=str(f))
  doc.save(ROOT/'pdfs'/(mode+'-sheets.pdf'),garbage=4,deflate=True);doc.close()
 # Full preview is a scan-friendly 4-column overview; individual images remain native1280x720.
 overview=Image.new('RGB',(1640,((len(rows)+3)//4)*260+54),'#e9edee');draw=ImageDraw.Draw(overview);font=ImageFont.truetype(FONT,15);draw.text((20,16),'RHETIS SPECTRUM BRIEF / 109 SLIDES / 7 DECKS',font=font,fill='#0c2738')
 for i,r in enumerate(rows):
  x=20+(i%4)*405;y=50+(i//4)*260;im=Image.open(ROOT/'renders/final/replica'/r['deck']/(r['id']+'.png')).resize((390,219),Image.Resampling.LANCZOS);overview.paste(im,(x,y));draw.text((x,y+224),r['deck']+' / '+r['id'],font=font,fill='#365762')
 overview.save(ROOT/'previews/overview.jpg',quality=90)
 data=json.dumps(rows,ensure_ascii=False).replace('</','<\\/')
 template=(ROOT/'tools/gallery-template.html').read_text();(ROOT/'preview.html').write_text(template.replace('__SLIDE_DATA__',data))
 print('Exported',len(rows),'slides; PDF and contact sheets complete')
if __name__=='__main__':main()
