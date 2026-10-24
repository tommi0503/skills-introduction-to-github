"""Download the exact pushed ZIP objects and verify SHA-256, CRC and layout."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re,sys,urllib.request,zipfile
ROOT=Path('/workspace/work/rebuild')
commit=sys.argv[1]
assert re.fullmatch('[a-f0-9]{40}',commit)
repository='tommi0503/skills-introduction-to-github'
prefix='rhetis-element-rebuild-20261024'
manifest=json.loads((ROOT/'dist/release-manifest.json').read_text())
folder=ROOT/'redownloaded';folder.mkdir(exist_ok=True)
def verify(item):
 url=f'https://raw.githubusercontent.com/{repository}/{commit}/{prefix}/dist/{item["file"]}'
 path=folder/item['file'];h=hashlib.sha256();size=0
 request=urllib.request.Request(url,headers={'User-Agent':'rhetis-delivery-verifier/1'})
 with urllib.request.urlopen(request,timeout=60)as response,path.open('wb')as output:
  status=response.status
  assert status==200,(url,status)
  while chunk:=response.read(1024*1024):output.write(chunk);h.update(chunk);size+=len(chunk)
 assert size==item['bytes'],(path,'size')
 assert h.hexdigest()==item['sha256'],(path,'sha256')
 with zipfile.ZipFile(path)as archive:
  assert archive.testzip()is None,(path,'CRC')
  assert archive.namelist()==[x['path']for x in item['entries']],(path,'members')
  if not path.name.endswith('-review.zip'):
   assert {x.split('/')[0]for x in archive.namelist()}=={path.stem}
   assert all(Path(x).suffix in {'.css','.json','.md','.html'}for x in archive.namelist())
 result={'file':item['file'],'url':url,'http_status':status,'bytes':size,'sha256':h.hexdigest(),'sha256_match':True,'zip_crc':'pass','member_count':item['file_count'],'member_list_match':True,'png_count':item['png_count']}
 print(item['file'],'HTTP200 SHA256/CRC/MEMBERS=pass',flush=True)
 return result
with ThreadPoolExecutor(max_workers=3)as pool:results=list(pool.map(verify,manifest['archives']))
report={'schema':'rhetis.remote-archive-verification/1','checked_utc':datetime.now(timezone.utc).isoformat(),'repository':repository,'commit':commit,'branch':'rhetis-decks-020-030-20261023','archives':results,'archive_count':len(results),'all_passed':len(results)==14 and all(x['sha256_match']for x in results),'png_dimensions_preserved_by_identical_archive_sha256':True}
assert report['all_passed']
(ROOT/'publication-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('VERIFIED all fourteen ZIPs downloaded from pushed commit',commit,flush=True)
