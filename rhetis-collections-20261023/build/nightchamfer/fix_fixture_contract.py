from pathlib import Path
import re
C=Path('/workspace/output/nightchamfer')
for n in ['delta','headline','gauge','pill','waffle','tag']:
 for p in (C/'elements'/n/'fixtures').glob('*.html'):
  s=p.read_text();s=re.sub(r';\s*(justify-content|gap|font-size|line-height):[^;\"]+','',s);p.write_text(s)
p=C/'elements/tag/fixtures/tag-hl.html';s=p.read_text().replace('class="prose" style=', 'class="prose" data-el="nightchamfer-prose" style=');s=re.sub(r'<!-- min:.*?-->','<!-- min: 6x3 -->',s,count=1);p.write_text(s)
p=C/'elements/tag/fixtures/tag-hl-extended.html';p.write_text('''<!-- min: 6x3 -->
<div class="prose" data-el="nightchamfer-prose" style="grid-column:1 / span 12; grid-row:1 / span 6"><p><span class="tag" data-el="nightchamfer-tag">장기 계약 갱신</span> 고객 접점을 통합한 뒤 <b class="hl" data-el="nightchamfer-tag">고객 유지율 96.4%</b>를 기록했습니다. 현장 피드백을 반영한 서비스 개선으로 주요 고객과의 협력 범위를 넓혔습니다.</p></div>
''')
p=C/'elements/legend/fixtures/legend-extended.html'
if not p.exists():p=next((C/'elements/legend/fixtures').glob('*extended.html'))
p.write_text('''<!-- min: 6x1 -->
<div class="legend" data-el="nightchamfer-legend" style="grid-column:1 / span 12; grid-row:1 / span 6"><span class="key tone-1">신규 고객</span><span class="key tone-2">기존 고객 확장</span><span class="key tone-3">파트너 협력</span><span class="key tone-4">해외 사업</span></div>
''')
p=next((C/'elements/pricing/fixtures').glob('*extended.html'));p.write_text('''<!-- min: 8x4 -->
<div class="plans" data-el="nightchamfer-pricing" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="plan" data-el="nightchamfer-pricing"><b class="name">팀 워크스페이스</b><div class="price"><b class="fig">19,000</b><small>원 / 월</small></div><div class="list check" data-el="nightchamfer-list"><div class="item"><b class="name">문서와 프로젝트 통합</b></div><div class="item"><b class="name">기본 업무 자동화</b></div></div></div><div class="plan on" data-el="nightchamfer-pricing"><span class="tag" data-el="nightchamfer-tag">성장 팀 추천</span><b class="name">엔터프라이즈 AI 협업</b><div class="price"><b class="fig">49,000</b><small>원 / 월</small></div><div class="list check" data-el="nightchamfer-list"><div class="item"><b class="name">조직 전체의 지식 검색</b></div><div class="item"><b class="name">전담 기술 지원과 보안 검토</b></div><div class="item"><b class="name">고객별 업무 흐름 자동화</b></div></div></div></div>
''')
p=next((C/'elements/versus/fixtures').glob('*extended.html'));s=p.read_text().replace('class="side on"','class="side"');s=s.replace('class="side"','class="side on"',1);p.write_text(s)
