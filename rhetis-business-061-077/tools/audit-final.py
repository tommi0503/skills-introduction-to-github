"""Independent final browser audit and render freshness evidence."""
import asyncio,functools,hashlib,json,threading
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
async def main():
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)))
 threading.Thread(target=server.serve_forever,daemon=True).start()
 records=[]
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for mode in ['replica','assembly']:
   for html in sorted((ROOT/'build'/mode).glob('*/slide_*.html')):
    errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
    await page.goto(f'http://127.0.0.1:{server.server_port}/'+str(html.relative_to(ROOT)))
    await page.wait_for_selector('body[data-ready="true"]')
    await page.evaluate('document.fonts.ready')
    result=await page.evaluate('''()=>{
     const root=document.querySelector('.slide'),b=root.getBoundingClientRect(),issues=[];
     const all=[...root.querySelectorAll('[data-kind="text"],[data-kind="pill"],.name,.note,.fig,.title,.kicker,.lead,th,td,.entry>.mark')];
     for(const el of all){const box=el.closest('[data-kind="pill"]')||el,q=box.getBoundingClientRect(),s=getComputedStyle(el);if(q.width===0||q.height===0||s.visibility==='hidden'||s.display==='none')continue;
      const range=document.createRange();range.selectNodeContents(el);const r=range.getBoundingClientRect();const id=el.dataset.node||el.className;
      if(r.width&&r.height&&(r.left<-.8||r.top<-.8||r.right>1280.8||r.bottom>720.8))issues.push({type:'text-outside-canvas',id,text:el.textContent});
      if(r.width>q.width+2||r.height>q.height+2)issues.push({type:'text-box-overflow',id,text:el.textContent,box:[q.width,q.height],range:[r.width,r.height]});
      if(!document.fonts.check(s.fontWeight+' '+s.fontSize+' '+s.fontFamily))issues.push({type:'font-load',id});
      let parent=el.parentElement;while(parent&&parent!==root){const ps=getComputedStyle(parent),pr=parent.getBoundingClientRect();if(['hidden','clip'].includes(ps.overflow)&&r.height&&r.width&&(r.bottom>pr.bottom+2||r.right>pr.right+2||r.top<pr.top-2||r.left<pr.left-2)){issues.push({type:'clipping-parent',id,parent:parent.className,text:el.textContent});break;}parent=parent.parentElement;}
     }
     for(const el of root.querySelectorAll('[data-kind="pill"]')){let l=el.querySelector('[data-chip-label]');if(!l)continue;let q=el.getBoundingClientRect(),v=l.getBoundingClientRect(),s=getComputedStyle(el),c=document.createElement('canvas').getContext('2d');c.font=s.fontWeight+' '+s.fontSize+' '+s.fontFamily;let m=c.measureText(l.textContent),dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2,dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2;let d=[v.x+v.width/2+dx-q.x-q.width/2,v.y+v.height/2+dy-q.y-q.height/2];if(d.some(x=>Math.abs(x)>1.3))issues.push({type:'chip-optical-center',id:el.dataset.node,offset:d});}
     return{size:[b.width,b.height],issues,loadedFonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>({family:f.family,weight:f.weight})),sourceImageCount:root.querySelectorAll('img,image').length,contracts:[...new Set([...root.querySelectorAll('[data-el]')].map(e=>e.dataset.el))]};
    }''')
    imagepath=ROOT/'renders/final'/mode/html.parent.name/(html.stem+'.png')
    result.update({'mode':mode,'deck':html.parent.name,'slide':html.stem,'errors':errors,'htmlSha256':digest(html),'renderSha256':digest(imagepath),'pngSize':list(Image.open(imagepath).size)})
    records.append(result)
   print(mode,'audited',sum(r['mode']==mode for r in records),'pages',flush=True)
  await browser.close()
 server.shutdown()
 report={'pages':len(records),'issues':sum(len(r['issues'])+len(r['errors']) for r in records),'sourceHashes':{str(p.relative_to(ROOT)):digest(p) for p in sorted((ROOT/'src').rglob('*.mjs'))},'records':records}
 (ROOT/'review/final-browser-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print('Final issues:',report['issues'])
asyncio.run(main())
