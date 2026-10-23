from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json
B=Path(__file__).parent; D=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('055*'))
def run(folder):
 audit=[]
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for f in sorted((B/folder).glob('slide_*.html')):
   page.goto('http://127.0.0.1:8765/current-fold-review/'+folder+'/'+f.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(f.with_suffix('.png')))
   audit.append({'file':f.name,**page.evaluate('''()=>({width:document.documentElement.clientWidth,height:document.documentElement.clientHeight,font:document.fonts.check('16px "Pretendard Variable"'),overflow:[...document.querySelectorAll('p,h1,h2,h3,b,td')].filter(e=>e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2).map(e=>e.textContent.slice(0,60))})''')})
   im=Image.new('RGB',(2560,720),'white');im.paste(Image.open(D/f.with_suffix('.png').name),(0,0));im.paste(Image.open(f.with_suffix('.png')),(1280,0));im.save(B/('compare-'+folder)/f.with_suffix('.png').name)
  browser.close()
 ims=[Image.open(f).convert('RGB') for f in sorted((B/folder).glob('slide_*.png'))]
 ims[0].save(B/folder/(folder+'.pdf'),save_all=True,append_images=ims[1:],resolution=96)
 (B/(folder+'-audit.json')).write_text(json.dumps(audit,ensure_ascii=False,indent=2))
if __name__=='__main__':
 import sys
 run(sys.argv[1] if len(sys.argv)>1 else 'replica')
