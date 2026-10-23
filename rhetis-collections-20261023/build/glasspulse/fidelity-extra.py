from pathlib import Path
C=Path('/workspace/output/glasspulse')
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s)
r='.card[data-el="glasspulse-card"]:has(>.parts>.bars.h):has(>.parts>.bars.h>.bar:nth-child(2):last-child)'
add('card',r+'>.parts>.callout{top:calc(var(--gap)*11 - var(--stroke))}\n'+'''
.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas){height:min(100%,calc(var(--gap)*12 + var(--gap-sm) + var(--stroke)*2));padding:0;align-self:start;transform:translateY(calc(var(--gap)*-0.5))}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts{display:block;position:relative;height:100%}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.stat{position:absolute;left:var(--pad);top:var(--gap);width:50%;height:calc(var(--gap)*4);padding:0;border:0;background:none;z-index:1}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.stat .parts{align-items:flex-start;justify-content:flex-start;gap:var(--gap-sm)}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.stat .name{font-size:var(--type-26);text-align:left}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.stat .fig{font-size:var(--type-60);white-space:nowrap}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.areas{position:absolute;inset:var(--gap) var(--gap) var(--gap);width:calc(100% - var(--gap)*2);height:calc(100% - var(--gap)*2)}
''')
add('chart-bar','''
.bars.h[data-el="glasspulse-chart-bar"]:has(>.bar:nth-child(2):last-child)>.bar>b{font-weight:var(--body-weight);letter-spacing:var(--label-track);left:calc(var(--v)/var(--max)*100% + var(--gap) + var(--stroke))}.bars.h[data-el="glasspulse-chart-bar"]:has(>.bar:nth-child(2):last-child)>.bar.on>b{font-weight:var(--figure-weight);letter-spacing:calc(var(--figure-track)*1.5);left:calc(var(--v)/var(--max)*100% + var(--gap))}
''')
add('callout','''
.callout[data-el="glasspulse-callout"]:has(>p>b){border:0;background:none;box-shadow:none}.callout[data-el="glasspulse-callout"]:has(>p>b)>p{font-size:var(--type-32)}.callout[data-el="glasspulse-callout"]:has(>p>b)>p>b{font-size:var(--type-52)}
''')
