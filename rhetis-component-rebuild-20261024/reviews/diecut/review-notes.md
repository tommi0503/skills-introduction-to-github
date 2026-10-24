# Diecut 재작성 검수 기록

기존 replica 19장과 replica.css는 불변 자료로 읽기만 했다. 19페이지의 직접 보이는 DOM 501개를 실제 브라우저에서 측정했다. `map.json`은 배경·머리글·연결 부품까지 소유자를 정하며, `dom-measurements.json`에 선택자·bbox·타이포·원문 HTML을 보존한다. 신규 element.css는 기존 element.css를 가져오거나 뒤에 덮지 않고 빈 파일에서 작성했다.

## 원본 기반 18개 base

agenda, hierarchy, list, pill, card, headline, chart-bar, chart-line, image-frame, tag, prose, table, steps, versus, chart-stack, legend, timeline, callout은 원본의 DOM 수치를 지역 비율로 변환했다. 원본에 없는 계약 요소는 이 base를 먼저 완성한 뒤 같은 면·선·캡슐·원형 문법에서 설계한다. 각 leaf의 description.md는 영어이며, CSS 첫 주석은 원본/파생 근거를 적는다.

## 검수 중 실제 수정

- card: 일반 card와 quiet 아치 card의 이름/설명 앵커를 분리했다. 긴 이름은 다음 영역을 함께 밀며, quiet 제목이 일반 카드 조건에 끌려 올라가던 문제를 제거했다.
- callout: foundation의 stack flex가 캡슐을 세로로 늘리는 현상은 자체 root flex:none으로 고쳤다.
- table: HTML table의 자동 행 높이로 원본보다 머리글이 커져 모든 행을 동일 grid 높이로 바꿨다.
- steps: 내부 step의 container가 전체 요소용 query를 잘못 발동시키던 문제는 root의 named container로 고쳤다. 세로형의 길어진 이름과 note도 확인했다.
- hierarchy: branch 중심과 공유 가로선 양끝의 약5px 차이를 실제 멤버 폭·간격 공식으로 고쳤다.
- agenda: 원본에 없던 활성 표시를 source 대응 fixture에서 제거했다.
- timeline: 채운 삼각 화살표를 원본의 얇은 열린 V형 화살촉으로 수정했다. source fixture의 임의 활성 강조를 제거했다.
- versus: 작은 칸에서 두 side 폭과 중앙 gap 합이 100%를 넘는 문제를 고쳤다.
- chart-bar/chart-line: root의 자기 크기 계산에 사용한 cqw/cqh가 부모 container를 참조하는 문제를 발견했다. 수평 여백은 자기 폭의 %로, 수직 값 계산은 부품에서 평가되는 cqh로 옮겨 작은 칸에서도 같은 플롯 비율을 유지했다.
- chart-line: 축 이름은 관측 간격에 맞춘 폭으로 정해 마지막 긴 이름의 겹침을 고쳤다. 값 label은 위쪽 최소 .8cqh 여유를 확보하므로 source crop 맨 위의 label이 약4px 아래로 갈 수 있다.
- chart-stack: 0 구간은 면이 없어도 숫자가 읽히도록 수치 기반 색 혼합으로 처리했다. 세로형 아래 이름의 glyph 초과는 하단 여유를 늘려 고쳤다.

## 색과 대비 판단

디자인은 원본 고정색을 가지지 않는다. 원본 검정/흰색/회색/라임은 map의 palette 역할로 이동했다. 큰 채움은 a1, 글자 아래 반쪽 밴드와 인덱스 뒤 원판은 a1-2-soft + ink를 쓴다. 다크에서 a1 위 ink로 반쪽 글자가 읽히지 않던 실제 문제를 고쳤다. chart-stack의 옅은 회색 구간 위 원본 흰 글자는 대비가 낮아 ink로 바꿨다. chart-bar의 역상 값은 ::before 막대 위에 놓이므로 투명 부모만 읽는 rawContrast 경고가 발생한다. 양 테마 실제 시트에서 dark-fill/page와 accent/a1-on 조합을 직접 확인했다.

## 계약으로 표현할 수 없는 부분

