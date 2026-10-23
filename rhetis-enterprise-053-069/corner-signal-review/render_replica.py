from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import json
R=Path(__file__).parent;D=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('067*'));checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for f in sorted((R/'replica').glob('slide*.html')):
  page.goto('http://127.0.0.1:8765/corner-signal-review/replica/'+f.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(f.with_suffix('.png')))
  checks.append({'page':f.name,'font':page.evaluate("document.fonts.check('16px \"Pretendard Variable\"')"),'size':page.evaluate('[document.documentElement.clientWidth,document.documentElement.clientHeight]')})
  c=Image.new('RGB',(2560,720),'white');c.paste(Image.open(D/f.with_suffix('.png').name),(0,0));c.paste(Image.open(f.with_suffix('.png')),(1280,0));c.save(R/'compare-replica'/f.with_suffix('.png').name)
 b.close()
ims=[Image.open(f).convert('RGB') for f in sorted((R/'replica').glob('slide*.png'))];ims[0].save(R/'replica/replica.pdf',save_all=True,append_images=ims[1:],resolution=96)
(R/'replica-checks.json').write_text(json.dumps(checks,indent=2));print(checks)
