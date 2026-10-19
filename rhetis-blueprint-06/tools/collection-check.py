"""Contract audit and real Chromium fixture rendering, full and minimum slots, light and dark."""
import argparse,asyncio,json,re,hashlib,sys,importlib.util,threading,functools
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from html.parser import HTMLParser
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
class Fragment(HTMLParser):
 def __init__(self):super().__init__();self.level=0;self.top=[];self.nodes=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs);self.nodes.append((tag,d));
  if self.level==0:self.top.append((tag,d))
  if tag not in ('br','img','hr','input','meta','link'):self.level+=1
 def handle_endtag(self,tag):self.level-=1

def audit(collection):
 tax=json.loads((ROOT/'contract/taxonomy.json').read_text()); required=json.loads((ROOT/'contract/kit-tokens.json').read_text())['tokens'];steps=json.loads((ROOT/'contract/type-steps.json').read_text());issues=[]
 kit=json.loads((collection/'kit/kit.json').read_text());tokens=(collection/'kit/css/tokens.css').read_text()
 for k,t in required.items():
  found=len(re.findall(re.escape(k)+r'\s*:',tokens));want=2 if t=='color' else 1
  if found!=want:issues.append(f'{k}: expected {want} definitions, found {found}')
 for c in tax['contracts']:
  folder=c['category'].split('.')[-1];p=collection/'elements'/folder
  for f in ['element.css','element.json','description.md']:
   if not (p/f).is_file():issues.append(f'Missing {folder}/{f}')
  meta=json.loads((p/'element.json').read_text());css=(p/'element.css').read_text();fixtures=list((p/'fixtures').glob('*.html'))
  if meta['contract']!=c['id']:issues.append(f'{folder}: incorrect contract')
  if len(fixtures)<2:issues.append(f'{folder}: fewer than two fixtures')
  if '@container' not in css:issues.append(f'{folder}: missing container rule')
  for bad in [r'#[0-9a-fA-F]{3,8}\b',r'url\s*\(',r'@(?:import|font-face|keyframes)\b',r'font-size\s*:\s*\d',r'font-weight\s*:\s*\d',r'(?:line-height|letter-spacing)\s*:\s*[-.\d]']:
   if re.search(bad,css):issues.append(f'{folder}: forbidden literal or resource {bad}')
  for n in re.findall(r'var\(--type-(\d+)\)',css):
   if int(n) not in steps:issues.append(f'{folder}: invalid type step {n}')
  # Every qualified selector prelude must contain its own data-el. Parent at-rules excluded.
  for rule in re.findall(r'([^{}]+)\{',css):
   if rule.strip().startswith('@'):continue
   if f'data-el="blueprint-06-{folder}"' not in rule:issues.append(f'{folder}: unscoped {rule[:100]}')
  for f in fixtures:
   h=f.read_text(); parser=Fragment();parser.feed(h)
   if len(parser.top)!=1:issues.append(f'{folder}/{f.name}: expected one root')
   if not re.match(r'<!-- min: \d+x\d+(?: \| \d+x\d+)* -->\n',h):issues.append(f'{folder}/{f.name}: missing min comment')
   if parser.top[0][1].get('data-el')!=f'blueprint-06-{folder}':issues.append(f'{folder}/{f.name}: incorrect data-el')
   if not re.search(r'grid-column:1 / span 12; grid-row:1 / span 6',parser.top[0][1].get('style','')):issues.append(f'{folder}/{f.name}: missing placement')
 return {'elements':len(tax['contracts']),'fixtures':sum(len(list(p.glob('fixtures/*.html')))for p in (collection/'elements').iterdir()),'issues':issues}
