from pathlib import Path
import re
p=Path(__file__).parent;c=p/'crossrail'
h=(p/'reassembled/slide_10.html').read_text();rich=re.search(r'(<div class="steps[^>]*>.*)</div></div></section>',h)[1];rich=rich[:rich.rfind('</div>')+6]
# Extract the individual source steps, keeping all contract pieces and actual empty icon markup.
steps=re.findall(r'<div class="step">.*?</div>',rich)
for n in [3,4,5]:
 members=steps[:n]
 if n==5:members=steps+['<div class="step"><span class="mark">5 STEP</span><p class="name"><span class="icon" data-icon="check-check"></span>성과 확인</p><p class="note">고객에게 전달한 가치를 다시 살펴보고 다음 분기에 이어갈 개선 과제를 정리합니다.</p></div>']
 root='<div class="steps" data-el="crossrail-steps" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(members)+'</div>'
 (c/f'elements/steps/fixtures/rich-{n}.html').write_text('<!-- min: '+('10x5' if n==5 else '8x5')+' -->\n'+root+'\n')
s='[data-el="crossrail-steps"]:has(.name>.icon):not(.col)';f=c/'elements/steps/element.css';f.write_text(f.read_text()+f'\n{s} .note{{height:auto;min-height:89px;flex:1}}@container(max-width:850px){{{s} .name{{font-size:var(--type-22)}}{s} .note{{font-size:var(--type-16)}}}}@container(max-height:300px){{{s} .note{{min-height:0}}}}\n')
h=(p/'reassembled/slide_24.html').read_text();roots=re.findall(r'<div class="donut" data-el="crossrail-chart-donut".*?</div>',h)
roots=[re.sub('grid-column:7 / span 6;grid-row:1 / span 6','grid-column:1 / span 2;grid-row:1 / span 1',x) for x in roots]
(c/'elements/chart-donut/fixtures/composite-five.html').write_text('<!-- min: 6x5 -->\n<div class="split" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(roots)+'</div>\n')
h=(p/'reassembled/slide_24.html').read_text();legend=re.search(r'<div class="legend" data-el="crossrail-legend".*?</div>',h)[0];legend=re.sub('grid-column:1 / span 6;grid-row:1 / span 4','grid-column:1 / span 12;grid-row:1 / span 6',legend);(c/'elements/legend/fixtures/legend-values.html').write_text('<!-- min: 6x4 -->\n'+legend+'\n')
print('rich3/4/5, composite5, value-legend added; golden fixtures unchanged')
