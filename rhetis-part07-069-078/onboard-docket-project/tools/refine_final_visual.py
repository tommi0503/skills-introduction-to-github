"""Final functional visual corrections only. Preserve final fixtures and parent runtime."""
from pathlib import Path
import re,math
P=Path(__file__).parent/'onboard-docket'
def add(n,css):
 p=P/'elements'/n/'element.css';s=p.read_text();s=s.split('\n/* Final functional visual review */')[0];p.write_text(s+'\n/* Final functional visual review */\n'+css+'\n')
def q(n):return '[data-el="onboard-docket-'+n+'"]'
s=q('bullet');add('bullet',s+'.bullet::before{background:linear-gradient(to right,transparent calc(var(--target)*1% - 1px),var(--ink) calc(var(--target)*1% - 1px) calc(var(--target)*1% + 1px),transparent calc(var(--target)*1% + 1px)),linear-gradient(to right,var(--a1) calc(var(--v)*1%),var(--n-4) 0)}'+s+'.bullet::after{display:none}')
s=q('balance');add('balance',s+' .pan{transform:translateY(calc(var(--tilt)*-.12px))}'+s+' .pan:nth-child(2){transform:translateY(calc(var(--tilt)*.12px))}')
s=q('chart-donut');add('chart-donut',s+'.donut{height:100%;container-type:size;aspect-ratio:auto}'+s+'.donut::before{inset:auto;left:50%;top:50%;translate:-50% -50%;width:calc(min(100cqw,100cqh) - var(--gap)*2);height:calc(min(100cqw,100cqh) - var(--gap)*2)}'+s+' .name{max-width:calc(min(100cqw,100cqh)*.64)}'+s+'.donuts>.donut{height:100%}')
p=P/'elements/chart-line/element.css';t=p.read_text();t=re.sub(r'(top|bottom):anchor\((--od-line-\d+ center)\)',r'\1:calc(anchor(\2) - 1px)',t);p.write_text(t)
s=q('chart-stack');css=''
for i,b,c in [(1,'a1','a1-on'),(2,'n-7','page'),(3,'a2','a2-on'),(4,'n-4','ink'),(5,'a3','a3-on')]:css+=s+f' .seg:nth-child({i} of .seg):not([class*="tone-"])'+'{background:var(--'+b+');color:var(--'+c+')}'
add('chart-stack',css)
s=q('concentric');add('concentric',s+' .ring{flex-direction:row;align-items:flex-start;justify-content:center;gap:var(--gap-sm);padding-top:calc(var(--gap-sm)*.5)}'+s+' .name{font-size:var(--type-14)}'+s+' .fig{font-size:var(--type-16)}'+s+' .note{position:absolute;bottom:20%;max-width:70%}@container(max-height:300px){'+s+' .name{font-size:var(--type-12)}'+s+' .fig{font-size:var(--type-14)}}')
s=q('hierarchy');add('hierarchy',s+' .branch{justify-content:flex-start}'+s+' .leaf{position:relative}'+s+' .leaf::before{content:"";position:absolute;left:50%;bottom:100%;height:var(--gap);width:var(--stroke);background:var(--n-4)}')
s=q('mindmap');css=s+'{container-type:size}'+s+'>.core{z-index:2}'
for n in range(2,7):
 rows=math.ceil(n/2)
 for i in range(1,n+1):
  row=(i-1)//2;delta=((row+.5)/rows-.5)*100;h=abs(delta);side='right' if i%2 else 'left';edge='top' if delta<0 else 'bottom';sel=s+f':has(>.branch:nth-child({n} of .branch):last-child)>.branch:nth-child({i} of .branch)::before'
  css+=sel+'{background:none;box-sizing:border-box;'
  if h<.01:css+='height:var(--stroke);border:0;border-top:var(--stroke) solid var(--n-4);top:50%;}'
  else:css+=f'height:{h:.5f}cqh;top:'+('50%' if delta<0 else f'calc(50% - {h:.5f}cqh)')+';border:0;border-'+edge+':var(--stroke) solid var(--n-4);border-'+side+':var(--stroke) solid var(--n-4);border-radius:var(--radius);}'
add('mindmap',css)
s=q('journey');css=s+'{container-type:size}'+s+' .stage::before{z-index:2}'+s+' .stage::after{z-index:1}'
for n in range(3,8):
 dx=f'calc((100cqw + var(--gap))/{n})';dy='calc((var(--mood) - var(--next))*.3cqh)'
 css+=s+f':has(>.stage:nth-child({n}):last-child) .stage:not(:last-child)::after'+'{width:hypot('+dx+','+dy+');transform:rotate(atan2('+dy+','+dx+'));translate:7px 7px}'
