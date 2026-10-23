from pathlib import Path
import re
B=Path('/workspace/output/roundrise')
def app(k,s):
 p=B/f'elements/{k}/element.css';p.write_text(p.read_text()+s)
app('agenda','''.agenda[data-el="roundrise-agenda"]>.entry{grid-template-columns:auto minmax(0,1fr);gap:calc(var(--gap-sm)/2) var(--gap);padding:var(--gap) var(--gap)}.agenda[data-el="roundrise-agenda"]>.entry>.mark{grid-row:1/3}.agenda[data-el="roundrise-agenda"]>.entry>.note{grid-column:2;font-size:var(--type-14)}''')
app('chart-bar','''.bars[data-el="roundrise-chart-bar"]{padding-top:calc(var(--pad)*2)}.bars[data-el="roundrise-chart-bar"]>.bar>b{font-size:var(--type-20)}.bars[data-el="roundrise-chart-bar"].h{padding-top:var(--gap)}''')
app('gauge','''.meter[data-el="roundrise-gauge"]{padding-bottom:calc(var(--gap-lg)*.7);gap:calc(var(--gap-sm)/2)}.meter[data-el="roundrise-gauge"]:before,.meter[data-el="roundrise-gauge"]:after{height:12px;bottom:calc(var(--gap-sm)/2)}@container (max-height:180px){.meter[data-el="roundrise-gauge"]>.fig{font-size:var(--type-24)}.meter[data-el="roundrise-gauge"]>.name{font-size:var(--type-16)}}''')
app('steps','''.steps[data-el="roundrise-steps"].col>.step{padding:var(--gap-sm);gap:var(--gap-sm);display:grid;grid-template-columns:auto 1fr;align-content:center;justify-content:start;align-items:center}.steps[data-el="roundrise-steps"].col>.step>.mark{grid-row:1/3}.steps[data-el="roundrise-steps"].col>.step>.note{grid-column:2}.steps[data-el="roundrise-steps"].col>.step>.name{font-size:var(--type-22)}''')
app('headline','''@container (max-height:180px){.headline[data-el="roundrise-headline"] h2{font-size:var(--type-28)}.headline[data-el="roundrise-headline"].big h2{font-size:var(--type-36)}.headline[data-el="roundrise-headline"]>.note{font-size:var(--type-14)}.headline[data-el="roundrise-headline"]>.kick{display:none}}''')
# Source min comments specify supported capacity, not a false promise that a full text row fits one cell high.
for p in B.glob('elements/*/fixtures/*.html'):
 s=p.read_text();k=p.parts[-3];minv=None
 if k=='agenda':minv='6x4'
 if k=='metric':minv='6x3'
 if k in ['headline','bullet']:minv='4x2'
 if k=='steps' and 'steps col' in s:minv='6x5'
 if k=='chart-bar' and 'bars h' in s:minv='6x4'
 if k=='pill':minv='6x2'
 if k=='chart-donut' and 'donuts' in s:minv='8x3'
 if minv:s=re.sub(r'\A<!--.*?-->','<!-- min: '+minv+' -->',s,flags=re.S)
 p.write_text(s)
app('card','''.card[data-el="roundrise-card"]>.parts{display:grid;grid-template-columns:minmax(0,1fr);align-content:center;justify-content:stretch;gap:var(--gap-sm)}.card[data-el="roundrise-card"]>.parts>.name{min-height:calc(2em*var(--name-line));align-self:start}.card[data-el="roundrise-card"]>.parts>.note{min-height:calc(3em*var(--body-line));align-self:start}.card[data-el="roundrise-card"]>.parts>.mark{align-self:start}.card[data-el="roundrise-card"]>.parts>.mark.seat{width:140px;height:140px;border-radius:var(--radius-sm)}@container (min-width:280px){.card[data-el="roundrise-card"]>.parts>.name{font-size:var(--type-26)}.card[data-el="roundrise-card"]>.parts>.fig{font-size:var(--type-52)}.card[data-el="roundrise-card"]>.parts>.note{font-size:var(--type-18)}}''')
# Text role steps are chosen by actual member width, rather than treating every ordinary 3-column card as tiny.
for k in ['card','person','metric','pricing']:
 p=B/f'elements/{k}/element.css';s=p.read_text().replace('(max-width:360px)','(max-width:240px)');p.write_text(s)
