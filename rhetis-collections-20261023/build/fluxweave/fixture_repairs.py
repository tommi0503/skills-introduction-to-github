from pathlib import Path
import re
O=Path('/workspace/output/fluxweave')
gold={'card','callout','chart-area','chart-bar','chart-donut','chart-line'}
for p in O.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name in gold:continue
 s=p.read_text()
 def listfix(m):
  attrs=m.group(1);body=m.group(2)
  if 'data-el=' not in attrs:attrs+=' data-el="fluxweave-list"'
  body=re.sub(r'<li(?:\s[^>]*)?>(.*?)</li>',lambda v:'<div class="item"><b class="name">'+v.group(1)+'</b></div>',body,flags=re.S)
  if 'pricing' in str(p) and 'check' not in attrs:attrs=attrs.replace('class="list"','class="list check"')
  return '<div'+attrs+'>'+body+'</div>'
 s=re.sub(r'<ul(\s[^>]*class="list[^>]*?)>(.*?)</ul>',listfix,s,flags=re.S)
 # Embedded element roots retain their own explicit scope.
 s=re.sub(r'(<(?:span|b)\b[^>]*class="(?:tag|hl)"[^>]*)(>)',lambda m:m.group(1)+('' if 'data-el=' in m.group(1) else ' data-el="fluxweave-tag"')+m.group(2),s)
 p.write_text(s)
for f,m in [('person','7x5'),('pricing','8x5')]:
 for p in (O/'elements'/f/'fixtures').glob('*.html'):p.write_text(re.sub(r'^<!-- min:.*?-->',f'<!-- min: {m} -->',p.read_text(),count=1))
(O/'elements/tag/fixtures/extended.html').write_text('''<!-- min: 3x1 -->
<span class="tag" data-el="fluxweave-tag" style="grid-column:1 / span 12; grid-row:1 / span 6">해외 시장 확장 · 우선 실행 과제</span>
''')
(O/'elements/legend/fixtures/extended.html').write_text('''<!-- min: 7x2 -->
<div class="legend" data-el="fluxweave-legend" style="grid-column:1 / span 12; grid-row:1 / span 6"><span class="key tone-1">기업 솔루션</span><span class="key tone-2">데이터 분석 서비스</span><span class="key tone-3">컨설팅·교육</span><span class="key tone-4">해외 파트너십</span><span class="key tone-5">기타 사업</span></div>
''')
(O/'elements/pricing/fixtures/extended.html').write_text('''<!-- min: 8x5 -->
<div class="plans" data-el="fluxweave-pricing" style="grid-column:1 / span 12; grid-row:1 / span 6">
<div class="plan" data-el="fluxweave-pricing"><b class="name">빠른 검증을 위한 시작 플랜</b><div class="price"><b class="fig">45만</b><small>원 / 월</small></div><div class="list check" data-el="fluxweave-list"><div class="item"><b class="name">핵심 설비 3대 연동</b><p class="note">현장의 주요 상태를 한 화면에서 확인합니다.</p></div><div class="item"><b class="name">주간 개선 리포트</b></div></div></div>
<div class="plan on" data-el="fluxweave-pricing"><span class="tag" data-el="fluxweave-tag">성장 조직 추천</span><b class="name">여러 사업장을 연결하는 통합 운영 플랜</b><div class="price"><b class="fig">120만</b><small>원 / 월</small></div><div class="list check" data-el="fluxweave-list"><div class="item"><b class="name">사업장별 데이터 통합</b><p class="note">의사결정에 필요한 지표와 권한을 조직에 맞게 구성합니다.</p></div><div class="item"><b class="name">전담 컨설턴트 지원</b></div><div class="item"><b class="name">운영 프로세스 고도화</b></div></div></div>
</div>
''')
p=O/'elements/tag/element.css';p.write_text(p.read_text()+'\n[data-el="fluxweave-tag"]{width:fit-content;justify-self:center;}')
p=O/'elements/legend/element.css';p.write_text(p.read_text()+'\n[data-el="fluxweave-legend"] .tone-5::before{background:var(--n-5);}')
p=O/'elements/matrix/element.css';p.write_text(p.read_text()+'\n[data-el="fluxweave-matrix"].swot>.cell.on [data-el="fluxweave-list"],[data-el="fluxweave-matrix"].swot>.cell.on [data-el="fluxweave-list"] .name{color:var(--a1-on);}')
print('nested roots and distinct fixtures repaired')
