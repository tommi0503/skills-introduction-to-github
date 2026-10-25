#!/usr/bin/env python3
"""Publish the exact ten authorized ZIPs on this repository's Round5 release.
No Git commands. A draft is published only after every asset is verified.
Existing releases/assets are preserved; conflicting bytes are never overwritten.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,os,urllib.request,urllib.error,time
ROOT=Path(__file__).resolve().parents[1];REPO='tommi0503/skills-introduction-to-github';TAG='rhetis-round5-20261025';API='https://api.github.com/repos/'+REPO
NAMES=[k+s for k in['vectorbox','seedmark','crossrail','meridian-deck','onboard-docket']for s in['.zip','-review.zip']]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def request(method,url,body=None,raw=False):
 data=body if raw else json.dumps(body).encode()if body is not None else None
 q=urllib.request.Request(url,data=data,method=method,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'Rhetis-round5-artifact-publisher','Content-Type':'application/zip'if raw else'application/json'})
 with urllib.request.urlopen(q,timeout=300)as response:return json.load(response)
def run(commit):
 pub=json.loads((ROOT/'api-publication.json').read_text());assert pub['commitSHA']==commit
 final=json.loads((ROOT/'integration-verification.json').read_text());assert not final['errors']and final['status']=='verified-with-recorded-candidates'
 sums={line.split('  ')[1]:line.split('  ')[0]for line in(ROOT/'deliverables/SHA256SUMS').read_text().splitlines()};assert set(sums)==set(NAMES)
 payloads={n:(ROOT/'deliverables'/n).read_bytes()for n in NAMES};assert all(hashlib.sha256(b).hexdigest()==sums[n]for n,b in payloads.items())
 releases=request('GET',API+'/releases?per_page=100');same=[x for x in releases if x['tag_name']==TAG];assert len(same)<=1
 if same:release=same[0];assert release['target_commitish']==commit,'Existing tag belongs to a different source commit; preserve it'
 else:release=request('POST',API+'/releases',{'tag_name':TAG,'target_commitish':commit,'name':'Rhetis ROUND5 · 5개 컬렉션 / 159개 실제 디자인','draft':True,'prerelease':False,'body':'불변 replica에서 다시 만든 반응형 디자인 라이브러리입니다. 5개 덱112장,159개 디자인,444개 fixture,크기 칸5326개와panel128개를 검수했습니다.\n\n소스와 요소별 출처: https://github.com/'+REPO+'/tree/'+commit+'/rhetis-round5\n\n컬렉션 ZIP은 CSS·JSON·MD·HTML만 포함합니다. 검수 ZIP에는 map,라이트·다크 크기 시트,원형 대조,조립본과3열 비교,로컬 폰트,검수 증거가 있습니다. 큰 검수 ZIP은 GitHub blob API 크기 제한으로 이 Release에 정확한 원본 바이트로 게시합니다.\n\n잔여 GAP: Seedmark20 단일 누적 막대(계약 최소2개)와Meridian14 연속15점 면 차트(계약 최대12개). SHA256SUMS와 manifest는 소스의deliverables에 있습니다.'})
 report={'schema':'rhetis.release-publication/1','startedAtUTC':now(),'repository':REPO,'tag':TAG,'sourceCommit':commit,'releaseId':release['id'],'url':release['html_url'],'status':'uploading','gitCommandsUsed':False,'assets':[]}
 def save():(ROOT/'release-publication.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 save();assets={x['name']:x for x in request('GET',API+'/releases/'+str(release['id'])+'/assets?per_page=100')}
 for n,b in payloads.items():
  if n in assets:
   asset=assets[n];assert asset['size']==len(b),'Existing asset has different bytes; no overwrite allowed'
   assert asset.get('digest')=='sha256:'+sums[n],'Existing asset digest cannot establish equality; preserve it'
  else:asset=request('POST',release['upload_url'].split('{')[0]+'?name='+n,b,True)
  assert asset['size']==len(b)
  if asset.get('digest'):assert asset['digest']=='sha256:'+sums[n]
  report['assets'].append({'name':n,'bytes':len(b),'sha256':sums[n],'id':asset['id'],'serverDigest':asset.get('digest'),'downloadURL':asset['browser_download_url']});save();print(n,'uploaded exact',len(b),'bytes',flush=True)
 actual=request('GET',API+'/releases/'+str(release['id'])+'/assets?per_page=100');assert set(NAMES)=={x['name']for x in actual},'Unexpected asset set; preserve draft for review'
 published=request('PATCH',API+'/releases/'+str(release['id']),{'draft':False})if release['draft']else release
 report.update(status='published-awaiting-actual-download',publishedAtUTC=now(),url=published['html_url']);save();print('Published release',published['html_url'],flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('commit');v=a.parse_args();assert len(v.commit)==40;run(v.commit)
