"""Re-download immutable GitHub ZIPs, compare local SHA256, and check each member's CRC."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen,Request
from datetime import datetime,timezone
import hashlib,json,re,sys,zipfile
commit=sys.argv[1]
if not re.fullmatch('[0-9a-f]{40}',commit):raise SystemExit('Expected full pushed commit SHA')
repo='tommi0503/skills-introduction-to-github';folder='rhetis-collections-20261023'
local=Path('/workspace/skills-introduction-to-github')/folder
downloads=Path('/workspace/work/downloaded')/commit;downloads.mkdir(parents=True,exist_ok=True)
names=[n+s+'.zip' for n in ['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse'] for s in ['','-review']]
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while chunk:=f.read(1024*1024):h.update(chunk)
 return h.hexdigest()
def verify(name):
 url=f'https://raw.githubusercontent.com/{repo}/{commit}/{folder}/{name}';target=downloads/name
 with urlopen(Request(url,headers={'User-Agent':'Rhetis-delivery-verification'}),timeout=120) as response,target.open('wb') as f:
  while chunk:=response.read(1024*1024):f.write(chunk)
 remote_sha=digest(target);expected=digest(local/name)
 if remote_sha!=expected:raise RuntimeError(name+': downloaded SHA256 mismatch')
 with zipfile.ZipFile(target) as z:
  bad=z.testzip()
  if bad:raise RuntimeError(name+': corrupt ZIP member '+bad)
  count=len(z.namelist())
 print(name,target.stat().st_size,'SHA256 and CRC OK',flush=True)
 return {'file':name,'download_url':url,'bytes':target.stat().st_size,'sha256':remote_sha,'matches_committed_source':True,'zip_members':count,'testzip':None}
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(verify,names))
result={'repo':repo,'artifact_commit':commit,'verified_at_utc':datetime.now(timezone.utc).isoformat(),'method':'Actual HTTPS download from immutable pushed commit; SHA256 compared with local committed ZIP; all member CRCs checked.','all_passed':True,'files':records}
(local/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Verified',len(records),'published ZIPs; verification.json written',flush=True)
