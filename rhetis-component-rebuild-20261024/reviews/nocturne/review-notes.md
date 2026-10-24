# Nocturne rebuild 검수 기록

## 자료와 계약
README220줄과 새 사용자 요청 전문을 끝까지 다시 읽었다. 기존 replica HTML6개와 공통 CSS의 시작 SHA와 마지막 SHA를 대조했다: **불변 일치=True**. 이7파일의 목록은 `build/replica-source-lock.json`에 있다. 이전 element.css를 읽어 고치거나 덧붙이지 않고 모든56개 CSS를 새 루트에서 처음부터 작성했다. 자동 검증기는 기존 바이트와 같지 않음을 비교할 뿐 디자인 소스로 읽지 않는다. kit/foundation은 주 에이전트가 별도로 새 작성했다.

`map.json`은 페이지 전체 면·브랜드·연도·표지 장치를 포함한44개 시각 항목과 실제 브라우저 측정 수치를 담는다. bbox는1280×720 replica 픽셀이다. 반복 인스턴스도 지도에 남기고 대표 base는 하나만 지정했다.

## 소스 대응과 판단
- 20 KPI는 채워진 원이므로 card다. 표면 없는 metric으로 위장하지 않는다. 원316px·윤곽3px·이름36/600·숫자60/800·간격9를 실제 작은 변 길이의 비율로 옮겼다. 큰 칸에서도 원은316px를 넘지 않는다.
- 19 캡슐은65px 높이·2px 윤곽·28/550 이름·수평패딩30의 pill이다. 글자는 flex 양축 중앙과 렌더 잉크 중심을 함께 확인한다.
- 19 headline은32px kicker와58px fading-dot,88.3px 표시 제목으로 측정했다. 공유 타입 상한88 내의 같은 비율을 쓴다. 작은 칸에서 kicker와 도트를 먼저 생략하고 h2를 보존한다.
- 20 callout은 세 점과26/350 결론 문장 전체를 한 요소가 소유한다.23 prose는956×3 괘선·57px 간격·32/350/1.7 본문이며 첫 줄만700이다.19 prose.quiet은25/350/1.4 회색 두 줄이다.
- 22 패널을 list의 대표 base로 지정했다. **source가 실제 보인 상태는 계약의 `.divided`**다. 기본 dot·num·check 표식은 동일 패널 언어의 새 설계이며 source에 있던 것으로 주장하지 않는다.1052×372/윤곽3/r25/행84/글자34/점선2를 옮겼다. 최종 점검에서 cqh의 content-box336px를 분모로 바로잡아 큰 칸 글자가30.7로 작아졌던 오류를34로 복구했다.
- Source에 없는50 leaf는19의 캡슐,20의 원과 얇은 윤곽,22의 점선 행,23의 면 없는 문장 언어에서 확장했다. 예시 컬렉션의 CSS·색·장식을 쓰지 않았다. source가 있는 것처럼 새 매핑을 지어내지 않았다.
- 조건 분기 `.ask`는 source의 둥근 패널에 점선 윤곽을 써서 구분했다. 새 다이아몬드 장식을 도입하지 않았다. Sankey는 원에서 캡슐로 나오는 실제 두께 비례 fan-band와 두 번째 분기를 그린다. 연결선·화살표·링·밴드는 연결된 멤버를 모두 가진 요소가 소유한다.

## 새 문구와 모범 fixture
전체147fixture. 비모범 문구는 한국어 실무 내용으로 새로 썼고 모든6개 immutable replica를 합친 corpus에 대해NFKC·소문자·공백/문장부호 제거 후 연속6문자 창을 검사했다. 충돌 **0건**. SQL의 테이블은 `case_log`로 썼다.

README의 모범28fixture는 구조와 수치 데이터를 그대로 보존했다. 다만 `card-2-quiet`의 설명 한 문장이 replica와6자 이상 겹쳤다. 최신 직접 요청의 복제 금지와 충돌하여 주 에이전트의 명시 결정에 따라 그 문장만 `기록과 지표가 한곳에 모여 바로 결정을 내립니다.`로 바꿨다. 이1건은 문구 규칙을 우선한 예외이며 모범의 마크업·숫자는 보존했다. 모범 원본의 wrapper·row5/span2·기호 아이콘 같은 형식은 동일 마크업 우선으로 보존하고 추가 fixture는 표준 배치·빈 Lucide 자리를 썼다.

