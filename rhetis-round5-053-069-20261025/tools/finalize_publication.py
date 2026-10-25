"""Verify every published remote source path and blob identity."""
import hashlib,json,time
from publish_api import ROOT,PREFIX,api

def main():
 pub=json.loads((ROOT/'publication.json').read_text());manifest=json.loads((ROOT/'publication-upload-manifest.json').read_text());expected={r['path'][len(PREFIX)+1:]:r['sha']for r in manifest}
 root=api('GET','/git/commits/'+pub['commit'])['tree']['sha'];row=next(x for x in api('GET','/git/trees/'+root)['tree']if x['path']==PREFIX);remote=api('GET','/git/trees/'+row['sha']+'?recursive=1');assert not remote.get('truncated');actual={r['path']:r['sha']for r in remote['tree']if r['type']=='blob'};assert actual==expected,'Remote source tree differs'
 proof={'commit':pub['commit'],'files':len(actual),'remoteTree':row['sha'],'manifestSHA256':hashlib.sha256((ROOT/'publication-upload-manifest.json').read_bytes()).hexdigest(),'result':'pass','method':'Actual remote recursive tree; every published source path and blob identity matches the uploaded local manifest.'};(ROOT/'publication-source-verification.json').write_text(json.dumps(proof,indent=2));print('Remote source paths and blob IDs verified:',len(actual),flush=True)
 print('Source verification complete',pub['commit'],flush=True)
if __name__=='__main__':main()
