from pathlib import Path
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside'
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s+'\n')
r='.card[data-el="dockside-card"]:has(>.parts>.fig):has(>.parts>.mark)'
add('card',r+'>.parts>.fig{color:var(--a1-on)}')
r='.orbit[data-el="dockside-concentric"]:has(>.ring:nth-child(2):last-child):has(.seat)'
add('concentric',r+'>.ring:nth-child(2)>.note{color:var(--n-7)}')
r='.steps[data-el="dockside-steps"]:has(>.step:nth-child(3):last-child):has(.name>.seat)'
add('steps',r+'>.step>.note{background:none}'+r+'>.step>.note::before{content:"";position:absolute;left:0;top:8px;width:5px;height:5px;background:var(--n-8);border-radius:50%;box-shadow:0 28px 0 var(--n-8)}')
r='.hub[data-el="dockside-hub"]:has(>.spoke:nth-child(5):last-child):has(>.core>.seat)'
add('hub','@container (max-height:700px){'+r+'>.core{top:420px}}')
for p in C.rglob('*.css'):shutil.copyfile(p,R/'review/assets/collection'/p.relative_to(C))
