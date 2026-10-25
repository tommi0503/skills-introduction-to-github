# Cinder Pulse Round5 최종 기록

상태: 요소 CSS와 map 동결. 원본 20페이지를 다시 읽어 의미 그룹 44개를 실제 관찰 디자인 32종으로 정리했다. foundation 패널 7개와 중첩 소유 관계를 map에 명시했으며 남은 GAP은 0개다. 원본 replica 파일과 이전 작업 경로는 수정하지 않았다.

## 검증

- 요소 fixture 70개, 공식 라이트·다크 전체 크기 674 states: 자동 flag 0개, staleDuringRender false. 마지막 `--skip-current`는 32/32 current unchanged였다.
- 최종 한국어 문구 검사: foundation 포함 78 fixture, 금지 문구 0개. 원문은 조립 map 마크업에 보존하고 fixture에는 새 한국어를 썼다.
- 32종 라이트·다크 시트를 각각 열어 최소 칸부터 12×6까지 확인했다. 원본 20장도 개별로 열어 비교했다. 마지막 변경된 cycle, steps, metric, list, pentagon, centered callout은 새 비교 PNG와 다크 시트를 다시 열어 확인했다. 통합 페이지의 최종 비교와 패널 시트는 부모 담당이다.
- 자동 검사는 글자·면 영역 초과, 텍스트 겹침, 숨겨진 이름/수치, 대비, 폰트 로딩, chip 정렬, 실제 읽은 CSS SHA를 포함한다. 개별 기록은 `../cinder-pulse-review/audits/`에 있다.

## 원본 대응

| 디자인 폴더 | 원본 페이지 | 검증 states | 설명 |
|---|---|---:|---|
| `agenda` | 02 | 10 | Observed on page 02. Ordered entries group an index, a heading and supporting copy. Its own painted parts include explicit framing or divider rules. Type uses bounded container-relative sizing, with shared weight and line-height roles. |
| `callout` | 11 | 12 | Observed source 11:1139×79 neutral concluding strip, left-aligned 21 px sentence with its actual bold lead-in. Inline emphasis and an optional icon follow callout.sentence@1. Source 07/09/12 have centered 23 px sentences and remain explicitly unexpressible because the contract has no centered presentation variant. |
| `callout--centered` | 07, 09 | 12 | A light outlined neutral conclusion strip centers a measured normal-weight sentence with consistent inset space. |
| `callout--narrow` | 12 | 26 | A light outlined neutral conclusion strip centers a measured normal-weight sentence with consistent inset space. |
| `card` | 14 | 96 | Observed on page 14: a 369×215 neutral product panel has its title at(29,28), body at(28,70) and a 313×40 white customer strip at(28,153). Two separate notes preserve the source’s descriptive and customer-text functions. Rounded panels and compact typography fit the received box using its own part proportions. |
| `card--business` | 13 | 20 | A wide business card owns a title with a small accent kicker, a two-line introduction, a white service strip and a white outcomes row with a round target mark and two figures. |
| `chart-bar--combo` | 10 | 20 | A neutral bar series and an accent connected line share the original plot. The element derives axis ticks from its maximum and owns every point connector, dot and category label. |
| `cycle` | 15 | 8 | Six small labeled circles sit on a thin neutral ring around a smaller central success figure. Two columns of soft cards explain the stages with a smaller accent step prefix, a larger title and two-line notes. Measured orbit type is eighteen pixels and central type is twenty-two pixels. |
| `headline` | 05 | 20 | A two-line medium-weight statement uses gray text with one accent phrase. Its measured thirty-four-pixel type and forty-seven-point-six-pixel line both respond to the available width and height. |
| `headline--compact` | 10 | 24 | A single compact normal-weight caption; its centered modifier aligns the same typography above a small content group. |
| `headline--partner` | 18 | 30 | A normal-weight twenty-three-pixel partner subheading sits above a separate two-line supporting note, without drawing the panel around it. |
| `hub` | 11 | 8 | Observed on page 11. A central hub and its surrounding named nodes share one owned connector field. Center circle 197×197 at 543,278, four quiet business boxes 417×168 at 102/762 ×203/384. Type uses bounded container-relative sizing, with shared weight and line-height roles. |
| `hub--pentagon` | 08 | 8 | A five-direction culture hub: a dotted pentagonal perimeter surrounds a solid central pentagon. Five rounded neutral heading tabs and three-line notes preserve the measured radial positions. |
| `hub--strength` | 17 | 6 | A central circular retention figure is surrounded by a dashed circular relation and four neutral strength panels. Separate round icon medallions bridge the left and right panels to that relation. |
| `image-frame` | 05 | 36 | Observed on page 05. The frame owns its image placeholder, framing edges and optional caption. 283 px circular portrait placeholder, no separate card surface. Container-relative dimensions scale the internal arrangement, while text uses the shared type roles. |
| `legend` | 10 | 32 | A compact fourteen-pixel inline legend pairs neutral and accent dots with normal-weight labels. The swatch preserves the original small painted circle and its surrounding glyph advance. |
| `list` | 12 | 20 | Four white rounded intersection rows use a full black circular marker, a bold short name and a normal-weight description. The six-pixel row gap and the measured twenty-eight-pixel and one-hundred-thirty-pixel text columns preserve the original alignment. |
| `list--capabilities` | 12 | 20 | Three unmarked capability rows align a larger name with a smaller description separated by a fine vertical rule. The surrounding technical panel belongs to foundation. |
| `list--retention` | 18 | 34 | Three open bullet lines use secondary neutral text and CSS-owned dots, with no inherited white-row surface. |
| `logo-group` | 18 | 20 | Observed on page 18. Repeated empty logo seats preserve a consistent grid and the spacing between marks. The internal spacing and placement are owned by this element rather than a surrounding page. Container-relative dimensions scale the internal arrangement, while text uses the shared type roles. |
| `metric` | 18 | 70 | A bare baseline row pairs a normal-weight twenty-pixel label with a twenty-four-pixel accent figure. The original two-space gap follows the actual label width, so a shorter label naturally places its figure further left; both fonts also respect the row height. |
| `prose` | 05 | 16 | Observed on page 05. Paragraphs preserve their reading order, inline emphasis and supported lead, quiet or column arrangements. The internal spacing and placement are owned by this element rather than a surrounding page. Type uses bounded container-relative sizing, with shared weight and line-height roles. |
| `prose--signature` | 05 | 24 | A leadership role line and a handwritten name form one signing group. The script face comes from the supplied font library. |
| `steps` | 09 | 8 | Four rising neutral stage cards share a bottom edge. Each owns its stage mark, accent bar, year, normal-weight phase name and bullet notes. The orange chevrons rise with the sequence and preserve their source stroke silhouette. |
| `table` | 06 | 8 | A compact body-only organization table uses fourteen-pixel text, minimum fifty-one-pixel rows and four measured unequal columns. Fine horizontal rules and a tinted final total row organize the departments. |
| `table--finance` | 06 | 16 | A compact finance grid uses a neutral header, normal-weight sixteen-pixel cells, fine horizontal rules and a final total tint, independent of the smaller organization table. |
| `table--revenue` | 10 | 18 | A revenue breakdown uses a solid accent twenty-pixel header and alternating neutral sixteen-pixel body rows. The four-column proportions follow the measured source table. |
| `timeline` | 07 | 16 | Four evenly spaced history lanes share a thick horizontal line and outlined circular points. Accent date capsules precede centered phase names and open bullet notes; a range capsule extends only for a multi-year period. |
| `timeline--columns` | 19 | 8 | Three ascending chronological columns share a common baseline. Each neutral column owns its accent step cap, period heading, year and bullet notes; the increasing heights are part of this timeline design. |
| `timeline--project` | 16 | 8 | A vertical project spine links round points to five week capsules. Each stage has a larger task title and a separate smaller explanation at the measured offsets. |
| `venn--triple` | 12 | 12 | Three overlapping circles retain their distinct neutral fills, the central accent lens and four labeled intersections. The set labels sit inside their original outer lobes, never in a substitute central circle. |
| `venn--values` | 04 | 8 | Two neutral circles share an exact accent intersection. A dotted connector leads from their core to an owned lower tray of three named principles; the tray and connector remain part of this single relationship. |

