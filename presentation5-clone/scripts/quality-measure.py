"""Compare selected text regions at identical page scale; never changes artwork.

Example: python scripts/quality-measure.py p004 s02-01 --round final
  --region title:80:90:700:200 --region body:80:320:700:160
Choose text-only regions; a silhouette measurement cannot identify a font.
"""
import argparse,json,pathlib
from PIL import Image,ImageOps,ImageChops,ImageStat

root=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('deck');p.add_argument('slide')
p.add_argument('--round',default='final');p.add_argument('--region',action='append',required=True)
p.add_argument('--threshold',type=int,default=45);p.add_argument('--output')
a=p.parse_args()
with Image.open(root/'public/reference'/a.deck/(a.slide+'.jpg')) as image:
 reference=Image.new('RGB',(1280,720),'white');contained=ImageOps.contain(image.convert('RGB'),(1280,720),Image.Resampling.LANCZOS)
 reference.paste(contained,((1280-contained.width)//2,(720-contained.height)//2))
render=Image.open(root/'renders'/a.round/f'{a.deck}-{a.slide}.png').convert('RGB')
def measure(im,rect):
 x,y,w,h=rect;crop=im.crop((x,y,x+w,y+h))
 # Dominant quantized color estimates the flat paragraph background.
 dominant=max(crop.quantize(colors=16).convert('RGB').getcolors(w*h),key=lambda v:v[0])[1]
 foreground=ImageChops.difference(crop,Image.new('RGB',crop.size,dominant))
 foreground=foreground.convert('RGB').point(lambda c:255 if c>=a.threshold else 0).convert('L').point(lambda c:255 if c else 0)
 rows=[sum(v>0 for v in foreground.crop((0,i,w,i+1)).getdata()) for i in range(h)]
 bands=[];start=None
 for i,count in enumerate(rows+[0]):
  if count>=3 and start is None:start=i
  if count<3 and start is not None:
   if i-start>=2:bands.append([y+start,y+i-1])
   start=None
 bounds=foreground.getbbox()
 return {'estimatedBackground':dominant,'inkBounds':None if bounds is None else [x+bounds[0],y+bounds[1],x+bounds[2],y+bounds[3]],
  'rowBands':bands,'inkPixelCount':sum(v>0 for v in foreground.getdata())}
report={'deck':a.deck,'slide':a.slide,'round':a.round,'threshold':a.threshold,'regions':[]}
for region in a.region:
 name,*numbers=region.split(':');assert len(numbers)==4
 rect=list(map(int,numbers));report['regions'].append({'name':name,'region':rect,'original':measure(reference,rect),'render':measure(render,rect)})
text=json.dumps(report,ensure_ascii=False,indent=2)
if a.output:pathlib.Path(a.output).write_text(text+'\n')
print(text)
