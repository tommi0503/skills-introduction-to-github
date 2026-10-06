"""Show one original/render pair for individual review, never a contact sheet."""
import pathlib,sys,json
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1]
if len(sys.argv)<3:raise SystemExit('python scripts/view.py p01 s11 [final|round1|round2]')
deck,slide=sys.argv[1:3];stage=sys.argv[3] if len(sys.argv)>3 else 'final'
p=root/'comparisons'/stage/f'{deck}-{slide}.jpg'
if not p.exists():raise SystemExit(f'Missing capture: {p}')
im=Image.open(p);im.resize((1800,round(im.height*1800/im.width)),Image.Resampling.LANCZOS).save('/tmp/presentation4-individual.jpg',quality=95)
print(p)