## 분리·제거 및 소유

기존 관찰 디자인 15종을 재검토하고 독립 디자인 17종을 새로 분리했다. 원본에 없는 범용 추론 폴더 38개를 제거했다. 기존 chart-bar/chart-line은 하나의 관찰 combo 차트로 통합했고, venn은 전체 연결 관계를 가진 values 디자인으로 대체했다. 목록이나 캡션을 독립 폰트 조각으로 남기지 않고 실제 소유 요소에 넣었다.

패널은 06 조직 구성·재무 현황, 12 역량 프레임, 18 누적 실적·고객사·대표 사례·파트너 띠의 7개다. 패널의 표제·판과 자식 요소는 중복하지 않는다. sourceNumbers와 children ID를 map.panels에 기록했고 구현은 foundation 담당자가 맡았다. 01·03·20 표지와 페이지 제목·바닥글·사진 좌석은 foundation furniture 소유다.

## 구체적으로 고친 부분

- 04는 두 원의 렌즈 교집합, 점선 연결, 하단 세 원칙을 한 요소로 보존했다. 작은 중심 원으로 대체하지 않았다.
- 08 오각형 허브, 12 삼중 교집합, 17 네 강점 허브, 19 높이가 다른 세 시간 열을 독립 디자인으로 구현했다. 도형은 CSS clip-path/mask/radii/gradient와 직접 그린 선을 사용한다.
- 10 combo는 막대 6개와 꺾은선 6개, 각각의 축·수치·연결선을 함께 소유한다. 조직·재무·매출 표는 서로 다른 열 폭과 타이포를 가진 별도 디자인이다. 조직 표의 빈 thead 때문에 fixed layout이 열 폭을 무시하던 문제는 auto layout으로 해결했다.
- 09 단계는 16px씩 올라가는 카드와 15px씩 올라가는 주황 chevron을 복원했다. 하단 callout의 원문 두 줄 줄바꿈을 되살리고 자체 cqh 글꼴 제한을 추가하여 통합의 약63px 높이에도 대응한다.
- 15 cycle은 원본의 중앙22px, 궤도18px, 바깥 제목22px/STEP18px 위계와 여섯 관계를 복원했다. STEP은 강조색이며 외곽 판은 원본8px 모서리다.
- 18 metric은 고정 수치 시작점 대신 원본 자연 라벨 폭과 baseline을 따른다. 원본220×34.8에서20/24px를 보존하면서 폭·높이 양쪽으로 제한하여 패널의 낮은 행에서 넘치지 않게 했다.
- 12 흰 목록은 원본40px 행,6px 간격,13px 원형 마커, 라벨/본문 실제 x비율을 반영했다. 재무·매출 표 헤더 정렬,14px 범례,13/14의 흰 내부판11px 모서리도 실측으로 맞췄다.
- 05 서명은 역할·이름·손글씨를 내재 크기 그룹으로 묶어 큰 칸에서도 분리되지 않게 했다. 본문 제목의 원래 강조 구간과 굵기도 복원했다.

