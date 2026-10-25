"""Stream the 14 unchanged ZIPs to a draft repository Release over HTTPS."""
from pathlib import Path
import concurrent.futures,hashlib,json,urllib.request,urllib.error,urllib.parse
from publish_api import ROOT,REPO,PREFIX,HEADERS,api,current,oid

def main():
 # Check every non-ZIP binary uploaded before the JSON request-size failure.
 extensions={'.png','.pdf','.woff','.woff2'};shas=sorted({oid(p.read_bytes())for p in ROOT.rglob('*')if p.is_file()and p.suffix in extensions and not any(x.startswith('.')or x=='__pycache__'for x in p.relative_to(ROOT).parts)})
 validation_trees=[]
 for start in range(0,len(shas),100):
  batch=shas[start:start+100];checked=api('POST','/git/trees',{'tree':[{'path':sha,'mode':'100644','type':'blob','sha':sha}for sha in batch]})
  assert {r['sha']for r in checked['tree']}==set(batch);validation_trees.append(checked['sha']);print('Verified existing binary batch',start+len(batch),'/',len(shas),flush=True)
 (ROOT/'publication-binary-cache.json').write_text(json.dumps({'sha':shas,'validationTrees':validation_trees}));print('Existing binary objects verified:',len(shas),flush=True)
 releases=api('GET','/releases?per_page=100');release=next((r for r in releases if r['tag_name']==PREFIX),None)
 if release is None:release=api('POST','/releases',{'tag_name':PREFIX,'target_commitish':current(),'name':'Rhetis Round 5 — 기업 덱 7개 컬렉션','body':'기존 replica를 보존하고 원본 요소 수치에서 다시 만든141개 디자인입니다. 크기/모드3448상태, 시트435장, 조립95페이지를 검수했습니다. 각 컬렉션 ZIP과 검수 ZIP을 함께 제공합니다. 소스와 개별 출처는 저장소의 `'+PREFIX+'` 폴더를 확인하세요.','draft':True,'prerelease':False})
 assert release['draft'],'Refuse to modify a previously published release'
 artifacts=json.loads((ROOT/'artifacts.json').read_text());existing={x['name']:x for x in api('GET','/releases/'+str(release['id'])+'/assets?per_page=100')};upload=release['upload_url'].split('{')[0]
 def send(item):
  if item['name']in existing:
   result=existing[item['name']];assert result['size']==item['bytes']and result.get('digest')=='sha256:'+item['sha256']
  else:
   headers={**HEADERS,'Content-Type':'application/zip'};data=(ROOT/item['name']).read_bytes();assert hashlib.sha256(data).hexdigest()==item['sha256']
   req=urllib.request.Request(upload+'?'+urllib.parse.urlencode({'name':item['name']}),data,headers,method='POST')
   try:
    with urllib.request.urlopen(req,timeout=300)as r:result=json.load(r)
   except urllib.error.HTTPError as e:raise RuntimeError(item['name']+' HTTP '+str(e.code)+' '+e.read(1200).decode())from None
  assert result['size']==item['bytes']and result['state']=='uploaded'
  if result.get('digest'):assert result['digest']=='sha256:'+item['sha256']
  print('Release asset uploaded:',item['name'],result['size'],flush=True)
  return{**item,'assetID':result['id'],'url':result['browser_download_url'],'releaseTag':PREFIX}
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:results=list(pool.map(send,artifacts))
 (ROOT/'artifacts.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 report={'releaseID':release['id'],'tag':PREFIX,'url':release['html_url'],'draft':True,'assets':results};(ROOT/'publication-release.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 for name in ['README.md','index.html']:
  p=ROOT/name;s=p.read_text()
  for item in results:s=s.replace('('+item['name']+')','('+item['url']+')').replace('href="'+item['name']+'"','href="'+item['url']+'"')
  p.write_text(s)
 print('Prepared draft release:',release['id'],'assets:',len(results),flush=True)
if __name__=='__main__':main()
