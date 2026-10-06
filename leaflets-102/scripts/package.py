from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import csv,json,hashlib,zipfile,html,sys
root=Path(__file__).resolve().parents[1]
dest=root/'deliverables';dest.mkdir(exist_ok=True)
manifest=json.loads((root/'src/data/manifest.json').read_text())
byid={r['filename'][:3]:r for r in manifest}
records=[]
for name in 'abcdef':
 p=root/'review'/f'group-{name}.json'
 if p.exists():records.append(json.loads(p.read_text()))
cards=[]
for i in range(1,103):
 id=f'{i:03}';p=root/'renders/final'/f'{id}.png';im=Image.open(p);im.load()
 assert im.size==(1280,910),(id,im.size)
 cards.append(f'<article><h2>{id} · {html.escape(byid[id]["title"])}</h2><a href="renders/final/{id}.png"><img loading="lazy" src="renders/final/{id}.png" width="1280" height="910" alt="{id}"></a><p><a href="comparisons/round-final/{id}.jpg">원본과 결과 나란히 보기</a> · <a href="comparisons/round-final/{id}.json">자동 검사 기록</a></p></article>')
page='''<!doctype html><html lang="ko"><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>리플렛 102개 전체 미리보기</title><style>*{box-sizing:border-box}body{margin:0;background:#eef0f3;color:#202830;font-family:Arial,sans-serif}header{max-width:1500px;margin:auto;padding:28px}h1{font-size:28px}main{max-width:1500px;margin:auto;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;padding:0 24px 40px}article{background:#fff;border:1px solid #dbe1e8;border-radius:10px;padding:16px}h2{font-size:14px;min-height:35px;line-height:1.5}img{width:100%;height:auto;display:block}a{color:#2859a7}p{font-size:13px;line-height:1.6}@media(max-width:800px){main{grid-template-columns:1fr}}</style><header><h1>리플렛 UI · 102개 화면</h1><p>51개 양면 리플렛 · 모든 결과 1280×910 · 원본 좌표·비율 유지 · 사진과 복잡한 그래픽은 연회색 placeholder</p><p><a href="review/검수기록.md">전체 검수 기록</a> · <a href="review/final-verification.json">최종 자동 검사</a></p></header><main>'''+''.join(cards)+'</main></html>'
(root/'preview.html').write_text(page)
sheet=Image.new('RGB',(1600,26*308),'#eef0f3');draw=ImageDraw.Draw(sheet)
fontpath=root/'node_modules/pretendard/dist/public/static/Pretendard-Regular.otf'
try:font=ImageFont.truetype(str(fontpath),14)
except:font=ImageFont.load_default()
for i in range(102):
 id=f'{i+1:03}';im=Image.open(root/'renders/final'/f'{id}.png').convert('RGB');im.thumbnail((384,273));x=(i%4)*400+8;y=(i//4)*308+26
 sheet.paste(im,(x,y));draw.text((x,y-20),id+' · '+byid[id]['title'][:23],font=font,fill='#222')
sheet.save(root/'preview.jpg',quality=91)
verification=json.loads((root/'review/final-verification.json').read_text());assert verification['passed'],verification
include=[]
for p in root.rglob('*'):
 if not p.is_file():continue
 parts=p.relative_to(root).parts
 if parts[0] in ['node_modules','dist','deliverables','.cache','public','work']:continue
 if parts[:2] in [('renders','1'),('renders','2'),('comparisons','round-1'),('comparisons','round-2')]:continue
 if p.suffix in ['.log','.tsbuildinfo'] or p.name.startswith('work-'):continue
 include.append(p)
archive=dest/'leaflets-102-review.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(include):z.write(p,'leaflets-102/'+str(p.relative_to(root)))
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 assert len([n for n in z.namelist() if '/renders/final/' in n and n.endswith('.png')])==102
 assert len([n for n in z.namelist() if '/comparisons/round-final/' in n and n.endswith('.jpg')])==102
report={'zip':archive.name,'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'png_count':102,'comparison_count':102,'all_png_size':[1280,910],'zip_crc_passed':True}
(dest/'integrity.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
if archive.stat().st_size>99*1024*1024:raise RuntimeError('Archive exceeds GitHub normal blob budget')