표현 불가 항목과 제안 마크업은 GAPS.md 및 map의 unexpressible instance에만 기록한다. 7단계 무중심 닫힌 loop를 core가 있는 cycle 계약에, 기울어진 ROI 타원을 집합 관계인 venn에 넣지 않는다. 페이지별 CSS나 tone 번호로 원본 형태를 숨기지 않는다.

## 검수 범위 상태

56개 요소를 작성할 때마다 선언 min 이상인 요구 크기 전체를 light/dark PNG로 직접 확인했다. 모든 요소를 실제 할당 slot과 6px 여유로 최종 재렌더했다. 최종 수치는 아래와 final-checks.json에 기록한다.

## 표지 강조 마크업 해석

.hl 안의 무class span은 새 semantic part가 아닌 일반 phrasing 래퍼로 허용했다. root는 투명한 size container이고, 각 span이 자기 문장 폭만큼 lower55% 밴드를 그린다. 원본 두 문장과 br 순서를 재조립에서도 유지한다. 큰 칸의 SUITE64px 텍스트 Range 높이80px와 line-height1.2의 행 간격76.8px 때문에 약3.2px의 Range bbox 교차가 발생한다. 원본44px도 Range55px와 행 간격52.8px의 같은 관계이다. 실제 글자 ink는 부딪히지 않는 것을 PNG로 확인했으며, 원본 행간을 임의 확대하지 않았다.

## Final rebuild checks and explicit decisions

- All 56 element sources were written afresh; 173 fixtures pass the new structural validator with no errors or warnings. The six-character source-copy audit reports zero collisions.
- The mandatory card-2-quiet sentence was changed only from “기록과 지표가 한곳에 모여 바로 결정할 수 있습니다.” to “기록과 지표가 한곳에 모여 바로 결정을 내립니다.” because the latest request forbids six-character source-copy overlap. The parent explicitly approved this narrow precedence exception; all other mandatory markup and numeric data remain intact. The non-mandatory OPERATION label became FULFILMENT.
- Stacked-area --v is cumulative per README. First series has higher stacking order, so the visible area bands equal consecutive cumulative differences; no duplicate cumulative data or contract gap is required.
- Direct sheet review corrected polygon outlines above area fills, radial connector attachment, circles into true equal dimensions, central positioning axes, inline icon sizing, and source-prose root container units. Root font-size could not query its own container, so prose sizes now target child paragraphs.
- Reassembled source uses original words only as data from the immutable replicas and earlier assembled HTML. No old stylesheet or old placement was reused. All ordinary-page body placements are regenerated integer grid coordinates. Unsupported diagram words are retained as plain prose, with their shapes reported in GAPS.

- Page-level review found old data .tone-N on before/after segments changed their source gray/black roles under the new palette. Those purely stylistic data classes were removed on reassembled page 13; raw numeric values are unchanged and the source max 425 was restored. Page 11 caption and SOLUTION capsule now occupy distinct integer rows. Page 18 preserves all six original statements in compact quiet prose; only the unsupported bottom-rule/list combination is omitted. Page 19 uses its correct foundation title role instead of enlarging the title through a content headline.

## Quantized page assembly differences

The ordinary foundation grid allows integer 12×6 allocations with a 20px gap. Independently measured source boundaries (especially the 2×2 product catalogue and 3×2 certificates) cannot all coincide with this quantized grid. Element comparisons show each supported base separately at its own aspect; the page comparisons expose this assembly constraint.

Replica 15 dividers begin at the body grid below the header, whereas source dividers extend behind the header. Replica 19 social label colors are represented by the current host palette text role. These are page assembly/host differences, not new semantic contract gaps.

The attempted 07 badge move over the media region was reverted. The supported standalone tag remains in the library and source comparison. Its inseparable placement next to the product model belongs to the unexpressible product-panel relationship, so the assembled page leaves a comment instead of relocating it to a wrong visual role.

## Final verification result

