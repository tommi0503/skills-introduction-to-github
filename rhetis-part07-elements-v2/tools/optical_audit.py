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
 initial={leaf:fingerprint(p,k,leaf)for leaf in ['pill','tag']}
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
   for leaf in ['pill','tag']:
    for f in sorted((p/k/'elements'/leaf/'fixtures').glob('*.html')):
     markup=re.sub(r'^<!--.*?-->\s*','',f.read_text(),count=1,flags=re.S)
     for c,r in sizing(minimum(f)):
      page.locator('.body').evaluate('(e,s)=>e.innerHTML=s',markup)
      page.locator('.body > *').evaluate('(e,s)=>{e.style.gridColumn="1 / span "+s[0];e.style.gridRow="1 / span "+s[1]}',[c,r])
      page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
      objects=page.evaluate('''()=>[...document.querySelectorAll('.body .tag,.body .pill>.parts')].filter(e=>!e.querySelector('.mark,.note,.icon')&&e.textContent.trim()).map(e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e),ctx=document.createElement('canvas').getContext('2d');const rgb=c=>{ctx.clearRect(0,0,1,1);ctx.fillStyle=c;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data]};return {box:[r.x,r.y,r.width,r.height],bg:rgb(s.backgroundColor),fg:rgb(getComputedStyle(e.querySelector('.name')||e).color),text:e.textContent.trim()}})''')
      if not objects:excluded+=1
      for obj in objects:
       x,y,w,h=obj['box']
       if obj['bg'][3]<250:excluded+=1;continue
       shot=Image.open(io.BytesIO(page.screenshot(clip={'x':x,'y':y,'width':w,'height':h}))).convert('RGB');a=np.array(shot).astype(int)
       yy,xx=np.indices(a.shape[:2]);bg=np.array(obj['bg'][:3]);fg=np.array(obj['fg'][:3]);delta=np.linalg.norm(a-fg,axis=2)
       # An inset excludes the page pixels in rounded outside corners. An exact
       # foreground core avoids counting antialias fringe as the glyph boundary.
       mask=(delta<32)&(xx>=min(4,w*.08))&(xx<w-min(4,w*.08))&(yy>=1)&(yy<h-1)
       iy,ix=np.where(mask)
       if len(ix)<4:excluded+=1;continue
       dx=(float(ix.min()+ix.max()+1)-w)/2;dy=(float(iy.min()+iy.max()+1)-h)/2
       results.append({'mode':mode,'leaf':leaf,'fixture':f.name,'size':[c,r],'text':obj['text'],'capsule':[round(v,2) for v in obj['box']],'glyphBounds':[int(ix.min()),int(iy.min()),int(ix.max()+1),int(iy.max()+1)],'dx':round(dx,2),'dy':round(dy,2),'threshold':2.5,'pass':abs(dx)<=2.5 and abs(dy)<=2.5})
  b.close()
 current={leaf:fingerprint(p,k,leaf)for leaf in ['pill','tag']}
 assert initial==current,('Source changed during optical rendering; rerun after freeze',k,initial,current)
 report={'collection':k,'generatedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'scope':'Raster glyph centre of plain filled pill/tag only; multi-part labels and inline highlights excluded; asymmetric script glyphs reported as candidates, never silently corrected. DOM chip checks separately cover every fixture.','sourceFingerprints':initial,'excludedCellsOrObjects':excluded,'checks':results,'candidates':[v for v in results if not v['pass']]}
 (p/'optical-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(k,len(results),'checked',len(report['candidates']),'candidates')

if __name__=='__main__':
 for k in sys.argv[1:]:run(k)
