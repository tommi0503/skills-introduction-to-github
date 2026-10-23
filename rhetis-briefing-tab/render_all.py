from pathlib import Path
import json,re
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;R=ROOT/'briefing-tab-review';base='http://127.0.0.1:8765/briefing-tab-review/'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 pg=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  pg.goto(base+'library/'+mode+'.html');pg.evaluate('document.fonts.ready');print(mode,'fonts',pg.evaluate("document.fonts.check('20px \"Pretendard Variable\"') && document.fonts.check('48px \"Noto Sans KR\"')"),flush=True)
  for folder in ['foundation']+[q.name for q in sorted((ROOT/'briefing-tab/elements').iterdir()) if q.is_dir()]:
   pg.set_viewport_size({'width':1328,'height':800});pg.goto(base+f'library/{folder}/{mode}.html');pg.evaluate('document.fonts.ready')
   pg.screenshot(path=str(R/f'library/{folder}/{mode}.png'),full_page=True)
  # Full vector PDF, one fixture per 1280×720 page.
  pg.goto(base+'library/'+mode+'.html');pg.evaluate('document.fonts.ready')
  pg.add_style_tag(content='@page{size:1280px 720px;margin:0}body{display:block;margin:0;padding:0;background:white}article{position:relative;width:1280px;height:720px;margin:0;break-after:page}article>h2{position:absolute;top:4px;left:46px;z-index:5;font-size:12px}article>.frame{width:1280px;height:720px;overflow:hidden;border-radius:0}article>.frame>.slide{transform:none}')
  pg.pdf(path=str(R/f'library/library-{mode}.pdf'),width='1280px',height='720px',print_background=True,prefer_css_page_size=True)
  print('rendered',mode,flush=True)
 # Actual page render and vector PDFs; merge individual PDFs to one deck.
 from pypdf import PdfReader,PdfWriter
 for folder in ['replica','reassembled']:
  writer=PdfWriter()
  for n in range(20,31):
   pg.set_viewport_size({'width':1280,'height':720});pg.goto(base+f'{folder}/slide_{n}.html');pg.evaluate('document.fonts.ready')
   pg.screenshot(path=str(R/f'{folder}/slide_{n}.png'))
   pdf=ROOT/f'temp-{folder}-{n}.pdf';pg.pdf(path=str(pdf),width='1280px',height='720px',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
   for page in PdfReader(pdf).pages:writer.add_page(page)
   orig=next((ROOT/'decks').rglob(f'slide_{n}.png'));img=Image.new('RGB',(2560,720));img.paste(Image.open(orig).convert('RGB'),(0,0));img.paste(Image.open(R/f'{folder}/slide_{n}.png').convert('RGB'),(1280,0));img.save(R/f'compare-{folder}/slide_{n}.png')
  with open(R/f'{folder}/{folder}.pdf','wb')as f:writer.write(f)
  print('rendered',folder,flush=True)
 b.close()
