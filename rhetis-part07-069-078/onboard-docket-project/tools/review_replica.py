from playwright.sync_api import sync_playwright
from pathlib import Path
from PIL import Image,ImageDraw
P=Path(__file__).parent
O=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('078*'))
(P/'replica-review').mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for n in range(1,20):
  response=page.goto(f'http://127.0.0.1:8765/onboard-docket-project/replica/slide_{n:02}.html');assert response.status==200;page.evaluate('document.fonts.ready');page.wait_for_timeout(150);page.screenshot(path=str(P/'replica-review'/f'replica_{n:02}.png'))
  a=Image.open(O/f'slide_{n:02}.png');r=Image.open(P/'replica-review'/f'replica_{n:02}.png');c=Image.new('RGB',(2560,720),'white');c.paste(a,(0,0));c.paste(r,(1280,0));c.save(P/'replica-review'/f'compare_{n:02}.jpg')
  print(n,page.evaluate('document.fonts.check("400 18px Noto")'))
 b.close()
