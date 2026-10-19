from PIL import Image,ImageDraw
from pathlib import Path
import sys
root=Path(__file__).resolve().parent.parent
for d in sorted((root/'public/reference').iterdir()):
 if len(sys.argv)>1 and d.name!=sys.argv[1]:continue
 out=root/'comparisons'/d.name;out.mkdir(parents=True,exist_ok=True)
 for p in sorted(d.glob('*.png')):
  sid=p.stem.split('_')[-1];render=root/'renders/replica'/d.name/f'{sid}.png'
  if not render.exists():continue
  a=Image.open(p).convert('RGB');a=a.resize((1280,720));b=Image.open(render).convert('RGB')
  c=Image.new('RGB',(2560,752),'#efefef');c.paste(a,(0,32));c.paste(b,(1280,32));dr=ImageDraw.Draw(c);dr.text((10,9),f'REFERENCE {d.name}/{sid}',fill='#111');dr.text((1290,9),'IMPLEMENTATION',fill='#111');c.save(out/f'{sid}.jpg',quality=90)
