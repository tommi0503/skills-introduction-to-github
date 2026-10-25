"""Publish the reviewed release through HTTPS APIs; never execute git commands.

Local binary streaming is needed because the connector accepts strings, not local
paths. The repository and publication scope are fixed to the user's request.
"""
from pathlib import Path
import base64,concurrent.futures,hashlib,json,os,threading,time,urllib.request,urllib.error
ROOT=Path(__file__).resolve().parents[1]
REPO='tommi0503/skills-introduction-to-github';PREFIX=ROOT.name;BASE='https://api.github.com/repos/'+REPO
TOKEN=os.environ['GH_TOKEN'];HEADERS={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','Content-Type':'application/json','User-Agent':'Rhetis-reviewed-release'}
def api(method,path,data=None):
 body=json.dumps(data,ensure_ascii=False,separators=(',',':')).encode()if data is not None else None
 for attempt in range(8):
  try:
   req=urllib.request.Request(BASE+path,body,HEADERS,method=method)
   with urllib.request.urlopen(req,timeout=180)as r:return json.load(r)
  except urllib.error.HTTPError as e:
   if e.code not in [403,429,500,502,503,504]or attempt==7:raise RuntimeError('GitHub API '+method+' '+path+' HTTP '+str(e.code)+' '+e.read(2000).decode())from None
   delay=min(60,max(5*2**attempt,int(e.headers.get('Retry-After','0'))));print('Retry',e.code,method,path,'in',delay,'s',flush=True);time.sleep(delay)
  except (TimeoutError,urllib.error.URLError):
   if attempt==7:raise
   time.sleep(min(30,2**attempt))
def oid(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def current():return api('GET','/git/ref/heads/main')['object']['sha']
def main():
 start=current();head=api('GET','/git/commits/'+start);tree=head['tree']['sha'];top=api('GET','/git/trees/'+tree)['tree'];known={x['sha']for x in top if x['type']=='blob'}
 if any(x['path']==PREFIX for x in top):raise RuntimeError('Publication prefix already exists; refuse to overwrite')
 for row in top:
  if row['path']in ['rhetis-enterprise-053-069','rhetis-elements-053-069-20261024']and row['type']=='tree':
   index=api('GET','/git/trees/'+row['sha']+'?recursive=1')
   if index.get('truncated'):raise RuntimeError('Existing tree inventory was truncated')
   known.update(x['sha']for x in index['tree']if x['type']=='blob')
 cache=ROOT/'publication-binary-cache.json'
 if cache.exists():known.update(json.loads(cache.read_text()).get('sha',[]))
 files=[];binaries={};texts=[];extensions={'.css','.json','.md','.html','.js','.woff','.woff2','.py','.png','.pdf','.zip','.txt'}
 for p in sorted(ROOT.rglob('*')):
  if not p.is_file()or any(x.startswith('.')or x=='__pycache__'for x in p.relative_to(ROOT).parts):continue
  if p.name.startswith(('publication','download-verification')):continue
  if p.suffix not in extensions and p.name!='SHA256SUMS':continue
  data=p.read_bytes();sha=oid(data);rel=PREFIX+'/'+str(p.relative_to(ROOT));files.append({'path':rel,'mode':'100644','type':'blob','sha':sha});record={'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha':sha,'sha256':hashlib.sha256(data).hexdigest()}
  if sha in known:continue
  if p.suffix in {'.png','.pdf','.woff','.woff2','.zip'}:binaries.setdefault(sha,record)
  else:
   record['content']=data.decode('utf-8');texts.append(record)
 print('Publication inventory',len(files),'files;',len(binaries),'new binary blobs;',len(texts),'text files;',len(known),'known blobs',flush=True)
 completed=0;lock=threading.Lock()
 def upload(row):
  nonlocal completed
  data=(ROOT/row['path']).read_bytes();result=api('POST','/git/blobs',{'encoding':'base64','content':base64.b64encode(data).decode()})
  if result['sha']!=row['sha']:raise RuntimeError('Remote binary SHA mismatch '+row['path'])
  with lock:
   saved=json.loads(cache.read_text())if cache.exists()else{'sha':[]}
   saved['sha']=sorted(set(saved['sha'])|{row['sha']});cache.write_text(json.dumps(saved))
   completed+=1
   if completed%25==0 or completed==len(binaries):print('Binary blobs',completed,'/',len(binaries),flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:list(pool.map(upload,sorted(binaries.values(),key=lambda r:r['bytes'])))
 # Create text blobs in size-limited tree batches, then bind the final complete
 # release tree onto the current main tree. Unrelated paths remain unchanged.
 batch=[];size=0
 def text_batch(rows):
  if not rows:return
  elements=[{'path':PREFIX+'/'+r['path'],'mode':'100644','type':'blob','content':r['content']}for r in rows]
  result=api('POST','/git/trees',{'tree':elements})
  print('Text batch',len(rows),'tree',result['sha'],flush=True)
 for row in texts:
  if batch and(size+row['bytes']>3*1024*1024 or len(batch)>=100):text_batch(batch);batch=[];size=0
  batch.append(row);size+=row['bytes']
 text_batch(batch)
 for attempt in range(3):
  parent=current();parentdata=api('GET','/git/commits/'+parent);parenttree=parentdata['tree']['sha'];entries=api('GET','/git/trees/'+parenttree)['tree']
  if any(x['path']==PREFIX for x in entries):raise RuntimeError('Concurrent release at publication prefix; refusing overwrite')
  result={'sha':parenttree}
  for start in range(0,len(files),100):
   result=api('POST','/git/trees',{'base_tree':result['sha'],'tree':files[start:start+100]})
   print('Source tree entries',min(start+100,len(files)),'/',len(files),flush=True)
  commit=api('POST','/git/commits',{'message':'Rebuild seven Rhetis collections from preserved replicas under round 5','tree':result['sha'],'parents':[parent]})
  if current()!=parent:print('Main advanced; preserving latest parent and retrying',flush=True);continue
  ref=api('PATCH','/git/refs/heads/main',{'sha':commit['sha'],'force':False});assert ref['object']['sha']==commit['sha']
  report={'repository':REPO,'prefix':PREFIX,'branch':'main','parent':parent,'commit':commit['sha'],'tree':result['sha'],'files':len(files),'createdUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'method':'GitHub connector metadata, HTTPS Git Data API for source and ZIP assets; no git commands; no force update; existing base tree and latest parent preserved.','sourceURL':'https://github.com/'+REPO+'/tree/'+commit['sha']+'/'+PREFIX,'reviewedStates':json.loads((ROOT/'verification.json').read_text())['states']}
  (ROOT/'publication.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));(ROOT/'publication-upload-manifest.json').write_text(json.dumps(files,ensure_ascii=False,indent=2));print('PUBLISHED',commit['sha'],len(files),'files',flush=True);return
 raise RuntimeError('Main advanced repeatedly; no branch ref was changed')
if __name__=='__main__':main()
