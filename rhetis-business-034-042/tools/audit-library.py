import asyncio,json,threading,functools,re,hashlib,sys
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.async_api import async_playwright
B=Path(__file__).resolve().parents[1];C=B/'collection/business-spectrum';OUT=B/'renders/library'
ONLY=set(sys.argv[1].split(',')) if len(sys.argv)>1 else set()
class Q(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
CHECK=r'''a=>{let slide=a.querySelector('.slide'),root=slide.querySelector('.body')?.firstElementChild??slide,q=root.getBoundingClientRect(),issues=[],boxes=[],contrasts=[];function rgb(x){let a=(x.match(/[\d.]+/g)||[]).map(Number);if(x.startsWith('color(srgb'))a=a.map((v,i)=>i<3?v*255:v);return a}function mix(f,b){let alpha=f.length>3?f[3]:1;return f.slice(0,3).map((v,i)=>v*alpha+b[i]*(1-alpha))}function luminance(c){let v=c.map(z=>{z/=255;return z<=.04045?z/12.92:((z+.055)/1.055)**2.4});return .2126*v[0]+.7152*v[1]+.0722*v[2]}for(let e of [root,...root.querySelectorAll('*')]){if(!e.textContent.trim()||!Array.from(e.childNodes).some(n=>n.nodeType===3&&n.textContent.trim()))continue;let s=getComputedStyle(e),r=e.getBoundingClientRect();if(s.display==='none'||!r.width||!r.height)continue;let z=document.createRange();z.selectNodeContents(e);let t=z.getBoundingClientRect();if(t.left<q.left-2||t.right>q.right+2||t.top<q.top-2||t.bottom>q.bottom+2)issues.push({type:'root-text-overflow',cls:e.className,text:e.textContent});if(!document.fonts.check(s.fontWeight+' '+s.fontSize+' '+s.fontFamily))issues.push({type:'font-failure',cls:e.className});boxes.push({e,r:t});let chain=[],p=e;while(p){chain.unshift(p);if(p===slide)break;p=p.parentElement;}let bg=[255,255,255];for(let n of chain){let br=n.getBoundingClientRect(),cx=t.x+t.width/2,cy=t.y+t.height/2;if(cx<br.left||cx>br.right||cy<br.top||cy>br.bottom)continue;let c=rgb(getComputedStyle(n).backgroundColor);if(c.length>=3)bg=mix(c,bg);}let fg=rgb(s.color),L1=luminance(fg),L2=luminance(bg),contrast=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05),threshold=parseFloat(s.fontSize)>=28?3:4.5;contrasts.push({text:e.textContent,contrast:Number(contrast.toFixed(2)),size:parseFloat(s.fontSize)});if(contrast<threshold-.05)issues.push({type:'contrast',cls:e.className,text:e.textContent,ratio:contrast,threshold});}for(let i=0;i<boxes.length;i++)for(let j=i+1;j<boxes.length;j++){let a=boxes[i],b=boxes[j];if(a.e.contains(b.e)||b.e.contains(a.e))continue;let w=Math.min(a.r.right,b.r.right)-Math.max(a.r.left,b.r.left),h=Math.min(a.r.bottom,b.r.bottom)-Math.max(a.r.top,b.r.top);if(w>3&&h>3&&w*h>Math.min(a.r.width*a.r.height,b.r.width*b.r.height)*.2)issues.push({type:'text-overlap',a:a.e.textContent,b:b.e.textContent});}let chip=null;if(root.matches('.pill,.tag,.hl')){let target=root.querySelector('.parts')??root,cr=target.getBoundingClientRect();chip={offset:[(cr.left+cr.right-q.left-q.right)/2,(cr.top+cr.bottom-q.top-q.bottom)/2]};if(chip.offset.some(v=>Math.abs(v)>1.3))issues.push({type:'chip-center',offset:chip.offset});}let b=slide.getBoundingClientRect();return{chip,size:[b.width,b.height],root:[q.width,q.height],issues,contrasts,fontReady:document.fonts.check('700 20px Pretendard')}}'''
async def main():
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory=str(B)));threading.Thread(target=server.serve_forever,daemon=True).start();report=[r for r in json.loads((OUT/'automatic-final.json').read_text()) if r['fixture'].split('--')[0] not in ONLY] if ONLY else []
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  fonts=''
  for f in (B/'assets/fonts').glob('Pretendard-*.woff2'):
   w=next((w for n,w in [('ExtraLight',200),('SemiBold',600),('ExtraBold',800),('Light',300),('Regular',400),('Medium',500),('Bold',700),('Black',900),('Thin',100)] if n.lower() in f.name.lower()),None)
   if w:fonts+=f"@font-face{{font-family:Pretendard;font-weight:{w};font-style:normal;src:url('/assets/fonts/{f.name}')}}"
  for mode in ['light','dark']:
   await page.goto(f'http://127.0.0.1:{server.server_port}/build/library/{mode}.html')
   await page.add_style_tag(content=fonts+'body{padding:0;display:block}article{display:none;margin:0}article.active{display:block}h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
   n=await page.locator('article').count()
   for i in range(n):
    article=page.locator('article').nth(i);await page.evaluate('(i)=>document.querySelectorAll("article").forEach((a,j)=>a.classList.toggle("active",i===j))',i);title=await article.locator('h2').inner_text();slug=title.split(' min ')[0].replace(' / ','--').replace('/','-').strip()
    if ONLY and slug.split('--')[0] not in ONLY:continue
    for size in ['full','min']:
     if size=='min':
      m=re.search(r'min (\d+)x(\d+)',title)
      if not m:continue
      await article.evaluate('(a,s)=>{let r=a.querySelector(".body")?.firstElementChild;if(r){r.style.gridColumn=`1 / span ${s[0]}`;r.style.gridRow=`1 / span ${s[1]}`}}',list(map(int,m.groups())))
     await page.evaluate('document.fonts.ready');await page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');result=await article.evaluate(CHECK)
     png=OUT/mode/size/(slug+'.png')
     if slug.split('--')[0] in ['tag','pill','hub','cycle','foundation','quote','person','logo-group','image-frame']:await article.locator('.slide').screenshot(path=str(png))
     report.append(dict(mode=mode,fixture=slug,variant=size,sha256=hashlib.sha256(png.read_bytes()).hexdigest(),**result))
   # Export all full-size fixture pages after the individual audit.
   await page.evaluate('''()=>{document.querySelectorAll('article').forEach(a=>{a.classList.add('active');let r=a.querySelector('.body')?.firstElementChild;if(r){r.style.gridColumn='1 / span 12';r.style.gridRow='1 / span 6';}})}''')
   await page.add_style_tag(content='@page{size:1280px 720px;margin:0}article{break-after:page;height:720px;overflow:hidden}.frame{height:720px}body{margin:0}')
   await page.pdf(path=str(OUT/f'library-{mode}.pdf'),width='1280px',height='720px',print_background=True,prefer_css_page_size=True)
   print(mode,'audited',n,flush=True)
  await browser.close()
 server.shutdown();(OUT/'automatic-final.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));hashes={str(f.relative_to(C)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(C.rglob('*')) if f.is_file() and f.suffix in ['.css','.json','.html'] and 'previews' not in f.parts and not f.name.startswith('preview-')};(OUT/'source-hashes.json').write_text(json.dumps(hashes,indent=2));print('Final findings:',sum(len(r['issues']) for r in report),flush=True)
asyncio.run(main())
