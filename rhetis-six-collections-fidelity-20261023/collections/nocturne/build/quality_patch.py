from pathlib import Path
C=Path('/workspace/work/deliverables/nocturne/collection/nocturne')
def patch(name,css):
 p=C/'elements'/name/'element.css';p.write_text(p.read_text()+css.replace('R',f'[data-el="nocturne-{name}"]')+'\n')
patch('timeline','''R.col .stop{min-height:0;display:grid;grid-template-columns:var(--type-60) 1fr;grid-template-rows:auto auto;align-content:center;column-gap:var(--gap-sm);row-gap:calc(var(--gap-sm)/3);padding:calc(var(--gap-sm)/2) var(--pad)}R.col .stop>.kick{grid-row:1/3;align-self:center;font-size:var(--type-22)}R.col .stop>.name{font-size:var(--type-22)}R.col .stop>.note{font-size:var(--type-16)}@container(max-height:400px){R.col .stop>.kick,R.col .stop>.name{font-size:var(--type-18)}R.col .stop>.note{font-size:var(--type-14)}}''')
patch('positioning','''R .axis-x,R .axis-y{color:var(--ink)}''')
patch('versus','''R .vs{color:var(--ink)}''')
patch('code','''R .s{color:color-mix(in srgb,var(--good) 60%,var(--ink))}''')
patch('journey','''R .pain{color:var(--ink);border-left:var(--stroke) solid var(--bad);padding-left:var(--gap-sm)}''')
patch('chart-area','''R .series:nth-of-type(3)>.name,R .series:nth-of-type(3) .pt>b{color:var(--a3-8)}''')
patch('chart-stack','''R .seg.tone-1 b{color:var(--a1-on)}R .seg.tone-2 b{color:var(--a2-on)}R .seg.tone-3 b{color:var(--a3-on)}R .seg.tone-4 b{color:var(--a4-on)}''')
patch('chart-scatter','''R .dot>span{color:var(--ink);background:var(--page);border-radius:999px;padding:calc(var(--gap-sm)/4)}''')
patch('roadmap','''R .mile>span{color:var(--ink);background:var(--page);border-radius:999px;padding:calc(var(--gap-sm)/4)}''')
patch('agenda','''@container(max-height:400px){R .entry{padding:calc(var(--gap-sm)/2);grid-template-columns:40px 1fr;min-height:0}R .mark{width:40px;height:40px;font-size:var(--type-18)}R .name{font-size:var(--type-18)}R .note{font-size:var(--type-14)}}''')
patch('architecture','''@container(max-height:400px){R .layer{padding:calc(var(--gap-sm)/2) var(--gap-sm);min-height:0}R .chip{min-height:32px;font-size:var(--type-14)}R .layer>.name{font-size:var(--type-18)}}''')
patch('funnel','''@container(max-height:400px){R .stage{min-height:0;padding:calc(var(--gap-sm)/2) var(--gap-sm)}R .name{font-size:var(--type-18)}R .fig{font-size:var(--type-22)}}''')
patch('pyramid','''@container(max-height:400px){R .level{min-height:0;padding:calc(var(--gap-sm)/2) var(--gap-sm);gap:calc(var(--gap-sm)/3)}R .name{font-size:var(--type-18)}R .note{font-size:var(--type-14)}}''')
patch('treemap','''R>.branch{display:grid;grid-template-columns:repeat(100,minmax(0,1fr));grid-template-rows:auto minmax(0,1fr);gap:var(--gap-sm) 0;container-type:inline-size}R .branch>.name{grid-column:1/-1}R .tile{grid-column:span var(--v);grid-row:2;min-width:0;padding:calc(var(--gap-sm)/2);margin:0 calc(var(--gap-sm)/4)}R .tile .name{font-size:var(--type-18)}R .tile .fig{font-size:var(--type-20)}@container(max-width:180px){R .branch>.name,R .tile .name{font-size:var(--type-14)}R .tile .fig{font-size:var(--type-18)}R .tile{padding:calc(var(--gap-sm)/3)}}''')
patch('waffle','''R .units{width:min(100%,calc(100cqh - var(--type-128) - var(--gap)));max-width:400px;max-height:none;flex:none}R.figures .units{width:min(100%,150cqh);max-width:none;max-height:none}''')
# Empty image/icon seats in the fixed model fixture must remain inside their own marks.
patch('card','''R .mark:has(>.seat){width:72px;height:72px;flex:none}R .mark>.seat{max-width:100%;max-height:100%;width:64px;height:64px;aspect-ratio:1}R .mark>.icon{display:flex;align-items:center;justify-content:center;line-height:var(--label-line)}''')
# Remove obsolete whitespace-sensitive radar selectors; style queries are the authoritative geometry.
p=C/'elements/radar/element.css';s=p.read_text();import re;s=re.sub(r'\[data-el="nocturne-radar"\]\[style\*="--n:\d+"\][^{}]*\{[^{}]*\}','',s);p.write_text(s)
print('Parent sweep findings and contrast safeguards applied')

patch('chart-line','''R .pt>b::after{margin-bottom:0}R .pt::before{top:calc(anchor(var(--nocturne-prev) bottom) - var(--nocturne-line-plot) - 5px);bottom:calc(var(--pad) + var(--type-32) + var(--stroke) + 5px)}''')

patch('bullet','''R.bullet::after{width:clamp(0%,calc(var(--v)*1%),100%)}R .fig::after{left:clamp(0px,calc(var(--target)*1%),calc(100% - 3px))}''')
