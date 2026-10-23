# 검수 기록

## 원본 재현 1차
- 실제 Chromium 1280×720 렌더 후 원본|replica 나란히 비교했다.
- 우측 건축 사진과 브랜드 이미지 로고는 요청대로 연회색 단색 placeholder로 치환했다. 사진 영역의 모듈별 직각 마스킹과 파란 정사각형은 직접 구현했다.
- `Thank You!`, 연락처와 본문은 읽을 수 있어 그대로 전사했다. 판독 불가로 지어낸 문구는 없다.
- 원본 영문 폰트명은 확정할 수 없어 README 지원 글꼴 Pretendard Variable을 선택했다. 글자폭이 원본과 약간 다르다.
- 제공 덱은 마지막 한 장뿐이다. 보이지 않는 56종 요소는 이 페이지의 직각 모듈·헤어라인·작은 채움 라벨에서 확장한다.
- 기본 sandbox에서는 Chromium 실행이 차단되어 승인된 확장 실행으로 로컬 HTTP를 사용했다. file URL은 관리 정책으로 차단되었고 HTTP 렌더는 성공했다.

## 요소 검수 및 수정
- 형식 검사: 56개 계약 폴더, 174개 fixture, 공유 토큰, 모범구성 마크업·데이터를 검사했다. static errors 0 / warnings 0.
- 1차 대표 렌더에서 line 연결선이 누락되고 area가 계단형으로 보이는 문제를 발견했다. anchor()를 width에 사용한 것이 원인이므로 inset 기반 연결선으로 변경했다. area는 실제 --v 값을 앵커로 잡아 연속 영역을 만들고, 누적 시리즈는 첫 시리즈를 앞으로 그려 모든 층이 보이게 했다.
- cycle의 순환 화살표, hub의 방사 연결선, mindmap의 중심 연결선, sankey의 흐름 밴드를 추가했다. code는 실제 Nanum Gothic Coding 폰트를 키트 확장 토큰으로 공급했다. sparkline 기본형은 연결선, bars 변형은 막대로 구분했다.
- 작은 슬롯에서 agenda·architecture·funnel·pyramid·table·waffle·bullet·gauge·delta·metric의 내부 간격과 글자 단계가 과대한 문제를 수정했다.
- 기준 팔레트의 a1은 작은 글자에서 대비가 부족하여 본문성 강조에는 a1-7을 사용한다. 라벨 채움은 a1과 a1-on을 유지하고, 단위 small은 주변 색을 상속한다. heatmap의 명도 범위는 읽을 수 있는 옅은 면 안에서 바뀌게 했다.
- 독립 replica는 원본의 직접 재현이다. 재조립은 실제 12×6 그리드와 계약 요소만 사용하므로 연락처 라벨·행의 높이, 제목과 부제 사이 간격, 사진 모듈 너비에 소폭 차이가 있다. 재조립의 회색 사진 자리는 이미지를 대체하기 위한 의도된 차이다.
- reassembled HTML은 collection의 foundation과 요소 CSS를 직접 링크한다. review/style.css는 타입 단계와 팔레트, 브라우저 기본 margin 제거만 제공하며 페이지 배치를 새로 정의하지 않는다.
- 네이티브 1280×720에서 글꼴 로딩 성공과 슬라이드 실제 치수를 확인했다. 마지막 수정 후 통합 렌더/자동 검수는 주 에이전트가 수행한다.

## 최종 자동 검수 결과
- 최신 CSS로 모범 fixture 포함 174개 fixture를 라이트·다크 양 모드에서 검사했다. 총 348 fixture-mode, 선언된 최소 크기에서 12×6까지의 정수 그리드 10,170개 크기 조합에서 findings 0.
- 검사 범위: 요소/텍스트의 슬롯 초과, 숨김 영역의 텍스트 잘림, 전체 크기에서의 텍스트 대비, 폰트 오류, chip의 시각적 중심 좌표.
- 최종 라이브러리 시트는 실제 preview.py 출력이며 foundation 및 56개 요소 폴더별 PNG를 라이트·다크 각각 57장 생성했다.
- 원본 collection과 review/collection 복사본의 모든 파일 SHA를 대조하여 동일함을 확인했다. 이 CSS로 페이지 최종 렌더를 수행한다.

- 최종 PNG 직접 비교에서 다중 area의 낮은 시리즈 마지막 값이 앞 시리즈 면 뒤로 가리는 문제를 추가 발견했다. 다중 area에 한해 마지막 값을 위 범례의 자기 이름 옆에 배치해 모두 읽히게 했다. 단일 area의 포인트 값은 기존 위치를 유지했다. 변경 후 해당 요소를 같은 크기 범위에서 재검사한다.

