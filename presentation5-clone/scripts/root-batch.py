"""Prepare four separate comparisons for actual root inspection, never a sheet."""
import json,pathlib,sys
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1]
mode=sys.argv[1];plan=json.loads((root/'review/root-integration-plan.json').read_text())
journal=json.loads((root/'review/root-review-journal.json').read_text())
pending=[]
for s in plan:
 key=f'{s["deck"]}/{s["slide"]}'
 if key in journal:continue
 pair=root/'comparisons/final'/f'{s["deck"]}-{s["slide"]}.jpg'
 if pair.exists():pending.append(s)
if mode=='prepare':
 batch=pending[:4];out=pathlib.Path('/tmp/presentation5-root-view');out.mkdir(exist_ok=True)
 for s in batch:
  p=root/'comparisons/final'/f'{s["deck"]}-{s["slide"]}.jpg'
  with Image.open(p) as im:im.resize((1800,round(im.height*1800/im.width)),Image.Resampling.LANCZOS).save(out/p.name,quality=96)
 (root/'review/root-active-batch.json').write_text(json.dumps(batch)+'\n')
 print(json.dumps({'remainingAvailable':len(pending),'batch':batch}))
elif mode=='record':
 import subprocess
 batch=json.loads((root/'review/root-active-batch.json').read_text())
 for s in batch:
  subprocess.run([sys.executable,str(root/'scripts/record-root-review.py'),s['deck'],s['slide'],'--note',sys.argv[2]],check=True)
else:raise ValueError(mode)
