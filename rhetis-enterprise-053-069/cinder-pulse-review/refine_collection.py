from pathlib import Path
import math
B=Path(__file__).parent;C=B.parent/'cinder-pulse'
def add(name,s):
 p=C/f'elements/{name}/element.css';p.write_text(p.read_text()+'\n/* Integrated review corrections */\n'+s)
r='.lines[data-el="cinder-pulse-chart-line"]'
add('chart-line',f'''{r} .pt>b{{position:relative;}} {r} .pt::before,{r} .pt::after{{content:'';position:absolute;left:anchor(var(--cinder-pulse-prev) center);right:anchor(var(--cinder-pulse-self) center);clip-path:none;pointer-events:none;}} {r} .pt::before{{top:calc(anchor(var(--cinder-pulse-prev) bottom) - 1px);bottom:calc(anchor(var(--cinder-pulse-self) bottom) - 1px);background:linear-gradient(to bottom right,color-mix(in srgb,var(--page) 0%,var(--page) 0%) calc(50% - 1.5px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),color-mix(in srgb,var(--page) 0%,var(--page) 0%) calc(50% + 1.5px));}} {r} .pt::after{{top:calc(anchor(var(--cinder-pulse-self) bottom) - 1px);bottom:calc(anchor(var(--cinder-pulse-prev) bottom) - 1px);background:linear-gradient(to top right,color-mix(in srgb,var(--page) 0%,var(--page) 0%) calc(50% - 1.5px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),color-mix(in srgb,var(--page) 0%,var(--page) 0%) calc(50% + 1.5px));}} {r} .pt:first-child::before,{r} .pt:first-child::after{{content:none;}}''')
r='.radar[data-el="cinder-pulse-radar"]'
s=''
for n in range(3,9):
 poly=[]
 for i in range(n):
  x=math.sin(2*math.pi*i/n)*48;y=-math.cos(2*math.pi*i/n)*48
  poly.append(f'calc(50% + {x:.5f}%*var(--v{i+1})/var(--max)) calc(50% + {y:.5f}%*var(--v{i+1})/var(--max))')
 s+=f'{r}[style*="--n:{n}"] .series,{r}[style*="--n: {n}"] .series{{clip-path:polygon('+','.join(poly)+');}\n'
 for i in range(n):
  x=50+math.sin(2*math.pi*i/n)*44;y=50-math.cos(2*math.pi*i/n)*44
  s+=f'{r}[style*="--n:{n}"] .axis:nth-child({i+1}),{r}[style*="--n: {n}"] .axis:nth-child({i+1}){{left:{x:.4f}%;top:{y:.4f}%;translate:-50% -50%;}}\n'
add('radar',s)
add('matrix-nine','.grid9[data-el="cinder-pulse-matrix-nine"]:not(:has(>.axis-x)){grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(3,minmax(0,1fr));}')
add('metric','@container (max-height:160px){:is(.stat,.stats)[data-el="cinder-pulse-metric"] .fig{font-size:var(--type-24);line-height:var(--name-line);}:is(.stat,.stats)[data-el="cinder-pulse-metric"] .name{font-size:var(--type-16);}}\n:is(.stat,.stats)[data-el="cinder-pulse-metric"] .fig{line-height:var(--name-line);}')
add('table','@container (max-height:520px){.tablebox[data-el="cinder-pulse-table"] table{font-size:var(--type-14);}.tablebox[data-el="cinder-pulse-table"] :is(td,th){padding:calc(var(--gap-sm)/1.5);}}')
add('cycle','.cycle[data-el="cinder-pulse-cycle"]:has(>.node:nth-of-type(4):last-child)>.node:nth-of-type(3){right:1%;top:auto;bottom:4%;}.cycle[data-el="cinder-pulse-cycle"]:has(>.node:nth-of-type(4):last-child)>.node:nth-of-type(4){right:auto;left:1%;bottom:4%;}')
# source-derived shallow round core instead of elliptical distortion
add('cycle','.cycle[data-el="cinder-pulse-cycle"] .core{width:28%;height:auto;aspect-ratio:1;top:35%;}')
# The fit of a component inside its slot is a library concern.
add('prose','@container (max-height:330px){.prose[data-el="cinder-pulse-prose"]{font-size:var(--type-18);gap:var(--gap-sm);}}')
p=C/'foundation/foundation.css';s=p.read_text();s+='''
.slide.cover .deco{clip-path:none;background:none;overflow:hidden;}
.slide.cover .deco::before{content:'';position:absolute;left:0;top:18%;width:18%;height:84%;border-radius:999px;background:var(--n-7);box-shadow:120px -92px 0 var(--n-7),240px 7px 0 var(--n-7),360px -52px 0 var(--n-7),480px 0 0 var(--n-7);}
.slide.cover .lockup.at-left{top:0;}
.slide.cover .lockup .kicker{margin-bottom:calc(var(--gap-lg)*2);}
.slide .head .title{word-break:keep-all;}
''';p.write_text(s)
print('refined line, radar, matrix-nine, metric, table, cycle, prose, cover')
