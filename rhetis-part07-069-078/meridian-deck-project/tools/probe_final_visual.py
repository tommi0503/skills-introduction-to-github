from pathlib import Path
import importlib.util,json
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;R=P.parent;out=P/'visual-final';out.mkdir(exist_ok=True)
s=importlib.util.spec_from_file_location('preview','/workspace/work/reference/tools/preview.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
names=['foundation','callout','headline','chart-donut','chart-stack','funnel','heatmap','journey','pricing','versus','waffle','slope','radar','chart-area']
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1360,'height':900})
 for dark in [False,True]:
  mode='dark' if dark else 'light';h=m.sheet(P/'meridian-deck',json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text()),json.loads(Path('/workspace/work/reference/contract/palette.json').read_text()),dark=dark,fonts_href='../assets/fonts/fonts.css');h=h.replace('</body>','<script src="../assets/lucide.min.js"></script><script src="../assets/render-icons.js"></script></body>');(out/(mode+'.html')).write_text(h)
  page.goto('http://127.0.0.1:8765/meridian-deck-project/visual-final/'+mode+'.html');page.evaluate('document.fonts.ready');page.wait_for_timeout(200)
  for name in names:
   page.evaluate("name=>{for(const a of document.querySelectorAll('article'))a.style.display=a.querySelector('h2').textContent.startsWith(name+' / ')?'':'none'}",name);page.screenshot(path=str(out/(name+'-'+mode+'.png')),full_page=True)
 page.set_viewport_size({'width':1280,'height':720});page.goto('http://127.0.0.1:8765/meridian-deck-project/reassembled/slide_20.html');page.evaluate('document.fonts.ready');page.wait_for_timeout(200);page.screenshot(path=str(out/'slide20.png'))
 b.close()
print('Probed 12 affected types, two modes, and source page20.')
