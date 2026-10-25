#!/usr/bin/env python3
"""Source-only requested archive. No image, PDF, font or nested archive bytes."""
from pathlib import Path
import datetime,hashlib,json,zipfile
from publish_api import ROOT,inventory
ALLOW={'.css','.json','.md','.html','.py','.js','.txt'}
def run():
 rows=inventory();chosen=[]
 for r in rows:
  p=ROOT/r['path']
  if p.suffix.lower()not in ALLOW:continue
  if p.name in {'source-zip-verification.json','source-zip-publication.json','publication-verification.json'}:continue
  # Download manifests refer to separately delivered binary artifacts and stay
  # outside this archive; source/contract/data/verification text is retained.
  if r['path'].startswith('deliverables/'):continue
  chosen.append({'path':r['path'],'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 manifest={'schema':'rhetis.source-only/1','createdAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':'rhetis-round5-source','allowedExtensions':sorted(ALLOW),'excluded':'All images (including SVG), PDF, fonts, archives, native render caches, credentials and temporary authoring generators.','collectionCount':5,'designCount':159,'files':chosen}
 out=ROOT/'deliverables/rhetis-round5-source.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
  for r in chosen:z.write(ROOT/r['path'],'rhetis-round5-source/'+r['path'])
  z.writestr('rhetis-round5-source/SOURCE-MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
  z.writestr('rhetis-round5-source/SOURCE-ONLY.md','# 소스 전용 ZIP\n\n요청에 따라 이미지·PDF·폰트·기타 바이너리는 포함하지 않았습니다. 컬렉션 CSS/HTML/JSON, replica·조립 HTML, 디자인 지도·문서·검수 JSON과 빌드/검수 스크립트가 들어 있습니다. 렌더링에 필요한 폰트·이미지 등은 별도 검수 자료의 원래 상대 경로에 복원해 사용합니다. 각 파일의 SHA는 SOURCE-MANIFEST.json에 있습니다.\n')
 with zipfile.ZipFile(out)as z:
  assert z.testzip()is None
  assert{p.split('/')[0]for p in z.namelist()}=={'rhetis-round5-source'}
  assert all(Path(p).suffix.lower()in ALLOW for p in z.namelist())
  for r in chosen:assert hashlib.sha256(z.read('rhetis-round5-source/'+r['path'])).hexdigest()==r['sha256']
 report={'artifact':out.name,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'files':len(chosen)+2,'sourceFiles':len(chosen),'excludedBinaryEntries':0,'CRC':'passed','SHA':'passed','extensions':sorted(ALLOW)}
 (ROOT/'source-zip-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':run()
