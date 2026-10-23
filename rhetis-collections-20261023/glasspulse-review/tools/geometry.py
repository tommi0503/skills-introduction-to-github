from pathlib import Path
import math
C=Path('/workspace/output/glasspulse/elements')
def r(folder,roots):return ':is('+','.join('.'+x+f'[data-el="glasspulse-{folder}"]' for x in roots)+')'
def add(folder,s):p=C/folder/'element.css';p.write_text(p.read_text()+'\n'+s)
rn=r('network',['network'])
add('network',f'''{rn} .link{{left:calc(10% + var(--x1)*.8%);top:calc(10% + var(--y1)*.8%);width:hypot(calc((var(--x2) - var(--x1))*.8cqw),calc((var(--y2) - var(--y1))*.8cqh));height:2px;background:var(--n-4);transform-origin:0 50%;transform:rotate(atan2(calc((var(--y2) - var(--y1))*.8cqh),calc((var(--x2) - var(--x1))*.8cqw)))}} {rn} .link.strong{{background:var(--a1);height:3px}}''')
rr=r('radar',['radar'])
s=f'''{rr}::before{{width:min(70cqw,70cqh);height:min(70cqw,70cqh);left:50%;top:50%;transform:translate(-50%,-50%);clip-path:none;border-radius:50%}} {rr} .series{{inset:auto;left:50%;top:50%;width:min(70cqw,70cqh);height:min(70cqw,70cqh);transform:translate(-50%,-50%);background:none;border:0;clip-path:none;color:var(--a1-7)}} {rr} .series:nth-child(2 of .series){{color:var(--a2-7)}} {rr} .series:nth-child(3 of .series){{color:var(--a3-7)}} {rr} .series::before{{content:'';position:absolute;inset:0;background:color-mix(in srgb,currentColor 22%,var(--page));border:var(--stroke) solid currentColor}} {rr} .series .name{{display:block;position:absolute;top:calc(var(--gap-lg)*-1);left:0;white-space:nowrap;font-size:var(--type-16);font-weight:var(--label-weight);color:var(--ink)}} {rr} .series:nth-child(2 of .series) .name{{left:45%}} {rr} .series:nth-child(3 of .series) .name{{left:75%}}'''
for n in range(3,9):
 points=[];rules=''
 for i in range(n):
  a=-90+i*360/n
  points.append(f'calc(50% + cos({a}deg)*var(--v{i+1})/var(--max)*45%) calc(50% + sin({a}deg)*var(--v{i+1})/var(--max)*45%)')
  rules+=f'{rr} .axis:nth-child({i+1} of .axis){{left:calc(50% + cos({a}deg)*min(42cqw,42cqh));top:calc(50% + sin({a}deg)*min(42cqw,42cqh))}}'
 s+=f' @container style(--n: {n})'+'{'+f'{rr} .series::before{{clip-path:polygon('+','.join(points)+')}'+rules+'}'
add('radar',s)
ro=r('concentric',['orbit']);s=''
for i,v in [(1,90),(2,62),(3,36),(4,18)]:
 s+=f'{ro} .ring:nth-child({i}){{inset:auto;left:50%;top:50%;width:min({v}cqw,{v}cqh);height:min({v}cqw,{v}cqh);transform:translate(-50%,-50%);padding:var(--gap-sm);font-size:var(--type-20)}}'
s+=f'{ro} .ring{{flex-wrap:wrap;align-content:flex-start;gap:calc(var(--gap-sm)/2)}} {ro} .ring .note{{flex-basis:100%;text-align:center;font-size:var(--type-14)}} {ro} .ring:last-child{{align-content:center}}'
add('concentric',s)
rs=r('sankey',['sankey']);add('sankey',f'{rs} .branch .branch{{display:flex;flex:1 1 60%;font-size:var(--type-16)}} {rs} .branch:has(>.branch){{flex-wrap:wrap}}')
rb=r('balance',['balance']);add('balance',f'{rb} .fulcrum{{position:absolute;left:50%;bottom:var(--gap-sm);transform:translateX(-50%);width:160px}}')

# Final contrast pair corrections
add('pill',':is(.pill[data-el="glasspulse-pill"]).on .mark{color:var(--a1-on)}')
add('matrix',':is(.matrix[data-el="glasspulse-matrix"])>.cell.on .kick{color:var(--a1-on)}')
add('chart-area',':is(.areas[data-el="glasspulse-chart-area"])>.series:nth-child(2){color:var(--a2-7)} :is(.areas[data-el="glasspulse-chart-area"])>.series:nth-child(3){color:var(--a3-7)}')
add('code',':is(.code[data-el="glasspulse-code"]) .s{color:var(--a3-7)} :is(.code[data-el="glasspulse-code"]) .n{color:var(--a2-7)} :is(.code[data-el="glasspulse-code"]) .c{color:var(--n-8)}')

add("waffle",':is(.waffle[data-el="glasspulse-waffle"]) .units{width:min(60cqw,85cqh);height:auto;max-height:100%;aspect-ratio:1;align-content:center;justify-self:center;grid-auto-rows:auto}')

add("chart-bar",':is(.bars[data-el="glasspulse-chart-bar"]).h{border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);box-shadow:inset 0 0 0 1px var(--n-2)}')

p=C.parent/'foundation/foundation.css';p.write_text(p.read_text()+'\n.slide .title b{color:var(--a1-7);font-weight:var(--title-weight)}')

