"""Host the contract preview with real font files, export every fixture and PDF."""
import asyncio,functools,json,threading,subprocess,re
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import fitz
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
async def main():
 fontcss=subprocess.check_output(['node','--input-type=module','-e',"import{fontCSS}from'./src/renderer.mjs';process.stdout.write(fontCSS.replaceAll('../../../assets','/assets'))"],cwd=ROOT,text=True)
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start()
 report=[]
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for mode in ['light','dark']:
   await page.goto(f'http://127.0.0.1:{server.server_port}/collection/business-prism/{mode}.html')
   await page.add_style_tag(content=fontcss)
   await page.evaluate('''()=>{const slides=[...document.querySelectorAll('article > .frame > .slide')].map(s=>s.outerHTML).join('');document.body.innerHTML=slides;}''')
   await page.add_style_tag(content='html,body{padding:0!important;margin:0!important;display:block!important;background:white!important}.slide{width:1280px!important;height:720px!important;transform:none!important;break-after:page}@page{size:1280px 720px;margin:0}@media print{.slide{print-color-adjust:exact;-webkit-print-color-adjust:exact}.slide:last-child{break-after:auto}}')
   await page.evaluate('document.fonts.ready');await page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
   out=ROOT/'renders/library'/mode;out.mkdir(parents=True,exist_ok=True)
   slides=page.locator('section.slide');count=await slides.count()
   for i in range(count):await slides.nth(i).screenshot(path=str(out/f'fixture-{i+1:03}.png'))
   fonts=await page.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>({family:f.family,weight:f.weight}))")
   raw=await page.pdf(width='1280px',height='720px',print_background=True,prefer_css_page_size=True)
   doc=fitz.open();src=fitz.open(stream=raw,filetype='pdf')
   for i in range(len(src)):
    pg=doc.new_page(width=1280,height=720);pg.show_pdf_page(pg.rect,src,i)
   doc.save(ROOT/'pdfs'/f'library-{mode}.pdf',deflate=True);doc.close();src.close()
   report.append({'mode':mode,'count':count,'loadedFonts':fonts});print(mode,count,'fixtures exported',flush=True)
  await browser.close()
 server.shutdown();(ROOT/'review/library-host-fonts.json').write_text(json.dumps(report,indent=2))
asyncio.run(main())