## 한계와 결정

원본 사진과 고객사 로고는 요청에 따라 밝은 회색 placeholder다. 아이콘은 빈 Lucide 슬롯이며 렌더러가 채운다. 손글씨는 실제 로드한 Nanum Pen을 쓴다. 원본을 새로 그리거나 판독 불가 문구를 지어내지 않았다. 팔레트는 역할 변수로만 지정했다. 마지막 요소 변경 후 공식 렌더와 SHA 동기화를 끝냈으며 추가 디자인 수정은 하지 않는다.

## 마지막 agenda 면 재검수

부모 실물 검수 후 agenda만 다시 열었다. 카드면은 --page로 존재했지만 같은 시트 배경색에 합쳐져 원본의 진한 틈과 모서리가 사라졌다. 요소 자체 backdrop을 --n-9로 하고 가로15/635·세로15/607 간격,11px 반경의 비율을 명시했다.635×607 브라우저 실측에서 네 카드 모두310×296, 시작점(0,0)/(325,0)/(0,311)/(325,311)을 확인했다. 새 원寸 PNG,light/dark 모든 칸과5멤버를 열어 재검수했고10states/0flags였다. 설명 갱신 뒤 SHA 재동기화했으며 다시 CSS/map을 동결한다.

## 조직 표 상단 띠와 마지막 셀 배경의 소유 확인

원본06 HTML의 조직 구성 표제는 별도 div로 y203에서 높이49.89이며, 조직 table 시작은 y247이다. 표제판이 표 영역 상단5.89px에 겹치므로 table bbox를 crop하면 주황 선처럼 보인다. 표 자체에는 border-top이 없다. 이 띠는 map.panels의 barBBox[70,203,670,49.89]와 childTop44로 기록한 foundation panel 소유다. 요소 CSS에 중복 선을 추가하지 않았다.

원본 마지막 열 아래 검은 부분은 의도된 table 선이 아니다. 끝의 source 스타일 `table:nth-child(1) td:last-child{background:inherit}`가 마지막 셀의 합계행 배경을 투명 상속으로 바꾸고, 표 하단691.75가 흰 page 바탕의686을 넘어 진한 slide 면을 노출하는 DOM 잔여물이다. 실제 표 가로 규칙은 td의1px 중성 border-bottom이다. 패널이 표 전체를 소유하는 새 조립에서는 원본의 흰 페이지를 벗어난 투명 셀 잔여물을 별도 검은 선으로 만들지 않는다. 이 확인으로 CSS와 SHA에는 변경이 없다.

## 초상 원과 표지 방향 화살표 소유 보정

05 초상 원의 bbox[70,357,283,283]는 옳았으나 map 원문 마크업에 남은 과거 fixture용 grid-column/grid-row가 조립 배치를 덮었다. 해당 inline을 제거했다. 이 요소는 본문 바깥 왼쪽 rail 소유이므로 source.placementField=rail을 명시해 통합 담당자에게 올바른 배치 field 지원을 요청했다. placeholder 숫자1을 없애고 원본처럼 빈 원으로 만들었다. image-frame은 자체 짧은 변에 맞추는 CSS 원으로 다시 정리했으며36states/0flags, 라이트·다크 전체 크기와 원본 비교를 직접 확인했다.

01의 우하단 원형 화살표는 표지 furniture 누락이었다. cinder-pulse-01-arrow-furniture에 bbox[1117,548,94,94], 내부61.1px 선 그림의viewBox48/stroke3/좌표와 팔레트 역할을 기록했다. 실제 foundation 방향 화살표와 rail 배치는 부모 통합 담당자가 구현한다. 원본 이미지는 수정하지 않았다.
