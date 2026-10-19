"""Create every final contact sheet, searchable deck PDF merge and offline gallery."""
from pathlib import Path
from PIL import Image,ImageDraw
import fitz,json,html,math
ROOT=Path(__file__).resolve().parents[1]
inventory=json.loads((ROOT/'review/reference-inventory.json').read_text())
for mode in ['replica','assembly']:
 files=sorted((ROOT/'renders/final'/mode).glob('*/*.png'))
 out=ROOT/'previews'/mode;out.mkdir(parents=True,exist_ok=True)
 pages=[]
 for offset in range(0,len(files),9):
  sheet=Image.new('RGB',(1280,720),'#e9edf2');d=ImageDraw.Draw(sheet)
  for i,p in enumerate(files[offset:offset+9]):
   im=Image.open(p).convert('RGB');im.thumbnail((410,231))
   x=10+(i%3)*424;y=4+(i//3)*240
   sheet.paste(im,(x,y));d.text((x+4,y+231),p.parent.name+' / '+p.stem,fill='#27354b')
  target=out/f'sheet-{offset//9+1:02}.png';sheet.save(target);pages.append(target)
 # Full preview is deliberately a contact image, not an individual slide output.
 full=Image.new('RGB',(1600,math.ceil(len(files)/4)*244),'#e9edf2');d=ImageDraw.Draw(full)
 for i,p in enumerate(files):
  im=Image.open(p).convert('RGB');im.thumbnail((392,221));x=4+(i%4)*400;y=4+(i//4)*244;full.paste(im,(x,y));d.text((x+4,y+222),p.parent.name+' / '+p.stem,fill='#27354b')
 full.save(ROOT/'previews'/f'{mode}-all.jpg',quality=90)
 doc=fitz.open()
 for p in pages:
  pg=doc.new_page(width=1280,height=720);pg.insert_image(pg.rect,filename=str(p))
 doc.save(ROOT/'pdfs'/f'{mode}-sheets.pdf',garbage=4,deflate=True);doc.close()
 doc=fitz.open()
 for pdf in sorted((ROOT/'pdfs'/mode).glob('*.pdf')):
  with fitz.open(pdf) as src:doc.insert_pdf(src)
 doc.save(ROOT/'pdfs'/f'{mode}-all.pdf',garbage=4,deflate=True);doc.close()
 print(mode,len(files),'PNGs,',len(pages),'sheet pages',flush=True)
cards=[]
for deck in inventory:
 for fn in deck['files']:
  id=fn[:-4];label=f"{deck['id']} / {id}"
  cards.append(f'''<button class="tile" data-deck="{deck['id']}" data-id="{id}" data-label="{label}"><img loading="lazy" src="renders/final/replica/{deck['id']}/{fn}" alt="{label}"><span>{label}</span></button>''')
css='''*{box-sizing:border-box}body{margin:0;background:#edf1f6;color:#172b48;font-family:system-ui,sans-serif}header{position:sticky;top:0;background:#fff;z-index:2;padding:20px 28px;border-bottom:1px solid #d3dce7}h1{font-size:24px;margin:0 0 6px}p{margin:6px 0;font-size:14px;color:#54657a}nav{display:flex;gap:10px;flex-wrap:wrap;margin-top:15px}select,nav button,a{font:inherit;padding:9px 12px;border:1px solid #bcccdc;border-radius:5px;background:white;color:#174879;text-decoration:none}nav button[aria-pressed=true]{background:#174879;color:white}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;padding:24px}.tile{background:white;border:1px solid #d5dfe9;border-radius:7px;overflow:hidden;padding:0;cursor:pointer;text-align:left}.tile img{width:100%;display:block}.tile span{display:block;padding:10px 12px;font-size:13px}.tile[hidden]{display:none}dialog{border:0;border-radius:8px;padding:0;max-width:96vw;background:#172b48;color:white}dialog::backdrop{background:#0b1428d9}dialog .bar{display:flex;justify-content:space-between;align-items:center;padding:10px 16px}dialog img{display:block;max-width:94vw;max-height:85vh;object-fit:contain}dialog button{padding:6px 12px;cursor:pointer}footer{padding:20px 28px;color:#63748b;font-size:13px}'''
script='''let mode='replica';const tiles=[...document.querySelectorAll('.tile')],dialog=document.querySelector('dialog'),viewer=dialog.querySelector('img'),label=dialog.querySelector('span');let active=0;function imagePath(t){return mode==='comparison'?`comparisons/final/replica/${t.dataset.deck}/${t.dataset.id}.jpg`:`renders/final/${mode}/${t.dataset.deck}/${t.dataset.id}.png`}function show(i){active=i;viewer.src=imagePath(tiles[i]);label.textContent=tiles[i].dataset.label;if(!dialog.open)dialog.showModal()}tiles.forEach((t,i)=>t.onclick=()=>show(i));document.querySelectorAll('[data-mode]').forEach(b=>b.onclick=()=>{mode=b.dataset.mode;document.querySelectorAll('[data-mode]').forEach(x=>x.setAttribute('aria-pressed',x===b));tiles.forEach(t=>t.querySelector('img').src=imagePath(t))});document.querySelector('select').onchange=e=>tiles.forEach(t=>t.hidden=e.target.value!=='all'&&t.dataset.deck!==e.target.value);dialog.querySelector('button').onclick=()=>dialog.close();document.onkeydown=e=>{if(!dialog.open)return;const visible=tiles.map((t,i)=>t.hidden?-1:i).filter(i=>i>=0),at=visible.indexOf(active);if(e.key==='ArrowRight')show(visible[(at+1)%visible.length]);if(e.key==='ArrowLeft')show(visible[(at+visible.length-1)%visible.length])};'''
page=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Business Prism · 117 slides</title><style>{css}</style></head><body><header><h1>Business Prism · 117 slides</h1><p>원본 재현 · Rhetis 라이브러리 재조립 · 원본과 나란히 비교</p><nav><select aria-label="덱 선택"><option value="all">전체 8개 덱</option>{''.join(f'<option value="{d["id"]}">{html.escape(d["name"])}</option>' for d in inventory)}</select><button data-mode="replica" aria-pressed="true">원본 재현</button><button data-mode="assembly" aria-pressed="false">라이브러리 재조립</button><button data-mode="comparison" aria-pressed="false">원본 / 결과 비교</button><a href="pdfs/replica-all.pdf">재현 PDF</a><a href="pdfs/assembly-all.pdf">재조립 PDF</a><a href="collection/business-prism/light.html">키트 라이트</a><a href="collection/business-prism/dark.html">키트 다크</a></nav></header><main>{''.join(cards)}</main><footer>슬라이드 1280 × 720 · 이미지를 누르면 확대 · ← → 이동 · Esc 닫기</footer><dialog><div class="bar"><span></span><button>닫기</button></div><img alt="확대 슬라이드"></dialog><script>{script}</script></body></html>'''
(ROOT/'preview.html').write_text(page)
