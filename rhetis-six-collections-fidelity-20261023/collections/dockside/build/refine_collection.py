from pathlib import Path
import math,re,json
C=Path('/workspace/work/deliverables/dockside/collection/dockside')
def append(f,s):p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n/* Browser review refinements. */\n'+s+'\n')
def root(f):
 d=json.load(open(C/f'elements/{f}/element.json'));tax=json.load(open('/workspace/work/reference/contract/taxonomy.json'))['contracts'];c=next(x for x in tax if x['id']==d['contract']);return ':is('+','.join('.'+x+'[data-el="dockside-'+f+'"]' for x in c['roots'])+')'
f='chart-area';r=root(f)
append(f,f'''{r} .pt{{--dockside-height:calc(100cqh - var(--gap-lg)*2);--dockside-value-height:calc(var(--dockside-height)*var(--v)/var(--max));margin-top:calc(var(--dockside-height) - var(--dockside-value-height))}}{r} .pt::before{{top:calc(anchor(var(--dockside-prev) top) - var(--dockside-height));bottom:0;background:var(--a1-2-soft);clip-path:polygon(0 var(--dockside-height),100% calc(100% - var(--dockside-value-height)),100% 100%,0 100%)}}{r} .pt::after{{top:calc(anchor(var(--dockside-prev) top) - var(--dockside-height));bottom:0;clip-path:polygon(0 calc(var(--dockside-height) - 1px),100% calc(100% - var(--dockside-value-height) - 1px),100% calc(100% - var(--dockside-value-height) + 1px),0 calc(var(--dockside-height) + 1px))}}{r} .series>.name{{left:0}}{r} .series:nth-of-type(2)>.name{{left:25%}}{r} .series:nth-of-type(3)>.name{{left:50%}}{r} .series:nth-of-type(4)>.name{{left:75%}}@container(max-width:550px){{{r} .axis span:nth-child(even){{visibility:hidden}}{r} .axis span{{font-size:var(--type-12)}}{r} .series>.name{{font-size:var(--type-12)}}}}''')
f='chart-donut';r=root(f);append(f,f'''@container (max-width:650px){{{r}.donuts:has(>.donut:nth-child(4)){{display:grid;grid-template-columns:1fr 1fr;gap:var(--gap-sm);align-items:center}}{r}.donuts:has(>.donut:nth-child(4))>.donut{{width:100%;max-height:100%;height:auto;flex:none;border-width:7px}}{r}.donuts:has(>.donut:nth-child(4))>.donut::before{{inset:9px}}{r}.donuts:has(>.donut:nth-child(4)) .name{{font-size:var(--type-12)}}{r}.donuts:has(>.donut:nth-child(4)) .fig{{font-size:var(--type-24)}}}}''')
f='radar';r=root(f);s=f'{r}>.series{{clip-path:none;background:none;border:none}}{r}>.series::before{{content:"";position:absolute;inset:0;background:color-mix(in srgb,var(--a1) 24%,transparent)}}{r}>.series.tone-2::before{{background:color-mix(in srgb,var(--a2) 24%,transparent)}}{r}>.series.tone-3::before{{background:color-mix(in srgb,var(--a3) 24%,transparent)}}{r}>.series>.name{{top:calc(var(--gap-lg)*-1);bottom:auto;left:0;font-size:var(--type-14)}}{r}>.series:nth-of-type(2)>.name{{left:30%}}{r}>.series:nth-of-type(3)>.name{{left:60%}}{r}::before{{background:repeating-conic-gradient(var(--n-3) 0deg .3deg,transparent .3deg calc(360deg/var(--n)))}}'
for n in range(3,9):
 pts=[]
 for i in range(n):
  x=math.sin(i*2*math.pi/n)*50;y=-math.cos(i*2*math.pi/n)*50
  pts.append(f'calc(50% + var(--v{i+1})/var(--max)*{x:.5f}%) calc(50% + var(--v{i+1})/var(--max)*{y:.5f}%)')
 s+=f'{r}[style*="--n:{n}"]>.series::before,{r}[style*="--n: {n}"]>.series::before{{clip-path:polygon('+','.join(pts)+')}}'
append(f,s)
# Give non-normative examples honest minimum allocations for the new design, not the old sample design.
req={'card':['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone'],'callout':['callout','callout-icon','callout-stack'],'chart-area':['area-1','areas-2','areas-stacked-3','area-3pt'],'chart-bar':['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2'],'chart-donut':['donut','donuts-3','donuts-4','donut-0','donut-100'],'chart-line':['lines-12','lines-6','lines-3','lines-flat']}
small={'tag':'3x2','pill':'6x2','delta':'4x2','legend':'6x2','sparkline':'4x2','image-frame':'4x4','logo-group':'8x3'}
for p in C.glob('elements/*/fixtures/*.html'):
 f=p.parent.parent.name
 if p.stem in req.get(f,[]):continue
 s=p.read_text();m=small.get(f,'8x4');s=re.sub(r'\A<!--\s*min:.*?-->\s*','',s);p.write_text(f'<!-- min: {m} -->\n'+s)
# Prevent nested graphic labels from inheriting the root-sized type.
for f in ['cycle','hub','architecture','hierarchy','mindmap','decision-tree','journey','roadmap','matrix','matrix-nine']:
 r=root(f);append(f,f'@container(max-width:650px){{{r} .name{{font-size:var(--type-16)}}{r} .note{{font-size:var(--type-14)}}}}')
# Defaults for dynamic data geometry.
p=C/'elements/chart-area/element.json';d=json.loads(p.read_text());d['tokenDefaults'].update({'--dockside-height':'300px','--dockside-value-height':'150px'});p.write_text(json.dumps(d,indent=2)+'\n')
