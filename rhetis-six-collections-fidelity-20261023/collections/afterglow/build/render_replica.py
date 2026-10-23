from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import fitz,json,threading,http.server,functools
server=http.server.ThreadingHTTPServer(("127.0.0.1",0),functools.partial(http.server.SimpleHTTPRequestHandler,directory="/workspace"));threading.Thread(target=server.serve_forever,daemon=True).start()
B=Path(__file__).resolve().parents[1];R=B/'review'; originals=Path('/workspace/work/deck/miricanvas_기업_selected/015_1a53x_검정과_파랑의_심플한_서비스_소개서')
checks=[];pdf=fitz.open()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for src in sorted((R/'replica').glob('slide*.html')):
  page.goto(f"http://127.0.0.1:{server.server_port}/"+str(src.relative_to("/workspace")));page.evaluate('document.fonts.ready');page.screenshot(path=str(src.with_suffix('.png')))
  checks.append({'page':src.name,'fonts':page.evaluate('document.fonts.check("16px Pretendard")'),'size':page.evaluate('({w:innerWidth,h:innerHeight})')})
  a=Image.open(originals/src.with_suffix('.png').name).convert('RGB');b=Image.open(src.with_suffix('.png')).convert('RGB');c=Image.new('RGB',(2560,720));c.paste(a,(0,0));c.paste(b,(1280,0));c.save(R/'compare-replica'/src.with_suffix('.png').name)
  pp=pdf.new_page(width=1280,height=720);pp.insert_image(pp.rect,filename=str(src.with_suffix('.png')))
 browser.close()
pdf.save(R/'replica'/'replica.pdf');(R/'replica'/'checks.json').write_text(json.dumps(checks,indent=2))
