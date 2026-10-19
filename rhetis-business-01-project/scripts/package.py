from pathlib import Path
from PIL import Image,ImageDraw
from pypdf import PdfReader,PdfWriter
import json,hashlib,zipfile,shutil
P=Path(__file__).resolve().parents[1];out=P/'deliverables';out.mkdir(exist_ok=True)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sheet(paths,target,cols=4,tw=320):
 th=180;cellh=210;im=Image.new('RGB',(cols*tw,((len(paths)+cols-1)//cols)*cellh),'#e4e6e8');d=ImageDraw.Draw(im)
 for i,p in enumerate(paths):
  thumb=Image.open(p).convert('RGB');thumb.thumbnail((tw-12,th));x=(i%cols)*tw;y=(i//cols)*cellh;im.paste(thumb,(x+6,y));d.text((x+8,y+183),p.stem,fill='#173537')
 im.save(target,quality=90)
for mode in ['clone','assembled']:
 paths=sorted((P/'renders'/'final'/mode).glob('*.png'));sheet(paths,out/f'preview-{mode}.jpg')
 writer=PdfWriter()
 for p in sorted((out/'pdf').glob(f'{mode}-d*.pdf')):writer.append(str(p))
 writer.write(str(out/f'{mode}-slides.pdf'))
for d in range(1,6):sheet(sorted((P/'renders/final/clone').glob(f'd0{d}-*.png')),out/f'preview-d0{d}.jpg')
def zip_files(path,files):
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p,arc in files:z.write(p,arc)
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None
  assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
 return {'name':path.name,'bytes':path.stat().st_size,'sha256':digest(path),'entries':len(files),'crcVerified':True}
collection=P/'rhetis-business-01'
summary=[];summary.append(zip_files(out/'rhetis-business-01.zip',[(p,p.relative_to(P).as_posix()) for p in sorted(collection.rglob('*')) if p.is_file()]))
render_files=[]
for folder in ['renders/final','comparisons/final','review/collection']:
 render_files.extend((p,p.relative_to(P).as_posix()) for p in sorted((P/folder).rglob('*')) if p.is_file())
for p in sorted((P/'review').rglob('*.json')):
 if p.name!='github-download-verification.json':render_files.append((p,p.relative_to(P).as_posix()))
render_files.append((P/'review/input-inventory.csv','review/input-inventory.csv'))
for p in sorted(out.glob('*.jpg')):render_files.append((p,p.name))
for p in sorted(out.glob('*.pdf')):render_files.append((p,p.name))
render_files.append((out/'preview.html','preview.html'))
for p in sorted((out/'pdf').glob('*.pdf')):render_files.append((p,p.relative_to(out).as_posix()))
for p in [P/'README.md',P/'review/REVIEW.md',P/'public/reference/manifest.json']:render_files.append((p,p.relative_to(P).as_posix()))
summary.append(zip_files(out/'rhetis-business-01-renders.zip',render_files))
source_files=[]
for folder in ['src','scripts','contract','tools','public','rhetis-business-01']:
 source_files.extend((p,'rhetis-business-01-project/'+p.relative_to(P).as_posix()) for p in sorted((P/folder).rglob('*')) if p.is_file())
for p in sorted((P/'review').glob('*')):
 if p.is_file() and p.suffix in ('.json','.md','.csv') and p.name!='github-download-verification.json':source_files.append((p,'rhetis-business-01-project/'+p.relative_to(P).as_posix()))
for p in sorted((P/'review/final').glob('*.json')):source_files.append((p,'rhetis-business-01-project/'+p.relative_to(P).as_posix()))
for name in ['.gitignore','index.html','package.json','package-lock.json','README.md','light.html','dark.html']:
 p=P/name;source_files.append((p,'rhetis-business-01-project/'+name))
summary.append(zip_files(out/'rhetis-business-01-source.zip',source_files))
(out/'checksums.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print(json.dumps(summary,ensure_ascii=False,indent=2))
