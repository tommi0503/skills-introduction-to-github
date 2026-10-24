"""Position-aware text contrast, without the prior 'worst gradient stop' approximation."""
import io
import numpy as np
from PIL import Image
from scipy.ndimage import maximum_filter
TEXT_JS=r'''()=>{const cv=document.createElement('canvas'),ctx=cv.getContext('2d');let out=[];for(let e of document.querySelectorAll('.slide *')){let s=getComputedStyle(e),r=e.getBoundingClientRect();if(s.display==='none'||s.visibility==='hidden'||+s.opacity===0||!r.width||!r.height)continue;for(let n of e.childNodes)if(n.nodeType===3&&n.textContent.trim()){let q=document.createRange();q.selectNodeContents(n);ctx.clearRect(0,0,1,1);ctx.fillStyle=s.color;ctx.fillRect(0,0,1,1);let c=[...ctx.getImageData(0,0,1,1).data];for(let t of q.getClientRects())if(t.width&&t.height)out.push({text:n.textContent.trim(),selector:e.className?.baseVal??e.className,color:c,size:parseFloat(s.fontSize),rect:[t.x,t.y,t.width,t.height],gradientText:s.backgroundClip==='text'||s.webkitBackgroundClip==='text'})}}return out}'''
def luminance(v):
 z=v/255.;z=np.where(z<=.04045,z/12.92,((z+.055)/1.055)**2.4);return z[...,0]*.2126+z[...,1]*.7152+z[...,2]*.0722

def audit(page,foreground,clip):
 texts=page.evaluate(TEXT_JS)
 hide=page.add_style_tag(content='.slide *{-webkit-text-fill-color:transparent!important;text-shadow:none!important;-webkit-text-stroke:0 transparent!important}')
 originals=page.evaluate('''()=>{let a=[];for(let e of document.querySelectorAll('.slide *')){let s=getComputedStyle(e);if(s.backgroundClip==='text'||s.webkitBackgroundClip==='text'){a.push([e,e.getAttribute('style')]);e.style.setProperty('background-image','none','important')}}window.__contrastTextBackgrounds=a;return a.length}''')
 bg=page.screenshot(clip=clip,animations='disabled');hide.evaluate('(e)=>e.remove()');page.evaluate('''()=>{for(let[e,s]of window.__contrastTextBackgrounds){if(s===null)e.removeAttribute('style');else e.setAttribute('style',s)}delete window.__contrastTextBackgrounds}''')
 a=np.asarray(Image.open(io.BytesIO(foreground)).convert('RGB')).astype(float);b=np.asarray(Image.open(io.BytesIO(bg)).convert('RGB')).astype(float);errors=[];checked=0
 for t in texts:
  x,y,w,h=t['rect'];x0=max(0,int(x-clip['x']));y0=max(0,int(y-clip['y']));x1=min(a.shape[1],int(np.ceil(x+w-clip['x'])));y1=min(a.shape[0],int(np.ceil(y+h-clip['y'])))
  if x1<=x0 or y1<=y0:continue
  fg=a[y0:y1,x0:x1];ground=b[y0:y1,x0:x1];strength=np.max(np.abs(fg-ground),axis=2);local=maximum_filter(strength,size=3);mask=(strength>12)&(strength>=local*.85)
  if np.count_nonzero(mask)<2:continue
  bg_lum=luminance(ground)[mask]
  if t['gradientText'] or t['color'][3]==0:fg_lum=luminance(fg)[mask]
  else:
   c=np.array(t['color'][:3],float);alpha=t['color'][3]/255.;ideal=c*alpha+ground[mask]*(1-alpha);fg_lum=luminance(ideal)
  ratios=(np.maximum(fg_lum,bg_lum)+.05)/(np.minimum(fg_lum,bg_lum)+.05);ratio=float(np.quantile(ratios,.05));limit=3 if t['size']>=28 else 4.5;checked+=1
  if ratio<limit-.08:errors.append({'text':t['text'][:120],'selector':t['selector'],'ratio':round(ratio,2),'required':limit,'rect':t['rect'],'gradientText':t['gradientText']})
 chips=page.evaluate("""()=>[...document.querySelectorAll('.slide .tag,.slide .mark,.slide .pill>.parts')].filter(e=>e.textContent.trim()&&!e.querySelector('[data-icon]')).map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return {text:e.textContent.trim().slice(0,100),rect:[r.x,r.y,r.width,r.height],selector:e.className,visible:s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0}}).filter(x=>x.visible)""")
 ink_centers=[]
 for chip in chips:
  x,y,w,h=chip['rect'];x0=max(0,int(x-clip['x']));y0=max(0,int(y-clip['y']));x1=min(a.shape[1],int(np.ceil(x+w-clip['x'])));y1=min(a.shape[0],int(np.ceil(y+h-clip['y'])))
  if x1<=x0 or y1<=y0:continue
  mask=np.max(np.abs(a[y0:y1,x0:x1]-b[y0:y1,x0:x1]),axis=2)>20
  yy,xx=np.where(mask)
  if len(xx)<2:continue
  ix=x0+clip['x']+(int(xx.min())+int(xx.max())+1)/2;iy=y0+clip['y']+(int(yy.min())+int(yy.max())+1)/2
  ink_centers.append({**chip,'inkOffsetX':round(ix-x-w/2,2),'inkOffsetY':round(iy-y-h/2,2)})
 return {'chipInkCenters':ink_centers,'checkedTextRanges':checked,'failures':errors,'method':'Actual glyph positions over a second screenshot with text fill hidden. Flat foregrounds use computed CSS color; clipped-gradient text uses core glyph pixels. 5th percentile background contrast, not all possible gradient stops.'}
