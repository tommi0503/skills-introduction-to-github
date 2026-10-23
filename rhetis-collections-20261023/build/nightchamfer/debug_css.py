from pathlib import Path
import threading,http.server,functools
from playwright.sync_api import sync_playwright
s=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(http.server.SimpleHTTPRequestHandler,directory='/workspace/output/nightchamfer-review'));threading.Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page();q.goto('http://127.0.0.1:8765/library/light.html');q.evaluate('document.fonts.ready')
 print(q.evaluate('''()=>({sheets:[...document.styleSheets].map(s=>({href:s.href,rules:s.cssRules.length,last:s.cssRules[s.cssRules.length-1].cssText.slice(0,200)})),allrules:[...document.styleSheets[1].cssRules].filter(s=>s.cssText.includes('--font-body:')).map(s=>s.cssText.slice(0,300)),styles:[...document.querySelectorAll('[data-el="nightchamfer-cycle"],[data-el="nightchamfer-sankey"],[data-el="nightchamfer-slope"]')].map(e=>({el:e.dataset.el,display:getComputedStyle(e).display,w:e.clientWidth,font:getComputedStyle(e).fontFamily,page:getComputedStyle(e.closest('.slide')).getPropertyValue('--page'),body:getComputedStyle(e.closest('.slide')).getPropertyValue('--font-body')}))})'''))
 b.close()
