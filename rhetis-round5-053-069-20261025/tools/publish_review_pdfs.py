"""Publish only PDF review additions, preserving the latest repository tree."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import base64,concurrent.futures,hashlib,json,urllib.parse
from publish_api import ROOT,REPO,PREFIX,api,current,oid

def main():
 out=ROOT/'pdfs';m=json.loads((out/'manifest.json').read_text());v=json.loads((out/'verification.json').read_text());assert v['status']=='pass'and v['totals']=={'fullSheets':435,'samples':3448,'pagesRendered':2151}
 # Documentation describes the readable detail pages and original-resolution sheets.
 lines=['# 전체 요소 PDF 검수 시트','','141개 요소 디자인과 foundation 패널의 전체 시트435장, 크기·모드 샘플3448개를 담았습니다. 전체2151페이지입니다.','','각 PDF에는 요소별 책갈피와 클릭 가능한 목록, 라이트·다크 전체 시트, fixture별 A3 확대 페이지, replica 대조 시트가 있습니다. 전체 시트는 원본 해상도를 보존하므로 확대해서 볼 수 있습니다. `MIN`은 fixture의 최소 칸입니다.','','| 덱 | 컬렉션 | PDF | 페이지 | 크기 |','|---|---|---|---:|---:|']
 cs=json.loads((ROOT/'collections.json').read_text());codes={c['id']:str(c.get('deck',c.get('number','')))for c in cs};codes=dict(zip([c['id']for c in cs],['053','054','055','056','058','067','069']))
 for c in m['collections']:lines.append('| '+codes[c['collection']]+' | '+c['collection']+' | [다운로드]('+Path(c['pdf']).name+') | '+str(c['pages'])+' | '+f"{c['bytes']/1048576:.2f} MiB"+' |')
 lines+=['','검증: 모든 PDF 페이지를 실제 렌더했고, 전체435개 시트의 포함 이미지 픽셀을 원본 PNG와 비교했습니다. 모든 fixture·모드·크기 조합, 확대 영역의 잘림·겹침, 내부 링크를 검사했습니다. 자세한 결과는 [verification.json](verification.json), 출처와 페이지 위치는 [manifest.json](manifest.json)에 있습니다.','','이 PDF는 기존 최종 PNG에서 생성했습니다. 기존 replica와 요소 CSS, fixture를 변경하지 않았습니다.','','재생성:','', '```bash','python tools/build_review_pdfs.py','python tools/verify_review_pdfs.py','```','']
 (out/'README.md').write_text('\n'.join(lines))
 files=[p for p in out.rglob('*')if p.is_file()and p.suffix in ['.pdf','.json','.md','.png']and not p.name.startswith(('publication','download'))]
 files +=[ROOT/'tools'/n for n in ['build_review_pdfs.py','verify_review_pdfs.py','publish_review_pdfs.py','verify_pdf_downloads.py']]
 for p in files:assert p.exists()
 entries=[]
 def upload(p):
  data=p.read_bytes();rel=str(p.relative_to(ROOT));sha=oid(data)
  if p.suffix in ['.pdf','.png']:
   result=api('POST','/git/blobs',{'content':base64.b64encode(data).decode(),'encoding':'base64'});assert result['sha']==sha;entry={'path':PREFIX+'/'+rel,'mode':'100644','type':'blob','sha':sha}
  else:entry={'path':PREFIX+'/'+rel,'mode':'100644','type':'blob','content':data.decode()}
  print('Prepared',rel,len(data),flush=True);return entry
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:entries=list(pool.map(upload,files))
 for attempt in range(3):
  parent=current();base=api('GET','/git/commits/'+parent)['tree']['sha'];changes=list(entries)
  # Fetch and amend the current versions so concurrent unrelated work is retained.
  for name in ['README.md','index.html','requirements.txt']:
   remote=api('GET','/contents/'+PREFIX+'/'+name+'?ref='+parent);text=base64.b64decode(remote['content']).decode()
   if name=='README.md':
    line='[전체 요소 PDF 검수 시트 — 7개 컬렉션](pdfs/README.md)'
    if line not in text:text+='\n\n'+line+'\n'
   elif name=='index.html':
    block='<section id="element-review-pdfs"><h2>전체 요소 PDF 검수 시트</h2><p>라이트·다크·replica 대조와 fixture 크기별 확대 페이지입니다.</p><ul>'+''.join('<li><a href="'+c['pdf']+'">'+c['collection']+' — '+str(c['pages'])+'페이지 PDF</a></li>'for c in m['collections'])+'</ul></section>'
    if 'id="element-review-pdfs"'not in text:text=text.replace('</h1>','</h1>'+block,1)
   elif not any(x.strip().lower().startswith('pymupdf')for x in text.splitlines()):text=text.rstrip()+'\nPyMuPDF>=1.26\n'
   changes.append({'path':PREFIX+'/'+name,'mode':'100644','type':'blob','content':text})
  tree=api('POST','/git/trees',{'base_tree':base,'tree':changes});commit=api('POST','/git/commits',{'message':'Add complete element review PDFs with every fixture size and replica comparison','tree':tree['sha'],'parents':[parent]})
  if current()!=parent:print('Main advanced; preserving latest parent',flush=True);continue
  ref=api('PATCH','/git/refs/heads/main',{'sha':commit['sha'],'force':False});assert ref['object']['sha']==commit['sha']
  report={'commit':commit['sha'],'parent':parent,'repository':REPO,'prefix':PREFIX,'sourceURL':'https://github.com/'+REPO+'/tree/'+commit['sha']+'/'+PREFIX+'/pdfs','publishedKST':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),'method':'GitHub HTTPS API; latest tree and parent preserved; non-forced ref update; no git commands.','pdfs':[{'collection':c['collection'],'path':c['pdf'],'pages':c['pages'],'bytes':c['bytes'],'sha256':c['sha256'],'url':'https://raw.githubusercontent.com/'+REPO+'/'+commit['sha']+'/'+PREFIX+'/'+c['pdf']}for c in m['collections']]};(out/'publication.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('PUBLISHED PDF REVIEW',commit['sha'],flush=True);return
 raise RuntimeError('Concurrent main updates prevented publication; no forced update attempted')
if __name__=='__main__':main()
