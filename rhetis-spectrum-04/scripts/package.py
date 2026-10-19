from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from pypdf import PdfReader,PdfWriter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
import json,zipfile,hashlib,shutil,html,os
root=Path(__file__).resolve().parent.parent
out=Path(os.environ.get('RHETIS_OUTPUT',str(root/'output')));out.mkdir(parents=True,exist_ok=True)
archives=root/'downloads';archives.mkdir(exist_ok=True)
manifest=json.loads((root/'review/manifest.json').read_text())
for mode in ['direct','assembled']:
 writer=PdfWriter()
 for f in sorted((root/'pdf/pages'/mode).glob('*.pdf')):writer.append(f)
 writer.write(root/'pdf'/f'{mode}-slides.pdf')
 # Four slide thumbnails per 1280×720 contact page; individual renders remain full resolution.
 files=sorted((root/'renders'/mode/'final').glob('*.png'));sheets=root/'sheets'/mode;sheets.mkdir(parents=True,exist_ok=True)
 pdf=Canvas(str(root/'pdf'/f'{mode}-contact-sheets.pdf'),pagesize=(960,540))
 for start in range(0,len(files),4):
  canvas=Image.new('RGB',(1280,720),'#e7e7e7');dr=ImageDraw.Draw(canvas)
  for j,f in enumerate(files[start:start+4]):
   x=(j%2)*640;y=(j//2)*360
   canvas.paste(Image.open(f).convert('RGB').resize((624,351)),(x+8,y+9))
   dr.rectangle((x+8,y+9,x+146,y+28),fill='white');dr.text((x+13,y+12),f.stem,fill='black')
  dest=sheets/f'sheet-{start//4+1:02d}.png';canvas.save(dest);pdf.drawImage(ImageReader(canvas),0,0,960,540);pdf.showPage()
 pdf.save()
# Compact complete visual overview, saved as JPEG so every deliverable PNG stays 1280×720.
files=sorted((root/'renders/direct/final').glob('*.png'));preview=Image.new('RGB',(1920,((len(files)+5)//6)*204),'#e7e7e7');dr=ImageDraw.Draw(preview)
for i,f in enumerate(files):
 x=i%6*320;y=i//6*204;preview.paste(Image.open(f).convert('RGB').resize((312,176)),(x+4,y));dr.text((x+8,y+180),f.stem,fill='black')
preview.save(root/'preview.jpg',quality=90)
cards=[]
for d in manifest:
 for s in d['slides']:
  f=d['id']+'-'+s['id'];cards.append(f'<article><a href="renders/direct/final/{f}.png"><img loading="lazy" src="renders/direct/final/{f}.png" alt="{html.escape(s["title"])}"></a><p>{f} · {html.escape(s["title"])}</p><a href="comparisons/direct/final/{f}.jpg">원본 비교</a> · <a href="renders/assembled/final/{f}.png">재조립</a></article>')
(root/'preview.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><title>Spectrum 04 · 전체 미리보기</title><style>body{font-family:system-ui;margin:24px;background:#eee;color:#222}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(460px,1fr));gap:20px}article{background:white;padding:12px}img{width:100%;height:auto}a{color:#333}</style><h1>Spectrum 04 · 82 slides</h1><p><a href="index.html">편집 가능한 HTML</a> · <a href="light.html">라이트 라이브러리</a> · <a href="dark.html">다크 라이브러리</a> · <a href="pdf/direct-slides.pdf">재현 PDF</a> · <a href="pdf/assembled-slides.pdf">재조립 PDF</a></p><main>'+''.join(cards)+'</main>',encoding='utf8')
def archive(dest,files,prefix=''):
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for f,rel in files:z.write(f,prefix+rel)
 with zipfile.ZipFile(dest) as z:
  bad=z.testzip();assert bad is None,(dest,bad)
 return {'file':dest.name,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
lib=root/'collections/spectrum-04';entries=[]
entries.append(archive(archives/'spectrum-04-collection.zip',[(f,f.relative_to(lib).as_posix()) for f in sorted(lib.rglob('*')) if f.is_file()],prefix='spectrum-04/'))
result=[]
for name in ['renders','comparisons','sheets','pdf','review']:
 for f in sorted((root/name).rglob('*')):
  if not f.is_file():continue
  rel=f.relative_to(root).as_posix()
  if '/review1/' in rel or '/round1/' in rel or '/pages/' in rel or '/checkfinal/' in rel:continue
  if name=='renders' and '/final/' not in rel and not rel.startswith('renders/library/'):continue
  result.append((f,rel))
for name in ['preview.jpg','preview.html','README.md','index.html','light.html','dark.html']:
 result.append((root/name,name))
# Editable source accompanies the offline preview, excluding dependencies and redundant intermediates.
source=[]
for name in ['src','public','collections','contract','tools','scripts','review']:
 for f in sorted((root/name).rglob('*')):
  if f.is_file() and '/review1/' not in str(f) and '/round1/' not in str(f):source.append((f,f.relative_to(root).as_posix()))
for name in ['index.html','light.html','dark.html','package.json','package-lock.json','requirements.txt','README.md','.gitignore']:source.append((root/name,name))
entries.append(archive(archives/'spectrum-04-source.zip',source,prefix='rhetis-spectrum-04/'))
# The review package includes runnable HTML and local fonts as well as every image/PDF.
existing={r for _,r in result}
result += [(f,r) for f,r in source if r not in existing and r.split('/')[0] in ['src','public','collections']]
entries.append(archive(archives/'spectrum-04-deliverables.zip',result,prefix='spectrum-04-deliverables/'))
(archives/'checksums.json').write_text(json.dumps(entries,indent=2)+'\n')
for e in entries:
 assert e['bytes']<100_000_000,('GitHub file limit',e)
 shutil.copy2(archives/e['file'],out/e['file'])
shutil.copy2(root/'preview.jpg',out/'spectrum-04-preview.jpg');shutil.copy2(archives/'checksums.json',out/'checksums.json')
print(json.dumps(entries,indent=2))
