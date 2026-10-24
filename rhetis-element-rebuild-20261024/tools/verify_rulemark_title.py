from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import threading,json,hashlib,sys
from playwright.sync_api import sync_playwright
from sheets import context
from font_qa import actual_fonts
R=Path('/workspace/work/rebuild');D=R/'rulemark/build/title-qa';D.mkdir(exist_ok=True)
html='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../review/assets/fonts/fonts.css"><style>'+context('rulemark')+'</style></head><body><section class="slide"><div class="page"><header class="head" style="--rulemark-furn-x:66px;--rulemark-furn-y:144px;--rulemark-furn-w:167.27px;--rulemark-furn-h:58px"><h1 class="title">핵심 요소</h1></header></div></section></body></html>'
(D/'source04.html').write_text(html)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory='/workspace/work'));threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright()as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720});cdp=pg.context.new_cdp_session(pg);cdp.send('DOM.enable');cdp.send('CSS.enable');report={}
 for name,url,selector in [('source','/delivery/rulemark/review/replica/slide_04.html','.slide>.title'),('foundation','/rebuild/rulemark/build/title-qa/source04.html','.head>.title')]:
  pg.goto(f'http://127.0.0.1:{server.server_port}'+url);pg.evaluate('document.fonts.ready');qa=pg.locator(selector).evaluate("""e=>{let c=getComputedStyle(e),q=e.getBoundingClientRect(),r=document.createRange();r.selectNodeContents(e);let a=[...r.getClientRects()].filter(x=>x.width);return{text:e.textContent,font:c.fontFamily,size:c.fontSize,weight:c.fontWeight,line:c.lineHeight,tracking:c.letterSpacing,whiteSpace:c.whiteSpace,bbox:[q.x,q.y,q.width,q.height],text_rects:a.map(x=>[x.x,x.y,x.width,x.height]),line_count:new Set(a.map(x=>Math.round(x.y))).size,loaded:document.fonts.check(c.font,c.fontFamily)}}""");qa['actual_fonts']=actual_fonts(pg,cdp);report[name]=qa;pg.screenshot(path=str(D/(name+'.png')))
 b.close()
server.shutdown();report['source_hashes']={str(x.relative_to(R/'rulemark')):hashlib.sha256(x.read_bytes()).hexdigest()for x in [R/'rulemark/rulemark/foundation/foundation.css',R/'rulemark/rulemark/kit/kit.json']};report['passed']=all(x['size']=='48px'and x['weight']=='750'and abs(float(x['line'][:-2])-60)<.001 and x['tracking']=='-1.92px'and x['line_count']==1 and not x['actual_fonts']['load_errors']for k,x in report.items()if k in ['source','foundation']);(R/'rulemark/review/validation/foundation-title-source04.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
