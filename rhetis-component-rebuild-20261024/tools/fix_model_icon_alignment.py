"""Keep mandated card-4 markup/data; centre its existing icon glyph within the 55–56% icon box."""
from pathlib import Path
B=Path('/workspace/work/rebuild-20261024')
for n in ['inflexion','diecut','dockside','confluence']:
 p=B/n/'collection'/n/'elements/card/element.css';rule='\n/* The required model icon remains unchanged, centered inside its allotted icon box. */\n.card[data-el="'+n+'-card"]>.parts>.mark>.icon{display:grid;place-items:center;line-height:var(--label-line)}\n';s=p.read_text()
 if rule not in s:p.write_text(s+rule)
 print(n,'model icon alignment')
