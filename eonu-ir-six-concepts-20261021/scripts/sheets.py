from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from io import BytesIO
import json, fitz

ROOT=Path(__file__).resolve().parent.parent
font=TTFont(ROOT/'shared/fonts/PretendardVariable.woff2');font.flavor=None
buf=BytesIO();font.save(buf)
def ft(size):return ImageFont.truetype(BytesIO(buf.getvalue()),size=size)
catalog=json.loads((ROOT/'review/slide-manifest.json').read_text())
colors={c['id']:c['accent'] for c in catalog['concepts']}
for c in catalog['concepts']:
 for mode in ['design','wireframe']:
  W=2048;pad=40;gap=24;cw=640;ch=360;rowh=416
  sheet=Image.new('RGB',(W,1840),'#f1f2f4');d=ImageDraw.Draw(sheet)
  d.text((40,32),f"{c['id'].upper()}  {c['name']}",font=ft(36),fill='#202630')
  d.text((40,84),'EONU · 12 SLIDES · '+('DESIGN' if mode=='design' else 'WIREFRAME'),font=ft(20),fill='#737b88')
  for i in range(12):
   x=pad+(i%3)*(cw+gap);y=144+(i//3)*rowh
   im=Image.open(ROOT/f"concepts/{c['id']}/previews/{mode}/{i+1:02}.png").convert('RGB');im=im.resize((cw,ch),Image.Resampling.LANCZOS)
   sheet.paste(im,(x,y));d.text((x,y+372),f"{i+1:02}  {catalog['topics'][i]}",font=ft(18),fill='#424b58')
  sheet.save(ROOT/f"concepts/{c['id']}/previews/{mode}-grid.jpg",quality=92)

for mode in ['design','wireframe']:
 cw,ch,gap,pad=480,270,24,32;W=pad*2+cw*6+gap*5;H=168+12*(ch+56)+32
 sheet=Image.new('RGB',(W,H),'#eef0f3');d=ImageDraw.Draw(sheet)
 d.text((pad,24),'EONU — SIX DESIGN DIRECTIONS',font=ft(32),fill='#25303d')
 d.text((pad,68),'동일한 12장의 이야기 · 6개의 시각 언어 · '+('디자인 시안' if mode=='design' else '와이어프레임'),font=ft(20),fill='#6e7784')
 for j,c in enumerate(catalog['concepts']):
  x=pad+j*(cw+gap);d.text((x,120),c['id'].upper()+'  '+c['name'],font=ft(24),fill=colors[c['id']])
  for i in range(12):
   y=168+i*(ch+56);im=Image.open(ROOT/f"concepts/{c['id']}/previews/{mode}/{i+1:02}.png").convert('RGB').resize((cw,ch),Image.Resampling.LANCZOS);sheet.paste(im,(x,y));d.text((x,y+282),f"{i+1:02}  {catalog['topics'][i]}",font=ft(16),fill='#697484')
 sheet.save(ROOT/f"previews/all-{'designs' if mode=='design' else 'wireframes'}-grid.jpg",quality=92)

cover=Image.new('RGB',(2000,1000),'#eef0f3');d=ImageDraw.Draw(cover)
d.text((36,24),'EONU — 6개 디자인 시안',font=ft(32),fill='#25303d')
for j,c in enumerate(catalog['concepts']):
 x=36+j%3*656;y=100+j//3*440;im=Image.open(ROOT/f"concepts/{c['id']}/previews/design/01.png").convert('RGB').resize((624,351),Image.Resampling.LANCZOS);cover.paste(im,(x,y));d.text((x,y+368),c['id'].upper()+'  '+c['name'],font=ft(24),fill=colors[c['id']])
cover.save(ROOT/'previews/six-covers.jpg',quality=94)

pdfchecks=[]
for mode in ['design','wireframe']:
 combined=fitz.open()
 for c in catalog['concepts']:
  p=ROOT/f"concepts/{c['id']}/pdfs/{mode}.pdf";doc=fitz.open(p)
  assert len(doc)==12,(str(p),len(doc))
  assert all(abs(page.rect.width-960)<1 and abs(page.rect.height-540)<1 for page in doc)
  assert all(len(page.get_text().strip())>20 for page in doc),'PDF text missing'
  pdfchecks.append({'file':str(p.relative_to(ROOT)),'pages':len(doc),'textExtractable':True,'pagePoints':[960,540]})
  combined.insert_pdf(doc);doc.close()
 combined.set_metadata({'title':'EONU — six concepts — '+mode,'author':'EONU','subject':'Six alternative 12-slide IR decks'})
 combined.save(ROOT/f'pdfs/all-{mode}.pdf',garbage=4,deflate=True);combined.close()
(ROOT/'review/pdf-checks.json').write_text(json.dumps(pdfchecks,indent=2))
print('14 grid images, 2 combined 72-page PDFs; all 12 individual PDFs validated.')
