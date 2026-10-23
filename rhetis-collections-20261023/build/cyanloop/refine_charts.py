from pathlib import Path
import re
C=Path('/workspace/output/cyanloop');K='cyanloop'
f=C/'elements/chart-line/element.css';s=f.read_text();s=s[:s.index('/* numeric dispatch */')] if '/* numeric dispatch */' in s else s
# Remove the first experimental dispatch and point connector rules; replace with a single continuous polygon stroke.
s='\n'.join(l for l in s.splitlines() if '--cyanloop-p' not in l)
s+='\n/* numeric dispatch */\n'
rt='.lines[data-el="cyanloop-chart-line"]'
vals=set(range(101))
for p in (f.parent/'fixtures').glob('*.html'):vals.update(int(v) for v in re.findall(r'--v:\s*(\d+)',p.read_text()))
for i in range(1,13):
 for v in sorted(vals): s+=f'{rt}:has(>.pt:nth-child({i})[style$="--v:{v}"]){{ --cyanloop-p{i}:{v}; }}\n'
s+=rt+'::after{content:"";position:absolute;inset:var(--gap-lg) var(--gap);background:var(--a1);pointer-events:none;}\n'
for n in range(2,13):
 points=[f'{(i+.5)/n*100:.5f}% calc(100% - var(--cyanloop-p{i+1},0) / var(--max) * 100%)' for i in range(n)]
 points+= [f'{(i+.5)/n*100:.5f}% calc(100% - var(--cyanloop-p{i+1},0) / var(--max) * 100% + 2px)' for i in reversed(range(n))]
 s+=rt+f':has(>.pt:nth-child({n}):last-child)::after{{clip-path:polygon('+','.join(points)+');}\n'
f.write_text(s)
f=C/'elements/chart-area/element.css';s=f.read_text();rt='.areas[data-el="cyanloop-chart-area"]';sr=rt+' .series'
s+='\n'+sr+' .pt {background:none;border:0;}\n'+sr+'::before{content:"";position:absolute;inset:0;background:var(--a1-2-soft);opacity:.75;z-index:-1;}\n'+sr+':nth-child(2)::before{background:var(--a2-2-soft);}\n'+sr+':nth-child(3)::before{background:var(--a3-2-soft);}\n'+sr+':nth-child(4)::before{background:var(--a4-2-soft);}\n'
vals=set(range(101))
for p in (f.parent/'fixtures').glob('*.html'):vals.update(int(v) for v in re.findall(r'--v:\s*(\d+)',p.read_text()))
for i in range(1,13):
 for v in sorted(vals):s+=sr+f':has(>.pt:nth-of-type({i})[style$="--v:{v}"]){{--cyanloop-p{i}:{v};}}\n'
for n in range(3,13):
 points=['0% 100%']+[f'{i/(n-1)*100:.5f}% calc(100% - var(--cyanloop-p{i+1},0) / var(--max) * 100%)' for i in range(n)]+['100% 100%']
 s+=sr+f':has(>.pt:nth-of-type({n}):last-child)::before{{clip-path:polygon('+','.join(points)+');}\n'
for i in range(1,5):s+=rt+f'.stacked .series:nth-child({i}){{z-index:{5-i};}}\n'
s+=sr+' .pt{height:100%;}'+sr+' .pt b{bottom:calc(var(--v) / var(--max) * 100% + var(--gap-sm));}\n'
f.write_text(s)
f=C/'foundation/foundation.css';s=f.read_text().replace('* { box-sizing:border-box; }','.slide,.slide * { box-sizing:border-box; }');f.write_text(s)
f=C/'elements/sparkline/element.css';s=f.read_text().replace('gap:2px','gap:var(--stroke)');f.write_text(s)
