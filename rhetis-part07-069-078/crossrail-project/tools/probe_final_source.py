from playwright.sync_api import sync_playwright
from pathlib import Path
import json
P=Path(__file__).parent;out={}
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for n in [6,7,8,12,13,14,15,19,23,24]:
  g.goto(f'http://127.0.0.1:8765/crossrail-project/reassembled/slide_{n:02}.html');g.evaluate('document.fonts.ready');g.wait_for_timeout(80);g.screenshot(path=str(P/f'qa/source-last-{n:02}.png'))
  if n==13:out['13']=g.locator('.steps .step,.steps .mark>.icon').evaluate_all('(es)=>es.map(e=>{let r=e.getBoundingClientRect();return[e.className,r.x,r.y,r.width,r.height,r.y+r.height/2]})')
  if n==7:out['07']=g.locator('.card .note').evaluate_all('es=>es.filter(e=>e.textContent.includes("위아래")).map(e=>{let rs=[],w=document.createTreeWalker(e,NodeFilter.SHOW_TEXT);while(w.nextNode()){let r=document.createRange();r.selectNode(w.currentNode);rs.push([...r.getClientRects()].map(a=>[a.x,a.y,a.width,a.height]))}return rs})')
 b.close()
(P/'qa/source-last-probes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
