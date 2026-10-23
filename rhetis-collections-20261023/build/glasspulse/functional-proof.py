from pathlib import Path
from playwright.sync_api import sync_playwright
import json,http.server,threading,functools,hashlib
R=Path('/workspace/output/glasspulse-review')
class H(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8140),functools.partial(H,directory=R));threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1320,'height':780});out={}
 for mode in ['light','dark']:
  page.goto('http://127.0.0.1:8140/library/'+mode+'.html');page.evaluate('document.fonts.ready')
  out[mode]=page.evaluate('''()=>{
   let o={};let sparks=[...document.querySelectorAll('.spark[data-el="glasspulse-sparkline"]:not(.bars)')];o.sparkline=sparks.map(s=>({points:s.children.length,segments:[...s.children].slice(1).map(e=>{let c=getComputedStyle(e,'::before');return {width:parseFloat(c.width),height:parseFloat(c.height),clip:c.clipPath}})}));
   o.slope=[...document.querySelectorAll('.slope[data-el="glasspulse-slope"]')].map(s=>{let max=+getComputedStyle(s).getPropertyValue('--max'),r=s.getBoundingClientRect(),cs=getComputedStyle(s),gap=parseFloat(cs.getPropertyValue('--gap')),pairs=[...s.querySelectorAll(':scope>.pair')],db=s.classList.contains('dumbbell');return {dumbbell:db,max,pairs:pairs.map(e=>{let c=getComputedStyle(e),er=e.getBoundingClientRect(),a=e.querySelector('.a'),bb=e.querySelector('.b'),ar=a.getBoundingClientRect(),br=bb.getBoundingClientRect(),va=+c.getPropertyValue('--a'),vb=+c.getPropertyValue('--b'),actual=db?[parseFloat(getComputedStyle(a).left)/e.clientWidth,parseFloat(getComputedStyle(bb).left)/e.clientWidth]:[(parseFloat(getComputedStyle(a).top)-gap*3)/(s.clientHeight-gap*5),(parseFloat(getComputedStyle(bb).top)-gap*3)/(s.clientHeight-gap*5)],expected=db?[.27+va/max*.66,.27+vb/max*.66]:[1-va/max,1-vb/max];return {values:[va,vb],actual,expected,max_error:Math.max(...actual.map((v,i)=>Math.abs(v-expected[i]))),connector:getComputedStyle(e,'::after').clipPath}})}});
   o.areas=[...document.querySelectorAll('.areas[data-el="glasspulse-chart-area"]')].map(e=>({series:[...e.querySelectorAll(':scope>.series')].map(s=>({points:s.querySelectorAll(':scope>.pt').length,visible_segments:[...s.querySelectorAll(':scope>.pt')].slice(1).filter(p=>parseFloat(getComputedStyle(p,'::after').width)>0&&getComputedStyle(p,'::after').clipPath!='none').length}))}));
   o.bullet=[...document.querySelectorAll('.bullet[data-el="glasspulse-bullet"]')].map(e=>{let c=getComputedStyle(e,'::after');return {low:getComputedStyle(e).getPropertyValue('--low'),high:getComputedStyle(e).getPropertyValue('--high'),bands:c.backgroundImage,band_height:c.height}});
   o.stacks=[...document.querySelectorAll('.stacks[data-el="glasspulse-chart-stack"]')].map(e=>({horizontal:e.classList.contains('h'),percent:e.classList.contains('pct'),series_colors:[...new Set([...e.querySelectorAll('.seg')].map(p=>getComputedStyle(p).backgroundColor))]}));
   o.balance=[...document.querySelectorAll('.balance[data-el="glasspulse-balance"]')].map(e=>({tilt:getComputedStyle(e).getPropertyValue('--tilt'),pans:[...e.querySelectorAll('.pan')].map(p=>getComputedStyle(p).transform)}));o.funnel=[];let fs=document.querySelector('.funnel[data-el="glasspulse-funnel"]>.stage');let fv=fs.style.getPropertyValue('--v');for(let v of [0,1,5,10,21,100]){fs.style.setProperty('--v',v);let c=getComputedStyle(fs,'::before');o.funnel.push({value:v,stage_width:fs.clientWidth,paint_width:parseFloat(c.width),expected_width:fs.clientWidth*v/100,border:parseFloat(c.borderLeftWidth)+parseFloat(c.borderRightWidth),padding:parseFloat(c.paddingLeft)+parseFloat(c.paddingRight)})}fs.style.setProperty('--v',fv);o.avatars=[...document.querySelectorAll('.person[data-el="glasspulse-person"]>.seat.avatar')].map(e=>({width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}));o.calendar=[...document.querySelectorAll('.heat.calendar[data-el="glasspulse-heatmap"] .cell')].map(e=>({width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}));o.venn=[...document.querySelectorAll('.venn[data-el="glasspulse-venn"]:has(>.core)')].map(e=>{let k=e.querySelector(':scope>.core').getBoundingClientRect(),x=k.x+k.width/2,y=k.y+k.height/2;return [...e.querySelectorAll(':scope>.set')].map(s=>{let r=s.getBoundingClientRect();return {width:r.width,height:r.height,shared_center_distance:Math.hypot(x-r.x-r.width/2,y-r.y-r.height/2),radius:r.width/2}})});return o
  }''')
 b.close()
for m,d in out.items():
 assert all(x['width']>0 and x['clip']!='none' for s in d['sparkline'] for x in s['segments'])
 assert all(p['max_error']<.005 for s in d['slope'] for p in s['pairs'])
 assert all(s['visible_segments']==s['points']-1 for a in d['areas'] for s in a['series'])
 assert all(len(s['series_colors'])>=2 for s in d['stacks'])
 assert all(abs(a['paint_width']-a['expected_width'])<.1 and a['border']==0 and a['padding']==0 for a in d['funnel'])
 assert all(abs(a['width']-a['height'])<1 for a in d['avatars']+d['calendar'])
 assert all(abs(a['width']-a['height'])<1 and a['shared_center_distance']<a['radius'] for v in d['venn'] for a in v)
 for z in d['balance']:
  if float(z['tilt']):
   ys=[float(x.removeprefix('matrix(').removesuffix(')').split(',')[-1]) for x in z['pans']];assert len(ys)==2 and ys[0]*ys[1]<0 and abs(sum(ys))<.01

out['_source_sha256']={str(p.relative_to(Path('/workspace/output/glasspulse'))):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path('/workspace/output/glasspulse').rglob('*')) if p.is_file()}
(R/'library/functional-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('functional geometry passes: spark segments, slope endpoints, area fills/lines, qualitative bands, stack variants, balance tilt')
srv.shutdown()
