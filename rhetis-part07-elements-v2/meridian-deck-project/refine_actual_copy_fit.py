from pathlib import Path
E=Path(__file__).parent/'meridian-deck/elements'
def add(l,s):
 p=E/l/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('hub','.hub[data-el="meridian-deck-hub"]:not(:has(>.spoke:nth-child(4 of .spoke)))>.spoke>.note{font-size:clamp(var(--type-12),1.3cqw,var(--type-14))}')
add('list','.list[data-el="meridian-deck-list"]:not(.check):not(.num):not(.divided)>.item>.name{font-weight:var(--body-weight)}')
add('legend','@container(max-width:250px){.legend[data-el="meridian-deck-legend"]>.key{font-size:var(--type-10);font-weight:var(--body-weight);white-space:nowrap;gap:calc(var(--gap-sm)/2);padding:0}}')
