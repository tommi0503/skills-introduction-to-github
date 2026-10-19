from pathlib import Path
import json,hashlib,zipfile,urllib.request,sys,datetime
root=Path(__file__).resolve().parent.parent
commit=sys.argv[1]
assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
target=Path('/workspace/work/rhetis/github-downloads');target.mkdir(parents=True,exist_ok=True)
entries=json.loads((root/'downloads/checksums.json').read_text());results=[]
for e in entries:
 url=f'https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/{commit}/rhetis-spectrum-04/downloads/{e["file"]}'
 request=urllib.request.Request(url,headers={'User-Agent':'Rhetis-Artifact-Verification/1.0'})
 dest=target/e['file'];digest=hashlib.sha256();total=0
 with urllib.request.urlopen(request,timeout=120) as r,dest.open('wb') as f:
  status=r.status
  while chunk:=r.read(1024*1024):f.write(chunk);digest.update(chunk);total+=len(chunk)
 assert status==200 and total==e['bytes'] and digest.hexdigest()==e['sha256'],e['file']
 with zipfile.ZipFile(dest) as z:
  assert z.testzip() is None
  if 'collection' in e['file']:assert all(n.startswith('spectrum-04/') for n in z.namelist())
  members=len(z.namelist())
 results.append({'file':e['file'],'url':url,'httpStatus':status,'bytes':total,'sha256':digest.hexdigest(),'sha256Matches':True,'zipCrc':'pass','members':members})
 print(e['file'],total,'bytes / SHA256 and ZIP CRC pass',flush=True)
report={'commit':commit,'checkedAt':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat(),'results':results}
(root/'review/github-download-verification.json').write_text(json.dumps(report,indent=2)+'\n')
