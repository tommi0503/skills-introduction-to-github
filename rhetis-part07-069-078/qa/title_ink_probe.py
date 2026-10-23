from pathlib import Path
import json
from PIL import Image
import numpy as np
P=Path(__file__).resolve().parents[1]/'crossrail-project'
rows=[]
for f in sorted((P/'fidelity').glob('slide_*-triple.png')):
 a=np.asarray(Image.open(f).convert('RGB')); found=[]
 for x in [0,1280,2560]:
  roi=a[125:215,x+96:x+450]; bg=np.median(roi.reshape(-1,3),axis=0)
  m=(roi.min(2)>205) if bg.mean()<150 else ((roi[:,:,0]<80)&(roi[:,:,1]<110)&(roi[:,:,2]<160))
  ys,xs=np.where(m); found.append([int(xs.min()+96),int(ys.min()+125),int(xs.max()+96),int(ys.max()+125)] if len(ys) else None)
 rows.append({'page':f.stem.split('-')[0],'original':found[0],'replica':found[1],'assembly':found[2],'replicaTopDelta':found[1][1]-found[0][1] if found[0] and found[1] else None,'assemblyTopDelta':found[2][1]-found[0][1] if found[0] and found[2] else None})
(P/'fidelity/title-ink-probe.json').write_text(json.dumps(rows,indent=2));print('\n'.join(f"{r['page']} original={r['original']} replica={r['replicaTopDelta']} assembly={r['assemblyTopDelta']}" for r in rows))
