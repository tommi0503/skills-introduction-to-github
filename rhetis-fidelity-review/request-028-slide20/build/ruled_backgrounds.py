"""Trace only the deck's ruled fan decoration into sparse vector line primitives.
No source image, text, chart or photograph is embedded in the SVG.
Each stripe is a vertical path with a sampled, smoothed linear opacity gradient.
"""
from pathlib import Path
from PIL import Image
from scipy.ndimage import minimum_filter1d,median_filter,gaussian_filter1d
from scipy.signal import find_peaks
import numpy as np,json
B=Path(__file__).resolve().parents[1];SRC=next(Path('/workspace/work/images').glob('*/028*'))
REGIONS={1:[(0,0,920,560)],2:[(0,220,631,720)],3:[(700,0,1280,515)],4:[(0,365,360,720)],5:[(940,0,1280,335)],6:[(1066,0,1280,720)],7:[(650,0,1280,381)],8:[(920,0,1280,446)],9:[(835,0,1280,720)],10:[(230,474,486,720)],11:[(0,377,419,720)],12:[(0,205,340,720)],13:[(980,210,1280,720)],14:[(921,563,1280,720)],15:[(0,0,504,400)],16:[(1087,340,1280,720)],17:[(0,308,490,720)],18:[(0,200,631,720)],19:[(1012,0,1280,211)],20:[(0,295,358,720),(358,633,537,720)],21:[(986,0,1280,211)],22:[(1060,632,1280,720)]}
def trace(n):
 im=np.array(Image.open(SRC/f'slide_{n:02}.png').convert('RGB')).astype(float);dark=n in [2,5,7,15,18];r,g,b=im[:,:,0],im[:,:,1],im[:,:,2]
 # Chroma isolates the repeated ruled lines; neutral live text is excluded.
 a=np.maximum(0,(58-(b-r))/58) if dark else np.maximum(0,(b-r)/98)
 if dark:a*=np.clip((r-158)/65,0,1)
 mask=np.zeros(a.shape,dtype=bool)
 for x,y,rr,bb in REGIONS.get(n,[]):mask[y:bb,x:rr]=True
 a*=mask
 # A solid surface has no repeating high-frequency variation across x.
 hp=np.maximum(0,a-minimum_filter1d(a,size=7,axis=1));signal=hp.sum(axis=0)
 period={1:9,2:7,3:5.5,4:4.3,5:4.3,6:6.5,7:6.5,8:4,9:5.2,10:7.8,11:6.8,12:5.8,13:6.2,14:5.5,15:8,16:5.5,17:5.8,18:5.2,19:3.5,20:5.3,21:5.4,22:4}.get(n,5)
 peaks,_=find_peaks(signal,distance=max(3,int(period*.75)),prominence=1)
 paths=[];defs=[];stroke='var(--ruled-ink, #ffffff)' if dark else 'var(--ruled-ink, #5c6dbe)'
 if n in [1,20]:
  cols=[(0,281,31),(281,593,34),(593,920,36)] if n==1 else [(0,179,34),(179,358,34),(358,537,34)]
  peaks=[round(start+2+(end-start)/count*j) for start,end,count in cols for j in range(count)]
 for x in peaks:
  vals=median_filter(np.clip((r[:,x]-158)/(255-158),0,1) if dark else np.clip((239-r[:,x])/(239-92),0,1),size=3);active=median_filter(a[:,x],size=3)>.018;edges=np.diff(np.r_[False,active,False].astype(int));starts=np.where(edges==1)[0];ends=np.where(edges==-1)[0]
  for y0,y1 in zip(starts,ends):
   if y1-y0<34:continue
   # Keep each repeated line as a single primitive, not a pixel mosaic.
   positions=np.unique(np.r_[y0,np.arange(y0+12,y1,24),y1-1]).astype(int)
   gid=f'f{n}-{len(paths)}';stops=''.join(f'<stop offset="{(y-y0)/max(1,y1-y0-1):.4f}" stop-color="{stroke}" stop-opacity="{min(1,vals[y]):.3f}"/>' for y in positions)
   defs.append(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{y0}" x2="0" y2="{y1-1}">{stops}</linearGradient>')
   paths.append(f'<path d="M{x+.2} {y0}V{y1}" stroke="url(#{gid})" stroke-width="{period*.64:.2f}" fill="none"/>')
 return '<svg class="decoration" aria-hidden="true" viewBox="0 0 1280 720" style="position:absolute;inset:0;width:1280px;height:720px;pointer-events:none"><defs>'+''.join(defs)+'</defs>'+''.join(paths)+'</svg>',len(paths)
if __name__=='__main__':
 out=B/'build/ruled-vectors';out.mkdir(exist_ok=True);stats={}
 for n in REGIONS:
  svg,count=trace(n);(out/f'slide_{n:02}.svg').write_text(svg);stats[n]=count
 (out/'counts.json').write_text(json.dumps(stats,indent=2));print(stats)
