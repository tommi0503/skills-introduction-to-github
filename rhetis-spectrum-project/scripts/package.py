from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import fitz,json,zipfile,hashlib,shutil,html,sys
ROOT=Path('.');ART=Path('artifacts');ART.mkdir(exist_ok=True);(ART/'sheets').mkdir(exist_ok=True)
fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font=ImageFont.truetype(fontpath,13);large=ImageFont.truetype(fontpath,22)
inventory=json.loads(Path('review/input-inventory.json').read_text());decks=inventory['decks']
# Each contact sheet is itself 1280 x 720; full slides are never resized in their own PNGs.
sheets={}
for mode in ['original','clone','assembly']:
 pages=[]
 for deck in decks:
  d=deck['deck'];ps=sorted(Path(f'public/references/{d}').glob('*.png')) if mode=='original' else sorted(Path(f'renders/final/{mode}').glob(f'{d}-*.png'))
  for start in range(0,len(ps),12):
   canvas=Image.new('RGB',(1280,720),'#eef2f5');draw=ImageDraw.Draw(canvas);draw.text((26,20),f'RHETIS SPECTRUM  /  {mode.upper()}  /  DECK {d}  /  {start+1}-{min(start+12,len(ps))}',font=large,fill='#172331')
   for i,p in enumerate(ps[start:start+12]):
    x=20+(i%4)*315;y=65+(i//4)*213;im=Image.open(p).convert('RGB').resize((300,169),Image.Resampling.LANCZOS);canvas.paste(im,(x,y));draw.text((x,y+177),p.stem,font=font,fill='#425669')
   out=ART/'sheets'/f'{mode}-{d}-{start//12+1}.png';canvas.save(out);pages.append(out)
 sheets[mode]=pages
# Browser-generated PDFs retain selectable text and vector content.
for mode in ['clone','assembly']:
 if '--resume' in sys.argv and (ART/'pdf'/f'all-slides-{mode}.pdf').exists():continue
 doc=fitz.open()
 for deck in decks:
  with fitz.open(ART/'pdf'/f"{deck['deck']}-{mode}.pdf") as part:doc.insert_pdf(part)
 assert len(doc)==76
 doc.save(ART/'pdf'/f'all-slides-{mode}.pdf',garbage=4,deflate=True);doc.close()
for mode,pages in sheets.items():
 ims=[Image.open(p).convert('RGB') for p in pages];ims[0].save(ART/'pdf'/f'contact-sheets-{mode}.pdf',save_all=True,append_images=ims[1:],resolution=96)
# Library fixture sheets: all full-resolution images plus compact navigable index and sheet PDFs.
for mode in ['light','dark']:
 ps=sorted(Path(f'renders/library/{mode}').glob('*.png'));pages=[]
 assert len(ps)==89
 for start in range(0,len(ps),12):
  c=Image.new('RGB',(1280,720),'#eef2f5');draw=ImageDraw.Draw(c);draw.text((26,20),f'RHETIS SPECTRUM  /  LIBRARY {mode.upper()}  /  {start+1}-{min(start+12,len(ps))}',font=large,fill='#172331')
  for i,p in enumerate(ps[start:start+12]):
   x=20+(i%4)*315;y=65+(i//4)*213;c.paste(Image.open(p).convert('RGB').resize((300,169),Image.Resampling.LANCZOS),(x,y));draw.text((x,y+177),p.stem,font=font,fill='#425669')
  out=ART/'sheets'/f'library-{mode}-{start//12+1}.png';c.save(out);pages.append(out)
 ims=[Image.open(p).convert('RGB') for p in pages];ims[0].save(ART/'pdf'/f'contact-sheets-library-{mode}.pdf',save_all=True,append_images=ims[1:],resolution=96)
# Offline preview relies solely on relative files; no server is required.
style='''*{box-sizing:border-box}body{margin:0;background:#eef2f5;font-family:system-ui,sans-serif;color:#172331}nav{padding:25px 32px;background:white;border-bottom:1px solid #ccd6de;display:flex;justify-content:space-between}header{padding:42px 32px 20px}h1{font-size:52px;letter-spacing:-2px;margin:12px 0}p{line-height:1.6}button,input{font:inherit;padding:10px 18px;border-radius:999px;border:1px solid #b2c5d4;background:white;color:#153a5e}button.active{background:#004391;color:white}section{padding:12px 32px 32px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:20px}article{padding:12px;background:white;border:1px solid #d3dde5;border-radius:9px}img{width:100%;aspect-ratio:16/9;display:block}article p{font-size:13px;margin:10px 0}a{color:#00569a;font-size:13px}footer{padding:30px}.library{display:none}small{color:#607487}'''
body='<nav><b>RHETIS / SPECTRUM</b><span>76 slides · 6 decks · 1280 × 720</span></nav><header><small>REFERENCE COLLECTION 098—106</small><h1>Rhetis Spectrum</h1><p>원본 재현과 라이브러리 재조립을 한 장씩 살펴보세요.</p><button class="active" data-mode="clone">원본 재현</button> <button data-mode="assembly">라이브러리 재조립</button> <button data-mode="library">라이브러리</button><p><a href="pdf/all-slides-clone.pdf">원본 재현 PDF</a> · <a href="pdf/all-slides-assembly.pdf">라이브러리 조립 PDF</a> · <a href="review/FINAL-REVIEW.md">검수 기록</a></p></header>'
for deck in decks:
 d=deck['deck'];body+=f'<section class="deck"><h2>{d} <small>{deck["count"]} slides</small></h2><div class="grid">'
 for p in sorted(Path('renders/final/clone').glob(d+'-*.png')):
  name=p.stem;body+=f'<article><a class="picture" href="renders/clone/{name}.png"><img loading="lazy" data-name="{name}" src="renders/clone/{name}.png" alt="{name}"></a><p>{name} · 1280×720</p><a href="comparisons/{name}.jpg">원본 / 결과 비교</a></article>'
 body+='</div></section>'
body+='<section class="library"><h2>Library · Light / Dark</h2><p><a href="pdf/contact-sheets-library-light.pdf">Light PDF</a> · <a href="pdf/contact-sheets-library-dark.pdf">Dark PDF</a></p><div class="grid">'
for mode in ['light','dark']:
 for p in sorted(Path(f'renders/library/{mode}').glob('*.png')):body+=f'<article><a href="library/{mode}/{p.name}"><img loading="lazy" src="library/{mode}/{p.name}" alt="{mode} {p.stem}"></a><p>{mode} / {p.stem}</p></article>'
body+='</div></section><footer>사진·복잡한 이미지는 지정된 회색 placeholder로 처리했습니다. 원본·결과 차이와 판독 판단은 검수 기록에 있습니다.</footer>'
js="document.querySelectorAll('[data-mode]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-mode]').forEach(x=>x.classList.toggle('active',x===b));const m=b.dataset.mode;document.querySelectorAll('.deck').forEach(x=>x.style.display=m==='library'?'none':'block');document.querySelector('.library').style.display=m==='library'?'block':'none';if(m!=='library')document.querySelectorAll('img[data-name]').forEach(i=>{i.src='renders/'+m+'/'+i.dataset.name+'.png';i.parentElement.href=i.src})});"
preview='<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Rhetis Spectrum · Offline preview</title><style>'+style+'</style>'+body+'<script>'+js+'</script></html>'
(ART/'preview.html').write_text(preview.replace('renders/clone/','../renders/final/clone/').replace('renders/assembly/','../renders/final/assembly/').replace('comparisons/','../comparisons/final/').replace('library/light/','../renders/library/light/').replace('library/dark/','../renders/library/dark/').replace('review/FINAL-REVIEW.md','../review/FINAL-REVIEW.md').replace("'renders/'+m+","'../renders/final/'+m+"))
# Single collection folder at the top level, per intake contract.
with zipfile.ZipFile(ART/'rhetis-spectrum-collection.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(Path('collection/rhetis-spectrum').rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to('collection')))
# Reproducible source package; installed dependencies and intermediate render rounds are excluded.
with zipfile.ZipFile(ART/'rhetis-spectrum-source.zip','w',zipfile.ZIP_DEFLATED) as z:
 for folder in ['src','collection','contract','tools','scripts','public','review']:
  for p in sorted(Path(folder).rglob('*')):
   if p.is_file() and '__pycache__' not in p.parts:z.write(p,'rhetis-spectrum-project/'+str(p))
 for filename in ['README.md','package.json','package-lock.json','vite.config.mjs','index.html','light.html','dark.html','.gitignore']:
  z.write(filename,'rhetis-spectrum-project/'+filename)
# Full result package: all full-sized PNGs, individual comparisons, vector PDFs, sheets and logs.
with zipfile.ZipFile(ART/'rhetis-spectrum-deliverables.zip','w',zipfile.ZIP_DEFLATED) as z:
 for mode in ['clone','assembly']:
  for p in sorted(Path(f'renders/final/{mode}').glob('*.png')):z.write(p,'renders/'+mode+'/'+p.name)
 for p in sorted(Path('comparisons/final').glob('*.jpg')):z.write(p,'comparisons/'+p.name)
 for mode in ['light','dark']:
  for p in sorted(Path(f'renders/library/{mode}').glob('*.png')):z.write(p,'library/'+mode+'/'+p.name)
 for folder in ['pdf','sheets']:
  for p in sorted((ART/folder).glob('*')):z.write(p,str(p.relative_to(ART)))
 for p in sorted(Path('review').rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:z.write(p,str(p))
 z.writestr('preview.html',preview)
 for p in [ART/'rhetis-spectrum-collection.zip',ART/'rhetis-spectrum-source.zip']:z.write(p,p.name)
 z.write('README.md','README.md')
for p in ART.glob('*.zip'):
 with zipfile.ZipFile(p) as z:assert z.testzip() is None
 print(p,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())
