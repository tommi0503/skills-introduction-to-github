import json,sys,hashlib,datetime
from pathlib import Path
p=Path('review/quality/group-b.json');q=json.loads(p.read_text());round=sys.argv[1]
for key in sys.argv[2:]:
 d,s=key.split('/');paths={'pair':f'comparisons/{round}/{d}-{s}.jpg','png':f'renders/{round}/{d}-{s}.png','reference':f'public/reference/{d}/{s}.jpg'}
 q['pages'][key]['individualViews'].append({'round':round,'actuallyViewedPair':True,'actuallyViewedNativePNG':False,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':{k:hashlib.sha256(Path(v).read_bytes()).hexdigest()for k,v in paths.items()},'paths':paths})
t=p.with_suffix('.tmp');t.write_text(json.dumps(q,ensure_ascii=False,indent=2));t.replace(p);print('logged',sys.argv[2:])
