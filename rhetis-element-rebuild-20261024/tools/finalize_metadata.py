"""Assemble factual provenance and review documentation from the final proofs."""
from pathlib import Path
from html import escape
import json,re,hashlib

R=Path('/workspace/work/rebuild')
NAMES=list(json.loads((R/'profiles.json').read_text()))
DECKS=dict(zip(NAMES,['020','022','024','026','027','028','030']))
GRAMMAR={'tide-tab':'05·06·08','cutfield':'05·10·11','filament':'03·06·07','portico':'08·11·13','toggle-grid':'06·09·12','lamella':'03·10·11·19','rulemark':'01·05·09·11'}

def origins(n):
 c=R/n/n;m=json.loads((R/n/'review/map.json').read_text());out={}
 for p in sorted((c/'elements').iterdir()):
  if not p.is_dir():continue
  a=[x for x in m['instances']if x.get('leaf')==p.name and x['use']not in ['unexpressible','furniture','background']]
  out[p.name]={'source_pages':sorted({x['page']for x in a}),'instances':[{'page':x['page'],'use':x['use'],'id':x['id']}for x in a], 'origin': 'source'if a else'inferred','grammar_pages':GRAMMAR[n]}
 return out

def run():
 allorig={n:origins(n)for n in NAMES}
 rows=['# 요소별 출처','', '숫자는 고정 replica 페이지입니다. `추론`은 해당 요소가 replica에 없으므로 그 덱의 측정된 형태·타이포·선 문법에서 새로 설계했다는 뜻입니다. base 없이 계약 변형만 나온 경우에는 그 변형의 페이지를 표시합니다.','', '| 요소 | '+' | '.join(DECKS[n]+' '+n for n in NAMES)+' |','|---|'+'---|'*7]
 for leaf in sorted(allorig[NAMES[0]]):rows.append('| '+leaf+' | '+' | '.join('·'.join(allorig[n][leaf]['source_pages'])or'추론('+GRAMMAR[n]+')'for n in NAMES)+' |')
 (R/'ORIGINS.md').write_text('\n'.join(rows)+'\n')
 gaps=['# 계약 미지원 목록','', '다른 요소로 대체하거나 페이지 전용 CSS로 숨기지 않은 항목입니다. 전체 제안 마크업은 각 컬렉션 review/GAPS.md에 있습니다.','']
 rootreview=json.loads((R/'root-final-review.json').read_text())if(R/'root-final-review.json').exists()else{}
 for n in NAMES:
  v=R/n/'review';m=json.loads((v/'map.json').read_text());unsupported=[x for x in m['instances']if x['use']=='unexpressible']
  (v/'validation/origins.json').write_text(json.dumps(allorig[n],ensure_ascii=False,indent=2))
  og=['# Element origins','', '| Element | Replica pages / inferred grammar |','|---|---|']
  for leaf,x in allorig[n].items():og.append('| '+leaf+' | '+(', '.join(x['source_pages'])or'inferred from '+GRAMMAR[n])+' |')
  (v/'ORIGINS.md').write_text('\n'.join(og)+'\n')
  gaps.append('## '+DECKS[n]+' '+n+' — '+str(len(unsupported))+'개\n')
  for x in unsupported:gaps.append('- '+x['page']+' / '+x['id']+': '+x['design'])
  gaps.append('')
  notes=['# 검수 기록 — '+n,'', '## 범위와 보존','', '기존 replica HTML·CSS·PNG·PDF는 수정하지 않았다. `replica-freeze.json`의 SHA-256으로 보존 여부를 확인한다. 새 작업은 56개 요소의 전체 CSS, kit/foundation, 새 fixture, 요소 지도와 검수·조립 자료다. 원본 이미지나 replica를 통째로 배경에 깔지 않았다.','', '## 출처와 해석','', '- 직접 대응하는 요소의 페이지·bbox·측정 수치는 map.json에 있다. 없는 요소는 추론이라고 명시하며 출처를 꾸며내지 않는다.', '- 사진·복잡한 일러스트·로고는 연한 회색 번호 자리로 둔다. 단순 벡터와 연결은 각 소유 요소 또는 foundation이 그린다.', '- 이 작업에서 fixture 문구는 새 한국어 업무 내용으로 작성했다. 기존 replica의 판독·추정 문구는 보존했으며 새 원문으로 단정하지 않는다. 이번 작업에서 새로 지어낸 원본 문구는 없다.', '- 색은 덱 전체의 역할을 고정해 팔레트 자리로 옮겼다. 기준 라이트/다크 시트는 README 팔레트를 쓰므로 원본의 고유 RGB와 다르다. 조립 비교에는 같은 역할에 원본 근접 팔레트를 공급한다.', '- 낮은 대비의 원본 보조색은 읽을 수 있는 깊은 단계로 옮긴다. 밝은 강조면의 on 색은 대비가 높은 ink가 될 수 있어 원본의 흰 글자와 다르다.', '- 고정 replica 자체의 글자 맞춤·원본과의 잔여 차이는 유지한다. 조립본의 12×6 양의 그리드 트랙은 bbox를 먼저 계산하며 여러 세로 경계를 여섯 행으로 담는 양자화 오차가 남을 수 있다. layout-before-render.json에 요소별 수치를 기록했다.', '- 독립 행별 글꼴 크기·자간, 복합 제목 패널, 계약에 없는 다중 조각 파이 등은 GAPS.md에만 미지원으로 기록했다. 이를 임의의 새 클래스로 우회하지 않았다.','', '## 검사 방식과 수정','', '- 각 fixture의 min 이상 지정 크기와 min 자체를 두 모드에서 실제 1280×720 foundation에 배치하고 요소 칸을 여유 포함 잘라 한 줄로 묶었다.', '- DOM/Range 경계·가림·멤버 교차·대비·chip 중앙·의사 요소 도형 경계를 검사하고, 실제 PNG를 빈 foundation과 비교해 그림자와 글리프의 칸 밖 픽셀도 검사했다.', '- 글꼴은 로딩 상태만 확인하지 않고 실제 자손 및 생성 문자의 CDP 플랫폼 글꼴을 확인했다. Montserrat/Do Hyeon에 없는 한국어·중간점은 허용된 body 글꼴로 교정했다.', '- 실제 픽셀 검사에서 발견한 Do Hyeon %의 1–2px 오른쪽 돌출, timeline 강조점·회색 note 면, list/quote 장식 여유를 해당 요소 CSS에서 수정했다.', '- 모범 fixture의 데이터·마크업은 보존했다. 원문의 특수문자 별표 아이콘은 비어 있는 Lucide 아이콘으로, 6자 중복 금지와 충돌한 일반 문장 한 구절은 뜻을 유지한 최소 표현으로 바꾼 예외를 구조 감사에 명시했다.', '- 담당자가 모든 최종 native 크기 칸을 확인하고 주 담당자가 통합 시트와 페이지 비교를 확인한다. 최종 해시는 validation과 root-final-review.json으로 연결한다.','', '## 통합 페이지 관찰','']
  for pg,x in rootreview.get(n,{}).get('pages',{}).items():notes.append('- '+pg+': '+x['note'])
  notes+=['','## 담당 요소별 상세 기록','']
  for p in sorted((R/n/'build').glob('review-*.md')):notes+=['### '+p.stem,'',p.read_text()]
  if (R/'build/review-root-pages.md').exists():notes+=['### 주 담당자 페이지 대조 기록','',(R/'build/review-root-pages.md').read_text()]
  (v/'review-notes.md').write_text('\n'.join(notes)+'\n')
  # A local, inspectable gallery; all linked originals remain unscaled files.
  cards=[]
  for leaf in allorig[n]:
   links=' '.join('<a href="sheets/'+leaf+'-'+mode+'.png">'+mode+'</a>'for mode in ['light','dark'])
   if(v/'sheets'/(leaf+'-replica.png')).exists():links+=' <a href="sheets/'+leaf+'-replica.png">replica | 12×6 | min</a>'
   htmls=sorted((v/'html'/leaf).glob('*-light.html'))
   if htmls:links+=' <a href="html/'+leaf+'/'+htmls[0].name+'">HTML</a>'
   cards.append('<article id="'+leaf+'"><h2>'+leaf+'</h2><p>'+links+'</p><a href="sheets/'+leaf+'-light.png"><img loading="lazy" src="sheets/'+leaf+'-light.png" alt="'+leaf+' light size sheet"></a><a href="sheets/'+leaf+'-dark.png"><img loading="lazy" src="sheets/'+leaf+'-dark.png" alt="'+leaf+' dark size sheet"></a></article>')
  pages=' '.join('<a href="compare-reassembled/'+p.name+'">'+p.stem[-2:]+'</a>'for p in sorted((v/'compare-reassembled').glob('*.png')))
  doc='<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+n+' 검수</title><style>body{font:16px/1.5 system-ui;margin:32px;color:#17202a;background:#f4f5f7}a{color:#1454a5}article{background:white;padding:20px;margin:24px 0;border:1px solid #c9cdd3}img{display:block;width:100%;height:auto;margin:12px 0}h1,h2{line-height:1.2}</style><h1>'+n+' 요소 검수</h1><p>라이트·다크의 모든 fixture와 크기를 담은 원본 PNG를 열어 확대할 수 있습니다.</p><p><a href="map.json">지도</a> · <a href="ORIGINS.md">요소 출처</a> · <a href="GAPS.md">미지원</a> · <a href="review-notes.md">검수 기록</a></p><p>페이지 비교: '+pages+'</p>'+''.join(cards)+'</html>'
  (v/'index.html').write_text(doc)
 (R/'GAPS-INDEX.md').write_text('\n'.join(gaps)+'\n')
 print('Provenance, gap index, review notes and seven local galleries written')

if __name__=='__main__':run()
