import asyncio,json,threading,functools,hashlib
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
async def main():
 srv=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)));threading.Thread(target=srv.serve_forever,daemon=True).start()
 findings=[]
 async with async_playwright() as pw:
  b=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);p=await b.new_page(viewport={'width':1280,'height':720})
  for f in sorted((ROOT/'build/assembly').glob('*/*slide_*.html')):
   await p.goto('http://127.0.0.1:'+str(srv.server_port)+'/'+str(f.relative_to(ROOT)));await p.wait_for_selector('body[data-ready="true"]')
   result=await p.evaluate('''()=>{let issues=[];for(let el of document.querySelectorAll('.name,.note,.fig,.kick,.title,.lead,.kicker,.chip,.entry>.mark,.key,.pt>b,.pt>span,.bar>b,.bar>span,th,td,.callout>p,blockquote')){let s=getComputedStyle(el);if(s.display==='none'||s.visibility==='hidden'||!el.textContent.trim())continue;let r=document.createRange();r.selectNodeContents(el);let q=r.getBoundingClientRect(),e=el.getBoundingClientRect(),root=el.closest('[data-el]'),v=root?.getBoundingClientRect();if(q.width===0||q.height===0)continue;if(q.left<-.8||q.top<-.8||q.right>1280.8||q.bottom>720.8)issues.push({type:'outside-canvas',text:el.textContent,rect:[q.left,q.top,q.right,q.bottom]});if(v&&(q.left<v.left-2||q.top<v.top-4||q.right>v.right+2||q.bottom>v.bottom+4))issues.push({type:'outside-component',text:el.textContent,el:root.dataset.el,component:[v.x,v.y,v.width,v.height],textRect:[q.x,q.y,q.width,q.height]});if(!document.fonts.check(s.fontWeight+' '+s.fontSize+' '+s.fontFamily))issues.push({type:'font-load',text:el.textContent})}for(let el of document.querySelectorAll('[data-el]'))if(el.scrollHeight>el.clientHeight+3||el.scrollWidth>el.clientWidth+3)issues.push({type:'scroll-overflow',el:el.dataset.el,size:[el.clientWidth,el.clientHeight,el.scrollWidth,el.scrollHeight]});return {issues,elementCount:document.querySelectorAll('[data-el]').length}}''')
   findings.append({'path':str(f.relative_to(ROOT)),**result})
  await b.close()
 srv.shutdown();out={'pages':findings,'issueCount':sum(len(x['issues']) for x in findings),'pageCount':len(findings)};(ROOT/'review/assembly-layout-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps({'pageCount':out['pageCount'],'issueCount':out['issueCount'],'problemPages':[{ 'path':x['path'],'issues':x['issues']} for x in findings if x['issues']]},ensure_ascii=False,indent=2))
asyncio.run(main())
