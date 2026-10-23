from pathlib import Path
from bs4 import BeautifulSoup
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
changes={
'card': [(' .never',' .never'),('.card[data-el="dockside-card"].quiet:has(.kick):not(:has(.mark)):not(:has(.fig))','.card[data-el="dockside-card"].quiet:has(.kick):not(:has(.mark)):not(:has(.fig)):not(:has(.name))')],
'concentric':[('.orbit[data-el="dockside-concentric"]:has(>.ring:nth-child(2):last-child)','.orbit[data-el="dockside-concentric"]:has(>.ring:nth-child(2):last-child):has(.seat)')],
'person':[('.people[data-el="dockside-person"]:has(>.person:nth-child(3):last-child)','.people[data-el="dockside-person"]:has(>.person:nth-child(3):last-child):has(.list)')],
'hub':[('.hub[data-el="dockside-hub"]:has(>.spoke:nth-child(5):last-child)','.hub[data-el="dockside-hub"]:has(>.spoke:nth-child(5):last-child):has(>.core>.seat)'),('.hub[data-el="dockside-hub"]:has(>.spoke:nth-child(6):last-child)','.hub[data-el="dockside-hub"]:has(>.spoke:nth-child(6):last-child):has(>.core>.seat)')],
'list':[('.list[data-el="dockside-list"].check:has(>.item:nth-child(4):last-child):not(:has(.note))','.list[data-el="dockside-list"].check.divided:has(>.item:nth-child(4):last-child):not(:has(.note))')]
}
for f,pairs in changes.items():
 p=C/f'elements/{f}/element.css';s=p.read_text()
 for a,b in pairs:s=s.replace(a,b)
 p.write_text(s)
p=V/'reassembled/slide_13.html';b=BeautifulSoup(p.read_text(),'html.parser');q=b.select_one('.list.check');q['class']=['list','check','divided'];p.write_text(str(b))
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'\n.slide::before{display:none}\n')
for p in C.rglob('*.css'):shutil.copyfile(p,V/'assets/collection'/p.relative_to(C))
