from pathlib import Path
from bs4 import BeautifulSoup
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
p=C/'elements/callout/element.css';s=p.read_text().replace(':has(>p>b:first-child)',':has(>p>b:first-child):has(>p>br)');p.write_text(s)
# Explicit source structures exercise the restored geometries in both palettes.
cases=[(5,'card','.group','source-growth-bubbles'),(7,'concentric','.orbit','source-keyword-orbit'),(17,'hub','.hub','source-differentiation'),(22,'steps','.steps','source-circle-steps'),(23,'steps','.steps','source-stair-steps'),(19,'person','.people','source-personas'),(27,'hierarchy','.org','source-team-tree'),(28,'mindmap','.mindmap','source-team-map')]
for n,folder,sel,name in cases:
 b=BeautifulSoup((V/f'reassembled/slide_{n:02}.html').read_text(),'html.parser');q=b.select_one(sel);q['style']='grid-column:1 / span 12; grid-row:1 / span 6'
 (C/f'elements/{folder}/fixtures/{name}.html').write_text('<!-- min: 12x6 -->\n'+str(q)+'\n')
# Shorter full-page slots retain the original geometry with a higher baseline.
selectors={
'card':['.card[data-el="dockside-card"]:has(>.parts>.fig):has(>.parts>.mark)'],
'concentric':['.orbit[data-el="dockside-concentric"]:has(.seat)'],
'hub':['.hub[data-el="dockside-hub"]:has(>.core>.seat)'],
'steps':['.steps[data-el="dockside-steps"]:has(.name>.seat)','.steps[data-el="dockside-steps"]:has(>.step:nth-child(5):last-child)'],
'person':['.people[data-el="dockside-person"]:has(.list)'],
'hierarchy':['.org[data-el="dockside-hierarchy"]:has(.person)'],
'mindmap':['.mindmap[data-el="dockside-mindmap"]:has(.person)']}
for folder,rs in selectors.items():
 p=C/f'elements/{folder}/element.css';p.write_text(p.read_text()+'\n@container (max-height:700px){'+','.join(rs)+'{translate:0 -150px}}\n')
for p in C.rglob('*.css'):shutil.copyfile(p,V/'assets/collection'/p.relative_to(C))