- 56 elements, 173 fixtures, 2,130 eligible fixture/mode/size cases. All 56 light and 56 dark size sheets exist; all 18 source-mapped leaves have comparison sheets.
- Outside text 0, clipped text 0, failed fonts 0, hidden essentials 0, zero-sized element roots 0. Six highlight Range intersections arise from the original 1.2 line height and SUITE glyph bounding boxes; actual ink remains separated in the directly reviewed sheets.
- Raw contrast flags: chart-bar 310 (white numbers over black pseudo bars), scatter 94 (labels outside the parent dot), roadmap 6 (milestone text outside its diamond), stack 8 (zero-width segment labels outside the absent segment), card 10 (accent pseudo panel background). All these actual painted backgrounds were checked directly. Pixel contrast was not run; a null pixel result is not evidence of passing.
- Matrix was caught at final direct review as a wrong three-column layout despite zero clipping: matrix-nine had overwritten a shared token default. Matrix root now explicitly preserves its contracted two columns. Its 18 cases were rerendered and both complete sheets directly checked as 2×2. final-render-delta.json records that this was the only changed collection file after the full run, with hashes for every unchanged file.
- All 19 rebuilt pages have final PNGs at 1280×720, no clipped text, font failures or script errors, and all source HTML hashes match the render audits. Every page was individually compared with its original; corrected pages were rerendered and checked again. Raw overflow includes intended foundation notch paint, SVG icon line boxes, and chart labels outside their bar primitives; it is retained in the audit rather than silently suppressed.
- These checks establish readable responsive elements and transparent assembly constraints. The rebuilt deck is visibly different where the fixed foundation grid or semantic contract is unable to express source geometry; it is not reported as a 100% visual match.

## Element origins (one line per leaf)

| Element | Replica origin |
|---|---|
| `agenda` | replica 02 |
| `architecture` | 직접 대응 없음 — replica 03, 04의 선·면·타이포 문법으로 확장 |
| `balance` | 직접 대응 없음 — replica 03의 선·면·타이포 문법으로 확장 |
| `bullet` | 직접 대응 없음 — replica 13의 선·면·타이포 문법으로 확장 |
| `callout` | replica 18 |
| `card` | replica 04, 06, 16 |
| `chart-area` | 직접 대응 없음 — replica 13의 선·면·타이포 문법으로 확장 |
| `chart-bar` | replica 05 |
| `chart-donut` | 직접 대응 없음 — replica 03의 선·면·타이포 문법으로 확장 |
| `chart-line` | replica 05 |
| `chart-scatter` | 직접 대응 없음 — replica 03, 13의 선·면·타이포 문법으로 확장 |
| `chart-stack` | replica 13 |
| `chart-waterfall` | 직접 대응 없음 — 덱의 선·면·타이포 문법으로 확장 |
| `code` | 직접 대응 없음 — replica 03, 04의 선·면·타이포 문법으로 확장 |
| `concentric` | 직접 대응 없음 — replica 03의 선·면·타이포 문법으로 확장 |
| `cycle` | 직접 대응 없음 — replica 03, 06의 선·면·타이포 문법으로 확장 |
| `decision-tree` | 직접 대응 없음 — replica 03의 선·면·타이포 문법으로 확장 |
| `delta` | 직접 대응 없음 — 덱의 선·면·타이포 문법으로 확장 |
| `flowchart` | 직접 대응 없음 — replica 03, 04, 10의 선·면·타이포 문법으로 확장 |
| `funnel` | 직접 대응 없음 — replica 13의 선·면·타이포 문법으로 확장 |
| `gauge` | 직접 대응 없음 — replica 13의 선·면·타이포 문법으로 확장 |
| `headline` | replica 03, 05, 07, 08, 09, 13, 18 |
| `heatmap` | 직접 대응 없음 — replica 04, 13의 선·면·타이포 문법으로 확장 |
| `hierarchy` | replica 03 |
| `hub` | 직접 대응 없음 — replica 03, 06의 선·면·타이포 문법으로 확장 |
| `image-frame` | replica 03, 07, 09, 17; cover 01 media uses foundation seat.back |
| `journey` | 직접 대응 없음 — replica 05, 15의 선·면·타이포 문법으로 확장 |
| `legend` | replica 13 |
| `list` | replica 03, 04, 05 |
| `logo-group` | 직접 대응 없음 — 덱의 선·면·타이포 문법으로 확장 |
| `matrix` | 직접 대응 없음 — replica 04, 13의 선·면·타이포 문법으로 확장 |
| `matrix-nine` | 직접 대응 없음 — replica 04, 13의 선·면·타이포 문법으로 확장 |
| `metric` | 직접 대응 없음 — replica 03의 선·면·타이포 문법으로 확장 |
| `mindmap` | 직접 대응 없음 — replica 03의 선·면·타이포 문법으로 확장 |
| `network` | 직접 대응 없음 — replica 03의 선·면·타이포 문법으로 확장 |
| `person` | 직접 대응 없음 — 덱의 선·면·타이포 문법으로 확장 |
| `pill` | replica 03, 05, 11, 13, 19 |
| `positioning` | 직접 대응 없음 — replica 03, 13의 선·면·타이포 문법으로 확장 |
| `pricing` | 직접 대응 없음 — replica 03, 04, 11의 선·면·타이포 문법으로 확장 |
| `prose` | replica 07, 08, 09, 17, 18, 19 |
| `pyramid` | 직접 대응 없음 — replica 04, 13의 선·면·타이포 문법으로 확장 |
| `quote` | 직접 대응 없음 — replica 04, 05의 선·면·타이포 문법으로 확장 |
| `radar` | 직접 대응 없음 — replica 03, 13의 선·면·타이포 문법으로 확장 |
| `roadmap` | 직접 대응 없음 — replica 03, 13의 선·면·타이포 문법으로 확장 |
| `sankey` | 직접 대응 없음 — replica 03, 13의 선·면·타이포 문법으로 확장 |
| `slope` | 직접 대응 없음 — replica 03, 05의 선·면·타이포 문법으로 확장 |
| `sparkline` | 직접 대응 없음 — replica 05의 선·면·타이포 문법으로 확장 |
| `steps` | replica 10 |
| `swimlane` | 직접 대응 없음 — replica 03, 04, 10의 선·면·타이포 문법으로 확장 |
| `table` | replica 08 |
| `tag` | replica 01, 07 |
| `timeline` | replica 15 |
| `treemap` | 직접 대응 없음 — replica 08, 13의 선·면·타이포 문법으로 확장 |
| `venn` | 직접 대응 없음 — replica 03, 14의 선·면·타이포 문법으로 확장 |
| `versus` | replica 11 |
| `waffle` | 직접 대응 없음 — replica 02, 03의 선·면·타이포 문법으로 확장 |

