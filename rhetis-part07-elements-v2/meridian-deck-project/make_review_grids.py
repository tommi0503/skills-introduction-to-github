from pathlib import Path
from PIL import Image,ImageDraw
import json,sys
P=Path(__file__).parent;D=P/'visual-review';D.mkdir(exist_ok=True)
for leaf in sys.argv[1:]:
 j=json.loads((P/'sheets'/(leaf+'-checks.json')).read_text())
 for mode,cases in j['modes'].items():
  by={}
  for x in cases:by.setdefault(x['fixture'],[]).append(x)
  for name,records in by.items():
   pics=[]
   for x in records:
    c,r=x['size'];f=P/'sheet-cells'/f'{leaf}--{Path(name).stem}--{mode}--{c}x{r}.png';pics.append((f'{c}x{r}'+(' MIN' if x['isMin'] else ''),Image.open(f).convert('RGB')))
   col=max(p.width for _,p in pics)+16;rows=[pics[i:i+2] for i in range(0,len(pics),2)];hs=[max(p.height for _,p in row)+30 for row in rows];im=Image.new('RGB',(col*2,sum(hs)+28),'#e4e7eb' if mode=='light' else '#30343b');draw=ImageDraw.Draw(im);draw.text((8,7),leaf+' / '+name+' / '+mode,fill='#222222' if mode=='light' else '#ffffff');y=28
   for row,h in zip(rows,hs):
    for k,(lab,pic) in enumerate(row):draw.text((k*col+8,y+2),lab,fill='#222222' if mode=='light' else '#ffffff');im.paste(pic,(k*col+6,y+20))
    y+=h
   im.save(D/f'{leaf}--{Path(name).stem}--{mode}.png')
 print(leaf,'review grids',len(by)*len(j['modes']))
