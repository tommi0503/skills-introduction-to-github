from pathlib import Path
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside'
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('chart-stack','.stack[data-el="dockside-chart-stack"] .seg span,.chart-stack[data-el="dockside-chart-stack"] .seg span{background:var(--page);color:var(--ink);border-radius:var(--radius-sm);padding:2px 4px}')
# Contract source root is bars, cover every permitted root through the data-el scope.
add('chart-stack','[data-el="dockside-chart-stack"] .seg span{background:var(--page);color:var(--ink);border-radius:var(--radius-sm);padding:2px 4px}')
add('matrix','[data-el="dockside-matrix"] .cell.on .list[data-el="dockside-list"] .name{color:var(--a1-on)}')
r='.radar[data-el="dockside-radar"]'
add('radar',f'{r}::before,{r}>.series{{inset:auto;left:50%;top:50%;width:min(56cqw,60cqh);height:min(56cqw,60cqh);transform:translate(-50%,-50%)}}{r}>.axis{{left:calc(50% + sin(var(--dockside-angle)) * min(39cqw,44cqh));top:calc(50% - cos(var(--dockside-angle)) * min(39cqw,44cqh))}}')
r='.donut[data-el="dockside-chart-donut"]:not(.donuts .donut)'
add('chart-donut',f'{r}{{width:100%;height:100%;aspect-ratio:auto;border:0;border-radius:0;background:none;box-shadow:none}}{r}::before{{inset:auto;left:50%;top:50%;transform:translate(-50%,-50%);width:min(90cqw,90cqh);height:min(90cqw,90cqh);background:conic-gradient(var(--a1) 0 calc(var(--v)*1%),var(--n-2) calc(var(--v)*1%) 100%);border:14px solid var(--page);box-shadow:0 7px 20px var(--n-2)}}{r}::after{{content:"";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:calc(min(90cqw,90cqh) - 64px);height:calc(min(90cqw,90cqh) - 64px);border-radius:50%;background:var(--page)}}{r} .fig,{r} .name{{z-index:2}}')
for p in C.rglob('*.css'):
 q=R/'review/assets/collection'/p.relative_to(C);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
