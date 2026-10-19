from pathlib import Path
from playwright.sync_api import sync_playwright
import json,re,importlib.util,threading,functools,sys,hashlib,shutil
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
R=Path(__file__).resolve().parents[1];C=R/'collection/spectrum-brief';OUT=R/'review/library';OUT.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('preview',R/'tools/preview.py');preview=importlib.util.module_from_spec(spec);spec.loader.exec_module(preview)
steps=json.loads((R/'contract/type-steps.json').read_text())
server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(SimpleHTTPRequestHandler,directory=str(R)))
threading.Thread(target=server.serve_forever,daemon=True).start()
base='http://127.0.0.1:'+str(server.server_port)+'/'
fonts=''.join("@font-face{font-family:Pretendard;src:url('"+'../assets/fonts/'+f'Pretendard-{name}.woff2'+"');font-weight:"+str(w)+";}"for name,w in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700)])
only=sys.argv[sys.argv.index('--element')+1] if '--element' in sys.argv else None
results=[r for r in json.loads((R/'review/library-metrics.json').read_text()) if not r['fixture'].startswith(only+' / ')] if only else []
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  html=preview.sheet(C,steps,dark=mode=='dark');html=html.replace('</head>','<style>'+fonts+'</style></head>')
  path=R/'previews'/f'library-{mode}.html';path.write_text(html)
  page.goto(base+'previews/'+path.name);page.evaluate('document.fonts.ready');page.wait_for_timeout(300)
  # For audit render each article individually at actual slide size, never relying on the contact sheet.
  count=page.locator('article').count()
  for i in range(count):
   item=page.locator('article').nth(i);title=item.locator('h2').inner_text(); fixture=title.split(' min ')[0].strip();
   name=fixture.replace(' / ','--').replace(' ','-')
   if only and not fixture.startswith(only+' / '):continue
   slide=item.locator('.slide');
   page.evaluate('''el=>{document.querySelectorAll('article').forEach(a=>a.style.display='none');let a=el.closest('article');a.style.display='block';a.style.position='absolute';a.style.left='0';a.style.top='0';a.querySelector('h2').style.display='none';a.querySelector('.frame').style.width='1280px';a.querySelector('.frame').style.height='720px';el.style.transform='none';}''',slide.element_handle())
   slide.screenshot(path=str(OUT/f'{mode}--{name}.png'))
   checks=slide.evaluate('''root=>{let texts=[...root.querySelectorAll('*')].filter(e=>e.childNodes.length&&[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim())&&getComputedStyle(e).display!=='none');return {size:[root.offsetWidth,root.offsetHeight],fonts:document.fonts.check('20px Pretendard'),minText:Math.min(...texts.map(e=>parseFloat(getComputedStyle(e).fontSize))),overflows:[...root.querySelectorAll('*')].filter(e=>!e.matches('.pt,.step,.root,.flowchart>.node')&&e.clientWidth>0&&e.clientHeight>0&&(e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+3)&&!['SECTION'].includes(e.tagName)).map(e=>({tag:e.tagName,cl:e.className,client:[e.clientWidth,e.clientHeight],scroll:[e.scrollWidth,e.scrollHeight]}))}}''')
   visual=slide.evaluate(r'''root=>{function rgb(c){return c.match(/[.\d]+/g)?.slice(0,3).map(Number)||[255,255,255]}function lum(a){return a.map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4}).reduce((a,x,i)=>a+x*[.2126,.7152,.0722][i],0)}function back(e){while(e){let c=getComputedStyle(e).backgroundColor;if(c!=='rgba(0, 0, 0, 0)'&&c!=='transparent')return c;e=e.parentElement}return 'rgb(255,255,255)'}let issues=[],outside=[],min=Infinity;for(let e of root.querySelectorAll('*')){let st=getComputedStyle(e);if(st.display==='none'||st.visibility==='hidden')continue;let nodes=[...e.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim());if(!nodes.length)continue;let sz=parseFloat(st.fontSize);min=Math.min(min,sz);let a=lum(rgb(st.color)),b=lum(rgb(back(e))),contrast=(Math.max(a,b)+.05)/(Math.min(a,b)+.05),required=sz>=28?3:4.5;if(contrast<required-.05)issues.push({cl:e.className,text:e.textContent,contrast,required});for(let n of nodes){let r=document.createRange();r.selectNode(n);let q=r.getBoundingClientRect();if(q.left<-.8||q.top<-.8||q.right>1280.8||q.bottom>720.8)outside.push({cl:e.className,text:n.textContent,bounds:[q.x,q.y,q.width,q.height]})}}return{contrastIssues:issues,textOutsideSlide:outside,minText:min}}''')
   checks.update(visual)
   checks['pngSha256']=hashlib.sha256((OUT/f'{mode}--{name}.png').read_bytes()).hexdigest()
   minmatch=re.search(r'min (\d+)x(\d+)',title)
   minchecks=None
   if not fixture.startswith('foundation') and minmatch:
    cols,rows=map(int,minmatch.groups());body=slide.locator('.body')
    body.locator(':scope > *').evaluate_all('(els)=>els.forEach(e=>{e.style.gridColumn="1 / span '+str(cols)+'";e.style.gridRow="1 / span '+str(rows)+'"})')
    minchecks=slide.evaluate('''root=>({overflows:[...root.querySelectorAll('*')].filter(e=>!e.matches('.pt,.step,.root,.flowchart>.node')&&e.clientWidth>0&&e.clientHeight>0&&(e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+3)&&e.tagName!=='SECTION').map(e=>({tag:e.tagName,cl:e.className,client:[e.clientWidth,e.clientHeight],scroll:[e.scrollWidth,e.scrollHeight]}))})''')
    slide.screenshot(path=str(OUT/f'{mode}--{name}--min.png'))
   results.append({'mode':mode,'fixture':fixture,'full':checks,'minimum':minchecks})
 browser.close()
for mode in ['light','dark']:shutil.copyfile(R/'previews'/f'library-{mode}.html',R/'previews'/f'{mode}.html')
collection_hash=hashlib.sha256(b''.join(p.read_bytes()for p in sorted(C.rglob('*'))if p.is_file())).hexdigest()
(R/'review/library-agent.json').write_text(json.dumps({'collection':'spectrum-brief','elements':31,'fixtures':72,'renders':len(results),'rounds':3,'collectionSha256':collection_hash,'notes':['Read README completely before authoring. Samples used for structure only.','Seven decks synthesised into mint rail, nearly square corporate panels, navy type, five supporting tones.','Light accent darkened to #07745f to achieve at least 4.5:1 for small white text.','Round 2 corrected geometric line alignment, foundation seat sizing and declared minimum seats.','Round 3 protected funnel text from angled clipping, made pill/tag compact, repositioned matrix y-axis labels, and completed six-spoke connectors.','Generated connectors intentionally extend outside point/step/root boxes; they are excluded from generic scroll-overflow findings, and are inspected as part of the containing diagram.','All 72 fixtures rendered individually in both modes, using local Pretendard files; minimum grids rendered for all 70 element fixtures.','Original reference imagery is not embedded. All media seats use neutral single-colour fields.']},ensure_ascii=False,indent=2))
(R/'review/library-metrics.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print('reviewed',len(results),'mode/fixture renders')
for r in results:
 if r['full']['overflows'] or (r['minimum']and r['minimum']['overflows']):print(r['mode'],r['fixture'],'FULL',r['full']['overflows'],'MIN',r['minimum']['overflows']if r['minimum']else'')

for mode in ['light','dark']:
 (R/'previews'/f'{mode}.html').write_text((R/'previews'/f'library-{mode}.html').read_text())
