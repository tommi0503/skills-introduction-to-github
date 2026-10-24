from pathlib import Path
import json,re
P=Path(__file__).parent;E=P/'crossrail/elements'
def edit(leaf,fn):
 p=E/leaf/'element.css';p.write_text(fn(p.read_text()))
def minf(leaf,fn,minimum):
 p=E/leaf/'fixtures'/fn;p.write_text(re.sub(r'<!-- min:[^>]*-->',f'<!-- min:{minimum} -->',p.read_text()))
# Exact connected semicircle coordinates; optional long notes take a separate lower row.
edit('hub',lambda s:s.replace('bottom:4%;transform:translateX(-50%)','bottom:20%;transform:translateX(-50%)')+' .hub[data-el="crossrail-hub"]:not(:has(>.spoke>.note))::before{bottom:3%} .hub[data-el="crossrail-hub"]:not(:has(>.spoke>.note))>.spoke{top:calc(97% + sin(var(--crossrail-spoke-angle))*var(--crossrail-hub-radius))} .hub[data-el="crossrail-hub"]:not(:has(>.spoke>.note))>.core{bottom:15%}'+''.join(f' .hub[data-el="crossrail-hub"]:has(>.spoke:nth-child(4 of .spoke):last-child)>.spoke:nth-child({i+1} of .spoke){{--crossrail-spoke-angle:{a}deg}}' for i,a in enumerate([-150,-110,-70,-30])))
edit('pyramid',lambda s:s.replace('background:var(--a1-6)','background:var(--a1-8)'))
edit('funnel',lambda s:s.replace('background:var(--a1-6)','background:var(--a1-8)'))
edit('pill',lambda s:s+' @container(max-width:900px){.pill[data-el="crossrail-pill"] .name{font-size:var(--type-20)}.pill[data-el="crossrail-pill"] .note{font-size:var(--type-14)}} @container(max-width:600px){.pill[data-el="crossrail-pill"] .note{display:none}}')
edit('card',lambda s:s+' @container(max-width:380px){.card[data-el="crossrail-card"]:not(.quiet):not(.line):not(.on) .name{left:7.8cqw;right:7.8cqw;top:34cqh;width:auto;text-align:left}.card[data-el="crossrail-card"]:not(.quiet):not(.line):not(.on) .parts::before{top:55cqh}.card[data-el="crossrail-card"]:not(.quiet):not(.line):not(.on) .note{top:61cqh}.card[data-el="crossrail-card"]:not(.quiet):not(.line):not(.on) .fig{top:12cqh}.card[data-el="crossrail-card"] .name{font-size:var(--type-20)}} @container(max-width:200px){.card[data-el="crossrail-card"] .name{font-size:var(--type-16)}.card[data-el="crossrail-card"] .note{font-size:var(--type-14)}.card[data-el="crossrail-card"] .fig{font-size:var(--type-28)}}')
minf('card','base-a.html','12x4');minf('card','base-b.html','9x4')
edit('gauge',lambda s:s.replace('padding:var(--pad)','padding:var(--gap-sm)').replace('left:var(--pad)','left:var(--gap-sm)').replace('bottom:var(--pad)','bottom:var(--gap-sm)').replace('right:var(--pad)','right:var(--gap-sm)').replace('var(--pad)*2','var(--gap-sm)*2')+' @container(max-height:120px){.meter[data-el="crossrail-gauge"] .name{font-size:var(--type-18)}.meter[data-el="crossrail-gauge"] .fig{font-size:var(--type-24)}}')
edit('chart-line',lambda s:s.replace('padding:calc(var(--gap-sm)*1.5)','padding:var(--gap-lg)'))
edit('chart-bar',lambda s:s.replace('padding:var(--gap-lg) var(--pad)','padding:calc(var(--pad)*2) var(--pad)').replace('inset:var(--gap-lg) var(--pad)','inset:calc(var(--pad)*2) var(--pad)'))
edit('headline',lambda s:s+' @container(max-height:120px){.headline[data-el="crossrail-headline"] .kick{display:none}.headline[data-el="crossrail-headline"] h2{font-size:var(--type-20)}.headline[data-el="crossrail-headline"] .note{font-size:var(--type-14);margin-top:calc(var(--gap-sm)/2)}}')
# Inline highlights need a line box inside a grid canvas, not a raw inline glyph at the slot top edge.
edit('tag',lambda s:s.replace('display:inline;color:var(--ink);font-size','display:flex;align-items:center;justify-content:center;color:var(--ink);font-size').replace('background:linear-gradient(transparent 60%,var(--a1-2-soft) 0)','background:none')+' .hl[data-el="crossrail-tag"]>span{background:linear-gradient(transparent 60%,var(--a1-2-soft) 0)}')
# Keep the single-letter SWOT semantics. Text decoration must still have readable contrast.
p=E/'matrix/fixtures/base-b.html';s=p.read_text();k=iter('SWOT');s=re.sub(r'(<b class="kick">).*?(</b>)',lambda m:m[1]+next(k)+m[2],s);p.write_text(s)
edit('matrix',lambda s:s.replace('color:var(--n-4)','color:var(--n-7)')+' .matrix[data-el="crossrail-matrix"].swot .cell.on .kick{color:inherit} @container(max-width:750px){.matrix[data-el="crossrail-matrix"].swot .kick{font-size:var(--type-40)}.matrix[data-el="crossrail-matrix"].swot .list{font-size:var(--type-14)}}')
# Guard the smallest full-height tile rows, without suppressing labels.
minf('matrix-nine','base-b.html','10x6');minf('matrix-nine','base-a.html','9x6')
minf('timeline','base-a.html','10x6')
minf('journey','base-a.html','8x6');minf('journey','base-b.html','12x6')
edit('journey',lambda s:s.replace('top:86cqh','top:84cqh'))
# Square unit arrays must budget the parent flex member's height, and small copy has its own line.
edit('waffle',lambda s:s.replace('gap:var(--gap-sm) var(--gap);align-items:center','gap:var(--gap-sm) var(--gap);padding:var(--gap-sm);align-items:center').replace('60cqw -','56cqw -').replace('grid-template-columns:60% 1fr','grid-template-columns:56% minmax(0,1fr)')+' .waffle[data-el="crossrail-waffle"] .name small{display:block;font-size:var(--type-14);line-height:var(--body-line);margin-top:calc(var(--gap-sm)/2);color:inherit} @container(max-height:140px){.waffle[data-el="crossrail-waffle"] .fig{font-size:var(--type-24)}.waffle[data-el="crossrail-waffle"] .name{font-size:var(--type-14)}.waffle[data-el="crossrail-waffle"] .name small{font-size:var(--type-12)}}')
minf('waffle','base-b.html','6x3')
# Counted rows centre their text block instead of overflowing the top and bottom of a fixed item.
edit('list',lambda s:s+' @container(max-height:350px){.list[data-el="crossrail-list"] .name{font-size:var(--type-18)}.list[data-el="crossrail-list"] .note{font-size:var(--type-14)}}')
minf('list','base-b.html','6x4');minf('list','base-a.html','5x4')
edit('agenda',lambda s:s.replace('align-content:start','align-content:center')+' @container(max-width:650px){.agenda[data-el="crossrail-agenda"] .name,.agenda[data-el="crossrail-agenda"] .mark{font-size:var(--type-24)}.agenda[data-el="crossrail-agenda"] .note{font-size:var(--type-14)}}')
# Hierarchy padding is a fraction of its own height, not the width-based CSS padding percentage.
edit('hierarchy',lambda s:s.replace('padding-top:25%','padding-top:var(--gap-lg)'))
# Concentric bands have limited radial height; step down when that height is short.
edit('concentric',lambda s:s+' @container(max-height:450px){.orbit[data-el="crossrail-concentric"] .ring .name{font-size:var(--type-12)}.orbit[data-el="crossrail-concentric"] .ring .fig{font-size:var(--type-16)}}')
# A six-node cycle keeps optional notes outside the node disk in a separate lower row.
minf('cycle','base-a.html','6x6');minf('cycle','base-b.html','10x6')
# Nested Sankey destinations reserve enough height for the smallest actual 15% share.
edit('sankey',lambda s:s.replace('>.branch>.branch:first-child','>.branch>.branch:nth-child(1 of .branch)')+' .sankey[data-el="crossrail-sankey"] .branch>.branch>.name{font-size:var(--type-12)}.sankey[data-el="crossrail-sankey"] .branch>.branch>.fig{font-size:var(--type-14);margin:0;line-height:var(--body-line)}')
minf('sankey','base-b.html','10x6');minf('sankey','base-a.html','8x4')
# A compact series legend carries close numeric values without moving the actual polyline.
p=E/'slope/element.css';s=p.read_text();s=s.replace('left:30%;right:10%;top:20%;bottom:20%','left:42%;right:8%;top:20%;bottom:20%');s=s.replace('left:0;top:calc(20% + 60%*(1 - var(--a)/var(--max)));transform:translateY(-50%);width:22%','left:0;top:calc(20% + var(--crossrail-pair-index)*60%/var(--crossrail-pair-count));transform:none;width:17%')
s=s.replace('left:30%;top:calc(20% + 60%*(1 - var(--a)/var(--max)));transform:translate(-50%,-50%)','left:20%;top:calc(20% + var(--crossrail-pair-index)*60%/var(--crossrail-pair-count));transform:none')
s=s.replace('left:90%;top:calc(20% + 60%*(1 - var(--b)/var(--max)))','left:30%;top:calc(20% + var(--crossrail-pair-index)*60%/var(--crossrail-pair-count))')
s=s.replace('color:var(--n-5)}','color:var(--a2-7)}',1)
for i,c in enumerate(['a1-7','a2-7','a3-7','a4-7','n-7','a2-8','a3-8','a4-8'],1):s+=f' .slope[data-el="crossrail-slope"] .pair:nth-child({i} of .pair){{color:var(--{c})}}'
s+=' .slope[data-el="crossrail-slope"] .pair>.name{border-left:2px solid currentColor;padding-left:calc(var(--gap-sm)/2)} .slope[data-el="crossrail-slope"].dumbbell .pair>.name{border:0;padding:0} .slope[data-el="crossrail-slope"].dumbbell .pair>.a{transform:translate(-50%,-120%)} .slope[data-el="crossrail-slope"].dumbbell .pair>.b{transform:translate(-50%,20%)}'
p.write_text(s)
