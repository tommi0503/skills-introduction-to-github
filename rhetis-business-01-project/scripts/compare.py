from pathlib import Path
from PIL import Image,ImageDraw
import sys,json
root=Path(__file__).resolve().parents[1]
round=sys.argv[1] if len(sys.argv)>1 else 'final'
ids=sys.argv[2:]
out=root/'comparisons'/round;out.mkdir(parents=True,exist_ok=True)
files=sorted((root/'renders'/round/'clone').glob('*.png'))
for p in files:
 deck,slide=p.stem.split('-')
 if ids and deck not in ids:continue
 ref=root/'public'/'reference'/deck/f'slide_{slide[1:]}.png'
 canvas=Image.new('RGB',(2560,756),'#d9dde0');d=ImageDraw.Draw(canvas)
 d.text((15,10),f'ORIGINAL {deck}/{slide}',fill='#111');d.text((1295,10),'RECREATED / editable HTML + CSS',fill='#111')
 canvas.paste(Image.open(ref).convert('RGB'),(0,36));canvas.paste(Image.open(p).convert('RGB'),(1280,36));canvas.save(out/(p.stem+'.jpg'),quality=92)
print('Comparisons:',len(list(out.glob('*.jpg'))))
