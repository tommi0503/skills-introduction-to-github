from playwright.sync_api import sync_playwright
from pathlib import Path
from PIL import Image,ImageDraw
import json
R=Path(__file__).parent;SRC=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('058*'))
(R/'compare-replica').mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 audits=[]
 for f in sorted((R/'replica').glob('slide*.html')):
  page.goto('http://127.0.0.1:8765/halo-field-review/replica/'+f.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(f.with_suffix('.png')))
  audits.append({'page':f.name,'font':page.evaluate('document.fonts.check("16px Freesentation")'),'size':page.evaluate('[document.body.scrollWidth,document.body.scrollHeight]')})
  im=Image.new('RGB',(2560,720));im.paste(Image.open(SRC/f.with_suffix('.png').name),(0,0));im.paste(Image.open(f.with_suffix('.png')),(1280,0));im.save(R/'compare-replica'/f.with_suffix('.png').name)
 b.close()
(R/'replica-audit.json').write_text(json.dumps(audits,indent=2))
ims=[Image.open(f).convert('RGB') for f in sorted((R/'replica').glob('slide*.png'))];ims[0].save(R/'replica'/'replica.pdf',save_all=True,append_images=ims[1:],resolution=96)
print('rendered',len(ims))
