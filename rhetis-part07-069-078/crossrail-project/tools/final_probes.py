from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).parent;q=p/'qa';q.mkdir(exist_ok=True)
css=(p/'crossrail/foundation/foundation.css').read_text()+'\n'+'\n'.join(x.read_text() for x in (p/'crossrail/elements').glob('*/element.css'))
for mode in ['light','dark']:
 h=(p/f'library/{mode}.html').read_text();h=h.replace('</head>','<style>'+css+'</style></head>');(q/f'final-{mode}.html').write_text(h.replace('../assets/','../assets/'))
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1360,'height':1000})
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:8765/crossrail-project/qa/final-{mode}.html');page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');page.wait_for_timeout(100)
  for t in ['balance','bullet','callout','chart-area','chart-donut','chart-stack','concentric','cycle','gauge','heatmap','hub','image-frame','sparkline','venn']:
   arts=page.locator('article').filter(has=page.locator('h2',has_text=t+' /'));arts.first.scroll_into_view_if_needed();boxes=[x.bounding_box() for x in arts.all()];x=min(v['x'] for v in boxes);y=min(v['y'] for v in boxes);right=max(v['x']+v['width'] for v in boxes);bot=max(v['y']+v['height'] for v in boxes);page.screenshot(path=str(q/f'{t}-{mode}.png'),clip={'x':x,'y':y,'width':right-x,'height':bot-y})
 b.close()
print('Functional probes rendered')
