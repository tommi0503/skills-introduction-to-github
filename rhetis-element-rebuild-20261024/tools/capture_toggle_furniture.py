from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import json,threading
W=Path('/workspace/work');B=W/'rebuild/toggle-grid/build'
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(W)));threading.Thread(target=server.serve_forever,daemon=True).start()
selectors={'coverTitle':'.slide.cover1>h1,.slide.cover2>h1','coverKicker':'.slide.cover1>.badge','coverLead':'.slide.cover1>p','header':'.slide>.header','headerTitle':'.header>h1','headerBadge':'.header>.badge','headerLead':'.header>small','rail':'.slide>.side','railTitle':'.side>h1','railLabel':'.side>.badge','railLead':'.side>p','top':'.slide>.topline','topDeck':'.topline>span:first-child','topSec':'.topline>span:nth-child(2)','topBrand':'.topline>b','foot':'.slide>.footer,.slide>.bottom','footNo':'.footer>span:first-child','footBrand':'.footer>.company','footSrc':'.bottom>small'}
out={}
with sync_playwright()as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad','--disable-crash-reporter']);page=browser.new_page(viewport={'width':1280,'height':720});cdp=page.context.new_cdp_session(page);cdp.send('DOM.enable');cdp.send('CSS.enable')
 for nn in range(1,13):
  n=f'{nn:02}';page.goto(f'http://127.0.0.1:{server.server_port}/delivery/toggle-grid/review/replica/slide_{n}.html',wait_until='networkidle');page.evaluate('document.fonts.ready');q=page.evaluate('''sels=>{let out={};for(let[k,s]of Object.entries(sels)){let e=document.querySelector(s);if(!e)continue;let b=e.getBoundingClientRect(),c=getComputedStyle(e);out[k]={html:e.outerHTML,text:e.textContent.trim(),bbox:[b.x,b.y,b.width,b.height],style:{font:c.fontFamily,size:c.fontSize,weight:c.fontWeight,line:c.lineHeight,tracking:c.letterSpacing,margin:c.margin,padding:c.padding,border:c.border,background:c.background,color:c.color}}}return out}''',selectors)
  doc=cdp.send('DOM.getDocument')['root']['nodeId']
  for k in ['coverTitle','headerTitle','railTitle']:
   if k not in q:continue
   node=cdp.send('DOM.querySelector',{'nodeId':doc,'selector':selectors[k]})['nodeId'];q[k]['actual_fonts']=cdp.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']
  out[n]=q
 font_html='''<!doctype html><html><head><link rel="stylesheet" href="/rebuild/toggle-grid/review/assets/fonts/fonts.css"><style>@font-face{font-family:SourceOswald;src:url('/delivery/toggle-grid/review/assets/fonts/Oswald-Bold.ttf');font-weight:700}div{font-size:79px;font-weight:700;white-space:nowrap;width:max-content;line-height:86.9px;letter-spacing:-1px}.source{font-family:SourceOswald}.native75{font-family:'Noto Sans';font-stretch:75%}.native100{font-family:'Noto Sans';font-stretch:100%}</style></head><body><div class="source">BRAND STRATEGY GRID</div><div class="native75">BRAND STRATEGY GRID</div><div class="native100">BRAND STRATEGY GRID</div></body></html>'''
 (B/'toggle-font-probe.html').write_text(font_html);page.goto(f'http://127.0.0.1:{server.server_port}/rebuild/toggle-grid/build/toggle-font-probe.html');page.evaluate('document.fonts.ready');out['native_width_probe']=page.evaluate('''()=>[...document.querySelectorAll('body>div')].map(e=>{let s=getComputedStyle(e),b=e.getBoundingClientRect();return{class:e.className,width:b.width,font:s.fontFamily,stretch:s.fontStretch,transform:s.transform}})''');browser.close()
server.shutdown();(B/'source-toggle-furniture.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('source12 apparatus captured; native font probe',out['native_width_probe'])
