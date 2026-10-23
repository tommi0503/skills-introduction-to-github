from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json,sys
R=Path('/workspace/output/roundrise-review'); O=Path('/workspace/work/deck/miricanvas_기업_selected/004_1kfbp_파랑_모던_기업행사_안내')
mode=sys.argv[1] if len(sys.argv)>1 else 'replica'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 checks=[]
 for f in sorted((R/mode).glob('slide_*.html')):
  page.goto('http://127.0.0.1:8767/'+str(f.relative_to(R)));page.evaluate('document.fonts.ready');page.screenshot(path=str(f.with_suffix('.png')))
  checks.append({'file':f.name,**page.evaluate('''()=>({width:innerWidth,height:innerHeight,font:document.fonts.check('16px "Pretendard Variable"'),overflow:[...document.querySelectorAll('h1,h2,h3,p,.name,.note,.fig,.badge')].filter(e=>{const r=e.getBoundingClientRect(),c=getComputedStyle(e);return r.left<-.5||r.top<-.5||r.right>1280.5||r.bottom>720.5||(['hidden','clip'].includes(c.overflowY)&&e.scrollHeight>e.clientHeight+2)||(['hidden','clip'].includes(c.overflowX)&&e.scrollWidth>e.clientWidth+2)}).map(e=>({tag:e.className,text:e.textContent.slice(0,90)}))})''')})
  im=Image.new('RGB',(2560,760),'#eee');im.paste(Image.open(O/f.with_suffix('.png').name),(0,40));im.paste(Image.open(f.with_suffix('.png')),(1280,40));dr=ImageDraw.Draw(im);dr.text((20,12),'ORIGINAL',fill='black');dr.text((1300,12),mode.upper(),fill='black');cp=R/f'compare-{mode}';cp.mkdir(exist_ok=True);im.save(cp/f.with_suffix('.png').name)
  print(f.name,flush=True)
 b.close()
(R/f'{mode}-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False))
ims=[Image.open(f).convert('RGB') for f in sorted((R/mode).glob('slide_*.png'))];ims[0].save(R/mode/f'{mode}.pdf',save_all=True,append_images=ims[1:],resolution=96)
