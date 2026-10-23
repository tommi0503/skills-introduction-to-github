import re
from pathlib import Path
C=Path('/workspace/work/deliverables/confluence/collection/confluence')
def add(folder,text):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+text+'\n')
q='.card[data-el="confluence-card"]'
add('card',f'''{q} .parts{{display:flex;flex-direction:column;justify-content:center;align-self:auto;width:100%;height:auto;gap:var(--gap-sm)}}{q} .parts:has(.mark){{display:grid;grid-template-rows:80px 64px minmax(96px,auto);align-content:center;align-items:start}}{q} .parts:has(.fig){{display:grid;grid-template-rows:auto auto auto minmax(96px,auto);align-content:center}}{q} .parts:has(.kick):not(:has(.fig)){{display:grid;grid-template-rows:auto auto minmax(96px,auto);align-content:center}}{q} .parts>.name{{text-align:center;width:100%;border-bottom:var(--stroke) solid var(--n-2);padding-bottom:var(--gap-sm)}}{q} .parts>.kick{{width:100%;min-height:56px;display:flex;justify-content:center;align-items:center;flex:none;align-self:auto}}{q} .parts>.note{{width:100%;align-self:start}}@container (min-width:650px){{{q} .parts:has(.kick):not(:has(.fig)){{display:flex;flex-direction:row;align-items:center;gap:var(--gap)}}{q} .parts:has(.kick):not(:has(.fig)) .kick{{width:auto;max-width:34%;flex:1;min-height:64px}}{q} .parts:has(.kick):not(:has(.fig)) .name{{flex:2;width:auto;border:0;text-align:left;align-self:center}}{q} .parts:has(.kick):not(:has(.fig)) .note{{flex:2;width:auto;align-self:center}}}}@container (max-width:380px){{{q} .parts:has(.mark){{grid-template-rows:52px 48px minmax(64px,auto)}}{q} .parts:has(.fig){{grid-template-rows:auto auto auto minmax(64px,auto)}}{q} .parts:has(.kick):not(:has(.fig)){{grid-template-rows:auto auto minmax(64px,auto)}}{q} .parts>.kick{{font-size:var(--type-16);min-height:40px}}}}''')
q='.areas[data-el="confluence-chart-area"]'
add('chart-area',f'''{q} .series:nth-child(2) .pt::before{{background:var(--a2-3-soft)}}{q} .series:nth-child(2) .pt::after{{background:var(--a2)}}{q} .series:nth-child(3) .pt::before{{background:var(--a3-3-soft)}}{q} .series:nth-child(3) .pt::after{{background:var(--a3)}}@container (max-width:500px){{{q} .axis span:nth-child(even){{visibility:hidden}}}}''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.slide{position:absolute;left:0;top:0}\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.head.center{max-height:none;padding-top:calc(var(--gap-lg)*2)}.title b+b{color:var(--a2)}\n')
p=C/'kit/css/tokens.css';p.write_text(p.read_text().replace('--margin-y: 64px','--margin-y: 76px'))
q='.card[data-el="confluence-card"]'
add('card',f'''{q} .parts:has(.fig){{grid-template-rows:68px 44px 80px 1fr;height:100%;align-content:start;align-self:stretch}}{q} .parts:has(.fig)>.kick{{height:100%;min-height:0}}{q} .parts:has(.fig)>.name{{font-size:var(--type-20);border:0;align-self:end;color:var(--a1)}}{q} .parts:has(.fig)>.fig{{font-size:var(--type-52);align-self:center;color:var(--n-8)}}{q} .parts:has(.fig)>.fig:has(br){{font-size:var(--type-24)}}{q} .parts:has(.fig)>.note{{align-self:center}}{q} .note b{{font-size:var(--type-18);font-weight:var(--name-weight);color:var(--a1)}}@container (max-width:380px){{{q} .parts:has(.fig){{grid-template-rows:52px 32px 64px 1fr}}{q} .parts:has(.fig)>.fig{{font-size:var(--type-44)}}}}''')
q='.hub[data-el="confluence-hub"]'
add('hub',f'''{q} .spoke .name{{font-size:var(--type-40)}}{q} .core{{position:relative;padding:var(--gap);padding-top:calc(var(--gap-lg)*2)}}{q} .core>.seat{{position:absolute;top:calc(-1 * var(--gap-lg));left:50%;transform:translateX(-50%);width:130px;height:128px}}{q} .core .name{{font-size:var(--type-52)}}''')
for f in (C.parent.parent/'review/reassembled').glob('slide_*.html'):
 s=f.read_text().replace('<b>목차</b>보기','<b>목차</b><b>보기</b>').replace('<b>프로젝트</b><br>개요','<b>프로젝트</b><br><b>개요</b>')
 if f.stem=='slide_04':s=s.replace('<div class="core">','<div class="core"><div class="seat" data-ph="1"></div>')
 f.write_text(s)
# Readable text uses a deep accent slot; saturated rank colours remain fills and chart marks.
for p in [C/'foundation/foundation.css',*(C/'elements').glob('*/element.css')]:
 s=p.read_text();s=re.sub(r'(?<![-\w])color:\s*var\(--a([1-4])\)',lambda m:'color:var(--a'+m[1]+'-7)',s);s=s.replace('color:var(--n-6)','color:var(--n-7)');p.write_text(s)
q='.radar[data-el="confluence-radar"]'
add('radar',f'''{q}{{container-type:size}}{q} .series{{background:none;border:0;clip-path:none}}{q} .series::before{{content:"";position:absolute;inset:0;background:var(--a1-3-soft)}}{q} .series:nth-child(2 of .series)::before{{background:var(--a2-3-soft)}}{q} .series:nth-child(3 of .series)::before{{background:var(--a3-3-soft)}}{q} .series .name{{top:auto;bottom:calc(-1 * var(--gap));left:0;font-size:var(--type-14)}}{q} .series:nth-child(2 of .series) .name{{left:40%}}{q} .series:nth-child(3 of .series) .name{{left:75%}}''')
import math
for n in range(3,9):
 points=[]
 for i in range(n):
  x=math.sin(2*math.pi*i/n)*50;y=-math.cos(2*math.pi*i/n)*50
  points.append(f'calc(50% + var(--v{i+1})/var(--max)*{x:.6f}%) calc(50% + var(--v{i+1})/var(--max)*{y:.6f}%)')
 add('radar',f'{q}[style*="--n:{n}"] .series::before'+'{clip-path:polygon('+','.join(points)+')}')
q='.network[data-el="confluence-network"]'
add('network',f'''{q}{{container-type:size}}{q} .link{{width:hypot(calc((var(--x2) - var(--x1))*.84cqw),calc((var(--y2) - var(--y1))*.84cqh));transform:rotate(atan2(calc((var(--y2) - var(--y1))*.84cqh),calc((var(--x2) - var(--x1))*.84cqw)))}}''')
q='.treemap[data-el="confluence-treemap"]'
add('treemap',f'''{q}>.branch{{flex-wrap:nowrap;flex-direction:row;gap:2px}}{q} .tile{{min-width:0;min-height:0;padding:calc(var(--gap-sm)/4);overflow-wrap:anywhere}}{q} .tile .name{{font-size:var(--type-14)}}{q} .tile .fig{{font-size:var(--type-20)}}''')
q='.sankey[data-el="confluence-sankey"]';add('sankey',f'{q} .source'+'{align-self:stretch;align-content:center}')
q='.pyramid[data-el="confluence-pyramid"]';add('pyramid',f'{q} .level'+'{clip-path:polygon(10% 0,90% 0,100% 100%,0 100%)}')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.top .seat.logo{margin-left:auto;width:36px;height:36px}.head.center .title{position:relative}.head.center .title::before,.head.center .title::after{content:"";position:absolute;top:50%;width:35%;height:1px;background:var(--n-3)}.head.center .title::before{left:0}.head.center .title::after{right:0}.rail::after{content:"";position:absolute;top:0;right:calc(-1 * var(--gap-lg));height:568px;width:1px;background:var(--n-3)}\n')
q='.hub[data-el="confluence-hub"]'
add('hub',f'''{q}:has(>.spoke:nth-child(5):last-child){{grid-template-rows:repeat(2,minmax(0,1fr))}}{q}:has(>.spoke:nth-child(5):last-child) .core{{grid-row:1 / span 2}}{q}:has(>.spoke:nth-child(5):last-child) .spoke{{justify-content:flex-start;padding-top:var(--gap-sm)}}{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(4),{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(5){{grid-row:2;padding-top:var(--gap-lg)}}''')
f=C.parent.parent/'review/reassembled/slide_01.html';s=f.read_text().replace('<section class="slide cover">','<section class="slide cover"><div class="top"><div class="seat logo" data-ph="2"></div></div>');f.write_text(s)
p=C/'kit/css/tokens.css';s=p.read_text().replace('--title-line: 1.04','--title-line: 1.14');p.write_text(s)
p=C/'foundation/foundation.css';s=p.read_text().replace('.cover .title{font-size:var(--type-128);line-height:var(--figure-line)}','.cover .title{font-size:var(--type-128);line-height:var(--title-line)}');p.write_text(s)
# Minimum-slot repairs from round-one browser measurements.
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.body>.seat{width:auto;height:100%;max-width:100%;aspect-ratio:1;justify-self:center}\n')
q='.arch[data-el="confluence-architecture"]'
add('architecture',f'''{q} .layer{{padding:var(--gap-sm);gap:var(--gap-sm)}}{q} .chip{{font-size:var(--type-16);min-height:32px;padding:calc(var(--gap-sm)/2) var(--gap-sm)}}@container (max-width:650px){{{q} .layer{{padding:calc(var(--gap-sm)/2) var(--gap-sm);gap:calc(var(--gap-sm)/2)}}{q} .layer>.name{{font-size:var(--type-16);width:24%}}{q} .chip{{font-size:var(--type-12);min-height:24px;padding:calc(var(--gap-sm)/2)}}}}''')
q='.tablebox[data-el="confluence-table"]'
add('table',f'''@container (max-width:650px){{{q} table{{font-size:var(--type-14);table-layout:fixed}}{q} th,{q} td{{padding:calc(var(--gap-sm)/2);overflow-wrap:anywhere}}}}@container (max-width:380px){{{q} table{{font-size:var(--type-12)}}}}''')
q=':is(.bullet[data-el="confluence-bullet"],.bullets[data-el="confluence-bullet"])'
add('bullet',f'''{q}.bullets{{gap:var(--gap-sm);container-type:size}}{q}.bullet,{q} .bullet{{container-type:size;min-height:0;flex:1;padding:calc(var(--gap-sm)/3) 0 var(--gap-sm);gap:2px;border-bottom-width:8px}}{q} .name{{font-size:var(--type-18)}}{q} .fig{{font-size:var(--type-24)}}{q}.bullet::before,{q} .bullet::before{{bottom:-8px;height:6px}}{q}.bullet::after,{q} .bullet::after{{bottom:-8px;height:24px;left:min(100%,calc(var(--target)*1%))}}@container (max-height:110px){{{q} .note{{display:none}}}}''')
q='.steps[data-el="confluence-steps"]'
add('steps',f'''{q}{{gap:var(--gap)}}{q} .step{{padding:var(--gap-sm)}}{q} .step:not(:last-child)::after{{width:var(--gap)}}{q}.col{{gap:var(--gap)}}{q}.col .step{{display:grid;grid-template-columns:40px 1fr;grid-template-rows:auto auto;gap:calc(var(--gap-sm)/3) var(--gap-sm);text-align:left;padding:var(--gap-sm);align-items:center;min-height:0}}{q}.col .mark{{grid-row:1 / span 2;width:36px;height:36px}}{q}.col .note{{font-size:var(--type-14)}}{q}.col .step:not(:last-child)::after{{width:1px;height:var(--gap)}}@container (max-width:380px){{{q}.col .step{{padding:calc(var(--gap-sm)/2)}}{q}.col .name{{font-size:var(--type-16)}}{q}.col .note{{font-size:var(--type-12)}}}}''')
q='.funnel[data-el="confluence-funnel"]'
add('funnel',f'''{q} .stage{{padding:calc(var(--gap-sm)/2) var(--gap-sm);gap:var(--gap-sm)}}{q} .stage .name{{font-size:var(--type-18)}}{q} .stage .fig{{font-size:var(--type-24)}}@container (max-width:650px){{{q} .stage .name{{font-size:var(--type-14)}}{q} .stage .fig{{font-size:var(--type-20)}}}}''')
q='.hub[data-el="confluence-hub"]'
add('hub',f'''{q}:has(>.spoke:nth-child(7):last-child) .spoke .name{{font-size:var(--type-24)}}{q}:has(>.spoke:nth-child(7):last-child) .core .name{{font-size:var(--type-32)}}@container (max-width:650px){{{q} .core .name{{font-size:var(--type-24)}}{q} .spoke .name{{font-size:var(--type-24)}}{q} .spoke .note{{font-size:var(--type-12)}}{q} .spoke{{gap:calc(var(--gap-sm)/2)}}}}''')
q='.frame[data-el="confluence-image-frame"]';add('image-frame',f'{q} .seat'+'{max-width:100%;max-height:100%;width:auto;height:100%;aspect-ratio:1}')
p=C/'elements/chart-bar/fixtures/source-performance.html';p.write_text(p.read_text().replace(' report',''))
