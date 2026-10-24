import sys,json
from pathlib import Path
P=Path(__file__).parent
r=json.loads((P/'review-progress.json').read_text())
for leaf in sys.argv[1:]:
 x=json.loads((P/'sheets'/f'{leaf}-checks.json').read_text());keys=['outside','clipped','overlaps','outsideComponent','outsideParts','contrast'];counts={k:sum(len(d.get(k,[])) for a in x['modes'].values() for d in a) for k in keys}
 if any(counts.values()):raise SystemExit(str((leaf,counts)))
 r[leaf]={'reviewedModes':['light','dark']+(['replica'] if (P/'sheets'/f'{leaf}-replica.png').exists() else []),'cells':sum(map(len,x['modes'].values())),'sourceFingerprint':x['sourceFingerprint'],'rendererVersion':x['rendererVersion'],'counts':counts}
(P/'review-progress.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
