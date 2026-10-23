from pathlib import Path
import importlib.util,json,re
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;Q=P/'qa-final-visual'
spec=importlib.util.spec_from_file_location('pv','/workspace/work/reference/tools/preview.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
res=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1280,'height':720})
 for dark in [False,True]:
  mode='dark'if dark else'light';f=Q/('probe-'+mode+'.html');f.write_text(m.sheet(P/'onboard-docket',json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text()),json.loads(Path('/workspace/work/reference/contract/palette.json').read_text()),dark=dark,fonts_href='../assets/fonts/fonts.css'));page.goto('http://127.0.0.1:8765/onboard-docket-project/qa-final-visual/'+f.name,wait_until='networkidle');page.evaluate('document.fonts.ready')
  for label in ['person / person ','waffle / units-100 ','waffle / waffle-figures ','venn / venn-2 ','venn / venn-3 ','pyramid / pyramid-4 ','sankey / sankey-6 ']:
   a=page.locator('article').filter(has=page.locator('h2').filter(has_text=re.compile('^'+re.escape(label)))).first
   page.evaluate('()=>{for(const a of document.querySelectorAll("article"))a.style.display="none"}');a.evaluate('a=>a.style.display="block"');title=a.locator(':scope>h2').inner_text();mat=re.search(r'min (\d+)x(\d+)',title);c,r=map(int,mat.groups());a.evaluate('(a,z)=>{a.querySelector(":scope>.frame").style.cssText="width:1280px;height:720px";a.querySelector(":scope>.frame>.slide").style.transform="none";for(const e of a.querySelector(".body").children){e.style.gridColumn="1 / span "+z[0];e.style.gridRow="1 / span "+z[1]}}',[c,r]);a.locator(':scope>.frame').screenshot(path=str(Q/(label.strip().replace(' / ','-')+'-min-'+mode+'.png')))
   tests=a.evaluate('''a=>{let out=[];for(const e of a.querySelectorAll('[data-el] .u,[data-el] .seat,[data-el].venn .set')){let root=e.closest('[data-el]'),x=e.getBoundingClientRect(),y=root.getBoundingClientRect();if(x.top<y.top-2||x.bottom>y.bottom+2||x.left<y.left-2||x.right>y.right+2)out.push({class:e.className,root:[y.width,y.height],delta:[x.top-y.top,x.bottom-y.bottom]})}return out}''');res.append({'mode':mode,'fixture':title,'outsideShapes':tests})
  # New arbitrary equal values prove horizontal connections are not fixture-value-specific.
  a=page.locator('article').filter(has=page.locator('h2').filter(has_text=re.compile('^chart-line / lines-6 '))).first;a.evaluate('a=>{a.style.display="block";for(const e of a.querySelectorAll(".pt"))e.style.setProperty("--v",37)}')
  hs=a.locator('.pt:nth-child(2)').evaluate('e=>[getComputedStyle(e,"::before").height,getComputedStyle(e,"::after").height]');assert all(float(x[:-2])>0 for x in hs),hs;res.append({'mode':mode,'arbitraryFlatValue':37,'segmentHeights':hs})
  a=page.locator('article').filter(has=page.locator('h2').filter(has_text=re.compile('^chart-stack / stack-5 '))).first;colors=a.locator('.sbar').first.locator('.seg').evaluate_all('es=>es.map(e=>getComputedStyle(e).backgroundColor)');assert len(set(colors))==3,colors;res.append({'mode':mode,'untonedSeriesColors':colors})
 b.close()
(Q/'data-probes.json').write_text(json.dumps(res,ensure_ascii=False,indent=2));print(json.dumps(res,ensure_ascii=False))
