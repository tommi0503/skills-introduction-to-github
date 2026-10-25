#!/usr/bin/env python3
"""Publish this authorized deliverable using GitHub REST only; no Git executable.
Blobs are content addressed; the normal main ref is updated only if its expected
head still matches. Existing repository trees and earlier deliveries are preserved.
"""
import argparse,base64,concurrent.futures,datetime,hashlib,json,os,ssl,time,threading
from pathlib import Path
from urllib.request import Request,build_opener,ProxyHandler,HTTPSHandler
from urllib.error import HTTPError
ROOT=Path(__file__).resolve().parents[1]
REPO='tommi0503/skills-introduction-to-github';PREFIX='rhetis-round5';API='https://api.github.com/repos/'+REPO
CACHE=ROOT/'api-blob-cache.json'
TEXT={'.css','.json','.md','.html','.py','.js','.txt'}
POST_LOCK=threading.Lock();LAST_POST=[0.0]
EXCLUDE={'__pycache__','sheet-cells','panel-cells','sheet-runtime','foundation-runtime','.git','node_modules'}

def stamp():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git_blob_sha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def inventory():
 rows=[]
 for p in sorted(ROOT.rglob('*')):
  if not p.is_file() or p.is_symlink():continue
  rel=p.relative_to(ROOT)
  if any(x in EXCLUDE for x in rel.parts):continue
  # REST Git blob rejects these large review archives; preserve exact bytes as
  # assets on this same repository's Round5 release. Small collection ZIPs commit normally.
  if p.suffix in {'.tmp','.pyc','.log'} or p.name in {'api-blob-cache.json','api-publication.json','release-publication.json','STATE.md'}:continue
  # Sources, immutable replicas/assets, canonical matrices, comparisons, previews,
  # review notes, all ten archives. Exclude old temporary functional probes.
  if rel.parts[0]=='tools' and ('integration-functional' in str(rel) or p.name.startswith('anchor-probe')):continue
  if rel.parts[0]=='reference' and ('samples' in rel.parts) and not (len(rel.parts)>3 and rel.parts[2]=='annual'and p.name=='element.json'):continue
  if rel.parts[0].endswith('-project'):
   second=rel.parts[1] if len(rel.parts)>1 else ''
   # Temporary authoring generators are preserved locally and in earlier work;
   # the delivered declarative HTML/CSS/JSON and supported tools are the source.
   if len(rel.parts)==2 and p.suffix=='.py':continue
   if second in {'sheet-cells','panel-cells','sheet-runtime','foundation-runtime'}:continue
   if p.suffix=='.png' and second not in {'replica','sheets','reassembled','compare-reassembled','foundation-sheets','panel-sheets','paint-proofs'}:continue
   if second=='sheets' and p.suffix=='.json' and p.stem.endswith('-checks'):
    k=rel.parts[0][:-8];leaf=p.stem[:-7]
    if not(ROOT/rel.parts[0]/k/'elements'/leaf).is_dir():continue
   if second=='sheets' and p.suffix=='.png':
    k=rel.parts[0][:-8];stem=p.stem;leaf=next((stem[:-len(t)] for t in ['-replica','-light','-dark'] if stem.endswith(t)),None)
    if leaf is None or not(ROOT/rel.parts[0]/k/'elements'/leaf).is_dir():continue
  raw=p.read_bytes();rows.append({'path':str(rel),'sha':git_blob_sha(raw),'size':len(raw)})
 return rows

