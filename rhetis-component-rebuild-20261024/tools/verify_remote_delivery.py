from pathlib import Path
import argparse,json,hashlib,zipfile,urllib.request,time,subprocess
p=argparse.ArgumentParser();p.add_argument('--base',required=True);p.add_argument('--ref',required=True);a=p.parse_args();base=Path(a.base);m=json.loads((base/'delivery-validation.json').read_text());out=Path('/workspace/work/download-verified');out.mkdir(exist_ok=True);rows=[]
for z in m['zips']:
 host='https://media.githubusercontent.com/media/' if z.get('gitStorage')=='lfs' else 'https://raw.githubusercontent.com/'
 url=host+'tommi0503/skills-introduction-to-github/'+a.ref+'/'+base.name+'/'+z['file']
 target=out/z['file']
 subprocess.run(['curl','--fail','--location','--retry','3','--retry-all-errors','--max-time','600','--connect-timeout','15','--silent','--show-error','--output',str(target),url],check=True)
 digest=hashlib.sha256(target.read_bytes()).hexdigest();assert digest==z['sha256'],z['file']
 with zipfile.ZipFile(target) as archive:assert archive.testzip() is None
 rows.append({'file':z['file'],'url':url,'bytes':target.stat().st_size,'sha256':digest,'sha256Matches':True,'zipIntegrity':'pass'});print(z['file'],'verified',flush=True)
(base/'github-download-verification.json').write_text(json.dumps({'ref':a.ref,'downloads':rows,'allVerified':True},ensure_ascii=False,indent=2))
