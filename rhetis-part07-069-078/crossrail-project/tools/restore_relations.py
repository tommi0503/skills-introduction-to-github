from pathlib import Path
import re
p=Path(__file__).parent;c=p/'crossrail'
# Restore the semicircular value hub without changing its centre/member semantics.
f=p/'reassembled/slide_07.html';h=f.read_text().replace('grid-column:5 / span 4','grid-column:4 / span 6').replace('<b class="name">핵심 가치</b>','<b class="name">핵심 가치<small>Value</small></b>');f.write_text(h)
s='[data-el="crossrail-hub"]:has(>.spoke:nth-child(4 of .spoke):last-child):not(:has(.spoke .mark,.spoke .note))'
f=c/'elements/hub/element.css';css=f'''\n/* Equal values arranged on a semicircular arch. */
{s}::before{{inset:auto;left:50%;top:110px;width:388px;height:194px;transform:translateX(-50%);border:2px solid var(--n-3);border-bottom:0;border-radius:194px 194px 0 0}}
{s} .core{{left:50%;top:55%;width:200px;height:auto;aspect-ratio:auto;transform:translateX(-50%);border:0;background:transparent;justify-content:flex-start}}
{s} .core .name{{font-size:var(--type-26);font-weight:var(--name-weight);line-height:var(--name-line)}}{s} .core small{{display:block;font-size:var(--type-18);color:var(--n-5);font-weight:var(--name-weight);line-height:var(--label-line)}}
{s} .spoke{{left:calc(50% + cos(var(--crossrail-angle))*194px);top:calc(304px + sin(var(--crossrail-angle))*194px);width:86px;height:86px;min-height:86px;padding:0;background:var(--a1-7);border:6px solid var(--n-3);border-radius:50%;color:var(--page)}}{s} .spoke .name{{font-size:var(--type-18);color:inherit}}{s} .spoke::before{{display:none}}
'''
for i,a in enumerate([-150,-110,-70,-30],1):css+=f'{s} .spoke:nth-child({i} of .spoke){{--crossrail-angle:{a}deg}}'
f.write_text(f.read_text()+css+'\n')
# Full original strength copy and the five actual icon roles.
f=p/'reassembled/slide_18.html';h=f.read_text().replace('grid-column:5 / span 4','grid-column:4 / span 6')
h=h.replace('<b class="name">우리의 강점</b>','<b class="name">우리의 강점<small>Strength</small></b>')
old=re.search(r'(<div class="hub .*?data-el="crossrail-hub".*?)(</div><div class="group col" style="grid-column:9)',h)
if old:
 core=old[1][:old[1].index('<div class="spoke">')]
 sp=''.join('<div class="spoke"><span class="mark"></span><p class="name"><span class="icon" data-icon="'+ic+'" aria-label="'+nm+'"></span></p><p class="note"></p></div>' for ic,nm in [('globe','글로벌'),('chart-no-axes-combined','성장'),('handshake','파트너십'),('user-round','고객'),('cpu','기술')])
 h=h[:old.start()]+core+sp+h[old.start()+len(old[1]):]
