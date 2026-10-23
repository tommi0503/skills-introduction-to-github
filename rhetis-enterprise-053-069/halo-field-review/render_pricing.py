from playwright.sync_api import sync_playwright
from pathlib import Path
from PIL import Image
R=Path(__file__).parent
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:8765/halo-field-review/library/pricing/{mode}.html');page.evaluate("document.fonts.load('400 16px Freesentation')");page.evaluate('document.fonts.ready');page.screenshot(path=str(R/'library/pricing'/f'{mode}.png'))
 b.close()
for mode in ['light','dark']:
 ims=[Image.open(f/(mode+'.png')).convert('RGB') for f in sorted((R/'library').iterdir()) if f.is_dir()];ims[0].save(R/'library'/('library-'+mode+'.pdf'),save_all=True,append_images=ims[1:],resolution=96)
print('pricing check variant final rendered')
