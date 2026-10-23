from pathlib import Path
import sys
from PIL import Image
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;out=P/'fidelity-pass';out.mkdir(exist_ok=True)
nums=list(map(int,sys.argv[1:])) or list(range(1,31));orig=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('074*'))
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720})
 for n in nums:
  name=f'slide_{n:02d}.png';page.goto(f'http://127.0.0.1:8765/meridian-deck-project/reassembled/slide_{n:02d}.html');page.evaluate('document.fonts.ready');page.wait_for_timeout(100);page.screenshot(path=str(P/'reassembled'/name));im=Image.new('RGB',(3840,720));im.paste(Image.open(orig/name),(0,0));im.paste(Image.open(P/'replica'/name),(1280,0));im.paste(Image.open(P/'reassembled'/name),(2560,0));im.save(out/name)
 b.close()
print('Fidelity renders',nums)
