from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
p=Path(__file__).parent
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for n in [5,10,11,19,21,24]:
  g.goto(f'http://127.0.0.1:8765/crossrail-project/reassembled/slide_{n:02}.html');g.evaluate('document.fonts.ready');g.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');g.wait_for_timeout(100);out=p/f'qa/restored-{n:02}.png';g.screenshot(path=str(out));orig=Image.open(p/f'compare-replica/slide_{n:02}.png').crop((0,0,1280,720));im=Image.new('RGB',(2560,720));im.paste(orig);im.paste(Image.open(out),(1280,0));im.save(p/f'qa/restored-{n:02}-compare.png')
 b.close()
print('restored subset rendered')
