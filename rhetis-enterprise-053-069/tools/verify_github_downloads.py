from pathlib import Path
import concurrent.futures,hashlib,zipfile,json,subprocess,time,io,tempfile
from PIL import Image
B=Path(__file__).resolve().parents[1];repo=B.parent
sha=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip();dest=Path(tempfile.mkdtemp(prefix='rhetis-github-verified-'));dest.mkdir(exist_ok=True);manifest=json.load(open(B/'downloads/manifest.json'))
def verify(row):
 name=row['file'];url=f'https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/{sha}/rhetis-enterprise-053-069/downloads/{name}';f=dest/name
 subprocess.run(['curl','--http1.1','--fail','--location','--silent','--show-error','--retry','4','--retry-delay','2','--output',str(f),url],check=True)
 actual=hashlib.sha256(f.read_bytes()).hexdigest();assert actual==row['sha256'],name+' hash mismatch';png=0;dims={};pdf=0
 with zipfile.ZipFile(f) as z:
  assert z.testzip() is None
  roots=sorted(set(n.split('/')[0] for n in z.namelist()))
  if row['kind']=='collection':assert roots==[row['collection']]
  else:
   assert all(any(n.startswith(d+'/') for n in z.namelist()) for d in ['replica','library','reassembled','compare-replica','compare-reassembled'])
  for n in z.namelist():
   if n.endswith('.png'):
    im=Image.open(io.BytesIO(z.read(n)));key='x'.join(map(str,im.size));dims[key]=dims.get(key,0)+1;png+=1
   if n.endswith('.pdf'):pdf+=1
 result={'file':name,'url':url,'bytes':f.stat().st_size,'sha256':actual,'hash_matches':True,'crc_ok':True,'root_directories':roots,'png_count':png,'png_dimensions':dims,'pdf_count':pdf};print(name,'downloaded; SHA256+CRC OK',flush=True);return result
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(verify,manifest))
report={'repository':'tommi0503/skills-introduction-to-github','downloaded_commit':sha,'zip_count':len(results),'all_sha256_match':all(r['hash_matches'] for r in results),'all_crc_ok':all(r['crc_ok'] for r in results),'files':results}
(B/'downloads/github-download-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('VERIFIED',len(results),'uploaded ZIPs')
