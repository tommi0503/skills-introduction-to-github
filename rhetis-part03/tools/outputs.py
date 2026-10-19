from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib
R=Path(__file__).resolve().parents[1];(R/'comparisons/final').mkdir(parents=True,exist_ok=True);(R/'deliverables/preview').mkdir(parents=True,exist_ok=True);(R/'deliverables/pdf').mkdir(exist_ok=True)
decks=json.loads((R/'review/scenes.json').read_text());summary=[];slides=[];contacts=[];comparisonpages=[]
for d in decks:
 imgs=[]
 for s in d['slides']:
  key=d['id']+'-'+s['id'];p=R/'renders/final'/f'{key}.png';im=Image.open(p).convert('RGB');assert im.size==(1280,720);imgs.append(im);slides.append(im)
  original=Image.open(R/'public/reference'/d['id']/f'{s["id"]}.png').convert('RGB');pair=Image.new('RGB',(2560,720),'white');pair.paste(original,(0,0));pair.paste(im,(1280,0));pair.save(R/'comparisons/final'/f'{key}.png',optimize=True)
  # Individually readable final comparison preview, not a deck contact sheet.
  pair.resize((1280,360)).save(R/'comparisons/final'/f'{key}.jpg',quality=90)
  comparisonpages.append(pair)
 rows=(len(imgs)+2)//3;sheet=Image.new('RGB',(1280,rows*260),'#e9ece8');dr=ImageDraw.Draw(sheet)
 for i,(im,s)in enumerate(zip(imgs,d['slides'])):
  x=(i%3)*426;y=(i//3)*260;sheet.paste(im.resize((416,234)),(x+5,y+5));dr.text((x+8,y+241),d['id']+' / '+s['id'],fill='#303b32')
 sheet.save(R/'deliverables/preview'/f'deck-{d["id"]}.jpg',quality=93);contacts.append(sheet)
 imgs[0].save(R/'deliverables/pdf'/f'reproduced-{d["id"]}.pdf',save_all=True,append_images=imgs[1:],resolution=96)
 summary.append({'deck':d['id'],'title':d['title'],'count':len(imgs)})
slides[0].save(R/'deliverables/pdf/reproduced-all-slides.pdf',save_all=True,append_images=slides[1:],resolution=96)
contacts[0].save(R/'deliverables/pdf/reproduced-contact-sheets.pdf',save_all=True,append_images=contacts[1:],resolution=96)
# One image pair per PDF page, full slide remains readable at zoom.
comparisonpages[0].save(R/'deliverables/pdf/original-vs-result.pdf',save_all=True,append_images=comparisonpages[1:],resolution=96)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20);overview=Image.new('RGB',(1280,4*400+80),'#e9ece8');dr=ImageDraw.Draw(overview);dr.text((24,22),'RHETIS / 90 SLIDES / 8 DECKS / 1280 x 720',font=font,fill='#17251a')
for i,d in enumerate(decks):
 im=Image.open(R/'renders/final'/f'{d["id"]}-{d["slides"][0]["id"]}.png');x=i%2*640;y=i//2*400+70;overview.paste(im.resize((616,347)),(x+12,y));dr.text((x+16,y+355),f'{d["id"]} / {len(d["slides"])} slides',font=font,fill='#253426')
overview.save(R/'deliverables/preview/overview.jpg',quality=94)
(R/'review/inventory.json').write_text(json.dumps({'total':len(slides),'size':[1280,720],'decks':summary},ensure_ascii=False,indent=2))
# Static preview uses final assets with a mode switch; usable without npm or a running server.
entries=[]
for d in decks:
 entries.append(f'<h2>{d["id"]} · {d["title"]}</h2>')
 for s in d['slides']:
  k=d['id']+'-'+s['id'];entries.append(f'<article><p>{k} · {s["title"]}</p><div class="pair"><img class="original" loading="lazy" src="../comparisons/final/{k}.png" alt="원본"><img loading="lazy" src="../renders/final/{k}.png" class="result" alt="재현"><img class="assembly" loading="lazy" src="../renders/assembly/{k}.png" alt="라이브러리 재조립"></div></article>')
(R/'deliverables/preview.html').write_text('''<!doctype html><html lang="ko"><meta charset="utf-8"><title>Rhetis Part 03 · Full preview</title><style>*{box-sizing:border-box}body{margin:0;background:#edf0ec;color:#1b281e;font-family:Arial,sans-serif}header{position:sticky;top:0;z-index:3;background:#17271e;color:#fff;padding:18px 28px;display:flex;gap:30px;align-items:center}h1{font-size:20px;margin:0}button{border:1px solid #a3b9a8;border-radius:20px;padding:10px 18px;background:#e5ff5b;cursor:pointer;color:#15251b}main{padding:24px}h2{margin-top:55px}article{margin:24px 0 36px}.pair{display:flex;gap:12px;flex-wrap:wrap}.pair img{display:block;width:min(100%,620px);height:auto;box-shadow:0 2px 8px #0002}.original{width:min(100%,1280px)!important}.show-original .result{display:none}.assembly{display:none}body.show-assembly .assembly{display:block}body:not(.show-original) .original{display:none}p{font-size:13px;color:#526355}</style><header><h1>Rhetis · 90 slides</h1><button onclick="document.body.classList.toggle('show-original')">원본 비교</button><button onclick="document.body.classList.toggle('show-assembly')">라이브러리 조립본</button><a style="color:white" href="pdf/reproduced-all-slides.pdf">PDF</a></header><main>'''+''.join(entries)+'</main></html>')
print('Created',len(slides),'PNG pairs, PDFs, static preview')