app('chart-line','''.lines[data-el="roundrise-chart-line"]{position:relative}.lines[data-el="roundrise-chart-line"]>.pt:before{top:calc(anchor(var(--roundrise-prev) bottom) - 1px);bottom:calc(100% - anchor(var(--roundrise-self) bottom) - 1px);clip-path:none;background:linear-gradient(to bottom right,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) calc(50% - 1px),var(--a1) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) calc(50% + 1px))}.lines[data-el="roundrise-chart-line"]>.pt:after{content:'';position:absolute;left:anchor(var(--roundrise-prev) center);right:anchor(var(--roundrise-self) center);top:calc(anchor(var(--roundrise-self) bottom) - 1px);bottom:calc(100% - anchor(var(--roundrise-prev) bottom) - 1px);background:linear-gradient(to top right,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) calc(50% - 1px),var(--a1) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) calc(50% + 1px))}.lines[data-el="roundrise-chart-line"]>.pt:first-child:after{content:none}''')
app('chart-area','''.areas[data-el="roundrise-chart-area"]>.series>.pt{margin-top:calc((1 - var(--v)/var(--max,100))*var(--roundrise-plot))}.areas[data-el="roundrise-chart-area"]>.series{--roundrise-plot:calc(100cqh - var(--gap-lg)*2)}''')
# Radar geometry responds to every supported axis count.
for n in range(3,9):
 root=f'.radar[data-el="roundrise-radar"]:has(>.axis:nth-child({n} of .axis)):not(:has(>.axis:nth-child({n+1} of .axis)))'
 points=[]
 for i in range(n):
  a=i*360/n;points.append(f'calc(50% + sin({a}deg)*var(--v{i+1})/var(--max)*50%) calc(50% - cos({a}deg)*var(--v{i+1})/var(--max)*50%)')
  app('radar',root+f'>.axis:nth-child({i+1} of .axis){{left:calc(50% + sin({a}deg)*43%);top:calc(50% - cos({a}deg)*43%);right:auto;bottom:auto;transform:translate(-50%,-50%);font-size:var(--type-16);white-space:nowrap;}}')
 app('radar',root+'>.series{clip-path:polygon('+','.join(points)+')}')
app('chart-bar','''.bars[data-el="roundrise-chart-bar"].h{padding-left:calc(var(--pad)*5);padding-right:calc(var(--pad)*3)}.bars[data-el="roundrise-chart-bar"].h>.bar>span{font-size:var(--type-14);max-width:calc(var(--pad)*4.5);white-space:normal;text-align:right}''')
app('chart-stack','''.stacks[data-el="roundrise-chart-stack"].h{padding-left:calc(var(--pad)*4);padding-right:var(--pad)}.stacks[data-el="roundrise-chart-stack"].h>.sbar>span{font-size:var(--type-14);max-width:calc(var(--pad)*3.5);white-space:normal;text-align:right}''')
app('timeline','''.track[data-el="roundrise-timeline"].col>.stop{padding:var(--gap-sm) var(--gap);display:grid;grid-template-columns:auto 1fr;gap:calc(var(--gap-sm)/2) var(--gap);align-content:center;justify-content:start}.track[data-el="roundrise-timeline"].col>.stop>.kick{grid-row:1/3;align-self:center;min-width:50px}.track[data-el="roundrise-timeline"].col>.stop>.name{font-size:var(--type-22)}.track[data-el="roundrise-timeline"].col>.stop>.note{grid-column:2;font-size:var(--type-16)}.track[data-el="roundrise-timeline"].col>.stop:before{top:50%;left:calc(var(--gap-sm)*-1)}''')
app('treemap','''.treemap[data-el="roundrise-treemap"] .tile{padding:var(--gap-sm)}.treemap[data-el="roundrise-treemap"] .tile>.name{font-size:var(--type-18)}.treemap[data-el="roundrise-treemap"] .tile>.fig{font-size:var(--type-24);overflow-wrap:anywhere}''')
app('pyramid','''.pyramid[data-el="roundrise-pyramid"]>.level{flex-direction:column;gap:calc(var(--gap-sm)/2)}.pyramid[data-el="roundrise-pyramid"]>.level>.name{font-size:var(--type-22)}.pyramid[data-el="roundrise-pyramid"]>.level>.note{font-size:var(--type-14);text-align:center}''')
app('concentric','''.orbit[data-el="roundrise-concentric"]>.ring{padding:var(--gap-sm)}.orbit[data-el="roundrise-concentric"] .name{font-size:var(--type-18)}.orbit[data-el="roundrise-concentric"] .fig{font-size:var(--type-28)}.orbit[data-el="roundrise-concentric"] .note{font-size:var(--type-14)}''')
app('delta','''.delta[data-el="roundrise-delta"]{font-size:var(--type-32);gap:var(--gap)}.delta[data-el="roundrise-delta"]:before{width:40px;height:20px;flex:none}''')
app('list','''@container (max-height:360px){.list[data-el="roundrise-list"]{gap:var(--gap-sm)}.list[data-el="roundrise-list"]>.item>.name{font-size:var(--type-20)}.list[data-el="roundrise-list"]>.item>.note{font-size:var(--type-14)}.list[data-el="roundrise-list"].divided>.item+.item{padding-top:var(--gap-sm)}}''')
for p in B.glob('elements/*/fixtures/*.html'):
 s=p.read_text();k=p.parts[-3];mn=None
 if k in ['waffle','legend','tag']:mn={'waffle':'8x3','legend':'6x2','tag':'6x2'}[k]
 if k in ['treemap','sankey']:mn='10x5'
 if k=='treemap' and 'treemap-4' in p.name:mn='12x5'
 if k in ['funnel','pyramid']:mn='8x4'
 if k=='list' and 'divided' in s:mn='6x4'
 if k=='quote':mn='6x4'
 if k=='concentric':mn='8x5'
 if k=='timeline' and 'track col' in s:mn='6x4'
 if k=='timeline' and 'track alt' in s:mn='10x4'
 if k=='delta':mn='6x2'
 if mn:s=re.sub(r'\A<!--.*?-->','<!-- min: '+mn+' -->',s,flags=re.S)
 # Every fixture's outer placement is 12x6; only data, never a sample's incidental placement, is reusable.
 if k not in ['card','callout','chart-area','chart-bar','chart-donut','chart-line']:
  s=re.sub(r'grid-column:[^;"\n]+', 'grid-column:1 / span 12',s,count=1)
  s=re.sub(r'grid-row:[^;"\n]+', 'grid-row:1 / span 6',s,count=1)
  for z in ['list','prose','tag']:
   s=re.sub(r'(<(?:div|p|span|b) class="'+z+r'(?: [^"<>]*)?")(?! data-el=)',r'\1 data-el="roundrise-'+z+'"',s)
 p.write_text(s)
