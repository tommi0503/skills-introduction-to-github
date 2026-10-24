import json,sys
from pathlib import Path
P=Path(__file__).parent
for leaf in sys.argv[1:]:
 x=json.loads((P/'sheets'/f'{leaf}-checks.json').read_text());print(leaf, 'cells',sum(map(len,x['modes'].values())))
 for m,a in x['modes'].items():
  print(m,{k:sum(len(d.get(k,[])) for d in a) for k in ['outside','clipped','overlaps','outsideComponent','outsideParts','contrast']})
  for d in a:
   for k in ['outside','clipped','overlaps','outsideComponent','outsideParts','contrast']:
    if d.get(k):print(d['fixture'],d['size'],k,str(d[k])[:1200])
