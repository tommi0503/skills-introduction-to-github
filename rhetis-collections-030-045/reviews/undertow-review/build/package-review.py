from pathlib import Path
from PIL import Image,ImageDraw
import re,json,shutil
R=Path('/workspace/work/deliverables/undertow-review');O=Path('/workspace/work/deck/miricanvas_기업_selected/031_1hfha_검정_미니멀_비즈니스_제안서')
for mode in ['light','dark']:
 fs=sorted((R/'library'/('fixtures-'+mode)).glob('*.png'));groups={};pages=[]
 for f in fs:
  n=f.name.split('---')[0][4:];groups.setdefault(n,[]).append(f);pages.append(Image.open(f).convert('RGB'))
 for n,imgs in groups.items():
  d=R/'library'/n;d.mkdir(exist_ok=True);sheet=Image.new('RGB',(1280,len(imgs)*748),'#ddd');dr=ImageDraw.Draw(sheet)
  for i,f in enumerate(imgs):dr.text((12,i*748+7),f.stem,fill='black');sheet.paste(Image.open(f).convert('RGB'),(0,i*748+28))
  sheet.save(d/(mode+'.png'))
 pages[0].save(R/'library'/('library-'+mode+'.pdf'),save_all=True,append_images=pages[1:],resolution=96,quality=90)
 print(mode,'pages',len(pages),'folders',len(groups))
for typ in ['replica','reassembled']:
 ims=[]
 for i in range(1,14):
  f=f'{i:02}';im=Image.open(R/typ/(f+'.png')).convert('RGB');orig=Image.open(O/('slide_'+f+'.png')).convert('RGB');c=Image.new('RGB',(2560,720));c.paste(orig,(0,0));c.paste(im,(1280,0));c.save(R/('compare-'+typ)/(f+'.png'));ims.append(im)
 ims[0].save(R/typ/(typ+'.pdf'),save_all=True,append_images=ims[1:],resolution=96,quality=90)
# Preserve authored generators/renderers as source, never source deck images in executable pages.
d=R/'build';d.mkdir(exist_ok=True)
for p in Path('/workspace/work/agents/031').glob('*'):
 if p.is_file():shutil.copy(p,d/p.name)
print('review bytes',sum(p.stat().st_size for p in R.rglob('*') if p.is_file()))