- 다중 area 값 가림 수정 뒤 전체 정수 그리드 검사를 다시 실행했다. 최종 결과도 348 fixture-mode / 10,170 grid sizes / findings 0이다. 마지막 library PNG/PDF에 이 수정이 반영된 것을 직접 확인했다.
- 페이지 text-range 경고 두 건은 96px 제목의 폰트 메트릭이 line box를 넘는 경우다. 브라우저에서 제목 전체가 보이며 overflow로 숨기는 영역이 없고 페이지 영역도 넘지 않으므로 실제 잘림으로 판단하지 않았다.

## 통합 검수 추가 수선
- 주 에이전트의 직접 PNG 검수에서 line의 각 점 오른쪽에 불필요한 수평 가지가 남는 문제를 발견했다. 양방향 연결선의 min-height가 잘못된 방향에도 2px 높이를 남긴 것이 원인이었다. 상승/하강 높이를 각각 anchor-size 차이의 max(0px, diff)로 정해 반대 방향은 0이 되게 하고, 평평한 구간만 별도 선으로 그렸다. 새 PNG에서 가지가 사라지고 44→44의 평평한 연결도 유지됨을 확인했다.
- 이 최종 line 변경은 8 fixture-mode, 가능한 정수 그리드 282개 크기에서 다시 검사하여 findings 0이었다(`line-final-audit.json`).
- spacing 리터럴 세 곳은 같은 픽셀값을 유지한 공유 토큰식으로 치환했다: heatmap 96px = rail-w(72px)+gap(24px), sparkline/waffle 2px = stroke(1px)×2.
- 마지막 변경 후 라이트·다크 HTML·요소별 PNG·PDF를 다시 만들었고 portable 복사본 SHA가 모두 일치한다.

- sparkline 기본 선에도 같은 min-height 가지 문제가 있어 동일 원리로 수선했다. 각 점의 y값을 anchor 높이로 표현하고, 실제 방향의 차이만 선으로 그리며 평평한 구간만 1px을 허용한다. bars 변형은 유지한다.
- 최종 chart-line+sparkline 14 fixture-mode, 가능한 정수 그리드 634개 크기에서 findings 0(`line-spark-final-audit.json`). 라이트·다크 PNG를 다시 직접 확인했고, 부정확한 수평 가지가 사라졌다.
- 모든 수선 뒤 최종 portable 복사본의 SHA 일치를 다시 확인했다.

## 카드 행 정렬 통합 수선
- 동일 행의 카드 제목이 note의 줄 수에 따라 약 10.84px 어긋나는 문제를 주 에이전트가 추가 발견했다. parts 전체의 콘텐츠 높이를 기준으로 중앙 정렬하던 것이 원인이었다.
- card 내부를 역할별 grid로 바꾸어 mark/fig/seat 영역과 두 줄 name 영역을 예약하고, note의 시작을 그 아래로 고정했다. 위아래의 동일한 가변 여백으로 전체 무게 중심을 유지한다.
- 최종 card+chart-line+sparkline 30 fixture-mode / 832 grid sizes에서 findings 0, 동일 행 카드 name의 최대 y 편차 0px을 확인했다(`card-line-spark-final-audit.json`).
- 최종 카드 라이트·다크 PNG를 직접 확인했고, 모든 변경 뒤 컬렉션 원본과 review/collection의 SHA 일치를 다시 확인했다.

## 현행 계약 마크업 정규화
- 비모범 pricing/versus/person/matrix fixture에 남아 있던 샘플의 옛 ul.list/li 구조를 현행 .list > .item > .name(.note) 구조로 바꿨다. 모든 중첩 list와 추천 tag에 각 요소의 data-el을 부여했다. 6종 모범구성 fixture는 변경하지 않았다.
- 중첩 list가 내용 높이를 실제로 갖도록 네 요소 안에서 inline-size containment를 사용했다. person 단일 프로필은 사진과 문장을 나란히 배치해 작은 칸에서도 사진·이름·경력 목록을 보존했다. pricing은 tag/name/price/list 역할 영역을 예약해 계획별 제목·금액 시작선을 정렬했다.
- matrix의 축 부품을 계약 순서로 정리해 첫 번째 cell이 왼쪽 위에 오도록 했고, y축은 높은 성장률이 위에 오도록 배치했다. SWOT의 목록도 실제 item/name 구조로 표시한다.
- 완전히 같은 복제 fixture였던 pricing/legend/tag의 두 번째 fixture는 각각 2개 플랜·3개 긴 범례명·다른 긴 비즈니스 문장으로 차별화했다. versus의 두 번째 fixture도 연도만 바뀌던 구성을 실제 긴 이름과 두 항목/긴 note 비교로 바꿨다. 현재 완전 동일 fixture는 없다.
- 최종 정규화 관련 6요소 26 fixture-mode / 670 정수 그리드 크기에서 findings 0(`contract-normalization-audit.json`). 실제 1280×720 PNG에서 목록 표현, 가격 행 정렬, 축의 의미, 긴 프로필/비교 문구를 직접 확인했다. 마지막 portable 복사본과 컬렉션 원본 SHA가 일치한다.
- 최종 고해상도 전체 시트 export는 주 에이전트가 담당한다. 이 정규화 후 collection과 review/collection 모두 최신 상태다.