주 에이전트 최종 통합검수: 실제 glyph 대비로 lines-12의8×2 강조값97이 최상단점과겹친것을발견했다(light3.65/dark1.42). 작은plot만32px의글자여유를확보하고라벨을점위로완전히옮겼다. 원본05의큰기하와마크업·데이터는보존했다. 변경후chart-line전크기를다시렌더하며최종source비교와19조립에도반영한다.

## 2026-10-24 최종 렌더 지원 검수

- 요소 CSS 생성기를 실행하지 않았다. 주 에이전트가 확정한 chart-line 소형 plot의 값 라벨 여유와 card 필수 모델 `✹` 중앙 정렬을 현재 CSS 그대로 사용했다. `build/model-icon-final.log`의 card 88칸 검사 결과와 최종 source 대조의 card 2행·chart-line 1행을 직접 확인했다.
- 19개 조립 HTML을 현재 컬렉션 CSS로 다시 만들고 Chromium으로 전부 렌더했다. 조립 PNG는 모두 1280×720이며, 비교 PNG 19개를 원본 | 동결 replica | 조립본 순서의 3840×720으로 교체했다. 19장 삼중 비교를 각각 직접 확인했다. 페이지 클립 및 사용 폰트 로딩 실패는 모두 0이다. 동결 replica는 수정하지 않았다.
- decision-tree의 세 갈래 fixture 질문을 `이번 안건의 검토 경로는?`로 고쳐 일반·긴급·보류 분기와 문장 성격을 맞췄다. 마크업·조건·결과 및 CSS는 보존했다. 해당 요소 양모드 크기 시트를 다시 렌더해 확인했으며 173개 fixture의 원문 6자 중복 검사는 충돌 0이다.
- 최종 컬렉션 SHA-256은 `1f73fb9874a41277cf8c7de6306faa55baa44329ee8c564ef050da7c8546eeb0`이다. `--contrast --resume`으로 56개 요소 2,130개 크기·모드 사례를 현재 소스 기준으로 집계했다. 글자 영역 초과, 클립, 폰트 실패, 필수 멤버 숨김, 0크기 root, 실제 픽셀 대비 실패는 각각 0이다. Range 중첩은 6건이며 모두 tag의 두 줄 Range 사각형이 약 3.2px 겹치는 경우다. `ink-overlap-proof.json`은 그 교집합에 실제 글자 픽셀이 0임을 확인한다. Range 중첩 수치를 0으로 바꾸지 않았다.
- 관련 CSS와 fixture가 동일함을 공용 도구가 증명한 요소는 `render-reuse/`의 활성 CSS 동등성 증거로 기존 픽셀 검사를 재사용했다. 변경한 decision-tree는 새로 렌더했다. 모든 요소가 마지막의 무관한 fixture 수정 이후 다시 래스터화되었다고 주장하지 않는다.
- 최종 라이트·다크 크기 시트 112개를 요소마다 직접 열어 표시된 최소칸 및 각 적격 크기 칸의 글자·선·채움·연결·칩 정렬을 확인했다. 추가 시각 오류는 발견하지 못했다. 확인 목록은 `build/support-viewed.json`, PNG 무결성·크기·HTML 및 fixture 해시 재확인은 `build/support-final-verification.json`에 남겼다.
- 조립본의 남은 원본 차이는 기존 GAPS의 표지 대형 wordmark·회전 목차 rail·일부 미디어와 패널의 중첩 관계·12/14번 자유형 다이어그램·분리된 페이지 면이다. 정수 그리드 위치 차이도 기존 기록을 유지한다. 이 지원 검수에서 새 페이지 CSS나 임의 변형으로 이를 숨기지 않았다.


