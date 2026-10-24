"""Native-pixel review panels, deduplicating only byte-identical cell PNGs."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib,sys
R=Path('/workspace/work/rebuild');F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13)
def build(n,leaf):
 d=R/n/'build';q=json.loads((R/n/'review/validation'/(leaf+'.json')).read_text());seen={};items=[]
 for a in q['cases']:
  x,y=a['grid'];p=d/'cells'/leaf/f"{a['fixture']}-{a['mode']}-{x}x{y}.png";h=hashlib.sha256(p.read_bytes()).hexdigest();key=(h,tuple(Image.open(p).size))
  if key in seen:seen[key]['also'].append([a['fixture'],a['mode'],a['grid']]);continue
  e={'file':str(p),'sha256':h,'also':[],'label':a['mode']+' '+str(a['grid'])+' '+a['fixture']};seen[key]=e;items.append(e)
 out=d/'root-native'/leaf;out.mkdir(parents=True,exist_ok=True);canvas=None;x=y=row=0;num=0;panels=[];covered=[]
 def new():return Image.new('RGB',(1600,1400),'#dedee5')
 canvas=new();draw=ImageDraw.Draw(canvas);x=8;y=8
 def flush():
  nonlocal canvas,draw,x,y,row,num,covered
  if not covered:return
  p=out/f'{num:03}.png';canvas.crop((0,0,1600,y+row+8)).save(p);panels.append({'file':str(p),'cells':covered,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()});num+=1;canvas=new();draw=ImageDraw.Draw(canvas);x=y=8;row=0;covered=[]
 for a in items:
  im=Image.open(a['file']).convert('RGB');w,h=im.size;pw=max(w,220)
  if x+pw+8>1600:x=8;y+=row+8;row=0
  if y+h+44>1400:flush()
  draw.text((x,y),n+'/'+leaf,font=F,fill='#111');draw.text((x,y+17),a['label'],font=F,fill='#111');canvas.paste(im,(x,y+36));covered.append(a);x+=pw+8;row=max(row,h+36)
 flush();(out/'manifest.json').write_text(json.dumps({'cases':len(q['cases']),'unique':len(items),'panels':panels},indent=2));print(n,leaf,len(q['cases']),len(items),len(panels),flush=True)
 return panels
if __name__=='__main__':build(sys.argv[1],sys.argv[2])
