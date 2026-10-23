from pathlib import Path
import json
from playwright.sync_api import sync_playwright
p=Path(__file__).parent
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1360,'height':1000})
 results={}
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:8765/crossrail-project/qa/final-{mode}.html');page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');page.wait_for_timeout(100)
  results[mode]=page.evaluate('''() => ({font:document.fonts.check('18px "Pretendard Variable"'),donuts:[...document.querySelectorAll('[data-el="crossrail-chart-donut"].donut')].map(e=>{let p=getComputedStyle(e,'::before');return [parseFloat(p.width),parseFloat(p.height)]}),rings:[...document.querySelectorAll('[data-el="crossrail-concentric"] .ring')].map(e=>{let b=e.getBoundingClientRect();return [b.width,b.height]}),spark:[...document.querySelectorAll('.parts>[data-el="crossrail-sparkline"]')].map(e=>[e.clientHeight,e.firstElementChild.clientHeight]),stackColors:[...document.querySelectorAll('[data-el="crossrail-chart-stack"] .sbar')][0]?[...document.querySelectorAll('[data-el="crossrail-chart-stack"] .sbar')][0].querySelectorAll('.seg').length:0,negativeBalances:[...document.querySelectorAll('[data-el="crossrail-balance"]')].filter(e=>parseFloat(e.style.getPropertyValue('--tilt'))<0).map(e=>[...e.querySelectorAll(':scope>.pan')].map(p=>p.getBoundingClientRect().top))})''')
  for typ,fixture in [('sankey','sankey-6'),('concentric','orbit-4'),('chart-area','areas-stacked-3'),('callout','callout-stack'),('heatmap','calendar-12'),('chart-stack','stacks-h-4'),('venn','venn-3')]:
   a=page.locator('article').filter(has=page.locator('h2',has_text=typ+' / '+fixture)).first
   if a.count():a.screenshot(path=str(p/'qa'/f'probe-{typ}-{mode}.png'))
 b.close()
(p/'qa/final-geometry.json').write_text(json.dumps(results,indent=2));print(json.dumps(results))
