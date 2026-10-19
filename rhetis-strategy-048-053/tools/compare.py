from pathlib import Path
from PIL import Image,ImageDraw
import sys
p=Path(__file__).resolve().parents[1];d=sys.argv[1]; ref=next((p/'public/reference').glob(d+'*'));out=p/'artifacts/comparisons'/d;out.mkdir(parents=True,exist_ok=True)
for f in sorted(ref.glob('*.png')):
 result=p/'artifacts/direct'/d/f'{d}-{f.stem[-2:]}.png'
 if not result.exists():continue
 im=Image.new('RGB',(2560,760),'#e2e5e9');im.paste(Image.open(f),(0,40));im.paste(Image.open(result),(1280,40));dr=ImageDraw.Draw(im);dr.text((20,12),f'ORIGINAL {d} {f.stem}',fill='black');dr.text((1300,12),'RECONSTRUCTED',fill='black');im.save(out/f'{d}-{f.stem[-2:]}.jpg',quality=90)