add('journey',css)
s=q('flowchart');add('flowchart',s+'{grid-template-columns:none;grid-template-rows:none;grid-auto-columns:minmax(0,1fr);grid-auto-rows:minmax(0,1fr)}')
s=q('cycle');add('cycle',s+'::after{content:"";position:absolute;left:calc(81% - 5px);top:50%;width:10px;height:14px;background:var(--n-5);clip-path:polygon(0 0,100% 0,50% 100%);z-index:1}')
s=q('funnel');add('funnel',s+' .stage{min-width:0}')
s=q('person');add('person',s+'.person{container-type:size}'+s+' .seat{width:min(70cqw,48cqh);height:min(70cqw,48cqh);max-height:none;aspect-ratio:1}'+s+' .seat.portrait{width:min(70cqw,40cqh);height:min(93.333cqw,53.333cqh)}')
s=q('positioning');add('positioning',s+' .axis-y{writing-mode:horizontal-tb;flex-direction:column;top:var(--gap-sm);bottom:calc(var(--gap-lg)*1.5);left:var(--gap-sm)}')
s=q('slope');add('slope',s+':not(.dumbbell) .pair{container-type:size;display:block}'+s+':not(.dumbbell) .a,'+s+':not(.dumbbell) .b{bottom:auto;transform:translateY(-50%);font-size:var(--type-16)}'+s+':not(.dumbbell) .a{left:var(--gap-lg);top:calc(80% - var(--a)/var(--max)*40%)}'+s+':not(.dumbbell) .b{right:var(--gap-lg);top:calc(80% - var(--b)/var(--max)*40%)}'+s+':not(.dumbbell) .pair::after{left:calc(var(--gap-lg)*3);right:auto;top:calc(80% - var(--a)/var(--max)*40%);width:hypot(calc(100cqw - var(--gap-lg)*6),calc((var(--a) - var(--b))/var(--max)*40cqh));transform:rotate(atan2(calc((var(--a) - var(--b))/var(--max)*40cqh),calc(100cqw - var(--gap-lg)*6)));transform-origin:0 50%}')
s=q('swimlane');add('swimlane',s+'{padding-left:calc(var(--pad)*3.5)}'+s+' .lane{position:relative}'+s+' .lane>.name{position:absolute;right:100%;width:calc(var(--pad)*3);padding:var(--gap-sm);text-align:left}')
s=q('timeline');add('timeline',s+':not(.col)::before{display:none}'+s+':not(.col) .stop::after{content:"";position:absolute;left:var(--gap);right:calc(0px - var(--gap));top:calc(35% + 5px);height:var(--stroke);background:var(--n-4)}'+s+':not(.col) .stop:last-child::after{right:var(--gap)}'+s+':not(.col) .stop::before{z-index:1}')
s=q('venn');add('venn',s+'{container-type:size;display:block}'+s+' .set,'+s+':has(>.set:nth-child(3))>.set{position:absolute;box-sizing:border-box;width:min(52cqw,78cqh);height:min(52cqw,78cqh);margin:0;left:40%;top:48%;transform:translate(-50%,-50%);padding:var(--gap)}'+s+' .set:nth-child(2){left:60%}'+s+' .core{bottom:var(--gap);z-index:2}'+s+':has(>.set:nth-child(3))>.set{width:min(42cqw,62cqh);height:min(42cqw,62cqh)}'+s+':has(>.set:nth-child(3))>.set:nth-child(1){left:50%;top:33%}'+s+':has(>.set:nth-child(3))>.set:nth-child(2){left:40%;top:64%}'+s+':has(>.set:nth-child(3))>.set:nth-child(3){left:60%;top:64%}'+s+':has(>.set:nth-child(3))>.core{bottom:27%;}')
s=q('image-frame');add('image-frame',s+'.frame{width:auto;height:100%;position:relative;overflow:visible;transform:none}')
s=q('radar');css=''
for i,a in [(1,'a1'),(2,'a2'),(3,'a3'),(4,'a4')]:
 css+=s+f' .series:nth-child({i} of .series):not([class*="tone-"])::before'+'{background:color-mix(in srgb,var(--'+a+') 25%,var(--page));border-color:var(--'+a+')}'
 css+=s+f' .series:nth-child({i} of .series)>.name'+'{left:'+str((i-1)*30)+'%;color:var(--'+a+'-7)}'
