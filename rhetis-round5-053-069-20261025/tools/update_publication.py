"""Publish the verified portable-font correction through non-forced HTTPS APIs."""
import base64,hashlib,json,time
from publish_api import ROOT,REPO,PREFIX,api,current,oid

def main():
 pub=json.loads((ROOT/'publication.json').read_text());manifest=json.loads((ROOT/'publication-upload-manifest.json').read_text());old={r['path']:r for r in manifest};portable=json.loads((ROOT/'publication-portable-verification.json').read_text());assert sum(x['extractedPagesPixelIdentical']for x in portable['collections'])==95
 paths=['current-fold-review.zip','artifacts.json','SHA256SUMS','tools/package_release.py','tools/verify_portable.py','tools/publish_verification.py','tools/update_publication.py'];entries=[]
 for name in paths:
  data=(ROOT/name).read_bytes();sha=oid(data);path=PREFIX+'/'+name
  if name.endswith('.zip'):
   result=api('POST','/git/blobs',{'encoding':'base64','content':base64.b64encode(data).decode()});assert result['sha']==sha;entries.append({'path':path,'mode':'100644','type':'blob','sha':sha})
  else:entries.append({'path':path,'mode':'100644','type':'blob','content':data.decode()})
  old[path]={'path':path,'mode':'100644','type':'blob','sha':sha}
 for attempt in range(3):
  parent=current();tree=api('GET','/git/commits/'+parent)['tree']['sha'];newtree=api('POST','/git/trees',{'base_tree':tree,'tree':entries});commit=api('POST','/git/commits',{'message':'Include the JSON-declared signature font in portable Rhetis review ZIP','tree':newtree['sha'],'parents':[parent]})
  if current()!=parent:continue
  ref=api('PATCH','/git/refs/heads/main',{'sha':commit['sha'],'force':False});assert ref['object']['sha']==commit['sha'];pub.update({'initialCommit':pub.get('initialCommit',pub['commit']),'parent':parent,'commit':commit['sha'],'tree':newtree['sha'],'files':len(old),'updatedUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'sourceURL':'https://github.com/'+REPO+'/tree/'+commit['sha']+'/'+PREFIX});(ROOT/'publication.json').write_text(json.dumps(pub,ensure_ascii=False,indent=2));(ROOT/'publication-upload-manifest.json').write_text(json.dumps(list(old.values()),ensure_ascii=False,indent=2));print('PUBLISHED portable-font correction',commit['sha'],flush=True);return
 raise RuntimeError('Main advanced repeatedly; ref was not changed')
if __name__=='__main__':main()
