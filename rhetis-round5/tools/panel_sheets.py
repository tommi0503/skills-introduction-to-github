"""Render foundation-owned panel fixtures through the same real12x6 grid at every admitted size."""
from pathlib import Path
import sys,json,re,io,hashlib,time
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
from sheets import ROOT,HTTP,style,minimum,sizing,AUDIT,raster_contrast,fingerprint

def run(k):
 P=ROOT/(k+'-project');F=P/k/'foundation/fixtures';fixtures=sorted(F.glob('panel*.html'))
 if not fixtures:print(k,'no dedicated panel fixture');return
 D=P/'panel-sheets';D.mkdir(exist_ok=True);cache=P/'panel-cells';cache.mkdir(exist_ok=True);tmp=P/'foundation-runtime';tmp.mkdir(exist_ok=True);fn=tmp/'panels.html';initial=fingerprint(P,k)
 css=style(P,k);skeleton='<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>html,body{margin:0;width:1280px;height:720px}*{box-sizing:border-box}'+css+'[data-icon]:empty::after{content:"";display:block;width:100%;height:100%;border:1.5px dashed currentColor;border-radius:50%;box-sizing:border-box}</style><body><section class="slide"><div class="page"><div class="body"></div></div></section></body></html>';fn.write_text(skeleton)
 report={'collection':k,'scope':'foundation panels, actual12x6 slot crops plus6px outside gutter','sourceFingerprint':initial,'rendererSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'modes':{}}
 with sync_playwright()as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=browser.new_page(viewport={'width':1280,'height':720})
  for mode in ['light','dark']:
   page.goto(HTTP+str(fn.relative_to(ROOT)));page.locator('.slide').evaluate('(e,m)=>e.classList.toggle("dark",m==="dark")',mode);rows=[];checks=[]
   for f in fixtures:
    markup=re.sub(r'^<!--.*?-->\s*','',f.read_text(),count=1,flags=re.S)
    if re.search(r'class=["\'][^"\']*\bslide\b',markup):continue
    mini=minimum(f);pics=[]
    for c,r in sizing(mini):
     page.locator('.body').evaluate('(e,s)=>e.innerHTML=s',markup);root=page.locator('.body > *');assert root.count()==1,f
     root.evaluate('(e,s)=>{e.style.gridColumn="1 / span "+s[0];e.style.gridRow="1 / span "+s[1]}',[c,r]);page.evaluate('document.fonts.ready');page.wait_for_timeout(80)
     diag=root.evaluate(AUDIT);diag.update(fixture=f.name,size=[c,r],isMin=(c,r)==mini)
     slot=page.locator('.body').evaluate('(e,s)=>{const r=e.getBoundingClientRect(),st=getComputedStyle(e),gx=parseFloat(st.columnGap),gy=parseFloat(st.rowGap);return[r.x,r.y,(r.width-11*gx)/12*s[0]+gx*(s[0]-1),(r.height-5*gy)/6*s[1]+gy*(s[1]-1)]}',[c,r]);diag['slot']=slot;x,y,w,h=slot;clip={'x':max(0,x-6),'y':max(0,y-6),'width':min(1280-max(0,x-6),w+12),'height':min(720-max(0,y-6),h+12)}
     b=page.screenshot(clip=clip,animations='disabled');im=Image.open(io.BytesIO(b)).convert('RGB');raster_contrast(diag,im,clip);checks.append(diag);(cache/f'{f.stem}--{mode}--{c}x{r}.png').write_bytes(b);pics.append(((c,r),im))
    rows.append((f.name,mini,pics))
   heights=[max(im.height for _,im in pics)+62 for _,_,pics in rows];width=max(sum(im.width+14 for _,im in pics)+220 for _,_,pics in rows);canvas=Image.new('RGB',(width,48+sum(heights)),'#151a22'if mode=='dark'else'#e9edf2');draw=ImageDraw.Draw(canvas);fg='#f2f4f7'if mode=='dark'else'#202732';draw.text((12,15),f'{k} foundation panels | {mode} | native1280x720 grid crops',fill=fg);yy=48
   for(name,mini,pics),hh in zip(rows,heights):
    draw.text((12,yy+30),name,fill=fg);draw.text((12,yy+48),f'min {mini[0]}x{mini[1]}',fill=fg);xx=210
    for size,im in pics:draw.text((xx,yy+5),f'{size[0]}x{size[1]}'+(' [MIN]'if size==mini else''),fill=fg);canvas.paste(im,(xx,yy+26));draw.rectangle((xx-1,yy+25,xx+im.width,yy+26+im.height),outline='#4b80ba'if size==mini else'#7e8996');xx+=im.width+14
    yy+=hh
   canvas.save(D/f'foundation-panels-{mode}.png');report['modes'][mode]=checks
  browser.close()
 assert fingerprint(P,k)==initial,'Source changed during panel render; rerender after freeze'
 (D/'panel-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(k,'panel cells',sum(len(v)for v in report['modes'].values()))
if __name__=='__main__':
 for k in sys.argv[1:]:run(k)
