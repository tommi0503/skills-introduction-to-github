from pathlib import Path
import json,re
P=Path(__file__).resolve().parent;E=P/'vectorbox/elements'
R='.hub[data-el="vectorbox-hub"]';p=E/'hub/element.css';s=p.read_text();s=s.replace('/* Source 06. One representative base; contract variants only. */','/* Source 06 circle, thin-line and folded-core motifs only.\n   Inferred radial hub: the source rectangle track is not a hub contract. */')
s=s.replace(R+'{position:relative;padding:0}',R+'{position:relative;padding:0;anchor-scope:all}')
s=re.sub(re.escape(R)+r":before\{content:'';position:absolute;left:30\.7%;.*?border:1px solid var\(--n-4\)\}",'',s,count=1)
s=s.replace(R+'>.core{position:absolute;',R+'>.core{anchor-name:--vectorbox-hub-core;z-index:1;position:absolute;')
for n in range(2,8):
 mark='--vectorbox-hub-mark-'+str(n); sel=R+'>.spoke:nth-child('+str(n)+')'
 # Each connector is laid out after both its own mark and the earlier core.
 grad='to top right' if n in [2,5] else 'to bottom right'
 # For the right-hand and left-hand bottom members, the slope reverses.
 # Explicit endpoint anchors make the segment work for every allowed member count.
 s+=f'\n{sel}>.mark{{anchor-name:{mark}}}'
 s+=f"{sel}:after{{content:'';position:absolute;z-index:-1;pointer-events:none;left:min(anchor(--vectorbox-hub-core center),anchor({mark} center));right:min(anchor(--vectorbox-hub-core center),anchor({mark} center));top:calc(min(anchor(--vectorbox-hub-core center),anchor({mark} center)) - .5*var(--stroke));bottom:calc(min(anchor(--vectorbox-hub-core center),anchor({mark} center)) - .5*var(--stroke));background:linear-gradient({grad},transparent calc(50% - .5*var(--stroke)),var(--n-4) calc(50% - .5*var(--stroke)),var(--n-4) calc(50% + .5*var(--stroke)),transparent calc(50% + .5*var(--stroke)))}}"
# Slope orientation depends only on this member's own count-derived position.
# Existing positions: 2/3 upper, 4/5 bottom for 4 members; 5/6/7 need their lower/middle cases.
for count in [3,4,5,6]:
 for i in range(count):
  n=i+2; right=i%2==1
  y=(0 if count<=4 and i<2 else 1) if count<=4 else i//2
  # count 3/4: top row then bottom row; count5/6: top/middle/bottom.
  row=(0 if i<2 else 2) if count<=4 else i//2
  down=row==2
  grad='to top right' if (not right and not down) or (right and down) else 'to bottom right'
  s+=f'\n{R}:has(>.spoke:nth-child({count+1}):last-child)>.spoke:nth-child({n}):after{{background:linear-gradient({grad},transparent calc(50% - .5*var(--stroke)),var(--n-4) calc(50% - .5*var(--stroke)),var(--n-4) calc(50% + .5*var(--stroke)),transparent calc(50% + .5*var(--stroke)))}}'
