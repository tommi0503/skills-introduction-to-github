import json,numpy as np
from PIL import Image,ImageOps
D=json.load(open('src/decks/group-b-data.json'));R={}
for k,p in D.items():
 if not k.startswith('p069'):continue
 e=next(e for e in p['elements'] if e['kind']=='text' and e['size']>50 and not e['text'][0].isdigit() and e['text'][0]!='$')
 x=max(0,int(e['x']*12.8)-25);y=max(65,int(e['y']*7.2)-25);w=min(1280-x,int(e['w']*12.8)+40);h=min(720-y,int(e['size']*1.4))
 ref=ImageOps.pad(Image.open('public/reference/'+k+'.jpg').convert('RGB'),(1280,720),method=Image.Resampling.LANCZOS,color='white');png=Image.open('renders/final/'+k.replace('/','-')+'.png')
 rec={'region':[x,y,w,h]}
 for name,im in [('source',ref),('baseline',png)]:
  a=np.array(im.crop((x,y,x+w,y+h)))[:,:,:3]; mask=(a.min(2)>210)&(a.max(2)-a.min(2)<35) if e['color']=='#fff' else (a.max(2)<115)
  rows=mask.sum(1)>12;bands=[];st=None
  for i,v in enumerate(list(rows)+[False]):
   if v and st is None:st=i
   if not v and st is not None:
    if i-st>8:bands.append((st,i))
    st=None
  if bands:
   lo,hi=bands[0];ys,xs=np.where(mask[lo:hi]);rec[name]=[x+int(xs.min()),y+lo,x+int(xs.max())+1,y+hi]
 rec['text']=e['text'].split('\n')[0];R[k]=rec
json.dump(R,open('review/quality/group-b-p069-title-metrics.json','w'),indent=2)
for k,v in R.items(): print(k,v)
