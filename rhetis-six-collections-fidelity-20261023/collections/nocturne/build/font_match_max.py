"""Compare original text silhouettes with actual loaded reference fonts.
Analysis only: never stretches or changes the deliverable.
"""
from pathlib import Path
import argparse,base64,io,json,sys
import numpy as np
from PIL import Image
from scipy.ndimage import distance_transform_edt
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/workspace/work/tools')
from render_review import serve_url,browser

def tight(a):
 y,x=np.where(a>0.25)
 return a[y.min():y.max()+1,x.min():x.max()+1] if len(x) else a

def score(a,b):
 h=max(a.shape[0],b.shape[0])+8;w=max(a.shape[1],b.shape[1])+8
 aa=np.zeros((h,w));bb=aa.copy()
 aa[4:4+a.shape[0],4:4+a.shape[1]]=a
 bb[4:4+b.shape[0],4:4+b.shape[1]]=b
 best=1e9
 for dy in [-1,0,1]:
  for dx in [-1,0,1]:
   c=np.roll(bb,(dy,dx),(0,1));m=aa>.4;n=c>.4
   d=(distance_transform_edt(~m)[n].mean()+distance_transform_edt(~n)[m].mean())/2
   e=np.abs(aa-c).sum()/max(aa.sum(),1)
   best=min(best,float(d+e))
 return best

def main():
 ap=argparse.ArgumentParser();ap.add_argument('image');ap.add_argument('--crop',required=True);ap.add_argument('--text',required=True);ap.add_argument('--out',required=True);ap.add_argument('--kind',choices=['dark','light','color'],default='dark');ap.add_argument('--weights',default='400,500,600,700,800,900');a=ap.parse_args()
 out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
 crop=Image.open(a.image).convert('RGB').crop(tuple(map(int,a.crop.split(','))))
 rgb=np.array(crop)/255
 if a.kind=='dark':mask=np.clip((.85-rgb.mean(axis=2))/.7,0,1)
 elif a.kind=='light':mask=np.clip((rgb.max(axis=2)-.45)/.55,0,1)
 else:mask=np.clip((rgb.max(axis=2)-rgb.max(axis=2))/.5,0,1)
 target=tight(mask);Image.fromarray(np.uint8(target*255)).save(out/'target-mask.png')
 fonts=['Pretendard Variable','SUITE','Freesentation','Noto Sans KR','Pretendard','Do Hyeon'] if any(ord(c)>127 for c in a.text) else ['Pretendard Variable','SUITE','Freesentation','Noto Sans KR','Montserrat','Noto Sans']
 results=[]
 with sync_playwright() as p:
  b=browser(p);page=b.new_page();page.goto(serve_url(Path('/workspace/work/reference/fonts/fonts.css')))
  page.set_content('<link rel="stylesheet" href="'+serve_url(Path('/workspace/work/reference/fonts/fonts.css'))+'">')
  for fam in fonts:
   weights=[400] if fam=='Do Hyeon' else list(map(int,a.weights.split(',')))
   for weight in weights:
    page.evaluate('async ([f,w,t])=>{await document.fonts.load(`${w} 100px "${f}"`,t)}',[fam,weight,a.text])
    # Render at final pixel size; inferred from the visible glyph height.
    datum=page.evaluate('''([f,w,t])=>{let c=document.createElement('canvas');c.width=1600;c.height=180;let x=c.getContext('2d');x.font=`${w} 100px "${f}"`;x.fillText(t,4,120);return c.toDataURL()}''',[fam,weight,a.text])
    sample=tight(np.array(Image.open(io.BytesIO(base64.b64decode(datum.split(',')[1]))))[:,:,3]/255)
    guess=100*target.shape[0]/sample.shape[0]
    for size in [round(guess,1)-.5,round(guess,1),round(guess,1)+.5]:
     for spacing in [-1.5,-1,-.5,0,.5]:
      datum=page.evaluate('''([f,w,t,s,k])=>{let c=document.createElement('canvas');c.width=1600;c.height=250;let x=c.getContext('2d');x.font=`${w} ${s}px "${f}"`;x.letterSpacing=k+'px';x.fillText(t,4,180);return c.toDataURL()}''',[fam,weight,a.text,size,spacing])
      im=Image.open(io.BytesIO(base64.b64decode(datum.split(',')[1])))
      m=tight(np.array(im)[:,:,3]/255);v=score(target,m)
      results.append({'font':fam,'weight':weight,'size':size,'spacing':spacing,'score':round(v,4),'width':m.shape[1],'height':m.shape[0]})
  b.close()
 results.sort(key=lambda x:x['score']);(out/'ranking.json').write_text(json.dumps({'source':a.image,'crop':a.crop,'text':a.text,'targetSize':[target.shape[1],target.shape[0]],'results':results},ensure_ascii=False,indent=2));print(json.dumps(results[:15],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
