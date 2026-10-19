"""Browser render and geometry audit for every Spectrum fixture, both modes and minima."""
import asyncio, json, re, hashlib, threading, functools, argparse
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.async_api import async_playwright
BASE=Path(__file__).resolve().parents[1]
COL=BASE/'collection/rhetis-spectrum'
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
async def main():
 css='\n'.join(p.read_text() for p in [COL/'kit/css/tokens.css',COL/'foundation/foundation.css',*sorted(COL.glob('elements/*/element.css'))])
 css+='\n.slide{'+''.join(f'--type-{n}:{n}px;' for n in json.loads((BASE/'contract/type-steps.json').read_text()))+'}\n'
 for weight,file in [(400,'Pretendard-Regular.woff2'),(600,'Pretendard-SemiBold.woff2'),(700,'Pretendard-Bold.woff2')]:css+=f'@font-face{{font-family:"Pretendard";font-weight:{weight};src:url("/assets/fonts/{file}")}}'
 css+='@font-face{font-family:"Gmarket Sans";font-weight:700;src:url("/assets/fonts/GmarketSansBold.woff")}body{margin:0;}'
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(BASE)));threading.Thread(target=server.serve_forever,daemon=True).start()
 out=BASE/'renders/library';out.mkdir(parents=True,exist_ok=True)
 results=[]
 old_report=BASE/'review/library-automatic.json'
 selected=None
 if len(__import__('sys').argv)>1:selected=set(__import__('sys').argv[1].split(','))
 if selected and old_report.exists():results=[x for x in json.loads(old_report.read_text()) if x['fixture'].split('/')[1] not in selected]
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  await page.goto(f'http://127.0.0.1:{server.server_port}/')
  for fixture in sorted(COL.glob('**/fixtures/*.html')):
   
   if selected and fixture.parent.parent.name not in selected:continue
   src=fixture.read_text();minimum=re.search(r'min:\s*(\d+)x(\d+)',src).groups();kind=fixture.parent.parent.name
   for mode in ['light','dark']:
    for size in ['full','minimum']:
     body=re.sub(r'<!--.*?-->','',src,flags=re.S).strip()
     if body.startswith('<section'):
      body=body.replace('class="slide',f'class="slide {"dark" if mode=="dark" else ""}',1)
      if size=='minimum':continue
     else:
      if size=='minimum':body=body.replace('grid-column:1 / span 12; grid-row:1 / span 6',f'grid-column:1 / span {minimum[0]}; grid-row:1 / span {minimum[1]}',1)
      body=f'<section class="slide {"dark" if mode=="dark" else ""}"><div class="page"><div class="body">{body}</div></div></section>'
     await page.set_content('<!doctype html><html lang="ko"><meta charset="utf-8"><style>'+css+'</style><body>'+body+'</body></html>')
     await page.evaluate('Promise.all([...document.fonts].map(f=>f.load()))');await page.evaluate('document.fonts.ready');await page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
     findings=await page.evaluate('''()=>{let out=[];const root=document.querySelector('[data-el]'),slide=document.querySelector('.slide'),r=root?.getBoundingClientRect();for(const el of document.querySelectorAll('.slide *')){if(!el.childNodes.length||![...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))continue;const s=getComputedStyle(el);if(s.display==='none'||!el.getClientRects().length)continue;const range=document.createRange();range.selectNodeContents(el);const t=range.getBoundingClientRect();if(r&&(t.left<r.left-2||t.right>r.right+2||t.top<r.top-2||t.bottom>r.bottom+2))out.push({type:'text-outside-root',text:el.textContent,box:[t.x,t.y,t.width,t.height],root:[r.x,r.y,r.width,r.height]});if(!document.fonts.check(s.fontWeight+' '+s.fontSize+' '+s.fontFamily))out.push({type:'font-load',text:el.textContent});}return{findings:out,size:[slide.offsetWidth,slide.offsetHeight],fonts:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status})),anchors:CSS.supports('top','anchor(--x bottom)')}}''')
     dest=out/mode/size/(kind+'--'+fixture.stem+'.png');dest.parent.mkdir(parents=True,exist_ok=True);await page.screenshot(path=str(dest))
     findings.update({'fixture':str(fixture.relative_to(COL)),'mode':mode,'variant':size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()});results.append(findings)
   print(kind,fixture.stem,flush=True)
  await browser.close()
 server.shutdown();(BASE/'review/library-automatic.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print('Rendered',len(results),'views;',sum(len(x['findings']) for x in results),'findings')
asyncio.run(main())
