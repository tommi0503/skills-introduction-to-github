from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import fitz,json
root=Path('/workspace/work/deliverables/confluence/review')
orig=Path('/workspace/work/deck/miricanvas_기업_selected/020_1bqgw_파랑과_하늘색의_트렌드한_산학협력_제안서')
checks=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for h in sorted((root/'replica').glob('slide_*.html')):
  page.goto('http://127.0.0.1:8020/review/replica/'+h.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(h.with_suffix('.png')))
  checks.append({'page':h.stem,'fonts':page.evaluate('document.fonts.check("16px P")'),'size':page.locator('.slide').bounding_box()})
  page.pdf(path=str(root/'replica'/f'{h.stem}.pdf'),width='1280px',height='720px',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
  side=Image.new('RGB',(2560,720),'white');side.paste(Image.open(orig/h.with_suffix('.png').name),(0,0));side.paste(Image.open(h.with_suffix('.png')),(1280,0));side.save(root/'compare-replica'/h.with_suffix('.png').name)
 browser.close()
doc=fitz.open()
for f in sorted((root/'replica').glob('slide_*.pdf')):
 d=fitz.open(f);doc.insert_pdf(d);d.close();f.unlink()
doc.save(root/'replica'/'replica.pdf');doc.close()
(root/'replica'/'checks.json').write_text(json.dumps(checks,indent=2))
