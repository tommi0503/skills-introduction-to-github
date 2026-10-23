from playwright.sync_api import sync_playwright
from pathlib import Path
from PIL import Image
import json,re
R=Path(__file__).parent;C=R.parent/'halo-field';SRC=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('058*'));URL='http://127.0.0.1:8765/halo-field-review/'
AUD=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  for folder in sorted((R/'library').iterdir()):
   if not folder.is_dir():continue
   f=folder/(mode+'.html');page.goto(URL+'library/'+folder.name+'/'+mode+'.html');page.evaluate("document.fonts.load('400 16px Freesentation')");page.evaluate("document.fonts.load('700 16px Freesentation')");page.evaluate('document.fonts.ready');page.screenshot(path=str(folder/(mode+'.png')))
   AUD.append({'element':folder.name,'mode':mode,'font':page.evaluate('document.fonts.check("16px Freesentation")'),'frames':page.locator('article').count()})
  ims=[Image.open(f/(mode+'.png')).convert('RGB') for f in sorted((R/'library').iterdir()) if f.is_dir()];ims[0].save(R/'library'/('library-'+mode+'.pdf'),save_all=True,append_images=ims[1:],resolution=96)
 for f in sorted((R/'reassembled').glob('slide*.html')):
  page.goto(URL+'reassembled/'+f.name);page.evaluate("document.fonts.load('400 16px Freesentation')");page.evaluate("document.fonts.load('700 16px Freesentation')");page.evaluate('document.fonts.ready');page.screenshot(path=str(f.with_suffix('.png')))
  (R/'compare-reassembled').mkdir(exist_ok=True);im=Image.new('RGB',(2560,720));im.paste(Image.open(SRC/f.with_suffix('.png').name),(0,0));im.paste(Image.open(f.with_suffix('.png')),(1280,0));im.save(R/'compare-reassembled'/f.with_suffix('.png').name)
  AUD.append({'page':f.name,'mode':'reassembled','font':page.evaluate('document.fonts.check("16px Freesentation")'),'size':page.evaluate('[document.querySelector(".slide").getBoundingClientRect().width,document.querySelector(".slide").getBoundingClientRect().height]'),'overflow':page.evaluate('''[...document.querySelectorAll('[data-el]')].filter(e=>e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2).map(e=>({el:e.dataset.el,w:[e.clientWidth,e.scrollWidth],h:[e.clientHeight,e.scrollHeight]}))''')})
 b.close()
ims=[Image.open(f).convert('RGB') for f in sorted((R/'reassembled').glob('slide*.png'))];ims[0].save(R/'reassembled'/'reassembled.pdf',save_all=True,append_images=ims[1:],resolution=96)
(R/'browser-audit.json').write_text(json.dumps(AUD,indent=2));print('rendered library sheets and reassembled')