css+=s+' .series>.name::before{content:"";display:inline-block;width:10px;height:10px;margin-right:var(--gap-sm);background:currentColor;border-radius:50%}'
add('radar',css)
p=P/'foundation/foundation.css';t=p.read_text().split('\n/* Final functional seat bounds */')[0];p.write_text(t+'\n/* Final functional seat bounds */\n.slide .body>.seat{height:100%;max-height:100%;aspect-ratio:auto}\n')
print('Corrected 21 element styles and foundation bounds; fixture HTML untouched.')
s=q('card');add('card','@container(max-height:200px){'+s+' .parts,'+s+' .parts:not(:has(.mark,.fig,.kick)){flex-direction:column;align-items:stretch;justify-content:center;gap:var(--gap-sm)}'+s+' .parts:not(:has(.note,.mark,.fig,.kick)){align-items:center}}')
s=q('callout');add('callout',s+' .name{flex-shrink:0;min-width:min-content;max-width:40%}')
p=P/'elements/concentric/element.css';t=p.read_text().replace('/* Final functional visual review */\n','/* Final functional visual review */\n'+q('concentric')+'{container-type:size}');p.write_text(t)
s=q('waffle');add('waffle',s+'{container-type:size}'+s+' .units:has(>.u:nth-child(100):last-child){width:min(100%,calc(100cqh - var(--type-40)*var(--figure-line) - var(--type-20)*var(--name-line) - var(--gap)*4))}')

s=q('venn');p=P/'elements/venn/element.css';t=p.read_text();t+=s+' .set{opacity:1}'+s+' .set>.name{position:relative;z-index:3}'+s+':has(>.set:nth-child(3))>.set>.name{position:absolute;left:50%;top:35%;transform:translate(-50%,-50%)}'+s+':has(>.set:nth-child(3))>.set:nth-child(2)>.name{left:18%;top:60%}'+s+':has(>.set:nth-child(3))>.set:nth-child(3)>.name{left:82%;top:60%}';p.write_text(t)
s=q('venn');p=P/'elements/venn/element.css';t=p.read_text();t+=s+':not(:has(>.set:nth-child(3)))>.set>.name{position:absolute;left:30%;top:50%;transform:translate(-50%,-50%)}'+s+':not(:has(>.set:nth-child(3)))>.set:nth-child(2)>.name{left:70%}'+s+':not(:has(>.set:nth-child(3)))>.core{left:42%;width:16%;top:48%;bottom:auto;transform:translateY(-50%)}';p.write_text(t)
s=q('waffle');p=P/'elements/waffle/element.css';t=p.read_text();t+='@container(max-height:90px){'+s+'.figures{flex-direction:row;padding:0;gap:var(--gap-sm);justify-content:flex-start}'+s+'.figures .units{width:30%;max-width:240px;gap:calc(var(--gap-sm)*.25)}'+s+'.figures .u{max-height:18px}'+s+'.figures .fig{font-size:var(--type-14);white-space:nowrap}'+s+'.figures .name{font-size:var(--type-12);white-space:nowrap}'+s+'.figures .name small{display:none}}';p.write_text(t)
s=q('person');p=P/'elements/person/element.css';t=p.read_text();t+=s+'.person:has(.list) .seat{width:min(70cqw,max(0px,calc(100cqh - var(--pad)*7.5)));height:min(70cqw,max(0px,calc(100cqh - var(--pad)*7.5)))}';p.write_text(t)
s=q('callout');p=P/'elements/callout/element.css';t=p.read_text();t+=s+'{container-type:size}'+s+'>.seat{flex:none;width:min(100px,65cqh);height:min(100px,65cqh);aspect-ratio:1;border-radius:50%}';p.write_text(t)
s=q('pyramid');add('pyramid',s+' .level:first-child{position:relative;clip-path:none;background:none}'+s+' .level:first-child::before{content:"";position:absolute;inset:0;clip-path:polygon(50% 0,100% 100%,0 100%);background:var(--a1)}'+s+' .level:first-child>*{position:relative;max-width:100%}')
s=q('sankey');add('sankey',s+'>.source{top:0;height:100%}'+s+'>.branch::before{height:calc(100% - var(--gap-sm));border-radius:0}')
s=q('waffle');p=P/'elements/waffle/element.css';t=p.read_text();t+=s+'.figures{flex-direction:row;padding:0;gap:var(--gap-sm);justify-content:center}'+s+'.figures .units{width:40%}';p.write_text(t)
s=q('sankey');p=P/'elements/sankey/element.css';t=p.read_text();t+=s+'{gap:var(--gap-sm)}'+s+'>.branch{padding:var(--gap-sm) var(--pad)}';p.write_text(t)
s=q('venn');p=P/'elements/venn/element.css';t=p.read_text();t+=s+' .set>.name{width:max-content;max-width:80%}';p.write_text(t)
s=q('venn');p=P/'elements/venn/element.css';t=p.read_text();t+='@container(max-width:600px){'+s+' .name{font-size:var(--type-14)}'+s+' .core{font-size:var(--type-12);padding:var(--gap-sm)}}';p.write_text(t)
