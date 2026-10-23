from pathlib import Path
import math
C=Path('/workspace/output/nightchamfer');s='[data-el="nightchamfer-chart-area"]';p=C/'elements/chart-area/element.css';p.write_text(p.read_text()+f'''\n{s}{{--nightchamfer-plot-h:100cqh}}\n{s}>.series:nth-child(2){{--nightchamfer-area-fill:var(--a2-2-soft);--nightchamfer-area-line:var(--a2)}}\n{s}>.series:nth-child(3){{--nightchamfer-area-fill:var(--a3-2-soft);--nightchamfer-area-line:var(--a3)}}\n{s}>.series:nth-child(4){{--nightchamfer-area-fill:var(--a4-2-soft);--nightchamfer-area-line:var(--a4)}}\n''')
s='[data-el="nightchamfer-radar"]';p=C/'elements/radar/element.css';css=f'''\n{s}::before,{s}>.series::before{{inset:auto;width:70cqh;height:70cqh;top:15%;left:50%;transform:translateX(-50%);aspect-ratio:1}}{s}>.series:nth-of-type(2)::before{{background:color-mix(in srgb,var(--a2) 22%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%))}}{s}>.series:nth-of-type(2)>.name{{left:40%;color:var(--a2-7)}}\n'''
for n in range(3,9):
 sel=f'{s}:is([style*="--n:{n}"],[style*="--n: {n}"])'
 for i in range(n):
  a=2*math.pi*i/n;css+=f'{sel}>.axis:nth-child({i+1}){{left:calc(50% + {math.sin(a)*41:.6f}cqh);top:calc(50% - {math.cos(a)*41:.6f}cqh)}}\n'
p.write_text(p.read_text()+css)