## 반응형·품질 점검
모든 루트는 data-el 범위와 `container-type:size`를 가진다. cqw/cqh와 명명된 자식/멤버 수만 사용한다. 사용자 새 요청에서 명시 허용한 `clamp(type토큰,상자비율,type토큰)`를 README의 연속 크기 금지보다 우선했다. 픽셀 글자 크기나 glyph-scale로 상한을 우회하지 않는다. raw scroll-overflow flag는384case에 남는다. 이는 chart막대 밖의 축/값, dot 바깥의 label, 연결선용 pseudo box, band/curve가 자기 작은 member를 벗어나는 경우다. 연결된 전체 요소 root 안에 실제 도형·문자는 유지되며 자동 outsideText/clip0과 칸 밖6px 포함 시트 전칸 눈검사로 분리 확인했다. scrollWidth가 각 작은 부품보다 크다는 사실을 실제 칸 초과0으로 바꿔 적지 않았다.

색은 팔레트 자리뿐이며 코드는 실제 Nanum Gothic Coding 토큰을 사용한다.

- 크기별 시트는 요구9크기 중 min 이상인 모든 칸과 min 자체를1280×720 grid에서 실제 렌더하고 칸 주위6px를 남겨 잘랐다. fixture마다 한 줄, light/dark 각각 한 장이다. 마지막 렌더에 픽셀 위치를 이용한 실제 배경 대비 검사도 포함했다. 최종112개 양모드 PNG의 전칸을 마지막 소스 수정 뒤 직접 재검수했다.
- 잘림/넘침/겹침: 텍스트 Range, 영역 경계, root0, 숨김 필수 부분을 검사하고 모든 leaf의 양모드 전칸을 직접 봤다. 단순 칩부터 복잡 도표까지 min을 구분했다. 추가 작은칸 probe 후 codeSQL6×5, matrix-nine6×4, nestedtreemap6×6, steps6은8×4로 최소칸을 낮췄다.
- 정렬: 카드 제목과 숫자 기준선, capsule 상하좌우, pricing의 제목/가격 시작점, 차트 라벨 baseline을 확인했다. 아이콘은 자체 badge 안의56%로 두었다. 진단 시트의 전역 small/frame 규칙과 충돌하지 않게 범위를 방어했다. 실제 잉크 중심530개 측정에서 최대 수직편차1.39px이며 숫자별 glyph차이 범위다.
- 차트: 실제 데이터로 막대·점·선·채움·누적·폭/면적을 그렸으며 축/범례/값이 자기 도형과 충돌하지 않도록 분리했다. source에 없는 임의 연결선은 만들지 않았다. 두 시리즈 이상에서도 한 강조만 두드러지게 했다.
- 수정한 실오류: anchor containing-block으로 사라졌던 line/area/sparkline의 선을 root 좌표로 복구; root padding을 두 번 빼서 어긋난 막대/폭포 baseline 수정; hub 연결선을 node 가장자리에서 멈춤; calendar 정사각; treemap 면적 비례; decision-tree 추가 stub 제거; radar의 불투명 그림자 제거로 겹친 시리즈 복구; list content-box 비율 수정.
- 장식: 원/점선/도트는 정보 구조에 필요한 위치만 사용했다. 의미 없는 샘플 장식은 남기지 않았다. dark는 별도 실제 렌더로 확인했다.
- 계약 정적 검사: **56요소/147fixture, 오류0, 경고0**. 검증 파일은 `contract-new.json`, 문구 검사는 `copy-audit.json`이다.

`size-summary-all.json`: {"collection": "nocturne", "leaves": ["agenda", "architecture", "balance", "bullet", "callout", "card", "chart-area", "chart-bar", "chart-donut", "chart-line", "chart-scatter", "chart-stack", "chart-waterfall", "code", "concentric", "cycle", "decision-tree", "delta", "flowchart", "funnel", "gauge", "headline", "heatmap", "hierarchy", "hub", "image-frame", "journey", "legend", "list", "logo-group", "matrix", "matrix-nine", "metric", "mindmap", "network", "person", "pill", "positioning", "pricing", "prose", "pyramid", "quote", "radar", "roadmap", "sankey", "slope", "sparkline", "steps", "swimlane", "table", "tag", "timeline", "treemap", "venn", "versus", "waffle"], "sourceSHA256": "6957cb0fac2a27b32b521b535c783bc3957b4855f3cf86ff8bcc3d48071a838f", "sourceUnchanged": true, "cases": 1684, "outsideCases": 0, "overlapCases": 0, "clipCases": 0, "fontFailureCases": 0, "hiddenCases": 0, "zeroCases": 0, "pixelFailureCases": 0}

