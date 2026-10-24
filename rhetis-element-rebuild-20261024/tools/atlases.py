from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,sys,hashlib
R=Path('/workspace/work/rebuild');F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
def build(n,leaf):
 D=R/n/'build';qa=json.loads((R/n/'review/validation'/(leaf+'.json')).read_text());out=D/'native-atlas'/leaf;out.mkdir(parents=True,exist_ok=True);manifest=[]
 for fixture in sorted(set(x['fixture']for x in qa['cases'])):
  for mode in ['light','dark']:
   cells=[]
   for a in qa['cases']:
    if a['fixture']!=fixture or a['mode']!=mode:continue
    x,y=a['grid'];p=D/'cells'/leaf/f'{fixture}-{mode}-{x}x{y}.png';im=Image.open(p).convert('RGB');cells.append((a,im,p))
   panels=[];canvas=Image.new('RGB',(1600,1400),'#e2e2e7');draw=ImageDraw.Draw(canvas);x=8;y=34;rowh=0;num=0;items=[]
   def flush():
    nonlocal canvas,draw,x,y,rowh,num,items
    if not items:return
    h=y+rowh+8;p=out/f'{fixture}-{mode}-{num:02d}.png';canvas.crop((0,0,1600,h)).save(p,optimize=True);manifest.append({'atlas':str(p),'cells':items,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()});num+=1;canvas=Image.new('RGB',(1600,1400),'#e2e2e7');draw=ImageDraw.Draw(canvas);x=8;y=34;rowh=0;items=[]
   for a,im,p in cells:
    w,h=im.size
    if x+w+8>1600:x=8;y+=rowh+8;rowh=0
    if y+h+30>1400:flush()
    draw.text((x,y),f'{n}/{leaf} {fixture} {mode} '+str(a['grid'])+(' MIN'if a['minimum']else''),font=F,fill='#111');canvas.paste(im,(x,y+24));items.append(str(p));rowh=max(rowh,h+24);x+=w+8
   flush()
 (D/'native-atlas'/(leaf+'.json')).write_text(json.dumps(manifest,indent=2));return manifest
if __name__=='__main__':
 for item in build(sys.argv[1],sys.argv[2]):print(item['atlas'])
