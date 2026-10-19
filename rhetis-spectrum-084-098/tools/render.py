import argparse,asyncio,json,hashlib,threading,functools
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from PIL import Image,ImageDraw
import fitz
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
class QuietHandler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
async def main():
 p=argparse.ArgumentParser();p.add_argument('--deck');p.add_argument('--round',default='final');p.add_argument('--assembly',action='store_true');a=p.parse_args();mode='assembly' if a.assembly else 'replica';rd=f'round{a.round}' if a.round!='final' else 'final';decks=[a.deck] if a.deck else sorted(d.name for d in (ROOT/'build'/mode).iterdir() if d.is_dir())
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(QuietHandler,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{server.server_port}/'
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  for deck in decks:
   out=ROOT/'renders'/rd/mode/deck;out.mkdir(parents=True,exist_ok=True);cmp=ROOT/'comparisons'/rd/mode/deck;cmp.mkdir(parents=True,exist_ok=True);reports=[]
   for f in sorted((ROOT/'build'/mode/deck).glob('slide_*.html')):
    await page.goto(base+str(f.relative_to(ROOT)));await page.wait_for_selector('body[data-ready="true"]');await page.evaluate('document.fonts.ready');await page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
    findings=await page.evaluate('''()=>{const issues=[],slide=document.querySelector('.slide'),b=slide.getBoundingClientRect();for(const el of document.querySelectorAll('[data-kind="text"], [data-kind="pill"]')){const r=document.createRange();r.selectNodeContents(el);const t=r.getBoundingClientRect(),q=el.getBoundingClientRect(),s=getComputedStyle(el);if(t.left<-.8||t.top<-.8||t.right>1280.8||t.bottom>720.8)issues.push({node:el.dataset.node,type:'outside-canvas',text:el.textContent});if(t.width>q.width+2||t.height>q.height+2)issues.push({node:el.dataset.node,type:'text-box-overflow',text:el.textContent,box:[q.width,q.height],textSize:[t.width,t.height]});if(!document.fonts.check(s.fontWeight+' '+s.fontSize+' '+s.fontFamily))issues.push({node:el.dataset.node,type:'font-load'});if(el.dataset.kind==='pill'){let l=el.querySelector('[data-chip-label]'),v=l.getBoundingClientRect(),c=document.createElement('canvas').getContext('2d');c.font=s.fontWeight+' '+s.fontSize+' '+s.fontFamily;let m=c.measureText(l.textContent),dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2,dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2;let offset=[v.x+v.width/2+dx-q.x-q.width/2-(parseFloat(s.paddingLeft)-parseFloat(s.paddingRight))/2,v.y+v.height/2+dy-q.y-q.height/2];if(offset.some(x=>Math.abs(x)>1.3))issues.push({node:el.dataset.node,type:'chip-center',offset})}}return{size:[b.width,b.height],fonts:Array.from(document.fonts).map(f=>({family:f.family,weight:f.weight,status:f.status})),findings:issues,sourceImageTags:slide.querySelectorAll('img,image').length}}''')
    dest=out/(f.stem+'.png');await page.locator('.slide').screenshot(path=str(dest));findings.update({'slide':f.stem,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'htmlSha256':hashlib.sha256(f.read_bytes()).hexdigest()});reports.append(findings)
    original=Image.open(ROOT/'references'/deck/(f.stem+'.png')).convert('RGB');result=Image.open(dest).convert('RGB');pair=Image.new('RGB',(2560,752),'#e6e7eb');pair.paste(original,(0,32));pair.paste(result,(1280,32));draw=ImageDraw.Draw(pair);draw.text((16,8),f'{deck} / {f.stem} | REFERENCE',fill='black');draw.text((1296,8),f'{mode.upper()} | {rd}',fill='black');pair.save(cmp/(f.stem+'.jpg'),quality=86)
   report={'deck':deck,'mode':mode,'round':rd,'errors':errors,'slides':reports,'sourceHash':hashlib.sha256((ROOT/'src/decks'/(deck+'.mjs')).read_bytes()).hexdigest(),'sourceBundleHash':hashlib.sha256(b''.join(p.read_bytes() for p in sorted((ROOT/'src').rglob('*')) if p.is_file())).hexdigest(),'rendererHash':hashlib.sha256((ROOT/'src/renderer.mjs').read_bytes()).hexdigest(),'primitiveHash':hashlib.sha256((ROOT/'src/primitives.mjs').read_bytes()).hexdigest(),'assemblyCompilerHash':hashlib.sha256((ROOT/'src/assembly.mjs').read_bytes()).hexdigest(),'collectionHash':hashlib.sha256(b''.join(p.read_bytes() for p in sorted((ROOT/'collection/spectrum-brief').rglob('*')) if p.is_file())).hexdigest()};(ROOT/'review'/f'automatic-{rd}-{mode}-{deck}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(deck,mode,len(reports),'rendered,',sum(len(r['findings'])for r in reports),'findings',flush=True)
   if rd=='final':
    pdf=ROOT/'pdfs'/mode;pdf.mkdir(parents=True,exist_ok=True);await page.goto(base+f'build/{mode}/{deck}/all.html');await page.wait_for_selector('body[data-ready="true"]');raw=await page.pdf(width='1280px',height='720px',print_background=True,prefer_css_page_size=True)
    srcpdf=fitz.open(stream=raw,filetype='pdf');doc=fitz.open()
    for idx in range(len(srcpdf)):
     pg=doc.new_page(width=1280,height=720);pg.show_pdf_page(pg.rect,srcpdf,idx)
    doc.save(pdf/(deck+'.pdf'));doc.close();srcpdf.close()
  await browser.close()
 server.shutdown()
asyncio.run(main())
