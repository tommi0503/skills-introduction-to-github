"""Local payload bridge for authenticated connector publication; never reads secrets."""
import argparse,base64,hashlib,importlib.util,json,sys,urllib.request,fcntl
from pathlib import Path
from publish_api import ROOT,REPO,inventory,git_blob_sha,TEXT,CACHE
D=Path('/tmp/r5-api-bridge');D.mkdir(exist_ok=True)
def get(path):
 req=urllib.request.Request('https://api.github.com/repos/'+REPO+path,headers={'User-Agent':'Rhetis-round5-public-metadata'})
 with urllib.request.urlopen(req,timeout=40)as r:return json.load(r)
a=sys.argv[1]
if a=='plan':
 head=get('/git/ref/heads/main')['object']['sha'];commit=get('/git/commits/'+head);base=commit['tree']['sha'];known=set();entries=get('/git/trees/'+base)['tree']
 for e in entries:
  if e['type']=='tree' and e['path'] in ['rhetis-part07-elements-v2','rhetis-round5']:
   t=get('/git/trees/'+e['sha']+'?recursive=1');assert not t.get('truncated');known.update(x['sha']for x in t['tree']if x['type']=='blob')
 cache=json.loads(CACHE.read_text())if CACHE.exists()else{};known.update(cache);rows=inventory();missing={x['sha']:x for x in rows if x['sha'] not in known and Path(x['path']).suffix not in TEXT}
 plan={'head':head,'baseTree':base,'rows':rows,'known':list(known),'missing':list(missing.values())};(D/'plan.json').write_text(json.dumps(plan));print(json.dumps({'files':len(rows),'missingBinary':len(missing),'head':head,'bytes':sum(x['size']for x in missing.values())}))
elif a=='list':print(json.dumps(json.loads((D/'plan.json').read_text())['missing']))
elif a=='read':
 row=json.loads((D/'plan.json').read_text())['missing'][int(sys.argv[2])];b=(ROOT/row['path']).read_bytes();assert git_blob_sha(b)==row['sha'],'Changed after snapshot';print(base64.b64encode(b).decode(),end='')
elif a=='read-part':
 row=json.loads((D/'plan.json').read_text())['missing'][int(sys.argv[2])];b=(ROOT/row['path']).read_bytes();assert git_blob_sha(b)==row['sha'],'Changed after snapshot'
 start=int(sys.argv[3]);count=int(sys.argv[4]);assert start%3==0 and count%3==0
 print(base64.b64encode(b[start:start+count]).decode(),end='')
elif a=='ack':
 row=json.loads((D/'plan.json').read_text())['missing'][int(sys.argv[2])];assert sys.argv[3]==row['sha']
 with (D/'cache.lock').open('w')as lock:
  fcntl.flock(lock,fcntl.LOCK_EX);cache=json.loads(CACHE.read_text())if CACHE.exists()else{};cache[row['sha']]=row['size'];CACHE.write_text(json.dumps(cache))
 print(row['path'])
elif a=='read-batch':
 plan=json.loads((D/'plan.json').read_text())['missing'];items=[]
 for i in map(int,sys.argv[2].split(',')):
  row=plan[i];b=(ROOT/row['path']).read_bytes()
  if git_blob_sha(b)!=row['sha']:items.append({'index':i,'changed':True});continue
  items.append({'index':i,'sha':row['sha'],'size':len(b),'content':base64.b64encode(b).decode()})
 print(json.dumps(items,separators=(',',':')),end='')
elif a=='ack-batch':
 plan=json.loads((D/'plan.json').read_text())['missing'];indices=list(map(int,sys.argv[2].split(',')))
 with(D/'cache.lock').open('w')as lock:
  fcntl.flock(lock,fcntl.LOCK_EX);cache=json.loads(CACHE.read_text())if CACHE.exists()else{}
  for i in indices:row=plan[i];cache[row['sha']]=row['size']
  CACHE.write_text(json.dumps(cache))
 print('Acknowledged',len(indices))
