from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import math,re
B=Path(__file__).parent;C=B.parent/'anchor-frame'
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13)
for p in sorted((B/'library').glob('*/*.png')):
 src=Image.open(p).convert('RGB')
 if src.size==(1280,720):continue
 count=src.height//390; assert src.width==1280 and src.height==count*390
 folder=p.parent.name;d=C/('foundation' if folder=='foundation' else 'elements/'+folder)
 fixtures=sorted((d/'fixtures').glob('*.html'));assert len(fixtures)==count
 cols=1 if count<=3 else 2;rows=math.ceil(count/cols);cw=1280/cols;ch=720/rows
 out=Image.new('RGB',(1280,720),'#e5e8ec');draw=ImageDraw.Draw(out)
 for j,f in enumerate(fixtures):
  x=int(j%cols*cw);y=int(j//cols*ch);text=f'{folder} / {f.stem} | 12x6 / minimum'
  draw.text((x+10,y+8),text,font=font,fill='#171b20')
  for k,(left,right) in enumerate([(4,634),(644,1274)]):
   tile=src.crop((left,j*390+30,right,j*390+384));bound=(int(cw/2)-16,int(ch)-42);tile=ImageOps.contain(tile,bound,Image.Resampling.LANCZOS)
   xx=x+int(k*cw/2+(cw/2-tile.width)/2);yy=y+32+int((ch-42-tile.height)/2);out.paste(tile,(xx,yy))
 out.save(p)
print('normalized',len(list((B/'library').glob('*/*.png'))),'sheets to 1280x720; aspect ratios preserved')