## Foundation correction 016 · final source furniture review

This section supersedes earlier statements that the cover media, page faces or the small contents corner triangle were impossible in foundation. The immutable replica and every element file were preserved byte for byte. Only the kit furniture extensions, foundation, its two demonstrations, the map/GAPS, source-data assembly builder and review outputs changed. No element CSS generator was run.

The foundation now uses the measured full-bleed cover with its right-hand partial media, top phrases and short connecting rule, thin Pretendard Variable wordmark, 24px introductory line, two 44px highlight bands using existing `tag.hl` markup, and date/author metadata. Cover has no head/body. Original source wording remains in assembly only. Exact 142px cover and 146px rotated contents typography exceed the contract's 128px ceiling: the text is retained at 128px without scaling, and the two precise gaps have proposed markup in GAPS.md and map.json.

Each page-face instance is explicitly mapped to `.page > .deco > svg`: curved notch plates and four holes, full gray or light surfaces, paired large ellipses, closing split plates and small holes, plus the contents corner triangle. These are source vector primitives filled with palette roles. The SVG is declared background furniture, not an embedded image or an HTML workaround for missing element semantics. Representative notch and flat-cover examples are shipped in foundation/fixtures.

The canonical normal grid keeps the original 72px side inset, 44px page inset, 55px navigation allocation and 20px gap. Header titles use normal contract flow, so their vertical placement still differs among source pages with individually positioned headings; there is no page-number selector, fixture switch or per-page CSS correction. Existing explicit product-panel and free-form diagram gaps (07/09/12/14 and others listed in GAPS) remain. In particular their prose fallbacks are not claimed to reproduce those missing geometries.

The final 19 original | frozen replica | assembly comparison PNGs were opened individually. The restored page furniture and palette families were checked on every page; remaining element/grid differences are visible rather than hidden. All 19 final assembly PNGs are 1280×720, comparison PNGs 3840×720; clipped text and failed fonts are both 0.

Final frozen collection SHA-256: `d3a068e12a9054c9deb62f0eb4f08f77e0d3ce672bc48d0f6d56c99e3e241477`. The complete 56-leaf/2,130-case contrast run finished, followed by a frozen-source `--contrast --resume` pass: `sourceUnchanged=true`; outside/clip/font/hidden/zero-root/pixel-contrast failures are all0. The six tag Range intersections exactly match the preserved zero-ink proof. The resume evidence uses identical fixture hashes and ordered matching CSS declarations; unrelated footer/furniture documentation changes were not falsely described as element changes. All18 mapped source leaves (26comparison rows),19assembly pages and their final PDF now carry this same source SHA. Foundation demonstrations both have0clip/0font errors. See `foundation-final-audit.json` and `build/foundation-final-verification-016.json`.
