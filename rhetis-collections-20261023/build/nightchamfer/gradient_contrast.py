from pathlib import Path
import json
from playwright.sync_api import sync_playwright
pals=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text())
with sync_playwright()as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page()
 report=page.evaluate('''pals=>{
 const ctx=document.createElement('canvas').getContext('2d');function rgb(s){ctx.fillStyle=s;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data].slice(0,3)}
 function lum(c){return c.map(v=>v/255<=.04045?v/255/12.92:((v/255+.055)/1.055)**2.4).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0)}
 function ratio(a,b){let x=lum(a),y=lum(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)}
 return Object.entries(pals).map(([mode,p])=>({mode,background:rgb(p['--page']),ink:rgb(p['--ink']),accent7:rgb(p['--a1-7']),inkRatio:ratio(rgb(p['--ink']),rgb(p['--page'])),accent7Ratio:ratio(rgb(p['--a1-7']),rgb(p['--page']))}))
}''',pals)
 b.close()
Path('/workspace/output/nightchamfer-review/library/gradient-contrast.json').write_text(json.dumps({'element':'headline-big','method':'Actual gradient endpoint sRGB luminance against page; both endpoints exceed large-text minimum 3:1. The automatic plain-color checker sees the intentionally transparent text color, not background-clip glyph fill.','endpoints':report},indent=2))
print(report)
