"""Download the published archive bytes, check SHA-256, ZIP CRC and required root layout."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import sys,json,hashlib,urllib.request,zipfile,time
from package import ROOT,DEST
commit=sys.argv[1]
manifest=json.loads((DEST/'archive-manifest.json').read_text())
work=ROOT/'github-redownload';work.mkdir(exist_ok=True)
def verify(entry,kid):
 name=entry['file'];url=f'https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/{commit}/rhetis-part07-069-078/downloads/{name}';path=work/name
 with urllib.request.urlopen(url,timeout=180) as res,path.open('wb') as out:
  while chunk:=res.read(1024*1024):out.write(chunk)
 digest=hashlib.sha256(path.read_bytes()).hexdigest();assert digest==entry['sha256'],name
 assert path.stat().st_size==entry['bytes'],name
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None,name
  if name==kid+'.zip':assert {n.split('/')[0] for n in z.namelist()}=={kid}
  else:
   for folder in ['replica/','compare-replica/','library/','reassembled/','compare-reassembled/']:
    assert any(n.startswith(folder) for n in z.namelist()),(name,folder)
 result={'file':name,'url':url,'bytes':path.stat().st_size,'sha256':digest,'zipCRC':'pass','publishedCommit':commit};print(name,'download+SHA256+CRC PASS',flush=True);return result
jobs=[(e,m['collection']) for m in manifest for e in m['archives']]
results=[]
with ThreadPoolExecutor(max_workers=2) as pool:
 futures=[pool.submit(verify,e,k) for e,k in jobs]
 for f in as_completed(futures):results.append(f.result())
report={'repository':'tommi0503/skills-introduction-to-github','publishedCommit':commit,'verifiedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'archives':sorted(results,key=lambda x:x['file']),'allPassed':len(results)==10}
(DEST/'github-download-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('ALL TEN ARCHIVES VERIFIED',flush=True)
