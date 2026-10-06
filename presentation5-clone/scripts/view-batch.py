"""Prepare separate readable comparison images; does not compose a sheet."""
import pathlib,sys,hashlib
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1]
stage,deck,*slides=sys.argv[1:]
out=pathlib.Path('/tmp/presentation5-root-view');out.mkdir(exist_ok=True)
for slide in slides:
 p=root/'comparisons'/stage/f'{deck}-{slide}.jpg'
 target=out/f'{p.stem}-{hashlib.sha256(p.read_bytes()).hexdigest()[:12]}.jpg'
 with Image.open(p) as im:
  im.resize((1800,round(im.height*1800/im.width)),Image.Resampling.LANCZOS).save(target,quality=96)
 print(target)
