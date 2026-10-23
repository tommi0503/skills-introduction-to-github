from pathlib import Path
O=Path('/workspace/output/fluxweave/elements')
def add(k,s):
 p=O/k/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('network','''[data-el="fluxweave-network"]>.link{left:calc(5% + var(--x1)*.9%);top:calc(90% - var(--y1)*.8%);width:hypot(calc((var(--x2) - var(--x1))*.9cqw),calc((var(--y2) - var(--y1))*-.8cqh));rotate:atan2(calc((var(--y2) - var(--y1))*-.8cqh),calc((var(--x2) - var(--x1))*.9cqw));}''')
add('chart-waterfall','''[data-el="fluxweave-chart-waterfall"]>.move:not(:last-child)::after{content:"";position:absolute;left:90%;width:calc(20% + var(--gap));bottom:calc(var(--to)/var(--max)*80%);height:var(--stroke);background:var(--n-4);}''')
add('heatmap','''[data-el="fluxweave-heatmap"].calendar{--fluxweave-cell:min(calc((100cqw - (var(--cols) - 1)*var(--gap-sm))/var(--cols)),calc((100cqh - var(--type-14)*var(--label-line) - var(--gap-sm)*7)/7));align-items:center;gap:var(--gap-sm);}[data-el="fluxweave-heatmap"].calendar>.row{flex:none;max-height:none;height:var(--fluxweave-cell);grid-template-columns:repeat(var(--cols),var(--fluxweave-cell));}[data-el="fluxweave-heatmap"].calendar>.heads{grid-template-columns:repeat(var(--cols),var(--fluxweave-cell));gap:var(--gap-sm);}[data-el="fluxweave-heatmap"].calendar .cell{width:var(--fluxweave-cell);height:var(--fluxweave-cell);aspect-ratio:1;}''')
s=''
for n in [2,3,5,6]:
 p=f'[data-el="fluxweave-mindmap"]>.branch:nth-child({n})::before'
 left=n in [2,6];upper=n in [2,3]
 a=f'--fluxweave-mindmap-{n}'
 vals=f'left:anchor({a} right);right:anchor(--fluxweave-mindmap-core left);' if left else f'left:anchor(--fluxweave-mindmap-core right);right:anchor({a} left);'
 vals+=f'top:anchor({a if upper else "--fluxweave-mindmap-core"} center);bottom:anchor({"--fluxweave-mindmap-core" if upper else a} center);'
 edge='top' if upper else 'bottom';side='right' if left else 'left';radius=('0 100% 0 0' if left else '100% 0 0 0') if upper else ('0 0 100% 0' if left else '0 0 0 100%')
 s+=p+'{'+vals+f'width:auto;height:auto;background:none;border:0;border-{edge}:var(--stroke) solid var(--a1-3-soft);border-{side}:var(--stroke) solid var(--a1-3-soft);border-radius:{radius};'+'}'
add('mindmap',s)
add('decision-tree','''[data-el="fluxweave-decision-tree"] .opts{position:relative;border-top:0;--fluxweave-opts:2;}[data-el="fluxweave-decision-tree"] .opts:has(>.opt:nth-child(3):last-child){--fluxweave-opts:3;}[data-el="fluxweave-decision-tree"] .opts::before{content:"";position:absolute;left:calc((100% + var(--gap-lg))/var(--fluxweave-opts)/2 - var(--gap-lg)/2);right:calc((100% + var(--gap-lg))/var(--fluxweave-opts)/2 - var(--gap-lg)/2);top:0;height:var(--stroke);background:var(--n-4);}[data-el="fluxweave-decision-tree"] .cond{position:relative;}[data-el="fluxweave-decision-tree"] .cond::after{content:"";position:absolute;left:50%;top:100%;height:var(--gap);width:var(--stroke);background:var(--n-4);}[data-el="fluxweave-decision-tree"] .opt>.q:has(+.opts)::after{height:var(--gap);}[data-el="fluxweave-decision-tree"] .opt>.opts{margin-top:0;}''')
# Radial polygons use the actual number of axes, including all eight values.
s=''
for n in range(3,9):
 coords=','.join(f'calc(50% + cos({-90+i*360/n}deg)*var(--v{i+1})/var(--max)*50%) calc(50% + sin({-90+i*360/n}deg)*var(--v{i+1})/var(--max)*50%)' for i in range(n))
 # Root axis count is structural, not a substring match which confuses --n with whitespace.
 pred=f'[data-el="fluxweave-radar"]:has(>.axis:nth-child({n} of .axis):last-of-type)' # axis b last-of-type accounts .series div below
 s+=pred+'>.series::before{clip-path:polygon('+coords+');}'
s+='''[data-el="fluxweave-radar"]>.series::before{opacity:.7;}[data-el="fluxweave-radar"]>.series:nth-child(2 of .series)::before{background:var(--a2-3-soft);}[data-el="fluxweave-radar"]>.series:nth-child(3 of .series)::before{background:var(--a3-3-soft);}[data-el="fluxweave-radar"]>.series:nth-child(2 of .series)>.name{color:var(--a2-7);}[data-el="fluxweave-radar"]>.series:nth-child(3 of .series)>.name{color:var(--a3-7);}'''
add('radar',s)
# Shared labels stay visible in the actual overlap, without changing icon-bearing source slide.
add('venn','''[data-el="fluxweave-venn"]:not(:has(>.set .icon))>.set{background:color-mix(in srgb,var(--a1) 28%,var(--page));}[data-el="fluxweave-venn"]:not(:has(>.set .icon))>.set.on{background:color-mix(in srgb,var(--a1) 38%,var(--page));color:var(--ink);}[data-el="fluxweave-venn"]:not(:has(>.set .icon)):has(>.set:nth-child(3))>.set:nth-child(2){background:color-mix(in srgb,var(--a2) 28%,var(--page));color:var(--ink);}[data-el="fluxweave-venn"]:not(:has(>.set .icon)):has(>.set:nth-child(3))>.set:nth-child(3){background:color-mix(in srgb,var(--a3) 28%,var(--page));color:var(--ink);}[data-el="fluxweave-venn"]:not(:has(>.set .icon))>.core{color:var(--ink);background:var(--page);padding:calc(var(--gap-sm)/3);border-radius:var(--radius-sm);}''')
print('patched seven semantic element files')
# Series without optional tone classes still receive distinct identities; translucent
# overlapping surfaces preserve the lower series and its terminal value.
s=''
for n in [1,2,3]:
 a=f'--a{n}'
 root='[data-el="fluxweave-chart-area"]:has(>.series:nth-child(2 of .series))'
 s+=f'{root}>.series:nth-child({n} of .series)>.pt::before'+'{background:color-mix(in srgb,var('+a+') 30%,var('+a+') 0%);}'
 s+=f'{root}>.series:nth-child({n} of .series)>.pt::after'+'{background:var('+a+');}'
 s+=f'{root}>.series:nth-child({n} of .series)>.name'+'{color:var('+a+'-7);}'
add('chart-area',s)
