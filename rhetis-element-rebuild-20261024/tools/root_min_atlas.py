from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,sys
R=Path('/workspace/work/rebuild');F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
leaf=sys.argv[1];names=sys.argv[2:]or['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark'];out=R/'root-final-minima'/leaf;out.mkdir(parents=True,exist_ok=True)
for mode in ['light','dark']:
 canvas=Image.new('RGB',(1600,1400),'#dedee5');d=ImageDraw.Draw(canvas);x=y=8;rh=0;idx=0;paths=[]
 def flush():
  global canvas,d,x,y,rh,idx
  if y+rh<=8:return
  p=out/f'{mode}-{idx:02}.png';canvas.crop((0,0,1600,y+rh+8)).save(p);paths.append(str(p));idx+=1;canvas=Image.new('RGB',(1600,1400),'#dedee5');d=ImageDraw.Draw(canvas);x=y=8;rh=0
 for n in names:
  q=json.loads((R/n/'review/validation'/(leaf+'.json')).read_text())
  for a in q['cases']:
   if a['mode']!=mode or not a['minimum']:continue
   w,h=a['grid'];p=R/n/'build/cells'/leaf/f"{a['fixture']}-{mode}-{w}x{h}.png";im=Image.open(p);cw,ch=im.size;pw=max(200,cw)
   if x+pw+8>1600:x=8;y+=rh+8;rh=0
   if y+ch+48>1400:flush()
   d.text((x,y),n+' '+a['fixture'],font=F,fill='#111');d.text((x,y+16),f'{w}x{h} MIN',font=F,fill='#111');canvas.paste(im,(x,y+32));x+=pw+8;rh=max(rh,ch+32)
 flush();print('\n'.join(paths))
