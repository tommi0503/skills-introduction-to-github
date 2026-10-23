from pathlib import Path
import re,json,hashlib
B=Path('/workspace/output/roundrise')
for k in ['versus','pricing','person','matrix']:
 for p in (B/'elements'/k/'fixtures').glob('*.html'):
  s=p.read_text()
  def sub(m):
   inner=re.sub(r'<li>(.*?)</li>',r'<div class="item"><span class="name">\1</span></div>',m[1],flags=re.S)
   return '<div class="list'+(' check' if k=='pricing' else '')+'" data-el="roundrise-list">'+inner+'</div>'
  s=re.sub(r'<ul class="list(?: check)?"[^>]*>(.*?)</ul>',sub,s,flags=re.S);p.write_text(s)
# Distinct extended fixtures exercise real content and member variations.
p=B/'elements/versus/fixtures/extended.html';s=p.read_text().replace('2055','도입 전: 분산된 고객 경험').replace('2056','도입 후: 연결되는 고객 경험').replace('부서마다 다른 생산 관리 도구','채널마다 반복하던 신규 고객 정보 확인').replace('월말에야 확인하는 실적','담당자별로 달랐던 고객 문의 처리 기준').replace('불량률 0.8%','첫 응답까지 평균 24시간 소요').replace('전 사업장 하나의 MES','온라인과 오프라인의 고객 이력을 한 화면에 통합').replace('실시간 생산 지표','담당자와 후속 조치를 실시간으로 공유').replace('불량률 0.3%','첫 응답까지 평균 4시간으로 단축');s=re.sub(r'\A<!--.*?-->','<!-- min: 8x5 -->',s,flags=re.S);p.write_text(s)
p=B/'elements/tag/fixtures/extended.html';p.write_text('<!-- min: 6x2 -->\n<div class="prose" data-el="roundrise-prose" style="grid-column:1 / span 12; grid-row:1 / span 6"><p>전사 고객 지원 체계가 <b class="hl" data-el="roundrise-tag">평균 응답 시간 62% 단축</b>이라는 변화를 만들었습니다. <span class="tag on" data-el="roundrise-tag">확대 적용</span> 다음 분기에는 해외 법인으로 운영 범위를 넓힙니다.</p></div>')
p=B/'elements/legend/fixtures/extended.html';p.write_text('<!-- min: 8x2 -->\n<div class="legend" data-el="roundrise-legend" style="grid-column:1 / span 12; grid-row:1 / span 6"><span class="key tone-1">핵심 고객 유지</span><span class="key tone-2">신규 사업 매출</span><span class="key tone-3">해외 파트너 확대</span><span class="key tone-4">장기 계약 갱신</span><span class="key tone-5">기타 운영 수익</span></div>')
p=B/'elements/pricing/fixtures/extended.html';p.write_text('''<!-- min: 8x5 -->
<div class="plans" data-el="roundrise-pricing" style="grid-column:1 / span 12; grid-row:1 / span 6">
<div class="plan" data-el="roundrise-pricing"><b class="name">성장하는 팀을 위한 스타터</b><div class="price"><b class="fig">49만</b><small>원 / 월</small></div><div class="list check" data-el="roundrise-list"><div class="item"><span class="name">프로젝트 20개</span></div><div class="item"><span class="name">주간 운영 리포트</span></div><div class="item"><span class="name">담당자 온보딩 지원</span></div></div></div>
<div class="plan on" data-el="roundrise-pricing"><span class="tag" data-el="roundrise-tag">성장 추천</span><b class="name">여러 조직을 연결하는 비즈니스</b><div class="price"><b class="fig">129만</b><small>원 / 월</small></div><div class="list check" data-el="roundrise-list"><div class="item"><span class="name">프로젝트 무제한</span></div><div class="item"><span class="name">실시간 고객 대시보드</span></div><div class="item"><span class="name">분기별 운영 개선 워크숍</span></div><div class="item"><span class="name">전담 고객 성공 매니저</span></div></div></div>
</div>''')
for p in (B/'elements/pricing/fixtures').glob('*.html'):
 s=p.read_text();s=re.sub(r'\A<!--.*?-->','<!-- min: '+('8x5' if p.name=='extended.html' else '12x5')+' -->',s,flags=re.S);p.write_text(s)
p=B/'elements/person/fixtures/person.html';s=p.read_text();p.write_text(re.sub(r'\A<!--.*?-->','<!-- min: 6x5 -->',s,flags=re.S))
p=B/'elements/chart-bar/fixtures/source-performance.html';s=p.read_text().replace(' report','').replace('report ','');p.write_text(s)
# Nested text receives a usable share of its semantic parent's slot.
for k,code in {
'versus':'.versus[data-el="roundrise-versus"]>.side>.list{flex:1;min-height:0;justify-content:center}.versus[data-el="roundrise-versus"]>.side>.list .name{font-size:var(--type-18)}',
'pricing':'.plan[data-el="roundrise-pricing"]>.list .name{font-size:var(--type-18)}.plan[data-el="roundrise-pricing"]>.list{gap:var(--gap-sm)}',
'person':'.person[data-el="roundrise-person"]>.list{container-type:inline-size;gap:var(--gap-sm)}.person[data-el="roundrise-person"]>.list .name{font-size:var(--type-18)}',
'matrix':'.matrix[data-el="roundrise-matrix"].swot>.cell>.list{container-type:inline-size;gap:var(--gap-sm)}.matrix[data-el="roundrise-matrix"].swot>.cell>.list .name{font-size:var(--type-18)}',
}.items():
 p=B/f'elements/{k}/element.css';p.write_text(p.read_text()+code)
# Remove native ul defaults entirely; the contract draws item markers.
p=B/'elements/list/element.css';p.write_text(p.read_text()+'.list[data-el="roundrise-list"]{list-style:none;margin:0}')
m={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.rglob('*') if p.is_file()};Path('/workspace/work/roundrise/frozen-source-manifest.json').write_text(json.dumps(m,indent=2))
