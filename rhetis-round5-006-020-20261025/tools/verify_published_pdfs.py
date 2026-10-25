"""Re-download all fourteen published review PDFs and verify their content."""
from pathlib import Path
import argparse,hashlib,json,tempfile,time,urllib.request
import fitz

ROOT=Path('/workspace/work/round5-delivery-20261025')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('commit');args=ap.parse_args()
    source=json.loads((ROOT/'element-review-pdfs/verification.json').read_text())
    assert len(source['pdfs'])==14 and source['uniqueElements']==135
    out=ROOT/'element-review-pdfs/github-download-verification.json'
    result={'repository':'tommi0503/skills-introduction-to-github','commit':args.commit,'elements':135,'files':[],'passed':False}
    if out.exists():
        old=json.loads(out.read_text())
        if old.get('commit')==args.commit:result['files']=old.get('files',[])
    done={x['file']for x in result['files']}
    for item in source['pdfs']:
        if item['file']in done:continue
        url='https://media.githubusercontent.com/media/tommi0503/skills-introduction-to-github/'+args.commit+'/rhetis-round5-006-020-20261025/'+item['file']
        for attempt in range(3):
            try:
                with tempfile.TemporaryDirectory(prefix='rhetis-pdf-github-',dir='/tmp')as temp:
                    p=Path(temp)/Path(item['file']).name;digest=hashlib.sha256();count=0
                    req=urllib.request.Request(url,headers={'User-Agent':'Rhetis-PDF-review-verification/1.0'})
                    with urllib.request.urlopen(req,timeout=120)as response,p.open('wb')as target:
                        assert response.status==200,response.status
                        while True:
                            chunk=response.read(1024*1024)
                            if not chunk:break
                            target.write(chunk);digest.update(chunk);count+=len(chunk)
                    assert count==item['bytes'],('bytes',item['file'],count)
                    assert digest.hexdigest()==item['sha256'],('SHA256',item['file'])
                    with fitz.open(p)as doc:
                        assert len(doc)==item['pages'],('pages',item['file'],len(doc))
                        bookmarks=len(doc.get_toc())
                        if item['collection']=='all':assert len(doc)==155 and bookmarks==161
                    row={'file':item['file'],'url':url,'bytes':count,'sha256':digest.hexdigest(),'sha256Match':True,'pages':item['pages'],'bookmarks':bookmarks,'download':'pass','pdf':'pass'}
                result['files'].append(row);out.write_text(json.dumps(result,ensure_ascii=False,indent=2))
                print('PASS',len(result['files']),'/14',Path(item['file']).name,item['pages'],'pages',flush=True)
                break
            except Exception as exc:
                print('Retry',attempt+1,Path(item['file']).name,type(exc).__name__,getattr(exc,'code',''),flush=True)
                if attempt==2:raise
                time.sleep(3)
    result['passed']=len(result['files'])==14
    assert result['passed'];out.write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print('All14 published PDFs downloaded and verified.',flush=True)
if __name__=='__main__':main()
