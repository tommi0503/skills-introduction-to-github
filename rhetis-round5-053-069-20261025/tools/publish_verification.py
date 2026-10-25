"""Attach actual HTTPS download evidence without executing git commands."""
from pathlib import Path
import json,time
from publish_api import ROOT,REPO,PREFIX,api,current

def main():
 release=json.loads((ROOT/'publication.json').read_text());downloads=json.loads((ROOT/'download-verification.json').read_text());artifacts=json.loads((ROOT/'artifacts.json').read_text())
 assert release['commit']==downloads['commit']and len(downloads['files'])==len(artifacts)==14
 assert all(x['crc']=='pass'for x in downloads['files'])
 entries=[{'path':PREFIX+'/'+name,'mode':'100644','type':'blob','content':(ROOT/name).read_text()}for name in ['publication.json','download-verification.json','publication-upload-manifest.json','tools/publish_verification.py','publication-source-verification.json','publication-portable-verification.json','tools/verify_portable.py']]
 for attempt in range(3):
  parent=current();tree=api('GET','/git/commits/'+parent)['tree']['sha'];newtree=api('POST','/git/trees',{'base_tree':tree,'tree':entries})
  commit=api('POST','/git/commits',{'message':'Record independently downloaded Rhetis round 5 ZIP verification','tree':newtree['sha'],'parents':[parent]})
  if current()!=parent:continue
  ref=api('PATCH','/git/refs/heads/main',{'sha':commit['sha'],'force':False});assert ref['object']['sha']==commit['sha'];report={'releaseCommit':release['commit'],'verificationCommit':commit['sha'],'method':'HTTPS API, non-forced fast-forward from latest main parent','url':'https://github.com/'+REPO+'/tree/'+commit['sha']+'/'+PREFIX};(ROOT/'publication-proof.json').write_text(json.dumps(report,indent=2));print(json.dumps(report));return
 raise RuntimeError('Main advanced repeatedly; proof ref not changed')
if __name__=='__main__':main()
