#!/usr/bin/env python3
"""Actually re-download the 10ZIPs, 11PDFs and source-only ZIP at one Git commit.
Public HTTPS only. Preserve inherited proxy and CA trust. Never read credentials.
"""
from pathlib import Path
import argparse,datetime,hashlib,importlib.util,json,re,ssl,sys,tempfile,urllib.request,zipfile
import fitz
ROOT=Path(__file__).resolve().parents[1];REPO='tommi0503/skills-introduction-to-github';PREFIX='rhetis-round5'
H=lambda b:hashlib.sha256(b).hexdigest()
def run(commit):
 assert re.fullmatch('[0-9a-f]{40}',commit)
 spec=importlib.util.spec_from_file_location('delivery_package',ROOT/'tools/package.py');pkg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pkg;spec.loader.exec_module(pkg)
 expected=[]
 for line in(ROOT/'deliverables/SHA256SUMS').read_text().splitlines():
  sha,name=line.split('  ');expected.append({'path':'deliverables/'+name,'sha256':sha,'kind':'collection'if not name.endswith('-review.zip')else'review'})
 pdf=json.loads((ROOT/'pdf-verification.json').read_text())
 for row in pdf['pdfs']:expected.append({'path':row['downloadPath'],'sha256':row['sha256'],'kind':'pdf','pages':row['pages']})
 src=json.loads((ROOT/'source-zip-verification.json').read_text());expected.append({'path':'deliverables/'+src['artifact'],'sha256':src['sha256'],'kind':'source'})
 assert len(expected)==22
 out=Path(tempfile.mkdtemp(prefix='rhetis-round5-downloaded-',dir='/tmp'));report={'schema':'rhetis.final-public-download/1','commit':commit,'repository':REPO,'status':'verifying','startedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'expectedArtifacts':22,'directory':str(out),'networkAuthentication':'Public HTTPS, configured proxy and CA, no token or cookies','artifacts':[],'errors':[]}
 opener=urllib.request.build_opener(urllib.request.ProxyHandler(),urllib.request.HTTPSHandler(context=ssl.create_default_context()))
 def save():(ROOT/'final-download-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 save()
 for item in expected:
  local=ROOT/item['path'];assert H(local.read_bytes())==item['sha256'];url='https://raw.githubusercontent.com/'+REPO+'/'+commit+'/'+PREFIX+'/'+item['path'];target=out/Path(item['path']).name;h=hashlib.sha256();n=0
  try:
   with opener.open(urllib.request.Request(url,headers={'User-Agent':'Rhetis-final-public-download-verifier'}),timeout=120)as response,target.open('wb')as stream:
    assert response.status==200
    while chunk:=response.read(1024*1024):stream.write(chunk);h.update(chunk);n+=len(chunk)
   assert n==local.stat().st_size and h.hexdigest()==item['sha256']
   row={**item,'url':url,'bytes':n,'downloadedSHA256':h.hexdigest(),'status':'verified'}
   if item['kind']in['collection','review']:
    checked=pkg.verify_zip(target);assert checked['crc']=='passed';row.update(zipCRC=checked['crc'],zipEntries=checked['entryCount'],pngCount=len(checked['pngDimensions']),topFolder=checked['topFolder'])
   elif item['kind']=='source':
    with zipfile.ZipFile(target)as z:
     assert z.testzip()is None;assert{p.split('/')[0]for p in z.namelist()}=={'rhetis-round5-source'};assert all(Path(p).suffix in{'.css','.html','.js','.json','.md','.py','.txt'}for p in z.namelist());row.update(zipCRC='passed',zipEntries=len(z.namelist()),binaryEntries=0)
   else:
    with fitz.open(target)as doc:assert doc.page_count==item['pages'];row['PDFPages']=doc.page_count
   report['artifacts'].append(row);print(Path(item['path']).name,n,'bytes exact /',item['kind'],'passed',flush=True)
  except Exception as e:report['errors'].append({'path':item['path'],'error':str(e)});print('FAILED',item['path'],type(e).__name__,str(e),flush=True)
  save()
 report.update(status='verified'if not report['errors']and len(report['artifacts'])==22 else'failed',completedAtUTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),verifiedArtifacts=len(report['artifacts']),verifiedZIPs=sum(x['kind']in['review','collection']for x in report['artifacts']),verifiedPDFs=sum(x['kind']=='pdf'for x in report['artifacts']),verifiedSourceZIPs=sum(x['kind']=='source'for x in report['artifacts']));save();return 0 if report['status']=='verified'else 1
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('commit');v=a.parse_args();raise SystemExit(run(v.commit))
