import asyncio,json,re,sys,time,os,hashlib
from pathlib import Path
from playwright.async_api import async_playwright
REF=Path('/workspace/work/reference'); OUT=Path('/workspace/output'); WORK=Path('/workspace/work/nightchamfer')
async def audit(name):
 root=OUT/name
 if not (root/'kit/kit.json').exists():return {'name':name,'error':'not ready'}
 kit=json.loads((root/'kit/kit.json').read_text())
 css=(root/'kit'/kit['tokens']).read_text()
 palette=json.loads((REF/'contract/palette.json').read_text())
 css+='\n'+''.join(('.slide.dark' if mode=='dark' else '.slide')+'{'+''.join(k+':'+str(v)+';' for k,v in vals.items())+'}' for mode,vals in palette.items())
 css+='\n.slide{'+''.join(f'--type-{s}:{s}px;' for s in json.loads((REF/'contract/type-steps.json').read_text()))+'}'
 for p in [root/'foundation/foundation.css']+sorted(root.glob('elements/*/element.css')):css+='\n'+p.read_text()
 for p in [root/'foundation/foundation.json']+sorted(root.glob('elements/*/element.json')):
  meta=json.loads(p.read_text());css+='\n'+''.join(meta.get('registrations',{}).values())
  css+='\n.slide{'+''.join(k+':'+v+';' for k,v in meta.get('tokenDefaults',{}).items())+'}'
 pagepath=WORK/'public'/(name+'-audit.html')
 pagepath.write_text('<!doctype html><html lang="ko"><meta charset="UTF-8"><link rel="stylesheet" href="'+'http://127.0.0.1:8765/fonts/fonts.css'+'"><style>'+css+'</style><style>html,body{margin:0;padding:0}section.slide{width:1280px;height:720px}</style><body></body></html>')
 if os.environ.get('RHETIS_PREPARE'):return
 sources={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.suffix in ['.css','.json','.html']}
 result={'source_sha256':sources,'collection':name,'fixtures':0,'tested_states':0,'issues':[],'fonts':[],'resources':[],'contrast_checks':[],'chip_checks':[]}
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1280,'height':720})
  page.on('requestfailed',lambda req:result['resources'].append(req.url))
  await page.goto('http://127.0.0.1:8765/'+pagepath.name);await page.evaluate('document.fonts.ready')
  result['fonts']=await page.evaluate('''() => Array.from(document.fonts).filter(f=>f.status==='error').map(f=>({family:f.family,status:f.status}))''')
  for fixture in sorted(root.glob('elements/*/fixtures/*.html')):
   
   if os.environ.get('NC_SELECT') and fixture.stem not in os.environ['NC_SELECT'].split(','):continue
   raw=fixture.read_text();minimum=re.search(r'<!--\s*min:\s*([^>]+)',raw)
   mins=[tuple(map(int,p)) for p in re.findall(r'(\d+)x(\d+)',minimum.group(1) if minimum else '12x6')]
   body=re.sub(r'<!--.*?-->','',raw,flags=re.S).strip()
   result['fixtures']+=1
   await page.evaluate('(html)=>document.body.innerHTML=html','<section class="slide"><div class="page"><div class="body">'+body+'</div></div></section>')
   # Text may trigger loading a face after mount.
   await page.evaluate('document.fonts.ready')
   sizes=[(c,r) for c in range(1,13) for r in range(1,7) if any(c>=a and r>=b for a,b in mins)]
   for dark in [False,True]:
    await page.locator('.slide').evaluate('(el,dark)=>el.classList.toggle("dark",dark)',dark)
    for c,r in sizes:
     findings=await page.evaluate('''([c,r])=>{
      let body=document.querySelector('.body'),root=body.firstElementChild;
      root.style.gridColumn='1 / span '+c;root.style.gridRow='1 / span '+r;
      let br=body.getBoundingClientRect(),gs=getComputedStyle(body),cs=gs.gridTemplateColumns.split(' ').map(parseFloat),rs=gs.gridTemplateRows.split(' ').map(parseFloat),cw=cs.slice(0,c).reduce((a,b)=>a+b,0)+(c-1)*(parseFloat(gs.columnGap)||0),rh=rs.slice(0,r).reduce((a,b)=>a+b,0)+(r-1)*(parseFloat(gs.rowGap)||0);let box={x:br.x,y:br.y,width:cw,height:rh,left:br.x,top:br.y,right:br.x+cw,bottom:br.y+rh},bad=[],walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
      while(walker.nextNode()){
       let node=walker.currentNode,el=node.parentElement,s=getComputedStyle(el);
       if(!node.textContent.trim()||s.display==='none'||s.visibility==='hidden'||!el.getClientRects().length)continue;
       let range=document.createRange();range.selectNodeContents(node);
       for(let q of range.getClientRects())if(q.width&&q.height&&(q.left<box.left-2||q.right>box.right+2||q.top<box.top-2||q.bottom>box.bottom+2)){
        bad.push({text:node.textContent.trim().slice(0,70),class:el.className,rect:[q.x,q.y,q.width,q.height],box:[box.x,box.y,box.width,box.height]});break;
       }
      }
      return bad.slice(0,5);
     }''',[c,r])
     result['tested_states']+=1
     if findings:result['issues'].append({'fixture':str(fixture.relative_to(root)),'mode':'dark' if dark else 'light','size':[c,r],'text_overflow':findings})
  result['fonts']=await page.evaluate("() => Array.from(document.fonts).filter(f=>f.status==='error').map(f=>({family:f.family,status:f.status}))")
  await browser.close()
 result['issues_count']=len(result['issues'])
 (WORK/(name+'-browser-audit.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2))
 print(name,result['fixtures'],result['tested_states'],'states',len(result['issues']),'issues',flush=True)
 return result
async def main():
 for name in sys.argv[1:]:await audit(name)
import threading,http.server,functools
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
if not os.environ.get('RHETIS_PREPARE'):
 server=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(Quiet,directory='/workspace/work/nightchamfer/public'));threading.Thread(target=server.serve_forever,daemon=True).start()
asyncio.run(main())
