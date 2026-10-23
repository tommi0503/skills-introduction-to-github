from PIL import Image,ImageDraw
from pathlib import Path
import json,math
r=Path('/workspace/work/deliverables/skylight-review/library');src=Path('/workspace/work/agents/038/fixtures');data=json.load(open('/workspace/work/agents/038/library-metadata.json'))
for theme in ['light','dark']:
 names=sorted(set(x['name'] for x in data))
 for name in names:
  rows=[x for x in data if x['theme']==theme and x['name']==name];w=1280;h=math.ceil(len(rows)/2)*388
  im=Image.new('RGB',(w,h),'#eee' if theme=='light' else '#242424');draw=ImageDraw.Draw(im)
  for j,d in enumerate(rows):
   x=(j%2)*640;y=(j//2)*388;im.paste(Image.open(src/(theme+'-'+str(d['i']).zfill(3)+'.png')).convert('RGB').resize((640,360)),(x,y+28));draw.text((x+10,y+7),d['title'],fill='black' if theme=='light' else 'white')
  out=r/name;out.mkdir(exist_ok=True);im.save(out/(theme+'.png'))
