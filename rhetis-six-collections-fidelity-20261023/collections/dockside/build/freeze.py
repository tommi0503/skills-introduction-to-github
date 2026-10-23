from pathlib import Path
import json,shutil
from bs4 import BeautifulSoup
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
for f in ['matrix','code','chart-donut']:
 p=C/f'elements/{f}/element.css';s=p.read_text()
 r='[data-el="dockside-'+f+'"]'
 if f=='matrix':s+=f'\n{r} .cell.on .note{{color:var(--a1-on)}}\n'
 if f=='code':s+=f'\n{r} .c{{color:var(--n-7)}}\n'
 if f=='chart-donut':s+=f'\n{r} .fig,{r} .name{{background:var(--page);color:var(--ink);border-radius:var(--radius-sm)}}\n'
 p.write_text(s)
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.slide:not(:has(.rail)) .page{padding-left:var(--margin-x)}\n')
for n in [2,3]:
 p=V/f'reassembled/slide_{n:02}.html';b=BeautifulSoup(p.read_text(),'html.parser');b.select_one('.rail').decompose();b.select_one('.head')['class'].append('center')
 if n==2:b.select_one('.kicker').decompose()
 else:b.select_one('.kicker').string='Index'
 p.write_text(str(b))
# Exact source CSS snapshot: this is copied library CSS, not a second authored design.
out=V/'assets/collection';out.mkdir(exist_ok=True)
for p in C.rglob('*.css'):
 target=out/p.relative_to(C);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
for p in (V/'reassembled').glob('*.html'):
 p.write_text(p.read_text().replace('../../collection/dockside/','../assets/collection/'))
print('Frozen CSS snapshots',len(list(out.rglob('*.css'))))