h=h.replace('class="card quiet"','class="card quiet line"')
notes=['• 해당 페이지는 회사의 강점과 경쟁력을 적는 페이지입니다.<br>• 키워드를 적어보세요.','• 경쟁사와 차별화되는 우리 회사만의<br>• 독특한 서비스와 제품을 강조해 보세요.','• 실제 고객의 긍정적인 피드백이나<br>• 추천사를 인용해 신뢰도를 높여보세요.','• 높은 고객 유지율을 강조하며 회사의<br>• 네트워크가 견고함을 보여주세요.','• 회사의 미래 가능성을 보여줄 수 있는<br>• 장기적인 비전과 목표를 보여주세요.'];it=iter(notes)
h=re.sub(r'(<div class="parts"><p class="name">.*?</p>)<p class="note">.*?</p>',lambda m:m[1]+'<p class="note">'+next(it)+'</p>',h);f.write_text(h)
s='[data-el="crossrail-hub"]:has(>.spoke:nth-child(5 of .spoke):last-child):has(.spoke .name>.icon)'
f=c/'elements/hub/element.css';css=f'''\n/* A five-member strength hub retains the pentagonal perimeter. */
{s}::before{{inset:auto;left:50%;top:42px;width:310px;height:302px;transform:translateX(-50%);border:0;border-radius:0;background:var(--n-5);clip-path:polygon(50% 0,100% 38.2%,80.9% 100%,19.1% 100%,0 38.2%)}}
{s}::after{{content:"";position:absolute;left:50%;top:44px;width:306px;height:298px;transform:translateX(-50%);background:var(--n-1);clip-path:polygon(50% 0,100% 38.2%,80.9% 100%,19.1% 100%,0 38.2%)}}
{s} .core{{top:48%;left:50%;width:200px;height:auto;aspect-ratio:auto;border:0;background:transparent;transform:translateX(-50%);z-index:5}}
{s} .core .name{{font-size:var(--type-26);line-height:var(--name-line)}}{s} .core small{{display:block;font-size:var(--type-18);line-height:var(--label-line);color:var(--n-5)}}
{s} .spoke{{left:calc(50% + cos(var(--crossrail-angle))*155px);top:calc(209px + sin(var(--crossrail-angle))*167px);width:96px;height:96px;min-height:96px;padding:0;gap:0;background:var(--a1-7);border:6px solid var(--n-3);border-radius:50%;color:var(--page);z-index:4}}
{s} .spoke::before{{display:none}}{s} .spoke>.mark,{s} .spoke>.note{{width:0;height:0;min-height:0;margin:0;padding:0;border:0}}{s} .spoke>.name{{display:flex;align-items:center;justify-content:center;background:transparent}}{s} .spoke>.name>.icon{{width:42px;height:42px;color:var(--page)}}
'''
for i,a in enumerate([-90,-18,54,126,198],1):css+=f'{s} .spoke:nth-child({i} of .spoke){{--crossrail-angle:{a}deg}}'
f.write_text(f.read_text()+css+'\n')
# Side explanations follow the same framing and paragraph hierarchy as the source.
s='[data-el="crossrail-card"].quiet:not(:has(.mark,.kick,.fig))'
f=c/'elements/card/element.css';css=f'''\n{s}{{border:0;background:transparent}}{s} .parts{{padding:0;gap:var(--gap);justify-content:flex-start}}{s} .name{{box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;height:54px;min-height:54px;font-size:var(--type-26);border-block:1px solid var(--n-3);padding:0}}{s} .note{{font-size:var(--type-18);text-align:center;min-height:0;line-height:var(--body-line);padding-inline:calc(var(--gap-sm)*5/12)}}
:where(.group.col:first-child)>{s}{{width:calc(100% - var(--gap-lg) - var(--gap-sm)*2/3);align-self:flex-start}}:where(.group.col:last-child)>{s}{{width:calc(100% - var(--gap-lg) - var(--gap-sm)*2/3);align-self:flex-end}}
:where(.group.col)>{s}:last-child .parts{{justify-content:flex-end}}
{s}.line .parts{{justify-content:center}}{s}.line .name{{background:var(--n-1)}}{s}.line .note{{text-align:left}}
''';f.write_text(f.read_text()+css+'\n')
# The KPI centre is a separate contract hub, overlaid on four matrix cells.
f=p/'reassembled/slide_17.html';h=f.read_text();start=h.index('<div class="matrix ');h=h[:start]+h[start:].replace('<div class="matrix ','<div class="matrix ',1)
# Retain the matrix's required two pairs of axis labels without adding visible text absent from the source.
h=h.replace('grid-row:1 / span 6"><div class="cell on">','grid-row:1 / span 6"><div class="axis-x"><span></span><span></span></div><div class="axis-y"><span></span><span></span></div><div class="cell on">',1)
hub='<div class="hub" data-el="crossrail-hub" style="grid-column:4 / span 6;grid-row:1 / span 6"><div class="core"><b class="name">시장<br>매력도</b></div>'+''.join('<div class="spoke"><span class="mark"><span class="icon" data-icon="'+ic+'"></span></span><p class="name"></p><p class="note"></p></div>' for ic in ['search','goal','chart-column-decreasing','chart-pie'])+'</div>'
h=h.replace('</div></div></section>',hub+'</div></div></section>');f.write_text(h)
s='[data-el="crossrail-matrix"]:not(.swot)';f=c/'elements/matrix/element.css';f.write_text(f.read_text()+f'''\n{s}{{padding:0;gap:var(--pad)}}{s} .cell{{background:transparent;color:inherit;padding:var(--pad);justify-content:center}}{s} .cell.on{{background:var(--a1-5);border-color:var(--n-3)}}{s} .cell:nth-child(2 of .cell),{s} .cell:nth-child(4 of .cell){{align-items:flex-end;text-align:right}}{s} .name{{font-size:var(--type-26)}}{s} .note{{max-width:340px;font-size:var(--type-18)}}\n''')
s='[data-el="crossrail-hub"]:has(.core>.name>br)';f=c/'elements/hub/element.css';css=f'''\n{s}::before{{inset:auto;left:50%;top:50%;transform:translate(-50%,-50%);width:298px;height:298px;border:2px solid var(--n-3);border-radius:50%;background:transparent}}{s} .core{{left:50%;top:50%;width:160px;height:160px;border:0;background:var(--page);color:var(--ink)}}{s} .core .name{{font-size:var(--type-26);line-height:var(--name-line)}}{s} .spoke{{left:calc(50% + cos(var(--crossrail-angle))*126px);top:calc(50% + sin(var(--crossrail-angle))*105px);width:42px;height:42px;min-height:42px;padding:0;border:0;background:transparent;gap:0;z-index:3}}{s} .spoke::before{{display:none}}{s} .spoke .mark{{width:42px;height:42px;background:transparent;border:0}}{s} .spoke .icon{{width:34px;height:34px;color:var(--n-3)}}{s} .spoke .name,{s} .spoke .note{{margin:0;padding:0;min-height:0}}'''
for i,a in enumerate([-135,-45,135,45],1):css+=f'{s} .spoke:nth-child({i} of .spoke){{--crossrail-angle:{a}deg}}'
f.write_text(f.read_text()+css+'\n')
print('semicircle, pentagonal strength hub, KPI centre and complete side copy restored')
