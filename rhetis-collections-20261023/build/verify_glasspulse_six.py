import json
from pathlib import Path
import numpy as np
from PIL import Image
SRC=next(Path('/workspace/work/deck').glob('*/006*'))/'slide_06.png'
DST=Path('/workspace/output/glasspulse-review/reassembled/slide-06.png')
def bbox(a,roi,kind):
 x1,y1,x2,y2=roi;b=a[y1:y2,x1:x2].astype(int)
 if kind=='blue':m=(b[:,:,2]-b[:,:,0]>=15)&(b[:,:,2]>=50)&(b[:,:,1]>=35)
 elif kind=='white':m=(b.min(2)>170)
 elif kind=='gray':m=(b.max(2)-b.min(2)<20)&(b.min(2)>45)
 ys,xs=np.where(m)
 if not len(xs):return None
 return [int(xs.min()+x1),int(ys.min()+y1),int(xs.max()+x1+1),int(ys.max()+y1+1)]
def runbox(a,roi,kind,minrun):
 x1,y1,x2,y2=roi;b=a[y1:y2,x1:x2].astype(int)
 if kind=='blue':m=(b[:,:,2]-b[:,:,0]>=15)&(b[:,:,2]>=50)&(b[:,:,1]>=35)
 else:m=(b.max(2)-b.min(2)<20)&(b.min(2)>45)
 found=[]
 for y,row in enumerate(m):
  transitions=np.diff(np.r_[False,row,False].astype(int));starts=np.where(transitions==1)[0];ends=np.where(transitions==-1)[0]
  if not len(starts):continue
  k=np.argmax(ends-starts)
  if ends[k]-starts[k]>=minrun:found.append((starts[k]+x1,y+y1,ends[k]+x1))
 if not found:return None
 return [int(min(q[0] for q in found)),int(min(q[1] for q in found)),int(max(q[2] for q in found)),int(max(q[1] for q in found)+1)]
def measure(p):
 a=np.array(Image.open(p).convert('RGB'))
 return {'title_ink':bbox(a,(400,100,880,180),'white'),'bar1_fill':runbox(a,(130,260,1020,380),'blue',400),'bar2_fill':runbox(a,(130,380,800,500),'gray',200)}
a=measure(SRC);b=measure(DST);report={'original':a,'reassembled':b,'absolute_edge_delta':{k:[abs(x-y) for x,y in zip(a[k],b[k])] if a[k] and b[k] else None for k in a}}
print(json.dumps(report,ensure_ascii=False,indent=2))
Path('/workspace/work/integration/glasspulse-six-visual-measurements.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
