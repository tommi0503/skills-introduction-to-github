from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).parent
with sync_playwright() as q:
 b=q.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1350,'height':850})
 page.goto('http://127.0.0.1:8765/crossrail-project/library/light.html');page.evaluate('document.fonts.ready')
 for name in ['chart-line / lines-flat','chart-line / lines-3','chart-area / area-1','chart-area / areas-stacked-3','waffle /','bullet /','radar /']:
  a=page.locator('article').filter(has=page.locator('h2',has_text=name)).first
  if a.count():a.screenshot(path=str(p/'library'/('check-'+name.replace(' / ','-').replace('/','')+'.png')))
 b.close()
print('figure screenshots done')
