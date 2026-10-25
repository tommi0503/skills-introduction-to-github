from pathlib import Path
import json,hashlib,sys
from PIL import Image,ImageDraw
Image.MAX_IMAGE_PIXELS=None
R=Path(__file__).resolve().parents[1];k=sys.argv[1];kind=sys.argv[2];p=R/f'{k}-project';out=Path('/tmp/r5-root')/k/kind;out.mkdir(parents=True,exist_ok=True)
if kind=='modes':groups=[[p/'sheets'/f'{d.name}-{m}.png' for m in ['light','dark']] for d in sorted((p/k/'elements').iterdir()) if d.is_dir()]
elif kind=='mapped':groups=[[f] for f in sorted((p/'sheets').glob('*-replica.png')) if (p/k/'elements'/f.name[:-12]).is_dir()]
elif kind=='triples':groups=[[f] for f in sorted((p/'compare-reassembled').glob('*.png'))]
elif kind=='foundation':groups=[[f] for folder in ['foundation-sheets','panel-sheets'] for f in sorted((p/folder).glob('*.png'))]
else:raise ValueError(kind)
import os
if os.environ.get('PENDING'):
 seen=json.loads((R/'root-visual-review.json').read_text())['images'];groups=[g for g in groups if not all(seen.get(str(f.relative_to(R)),{}).get('sha256')==hashlib.sha256(f.read_bytes()).hexdigest() for f in g)]
manifest={};batches=[]
for start in range(0,len(groups),4):
 selected=groups[start:start+4];thumbs=[];paths=[]
 for gg in selected:
  ims=[]
  for f in gg:
   rel=str(f.relative_to(R));manifest[rel]=hashlib.sha256(f.read_bytes()).hexdigest();paths.append(rel)
   im=Image.open(f).convert('RGB');im.thumbnail((1300,1000 if kind=='modes' else 1050));ims.append(im)
  cell=Image.new('RGB',(max(i.width for i in ims),sum(i.height for i in ims)+28),'#dae1e8');dd=ImageDraw.Draw(cell);dd.text((8,7),' / '.join(x.name for x in gg),fill='black');y=28
  for im in ims:cell.paste(im,(0,y));y+=im.height
  if kind=='modes':cell.thumbnail((1300,1500))
  thumbs.append(cell)
 # triples stacked for readable 3-column comparison, other kinds two columns
 cols=1 if kind=='triples' else 2;w=max(t.width for t in thumbs);h=max(t.height for t in thumbs)
 result=Image.new('RGB',(w*cols,h*((len(thumbs)+cols-1)//cols)),'#b7c2cf')
 for j,t in enumerate(thumbs):result.paste(t,((j%cols)*w,(j//cols)*h))
 target=out/f'{start//4+1:02d}.png';result.save(target);batches.append({'image':str(target),'paths':paths})
(out/'manifest.json').write_text(json.dumps(manifest));(out/'batches.json').write_text(json.dumps(batches));print(k,kind,len(groups),'groups',len(batches),'batches')
