from pathlib import Path
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside'
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s+'\n')
r='.mindmap[data-el="dockside-mindmap"]:has(.person):has(>.branch:nth-child(5):last-child)'
add('mindmap',r+'>.branch>.person>.name{font-size:var(--type-22)}')
r='.card[data-el="dockside-card"].line:has(.mark>.icon):has(.note>.list)'
add('card',r+'>.parts>.mark>.icon:last-child,'+r+'>.parts>.kick>.icon:last-child{position:absolute;left:58px;top:55px;width:23px;height:23px;padding:0;border:0;border-radius:50%;background:var(--a1);color:var(--a1-on);box-shadow:none}')
r='.hub[data-el="dockside-hub"]:has(>.spoke:nth-child(5):last-child)'
add('hub',r+'>.core::after{display:block;z-index:0;border-color:var(--a1-2-soft)}')
for p in C.rglob('*.css'):shutil.copyfile(p,R/'review/assets/collection'/p.relative_to(C))
