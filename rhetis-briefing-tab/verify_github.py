from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import urllib.request,json,hashlib,zipfile,subprocess
ROOT=Path(__file__).resolve().parent;repo=ROOT.parent;commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip();expected=json.loads((repo/'rhetis-briefing-tab/archive-verification.json').read_text());dest=ROOT/'downloaded-github';dest.mkdir(exist_ok=True)
def verify(pair):
 kind,exp=pair;url=f'https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/{commit}/{exp["name"]}';p=dest/exp['name'];h=hashlib.sha256()
 with urllib.request.urlopen(url,timeout=60)as response,open(p,'wb')as f:
  status=response.status
  while True:
   chunk=response.read(1024*1024)
   if not chunk:break
   f.write(chunk);h.update(chunk)
 with zipfile.ZipFile(p)as z:
  corrupt=z.testzip();entries=len(z.namelist())
  if kind=='collection':assert sorted(set(x.split('/')[0]for x in z.namelist()))==['briefing-tab']
 assert status==200 and h.hexdigest()==exp['sha256'] and p.stat().st_size==exp['bytes'] and corrupt is None and entries==exp['entries']
 return {'archive':exp['name'],'url':url,'http_status':status,'bytes':p.stat().st_size,'sha256':h.hexdigest(),'expected_sha256':exp['sha256'],'sha256_matches':True,'zip_crc':'pass','entries':entries}
with ThreadPoolExecutor(max_workers=2)as pool:results=list(pool.map(verify,expected.items()))
report={'repository':'tommi0503/skills-introduction-to-github','artifact_commit':commit,'verified_at_utc':datetime.now(timezone.utc).isoformat(),'download_method':'HTTPS GET from raw.githubusercontent.com after push; ZIP bytes re-downloaded, hashed and CRC-tested','results':results,'all_passed':True}
(repo/'rhetis-briefing-tab/github-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
