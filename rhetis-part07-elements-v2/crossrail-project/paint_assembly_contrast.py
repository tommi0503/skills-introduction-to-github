from pathlib import Path
import json,sys,hashlib,collections
from PIL import Image
sys.path.insert(0,'/workspace/work/rhetis-elements-v2/tools')
from sheets import raster_contrast,fingerprint
P=Path(__file__).parent
raw=json.loads((P/'reassembly-checks.json').read_text());out=json.loads(json.dumps(raw));total=collections.Counter()
for diag in out['pages']:
 assert diag['sourceFingerprint']==fingerprint(P,'crossrail'),('stale source',diag['page'])
 f=P/'reassembled'/(diag['page']+'.html');assert diag['htmlSHA256']==hashlib.sha256(f.read_bytes()).hexdigest()
 raster_contrast(diag,Image.open(P/'reassembled'/(diag['page']+'.png')),{'x':0,'y':0})
 for key in ['outside','clipped','overlaps','outsideComponent','outsideParts','contrast']:total[key]+=len(diag.get(key,[]))
 total['fontFailed']+=sum(not x.get('loaded') for x in diag.get('fonts',[]));total['requestFailures']+=len(diag.get('requestFailures',[]))
out['method']='Raw DOM candidates remain in reassembly-checks.json. The shared sheets.raster_contrast method reevaluates actual rendered text background pixels here; source and HTML hashes are asserted identical.'
out['totals']=dict(total)
(P/'reassembly-painted-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(dict(total))
for d in out['pages']:
 for key in ['outsideComponent','contrast']:
  if d[key]:print(d['page'],key,d[key])
