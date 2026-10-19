from pathlib import Path
from PIL import Image,ImageDraw
from concurrent.futures import ProcessPoolExecutor
import sys

def compare(job):
 p,round,mode=job;d,s=p.stem.split('-');ref=Path(f'public/references/{d}/slide_{s}.png');a=Image.open(ref).convert('RGB');b=Image.open(p).convert('RGB');c=Image.new('RGB',(2560,760),'#edf1f4');c.paste(a,(0,40));c.paste(b,(1280,40));draw=ImageDraw.Draw(c);draw.text((15,12),f'{d} / {s}   ORIGINAL',fill='black');draw.text((1295,12),f'{mode.upper()} / {round}',fill='black');c.save(Path(f'comparisons/{round}')/(p.stem+'.jpg'),quality=90)

if __name__=='__main__':
 round=sys.argv[1] if len(sys.argv)>1 else 'round1';mode=sys.argv[2] if len(sys.argv)>2 else 'clone';Path(f'comparisons/{round}').mkdir(parents=True,exist_ok=True)
 jobs=[(p,round,mode) for p in sorted(Path(f'renders/{round}/{mode}').glob('*.png'))]
 with ProcessPoolExecutor(max_workers=4) as pool:list(pool.map(compare,jobs))
 print(f'{len(jobs)} individual comparisons written')
