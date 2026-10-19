from PIL import Image,ImageDraw
from pathlib import Path
import sys,json
root=Path(__file__).resolve().parent.parent
round=next((x.split('=')[1] for x in sys.argv if x.startswith('--round=')),'round1')
ids=[x for x in sys.argv[1:] if x.isdigit()]
for d in sorted((root/'public/reference').iterdir()):
 if not d.is_dir() or ids and d.name not in ids:continue
 dest=root/'comparisons'/round/d.name;dest.mkdir(parents=True,exist_ok=True)
 for ref in sorted(d.glob('*.jpg')):
  n=ref.stem.split('_')[1];result=root/f'renders/{round}/replica/{d.name}-{n}.png'
  if not result.exists():continue
  original=Image.open(ref).convert('RGB').resize((1280,720),Image.Resampling.LANCZOS);render=Image.open(result).convert('RGB')
  board=Image.new('RGB',(2560,752),'#eee');board.paste(original,(0,32));board.paste(render,(1280,32));dr=ImageDraw.Draw(board);dr.text((20,10),f'{d.name}-{n} ORIGINAL',fill='#111');dr.text((1300,10),'IMPLEMENTATION',fill='#111');board.save(dest/f'{n}.jpg',quality=92)
print('Comparisons ready')
