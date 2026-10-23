from pathlib import Path
import json,math
from PIL import Image
import numpy as np
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;R=ROOT/'briefing-tab-review';out=[]
with sync_playwright()as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720})
 for n,selector in [(20,'.pill .mark'),(24,'.bars .bar>b:not(:empty)'),(27,'.donut>.name'),(28,'.donut>.name')]:
  pg.goto(f'http://127.0.0.1:8765/briefing-tab-review/reassembled/slide_{n}.html');pg.evaluate('document.fonts.ready');png=ROOT/f'chip-page-{n}.png';pg.screenshot(path=str(png));im=np.asarray(Image.open(png).convert('RGB'))
  boxes=pg.locator(selector).evaluate_all('es=>es.map(e=>({text:e.textContent,box:e.getBoundingClientRect().toJSON(),radius:getComputedStyle(e).borderRadius}))')
  for a in boxes:
   r=a['box'];x=max(0,int(math.floor(r['x'])));y=max(0,int(math.floor(r['y'])));w=int(round(r['width']));h=int(round(r['height']));crop=im[y:y+h,x:x+w]
   if not crop.size:continue
   yy,xx=np.indices(crop.shape[:2]);rad=min(w,h)/2;cx=np.clip(xx,rad,w-rad);cy=h/2
   inside=(xx-cx)**2+(yy-cy)**2<(rad-2)**2
   fg=(crop.min(axis=2)>205)&inside
   ys,xs=np.where(fg)
   if len(xs):
    dx=(xs.min()+xs.max()+1)/2-w/2;dy=(ys.min()+ys.max()+1)/2-h/2
    out.append({'slide':n,'text':a['text'].replace('\n',' ').strip(),'box':[w,h],'ink_center_offset':[round(float(dx),2),round(float(dy),2)],'pass':bool(abs(dx)<=3 and abs(dy)<=3)})
 b.close()
(R/'chip-validation.json').write_text(json.dumps({'method':'Rendered foreground pixel bounds inside the capsule/circle, tolerance 3px per axis','count':len(out),'failures':sum(not a['pass']for a in out),'results':out},ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False,indent=2))
