from pathlib import Path
from PIL import Image,ImageDraw
import zipfile,json,hashlib,shutil,fitz
root=Path(__file__).resolve().parent.parent
# GitHub delivery files live beside the isolated source folder.
out=root.parent;out.mkdir(parents=True,exist_ok=True)
exp=root/'exports';exp.mkdir(exist_ok=True)
for mode in ['replica','assembled']:
 doc=fitz.open()
 for p in sorted((exp/'pdf').glob(f'{mode}-[0-9][0-9].pdf')):
  src=fitz.open(p);doc.insert_pdf(src)
 doc.save(exp/f'{mode}-107-slides.pdf',garbage=4,deflate=True)
 files=sorted((root/f'renders/final/{mode}').glob('*.png'))
 W=1280;tw=312;th=176;rowh=204
 board=Image.new('RGB',(W,((len(files)+3)//4)*rowh+24),'#e8e8e8');d=ImageDraw.Draw(board)
 for i,p in enumerate(files):
  x=8+(i%4)*320;y=12+(i//4)*rowh;im=Image.open(p).convert('RGB').resize((tw,th),Image.Resampling.LANCZOS);board.paste(im,(x,y+19));d.text((x,y+2),p.stem,fill='#222')
 board.save(exp/f'{mode}-overview.jpg',quality=92)
shutil.copy(exp/'replica-overview.jpg',out/'rhetis-studio-preview.jpg')
collection=root/'collections/studio-spectrum'
with zipfile.ZipFile(out/'studio-spectrum.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(collection.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(collection.parent))
with zipfile.ZipFile(out/'rhetis-studio-delivery.zip','w',zipfile.ZIP_DEFLATED) as z:
 for sub in ['src','public','contract','tools','scripts','review','collections','renders/final','comparisons/final','exports']:
  for p in sorted((root/sub).rglob('*')):
   if p.is_file() and 'node_modules' not in p.parts and '__pycache__' not in p.parts and not any(x.startswith('round') or x=='adapter-check' for x in p.relative_to(root).parts):z.write(p,Path('rhetis-studio')/p.relative_to(root))
 for name in ['package.json','package-lock.json','index.html','vite.config.ts','tsconfig.json','README.md']:
  p=root/name
  if p.exists():z.write(p,Path('rhetis-studio')/name)
for p in [out/'studio-spectrum.zip',out/'rhetis-studio-delivery.zip']:
 with zipfile.ZipFile(p) as z:assert z.testzip() is None
 print(p.name,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())
