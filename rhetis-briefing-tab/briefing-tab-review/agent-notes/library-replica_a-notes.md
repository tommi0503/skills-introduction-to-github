# Elements A 검수 기록

## 범위와 산출물

- card, pill, callout, tag, list, quote, headline, prose, metric, delta, gauge, table, legend, code: 14개 요소, 37개 fixture, 총79개 파일(.css14 .json14 .md14 .html37).
- 모든 요소 CSS는 원본 덱의 조용한 중립 면, 작은 라운드, 1px 구획선, 슬림한 챕터 캡을 바탕으로 새로 작성했다. 샘플 CSS를 복사하지 않았다.
- card 필수6개와 callout 필수3개는 원본 fixture를 data-el만 바꿔 보존했다. 그 외 모든 요소는 2개 이상이며 긴 이름·긴 설명, 멤버 수와 변형을 섞었다.

## 브라우저 검사

- /workspace/work/review-a/sheet.html 임시 자체 시트에 담당37fixtures × 최소/12x6 × 라이트/다크 =148case를 넣었다.
- 실제 Chromium에서 로컬 Noto Sans KR, Pretendard Variable, Nanum Gothic Coding 로드 성공을 확인했다.
- DOM 텍스트가 자기 data-el root 경계를 벗어나는 검사: 최종0개. 검사는 p,b,small,span,th,td,h2,blockquote의 렌더된 박스를 root와 비교했다.
- 14종 최소 크기 PNG를 각각 열었고, 추가로 card-3-on, card-4 dark, card-5-tone, source-keywords, list divided dark, numbered code dark, tag labels를 열어 확인했다.
- 수정은 3개 묶음으로 진행했다. (1) inline tag의 size containment로 폭이0이 되는 문제 수정. (2) divided list를 원본의 중립 point 패널·라벨 구분선 형태로 정리. (3) 원본20에 대응하는 quiet pill의 mark capsule 추가 후 재렌더. 최종 재렌더에 모든 수정이 반영됐다.
- card의 fig/name/note 기준 높이를 맞춰 나란히 놓은 카드의 시작점을 정렬했다. 좁은 칸에서는 kick을 먼저 숨기고 note를 줄이며, 매우 낮은 칸에서만 note를 숨긴다. fig/name은 숨기지 않는다.
- pill/mark/tag는 flex 양축 중앙 정렬이다. 아이콘 원은56px/30px 또는44px/24px로 실제 아이콘 칸을 원 지름의 약54%로 제한했다.
- 눈으로 확인한 최소 시트에서 잘림·겹침을 발견하지 않았다. 모든 중간 칸 크기의 전수검사는 주 에이전트의 통합검수에서 수행한다.

## 기하와 재조립 결정

- card는14px 반경과 얇은 상단 캡을 쓴다. 중립 기본 면과 단일 .on 강조가 원본 표·설명 패널의 위계를 이어간다.
- pill.quiet: .mark만136×40px capsule, .name은 그 옆의 설명으로 만들어 원본20의 키워드 행을 계약 마크업으로 재조립할 수 있다. source-keywords fixture 추가.
- list.divided: 각 item을 중립 사각 패널로 두고 name/note 사이에1px 수직선을 쓴다. POINT 레이블과 설명을 가진 원본25에 대응한다.
- code는 --briefing-tab-code-font를 element.json tokenDefaults에 선언하고 kit extension font와 연계했다. 값은 계약이 허용한 Nanum Gothic Coding이며 CSS는 var()만 쓴다.

## 명시적 예외와 해석

- mandatory card-4 원본은 .icon 안에 ✹ 글자4개를 포함한다. 사용자의 같은 마크업·데이터 요구를 우선해 보존했다. 새 fixture는 Lucide data-icon의 빈 칸 규칙을 따른다.
- mandatory callout 및 callout-icon의 원본 최상위 grid placement는1/span12,1/span6 일반 규칙과 다르다. 동일 마크업 보존을 우선해 그대로 유지했다.
- inline tag/hl은 intrinsic width를 유지해야 하므로 container-type:normal이다. 부모 prose container의 query로 타이포를 단계적으로 조정한다. size containment를 직접 적용하면 폭이0이 되어 글자가 세로로 무너지는 실제 브라우저 오류를 확인했다.
- 원본 덱에 없는 요소의 문구는 정상적인 한국어 온보딩·비즈니스 내용으로 새로 작성했다. 원본에서 읽지 못해 지어낸 문구와 구별된다.

## 실제 재조립 칸 통합 수정

