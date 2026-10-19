import asyncio, json, threading, functools, re, hashlib
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.async_api import async_playwright
B=Path(__file__).resolve().parents[1];C=B/'collection/business-spectrum';OUT=B/'renders/library';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
async def main():
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(B)));threading.Thread(target=server.serve_forever,daemon=True).start()
 report=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for mode in ['light','dark']:
   await page.goto(f'http://127.0.0.1:{server.server_port}/build/library/{mode}.html')
   fonts=''.join(f"@font-face{{font-family:Pretendard;font-weight:{w};font-style:normal;src:url('/assets/fonts/Pretendard-{w}.woff2')}}" for w in [300,400,500,600,700,800,900])
   # Actual host filenames may use weight names, inspect and resolve.
   fontfiles=list((B/'assets/fonts').glob('*.woff2'))
   if fontfiles:
    fonts=''
    for f in fontfiles:
     weight=next((w for name,w in [('ExtraLight',200),('SemiBold',600),('ExtraBold',800),('Light',300),('Regular',400),('Medium',500),('Bold',700),('Black',900),('Thin',100)] if name.lower() in f.name.lower()),None)
     if weight:fonts+=f"@font-face{{font-family:Pretendard;font-weight:{weight};font-style:normal;src:url('/assets/fonts/{f.name}')}}"
   await page.add_style_tag(content=fonts+'body{padding:0;display:block}article{display:none;margin:0}article.active{display:block}h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
   await page.evaluate('document.fonts.ready');n=await page.locator('article').count()
   for i in range(n):
    await page.evaluate('(i)=>{document.querySelectorAll("article").forEach((a,j)=>a.classList.toggle("active",i===j))}',i)
    article=page.locator('article').nth(i);title=await article.locator('h2').inner_text();slug=title.split(' min ')[0].replace(' / ','--').replace('/','-').strip()
    for size in ['full','min']:
     if size=='min':
      m=re.search(r'min (\d+)x(\d+)',title)
      if not m:continue
      cols,rows=map(int,m.groups())
      await article.evaluate('(a,sz)=>{let r=a.querySelector(".body")?.firstElementChild;if(r){r.style.gridColumn=`1 / span ${sz[0]}`;r.style.gridRow=`1 / span ${sz[1]}`}}',[cols,rows])
     await page.evaluate('document.fonts.ready');await page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
     issues=await article.evaluate('''a=>{let slide=a.querySelector('.slide'),root=slide.querySelector('.body')?.firstElementChild??slide,q=root.getBoundingClientRect(),issues=[];for(const e of root.querySelectorAll('*')){if(!e.textContent.trim()||!Array.from(e.childNodes).some(n=>n.nodeType===3&&n.textContent.trim()))continue;let s=getComputedStyle(e),r=e.getBoundingClientRect();if(s.display==='none'||!r.width||!r.height)continue;let rr=document.createRange();rr.selectNodeContents(e);let t=rr.getBoundingClientRect();if(t.left<q.left-2||t.right>q.right+2||t.top<q.top-2||t.bottom>q.bottom+2)issues.push({type:'root-text-overflow',cls:e.className,text:e.textContent,root:[q.x,q.y,q.width,q.height],box:[t.x,t.y,t.width,t.height]});if(!document.fonts.check(s.fontWeight+' '+s.fontSize+' '+s.fontFamily))issues.push({type:'font-failure',cls:e.className});}let textBoxes=Array.from(root.querySelectorAll('*')).filter(e=>e.textContent.trim()&&Array.from(e.childNodes).some(n=>n.nodeType===3&&n.textContent.trim())&&getComputedStyle(e).display!=='none').map(e=>{let z=document.createRange();z.selectNodeContents(e);return{e,r:z.getBoundingClientRect()}}).filter(x=>x.r.width&&x.r.height);for(let i=0;i<textBoxes.length;i++)for(let j=i+1;j<textBoxes.length;j++){let a=textBoxes[i],b=textBoxes[j];if(a.e.contains(b.e)||b.e.contains(a.e))continue;let w=Math.min(a.r.right,b.r.right)-Math.max(a.r.left,b.r.left),h=Math.min(a.r.bottom,b.r.bottom)-Math.max(a.r.top,b.r.top);if(w>3&&h>3&&w*h>Math.min(a.r.width*a.r.height,b.r.width*b.r.height)*.2)issues.push({type:'text-overlap',a:a.e.textContent,b:b.e.textContent});}let b=slide.getBoundingClientRect();return{size:[b.width,b.height],root:[q.width,q.height],issues,fontReady:document.fonts.check('700 20px Pretendard')}}''')
     target=OUT/mode/size/(slug+'.png');target.parent.mkdir(parents=True,exist_ok=True);await article.locator('.slide').screenshot(path=str(target));report.append(dict(mode=mode,fixture=slug,variant=size,sha256=hashlib.sha256(target.read_bytes()).hexdigest(),**issues))
    if i%20==0:print(mode,i,n,flush=True)
   # full sheet in standard sheet format after the individual checks
  await browser.close()
 server.shutdown()
 (OUT/'automatic.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 hashes={str(f.relative_to(C)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(C.rglob('*')) if f.is_file() and f.suffix in ['.css','.json','.html'] and 'previews' not in f.parts and not f.name.startswith('preview-')};(OUT/'source-hashes.json').write_text(json.dumps(hashes,indent=2))
 print('Checked',len(report),'fixture renders; issues',sum(len(r['issues']) for r in report),flush=True)
asyncio.run(main())
