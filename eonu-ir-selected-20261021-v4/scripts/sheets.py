from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from io import BytesIO
import fitz,json,shutil
ROOT=Path(__file__).resolve().parent.parent
font=TTFont(ROOT/'shared/fonts/PretendardVariable.woff2');font.flavor=None
b=BytesIO();font.save(b)
def ft(s):return ImageFont.truetype(BytesIO(b.getvalue()),s)
cat=json.loads((ROOT/'review/slide-manifest.json').read_text());mapping=json.loads((ROOT/'selection.json').read_text())['mapping']
for mode in ['design','wireframe']:
 sheet=Image.new('RGB',(2048,1840),'#f1f3f6');d=ImageDraw.Draw(sheet)
 d.text((40,28),'EONU — '+('DESIGN' if mode=='design' else 'WIREFRAME'),font=ft(36),fill='#202632')
 d.text((40,80),'선택 구성 통합 · 화이트 & 블루 · 12 SLIDES',font=ft(20),fill='#788292')
 for i in range(12):
  x=40+(i%3)*664;y=144+(i//3)*416
  im=Image.open(ROOT/f'concepts/final/previews/{mode}/{i+1:02}.png').convert('RGB').resize((640,360),Image.Resampling.LANCZOS)
  sheet.paste(im,(x,y));d.text((x,y+372),f'{i+1:02}  {cat["topics"][i]}',font=ft(18),fill='#586477');d.text((x+568,y+372),mapping[i].upper(),font=ft(16),fill='#437aff')
 sheet.save(ROOT/f'previews/{mode}-grid.jpg',quality=94)
 shutil.copyfile(ROOT/f'previews/{mode}-grid.jpg',ROOT/f'concepts/final/previews/{mode}-grid.jpg')
 shutil.copyfile(ROOT/f'concepts/final/pdfs/{mode}.pdf',ROOT/f'pdfs/{mode}.pdf')
compare=Image.new('RGB',(2048,5392),'#f1f3f6');d=ImageDraw.Draw(compare)
d.text((40,28),'EONU — DESIGN / WIREFRAME',font=ft(36),fill='#202632')
for i in range(12):
 y=112+i*436
 for j,mode in enumerate(['design','wireframe']):
  x=40+j*1000;im=Image.open(ROOT/f'concepts/final/previews/{mode}/{i+1:02}.png').convert('RGB').resize((960,540),Image.Resampling.LANCZOS)
  im=im.resize((720,405),Image.Resampling.LANCZOS);compare.paste(im,(x,y));d.text((x+736,y+8),f'{i+1:02}',font=ft(32),fill='#437aff');d.text((x+736,y+56),'DESIGN' if j==0 else 'WIREFRAME',font=ft(18),fill='#788292')
compare.save(ROOT/'previews/design-wireframe-grid.jpg',quality=92)
pdfs={mode:fitz.open(ROOT/f'pdfs/{mode}.pdf') for mode in ['design','wireframe']};combined=fitz.open();checks=[]
for mode,doc in pdfs.items():
 assert len(doc)==12
 assert all(len(p.get_text().strip())>20 for p in doc)
 assert all(abs(p.rect.width-960)<1 and abs(p.rect.height-540)<1 for p in doc)
 checks.append({'file':f'pdfs/{mode}.pdf','pages':12,'textExtractable':True,'pagePoints':[960,540]})
for i in range(12):
 for mode in ['design','wireframe']:combined.insert_pdf(pdfs[mode],from_page=i,to_page=i)
combined.save(ROOT/'pdfs/design-wireframe.pdf',garbage=4,deflate=True)
(ROOT/'review/pdf-checks.json').write_text(json.dumps(checks,indent=2))
print('Created 12-slide design/wireframe grids, comparison sheet and vector PDFs (12/12/24 pages).')