## 팔레트와 비교 시트
library light/dark는 README 기준 팔레트로 렌더한다. `*-replica.png`와 재조립은 같은 색 역할에 source host 팔레트를 공급해 원본 모양을 비교한다. source의 파랑·검정·회색 값은 컬렉션 CSS에 넣지 않았다. 따라서 기준팔레트에서는 주황 등 다른 색으로 보일 수 있으며 디자인은 원·캡슐·윤곽·간격·타이포와 역할 배치로 평가한다.

## 재조립6장과 차이
새 reassembled HTML은 map대로 계약 마크업과 foundation만 사용한다. 각 body 직접 자식의 inline배치는 정수 grid-column/grid-row뿐이다. 원본/immutable replica/조립본을3840×720 비교 PNG로 한 장씩 직접 봤다. 페이지별 보정 CSS나 다른 의미의 요소로 빈 곳을 메우지 않았다.

-19: 원본은 전체폭1280에서88.3 제목이지만 foundation body는1144이므로 같은 비율의 제목78.9/quiet22.34로 작아진다. 제목 ink bbox는(381.1,221.1,517.8,94), source의 전체폭88.3 제목보다 위/작다. group의 세 동일 grid칸 안에 캡슐을 두므로 원본의 내용폭에 따른 묶음 간격보다 넓게 벌어진다. 원본 고유 중앙 상단 빔/아래 띠는 공통 좌상·우하 광원과 다르다. 페이지전용CSS로 숨기지 않았다.
-20: 원316·이름36·숫자60은 유지된다. 공통1144 body의 등분 group 때문에 원 중심x는251.3/640/1028.7이고 source268/639/1010과 다르다. 원의 상하 위치와 callout의 문자 크기는 받은 grid칸 비율을 따른다. callout 본문은23.24px이며 원본26보다 작다.
-21: 공통 머리글만 조립되며 세 중첩 미디어 패널은 GAPS로 남는다. 사진placeholder만으로 세 텍스트 역할까지 그려진 것처럼 대체하지 않았다.
-22: 패널은1052×372를 유지하나 공통 grid 중앙 정렬로(114,255.5)에 놓여 source(119,233)와 다르다. 배경사진 자리는1144×304의 grid로(68,371)에 놓여 source1280×330/(0,390)과 다르다. 라운드 단색 seat의 번호도 보인다. opaque패널은 회색사진placeholder 위에 얹히며 원본의 실제사진/반투명 합성과 다르다.
-23:204px Q&A+kicker 묶음은 GAPS로 남는다. prose만 조립한다. 가로선은 source956에서854.4로 비례축소되고 본문32에서28.6으로 줄어든다. 큰 제목을128로 바꾸어 충실하다고 주장하지 않는다.
-24: foundation의100px Montserrat 중앙 lockup과 코너 seat를 사용한다. 제목중간에 어두운 shade가 들어가던 실제 오류는 밝은 ink/accent mix로 고쳤다. 원본 3D그래픽은 회색 단색 cornerseat이며 번호가 표시된다. 브랜드 아이콘도 canonical 번호seat이므로 source 로고 도형과 다르다.

원본 작은 문구의 판독/대체 결정은 immutable replica의 기존 기록을 존중한다. 새 컬렉션 fixture에는 원본 문구를 복제하지 않았다. 재조립에서는 replica 문구를 그대로 허용한 사용자 규칙을 따랐다.

## Unexpressible
GAPS.md는 세 유형/다섯 인스턴스만 담는다:19-spotlight-scene,21-media-panel1~3,23-qa-heading.19는 기본 면과 별개의 spotlight/beam 장면을 선택할 명명된 foundation 변형이 없다.21은 사진면과 keyword/두줄 부분굵기 제목/note를 함께 소유할 계약이 없고,23은 표시 타입204가 허용상한128보다 크다. 각 제안마크업은 GAPS에 있으며 실제 컬렉션에는 넣지 않았다.

## 요소별 출처