## 원본과의 정밀 재비교
- 050/052의 사용자 시각 거절 이후 045도 freeze를 해제하고 원본·replica·조립본을 다시 개별 비교했다. 기존 조립본은 대제목이 약 11px 위이고 CONTACT가 11px 아래였으며 연락처가 과대했다.
- 원본 텍스트의 래스터 경계를 직접 측정하고 실제 로드한 폰트 후보를 비교했다. 대제목은 Pretendard Variable 96px·800·자간 0, 연락처는 Noto Sans KR 16px·26px 행간을 선택했다. 이미지로 원래 폰트명을 확정할 수 없으므로 이 선택은 재현에 가장 가까운 해석이다.
- 최종 원본/조립본 검정 글자 경계: 제목 시작 (105,246) 동일, 제목 끝 x611/610; 부제 시작 (109,358) 동일, 끝 x680/681; 브랜드 시작 (147,119) 동일, 끝 y135/136. CONTACT 채움은 (107,485)–(215,515)로 동일하다. 연락처 전체 시작 y543 동일, 끝 y634/635로 1px 차이가 남는다. replica에도 같은 타이포를 반영했다.
- headline의 광학 정렬이 요소 영역 바깥으로 튀어나오지 않도록 foundation 그리드의 시작점을 조정했다. 이미지 프레임도 독립 replica의 8개 직각 면과 같은 union 마스크로 수정했다. 단순 도형인 왼쪽 세로 띠는 x0–10/y72–162로 복원했으며 원본 사진과 이미지 로고만 회색 placeholder다.
- 최종 정밀 수정 관련 5요소(card/headline/tag/table/image-frame) 42 fixture-mode / 1,112 정수 그리드 크기에서 findings 0(`precise-layout-audit.json`). 비모범 card fixture의 텍스트 아이콘도 empty span.icon/data-icon으로 정규화했고, 정확한 마크업을 요구하는 모범 card-4는 보존했다.
- 마지막 수정 후 PNG/PDF/양쪽 비교 PNG를 다시 렌더해 실제 페이지를 열었다. 모든 원본·replica·조립본 페이지 PNG는 1280×720이다.


## 최종 시트 직접 관찰 후 두 요소 수선
- hub spoke의 translate transform이 별도 stacking context를 만들어 음수 z-index 연결선도 spoke 배경보다 앞에 나타났다. transform 없는 등가 좌표로 변경해 선을 hub context의 배경 층에 두고 spoke/core 면에서 가려지도록 수정했다.
- chart-line의 동일값 전용 연결은 1px 래스터 선이었으나 시트 export에서 끊겨 보인다는 통합 검수에 따라 같은 값인 경우에만 명시적인 2px 수평선이 생기도록 강화했다. sign/abs 함수가 실제 Chromium에서 지원됨을 확인했다.
- 두 요소의 최종 14 fixture-mode / 424 정수 그리드 크기에서 findings 0(`hub-line-audit.json`). dark 3-spoke hub/12점 line, light 6-spoke hub/미세 변화 line을 각각 실제 PNG로 열어 선이 글자를 가로지르지 않고 동일값 구간이 끊기지 않음을 확인했다.

