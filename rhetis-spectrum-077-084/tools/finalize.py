from pathlib import Path
import json,html,hashlib,shutil
from PIL import Image,ImageDraw,ImageFont
import fitz
ROOT=Path(__file__).resolve().parents[1]
def make():
 # CSS pixels and PDF points use different units; normalize every exported page to one 1280x720 coordinate system.
 for p in (ROOT/'pdfs').rglob('*.pdf'):
  src=fitz.open(stream=p.read_bytes(),filetype='pdf')
  if any(abs(pg.rect.width-1280)>.01 or abs(pg.rect.height-720)>.01 for pg in src):
   normalized=fitz.open()
   for idx in range(len(src)):
    pg=normalized.new_page(width=1280,height=720);pg.show_pdf_page(pg.rect,src,idx)
   p.write_bytes(normalized.tobytes());normalized.close()
  src.close()
 inv=json.loads((ROOT/'review/inventory.json').read_text());manifest=json.loads((ROOT/'build/manifest.json').read_text());index=ROOT/'preview.html';sections=[]
 preview=ROOT/'previews';preview.mkdir(exist_ok=True)
 font=ImageFont.load_default()
 for mode in ['replica','assembly']:
  pdf=fitz.open()
  for deck in manifest:
   d=fitz.open(ROOT/'pdfs'/mode/(deck['id']+'.pdf'));pdf.insert_pdf(d);d.close()
  pdf.save(ROOT/'pdfs'/f'{mode}-all.pdf');pdf.close()
  sheetpdf=fitz.open();full=Image.new('RGB',(1280,202*((len(inv)+3)//4)), '#e6e8ef');dr=ImageDraw.Draw(full)
  for i,row in enumerate(inv):
   im=Image.open(ROOT/'renders/final'/mode/row['deck']/(row['slide']+'.png')).convert('RGB');x=(i%4)*320;y=(i//4)*202;full.paste(im.resize((320,180)),(x,y+22));dr.text((x+8,y+5),row['deck']+' / '+row['slide'],fill='#19263f')
  full.save(preview/f'{mode}-all.jpg',quality=90)
  for start in range(0,len(inv),12):
   batch=inv[start:start+12];sheet=Image.new('RGB',(1280,606),'#e6e8ef');draw=ImageDraw.Draw(sheet)
   for i,row in enumerate(batch):
    im=Image.open(ROOT/'renders/final'/mode/row['deck']/(row['slide']+'.png')).convert('RGB');x=(i%4)*320;y=(i//4)*202;sheet.paste(im.resize((320,180)),(x,y+22));draw.text((x+8,y+5),row['deck']+' / '+row['slide'],fill='#19263f')
   name=f'{mode}-sheet-{start//12+1:02}.png';sheetpage=Image.new('RGB',(1280,720),'#e6e8ef');sheetpage.paste(sheet,(0,57));sheetpage.save(preview/name);page=sheetpdf.new_page(width=1280,height=720);page.insert_image(fitz.Rect(0,0,1280,720),filename=str(preview/name))
  sheetpdf.save(ROOT/'pdfs'/f'{mode}-sheets.pdf',garbage=4,deflate=True);sheetpdf.close()
 for deck in manifest:
  cards=[]
  for s in deck['slides']:
   id=deck['id'];sid=s['id'];label=f'{id} / {sid} — {s["title"]}';cards.append(f'<article data-deck="{id}"><a class="image" href="build/replica/{id}/{sid}.html"><img loading="lazy" width="640" height="360" src="renders/final/replica/{id}/{sid}.png" alt="{html.escape(label)}"></a><h3>{html.escape(label)}</h3><nav><a href="references/{id}/{sid}.png">원본</a><a href="comparisons/final/replica/{id}/{sid}.jpg">원본·결과 비교</a><a href="build/assembly/{id}/{sid}.html">라이브러리 재조립</a></nav></article>')
  sections.append(f'<section id="deck-{deck["id"]}"><h2>{html.escape(deck["title"])} · {len(deck["slides"])}장</h2><div class="grid">'+''.join(cards)+'</div></section>')
 doc='''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Rhetis Spectrum · 106 slides</title><style>*{box-sizing:border-box}body{font-family:system-ui,sans-serif;background:#eef2f8;color:#172658;margin:0;padding:32px}header{background:#172658;color:white;border-radius:20px;padding:32px;margin-bottom:32px}h1{font-size:36px;margin:0 0 12px}p{line-height:1.7}a{color:#284ab7}header a{color:#c9d9ff}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(460px,1fr));gap:24px}article{background:white;border:1px solid #d1dbee;border-radius:12px;overflow:hidden;padding-bottom:20px}article img{display:block;width:100%;height:auto}article h3,article nav{margin:16px 20px}h2{margin-top:48px}.image{display:block}small{opacity:.8}@media(max-width:600px){body{padding:16px}.grid{grid-template-columns:1fr}}.filter{position:sticky;top:0;background:#eef2f8;padding:16px 0;z-index:5}</style></head><body><header><h1>Rhetis Spectrum</h1><p>5개 덱 · 원본 106장 · 1280×720<br>HTML/CSS·벡터·실제 폰트로 재현하고, Rhetis 컬렉션으로 다시 조립했습니다. 사진·3D·기기 화면·이미지 로고는 회색 placeholder입니다.</p><nav><a href="pdfs/replica-all.pdf">재현본 전체 PDF</a><a href="pdfs/replica-sheets.pdf">재현본 시트 PDF</a><a href="pdfs/assembly-all.pdf">재조립 전체 PDF</a><a href="pdfs/assembly-sheets.pdf">재조립 시트 PDF</a><a href="build/library/light.html">라이브러리 라이트</a><a href="build/library/dark.html">라이브러리 다크</a><a href="review/final-review.md">검수 기록</a></nav></header><nav class="filter">'''
 doc+=''.join(f'<a href="#deck-{d["id"]}">{d["id"]} · {len(d["slides"])}장</a>'for d in manifest)+'</nav>'+''.join(sections)+'</body></html>';index.write_text(doc)
 print('PDFs, contact sheets and preview.html generated')
if __name__=='__main__':make()