p.write_text(s+'\n')
f=E/'hub/fixtures/replica-06.html'; f.rename(f.with_name('inferred-radial.html'))
(E/'hub/description.md').write_text('# 방사형 허브\n\n원본06의 원형 표식, 검은 중심, 접힌 작은 면, 얇은 연결선에서 추론했다. 실제 원본은 주변 네 점을 사각 트랙으로 잇고 중심과 연결하지 않으므로 hub.spokes의 관측 base가 아니다. 이 요소는 중심에서 각 spoke mark로 실제 선을 연결하며 3–6개 멤버를 수용한다. inferred-radial fixture는 새 업무 문구를 사용한 추론 예시다.\n')
# One uninterrupted root-level bus; vertical drops meet node upper borders.
R='.org[data-el="vectorbox-hierarchy"]';p=E/'hierarchy/element.css';s=p.read_text().replace('gap:var(--gap);padding:calc(2*var(--gap-lg))','--vectorbox-org-count:3;gap:var(--gap);padding:calc(2*var(--gap-lg))')
s=s.replace('gap:var(--gap-sm);border-top:1px solid var(--n-4);padding-top:var(--gap-sm)','gap:var(--gap-sm);padding-top:var(--gap-sm)')
s+='\n'+R+":before{content:'';position:absolute;top:calc(2*var(--gap-lg));left:calc(var(--gap-sm) + (100% - 2*var(--gap-sm) - (var(--vectorbox-org-count) - 1)*var(--gap))/(2*var(--vectorbox-org-count)));right:calc(var(--gap-sm) + (100% - 2*var(--gap-sm) - (var(--vectorbox-org-count) - 1)*var(--gap))/(2*var(--vectorbox-org-count)));height:1px;background:var(--n-4)}"
for n in [2,3,4]:s+=f'\n{R}:has(>.branch:nth-child({n+1}):last-child){{--vectorbox-org-count:{n}}}'
p.write_text(s+'\n');m=json.loads((E/'hierarchy/element.json').read_text());m['tokenDefaults']['--vectorbox-org-count']='3';(E/'hierarchy/element.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
# Child .name must use the node's bounded text scale, rather than common name cap28.
R='.swimlane[data-el="vectorbox-swimlane"]';p=E/'swimlane/element.css';s=p.read_text();s=s.replace('padding:var(--gap-sm);font-size:clamp(var(--type-12),2.5cqw,var(--type-20))','padding:calc(var(--gap-sm)/2);font-size:clamp(var(--type-12),min(2.5cqw,5cqh),var(--type-20))')
s+='\n'+R+'>.node>.name{font-size:inherit;line-height:var(--name-line)}\n';p.write_text(s)
# Correct the map's semantic classification, not just its prose.
p=P/'map.json';m=json.loads(p.read_text())
for i in m['instances']:
 if i['id']=='06-hub':
  i.update(leaf=None,use='unexpressible',fixture=None,why='외곽 네 노드의 사각 연결 트랙과 독립 중앙 원은 중심→각 spoke 관계가 아니다. hub.spokes로 조립하면 원본에 없는 중심 방사 연결을 만들거나 계약을 위반한다. 필요한 구조는 독립 node/core와 외곽 edge endpoint 목록을 가진 graph다.')
  i['design']=i['design'].replace('네 방향 연결형 허브','외곽 사각 트랙과 독립 중앙 원의 관계도')+' 중앙과 주변 원 사이의 방사 선은 실제로 없다. 이 관계는 현재 hub 계약으로 표현할 수 없다.'
m['roles']={'균일한 종이 바탕':'--page','주 제목·검은 중심·검은 프레임':'--ink','강조색 원·카드 선·선택 핸들·주 계열':'--a1','강조 제목·강조 수치의 글자':'--a1-7','강조 채움 위 반전 글자':'--a1-on','보조 검정 계열과 강조':'--a2','보조 채움 위 반전 글자':'--a2-on','옅은 강조 카드 면':'--a1-1-soft','제안열의 옅은 강조 바탕':'--a1-2-soft','가느다란 강조 테두리':'--a1-4-soft','부드러운 중간강조 계열':'--a3','매우 옅은 계열':'--a4','사진을 비운 placeholder·추론 보조면':'--n-1','얇은 표 구분선':'--n-3','가는 관계 연결선':'--n-4','중앙 접힌 면':'--n-5','가장 옅은 보조 문구':'--n-7','본문 보조 설명':'--n-8','상승·양호 상태':'--good','주의 상태':'--warn','하락·위험 상태':'--bad'}
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
p=P/'GAPS.md';s=p.read_text();s+='\n- 06 / perimeter graph with independent core: 주변 네 원을 잇는 사각 트랙 안에 중앙 원이 독립적으로 놓인다. 중심→각 spoke의 방사 연결이 없으므로 hub.spokes로 표현할 수 없다. 필요한 마크업은 독립 core/node 목록과 외곽 node 사이 endpoint를 정하는 edge 목록이다. 원본에 없는 방사 선을 추가해 조립하지 않았다.\n';p.write_text(s)
# The assembly must not continue claiming this source graph is the inferred radial hub.
p=P/'reassembled/slide_06.html';s=p.read_text();start=s.index('<div class="body">');end=s.index('</div></div><div class="idx">',start)
s=s[:start]+'<div class="body"><!-- 06 perimeter graph: unexpressible; see map.json and GAPS.md. -->'+s[end:];p.write_text(s)
p=P/'review-notes.md';s=p.read_text();s+='''\n## 관계 의미 교차검수 후 정정\n\n최종 원본 대조 다음의 별도 기능 검수에서, 06 외곽 사각 트랙을 hub로 매핑한 해석 오류를 발견했다. 중앙 원은 외곽 네 점과 연결되어 있지 않으므로 hub.spokes가 아니다. map의06-hub를 unexpressible로 바꾸고 필요한 graph edge 마크업을 GAPS.md에 적었다. 조립본의 잘못된 hub도 제거했으며 원본에 없는 방사 연결을 추가하지 않았다. 이로써 gap은5개가 되었다. 원본 자체를 맞춘 replica는 변경하지 않았다. hub CSS는 원·검은 접힌 중심·가는 선만 같은 언어로 쓰는 inferred radial로 바꾸고 replica-06 fixture를 inferred-radial로 이름을 바로잡았다.\n\nhierarchy는 각 branch 상단선이 gap에서 끊겼던 문제를 root 소유의 연속 bus와 실제 node로 내려오는 세로선으로 수정했다. swimlane 최소6×3에서 공통 .name28px가 작은 노드의 본문 크기보다 우선해 면 밖으로3줄이 나왔던 문제는 .node 자신의 cqw/cqh 제한 글자 크기를 .name에 그대로 적용해 고쳤다. wholeComponent 자동검사가0이어도 내부 node 면 밖 글자를 놓친 사례로 기록한다. map.roles에는 덱 공통의 색 역할을 한 번 정의하고, 기존 CSS의 page/ink/강조면/강조문자/관계선/보조문자 용도와 대응시켰다.\n''';p.write_text(s)
print('updated hub hierarchy swimlane; map roles',len(m['roles']))
