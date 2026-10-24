"""Prepare current unreviewed sheets. This script never records acceptance."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib,sys
R=Path('/workspace/work/rebuild');out=R/'root-sheet-pairs';out.mkdir(exist_ok=True)
data=json.loads((R/'root-final-review.json').read_text());take=int(sys.argv[1])if len(sys.argv)>1 else 2;items=[]
for n in json.loads((R/'profiles.json').read_text()):
 for f in sorted((R/n/n/'elements').iterdir()):
  leaf=f.name
  v=R/n/'review';paths=[v/'sheets'/(leaf+'-'+m+'.png')for m in ['light','dark']]
  old=data.get(n,{}).get('elements',{}).get(leaf,{})
  hashes={m:hashlib.sha256(p.read_bytes()).hexdigest() for m,p in zip(['light','dark'],paths)}
  if old.get('status')=='pass' and old.get('sheet_sha256')==hashes:continue
  if len(items)>=take:break
  panes=[]
  for p,m in zip(paths,['LIGHT','DARK']):
   im=Image.open(p).convert('RGB');im=im.resize((2048,round(im.height*2048/im.width)));pane=Image.new('RGB',(2048,im.height+28),'#d9d9df');ImageDraw.Draw(pane).text((8,7),n+'/'+leaf+' '+m,fill='#111');pane.paste(im,(0,28));panes.append(pane)
  canvas=Image.new('RGB',(2048,sum(p.height for p in panes)),'white');y=0
  for im in panes:canvas.paste(im,(0,y));y+=im.height
  p=out/(n+'-'+leaf+'.png');canvas.save(p);items.append({'id':n+'/'+leaf,'pair':str(p),'height':canvas.height})
 if len(items)>=take:break
print(json.dumps(items))
