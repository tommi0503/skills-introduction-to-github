from pathlib import Path
P=Path(__file__).parent; E=P/'meridian-deck/elements'
f=E/'metric/element.css';f.write_text(f.read_text()+'''\n@container(max-height:110px){.stat[data-el="meridian-deck-metric"]>.parts{gap:calc(var(--gap-sm)/2)}.stat[data-el="meridian-deck-metric"] .fig{font-size:var(--type-28)}.stat[data-el="meridian-deck-metric"] .fig>small{font-size:var(--type-12)}.stat[data-el="meridian-deck-metric"] .name{font-size:var(--type-12)}.stat[data-el="meridian-deck-metric"] .note{display:none}}\n''')
f=E/'gauge/element.css';f.write_text(f.read_text()+'''\n@container(max-height:90px){.meter[data-el="meridian-deck-gauge"]>.name{font-size:var(--type-12)}.meter[data-el="meridian-deck-gauge"]>.fig{font-size:var(--type-18)}}\n''')
f=E/'radar/element.css';s=f.read_text().replace('background:color-mix(in oklab,var(--a1) 36%,transparent);clip-path:var(--meridian-deck-radar-shape);','background:none;')
s=s.replace('position:fixed;display:none','position:absolute;left:0;top:calc(var(--gap-lg)*-1);font-size:var(--type-12);line-height:var(--label-line);color:var(--n-7);font-weight:var(--name-weight);white-space:nowrap')
s+='''\n.radar[data-el="meridian-deck-radar"]>.series::before{content:"";position:absolute;inset:0;background:color-mix(in oklab,var(--a1) 36%,transparent);clip-path:var(--meridian-deck-radar-shape)}.radar[data-el="meridian-deck-radar"]>.series:nth-child(2 of .series),.radar[data-el="meridian-deck-radar"]>.series:nth-child(3 of .series){background:none}.radar[data-el="meridian-deck-radar"]>.series:nth-child(2 of .series)::before{background:color-mix(in oklab,var(--a2) 32%,transparent)}.radar[data-el="meridian-deck-radar"]>.series:nth-child(3 of .series)::before{background:color-mix(in oklab,var(--a3) 32%,transparent)}.radar[data-el="meridian-deck-radar"]>.series:nth-child(2 of .series)>.name{left:40%}.radar[data-el="meridian-deck-radar"]>.series:nth-child(3 of .series)>.name{left:80%}\n''';f.write_text(s)
f=E/'sankey/element.css';f.write_text(f.read_text()+'''\n.sankey[data-el="meridian-deck-sankey"]{display:flex;flex-direction:column;padding-left:40%}.sankey[data-el="meridian-deck-sankey"]>.branch{flex:var(--v);min-height:0;margin-left:0}.sankey[data-el="meridian-deck-sankey"]>.branch::before{width:25cqw}\n''')
f=E/'journey/element.css';s=f.read_text().replace('hypot(100%,calc((var(--mood) - var(--next))*.4cqh))','hypot(calc(100cqw / var(--meridian-deck-stages)),calc((var(--mood) - var(--next))*.4cqh))').replace('atan2(calc((var(--mood) - var(--next))*.4cqh),100%)','atan2(calc((var(--mood) - var(--next))*.4cqh),calc(100cqw / var(--meridian-deck-stages)))')
for n in range(3,8):s+=f'.journey[data-el="meridian-deck-journey"]:has(>.stage:nth-child({n}):last-child){{--meridian-deck-stages:{n}}}\n'
f.write_text(s)
f=E/'tag/fixtures/tag-labels.html';f.write_text('''<!-- min: 4x1 -->
<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6"><span class="tag" data-el="meridian-deck-tag">정밀 점검</span><span class="tag" data-el="meridian-deck-tag">담당자 검토 대기</span><span class="tag" data-el="meridian-deck-tag">운영 완료</span></div>
''')
f=E/'versus/fixtures/versus-long.html';s=(E/'versus/fixtures/versus.html').read_text() if (E/'versus/fixtures/versus.html').exists() else next((E/'versus/fixtures').glob('*.html')).read_text();s=s.replace('2055','수기 발주 단계').replace('2056','분산 창고 통합');f.write_text(s)
f=E/'pricing/fixtures/pricing-2.html';s=next((E/'pricing/fixtures').glob('*.html')).read_text();import re
# Two complete plans, preserving contractual parts and contrasting member counts.
start=s.index('<div class="plan"');a=s.index('<div class="plan on"',start);b=s.index('<div class="plan"',a);s=s[:b]+'</div>\n';s=s.replace('<!-- min: 8x4 -->','<!-- min: 6x4 -->').replace('베이직','현장 도입').replace('스탠다드','다중 거점 전환');f.write_text(s)
(E/'legend/fixtures/replica-11.html').write_text('''<!-- min: 3x1 -->
<div class="legend" data-el="meridian-deck-legend" style="grid-column:1 / span 12;grid-row:1 / span 6"><span class="key tone-1">입고량</span><span class="key tone-2">반출량</span></div>
''')
print('data refinements and missing basic specimens complete')
