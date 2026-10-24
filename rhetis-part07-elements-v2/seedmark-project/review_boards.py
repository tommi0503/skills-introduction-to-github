from pathlib import Path
from PIL import Image,ImageDraw
import json,math
P=Path(__file__).parent;O=P/'visual-review';O.mkdir(exist_ok=True)
for f in (P/'sheets').glob('*-checks.json'):
 d=json.loads(f.read_text());leaf=d['leaf']
 for mode,cells in d['modes'].items():
  names=list(dict.fromkeys(x['fixture']for x in cells));rows=[]
  for name in names:
   qs=[q for q in cells if q['fixture']==name];pics=[]
   for q in qs:
    c,r=q['size'];im=Image.open(P/'sheet-cells'/f'{leaf}--{Path(name).stem}--{mode}--{c}x{r}.png').convert('RGB');im.thumbnail((290,180));pics.append((q,im))
   h=max(p.height for q,p in pics)+42;row=Image.new('RGB',(len(pics)*300,h),'#e3e6e9'if mode=='light'else'#36383b');dr=ImageDraw.Draw(row)
   for j,(q,im)in enumerate(pics):
    dr.text((j*300+4,4),f'{name[:24]} {q["size"]}'+(' MIN'if q['isMin']else''),fill='#111'if mode=='light'else'#fff');row.paste(im,(j*300+4,28))
   rows.append(row)
  # Separate parts keep every rendered size visible at a useful scale.
  for part in range(math.ceil(len(rows)/4)):
   rs=rows[part*4:part*4+4];im=Image.new('RGB',(max(r.width for r in rs),sum(r.height for r in rs)),'#ccd1d6');y=0
   for r in rs:im.paste(r,(0,y));y+=r.height
   im.save(O/f'{leaf}-{mode}-{part+1}.png')
print('boards',len(list(O.glob('*.png'))))
