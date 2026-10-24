from pathlib import Path
import json,re
P=Path(__file__).parent;E=P/'crossrail/elements'
h='.hub[data-el="crossrail-hub"]'
s=f'''{h}{{box-sizing:border-box;container-type:size;position:relative;isolation:isolate;min-width:0;min-height:0;font-family:var(--font-body);font-size:var(--type-18);color:var(--ink);line-height:var(--body-line)}}
{h}>.core{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(24cqw,32cqh);height:min(24cqw,32cqh);border:1px solid var(--n-3);border-radius:50%;background:var(--page);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;z-index:2}}
{h}>.core>.name{{font-size:var(--type-24);line-height:var(--name-line);font-weight:var(--name-weight)}}{h}>.core>.icon{{width:35%;height:35%}}
{h}>.spoke{{position:absolute;left:var(--crossrail-spoke-x);top:var(--crossrail-spoke-y);transform:translate(-50%,-50%);width:29%;height:29%;display:grid;grid-template-columns:var(--type-24) minmax(0,1fr);align-content:center;gap:calc(var(--gap-sm)/2);background:var(--page);box-sizing:border-box}}
{h}>.spoke::before{{content:"";position:absolute;left:50%;top:50%;width:hypot(calc(50cqw - var(--crossrail-spoke-x)),calc(50cqh - var(--crossrail-spoke-y)));height:1px;background:var(--n-4);transform-origin:0 50%;transform:rotate(atan2(calc(50cqh - var(--crossrail-spoke-y)),calc(50cqw - var(--crossrail-spoke-x))));z-index:-1}}
{h}>.spoke>.mark{{width:var(--type-24);height:var(--type-24);border:1px solid var(--n-3);border-radius:50%;display:flex;align-items:center;justify-content:center}}{h}>.spoke>.mark>.icon{{width:70%;height:70%}}
{h}>.spoke>.name{{margin:0;align-self:center;font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line)}}{h}>.spoke>.note{{margin:0;grid-column:1/-1;font-size:var(--type-14);line-height:var(--body-line);color:var(--n-7)}}
@container(max-width:650px){{{h}>.core>.name{{font-size:var(--type-18)}}{h}>.spoke>.name{{font-size:var(--type-16)}}{h}>.spoke>.note{{font-size:var(--type-12)}}}}
'''
for n in range(3,7):
 left=(n+1)//2;right=n-left
 for k in range(n):
  side=0 if k<left else 1;idx=k if not side else k-left;count=left if not side else right
  y=50 if count==1 else 18+idx*64/(count-1)
  s+=f'{h}:has(>.spoke:nth-child({n} of .spoke):last-child)>.spoke:nth-child({k+1} of .spoke){{--crossrail-spoke-x:{15 if not side else 85}cqw;--crossrail-spoke-y:{y:g}cqh}}\n'
(E/'hub/element.css').write_text(s)
from lxml import html,etree
for f in (E/'hub/fixtures').glob('*.html'):
 d=html.fromstring(f.read_text());sp=d.xpath('./div[@class="spoke"]')
 for j,a in enumerate(sp):
  mark=etree.Element('span',{'class':'mark'});etree.SubElement(mark,'span',{'class':'icon','data-icon':'package-check'});a.insert(0,mark)
  a.xpath('./p[@class="note"]')[0].text=['입고 순번을 확인한 뒤 담당 선반에 둡니다.','반출 요청 건은 운송장별로 모아 둡니다.','봉인 상태를 살펴 파손 건만 따로 맡깁니다.','담당 기사가 출발 전에 수량을 대조합니다.','보관 기한이 지난 물품은 별도로 알립니다.','회수 차량의 도착 시각을 배차표에 씁니다.'][j]
 f.write_text(f'<!-- min:{"6x4" if len(sp)==3 else "10x6"} -->\n'+etree.tostring(d,encoding='unicode',method='html')+'\n')
