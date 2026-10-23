"""Independent final browser checks of actual slide files and published PNG pixels."""
import asyncio, hashlib, io, json, re, sys
from pathlib import Path
from PIL import Image, ImageChops, ImageStat
from playwright.async_api import async_playwright
OUT=Path('/workspace/output'); WORK=Path('/workspace/work/integration'); PUBLIC=WORK/'public'
COUNTS={'fluxweave':18,'cyanloop':18,'roundrise':24,'nightchamfer':18,'glasspulse':18}
async def audit(name,browser):
 review=OUT/(name+'-review'); link=PUBLIC/(name+'-review')
 if not link.exists():link.symlink_to(review,target_is_directory=True)
 results={'collection':name,'pages':[],'errors':[],
  'collection_source_sha256':{str(p.relative_to(OUT/name)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (OUT/name).rglob('*') if p.suffix in ['.css','.json','.html']},
  'review_assets_sha256':{str(p.relative_to(review)):hashlib.sha256(p.read_bytes()).hexdigest() for p in review.rglob('*') if p.suffix in ['.css','.js']}}
 page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 failures=[];page.on('requestfailed',lambda request:failures.append(request.url))
 for kind in ['replica','reassembled']:
  sources=sorted(p for p in (review/kind).glob('*.html') if re.match(r'slide[-_]\d+\.html$',p.name))
  if len(sources)!=COUNTS[name]:results['errors'].append(f'{kind}: {len(sources)} HTML files, expected {COUNTS[name]}')
  for source in sources:
   failures.clear();url='http://127.0.0.1:8760/'+name+'-review/'+kind+'/'+source.name
   await page.goto(url,wait_until='networkidle');await page.evaluate('document.fonts.ready')
   check=await page.evaluate('''() => {
    const slide=document.querySelector('.slide')||document.querySelector('main')||document.body, rect=slide.getBoundingClientRect();
    const issues=[], fonts=new Set(), walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    while(walker.nextNode()){
     const node=walker.currentNode,el=node.parentElement;if(['SCRIPT','STYLE','TITLE'].includes(el.tagName)||!node.textContent.trim()||!el.getClientRects().length)continue;
     const st=getComputedStyle(el);if(st.visibility==='hidden'||st.display==='none'||parseFloat(st.opacity)===0)continue;
     fonts.add(st.fontFamily);const range=document.createRange();range.selectNodeContents(node);
     for(const r of range.getClientRects()){
      if(!r.width||!r.height)continue;
      if(r.left<-2||r.top<-2||r.right>1282||r.bottom>722)issues.push({type:'viewport',text:node.textContent.trim().slice(0,90),rect:[r.x,r.y,r.width,r.height]});
      let a=el;while(a&&a!==document.body){
       const as=getComputedStyle(a);if(['hidden','clip'].includes(as.overflowX)||['hidden','clip'].includes(as.overflowY)){
        const ar=a.getBoundingClientRect();if(r.left<ar.left-2||r.right>ar.right+2||r.top<ar.top-2||r.bottom>ar.bottom+2){issues.push({type:'clipped',text:node.textContent.trim().slice(0,90),ancestor:a.className,rect:[r.x,r.y,r.width,r.height],clip:[ar.x,ar.y,ar.width,ar.height]});break;}
       }a=a.parentElement;
      }
     }
    }
    return {size:[rect.width,rect.height],issues,fonts:[...fonts],font_errors:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)};
   }''')
   png=source.with_suffix('.png');shot=await page.screenshot();current=Image.open(io.BytesIO(shot)).convert('RGB')
   pixels={'published_png_exists':png.is_file()}
   if png.is_file():
    old=Image.open(png).convert('RGB');pixels['size']=list(old.size)
    if old.size==current.size:
     diff=ImageChops.difference(old,current);hist=diff.convert('L').histogram();pixels.update({'different_pixels':old.width*old.height-hist[0],'total_pixels':old.width*old.height,'mean_channel_difference':sum(ImageStat.Stat(diff).mean)/3})
    else:results['errors'].append(str(png.relative_to(review))+': PNG dimensions differ')
   else:results['errors'].append(str(png.relative_to(review))+': missing PNG')
   record={'source':str(source.relative_to(review)),'html_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),**check,'failed_resources':list(failures),'render_check':pixels}
   results['pages'].append(record)
   if check['size']!=[1280,720]:results['errors'].append(record['source']+': page size '+str(check['size']))
   if check['issues']:results['errors'].append(record['source']+': '+str(len(check['issues']))+' visible text bounds candidates')
   if check['font_errors'] or failures:results['errors'].append(record['source']+': font/resource failure')
   if pixels.get('mean_channel_difference',0)>0.2:results['errors'].append(record['source']+': PNG does not match current browser render')
 await page.close();(WORK/(name+'-page-audit.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
 print(name,len(results['pages']),'pages',len(results['errors']),'errors',flush=True)
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for name in sys.argv[1:]:await audit(name,browser)
  await browser.close()
asyncio.run(main())
