"""Distinguish real overflow clipping from harmless font ink beyond a line box.
Uses latest source CSS and tests only declared minima and larger slot sizes.
"""
from pathlib import Path
import sys,json,re,importlib.util,hashlib
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE,COLLECTIONS
spec=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(spec);spec.loader.exec_module(pv)
CHECK='''a=>{const found=[];for(const slide of a.querySelectorAll('.slide')){const walker=document.createTreeWalker(slide,NodeFilter.SHOW_TEXT);let node;while(node=walker.nextNode()){if(!node.textContent.trim())continue;const parent=node.parentElement;const style=getComputedStyle(parent),pr=parent.getBoundingClientRect(),sr=parent.matches('b')&&parent.closest('.bars.quiet')&&style.position==='absolute'&&pr.width<=2&&pr.height<=2&&style.clipPath!=='none';if(style.visibility==='hidden'||style.display==='none')continue;let range=document.createRange();range.selectNodeContents(node);for(const tr of range.getClientRects()){if(!tr.width||!tr.height)continue;for(let e=parent;e&&e!==slide.parentElement;e=e.parentElement){let s=getComputedStyle(e),er=e.getBoundingClientRect(),x=['hidden','clip','scroll','auto'].includes(s.overflowX),y=['hidden','clip','scroll','auto'].includes(s.overflowY);if((x&&(tr.left<er.left-2||tr.right>er.right+2))||(y&&(tr.top<er.top-2||tr.bottom>er.bottom+2))){found.push({intentionalAccessibleValue:!!sr,text:node.textContent.trim().slice(0,100),element:parent.className,clipAncestor:e.className,textBox:[tr.x,tr.y,tr.width,tr.height],clipBox:[er.x,er.y,er.width,er.height]});break;}}}}}return found;}'''
if __name__=='__main__':
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1360,'height':900});page.goto('http://127.0.0.1:8765/qa/probe.html')
  for k in (sys.argv[1:] or COLLECTIONS):
   root=BASE/(k+'-project')/k
   if len(list((root/'elements').glob('*/element.css')))!=56:continue
   markup=pv.sheet(root,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),dark=True,fonts_href=f'/{k}-project/assets/fonts/fonts.css')
   page.set_content(markup,wait_until='networkidle');page.evaluate('document.fonts.ready')
   allchecks=[]
   for a in page.locator('article').all():
    title=a.locator(':scope > h2').inner_text();mins=[tuple(map(int,x)) for x in re.findall(r'(\d+)x(\d+)',title.split('min',1)[-1])];sizes=list(dict.fromkeys(mins+[(12,6)]))
    if any(6>=c and 3>=r for c,r in mins) and (6,3) not in sizes:sizes.insert(-1,(6,3))
    for c,r in sizes:
     a.evaluate('''(a,size)=>{let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';f.querySelector('.slide').style.transform='none';let body=a.querySelector('.body');if(body&&!a.querySelector(':scope > h2').textContent.startsWith('foundation /'))for(const el of body.children){el.style.gridColumn='1 / span '+size[0];el.style.gridRow='1 / span '+size[1]}}''',[c,r])
     clips=a.evaluate(CHECK);allchecks.append({'fixture':title,'size':[c,r],'actualClipCandidates':[x for x in clips if not x.get('intentionalAccessibleValue')],'accessibleValueClips':[x for x in clips if x.get('intentionalAccessibleValue')]})
   result={'collection':k,'mode':'dark','sourceSha256':hashlib.sha256(markup.encode()).hexdigest(),'checks':allchecks,'intentionalAccessibleValueClips':sum(len(x['accessibleValueClips']) for x in allchecks),'clippedCases':sum(bool(x['actualClipCandidates']) for x in allchecks),'clippedTextRuns':sum(len(x['actualClipCandidates']) for x in allchecks),'note':'Range line boxes crossing an ancestor overflow clip; visual review still needed for overlaps.'}
   (BASE/'qa'/(k+'-clipping-dark-audit.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(k,result['clippedCases'],result['clippedTextRuns'],flush=True)
  b.close()
