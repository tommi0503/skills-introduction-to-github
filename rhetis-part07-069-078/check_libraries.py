from pathlib import Path
import json,re,sys,importlib.util
from playwright.sync_api import sync_playwright
from render import ROOT,REF,url,browser,ready
s=importlib.util.spec_from_file_location('preview',REF/'tools/preview.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
steps=json.loads((REF/'contract/type-steps.json').read_text());palette=json.loads((REF/'contract/palette.json').read_text())
with sync_playwright() as pw:
 b=browser(pw);page=b.new_page(viewport={'width':1360,'height':900},device_scale_factor=1)
 for kid in sys.argv[1:]:
  P=ROOT/(kid+'-project');out=P/'library';out.mkdir(exist_ok=True);result={}
  for dark in [False,True]:
   mode='dark' if dark else 'light';f=out/('check-'+mode+'.html');f.write_text(m.sheet(P/kid,steps,palette,dark=dark,fonts_href='../assets/fonts/fonts.css'))
   page.goto(url(f),wait_until='networkidle');ready(page)
   data=page.evaluate(r'''()=>{let all=[];for(const a of document.querySelectorAll('article')){let title=a.querySelector('h2').textContent,m=title.match(/min\s+(\d+)x(\d+)/),sizes=[[12,6]];if(m)sizes.unshift([+m[1],+m[2]]);if(m){let mid=[Math.ceil((+m[1]+12)/2),Math.ceil((+m[2]+6)/2)];if(!sizes.some(s=>s[0]===mid[0]&&s[1]===mid[1]))sizes.splice(sizes.length-1,0,mid);}let fr=a.querySelector('.frame'),sl=fr.querySelector('.slide'),body=sl.querySelector('.body');fr.style.width='1280px';fr.style.height='720px';sl.style.transform='none';if(!body)continue;for(const sz of sizes){if(!title.startsWith('foundation /'))for(const e of body.children){e.style.gridColumn='1 / span '+sz[0];e.style.gridRow='1 / span '+sz[1]}let issues=[];for(const e of body.querySelectorAll('*')){let cs=getComputedStyle(e),r=e.getBoundingClientRect();if(!r.width||!r.height||cs.display==='none'||e.children.length||!e.textContent.trim())continue;if(e.matches('b')&&e.closest('.bars.quiet')&&cs.position==='absolute'&&r.width<=2&&r.height<=2&&cs.clipPath!=='none')continue;if(e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+4)issues.push({class:e.className,text:e.textContent.slice(0,75),client:[e.clientWidth,e.clientHeight],scroll:[e.scrollWidth,e.scrollHeight]})}all.push({fixture:title,size:sz,overflowCandidates:issues})}}return all}''')
   contrast=page.evaluate((ROOT/'contrast.js').read_text());result[mode]={'sizeChecks':data,'contrast':contrast}
   print(kid,mode,'overflow-candidates',sum(len(x['overflowCandidates']) for x in data),'contrast-candidates',len(contrast['candidates']),flush=True)
  (P/'library-quick-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
 b.close()
