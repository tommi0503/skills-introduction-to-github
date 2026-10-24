from pathlib import Path
from PIL import Image,ImageDraw
import json,sys
from review_queue import pending
R=Path('/workspace/work/rebuild');out=R/'root-sheet-pairs';out.mkdir(exist_ok=True)
data=pending(int(sys.argv[1])if len(sys.argv)>1 else 6)
for a in data:
 ims=[]
 for mode,p in zip(['LIGHT','DARK'],a['paths']):
  im=Image.open(p).convert('RGB');im=im.resize((2048,round(im.height*2048/im.width)))
  pane=Image.new('RGB',(2048,im.height+28),'#d9d9df');ImageDraw.Draw(pane).text((8,7),a['collection']+'/'+a['leaf']+' '+mode,fill='#111');pane.paste(im,(0,28));ims.append(pane)
 canvas=Image.new('RGB',(2048,sum(i.height for i in ims)),'white');y=0
 for im in ims:canvas.paste(im,(0,y));y+=im.height
 target=out/(a['collection']+'-'+a['leaf']+'.png');canvas.save(target);a['pair']=str(target)
print(json.dumps(data))