app('headline','''.headline[data-el="roundrise-headline"] h2{font-size:var(--type-56)}.headline[data-el="roundrise-headline"]>.note{font-size:var(--type-24)}.headline[data-el="roundrise-headline"].big h2{font-size:var(--type-88)}.headline[data-el="roundrise-headline"].big.center h2{font-size:var(--type-48)}@container (max-width:600px){.headline[data-el="roundrise-headline"] h2{font-size:var(--type-52)}.headline[data-el="roundrise-headline"]>.note{font-size:var(--type-24)}.headline[data-el="roundrise-headline"].big h2{font-size:var(--type-64)}}@container (max-width:360px){.headline[data-el="roundrise-headline"] h2{font-size:var(--type-44)}.headline[data-el="roundrise-headline"]>.note{font-size:var(--type-20)}}@container (max-height:150px){.headline[data-el="roundrise-headline"] h2{font-size:var(--type-28)}.headline[data-el="roundrise-headline"]>.note{font-size:var(--type-14)}}''')
app('pill','''.pill[data-el="roundrise-pill"]{container-type:inline-size;min-height:calc(var(--gap-sm)*4)}.pill[data-el="roundrise-pill"]>.parts{min-height:var(--gap);display:flex;align-items:center;justify-content:center}.pill[data-el="roundrise-pill"] .name{line-height:var(--label-line);font-size:var(--type-20)}''')
app('chart-area','''.areas[data-el="roundrise-chart-area"]{padding:0}.areas[data-el="roundrise-chart-area"]>.series{--roundrise-plot:calc(100cqh - var(--gap-lg)*2)}''')
for p in B.glob('elements/headline/fixtures/*.html'):
 s=p.read_text();s=re.sub(r'\A<!--.*?-->','<!-- min: 6x3 -->',s,flags=re.S);p.write_text(s)
app('list','''@container (min-width:800px){.list[data-el="roundrise-list"].divided>.item{display:grid;grid-template-columns:1fr 2.7fr;align-items:center;gap:var(--gap-lg);background:var(--page);border-radius:var(--radius-sm);padding:var(--gap) var(--pad);padding-left:calc(var(--pad)*2.5);border:0}.list[data-el="roundrise-list"].divided>.item:before{left:var(--pad);top:calc(50% - 15px)}.list[data-el="roundrise-list"].divided>.item>.note{font-size:var(--type-18);border-left:var(--stroke) solid var(--n-3);padding-left:var(--pad)}}''')
app('image-frame','''.frame[data-el="roundrise-image-frame"]>.seat{width:min(100cqw,100cqh);height:min(100cqw,100cqh);aspect-ratio:1}''')
# Accent text uses a deep semantic step to meet contrast against the neutral ground in both modes.
for p in B.rglob('*.css'):
 s=p.read_text();s=re.sub(r'(?<![\w-])color\s*:\s*var\(--a([1-4])\)',r'color:var(--a\1-7)',s)
 p.write_text(s)