- 최종 담당 수량은14요소·40fixtures·82파일로 늘었다. 원본23 긴 설명 카드,7행 표, 설명 없는5행 divided list를 각각 회귀 확인용 fixture로 추가했다.
- slide23의4×6 카드: 폭281–400px에서 name20px/note16px 단계로 내려 긴 설명을 모두 보이게 했다. note가 flex-shrink로 박스만 줄고 실제 글자는 넘는 상황을 막았다.
- slide27의6×4,7행 표: 높이270px 이하에서14px 글자와4px 세로 셀 패딩을 적용했다.3열 표에만26.2/58.9/14.9% 폭을 적용하고4열 이상은 기본 분배를 유지했다.
- slide29의 설명 없는 divided list: note가 있는 item만2열로 나누고 note 없는 item은 전폭1열로 두었다.5행이 제목 칸과 겹치지 않도록 각 행의 세로 패딩을8px로 조정했다.
- slide27 범례: 폭600px 이하에서14px 글자·16px 키·16px 열 간격으로 다섯 키를 한 줄에 배치했다.
- 실제 reassembled23/27/29를 Chromium에서 열어 각각 캡처·시각 확인했다. Range로 실제 글자 경계를 root와 비교해 세 페이지 모두 초과0개를 확인했다. 이후3열 폭 적용은 통합 최종 렌더에서 재확인한다.
- 전체 담당40fixtures × 최소/12x6 × 라이트/다크 =160case 자체 시트를 다시 렌더했으며 요소 경계 초과0개였다.


## 원본 충실도 재작업과 최종 동결

이전 조립본이 원본의 주요 시각 객체를 생략했던 문제를 인정하고, 원본21·22·29를 다시 직접 열어 좌표·크기로 비교했다. 유사하다는 추상 평가 대신 다음처럼 복원했다.

- 21·22: 기존 전체 문장형 callout을 label+divider+두 줄 summary로 복원했다. 새 class 없이 p의 b+span 구조를 읽는 범용 prefix 패턴이다. 필수 golden fixture는 변경하지 않았다. stack에서 callout과 표의 자연 높이를 쓰게 하여 표를 그리드 셀 높이로 불필요하게 늘리지 않았다.
- 21 최종 측정: callout (96,238,1088,104), 표 (96,358,1088,273.5). 원본의 callout (97,237,1086,101), 표 시작 (97,359)와 주요 구획이1–3px 차이이다.
- 22 최종 측정: 두 표 시작 (96,242)/(648,242), 각각536×273.5, summary (96,531.5,1088,104). 원본의 비대칭531/547px 표 폭과10px 간격은 계약의 동등 group으로536/536px·16px 간격이 되어 약5–12px 차이가 남는다. 표 행·모든 텍스트·하단 요약 띠는 빠짐없이 복원했다.
- 23(관계 담당과 협업): 읽기 카드 폭368px, title22px 중앙, note16px·행간1.7·기본 ink로 원문을 복원했다. fig만 있는 card의 quiet/on 변형을84/108px 원형 말풍선으로 설계했고, 비어 있는 delta의 from/to는 원본의 두꺼운 방향 화살표를 표현한다. 관계 담당이 두 선과 원형 라벨·화살표를 포함한 최종 원본 대조를 수행했다.
- 29: 왼쪽 tab·구분선 목록, 오른쪽 큰 사람2개·20/40%·각10개의 원형 unit을 전부 복원했다. 10-unit waffle.figures의 범용 요약형을 만들고50-unit waffle 기본형은 유지했다. 큰 수치는 Freesentation600을 실제 로드하고 공유 tracking의 배수로 폭을 맞췄다. source29의 accent3/4는 별도 source style에서 원본 픽셀 청록#51a6cb/분홍#dc5c7e를 공급한다. 컬렉션 CSS는 색 리터럴을 갖지 않는다.
- 29 최종 측정: tab (182,254,400,44), list panel (142,298,480,324), 첫 unit row (770,398,352,28), 둘째 (770,577,352,28). 원본 tab (184,255,398,44), panel (143,299,481,324), dots (769,399…)와 약1–2px 차이이다. 사람은 CSS 기하로 구현하여 원본의 둥근 꼭짓점과 약간 다르다.
- 20 추가 검수: keyword capsule은 (630.3,462)/(630.3,515)/(630.3,568), 각각136×40px로 최종 렌더 확인했다. 원본의 y좌표 세 개와 일치하고 x는 그리드 때문에 약7px 오른쪽이다.
- 25·28 추가 검수:3-note point panel은 각각 (606,266,576,330)/(96,266,577,330). 129px label·수직선·16px note·13px 행 간격이 원본 패널 구도를 복원한다.
- 27 추가 검수: plain summary (110,230,536,101), 뒤 표는 자연 행 높이로 복원했다. 24의 혼합 범례도 막대 사각형·선+중앙 점으로 복원했다.
- 원본|조립본21·22·29의 최종 비교 PNG를 각각 직접 열어 주요 객체 누락이 없음을 확인했다. actual text Range 경계 초과0개. Freesentation600 76px loaded=true, font error0개를 확인했다. 기본400 굵기를 요청하는 document.fonts.check는 미사용 face를 false로 보고하므로 실제 사용 굵기로 검사했다.
- 최종 담당 범위는15요소(기존14+waffle),48fixtures,93개 파일이다. 최종 자체 시트192cases(48×최소/12x6×라이트/다크)를 재렌더했고 실제 글자 Range가 data-el root를 벗어나는 경우0개였다.
- main의 동결 선언 후 요소 CSS 추가 수정은 중단했다. 이후 전체 시트·PDF·ZIP 최종 생성은 주 에이전트가 수행한다.