## Native 요소 전수 검수와 의미 보정
- 축소 연락처 시트 대신 각 fixture를1280×720로 출력한 라이트·다크 총352패널을 직접 열어56요소와foundation을 모두 읽었다. bounds/contrast0만으로 기능을 통과시키지 않았다. 초기25요소에서 관계선·축·실데이터 의미 오류를 발견했다. 상세 baseline과 열람PNG의mtime/SHA는 `library-visual-review.md`에 남겼다.
- balance에 실제 빔·받침을 추가하고 음수tilt일 때 왼쪽이 내려가도록 복구했다. bullet 목표tick을 실제track 행에 고정하고 qualitative bands와 note를 보존했다. 범위0–100 계약을 넘던 비모범fixture의104%는98%로 교정했다.
- cycle의3/4/6 순환선과 화살촉을 node면 뒤로 옮기고 화살촉을 edge중간에 놓았다. decision-tree 질문→가지→조건→결과, hierarchy 부모→본부→형제leaf, flowchart/swimlane4방향과 화살촉을 실제 연결했다. mindmap은 면 뒤의 곡선으로 중심과 방사 branch를 이었다.
- journey의 감정곡선을 stage 전체에 연속 연결하고 pain유무와 관계없이 같은 행의 제목·note 시작높이를 예약했다. matrix-nine은 축과9cell의 명시적3×3배치/low아래·high위 축으로 복구했다. positioning y축도 세로로 정정했다.
- chart-bar의 긴 가로라벨을 별도 폭에 줄바꿈해 plot침범을 제거했다. funnel의35%최소폭과 treemap의20%최소폭을 제거해 --v에 비례하도록 그렸다. stat 내부sparkline에 명시적 높이를 공급해 실제추세가 보이게 했다. timeline 선은 연속으로 잇고 alt는 선의 위아래로 교대 배치했다. venn3은 세원 공통영역과 투명한 팔레트 역할채움으로 교집합을 드러냈다. 다섯번째legend는 중립역할로 구별했다.
- 통합 담당의6요소 수선: code행번호1–9와monospace, chart-stack계열별색과분할, chart-scatter의식별 가능한점/강조, chart-waterfall의1241누적합/연결, radar의3–8축다각형·격자·spoke·범례, sankey의2단계band를 복구했다. fixture최소칸은 stack-h-4=10×3, sankey6=8×4로 조정했다.
- 본인19요소 최종114fixture-mode/2,972정수그리드에서0 findings, 마지막5관계도24fixture-mode/580그리드에서0 findings를 확인하고 각변형의실제연결/비율을 다시 직접 열람했다. 마지막native export와전체fixture검사를 거쳐 최종PNG해시의56개판정을 별도JSON에 기록한다.
- 최종 해시 대조에서 funnel이 수선 전PNG와 동일한 것을 발견해 `min-width:35%` 잔여를 제거했다. 3/5/6stage 양모드에서34%와24%가 서로 다른 실제 너비로 줄어드는 것을 직접 재확인했고188그리드0을 확인했다.
- 누적차트4fixture에는 계열을 명시하는 own-legend를 중첩했다. legend key의 채움은 실제seg순서와 같은 a1/n-4/n-2/a1-2-soft를 사용하며 축문구와 분리된 하단자리를 예약했다. 마지막8fixture-mode/200그리드0 및8native패널의색·명칭·간격을 확인했다.
- 최종 공식시트는57leaf, 모드마다176native1280×720패널과176PDF페이지다. 시트PNG너비는1280이며 높이는leaf별fixture수에 따라40+760×N이다. 최신 전체348fixture-mode/10,070정수크기에서0 findings, static errors0/warnings0이다. 56요소의 실제관찰근거와최종light/dark PNG SHA를 `library-visual-audit.json`에 저장했다.
- 마지막 portable→pages렌더 이후 replica/조립본1280×720과왼쪽x0~10/y72~162단순파랑띠를 확인했다. 원본/replica/조립본을 실제비교했고, 렌더시읽은HTML/CSS/폰트해시와현재소스가일치한다. 컬렉션원본350파일과review/collection350파일도SHA동일하다.


2026-10-23 최종 호스트 CSS 정리: 조립본이 읽는 style.css의 html/body margin·width·height 규칙을 제거했다. foundation의 body > .slide 규칙에서 단독 페이지를 viewport 원점에 배치한다. 호스트 CSS는 팔레트 및 37개 type custom properties만 제공한다. replica CSS는 유지한다. 화면 동일성과 최종 렌더·실제 폰트 해시는 재검증한다.
최종 확인: 기존 PNG 118개(페이지·비교·library)의 SHA-256 모두 동일. 공식 pages 재렌더 후 replica/조립본 모두 1280×720, fontErrors 및 problems 0. 실제 폰트 감사 2페이지 findings 0이며 sourceFingerprint fd49d26dac9f42acc6cdc974e175e627cb2d19d765015a7f8b991bcab21c052b로 갱신했다.
추가로 호스트 custom properties 파일을 assets/host-custom-properties.css로 옮겨 최종 렌더·폰트 지문에 포함했다. 이동 뒤 다시 pages와 font audit를 실행했고 PNG118개 SHA는 모두 동일하다. 최종 fontFingerprint 6788a533b2ddfc38c6df7d637390016eb860c4f1b7803cb80763e2dc6e377475; actual font audit2페이지 findings0.


## 주 에이전트 최종 통합 판정

원본별 개별 비교 회차와 마지막 변경 화면 재열람 후, 최신 비교 PNG·소스·실제 폰트 지문을 최종 승인 기록에 묶었다. 자동 bounds 검사와 시각 검수는 별도 근거다. 사진·복잡 이미지의 요청된 회색 대체, Lucide 치환, 가장 가까운 허용 실폰트와 안티앨리어싱의 미세 차이를 픽셀100% 동일로 표현하지 않는다. 렌더 뒤 일반 호스트 CSS·팔레트 의존성과 컬렉션 복사본 SHA를 다시 확인했다.
