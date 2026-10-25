# Round5 — cutfield

## 새 디자인 폴더 ← replica 페이지

- `card--bands` ← 03
- `card--phase` ← 12
- `chart-bar--grouped-cost` ← 04
- `image-frame--wide` ← 02
- `positioning--named-axes` ← 09
- `versus--facing-planes` ← 07

## 패널을 쓴 곳

- 06 / 06-r5-furniture-31: White cut-corner panel containing sourceheadline and3-arrow convictions list.; bbox [795, 205, 389, 411]

## 차트 확장

- `chart-bar--grouped-cost` ← 04; 묶음/조각/공유축/주석은 요소가 소유한다.
- `positioning--named-axes` ← 09; 묶음/조각/공유축/주석은 요소가 소유한다.

## 지운 일반 요소

`agenda`, `architecture`, `balance`, `bullet`, `callout`, `chart-area`, `chart-bar`, `chart-donut`, `chart-line`, `chart-scatter`, `chart-stack`, `chart-waterfall`, `code`, `concentric`, `cycle`, `decision-tree`, `delta`, `flowchart`, `funnel`, `gauge`, `heatmap`, `hierarchy`, `hub`, `journey`, `legend`, `logo-group`, `matrix`, `matrix-nine`, `metric`, `mindmap`, `network`, `person`, `pill`, `positioning`, `pricing`, `pyramid`, `radar`, `roadmap`, `sankey`, `slope`, `sparkline`, `swimlane`, `tag`, `treemap`, `venn`, `versus`, `waffle`

공통 상태 fixture는 선택이므로 기존 필수 예시를 6개 제외하고, source 기반의 새 한국어 fixture와 데이터 변형을 남겼다.

## 남은 gap과 이유

- 없음. 글자 스타일·캡션·측정 잔여물·큰 제목·사진 비율은 gap으로 분류하지 않았다.

## 실제 최종 시트·비교

요소별 `sheets/<design>-light.png`, `-dark.png`, `-replica.png`; foundation도 동일한 크기별 시트다. 실제 열람 증거는 주 담당자의 `root-final-review.json`의 최종 PNG 해시와 아래 담당자 기록에 연결한다. 조립 비교는 `compare-reassembled/slide_NN.png`이다.

### review-round5-charts

# Round5 차트·포지셔닝 검수