m=json.loads((E/'hub/element.json').read_text());m['description']='Radial peer fields linked by fine spokes to a central circular core.';(E/'hub/element.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
v='.venn[data-el="crossrail-venn"]';D='min(58cqw,76cqh)';D3='min(51cqw,60cqh)'
s=f'''{v}{{box-sizing:border-box;container-type:size;position:relative;isolation:isolate;min-width:0;min-height:0;font-family:var(--font-body);font-size:var(--type-18);color:var(--ink);line-height:var(--body-line)}}
{v}>.set{{position:absolute;left:calc(50% - .77*{D});top:calc(50% - .5*{D});width:{D};height:{D};border:1px solid var(--a1-7);border-radius:50%;box-sizing:border-box}}
{v}>.set::before{{content:"";position:absolute;inset:0;border-radius:50%;background:color-mix(in srgb,var(--a1-7) 10%,transparent)}}
{v}>.set:nth-child(2 of .set){{left:calc(50% - .23*{D});border-color:var(--n-5)}}{v}>.set:nth-child(2 of .set)::before{{background:color-mix(in srgb,var(--n-5) 10%,transparent)}}
{v}>.set.on{{border-width:2px}}{v}>.set>.name{{position:absolute;left:12%;right:55%;top:43%;margin:0;text-align:center;font-size:clamp(var(--type-14),min(2cqw,6cqh),var(--type-22));font-weight:var(--name-weight);line-height:var(--name-line);z-index:2}}
{v}>.set:nth-child(2 of .set)>.name{{left:55%;right:12%}}{v}>.core{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:18%;font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line);text-align:center;z-index:3}}
{v}:has(>.set:nth-child(3 of .set))>.set{{width:{D3};height:{D3};left:calc(50% - .75*{D3});top:calc(50% - .7*{D3})}}
{v}:has(>.set:nth-child(3 of .set))>.set:nth-child(2 of .set){{left:calc(50% - .25*{D3})}}
{v}:has(>.set:nth-child(3 of .set))>.set:nth-child(3 of .set){{left:calc(50% - .5*{D3});top:calc(50% - .22*{D3});border-color:var(--a2-7)}}
{v}:has(>.set:nth-child(3 of .set))>.set:nth-child(3 of .set)::before{{background:color-mix(in srgb,var(--a2-7) 10%,transparent)}}
{v}:has(>.set:nth-child(3 of .set))>.set>.name{{top:22%}}{v}:has(>.set:nth-child(3 of .set))>.set:nth-child(3 of .set)>.name{{left:25%;right:25%;top:70%}}
@container(max-width:650px){{{v}>.core{{font-size:var(--type-14)}}}}
''';(E/'venn/element.css').write_text(s)
# Fixed shared rows preserve every plan name and price baseline, including optional recommendation tags.
p=E/'pricing/element.css';s=p.read_text();s+= '''\n.plans[data-el="crossrail-pricing"]{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:var(--pad) 0 0 calc(var(--type-26)*var(--name-line)) var(--gap-sm) calc(var(--type-64)*var(--figure-line) + var(--gap-sm) + 1px) var(--gap-sm) minmax(0,1fr) var(--pad);column-gap:var(--gap-sm);row-gap:0;align-items:stretch}
.plans[data-el="crossrail-pricing"]:has(>.plan>.tag){grid-template-rows:var(--pad) var(--gap-lg) var(--gap-sm) calc(var(--type-26)*var(--name-line)) var(--gap-sm) calc(var(--type-64)*var(--figure-line) + var(--gap-sm) + 1px) var(--gap-sm) minmax(0,1fr) var(--pad)}
.plans[data-el="crossrail-pricing"]>.plan{display:grid;grid-row:1/-1;grid-template-rows:subgrid;row-gap:0;padding:0 var(--pad);justify-content:initial}.plans[data-el="crossrail-pricing"]>.plan>.tag{grid-row:2;align-self:start}.plans[data-el="crossrail-pricing"]>.plan>.name{grid-row:4;align-self:start}.plans[data-el="crossrail-pricing"]>.plan>.price{grid-row:6;align-self:stretch}.plans[data-el="crossrail-pricing"]>.plan>.list{grid-row:8;align-self:stretch}
''';p.write_text(s)
# Standard slope value pills use the same endpoint equations as their lines; dumbbell geometry is left intact.
p=E/'slope/element.css';s=p.read_text();s+='''\n.slope[data-el="crossrail-slope"]:not(.dumbbell)>.heads{left:42%;right:8%}.slope[data-el="crossrail-slope"]:not(.dumbbell)>.pair>.a{left:42%;top:calc(20% + 60%*(1 - var(--a)/var(--max)));transform:translate(-100%,-50%)}.slope[data-el="crossrail-slope"]:not(.dumbbell)>.pair>.b{left:92%;top:calc(20% + 60%*(1 - var(--b)/var(--max)));transform:translate(0,-50%)}
''';p.write_text(s)
# One radial spoke for every contracted radar axis, using the same count-derived angles as its label.
p=E/'radar/element.css';s=p.read_text();s+='''\n.radar[data-el="crossrail-radar"]>.axis{position:static;transform:none;width:auto}.radar[data-el="crossrail-radar"]>.axis::before{content:"";position:absolute;left:50%;top:54%;width:min(34cqw,34cqh);height:1px;transform-origin:0 50%;transform:rotate(calc(var(--crossrail-axis-angle) - 90deg));background:var(--n-3);z-index:-1}.radar[data-el="crossrail-radar"]>.axis>.name{position:absolute;left:calc(50% + sin(var(--crossrail-axis-angle))*min(43cqw,43cqh));top:calc(54% - cos(var(--crossrail-axis-angle))*min(43cqw,43cqh));transform:translate(-50%,-50%);width:22%;text-align:center}
''';p.write_text(s)
m=json.loads((P/'map.json').read_text());m['roles']={'page':'--page: broad unframed canvas and negative space','primary-ink':'--ink: titles, numeric data and primary labels','structural-rail':'--a1-7: continuous navy-equivalent rail, chevrons and selected faces','secondary-accent':'--a2-7: contrasting secondary comparison series and markers','neutral-surface':'--n-1: pale inset tables and restrained neutral panels','rule':'--n-3: fine intersecting furniture rules and chart grids','secondary-copy':'--n-7: readable paragraph and quiet labels','series':'--a1-7 / --a2-7 / --a3-7 / --a4-7: data order, not fixed source hues','inverse-copy':'--page on --a1-7: text on structural dark panels'};(P/'map.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print('seven authorized leaves and roles updated')