async def render(collection,report_dir):
 spec=importlib.util.spec_from_file_location('preview',ROOT/'tools/preview.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 steps=json.loads((ROOT/'contract/type-steps.json').read_text());report=[];report_dir.mkdir(parents=True,exist_ok=True)
 fontcss=''.join('@font-face{font-family:Pretendard;src:url("'+'/assets/fonts/'+f'Pretendard-{name}.woff2'+'");font-weight:'+str(w)+';font-display:block}' for name,w in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700),('ExtraBold',800)])
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(SimpleHTTPRequestHandler,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{server.server_port}/'
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--allow-file-access-from-files']);page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for dark in [False,True]:
   source=mod.sheet(collection,steps,dark);sheet=report_dir/('dark-inspection.html' if dark else 'light-inspection.html');sheet.write_text(source.replace('</head>',f'<style>{fontcss}</style></head>'))
   await page.goto(base+str(sheet.relative_to(ROOT)));await page.evaluate('document.fonts.ready');elements=await page.locator('article').count()
   for i in range(elements):
    article=page.locator('article').nth(i);label=await article.locator('h2').inner_text();folder=label.split(' / ')[0];name=label.split(' / ')[1].split(' ')[0];minimum=re.search(r'min (\d+)x(\d+)',label);mn=[int(minimum[1]),int(minimum[2])] if minimum else [12,6]
    for size in ['full','min']:
     # Hide unrelated articles while testing each real page at unscaled output dimensions.
     await page.evaluate('''({i,mn,size})=>{document.querySelectorAll('article').forEach((a,n)=>{a.style.display=n===i?'block':'none'});document.body.style.cssText='margin:0;padding:0;display:block;background:#eee';let a=document.querySelectorAll('article')[i];a.querySelector('h2').style.display='none';let frame=a.querySelector('.frame');frame.style.cssText='width:1280px;height:720px;overflow:visible';let s=a.querySelector('.slide');s.style.cssText='transform:none;width:1280px;height:720px';let root=s.querySelector('.body')?.firstElementChild;if(root){root.style.gridColumn='1 / span '+(size==='full'?12:mn[0]);root.style.gridRow='1 / span '+(size==='full'?6:mn[1]);}}''',{'i':i,'mn':mn,'size':size})
     await page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
     info=await article.locator('.slide').evaluate('''s=>{const errors=[],r=s.getBoundingClientRect();for(const el of s.querySelectorAll('*')){if(!el.firstChild||!Array.from(el.childNodes).some(n=>n.nodeType===3&&n.textContent.trim()))continue;const cs=getComputedStyle(el);if(cs.display==='none'||cs.visibility==='hidden'||el.clientWidth===0)continue;let range=document.createRange();range.selectNodeContents(el);let b=range.getBoundingClientRect(),e=el.getBoundingClientRect();if(b.width<1||b.height<1)continue;let clip=el.closest('[data-el]')?.getBoundingClientRect();if(b.left<r.left-1||b.right>r.right+1||b.top<r.top-1||b.bottom>r.bottom+1)errors.push({type:'outside-slide',text:el.textContent.trim().slice(0,70),rect:[b.x,b.y,b.width,b.height]});if(clip&&(b.left<clip.left-2||b.right>clip.right+2||b.top<clip.top-2||b.bottom>clip.bottom+2))errors.push({type:'outside-element',text:el.textContent.trim().slice(0,70),rect:[b.x,b.y,b.width,b.height],element:[clip.x,clip.y,clip.width,clip.height]});if(!document.fonts.check(cs.fontWeight+' '+cs.fontSize+' '+cs.fontFamily))errors.push({type:'font',text:el.textContent.trim()});}return{size:[r.width,r.height],fonts:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status})),errors}}''')
     dest=report_dir/f'{folder}-{name}-{size}-{"dark" if dark else "light"}.png';await article.locator('.slide').screenshot(path=str(dest));info.update({'fixture':folder+'/'+name,'slot':size,'mode':'dark' if dark else 'light','png':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()});report.append(info)
   print('dark' if dark else 'light',elements,'fixtures rendered independently',flush=True)
  await browser.close()
 server.shutdown()
 (report_dir/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));return report
async def main():
 p=argparse.ArgumentParser();p.add_argument('--render',action='store_true');p.add_argument('--out',default='review/library-render');a=p.parse_args();collection=ROOT/'collection/blueprint-06';result=audit(collection);report_dir=ROOT/a.out
 if a.render:
  report=await render(collection,report_dir);result['renders']=len(report);result['renderFindings']=sum(len(r['errors'])for r in report)
 (ROOT/'review/library-contract.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['issues']))
if __name__=='__main__':asyncio.run(main())