chart-bar--grouped-cost ← replica04. 4series×3group을12독립bar로풀지않고group/category/keys/자체축으로복구. source43pxbar·9pxgap·218pxgroup·13pxinsidevalue·8pxaxis/keys비율. 첫시트의작은범례세로범위/하단category초과98건을직접보고범례최소12pxheight와480px미만plot footer12px로새작성수정. source499px높이의정확한plot462px은유지. 최종26칸9QA0/원문0. 두모드전행·native최소칸을직접열었다. 실제본파일review/sheets/chart-bar--grouped-cost-light.png·dark.png,build/chart-bar--grouped-cost-review/*-all-minima.png.

positioning--named-axes ← replica09. 실제496×454교차축,60px경쟁사원/86px자사원과40pxlogo좌석,각하단14pxname,축명15px를source에서새작성. 축endpoint를가짜로채우지않고한span을축명으로해석. --r0..100으로크기를지원하며긴이름·5멤버변형포함. 최종18칸양모드9QA0/원문0, 모든행·native최소칸을직접열었다. 실제본파일review/sheets/positioning--named-axes-light.png·dark.png,build/positioning--named-axes-review/*-all-minima.png.

### review-round5-diagrams

# Round5 diagrams 검수 — cutfield

신규 2개 디자인, 원본 2개 인스턴스, 최종 64개 light/dark 크기별 셀을 직접 열어 확인했다. 9개 자동 지표·raster·복제 문구 검사·정적 계약 오류는 모두 0이다. 원본 replica는 수정하지 않았다.

## 출처와 크기

- `image-frame--wide` ← replica 02. 40칸. logistics-site: min 3x1, research-workplace: min 3x1.
- `versus--facing-planes` ← replica 07. 24칸. customer-care: min 6x3, warehouse-methods: min 6x3.

## 판단·잔차

- 07의 서로 마주 보는 두 절단면, From/To, 쌍별 본문과 괘선을 versus 한 요소가 소유한다. marker를 임의로 추가하지 않았다.
- 단순 레이아웃 top319가 실제 SVG 글자 Range ascent를 자르는 것을 확인하여 실제 면과 텍스트 Range의 union [0,307.932,1280,412.068]을 사용했다. source 잉크 좌표를 유지하며 52.068px 머리 공간과 1.014px 두 번째 글자 오프셋을 비율로 보존한다.
- 02는 가로로 긴 회색 사진 좌석이다. image-frame--wide의 seat를 n2로 사용하며 원본처럼 표시 숫자를 비운다. source CSS 좌석은 #e7e7e7, 표준 팔레트 및 source-preview의 근소한 회색 차이는 역할 변환 잔차다.
- 원본 From/To의 밝은 강조색은 표준 대비를 위해 강조 단계 역할을 사용하므로 원본 팔레트와 명도 차이가 남는다. 직접 RGB나 페이지 조건은 넣지 않았다.

## 실제 렌더 확인 기록

마지막 소스 변경 뒤의 native 패널과 각 셀 PNG SHA-256, 원본 크기 대조 PNG의 SHA-256은 같은 이름의 JSON에 기록했다. native 패널은 원본 셀 이미지를 축소하지 않고 배치한 확인 자료다. 요소 안의 글자/면 경계, 두 모드 대비, 정렬, 작은 칸의 유지, 연결 방향을 확인했다. 새 unexpressible은 없다.

전체 페이지 조립, 공유 foundation, 최종 공개 패키지는 주 에이전트가 별도로 통합 검수한다. 이 기록은 담당 요소의 최종 소스·크기별 시트·source bbox 대조에 대한 기록이다.

### review-round5-systems

# Round5 foundation 최종 담당 검수 기록

담당 소스는 동결했습니다. replica는 수정하지 않았습니다. root의 통합 페이지 검수와 최종 수락은 별도입니다.

01–13의 측정 제목·caption을 HTML glyph 행으로 옮겼습니다. 02 Mission target은 기존 지도에서 빠졌던 실제 SVG [526,158,65,65]를 추가했습니다. 03 세 underlay의 source 자리는 a1/a2/a2이며 최하단 원본 픽셀도 lime임을 확인했습니다. 06 흰 cut-panel에 headline/list를 중첩했고 면 clip은 자신의 pseudo container를 참조하며 source28px notch를 토큰으로 제한합니다. panel.on은 source11의 진한 면 문맥을 제공합니다.

타이포 수치는 실제 source DOM/Range/loaded font를 읽어 요소 상자 비율로 옮겼습니다. SVG text는 선택 가능한 HTML로, source 인장은 실제 글자 좌표/회전으로 그렸습니다. 폰트 크기는 공유 type8–256과 cqw/cqh의 clamp를 사용하며 디자인 색상은 팔레트 자리만 사용합니다. 장면 selector나 fixture별 CSS 보정은 없습니다.

source 장치 31개, 기존 중복 제거 ID 18개입니다. source 페이지/정확 bbox/완전 원문 markup 및 nested source_children은 build/map-round5-systems.json에 있습니다. 불필요한 원문 fragment/측정 dump는 새 장치로 만들지 않았습니다. 담당 신규 unexpressible은 없습니다.

최종 size matrix는 foundation/fixtures 12개, 양모드 합 152칸입니다. review/validation/foundation.json의 9종 QA는 모두 0입니다. proof source_hashes는 실제 현재 파일과 일치합니다. 새 한국어 fixture와 전체 frozen replica의 정규화 6자 중복 검사도 0건입니다. 원문은 검증 조립 markup에만 둡니다.

실제로 연 최종 자료: review/sheets/foundation-light.png와 foundation-dark.png를 그대로 보존한 root-sheet-pairs/cutfield-foundation-part01.png부터 part03.png까지 모든 행의 양모드 pair를 직접 열었습니다. 작은 칸에서도 도형/선/표/문자가 겹치거나 잘리지 않는지 확인했습니다. 별도로 직접 연 native 칸: r5-vector-target-light-3x3.png, r5-corner-underlay-dark-12x6.png. 앞선 source/native 검토와 이번 마지막 렌더 파일 검토는 구분하며, 최종 전체 페이지 원본|replica|조립본 비교는 주 에이전트 담당입니다.

거대 native PNG는 바꾸지 않았습니다. 축소 pair manifest에는 각 원본 SHA256·크기·source hash current 여부·chunk 행/좌표가 기록되어 있습니다. 이 자료의 상태는 awaiting_root_visual_review이며 자동 수락하지 않았습니다.

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