def run(args):
 token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
 if not token:raise RuntimeError('Configured GitHub authentication is unavailable')
 opener=build_opener(ProxyHandler(),HTTPSHandler(context=ssl.create_default_context()))
 def api(method,path,data=None):
  if method=='POST':
   with POST_LOCK:
    pause=max(0,1.05-(time.monotonic()-LAST_POST[0]));time.sleep(pause);LAST_POST[0]=time.monotonic()
  body=None if data is None else json.dumps(data,separators=(',',':')).encode()
  req=Request(API+path,body,method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'Rhetis-round5-authorized-publisher','Content-Type':'application/json'})
  for attempt in range(5):
   try:
    with opener.open(req,timeout=60) as response:return json.load(response)
   except HTTPError as e:
    details=json.load(e)
    retry=e.code in [429,500,502,503,504] or (e.code==403 and 'secondary rate' in details.get('message','').lower())
    if not retry or attempt==4:raise RuntimeError(f'GitHub API {method} {path}: HTTP {e.code}; '+details.get('message','')) from None
    delay=min(60,max(10,int(e.headers.get('Retry-After','60'))));print('Respecting GitHub retry window',delay,'seconds',flush=True);time.sleep(delay)
 head=api('GET','/git/ref/heads/main')['object']['sha'];commit=api('GET','/git/commits/'+head);tree=commit['tree']['sha'];entries=api('GET','/git/trees/'+tree)['tree'];known=set()
 for ent in entries:
  if ent['type']=='tree' and ent['path'] in ['rhetis-part07-elements-v2',PREFIX]:
   subtree=api('GET','/git/trees/'+ent['sha']+'?recursive=1');assert not subtree.get('truncated');known.update(x['sha'] for x in subtree['tree'] if x['type']=='blob')
 cache=json.loads(CACHE.read_text()) if CACHE.exists() else {};known.update(cache)
 rows=inventory();missing={r['sha']:r for r in rows if r['sha'] not in known and (Path(r['path']).suffix not in TEXT or r['size']>100000)};print('Inventory',len(rows),'files; existing blobs',len(rows)-sum(r['sha'] in missing for r in rows),'unique uploads',len(missing),flush=True)
 def upload(row):
  raw=(ROOT/row['path']).read_bytes()
  if args.stage_only and git_blob_sha(raw)!=row['sha']:return None,0
  assert git_blob_sha(raw)==row['sha'],'Input changed; retry snapshot'
  answer=api('POST','/git/blobs',{'content':base64.b64encode(raw).decode(),'encoding':'base64'});assert answer['sha']==row['sha'];return row['sha'],row['size']
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
  jobs=[pool.submit(upload,row)for row in missing.values()];failed=None;n=0
  for future in concurrent.futures.as_completed(jobs):
   try:sha,size=future.result()
   except Exception as error:
    failed=failed or error
    for job in jobs:job.cancel()
    continue
   if sha:cache[sha]=size
   n+=1;CACHE.write_text(json.dumps(cache))
   if n%20==0 or n==len(missing):print('Uploaded',n,'/',len(missing),flush=True)
  if failed:raise failed
 CACHE.write_text(json.dumps(cache))
 if args.stage_only:return
 assert rows==inventory(),'Source inventory changed while uploading; rerun before commit'
 assert api('GET','/git/ref/heads/main')['object']['sha']==head,'Repository advanced; rerun to preserve new work'
 chunks=[];chunk=[];size=0
 for row in rows:
  ent={'path':PREFIX+'/'+row['path'],'mode':'100644','type':'blob'}
  if row['sha'] in known or row['sha'] in cache:ent['sha']=row['sha']
  else:ent['content']=(ROOT/row['path']).read_text()
  length=len(json.dumps(ent).encode())
  if chunk and (size+length>250_000 or len(chunk)>=100):chunks.append(chunk);chunk=[];size=0
  chunk.append(ent);size+=length
 if chunk:chunks.append(chunk)
 for n,chunk in enumerate(chunks,1):
  newtree=api('POST','/git/trees',{'base_tree':tree,'tree':chunk});tree=newtree['sha'];print('Created tree chunk',n,'/',len(chunks),flush=True)
 assert rows==inventory(),'Source inventory changed before commit; rebuild the snapshot'
 assert api('GET','/git/ref/heads/main')['object']['sha']==head,'Repository advanced before commit; preserve and retry'
 newcommit=api('POST','/git/commits',{'message':'Rebuild replica-derived responsive libraries under round5 contract','tree':newtree['sha'],'parents':[head]})
 # The API performs a normal non-forced fast-forward. Parent is the observed head.
 api('PATCH','/git/refs/heads/main',{'sha':newcommit['sha'],'force':False})
 report={'schema':'rhetis.api-publication/1','publishedAtUTC':stamp(),'repository':REPO,'prefix':PREFIX,'previousHead':head,'commitSHA':newcommit['sha'],'treeSHA':newtree['sha'],'fileCount':len(rows),'gitCommandsUsed':False,'force':False,'inventorySHA256':hashlib.sha256(json.dumps(rows,sort_keys=True).encode()).hexdigest()}
 (ROOT/'api-publication.json').write_text(json.dumps(report,indent=2));print('Published',newcommit['sha'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--stage-only',action='store_true');p.add_argument('--workers',type=int,default=4);run(p.parse_args())