add("card",':is(.card[data-el="glasspulse-card"]):has(>.parts>:is(.bars,.areas))>.parts{display:grid;grid-template-rows:minmax(0,1fr) auto;height:100%;gap:var(--gap-sm)} :is(.card[data-el="glasspulse-card"]) .parts>.bars,:is(.card[data-el="glasspulse-card"]) .parts>.areas{border:0;background:none;box-shadow:none} :is(.card[data-el="glasspulse-card"]) .parts>.callout{height:auto;border:0;background:none;box-shadow:none;padding:var(--gap-sm);} :is(.card[data-el="glasspulse-card"]) .parts>.callout p{font-size:var(--type-32);line-height:var(--lead-line)}')
add("tag",':is(.tag[data-el="glasspulse-tag"],.hl[data-el="glasspulse-tag"]){width:auto;height:auto;container-type:normal} .hl[data-el="glasspulse-tag"]{font-size:var(--type-20)}')

add("card",':is(.card[data-el="glasspulse-card"]):has(>.parts>:is(.bars,.areas))>.parts{grid-template-columns:minmax(0,1fr);justify-content:stretch;align-items:stretch}')

add("card",':is(.card[data-el="glasspulse-card"]).tone-1{border-color:var(--a1);background:linear-gradient(0deg,var(--a1-2-soft),var(--n-1) 55%)}:is(.card[data-el="glasspulse-card"]).tone-2{background:linear-gradient(0deg,var(--a2-1-soft),var(--n-1) 55%)}:is(.card[data-el="glasspulse-card"]).tone-3{background:linear-gradient(0deg,var(--a3-1-soft),var(--n-1) 55%)}:is(.card[data-el="glasspulse-card"]).tone-4{background:linear-gradient(0deg,var(--a4-1-soft),var(--n-1) 55%)}:is(.card[data-el="glasspulse-card"]).tone-5{background:linear-gradient(0deg,var(--n-2),var(--n-1) 55%)}')

add("list",'.list[data-el="glasspulse-list"]{container-type:inline-size;height:auto}')

add("timeline",'.track[data-el="glasspulse-timeline"].alt{display:grid;grid-template-columns:repeat(var(--glasspulse-count,6),minmax(0,1fr));grid-template-rows:1fr 1fr;row-gap:var(--gap-lg)} .track[data-el="glasspulse-timeline"].alt>.stop{display:flex;flex-direction:column;gap:var(--gap-sm);grid-column:var(--glasspulse-i);grid-row:1;align-self:end} .track[data-el="glasspulse-timeline"].alt>.stop:nth-child(even){grid-row:2;align-self:start} .track[data-el="glasspulse-timeline"].alt>.stop::after{content:"";position:absolute;left:50%;top:100%;width:2px;height:calc(var(--gap-lg)/2);background:var(--n-4)} .track[data-el="glasspulse-timeline"].alt>.stop:nth-child(even)::after{top:auto;bottom:100%}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(1){--glasspulse-i:1}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(2){--glasspulse-i:2}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(3){--glasspulse-i:3}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(4){--glasspulse-i:4}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(5){--glasspulse-i:5}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(6){--glasspulse-i:6}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(7){--glasspulse-i:7}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(8){--glasspulse-i:8}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(9){--glasspulse-i:9}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(10){--glasspulse-i:10}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(11){--glasspulse-i:11}.track[data-el="glasspulse-timeline"].alt>.stop:nth-child(12){--glasspulse-i:12}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(2):last-child){--glasspulse-count:2}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(3):last-child){--glasspulse-count:3}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(4):last-child){--glasspulse-count:4}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(5):last-child){--glasspulse-count:5}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(6):last-child){--glasspulse-count:6}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(7):last-child){--glasspulse-count:7}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(8):last-child){--glasspulse-count:8}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(9):last-child){--glasspulse-count:9}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(10):last-child){--glasspulse-count:10}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(11):last-child){--glasspulse-count:11}.track[data-el="glasspulse-timeline"].alt:has(>.stop:nth-child(12):last-child){--glasspulse-count:12}')

add('matrix','.matrix[data-el="glasspulse-matrix"].swot>.cell{padding:var(--gap-sm);gap:calc(var(--gap-sm)/2)} .matrix[data-el="glasspulse-matrix"].swot .kick{font-size:var(--type-28);line-height:var(--figure-line)} .matrix[data-el="glasspulse-matrix"].swot>.cell>.name{font-size:var(--type-24);line-height:var(--name-line)} .matrix[data-el="glasspulse-matrix"].swot .list{flex-shrink:0}')

add('pricing',':is(.plan[data-el="glasspulse-pricing"],.plans[data-el="glasspulse-pricing"]) .list{gap:var(--gap-sm);flex-shrink:0}')

add('timeline','.track[data-el="glasspulse-timeline"].alt>.stop{gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);padding-top:var(--gap)} .track[data-el="glasspulse-timeline"].alt>.stop .name{font-size:var(--type-22);line-height:var(--name-line)} .track[data-el="glasspulse-timeline"].alt>.stop .note{font-size:var(--type-16)}')

add("matrix",'.matrix[data-el="glasspulse-matrix"]>.cell.on .list .name{color:var(--a1-on)}')

add('card','.card[data-el="glasspulse-card"] .name{align-items:flex-start}')

add('list','.list[data-el="glasspulse-list"]{list-style:none;margin:0}')

add('chart-donut','.donut[data-el="glasspulse-chart-donut"]>.name{max-width:min(58cqw,58cqh);line-height:var(--name-line)}')

add('timeline','.track[data-el="glasspulse-timeline"]:not(.alt):not(.col)>.stop{display:flex;flex-direction:column;gap:var(--gap-sm)} .track[data-el="glasspulse-timeline"]:not(.alt):not(.col)>.stop>.kick{display:block;line-height:var(--label-line)} .track[data-el="glasspulse-timeline"]:not(.alt):not(.col)>.stop>.name{display:block;line-height:var(--name-line)}')
