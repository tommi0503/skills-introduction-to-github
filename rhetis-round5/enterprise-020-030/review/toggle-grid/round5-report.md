# Round5 — toggle-grid

## 새 디자인 폴더 ← replica 페이지

- `flowchart--framework` ← 07
- `flowchart--question-idea` ← 05
- `prose--bullet-panel` ← 03
- `table--component-matrix` ← 10
- `table--definition-rows` ← 12

## 패널을 쓴 곳

- 06 / 06-r5-furniture-2: Media-list wrapper: three167px photos,43px number capsules,own prose and two1px full-width row rules.; bbox [494, 62, 700, 571]
- 07 / 07-r5-furniture-3: One complete source framework, owning3arrow-title panels and the autonomous3-column relationship body.; bbox [139, 239, 1060, 346]
- 08 / 08-r5-furniture-4: Source46px arrow title bar +19px gap +277px table, both owned by this foundation panel.; bbox [139, 243, 1060, 342]
- 09 / 09-r5-furniture-5: Source46px arrow title bar +19px gap +277px table, both owned by this foundation panel.; bbox [139, 243, 1060, 342]
- 10 / 10-r5-furniture-6: Source46px arrow title bar +19px gap +277px table, both owned by this foundation panel.; bbox [139, 243, 1060, 342]
- 11 / 11-r5-furniture-7: Source46px arrow title bar +19px gap +277px table, both owned by this foundation panel.; bbox [139, 243, 1060, 342]
- 12 / 12-r5-furniture-8: One input/output identity panel owns its2-row table,6-spoke brand-assets hub and230x100 upward gray-to-page gradient arrow.; bbox [498, 67, 709, 561]

## 차트 확장

- 새 차트 확장 없음.

## 지운 일반 요소

`agenda`, `architecture`, `balance`, `bullet`, `callout`, `card`, `chart-area`, `chart-bar`, `chart-donut`, `chart-line`, `chart-scatter`, `chart-stack`, `chart-waterfall`, `code`, `concentric`, `cycle`, `decision-tree`, `delta`, `flowchart`, `funnel`, `gauge`, `heatmap`, `hierarchy`, `journey`, `legend`, `logo-group`, `matrix`, `matrix-nine`, `metric`, `mindmap`, `network`, `positioning`, `pricing`, `pyramid`, `quote`, `radar`, `roadmap`, `sankey`, `slope`, `sparkline`, `steps`, `swimlane`, `tag`, `timeline`, `treemap`, `venn`, `versus`, `waffle`

공통 상태 fixture는 선택이므로 기존 필수 예시를 0개 제외하고, source 기반의 새 한국어 fixture와 데이터 변형을 남겼다.

## 남은 gap과 이유

- 없음. 글자 스타일·캡션·측정 잔여물·큰 제목·사진 비율은 gap으로 분류하지 않았다.

## 실제 최종 시트·비교

요소별 `sheets/<design>-light.png`, `-dark.png`, `-replica.png`; foundation도 동일한 크기별 시트다. 실제 열람 증거는 주 담당자의 `root-final-review.json`의 최종 PNG 해시와 아래 담당자 기록에 연결한다. 조립 비교는 `compare-reassembled/slide_NN.png`이다.

### review-round5-charts

# Round5 표 검수

