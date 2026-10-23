from pathlib import Path
from bs4 import BeautifulSoup as B
import json,re
P=Path(__file__).parent;C=P/'crossrail';E=C/'elements'
def app(el,s):f=E/el/'element.css';f.write_text(f.read_text()+'\n'+s+'\n')
# No hard line may wrap once more inside the source's paragraph box.
app('prose','''[data-el="crossrail-prose"]:has(>p:first-child>b:only-child){max-width:none;width:100%}''')
app('headline','''[data-el="crossrail-headline"] .note{margin:0}[data-el="crossrail-headline"].quiet{margin-top:calc(var(--gap)*-1);height:calc(100% + var(--gap))}''')
app('list','''[data-el="crossrail-list"].check:not(:has(.note)){padding-top:calc(var(--gap-lg)*1.1)}''')
app('pill',''':where([data-el="crossrail-versus"] .side)>[data-el="crossrail-pill"]{width:auto;max-width:none;flex:none}''')
# Restore business-grid intersections and asymmetric inner gutters from the source.
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide .group.two:has(>[data-el="crossrail-card"].line .kick){gap:0}\n''')
s='[data-el="crossrail-card"].line:has(.parts>.kick):not(:has(.mark,.fig))'
app('card',s+'{transform:translateY(calc(var(--gap-sm)*-.25));border-bottom:1px solid var(--n-3)}'+s+' .parts{padding-right:var(--gap-lg)}'+s+':nth-child(even){border-left:1px solid var(--n-3)}'+s+':nth-child(even) .parts{padding-left:var(--gap-lg);padding-right:0}')
s='[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick)):not(:has(.fig>b))'
app('card',':where(.group:has(>[data-el="crossrail-card"]:nth-child(4):last-child))>'+s+':not(:last-child){margin-right:var(--gap)}'+s+'::after{right:calc(var(--gap-sm)*-1.5)}')
s='[data-el="crossrail-table"]:not(:has(thead)):not(:has(tr>td:nth-child(3))):has(tr:nth-child(6))'
app('table',s+' td:first-child{width:calc(var(--gap-lg)*6.325)}')
# Source23's plot caption is a separate contract legend; numeric values remain chart b.
f=P/'reassembled/slide_23.html';soup=B(f.read_text(),'html.parser');soup.select_one('.body').append(B('<div class="legend center" data-el="crossrail-legend" style="grid-column:1 / span 6;grid-row:6 / span 1"><span class="key"><em>고객 유입 수</em></span></div>','html.parser').find());f.write_text(str(soup))
app('legend','''[data-el="crossrail-legend"]:has(>.key>em){display:flex;justify-content:center;align-items:flex-start;padding-right:var(--gap);padding-top:calc(var(--gap-sm)*.5);height:var(--gap-lg);position:relative;z-index:4;color:var(--page)}[data-el="crossrail-legend"]>.key:has(>em)::before{display:none}[data-el="crossrail-legend"]>.key>em{font-size:var(--type-18);font-weight:var(--body-weight);font-style:normal}''')
# Smaller slots retain the rich structure instead of deleting icons or notes.
app('steps','''@container(max-height:380px){[data-el="crossrail-steps"]:has(.name>.icon):not(.col) .step{padding-top:var(--gap)}[data-el="crossrail-steps"]:has(.name>.icon):not(.col) .mark{height:calc(var(--gap-lg)*1.4);min-height:calc(var(--gap-lg)*1.4)}[data-el="crossrail-steps"]:has(.name>.icon):not(.col) .name{height:calc(var(--gap-lg)*2.4);grid-template-rows:calc(var(--gap-lg)*1.2) 1fr;gap:calc(var(--gap-sm)*5/6);margin-top:var(--gap-sm);font-size:var(--type-22)}[data-el="crossrail-steps"]:has(.name>.icon):not(.col) .name>.icon{width:calc(var(--gap-lg)*1.2);height:calc(var(--gap-lg)*1.2)}[data-el="crossrail-steps"]:has(.name>.icon):not(.col) .note{margin-top:var(--gap-sm);min-height:0;font-size:var(--type-16)}[data-el="crossrail-steps"].col:has(.mark>.icon){padding-top:var(--gap);gap:var(--gap-sm)}[data-el="crossrail-steps"].col:has(.mark>.icon) .step{height:calc(var(--gap-lg)*1.5);min-height:calc(var(--gap-lg)*1.5)}[data-el="crossrail-steps"].col:has(.mark>.icon) .mark,[data-el="crossrail-steps"].col:has(.mark>.icon) .name{height:calc(var(--gap-lg)*1.5);min-height:0}[data-el="crossrail-steps"].col:has(.mark>.icon) .mark>.icon{width:calc(var(--gap-lg)*1.35);height:calc(var(--gap-lg)*1.35);padding:var(--gap-sm)}[data-el="crossrail-steps"].col:has(.mark>.icon) .note{font-size:var(--type-16)}}''')
app('hub','''@container(max-height:380px){[data-el="crossrail-hub"]:has(.spoke .name>.icon)::before{top:calc(var(--gap-lg)*.5);width:calc(var(--gap-lg)*6.25);height:calc(var(--gap-lg)*6.1)}[data-el="crossrail-hub"]:has(.spoke .name>.icon)::after{top:calc(var(--gap-lg)*.55);width:calc(var(--gap-lg)*6.15);height:calc(var(--gap-lg)*6)}[data-el="crossrail-hub"]:has(.spoke .name>.icon) .spoke{left:calc(50% + cos(var(--crossrail-angle))*var(--gap-lg)*3.125);top:calc(50% + sin(var(--crossrail-angle))*var(--gap-lg)*3.125);width:calc(var(--gap-lg)*1.8);height:calc(var(--gap-lg)*1.8);min-height:0}[data-el="crossrail-hub"]:has(.spoke .name>.icon) .spoke>.name>.icon{width:var(--gap);height:var(--gap)}}''')
# Add source structures as reviewable fixtures, leaving all golden fixtures byte-equivalent.
items=[('hub',7,'hub-semicircle',8,5),('hub',17,'hub-matrix-overlay',8,5),('hub',18,'hub-pentagon',8,5),('steps',13,'steps-icon-column',10,5),('steps',14,'steps-reverse',8,4),('card',12,'card-letter-columns',8,5),('card',22,'card-score-panel',6,3),('roadmap',26,'roadmap-split-lane',10,5),('timeline',28,'timeline-four-bands',10,6),('table',27,'table-calendar',8,6),('image-frame',15,'image-circle',4,3),('pill',27,'pill-two-line',4,2),('chart-bar',23,'bars-annotated',12,6),('legend',22,'legend-numeric-axis',6,5),('legend',22,'legend-chart-caption',4,2)]
for el,n,name,w,h in items:
 s=B((P/f'reassembled/slide_{n:02}.html').read_text(),'html.parser');rs=s.select(f'[data-el="crossrail-{el}"]');r=rs[-1] if name=='legend-chart-caption' else rs[0]
 if name=='card-letter-columns':r=s.select_one('.body>.group')
 # Copies are data-driven source structures; numeric geometry must survive the fixture.
 r['style']=';'.join(x for x in r.get('style','').split(';') if x and not x.startswith(('grid-column:','grid-row:')))
 if not r['style']:del r['style']
 d=E/el/'fixtures';(d/f'{name}.html').write_text(f'<!-- min:{w}x{h} max:12x6 -->\n'+str(r)+'\n')
# Composite chart keeps all external labels within its dedicated full-slide review cell.
f=E/'chart-donut/fixtures/composite-five.html';h=f.read_text();h=re.sub(r'min:\d+x\d+','min:12x6',h);f.write_text(h)
