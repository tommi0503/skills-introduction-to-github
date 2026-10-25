"""Independent raster centring check of plain filled tags and pill labels.

This deliberately excludes labels sharing their capsule with icons/notes and inline
highlights: their meaningful centre is not the centre of the complete capsule.
"""
from pathlib import Path
import json,re,io,sys,time
from PIL import Image
import numpy as np
from playwright.sync_api import sync_playwright
from sheets import ROOT,HTTP,style,minimum,sizing,fingerprint

def run(k):
 p=ROOT/(k+'-project');runtime=p/'sheet-runtime'
 leaves=[d.name for d in sorted((p/k/'elements').iterdir())if d.is_dir()and d.name.split('--')[0]in ['pill','tag']]
 initial={leaf:fingerprint(p,k,leaf)for leaf in leaves}
 fn=runtime/'optical-audit.html'
 document=('<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>html,body{margin:0;width:1280px;height:720px}*{box-sizing:border-box}'+style(p,k)+'</style><section class="slide"><div class="page"><div class="body"></div></div></section>')
 results=[];excluded=0
 with sync_playwright() as pw:
  b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  page=b.new_page(viewport={'width':1280,'height':720})
  # Serve diagnostic markup from memory: final verification never rewrites HTML inputs.
  page.route(HTTP+str(fn.relative_to(ROOT)),lambda route:route.fulfill(status=200,content_type='text/html',body=document))
  for mode in ['light','dark']:
   page.goto(HTTP+str(fn.relative_to(ROOT)));page.locator('.slide').evaluate('(e,m)=>e.classList.toggle("dark",m==="dark")',mode)
   for leaf in leaves:
    for f in sorted((p/k/'elements'/leaf/'fixtures').glob('*.html')):
     markup=re.sub(r'^<!--.*?-->\s*','',f.read_text(),count=1,flags=re.S)
     for c,r in sizing(minimum(f)):
      page.locator('.body').evaluate('(e,s)=>e.innerHTML=s',markup)
      page.locator('.body > *').evaluate('(e,s)=>{e.style.gridColumn="1 / span "+s[0];e.style.gridRow="1 / span "+s[1]}',[c,r])
      page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
      objects=page.evaluate('''()=>[...document.querySelectorAll('.body .tag,.body .pill>.parts')].filter(e=>!e.querySelector('.mark,.note,.icon')&&e.textContent.trim()).map(e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e),ctx=document.createElement('canvas').getContext('2d');const rgb=c=>{ctx.clearRect(0,0,1,1);ctx.fillStyle=c;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data]};e.setAttribute('data-optical-probe',String([...document.querySelectorAll('.body .tag,.body .pill>.parts')].indexOf(e)));return {probe:e.getAttribute('data-optical-probe'),radii:[s.borderTopLeftRadius,s.borderTopRightRadius,s.borderBottomRightRadius,s.borderBottomLeftRadius],box:[r.x,r.y,r.width,r.height],bg:rgb(s.backgroundColor),fg:rgb(getComputedStyle(e.querySelector('.name')||e).color),text:e.textContent.trim()}})''')
      if not objects:excluded+=1
      for obj in objects:
       x,y,w,h=obj['box']
       if obj['bg'][3]<250:excluded+=1;continue
       shot=Image.open(io.BytesIO(page.screenshot(clip={'x':x,'y':y,'width':w,'height':h}))).convert('RGB');a=np.array(shot).astype(int)
       target=page.locator('[data-optical-probe="'+obj['probe']+'"]')
       saved=target.get_attribute('style')
       target.evaluate('(e)=>e.style.setProperty("-webkit-text-fill-color","transparent","important")')
       bare=np.array(Image.open(io.BytesIO(page.screenshot(clip={'x':x,'y':y,'width':w,'height':h}))).convert('RGB')).astype(int)
       target.evaluate('(e,s)=>s===null?e.removeAttribute("style"):e.setAttribute("style",s)',saved)
       painted=np.linalg.norm(a-bare,axis=2)>8
       yy,xx=np.indices(a.shape[:2]);bg=np.array(obj['bg'][:3]);fg=np.array(obj['fg'][:3]);delta=np.linalg.norm(a-fg,axis=2)
       # Difference against the same capsule with text fill hidden isolates
       # painted glyphs, excluding page-coloured rounded corners and cylinder art.
       radii=[]
       for raw in obj['radii']:
        values=raw.split();values=values+[values[0]]if len(values)==1 else values
        radii.append([float(v.rstrip('%px'))*(w if j==0 else h)/100 if v.endswith('%')else float(v.rstrip('px'))for j,v in enumerate(values)])
       factor=min(1,w/max(1,radii[0][0]+radii[1][0]),w/max(1,radii[3][0]+radii[2][0]),h/max(1,radii[0][1]+radii[3][1]),h/max(1,radii[1][1]+radii[2][1]))
       shape=(xx>=1)&(xx<w-1)&(yy>=1)&(yy<h-1)
       for corner,(rx,ry) in enumerate(radii):
        rx*=factor;ry*=factor
        if min(rx,ry)<1:continue
        cx=rx if corner in[0,3]else w-rx;cy=ry if corner in[0,1]else h-ry
        quadrant=((xx<cx)if corner in[0,3]else(xx>cx))&((yy<cy)if corner in[0,1]else(yy>cy))
        ellipse=((xx+.5-cx)/max(1,rx-1))**2+((yy+.5-cy)/max(1,ry-1))**2<=1
        shape&=(~quadrant)|ellipse
       mask=(delta<32)&painted&shape
       iy,ix=np.where(mask)
       if len(ix)<4:excluded+=1;continue
       dx=(float(ix.min()+ix.max()+1)-w)/2;dy=(float(iy.min()+iy.max()+1)-h)/2
       results.append({'mode':mode,'leaf':leaf,'fixture':f.name,'size':[c,r],'text':obj['text'],'capsule':[round(v,2) for v in obj['box']],'glyphBounds':[int(ix.min()),int(iy.min()),int(ix.max()+1),int(iy.max()+1)],'dx':round(dx,2),'dy':round(dy,2),'threshold':2.5,'pass':abs(dx)<=2.5 and abs(dy)<=2.5})
  b.close()
 current={leaf:fingerprint(p,k,leaf)for leaf in leaves}
 assert initial==current,('Source changed during optical rendering; rerun after freeze',k,initial,current)
 report={'collection':k,'generatedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'scope':'Raster glyph centre isolated by a paired screenshot with text fill hidden, of plain filled pill/tag only; multi-part labels and inline highlights excluded; asymmetric script glyphs reported as candidates, never silently corrected. DOM chip checks separately cover every fixture.','sourceFingerprints':initial,'excludedCellsOrObjects':excluded,'checks':results,'candidates':[v for v in results if not v['pass']]}
 (p/'optical-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(k,len(results),'checked',len(report['candidates']),'candidates')

if __name__=='__main__':
 for k in sys.argv[1:]:run(k)
