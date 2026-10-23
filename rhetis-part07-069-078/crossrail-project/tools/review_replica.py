from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
p=Path(__file__).parent
src=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('073*'))
(p/'compare-replica').mkdir(exist_ok=True)
with sync_playwright() as q:
 b=q.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for f in sorted((p/'replica').glob('slide_*.html')):
  page.goto('http://127.0.0.1:8765/crossrail-project/replica/'+f.name);page.evaluate('document.fonts.ready');page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');page.wait_for_timeout(100);page.screenshot(path=str(f.with_suffix('.png')))
  a=Image.open(src/f.with_suffix('.png').name).convert('RGB');c=Image.new('RGB',(2560,720),'white');c.paste(a,(0,0));c.paste(Image.open(f.with_suffix('.png')).convert('RGB'),(1280,0));c.save(p/'compare-replica'/f.with_suffix('.png').name)
 b.close()
print('rendered 30 paired comparisons')
