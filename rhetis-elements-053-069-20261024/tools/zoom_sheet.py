"""Readable primary-review crops from existing audited sheets, without new rendering."""
import json,math,argparse
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
SIZES=['12x6','12x3','9x4','8x6','6x6','6x3','4x4','4x3','3x3']
def main(cid,leaf):
 R=ROOT/(cid+'-review');a=json.loads((R/'audits'/(leaf+'.json')).read_text());out=ROOT/'.sheet-work/zoom';out.mkdir(exist_ok=True,parents=True)
 for mode in ['light','dark']:
  states=[s for s in a['states']if s['mode']==mode];groups={}
  for s in states:groups.setdefault(s['fixture'],[]).append(s)
  cols=SIZES+sorted({s['size']for s in states if s['size']not in SIZES});widths={k:max([math.ceil(s['slot']['x']+s['slot']['w']+6)-math.floor(s['slot']['x']-6)for s in states if s['size']==k]or[80])for k in cols};xs={};x=210
  for k in cols:xs[k]=x;x+=widths[k]+12
  im=Image.open(R/'sheets'/(leaf+'-'+mode+'.png'));y=40;parts=[]
  for name,ss in groups.items():
   rh=max(math.ceil(s['slot']['y']+s['slot']['h']+6)-math.floor(s['slot']['y']-6)for s in ss)+38;minimum=next(s['size']for s in ss if s['minimum']);first=im.crop((0,y,210+widths['12x6'],y+rh));small=im.crop((xs[minimum],y,xs[minimum]+widths[minimum],y+rh));part=Image.new('RGB',(first.width+small.width+20,rh),'#e6e8ed');part.paste(first,(0,0));part.paste(small,(first.width+20,0));parts.append(part);y+=rh
  for n in range(0,len(parts),3):
   batch=parts[n:n+3];z=Image.new('RGB',(max(p.width for p in batch),sum(p.height for p in batch)),'#e6e8ed');y=0
   for p in batch:z.paste(p,(0,y));y+=p.height
   p=out/f'{cid}-{leaf}-{mode}-{n//3:02}.png';z.save(p);print(str(p))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('collection');p.add_argument('leaf');a=p.parse_args();main(a.collection,a.leaf)
