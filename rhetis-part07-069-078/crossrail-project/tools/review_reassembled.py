from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import json
p=Path(__file__).parent;src=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('073*'));(p/'compare-reassembled').mkdir(exist_ok=True);out=[]
with sync_playwright() as q:
 b=q.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for f in sorted((p/'reassembled').glob('slide_*.html')):
  page.goto('http://127.0.0.1:8765/crossrail-project/reassembled/'+f.name);page.evaluate('document.fonts.ready');page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');page.wait_for_timeout(100);page.screenshot(path=str(f.with_suffix('.png')))
  issues=page.evaluate('''() => ({fonts:document.fonts.check('700 24px "Pretendard Variable"'),slide:[document.querySelector('.slide').offsetWidth,document.querySelector('.slide').offsetHeight],overflows:[...document.querySelectorAll('[data-el]')].filter(e=>e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2).map(e=>({el:e.dataset.el,w:[e.clientWidth,e.scrollWidth],h:[e.clientHeight,e.scrollHeight]}))})''');out.append({'page':f.name,**issues})
  a=Image.open(src/f.with_suffix('.png').name).convert('RGB');c=Image.new('RGB',(2560,720),'white');c.paste(a,(0,0));c.paste(Image.open(f.with_suffix('.png')).convert('RGB'),(1280,0));c.save(p/'compare-reassembled'/f.with_suffix('.png').name)
 b.close()
(p/'reassembled-checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,ensure_ascii=False))
