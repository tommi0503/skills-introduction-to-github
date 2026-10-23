from pathlib import Path
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside'
def add(f,s):
 p=C/('foundation/foundation.css' if f=='foundation' else f'elements/{f}/element.css');p.write_text(p.read_text()+'\n'+s+'\n')
add('pill','.pill[data-el="dockside-pill"].quiet:has(.mark>.seat):has(.note){top:351px}.pill[data-el="dockside-pill"].line:has(.mark>.icon){top:478px}')
add('callout','.callout[data-el="dockside-callout"]:has(>.icon):not(:has(>p>b)){justify-content:flex-start}')
add('agenda','.agenda[data-el="dockside-agenda"]:has(.mark>.seat.icon)>.entry>.name{border-bottom:0;padding-bottom:0}')
add('card','.card[data-el="dockside-card"]:is(.line,.quiet):has(>.parts>.fig):has(>.parts>.mark)>.parts>.fig{color:var(--a1-on)}')
add('foundation','''.slide.overrides::before{display:block;content:"";position:absolute;inset:0;clip-path:none;background:repeating-linear-gradient(45deg,color-mix(in srgb,var(--a1-4) 22%,transparent) 0 56px,transparent 57px 112px);mask-image:linear-gradient(90deg,transparent 72%,var(--ink) 100%);opacity:.7;pointer-events:none}.slide.cover.overrides::before,.slide.overrides:has(.head.center):not(:has(.head .kicker))::before{mask-image:linear-gradient(0deg,var(--ink) 0%,var(--ink) 22%,transparent 55%);opacity:.65}''')
for p in C.rglob('*.css'):shutil.copyfile(p,R/'review/assets/collection'/p.relative_to(C))
