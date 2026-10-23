"""Native-paint contrast for sibling-layer bar annotations, preserving raw audit evidence."""
import json,hashlib,importlib.util,io
from PIL import Image
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
def lum(rgb):
 c=[v/255 for v in rgb];c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c];return sum(v*w for v,w in zip(c,[.2126,.7152,.0722]))
results={}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1360,'height':900});q.goto('http://127.0.0.1:8765/qa/probe.html')
 for dark in [False,True]:
  m=pv.sheet(BASE/'crossrail-project/crossrail',json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),dark=dark,fonts_href='/crossrail-project/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready');a=q.locator('article').filter(has=q.locator('h2',has_text='chart-bar / bars-annotated')).first;q.locator('article').evaluate_all("aa=>aa.forEach(a=>a.style.display='none')");a.evaluate("a=>{a.style.display='block';a.querySelector('.frame').style.width='1280px';a.querySelector('.frame').style.height='720px';a.querySelector('.slide').style.transform='none';for(let e of a.querySelector('.body').children){e.style.gridColumn='1 / span 12';e.style.gridRow='1 / span 6'}}")
  a.locator('.slide').screenshot(path=str(BASE/'qa'/f'crossrail-bars-annotated-{"dark" if dark else "light"}.png'))
  rows=a.evaluate('''a=>{let slide=a.querySelector('.slide'),r0=slide.getBoundingClientRect(),can=document.createElement('canvas'),ctx=can.getContext('2d'),rows=[];can.width=can.height=1;for(let e of slide.querySelectorAll('*')){if(e.children.length||!e.textContent.trim())continue;let r=e.getBoundingClientRect(),s=getComputedStyle(e);if(!r.width||!r.height||s.display==='none'||s.visibility==='hidden')continue;ctx.clearRect(0,0,1,1);ctx.fillStyle=s.color;ctx.fillRect(0,0,1,1);rows.push({text:e.textContent.trim(),class:e.className,size:s.fontSize,weight:s.fontWeight,fg:[...ctx.getImageData(0,0,1,1).data].slice(0,3),point:[r.x-r0.x+r.width/2,r.y-r0.y+r.height/2]});e.style.color='transparent'}return rows}''')
  im=Image.open(io.BytesIO(a.locator('.slide').screenshot())).convert('RGB')
  for r in rows:
   x,y=[round(v) for v in r['point']]
   if not(0<=x<im.width and 0<=y<im.height):r['outside']=True;continue
   r['bg']=im.getpixel((x,y));l1,l2=lum(r['fg']),lum(r['bg']);r['ratio']=round((max(l1,l2)+.05)/(min(l1,l2)+.05),2);sz=float(r['size'][:-2]);r['threshold']=3 if sz>=24 or sz>=18.6667 and float(r['weight'])>=700 else 4.5;r['pass']=r['ratio']+.04>=r['threshold']
  results['dark' if dark else 'light']={'sourceSha256':hashlib.sha256(m.encode()).hexdigest(),'fixture':a.locator(':scope > h2').inner_text(),'rows':rows,'note':'Text-only paint made transparent without layout changes; background sampled from real browser PNG, including sibling panels.'}
 b.close()
(BASE/'qa/crossrail-native-contrast.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print({mode:[{k:r[k] for k in ['text','ratio','threshold']} for r in v['rows'] if 'pass' in r and not r['pass']] for mode,v in results.items()})