table--component-matrix ← replica10. 실제1060×277/29.15% label열/46pxheader·5rows를source에서새작성. 원문5행과새7행fixture. 첫시트의잘못된50%열분배와마지막행range초과4건을colgroup과source1.2line으로수정, 두번째시트의7행불균형은자기행수로높이를계산하여고침. 디자인별CSS토큰도독립이름으로분리. 최종20칸9QA0/원문0, light/dark전행및native최소칸을직접열어확인. 실제본파일 review/sheets/table--component-matrix-light.png·dark.png 및build/table--component-matrix-review/*-all-minima.png.

table--definition-rows ← replica12. source709×228·36.5%label열·각row102px·8px간격·24pxlabel/19pxnote를독립디자인으로새작성. 실제2행원문형태와긴2행변형,둘다새한국어. 최종20칸9QA0/원문0, 두모드전fixture행과native최소칸모두열어확인. 실제본파일review/sheets/table--definition-rows-light.png·dark.png,build/table--definition-rows-review/*-all-minima.png.

### review-round5-diagrams

# Round5 diagrams 검수 — toggle-grid

신규 2개 디자인, 원본 2개 인스턴스, 최종 48개 light/dark 크기별 셀을 직접 열어 확인했다. 9개 자동 지표·raster·복제 문구 검사·정적 계약 오류는 모두 0이다. 원본 replica는 수정하지 않았다.

## 출처와 크기

- `flowchart--framework` ← replica 07. 24칸. delivery-framework: min 6x3, partner-framework: min 6x3.
- `flowchart--question-idea` ← replica 05. 24칸. design-feedback: min 6x3, value-proposition: min 6x3.

## 판단·잔차

- 05 question→idea의 두 판과 가운데 줄무늬/실선 화살표 전체를 flowchart--question-idea 한 요소가 소유한다. 343×233/443×301 판과 55/69 말풍선 carrier의 비율을 유지한다.
- 원본 ?는 Oswald Bold glyph이며 Rhetis 공급 글꼴 표에 없다. 새 폰트 의존성을 만들지 않고 원본 TTF를 읽기 전용으로 측정하여 글자 없는 geometric SVG mask로 정규화했다. source glyph bbox(31,0,448,821), advance483/1000에서 14.178×27.914 잉크와 bubble 중심 대비 위치를 산출했다. 마지막 24칸에서 윤곽·광학 중심을 직접 확인했다.
- 전구는 data-icon=lightbulb이다. 시트 하네스의 아이콘 프리뷰는 단순 캐리어를 그리므로 원본 solid bulb와 같은 잉크는 아니다. 실제 라이브러리는 Lucide 자리 계약을 유지한다.
- 07 framework body [139,294,1060,283]은 3열 Input/Development/Output과 내부 상자 전체를 flowchart--framework가 소유한다. 외부 panel 및 3개 화살표 머리띠는 systems 소유이며 panel 안에 중첩한다. 원본 Fundametal 오타는 source 조립 데이터에만 그대로 보존한다.
- 하단 회색 field의 source-preview N3=#dedede 및 source N2=#e8e8e6은 공유 팔레트 결정이다. 표준 팔레트는 고치지 않는다.

## 실제 렌더 확인 기록

마지막 소스 변경 뒤의 native 패널과 각 셀 PNG SHA-256, 원본 크기 대조 PNG의 SHA-256은 같은 이름의 JSON에 기록했다. native 패널은 원본 셀 이미지를 축소하지 않고 배치한 확인 자료다. 요소 안의 글자/면 경계, 두 모드 대비, 정렬, 작은 칸의 유지, 연결 방향을 확인했다. 새 unexpressible은 없다.

전체 페이지 조립, 공유 foundation, 최종 공개 패키지는 주 에이전트가 별도로 통합 검수한다. 이 기록은 담당 요소의 최종 소스·크기별 시트·source bbox 대조에 대한 기록이다.

### review-round5-systems

# Round5 foundation 최종 담당 검수 기록

담당 소스는 동결했습니다. replica는 수정하지 않았습니다. root의 통합 페이지 검수와 최종 수락은 별도입니다.

01 기울어진 미니 페이지 면은 source 회전각·면 배치의 gray montage로 그립니다. 06 media-rows의 프레임·pill·prose·두 괘선을 한 부모가 소유하며 inline top 대신 prefixed rule-y 변수를 사용합니다. 07 세 검정 화살표 띠와 단일 flowchart--framework를 하나의 framework panel에 넣었습니다. 08–11 각 bar/table을 table-panel로 묶고 10은 독립 component-matrix를 사용합니다. 12는 hub+definition-rows+그 둘 사이 gradient arrow를 identity-assets 한 부모가 소유합니다. Oswald와 계약 글꼴의 차이는 승인된 Noto Sans native75%의 글꼴 잔차로 기록하며 GAP으로 남기지 않습니다.

타이포 수치는 실제 source DOM/Range/loaded font를 읽어 요소 상자 비율로 옮겼습니다. SVG text는 선택 가능한 HTML로, source 인장은 실제 글자 좌표/회전으로 그렸습니다. 폰트 크기는 공유 type8–256과 cqw/cqh의 clamp를 사용하며 디자인 색상은 팔레트 자리만 사용합니다. 장면 selector나 fixture별 CSS 보정은 없습니다.

source 장치 8개, 기존 중복 제거 ID 18개입니다. source 페이지/정확 bbox/완전 원문 markup 및 nested source_children은 build/map-round5-systems.json에 있습니다. 불필요한 원문 fragment/측정 dump는 새 장치로 만들지 않았습니다. 담당 신규 unexpressible은 없습니다.

최종 size matrix는 foundation/fixtures 16개, 양모드 합 84칸입니다. review/validation/foundation.json의 9종 QA는 모두 0입니다. proof source_hashes는 실제 현재 파일과 일치합니다. 새 한국어 fixture와 전체 frozen replica의 정규화 6자 중복 검사도 0건입니다. 원문은 검증 조립 markup에만 둡니다.

실제로 연 최종 자료: review/sheets/foundation-light.png와 foundation-dark.png를 그대로 보존한 root-sheet-pairs/toggle-grid-foundation-part01.png부터 part04.png까지 모든 행의 양모드 pair를 직접 열었습니다. 작은 칸에서도 도형/선/표/문자가 겹치거나 잘리지 않는지 확인했습니다. 별도로 직접 연 native 칸: r5-panel-framework-light-9x4.png, r5-panel-identity-assets-dark-6x6.png, r5-panel-media-rows-dark-9x4.png. 앞선 source/native 검토와 이번 마지막 렌더 파일 검토는 구분하며, 최종 전체 페이지 원본|replica|조립본 비교는 주 에이전트 담당입니다.

거대 native PNG는 바꾸지 않았습니다. 축소 pair manifest에는 각 원본 SHA256·크기·source hash current 여부·chunk 행/좌표가 기록되어 있습니다. 이 자료의 상태는 awaiting_root_visual_review이며 자동 수락하지 않았습니다.

최종 hub CSS/JSON 의존성 갱신 뒤 foundation84칸을 다시 렌더했습니다. 9종 QA0, source hashes 모두 현재이며 identity-assets 최소6×6 light 및12×6 dark native를 직접 열어 pill 중심·문자·gradient 연결·표 경계가 정상임을 확인했습니다. 자체 CSS/fixture는 추가 수정하지 않았습니다.

### 주 담당자 통합 검수

# 주 담당자 최종 통합 검수

## 검수 범위와 판정의 뜻

7개 컬렉션은 동결 replica의 실제 source 수치로 만든 디자인과 필요한 의존 요소만 남겼다. 남긴 요소107개, 신규 독립 디자인44개, 제외·보존한 일반 요소329개다. 요소의 크기별 light/dark 시트와 foundation 시트를 직접 열었고, 원본 | 동결 replica | 조립본 비교를87페이지 각각 열어 확인했다. 담당자는 각 native 칸을 확인했고 주 담당자는 통합 시트와 페이지 대조를 확인했다. 최종 파일 해시별 열람 기록은 root-final-review.json에 있다.

READY는 계약·반응형 fixture·현재 소스와 증거의 일치·파일 무결성 판정이다. 원본과 픽셀 단위로100% 같다는 뜻이 아니다. 아래 잔차를 숨기지 않는다. gap0은 round5의 확장 계약으로 표현하지 못한 디자인이 없다는 뜻이며, 시각적 차이가0이라는 뜻이 아니다.

## 직접 고쳐 확인한 문제

- Lamella20: 작은 도넛3개로 바뀌었던 구성을 지우고, 원본의 큰3조각 파이1개와 오른쪽 배분 패널/카드3개를 복구했다. 파이와 카드의 연결된 데이터/형태를 독립 요소가 소유한다.
- Cutfield02: 빠졌던 과녁 도형을 source의65×65 벡터로 복구했다.03 하단 절단면의 마지막 조각을 원본 팔레트 역할로 정정했다.06 목록 화살표와11 타임라인,08·12·13의 source 반전 글자 역할도 정정했다.
- Portico12: 사진의 흰 테두리, 회색 사진 자리, 교대 면, 금색 직함을 source 수치로 복구했다.
- Toggle04:212×212 원형 사진 테두리를 복구했다.12 중앙 영문은 허용된 가변 폭 폰트로1행을 유지한다. source Oswald 폭252.296875px에 대해 대체 Noto Sans 폭251.78125px이며, 글리프 모양 차이는 남는다. 글자를 기울이거나 transform으로 늘리지 않았다.
- Filament01: 반전 표지에서 사라졌던 ellipse seal의 currentColor 상속을 복구했다.04·07에서는 부모 표제에 들어 있는 span을 별도 인스턴스로도 포착했던 중복2건을 지웠다. 원본 부모 마크업은 보존했다. 전체7덱 DOM 부모/자식 자동 검사에서 이 두 건 외의 중복 포착은 없었다.
- Rulemark06: data.sourceText를 읽지 않아3개 카드의 parts가 비었던 조립기 문제를 바로잡았다. 원문 숫자·제목·설명을 kick/name/note로 읽는다. 페이지별 CSS 보정은 쓰지 않았다.

## 남겨 둔 차이와 스스로 내린 결정

- 모든 사진·복잡한 브랜드 로고·일러스트는 회색 placeholder다. Filament04의 입체 점 구체와 개별 로고, Toggle01의 기울어진 덱 몽타주도 이 범주로 판단했다. 단순 도형/괘선/표/차트는 구현했다. placeholder 숫자는 이미지 내용이 아니며, 독립 자리와 패널 안에서 번호/표시 여부가 원본과 다를 수 있다(Portico05, Toggle06 등).
- Lamella의 동결 replica01·03·06·08·09·11·13·14·16·18·19·21에는 일부 영문 표제가 과도한 음수 자간으로 뭉쳐 보이는 문제가 이미 있다. 동결 replica를 변경하지 말라는 요청에 따라 그 수치를 유지했다. 이는 원본 이미지와의 알려진 차이다. 신규 한국어 fixture에서는 이 겹침이 없도록 검수했다.
- 12×6 정수 슬롯의 양자화 때문에 본문/카드 간격이 source와 다를 수 있다. 구체적으로 Tide08 callout source bbox[210,553.34,860,23.89]는 슬롯[210,565.285,860,79.715]에 놓여 문장 시각 중심이 약40px 아래로 내려간다. 이를 숨기는 페이지 CSS나 전체 장면 패널은 만들지 않았다. Rulemark02의 목차 열, Filament05의 사진/본문 배치, Lamella19의 일정표 구획에도 그리드 비율 차이가 있다.
- Rulemark09의 밝은 단계 면은 읽기 쉬운 palette foreground를 사용하여 원본의 흰 글자와 다르다. source를 재현하기 위한 일부 밝은 반전 면은 해당 데이터의 팔레트 바인딩으로 흰 글자를 유지했다. 밝은 사진 placeholder 위 source의 흰 문구(Cutfield06)는 replica의 대비 문제도 물려받는다. 이 조립본 문맥과 신규 fixture 대비 검사는 구별한다.
- Portico02의 목차10개는 독립5행 두 열로 해석해 foundation panel로 묶었다. 전체를 계약 최대 멤버 초과 gap으로 버리지 않았다. Toggle12의 위 화살표는 hub와 표를 묶는 panel의 연결 장치다.
- Lamella20의 source 파이 실제 조각40/30/30과 source 라벨30/30/40의 불일치는 검증 조립본에서 그대로 보존했다. 새 fixture의 값과 라벨은 일치한다.
- Filament01 Branding의 왼쪽−14px 출혈은 frozen replica의 의도된 페이지 가장자리 잘림이다. 실제 텍스트 Range 검사에서 이 source 출혈만 별도로 기록하고 새로운 페이지 밖 글자 오류와 구분했다.
- 실제 로드할 수 있는 README 허용 폰트 중 가까운 글꼴을 썼다. Lucide로 대체한 아이콘은 원본 그림과 획/자형이 다르다.8px보다 작은 source 글자는 확장된 타입 토큰의 하한8px를 따른다. 원본의 부드러운 색조는 팔레트 자리와 preview palette로 옮겼으므로 색 보간/렌더링 차이가 있다.

## 보존과 배포

동결 replica192개 파일은 SHA256로 보존 여부를 검사한다. 소스 ZIP은 컬렉션 최상위 폴더1개와 허용된.css/.json/.md/.html만 포함한다. 검수 ZIP에는 지도·최종 크기별 시트·요소 대조·조립 소스/PNG·원본/replica/조립 비교·검수 증거를 담는다. git 명령은 사용하지 않는다. GitHub REST API로 기존 main의 트리를 보존한 새 commit을 만들고 force:false로 반영하며, 올라간14개 ZIP을 고정 commit에서 다시 내려받아 SHA256/CRC/멤버/PNG 크기를 검사한다.

