from pathlib import Path
import math,json,shutil,hashlib
C=Path('/workspace/work/deliverables/confluence/collection/confluence');R=C.parent.parent/'review';q='.radar[data-el="confluence-radar"]';p=C/'elements/radar/element.css';s=p.read_text()
for n in range(3,9):
 points=[]
 for i in range(n):
  x=math.sin(2*math.pi*i/n)*50;y=-math.cos(2*math.pi*i/n)*50
  points.append(f'calc(50% + var(--v{i+1})/var(--max)*{x:.6f}%) calc(50% + var(--v{i+1})/var(--max)*{y:.6f}%)')
 s+=f'@container style(--n:{n})'+'{'+q+' .series::before{clip-path:polygon('+','.join(points)+')}}\n'
p.write_text(s)
for f in C.rglob('*.css'):shutil.copy(f,R/'assets/collection'/f.relative_to(C))
(R/'source-manifest.json').write_text(json.dumps({str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(C.rglob('*')) if p.is_file()},indent=2))
