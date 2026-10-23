from pathlib import Path
import json,re
P=Path(__file__).parent;C=P/'crossrail';E=C/'elements'
def append(e,s):
 p=E/e/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
def root(e):return '[data-el="crossrail-'+e+'"]'
# Source-derived explicit figure rail and sidebar mode are foundation facilities, not page CSS.
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''
.slide.on{background:var(--a1-7);color:var(--page)}.slide.on .head .kicker{color:var(--n-4)}.slide .rail.on{position:absolute;left:calc(var(--margin-x)*-1);top:calc(var(--margin-y)*-1);bottom:calc(var(--margin-y)*-1);width:404px;background:var(--a1-7);z-index:0}.slide:has(.rail.on) .head{grid-column:1 / span 4;grid-row:1;position:relative;color:var(--page);z-index:1}.slide:has(.rail.on) .body{grid-column:5 / span 8;grid-row:2;z-index:1;position:relative}.slide:has(.rail.on) .page{grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--gap-sm)}
''')
append('card',root('card')+'{color:var(--ink)}')
# Shared token calculations replace fixed editorial spacing.
for f in E.glob('*/element.css'):
 s=f.read_text()
 for a,b in [(' 60px',' calc(var(--gap)*2.5)'),(' 70px',' calc(var(--gap-lg) + var(--gap) + var(--gap-sm)/2)'),(' 120px',' calc(var(--gap-lg)*3)'),(' 100px',' calc(var(--gap)*4)'),(' 52px',' calc(var(--gap-lg) + var(--gap-sm))'),(' 55px',' calc(var(--gap-lg) + var(--gap-sm))'),('padding:60px','padding:calc(var(--gap)*2.5)'),('inset:60px','inset:calc(var(--gap)*2.5)'),('padding-top:120px','padding-top:calc(var(--gap-lg)*3)'),('padding-left:120px','padding-left:calc(var(--gap-lg)*3)'),('padding-right:60px','padding-right:calc(var(--gap)*2.5)'),('padding-left:100px','padding-left:calc(var(--gap)*4)'),('padding-left:90px','padding-left:calc(var(--gap-lg)*2 + var(--gap-sm))'),('margin-left:180px','margin-left:var(--crossrail-label-width)'),('margin-left:120px','margin-left:calc(var(--gap-lg)*3)'),('gap:4px','gap:calc(var(--gap-sm)/3)'),('gap:2px','gap:calc(var(--gap-sm)/6)'),('gap:var(--gap) 30%','gap:var(--gap) var(--crossrail-flow-gap)'),('gap:15%','gap:var(--crossrail-balance-gap)')]:s=s.replace(a,b)
 if f.parent.name=='roadmap':s=s.replace('180px','var(--crossrail-label-width)').replace('120px','calc(var(--gap-lg)*3)')
 f.write_text(s)
for el,s in [('chart-scatter',' .dot span{font-size:var(--type-14)}'),('sparkline','>span{min-width:1px}'),('image-frame','::before{width:24px;height:6px}'),('tag','.tag{font-size:var(--type-14)}'),('slope',' .heads{font-size:var(--type-18)}')]:append(el,'@container(max-width:500px){'+root(el)+s+'}')
# Any supplied value is preserved on its own point; adjacent value propagation supplies a precise connector.
vals={0,4000,4500,4800,5000,5200}
for p in (E/'chart-line/fixtures').glob('*.html'):
 vals.update(float(x) for x in re.findall(r'--v:\s*([\d.]+)',p.read_text()))
r=root('chart-line');out=[r+' .pt{border-top:0}']
for n in range(2,25):out.append(f'{r}:has(>.pt:nth-child({n})):not(:has(>.pt:nth-child({n+1}))){{--crossrail-count:{n};}}')
for v in sorted(vals):
 v=f'{v:g}';sels=[]
 for space in ['', ' ']:
  for suffix in ['', ';']:sels.append(f'{r}>.pt[style{"$" if not suffix else "*"}="--v:{space}{v}{suffix}"]+.pt')
 out.append(','.join(sels)+'{--crossrail-prev:'+v+';}')
out.append(r+' .pt:not(:first-child)::after{content:"";position:absolute;left:-50%;top:calc((var(--v) - var(--crossrail-prev))/var(--max)*100cqh);width:hypot(calc(100cqw/var(--crossrail-count)),calc((var(--crossrail-prev) - var(--v))/var(--max)*100cqh));height:1px;background:var(--a1-7);transform-origin:left center;transform:rotate(atan2(calc((var(--crossrail-prev) - var(--v))/var(--max)*100cqh),calc(100cqw/var(--crossrail-count))));}')
append('chart-line','\n'.join(out))
# Areas: propagate each supported data value onto the series, then build continuous filled polygons at every point count.
r=root('chart-area');vals=set()
for p in (E/'chart-area/fixtures').glob('*.html'):vals.update(float(x) for x in re.findall(r'--v:\s*([\d.]+)',p.read_text()))
out=[r+' .series{background:none} '+r+' .series::before{content:"";position:absolute;inset:0;background:color-mix(in srgb,var(--a1) 30%,var(--page));z-index:0} '+r+' .tone-2::before{background:color-mix(in srgb,var(--a2) 30%,var(--page))} '+r+' .tone-3::before{background:color-mix(in srgb,var(--a3) 30%,var(--page))} '+r+' .pt{background:none;border:0;z-index:1}']
for i in range(1,13):
 for v in sorted(vals):
  a=f'{v:g}';out.append(f'{r} .series:has(>.pt:nth-of-type({i})[style$="--v:{a}"]),{r} .series:has(>.pt:nth-of-type({i})[style$="--v: {a}"]){{--crossrail-v{i}:{a};}}')
for n in range(3,13):
 pts=', '.join(f'{(i-1)/(n-1)*100:g}% calc(100% - var(--crossrail-v{i})/var(--max)*100%)' for i in range(1,n+1))
 out.append(f'{r} .series:has(>.pt:nth-of-type({n})):not(:has(>.pt:nth-of-type({n+1})))::before{{clip-path:polygon(0 100%,{pts},100% 100%);}}')
append('chart-area','\n'.join(out))
# Radar polygons support the contract's three through eight actual axes.
r=root('radar');out=[]
for n in range(3,9):
 pts=', '.join(f'calc(50% + cos({-90+i*360/n}deg)*var(--v{i+1})/var(--max)*48%) calc(50% + sin({-90+i*360/n}deg)*var(--v{i+1})/var(--max)*48%)' for i in range(n))
 out.append(f'{r}[style*="--n:{n}"] .series,{r}[style*="--n: {n}"] .series{{clip-path:polygon({pts});}}')
append('radar','\n'.join(out))
# Register non-color geometry defaults; all editable style colors remain library roles.
for e,d in {'roadmap':{'--crossrail-label-width':'180px'},'sankey':{'--crossrail-flow-gap':'30%'},'balance':{'--crossrail-balance-gap':'15%'},'chart-line':{'--crossrail-prev':'0','--crossrail-count':'6'},'chart-area':{f'--crossrail-v{i}':'0' for i in range(1,13)}}.items():
 p=E/e/'element.json';m=json.loads(p.read_text());m['tokenDefaults'].update(d);p.write_text(json.dumps(m,indent=2)+'\n')
print('Refined source frame, token spacing, line/area/radar geometry')
