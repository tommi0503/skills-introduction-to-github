"""Record the real contract composition of every reassembled source page."""
from pathlib import Path
import sys,json
from lxml import html
ROOT=Path(__file__).resolve().parent
for kid in sys.argv[1:]:
 P=ROOT/(kid+'-project');rows=[]
 for f in sorted((P/'reassembled').glob('slide*.html')):
  doc=html.parse(str(f));els=sorted(set(x.split(kid+'-',1)[-1] for x in doc.xpath('//*[@data-el]/@data-el')));rows.append({'page':f.name,'elements':els,'usesOnlyFoundation':not els})
 lines=['# 최종 조립 계약 대응표','','원본 이미지 목록의 페이지 유형 분류와 별도로, 최종 HTML이 실제로 사용하는 계약 요소를 기록했다. 각 페이지는 foundation 위에서 조립한다.','','| 페이지 | 실제 요소 계약 폴더 |','|---|---|']
 for r in rows:lines.append('| '+r['page']+' | '+(', '.join(r['elements']) or 'foundation cover')+' |')
 (P/'assembly-map.md').write_text('\n'.join(lines)+'\n');(P/'assembly-map.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print(kid,len(rows),'pages mapped')
