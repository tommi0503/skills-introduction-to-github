from pathlib import Path
from bs4 import BeautifulSoup as B
import json,re
P=Path(__file__).parent;C=P/'crossrail'
rows=json.loads((P/'qa/title-baselines-canonical.json').read_text())
f=C/'kit/css/tokens.css';f.write_text(f.read_text()+'\n.slide{--crossrail-head-offset:0px}\n')
f=C/'kit/kit.json';j=json.loads(f.read_text());j.setdefault('extensions',{})['--crossrail-head-offset']='length';f.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'\n.slide:not(.cover) .head>.title{transform:translateY(var(--crossrail-head-offset))}\n')
for r in rows:
 n=r['page'];d=r['replica_delta']
 if d:
  f=P/f'replica/slide_{n:02}.html';s=B(f.read_text(),'html.parser')
  for x in s.select('div[style]'):
   if re.search(r'font-size:(64|76)px',x['style']):x['style']=re.sub(r'top:([0-9.]+)px',lambda m:'top:'+str(float(m[1])-d).removesuffix('.0')+'px',x['style'])
  f.write_text(str(s))
 d=r['reassembled_delta']
 if d:
  f=P/f'reassembled/slide_{n:02}.html';s=B(f.read_text(),'html.parser');s.select_one('section.slide')['style']=f'--crossrail-head-offset:{-d}px';f.write_text(str(s))
f=P/'review-notes.md';f.write_text(f.read_text()+'''\n## 페이지별 제목 잉크 기준선\n\n원본과 최신 replica·조립본을60번 실제 브라우저 렌더하고 x96–450/y125–215 ROI에서 배경 median과 전경색으로 첫 잉크 행을 추출했다. 일부 원본은 제목이6–7px 높은 별도 기준선이며, 단일 공통 header를 전체 이동하는 것은 맞지 않았다. 각 페이지 실측 delta를 반대로 적용했다. kit의 namespaced length `--crossrail-head-offset`은 기본0이며 해당 source 페이지의 제목에만 공급한다. 06·10처럼 이미 일치하는 제목과 모든 본문·아이콘·도형 좌표는 이동하지 않는다. replica는 각자의 실측 top만 수정했다. 근거는 `qa/title-baselines-canonical.json`이다.\n''')
