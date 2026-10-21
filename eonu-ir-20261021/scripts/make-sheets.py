from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import fitz, json
ROOT=Path(__file__).resolve().parents[1]
font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font=ImageFont.truetype(font_path,22)
small=ImageFont.truetype(font_path,16)
def sheet(theme):
    cols=3; tw=640; th=360; gap=24; top=105; bottom=28; label=33
    img=Image.new('RGB',(cols*tw+(cols+1)*gap,top+4*(th+label+gap)+bottom),'#ebeaf0')
    d=ImageDraw.Draw(img)
    d.text((gap,25),'EONU / '+('DESIGN DIRECTION' if theme=='design' else 'WIREFRAME'),font=font,fill='#34343b')
    d.text((gap,59),'12 SLIDES  /  1280 x 720  /  2026.10.21',font=small,fill='#777783')
    for i in range(12):
        x=gap+(i%3)*(tw+gap);y=top+(i//3)*(th+label+gap)
        slide=Image.open(ROOT/'previews'/theme/f'{i+1:02}.png').convert('RGB').resize((tw,th),Image.Resampling.LANCZOS)
        img.paste(slide,(x,y));d.text((x,y+th+8),f'{i+1:02} / 12',font=small,fill='#6e6e79')
    img.save(ROOT/'previews'/f'eonu-{theme}-grid.jpg',quality=94)
    return img
a=sheet('wireframe');b=sheet('design')
both=Image.new('RGB',(a.width+b.width+24,max(a.height,b.height)),'#ebeaf0');both.paste(a,(0,0));both.paste(b,(a.width+24,0));both.save(ROOT/'previews'/'eonu-all-24-grid.jpg',quality=94)
pdfs=[]
for theme in ['wireframe','design']:
    p=ROOT/'previews'/f'eonu-{theme}.pdf';doc=fitz.open(p)
    info={'file':p.name,'pages':len(doc),'sizes':[list(page.rect) for page in doc],'textExtracts':[len(page.get_text()) for page in doc]}
    assert len(doc)==12,(p,len(doc))
    assert all(page.rect.width==960 and page.rect.height==540 for page in doc)
    assert all(len(page.get_text())>100 for page in doc)
    pdfs.append(info)
combined=fitz.open()
for theme in ['wireframe','design']:
    with fitz.open(ROOT/'previews'/f'eonu-{theme}.pdf') as doc: combined.insert_pdf(doc)
combined.save(ROOT/'previews'/'eonu-combined-24p.pdf')
(ROOT/'review'/'pdf-check.json').write_text(json.dumps({'status':'passed','pdfs':pdfs,'combinedPages':24},ensure_ascii=False,indent=2))
print('Created 3 grid images, combined PDF, verified 12 + 12 PDF pages and text extraction.')
