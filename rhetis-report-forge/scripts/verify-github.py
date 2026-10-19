from pathlib import Path
import urllib.request,json,hashlib,zipfile,sys,time
P=Path(__file__).resolve().parent.parent
R=P.parent
commit=sys.argv[1]
out=Path('/workspace/work/report-forge-github-download');out.mkdir(parents=True,exist_ok=True)
manifest=json.loads((R/'rhetis-report-forge-archives.json').read_text());results=[]
for item in manifest:
 url=f"https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/{commit}/{item['file']}"
 dest=out/item['file']
 request=urllib.request.Request(url,headers={'User-Agent':'Report-Forge-Integrity-Check/1.0'})
 with urllib.request.urlopen(request,timeout=180) as response,dest.open('wb') as target:
  while chunk:=response.read(1024*1024):target.write(chunk)
 digest=hashlib.sha256(dest.read_bytes()).hexdigest()
 with zipfile.ZipFile(dest) as z:
  assert z.testzip() is None
  assert len(z.namelist())==item['entries']
  assert {p.split('/')[0] for p in z.namelist()}=={item['topFolder']}
 assert dest.stat().st_size==item['bytes'] and digest==item['sha256']
 results.append({**item,'downloadUrl':url,'downloadBytes':dest.stat().st_size,'downloadSHA256':digest,'matchesLocal':True})
 print(item['file'],'download verified',flush=True)
record={'repository':'tommi0503/skills-introduction-to-github','uploadedCommit':commit,'checkedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'pass':True,'archives':results}
(R/'rhetis-report-forge-github-verification.json').write_text(json.dumps(record,indent=2)+'\n')