| leaf | replica 출처/설계 근거 |
|---|---|
| `agenda` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `architecture` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `balance` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `bullet` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `callout` | 20 도트·결론 문장을 직접 옮김 |
| `card` | 20 원형 KPI를 직접 옮김 |
| `chart-area` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `chart-bar` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `chart-donut` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `chart-line` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `chart-scatter` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `chart-stack` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `chart-waterfall` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `code` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `concentric` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `cycle` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `decision-tree` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `delta` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `flowchart` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `funnel` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `gauge` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `headline` | 19 kicker·도트·표시 제목을 직접 옮김 |
| `heatmap` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `hierarchy` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `hub` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `image-frame` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `journey` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `legend` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `list` | 22 패널을 대표 base로 옮김; 관찰된 마크업은 divided |
| `logo-group` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `matrix` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `matrix-nine` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `metric` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `mindmap` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `network` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `person` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `pill` | 19 단일 캡슐을 직접 옮김 |
| `positioning` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `pricing` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `prose` | 23 괘선·본문을 직접 옮김; quiet는19 |
| `pyramid` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `quote` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `radar` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `roadmap` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `sankey` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `slope` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `sparkline` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `steps` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `swimlane` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `table` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `tag` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `timeline` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `treemap` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `venn` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `versus` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |
| `waffle` | 19 캡슐·20 원형 KPI·22 패널/점선·23 면 없는 문장에서 확장 설계 |

## 최종 통화 단위 및 패키징 기준 갱신

주 에이전트가 pricing fixture의 월 과금 단위를 `/월`에서 `원/월`로 고쳐 금액의 통화를 명시했다. 가격 수치·계약 마크업·요소 CSS는 보존했다. 마지막 pricing 라이트·다크 크기 시트를 직접 확인했으며 14개 크기·모드 사례의 영역 초과, 겹침, 클립, 폰트 실패, 숨김, 0크기 및 실제 픽셀 대비 실패는 모두 0이다. 현재 컬렉션 SHA-256은 `dd47629d191f18fb79ab9b105e7a66aa10f93b6b1d8460391b8843760243fcc8`이다. 이 SHA의 전체 56요소 1,684개 사례 최종 집계도 같은 7개 실패 항목이 모두 0이다.

현재 컬렉션의 CSS를 읽는 조립 HTML builder만 실행한 뒤 공용 Chromium 렌더러로 6페이지를 최종 렌더했다. 페이지 본문과 요소 CSS·fixture는 이 지원 단계에서 수정하지 않았다. 원본 | 동결 replica | 조립본 비교 6개를 각각 다시 보았으며, 기존 GAPS 및 정수 그리드 배치 차이 외 추가 오류를 발견하지 못했다. 사용 폰트 실패와 페이지 클립은 0이다. 조립 PNG 6개는 모두 1280×720, 비교 PNG 6개는 모두 3840×720이며 디코딩 무결성을 확인했다.

전체 source comparison도 다시 렌더하여 callout·card·headline·list·pill·prose 6개 요소, 7개 디자인 행의 대조 시트를 각각 직접 확인했다. `size-summary-all.json`, `size-summary-pricing.json`, `reassembled-audit.json`, `replica-comparison-audit.json`의 SHA가 모두 위 현재 값과 일치한다. 조립 audit의 6개 HTML 해시도 실제 소스와 일치한다. 기존 replica HTML 6개와 공통 CSS의 잠금 해시 7개는 여전히 불변이다.


## Native bbox 분모 최종 감사

6개 mapped base와 prose.quiet를 map의 원본 bbox 폭·높이로 임시 진단 할당하여 frozen replica의 실제 DOM과 비교했다. 자식 container를 잘못 분모로 사용해 글자가 축소되는 오류는 없었다. 실제 글자 크기는 pill28→28, card 이름36→36/수치60→59.9999, list34→34, callout26→25.9972, prose32→31.9935, quiet25→25, headline 보조32→31.9973px이다. font-weight는 모두 일치하고 측정된 글자 Range 높이도 전부 일치한다. 본문 headline은 기존 type88 상한 때문에88.3→88px로0.3px 차이가 남는다. 이것은 cqw 분모 축소가 아니다. normal 원본 행상자와 토큰 행간 차이로 Range y 위치의 최대 차이는0.796875px이다.

주요 도형은 원형 card316×316/3px 선, list1052×372/3px 선/25px 반경이 일치한다. headline 점선2×58→1.98438×57.9844, callout 점선4×28→3.98438×27.9844, prose 괘선956×3→955.797×2.98438px의 미세 반올림 차이가 있다. pill 높이65·선2·수평 padding30·반경999px가 일치한다. 다른 문구의 가로 글자 폭을 원문과 동일하다고 주장하지 않는다. `native-source-audit.json`에 원본/요소 computed DOM과 Range·수치 비교를 기록했다. 이 감사는 production CSS·fixture·페이지를 바꾸지 않았으므로 앞의 최종 SHA와 렌더 결과가 유지된다.
