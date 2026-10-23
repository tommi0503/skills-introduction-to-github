from pathlib import Path
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside'
p=C/'elements/chart-donut/element.css'
s=p.read_text();s+='''
/* Nested contract donuts use their group as the size container. */
.donuts[data-el="dockside-chart-donut"]:has(>.donut)>.donut[data-el="dockside-chart-donut"]{container-type:normal;width:min(340px,calc((100cqw - var(--gap) * (var(--dockside-count) - 1)) / var(--dockside-count)),calc(100cqh - var(--pad)));height:min(340px,calc((100cqw - var(--gap) * (var(--dockside-count) - 1)) / var(--dockside-count)),calc(100cqh - var(--pad)))}
@container(max-width:650px){.donuts[data-el="dockside-chart-donut"]:has(>.donut:nth-child(4))>.donut[data-el="dockside-chart-donut"]{width:calc((min(100cqw,100cqh) - var(--gap) * 2) / 2);height:calc((min(100cqw,100cqh) - var(--gap) * 2) / 2)}}
''';p.write_text(s)
import shutil
for p in C.rglob('*.css'):
 q=R/'review/assets/collection'/p.relative_to(C);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
