from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import fitz,json,threading,http.server,functools
server=http.server.ThreadingHTTPServer(("127.0.0.1",0),functools.partial(http.server.SimpleHTTPRequestHandler,directory="/workspace"))
threading.Thread(target=server.serve_forever,daemon=True).start()
B=Path('/workspace/work/deliverables/nocturne');R=B/'review';S=Path('/workspace/work/deck/miricanvas_기업_selected/006_1kkda_파랑_모던_타운홀_행사')
checks=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-crash-reporter','--disable-crashpad','--noerrdialogs','--disable-breakpad']);page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 pdf=fitz.open()
 for n in range(19,25):
  source=R/'replica'/f'slide_{n}.html';page.goto("http://127.0.0.1:"+str(server.server_port)+"/"+str(source.relative_to("/workspace")));page.evaluate('document.fonts.ready');page.screenshot(path=str(source.with_suffix('.png')))
  checks.append({'page':n,'font':page.evaluate("document.fonts.check('16px PV')"),'size':page.evaluate('({w:document.body.scrollWidth,h:document.body.scrollHeight})')})
  tmp=page.pdf(width='1280px',height='720px',print_background=True);part=fitz.open(stream=tmp,filetype='pdf');pdf.insert_pdf(part)
  a=Image.open(S/f'slide_{n}.png').convert('RGB');b=Image.open(source.with_suffix('.png')).convert('RGB');out=Image.new('RGB',(2560,750),'#eeeeee');out.paste(a,(0,30));out.paste(b,(1280,30));draw=ImageDraw.Draw(out);draw.text((20,10),'ORIGINAL',fill='black');draw.text((1300,10),'REPLICA',fill='black');out.save(R/'compare-replica'/f'slide_{n}.png')
 pdf.save(R/'replica'/'replica.pdf');browser.close()
(R/'replica'/'checks.json').write_text(json.dumps(checks,indent=2));print(checks)
