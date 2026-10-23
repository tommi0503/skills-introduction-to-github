from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
P=Path(__file__).parent;S=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('069*'));C=P/'compare-reassembled';C.mkdir(exist_ok=True)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--allow-file-access-from-files']);page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for f in sorted((P/'reassembled').glob('slide_*.html')):
  page.goto('http://127.0.0.1:8871/reassembled/'+f.name);page.evaluate('document.fonts.ready');page.add_script_tag(path='/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/lucide/dist/umd/lucide.min.js');page.evaluate('lucide.createIcons({nameAttr: "data-icon"})');page.screenshot(path=str(f.with_suffix('.png')))
  im=Image.new('RGB',(2560,720));im.paste(Image.open(S/f.with_suffix('.png').name),(0,0));im.paste(Image.open(f.with_suffix('.png')),(1280,0));im.save(C/f.with_suffix('.png').name)
 browser.close()
