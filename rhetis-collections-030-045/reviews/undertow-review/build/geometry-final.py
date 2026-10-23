from pathlib import Path
C=Path('work/deliverables/undertow/elements')
def add(n,s):p=C/n/'element.css';p.write_text(p.read_text()+'\n'+s)
add('hub','.hub[data-el="undertow-hub"]:has(> .spoke:nth-child(4 of .spoke):last-child) .core {grid-area:auto;}')
r='.org[data-el="undertow-hierarchy"]';add('hierarchy',r+' {grid-template-columns:repeat(var(--undertow-org-branches,3),minmax(0,1fr));} '+''.join(r+f':has(> .branch:nth-child({i} of .branch):last-child) {{ --undertow-org-branches:{i};}}' for i in range(2,5)))
for n in ['flowchart','swimlane']:
 r='.'+n+'[data-el="undertow-'+n+'"]';add(n,''.join(r+f':has(> .node[style*="grid-column:{i}"]),'+r+f':has(> .node[style*="grid-column: {i}"]) {{ --cols:{i};}}' for i in range(4,7)))
r='.journey[data-el="undertow-journey"]';add('journey',r+' .stage::after {--undertow-journey-dx:calc((100cqw + var(--gap-sm))/var(--undertow-journey-count));--undertow-journey-dy:calc((var(--mood) - var(--next,var(--mood)))*(100cqh - var(--gap-lg))*.005);width:hypot(var(--undertow-journey-dx),var(--undertow-journey-dy));transform:rotate(atan2(var(--undertow-journey-dy),var(--undertow-journey-dx)));z-index:2;} '+r+' .stage::before {z-index:3;} '+''.join(r+f':has(> .stage:nth-child({i} of .stage):last-child) {{ --undertow-journey-count:{i};}}' for i in range(3,8)))
r='.plan[data-el="undertow-pricing"]';add('pricing',r+' {display:grid;grid-template-rows:minmax(0,1fr) var(--type-40) var(--type-64) minmax(0,1fr);gap:var(--gap-sm);align-content:stretch;} '+r+' > .name {grid-row:2;align-self:center;} '+r+' > .price {grid-row:3;align-self:center;} '+r+' > .list {grid-row:4;align-self:start;}')
r='.card[data-el="undertow-card"]';add('card','@container (min-height:300px) {'+r+' .name {min-height:var(--type-64);display:flex;align-items:center;justify-content:center;} '+r+' .note {min-height:var(--type-80);} '+r+' .parts:has(.fig) {grid-template-rows:var(--type-16) var(--type-56) var(--type-64) var(--type-80);} }')
mandatory={'card','callout','chart-area','chart-bar','chart-donut','chart-line'}
for d in C.iterdir():
 if d.name in mandatory:continue
 for p in (d/'fixtures').glob('*.html'):
  s=p.read_text().replace('TEXT HERE 제품 경쟁력','핵심 제품 경쟁력').replace('TEXT HERE','사업 전환').replace('GRAPH DATA','선순환 가치').replace('MIRAE HOLDINGS','MIRI COMPANY')
  for i in range(1,10):s=s.replace('205'+str(i),'202'+str(i))
  if d.name=='quote':s=s.replace('<b class="name">사업 전환</b>','<b class="name">김미리 대표이사</b>')
  p.write_text(s)
p=C/'legend/fixtures/extended.html';p.write_text('''<!-- min: 4x1 -->
<div class="legend" data-el="undertow-legend" style="grid-column:1 / span 12;grid-row:1 / span 6"><span class="key tone-1">신규 고객 계약</span><span class="key tone-2">글로벌 파트너 매출</span><span class="key tone-5">그 밖의 운영 수익</span></div>''')
p=C/'card/fixtures/card.html';p.write_text(p.read_text().replace('<span class="icon">✹</span>','<span class="icon" data-icon="rocket"></span>'))
