from pathlib import Path
P=Path(__file__).parent/'meridian-deck/elements'
f=P/'card/element.css';s=f.read_text();a=s.index('.card[data-el="meridian-deck-card"]:not(:has(>.parts>.mark))>.parts:has(>.note>[data-el])');b=s.index('}}',a)+2;block=s[a:b].replace(':has(>.note>[data-el])',':has(>.note>p):has(>.note>[data-el])');s=s[:a]+block+s[b:];s+='''\n@container(max-height:200px){.card[data-el="meridian-deck-card"].line>.parts:has(>.kick)>.name:not(:empty)+.note{top:70%}}\n''';f.write_text(s)
f=P/'chart-area/element.css';f.write_text(f.read_text()+'''\n.areas.stacked[data-el="meridian-deck-chart-area"]>.series>.pt:not(:nth-child(1 of .pt))::before{opacity:1}\n''')
f=P/'chart-bar/element.css';f.write_text(f.read_text()+'''\n.bars[data-el="meridian-deck-chart-bar"]{border:0}\n''')
