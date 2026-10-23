from playwright.sync_api import sync_playwright
from pathlib import Path
import json
ks=['sankey','mindmap','cycle','journey','chart-waterfall','hub','hierarchy','decision-tree','concentric']
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1280,'height':2000},device_scale_factor=1)
 page.goto('http://127.0.0.1:8760/glass-contract-proof.html');page.evaluate('document.fonts.ready')
 page.add_style_tag(content='body{display:block;padding:0}article{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}h2{display:none}')
 result={}
 for k in ks:
  arts=page.locator('article').filter(has=page.locator('h2').filter(has_text=k+' /'))
  for j in range(arts.count()):
   a=arts.nth(j);a.evaluate("x=>x.style.display='block'")
   a.locator('.frame').screenshot(path=f'/workspace/work/fluxweave/glass-proof-{k}-{j}.png')
   result[k+str(j)]=a.locator('[data-el]').first.evaluate("x=>({w:x.clientWidth,h:x.clientHeight,children:[...x.children].map(n=>({cls:n.className,r:n.getBoundingClientRect().toJSON(),before:getComputedStyle(n,'::before').cssText,afterW:getComputedStyle(n,'::after').width,afterT:getComputedStyle(n,'::after').transform}))})")
   a.evaluate("x=>x.style.display='none'")
 Path('/workspace/work/fluxweave/glass-proof.json').write_text(json.dumps(result,indent=2))
 b.close()
