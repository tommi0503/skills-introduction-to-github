# 검수 기록 — lamella

## 범위와 보존

기존 replica HTML·CSS·PNG·PDF는 수정하지 않았다. `replica-freeze.json`의 SHA-256으로 보존 여부를 확인한다. 새 작업은 56개 요소의 전체 CSS, kit/foundation, 새 fixture, 요소 지도와 검수·조립 자료다. 원본 이미지나 replica를 통째로 배경에 깔지 않았다.

## 출처와 해석

- 직접 대응하는 요소의 페이지·bbox·측정 수치는 map.json에 있다. 없는 요소는 추론이라고 명시하며 출처를 꾸며내지 않는다.
- 사진·복잡한 일러스트·로고는 연한 회색 번호 자리로 둔다. 단순 벡터와 연결은 각 소유 요소 또는 foundation이 그린다.
- 이 작업에서 fixture 문구는 새 한국어 업무 내용으로 작성했다. 기존 replica의 판독·추정 문구는 보존했으며 새 원문으로 단정하지 않는다. 이번 작업에서 새로 지어낸 원본 문구는 없다.
- 색은 덱 전체의 역할을 고정해 팔레트 자리로 옮겼다. 기준 라이트/다크 시트는 README 팔레트를 쓰므로 원본의 고유 RGB와 다르다. 조립 비교에는 같은 역할에 원본 근접 팔레트를 공급한다.
- 낮은 대비의 원본 보조색은 읽을 수 있는 깊은 단계로 옮긴다. 밝은 강조면의 on 색은 대비가 높은 ink가 될 수 있어 원본의 흰 글자와 다르다.
- 고정 replica 자체의 글자 맞춤·원본과의 잔여 차이는 유지한다. 조립본의 12×6 양의 그리드 트랙은 bbox를 먼저 계산하며 여러 세로 경계를 여섯 행으로 담는 양자화 오차가 남을 수 있다. layout-before-render.json에 요소별 수치를 기록했다.
- 독립 행별 글꼴 크기·자간, 복합 제목 패널, 계약에 없는 다중 조각 파이 등은 GAPS.md에만 미지원으로 기록했다. 이를 임의의 새 클래스로 우회하지 않았다.

## 검사 방식과 수정

- 각 fixture의 min 이상 지정 크기와 min 자체를 두 모드에서 실제 1280×720 foundation에 배치하고 요소 칸을 여유 포함 잘라 한 줄로 묶었다.
- DOM/Range 경계·가림·멤버 교차·대비·chip 중앙·의사 요소 도형 경계를 검사하고, 실제 PNG를 빈 foundation과 비교해 그림자와 글리프의 칸 밖 픽셀도 검사했다.
- 글꼴은 로딩 상태만 확인하지 않고 실제 자손 및 생성 문자의 CDP 플랫폼 글꼴을 확인했다. Montserrat/Do Hyeon에 없는 한국어·중간점은 허용된 body 글꼴로 교정했다.
- 실제 픽셀 검사에서 발견한 Do Hyeon %의 1–2px 오른쪽 돌출, timeline 강조점·회색 note 면, list/quote 장식 여유를 해당 요소 CSS에서 수정했다.
- 모범 fixture의 데이터·마크업은 보존했다. 원문의 특수문자 별표 아이콘은 비어 있는 Lucide 아이콘으로, 6자 중복 금지와 충돌한 일반 문장 한 구절은 뜻을 유지한 최소 표현으로 바꾼 예외를 구조 감사에 명시했다.
- 담당자가 모든 최종 native 크기 칸을 확인하고 주 담당자가 통합 시트와 페이지 비교를 확인한다. 최종 해시는 validation과 root-final-review.json으로 연결한다.

## 통합 페이지 관찰

- 23: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 01: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 02: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 03: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 04: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 06: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 09: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 10: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 11: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 13: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 14: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 15: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 16: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 17: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 19: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 20: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 21: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 22: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 07: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 08: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 05: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 12: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 18: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.

## 담당 요소별 상세 기록

### review-charts

# Chart element review

## chart-bar — replica 11

Source:805x411 crop,106px bars in161px columns,27px first offset (16.7702% of each column), baseline393px down the crop;392px maximum bar. Source label size is approximately9.8px, rounded to the nearest contract type10. The L-shaped axis stays1px; bars are square. A continuous source outline arrow is approximated from the two actual quadratic curves with16 samples each and a CSS evenodd polygon; inset edge normals keep the contour1px across allocations. It overlays bars as in the source SVG. The projection label and growth badge visible inside the source crop are independent mapped text/gap overlays and are not faked in this chart.

Value-present b markup reserves annotation space and removes only the secondary source ornament. Parent approved this real own-child condition. The horizontal variant omits the vertical source arrow and puts categories left and values at bar ends. Default source bars use --a1; an own .on member quiets its peers to --n-4. Text uses --ink, fine axes --n-4, arrow --a1-4-soft. No values or names are hidden, no axis label is wrapped. Narrow dense bar counts use type10 axis labels.

Corrections: fixed horizontal members incorrectly inheriting100% height; reduced specificity of own b-presence label rules so the horizontal layout wins; removed wrapping on category labels; adjusted original27px offset and exact392px source bar range; moved source arrow above bars and kept its stroke1px.

Minimums are based on42 separate smaller-cell probes, visual review and bounds checks: bars-12 3x2; bars-2 1x2; bars-3 3x2; bars-6 4x2; bars-h-5 4x2; bars-h-8 2x2; source-shaped five bars3x2; long category7x3. Smaller supported matrix sizes and all minima were viewed in both modes; especially 12 bars3x3 and horizontal8 members2x2 were opened natively. Final146-case light/dark matrix has outside/clipped/hidden/member_outside/overlaps/contrast all zero. All16 fixture rows were individually viewed, minima atlases both modes viewed, source comparison viewed; final full sheets viewed again after the last geometry correction. Copy audit:8 fixtures, zero source fragments.

Final CSS SHA256: e277d0eef7cf676079da0fbb999ba56e5c2c12c3f4db043e469ceb6af5d3de64.

## chart-donut — replica 14

Source: three small97px rings at x87/378/669 (291px spacing), names above, centre hole29.1px (30%), approximately18px whole percentages. Tight bbox761x131 includes the long names. Regular tracks are291px and the final track179px (.6151202749fr), and each ring has a common2px inset. Names retain a common1px inset rather than arbitrary per-member adjustments; source name x offsets vary by0.5–3px, so tiny original label-position differences remain. The source name fonts also vary slightly; the library uses one proportional name scale. The two vertical panel rules visible in the source crop belong to separate surrounding panels/gaps, not this share chart, and are not duplicated here. Palette roles: primary --a1; secondary shares --a1-3-soft/--a1-2-soft; empty track --n-1; centre --page; text --ink.

Independent donut and group roots are size containers. A donut nested as a group data member uses container-type:normal to share intrinsic subgrid name tracks and query the containing group; parent explicitly approved this real structural distinction. The circle's figure frame is a size container so every ring stays circular. Four members form two rows; in tall allocations two members stack and three form2+1, preventing over70% unused vertical space. Source native-wide layout is unchanged.

The original percentage is slightly wider than the30% hole. A2px page-colored text halo preserves readability where the final glyph extends over a filled sector, especially in dark mode; this small contrast aid is an intentional difference from the source. No number or name is hidden. Source-shaped fixtures use entirely new business names; mandatory five fixtures keep their exact original markup and data. A new two-member fixture checks the unequal-track grammar at another count.

Minimum investigations:27 smaller cells inspected. Standalone mandatory fixtures1x2, long name2x2, source and mandatory3-member6x2, four members4x3, new two members4x2. Smaller grouped circles were rejected because the minimum readable figure overwhelmed the source hole/ring balance, even when bounds checks passed. All16 final row sheets, both native minimum atlases, source comparison and critical tall/wide native cells were directly viewed. Final142 cases have outside/clipped/hidden/member_outside/overlaps/contrast all zero;8 fixtures copy audit zero.

Final CSS SHA256: dbe2eadca644d340577f9e2f8b8b1418018ce3b15259ccef303a4c231520d35f.

## chart-area — replica 17

Source plot701x480 inside723x502 crop;1px L-axis,0.7px lines and6px circular markers. Point coordinates were read directly: the point grid begins0.35px left of the axis and ends1.15px before its far edge. Both source polygons use the same a1 SVG gradient; the second line is a2. The original alpha40% starts at global y0, so the actual plot-top alpha at y155 is30.23622047%, fading to0 at baseline635. The library keeps this measured fill role and alpha for all ordinary series, with ranked lines; the named stacked variant instead uses opaque ranked cumulative bands, painting lower bands above larger ones.

Real nonempty series names create a top legend; real point labels reserve annotation room. Source names are empty and no badge or headline is put into a series.name. The growth/retention badges visible inside the comparison crop are separate mapped gaps. Numeric tick labels come from --max. Plot insets and label space scale, with minimum4px above the highest6px marker and18px for baseline labels. All text uses contract steps or proportional clamps. Axis labels never wrap. Compact legend swatches/padding prevent the word 서비스 splitting in the2x2 stacked minimum.

Corrections: replaced zero-size shadow markers, which painted squares, with real6px circular boxes; aligned strokes to marker centres; preserved the common a1 fill and measured30.236% upper alpha; corrected point-grid offsets; used a0.4px wedge overlap to reduce raster seams. CSS wedge antialiasing can differ slightly from SVG at steep slopes. These are small raster differences rather than substituted data/geometry.

Minimums based on25 smaller-cell probes: area-1 3x2; area-3pt2x2; areas-2 2x2; stacked3 2x2; source3x2; long3-series4x2. Rejected source2x2 for visually joined axis labels despite automatic0, and rejected long-series3x2/3x3 for actual legend/value overlap. All12 final fixture rows, both minimum atlases, source comparison and native critical cells were viewed. Final118-case matrix: all six QA counts zero. A separate final118-case browser audit also confirms all real point marker rectangles within their roots and all pages1280x720, zero failures. Six fixtures copy audit zero.

Final CSS SHA256: 20cc0461e00576e318a08770caaf1953368ccff3687f8efbac4da6ad1aa55be1.

## gauge — inferred, no source instance

Replica09 tabs measure217x30 with border-radius0 34px 0 34px: upper-right and lower-left both curve, upper-left and lower-right stay square. The inferred progress rail and actual fill use0 999px 0 999px, letting CSS preserve the same full-height opposite arcs across allocations. This is explicitly not a source gauge base. Figures and labels use body weight, matching the light numerical/plot grammar. Roles: --a1 actual, --n-3 remaining, --ink text. Three new0/64/100% business fixtures have2x2 minima and no hidden parts. All six final rows and both native minimum atlases viewed. Final60 cases: all eight QA counts zero; three fixtures copy audit zero.

Final CSS SHA256: 7eeda4657e2268bbe5381f51414f38a74647e54ebf2a0a3042ee97bf7e82c0f4.

## Inferred bullet
Source09's tabs have opposite upper-right/lower-left arcs, retained on the new qualitative range field. Light numerical type, thin secondary target mark and pale primary-step bands follow the deck. This target/band contract is absent from source and not claimed as a base instance. All70 final renders, eight mode/fixture rows and both native minimum atlases inspected; nine QA checks and source-copy audit zero. Minimum4x4 supports four notes without squeezing them against the next member.

## Inferred sparkline
Source17's0.7px series and6px points supply this new axis-free trend. Its mini bars use the source plot's65.84%-width rhythm and a pale-to-solid primary fade. The source area remains a distinct mapped element; this sparkline is inferred and never substituted for the original composite. All80 final renders, eight mode/fixture rows and native1x1 minima inspected; nine checks/source-copy audit zero.

## Inferred heatmap
Source09's opposite upper-right/lower-left cap and thin type/rule language informs this new density matrix. Regular cells preserve the measured corner direction; calendar mode caps those corner arcs at18% so its day cells read as squares rather than leaf pictograms. This change followed direct native visual review, despite geometry QA already being zero. All58 final renders, every fixture/mode row and native minima were regenerated and inspected. Nine QA checks and source-copy audit zero; no source heatmap instance is claimed.

## Inferred waffle
Source09's opposite-corner cap and source14's restrained percentage type inform this new counted-share matrix. Unit arcs use20% of each cell side to retain distinct countable squares, with an upper-right/lower-left direction. The complete unit count sets the matrix and CSS figures mode draws people. All60 final renders, every fixture/mode row and native minima viewed; nine QA checks/source-copy audit zero. No source waffle instance is claimed.

## Inferred chart-line
Source21 supplies its actual2px stroke and10px hollow point ratio; the complete mixed bar/line source remains unexpressible and is not split into mapped leaves. This new pure-line contract retains the point grammar and adds separate data labels. Four mandatory showcases preserve exact markup/data, including their real .pt.on emphasis. README chart quality requires nowrap axis labels: dense7+ point plots below700px retain every third axis label, remove the crowded tail label and keep the final endpoint, with clamped first/last alignment. Values and points always remain visible. New boundary data is a natural0→28→67→100→93→86 progression, not a repeating sawtooth. All116 final renders, twelve fixture/mode rows and native minima inspected; nine QA checks/copy audit zero and actual custom fonts loaded without error. Minima: monthly12=3x2, three points2x2, six longer month labels4x2, flat5=2x2, long business periods4x2, boundary6=3x2. This is inferred, not a source base.

Final chart-line:8px shared-token gutters keep the hollow point/value labels clear of the plot L-axis. All116 final light/dark cases,12 fixture rows and native minima viewed; all9 QA checks and copy matches0. Source21 is still a mixed bar/line gap and is not claimed as a mapped pure-line base.

Radar (inferred, no mapped base):own-axis CSS wedges draw spokes and concentric polygons; each series owns its filled polygon and actual vertex marks.3/5/8 axes and1/2/3 series use fresh Korean business content. Side axis labels align outward, protecting outer vertices; radius25cqw capped29cqh preserves space for legends. All48 final cases,6 light/dark rows and native minima viewed;9 QA counts0/copy0/font load errors0. Minima2x3,3x3,4x4 retain all labels. Deck-specific marker shape, grid weight and legend treatment follow measured source grammar.


## Slope — final inferred design
Replica에 직접적인 paired-value 도표는 없어 각 덱의 실제 점·선·라벨 문법으로 새 설계했다. 원본 복합 플롯은 이 요소로 바꾸지 않았다. 각 pair 전체가 두 시점 연결선을 소유하며, dumbbell은 이전=open / 이후=solid 표식과 머리 키를 사용해 감소항목의 의미도 유지한다. 긴 이름 칸을 실제 두 줄이 읽히는 너비로 조정했다. 3·6개 변화, 0/100 경계, 긴 이름의 dumbbell 4개 fixture의 최종 라이트·다크 62칸 전행과 native 최소칸을 확인했다. 자동9항목0, 원문6자 일치0. 자동0은 시각적 동일성을 뜻하지 않는다.


## Scatter — final inferred design
Replica17의 .7px plot·작은원·열린면 문법을 신규 산점도에 적용. 실제좌표 점과 면적비례 버블, 무채색 보조/주강조 한점, 독립축/값범위를 사용했다. 원본영역·복합차트는지도그대로유지했다.6fixture 최종76칸 전행/native최소칸 양모드직접확인,9지표0/원문일치0.


## Waterfall — final inferred design
Replica11의106/161 막대폭비·가는축·투명그라데이션에서신규waterfall을설계했다. source growtharrow는없는도표에복사하지않고 실제누적값연결선만그린다.5fixture 최종66칸 전행/native최소칸양모드검수,9지표0/원문일치0.

### review-readme-quality

# README 품질 기준 확인

- 잘림·겹침: fixture별 정직한 min 이상 지정 크기와 min 자체를 두 모드로 검사했다. DOM/문자 Range·가림·멤버 교차·그려진 픽셀을 확인하고 현재 해시의 9개 QA 집계를 release-audit에 연결한다.
- 대비: 실제 색·배경을 계산해 일반 글자4.5, 큰 글자3 기준을 확인했다. 원본의 흐린 글자나 흰 글자가 기준을 넘지 못하면 팔레트의 깊이 또는 명암 역할을 선택했다. 그러므로 원본 RGB와 일부 on 글자색은 다르다.
- 아이콘: 원/배지 안의 아이콘은 중간 크기(통상50~60%)로 두고 실제 native min에서 확인했다. 텍스트/번호 자체를 icon으로 취급하지 않았다.
- 정렬: 같은 행의 멤버 기준선을 일치시키고 큰 칸과 작은 칸의 콘텐츠 무게 중심을 대조했다. source 자체의 비대칭 배치는 그대로 비율화했다.
- 남은 장식: 연결선은 모든 멤버를 소유하는 요소 안에서 그렸다. 페이지 독립 장식은 foundation으로 분리했다. 장식의 칸 밖 픽셀과 본문 교차를 검사했다.
- 차트: 축/라벨/범례/데이터 표식과 줄바꿈을 native 크기에서 확인했다. 작은 칸에서는 보조 라벨을 솎거나 줄이고 강조를 분명히 했다. 계약이 허용하지 않는 다중 조각 pie를 여러 donut으로 바꾸지 않고 GAPS에 기록했다.
- 한 디자인: 직접 측정한 base/계약 변형을 먼저 만들고, 나머지 계약은 같은 덱의 선·모서리·면·타입 규칙으로 추론했다. 직접 출처와 추론은 ORIGINS에 구별했다.
- 다크 모드: 독립 라이트·다크 팔레트로 모든 최종 크기를 다시 렌더했다. 단순 이미지 반전을 사용하지 않았다.
- 중복 금지: samples의 클래스·구조와 mandatory fixture 형식만 사용했다. 기존 sample의 디자인 CSS를 가져오지 않았고 7개 덱의 독립 소스 수치를 element.css 첫 주석과 description에 연결했다.

각 항목의 최종 상태는 validation/release-audit.json, 요소별 validation/*.json, raster-paint-audit.json 및 실제 sheets PNG를 함께 확인한다. 이 체크리스트는 100% 픽셀 동일성을 뜻하지 않으며 계약 미지원과 공유 글꼴·그리드 차이는 GAPS/review-notes에 남긴다.

### review-residual-actual-paint

# Lamella residual source coverage review

- 원본 replica 23페이지는 수정하지 않았다. 실제 브라우저 DOM 3,699개를 확인했으며 원본 SHA-256 전부가 유지된다.
- 전체 화면 SVG의 1280×720 바운딩 박스는 다른 요소의 소유권이 아니다. 기존 source_svg 안의 실제 도형 속성이 동일한 2,642개와 개별 요소/장치/GAP 상자 및 의미 소유를 따로 확인했다.
- 독립 페이지 괘선 16개를 source stroke의 실제 paint 경계로 residual-furniture에 추가했다. 소스 중심선 좌표와 stroke 폭도 함께 기록했다. 07쪽 가로 rule과 두 세로 rail, 08쪽 긴 가로 rule도 포함한다.
- 07쪽 The Problem/The Solution 캡은 흰 198×30px 면에 우상단 한 모서리만34px 곡선이다. 22쪽 headline base의 연한 면/양대각 모서리와 다르고, 현재 .big/.center/.on 중 적합한 계약 변형이 없어 GAP 두 건으로 남겼다.
- 12쪽 CardB/ar와14쪽 ge는 fitting 과정에 남은 독립 텍스트 조각이다. 의미가 불명확한 원문을 임의의 문장으로 복원하지 않았고, 미지원 source-fragment 제안 마크업과 실제 경계로 GAP 세 건을 추가했다.
- 01쪽 lockup lead,03/08쪽 긴 카드 본문,18쪽 네 인용부호는 기존 소유 요소의 텍스트/장식이다. 실제 source overhang을 별도 요소로 분리하지 않았다. 정확한 union bbox 추천7건만 별도 JSON으로 전달했으며 기존 소유자 지도는 수정하지 않았다.
- 23페이지의 measured-tab/manual-tab 70개와 thin rule 후보95개를 전수 대조했다. 신규 GAP5/괘선16을 포함하면 미분류 actual paint/text는0건이다. 빈 SVG group13개는 실제 paint가 없다. 08쪽 white alternate card의 계약 변형 판정은 text 소유자의 별도 검토 범위다.

### review-root-pages

주검수 01/02에서 top metadata가a1-7/label650로고정되어검정·흰원문을무시하고짧은이름을줄바꿈하는것을발견했다. 선언된source색역할·글자크기변수와body400·nowrap로교정했다. 다행표제map에foreground_role을빠뜨려밝은원문이검정이되던오류도source_texts첫색으로복원했다. 원본의행별비정상폭맞춤문제는GAPS에그대로남기며그것을장면별CSS로구현하지않는다.

### review-systems

# Systems element review

## table

{
  "replica_pages": [
    "16"
  ],
  "final_render_cases": 32,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "cell_text_outside": 0,
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/table/districts-3-rows-4-dark-01.png",
    "build/native-review/table/districts-3-rows-4-dark-02.png",
    "build/native-review/table/districts-3-rows-4-dark-03.png",
    "build/native-review/table/districts-3-rows-4-dark-04.png",
    "build/native-review/table/districts-3-rows-4-dark-05.png",
    "build/native-review/table/districts-3-rows-4-light-01.png",
    "build/native-review/table/districts-3-rows-4-light-02.png",
    "build/native-review/table/districts-3-rows-4-light-03.png",
    "build/native-review/table/districts-3-rows-4-light-04.png",
    "build/native-review/table/districts-3-rows-4-light-05.png",
    "build/native-review/table/replica-16-dark-01.png",
    "build/native-review/table/replica-16-dark-02.png",
    "build/native-review/table/replica-16-dark-03.png",
    "build/native-review/table/replica-16-light-01.png",
    "build/native-review/table/replica-16-light-02.png",
    "build/native-review/table/replica-16-light-03.png"
  ],
  "decisions": [
    "Source column tint and vertical rules continue23.5/488of the box below the final data row. It is background geometry, not invented data.",
    "Per-cell OCR-fitted font differences are replaced by semantic column hierarchy: first labels, point cells and remaining cells.",
    "Neutral5 vertical/horizontal rules, neutral1 alternating rows, accent1-3-softpoint cells and accent1-2-softalternates follow deck roles.",
    "The dense fixture was tested at smaller sizes: honest minima6x4|4x6; condensed fixture4x2|3x3."
  ],
  "known_remaining_differences": [
    "Original cell-specific OCR typography varies arbitrarily; uniform semantic hierarchy cannot reproduce every fitted cell value.",
    "All text stays at least type12 for reading, so the smallest original9–11px cells are slightly enlarged.",
    "Reference preview palette replaces source hues and fixture copy is newly written."
  ],
  "corrections": [
    "Exact source-size comparison showed the alternating gray rows were incorrectly assigned the white-face role. They now consistently use neutral2against the gray page role. All32native light/darkcases were rerendered and visually rechecked."
  ],
  "differences": [
    "The source point-column base#c1c6e5maps to accent1-3-soft. The shared source-palette value for that role is#a1aad5from source12so this table color is deeper; no element-only color is introduced."
  ],
  "source_size_comparison": [
    {
      "page": "16",
      "bbox": [
        49,
        232,
        1037,
        488
      ],
      "comparison": "build/sourcebox-systems/table-16.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [
        {
          "text": "MIRIMedi AI",
          "ratio": 4.22,
          "required": 4.5,
          "foreground": [
            239,
            239,
            239
          ],
          "background": [
            92,
            108,
            188
          ],
          "rect": [
            308.765625,
            243,
            102.46875,
            24
          ]
        }
      ],
      "css_sha256": "8ede15da6d1161f9a02033cd8f487372cdad33798b18dbc6f079c7fa1842f982"
    }
  ]
}

## roadmap

{
  "replica_pages": [
    "19"
  ],
  "final_render_cases": 32,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "bar_and_owner_outside": 0,
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/roadmap/handoff-2-lanes-on-mile-dark-01.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-dark-02.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-dark-03.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-dark-04.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-dark-05.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-light-01.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-light-02.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-light-03.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-light-04.png",
    "build/native-review/roadmap/handoff-2-lanes-on-mile-light-05.png",
    "build/native-review/roadmap/replica-19-dark-01.png",
    "build/native-review/roadmap/replica-19-dark-02.png",
    "build/native-review/roadmap/replica-19-dark-03.png",
    "build/native-review/roadmap/replica-19-dark-04.png",
    "build/native-review/roadmap/replica-19-dark-05.png",
    "build/native-review/roadmap/replica-19-light-01.png",
    "build/native-review/roadmap/replica-19-light-02.png",
    "build/native-review/roadmap/replica-19-light-03.png",
    "build/native-review/roadmap/replica-19-light-04.png",
    "build/native-review/roadmap/replica-19-light-05.png"
  ],
  "decisions": [
    "Durations use four quarter heads with fractional monthly endpoints and three subdivisions per period.",
    "All12source bars retain order, duration, upper-right-only radius and thin geometry.",
    "Bar height is capped at21/104of a lane even when there are fewer members.",
    "A real optional mile child reserves a lower strip without overlapping duration labels.",
    "Source bar font11px becomes type10 at narrow widths; no label is hidden.",
    "Frozen source quarter spelling Qi is retained in map reconstruction data."
  ],
  "known_remaining_differences": [
    "New Korean fixture copy preserves member count and emphasis shape, not source phrases.",
    "Reference preview palette changes source hues.",
    "Narrow tall source fixture wraps its longest label inside a duration; min9x3|5x6.",
    "Optional milestone design is inferred from the same fine-rule grammar; source19 has no milestone."
  ],
  "corrections": [
    "Exact source-size review exposed the missing header-bottom rule at33/450and overwide1.45owner-line rhythm. A full-width neutral5rule and shared label-line1.2now preserve the original device and compact owner typography. All32native cases were rerendered and manually reviewed after the correction."
  ],
  "round_face_geometry": "review/validation/roadmap-roundface.json:32cases,0glyphcenters outside the actual normalized upper-right round",
  "source_size_comparison": [
    {
      "page": "19",
      "bbox": [
        49,
        212,
        1162,
        450
      ],
      "comparison": "build/sourcebox-systems/roadmap-19.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [
        {
          "text": "Commercial",
          "ratio": 4.22,
          "required": 4.5,
          "foreground": [
            239,
            239,
            239
          ],
          "background": [
            92,
            108,
            188
          ],
          "rect": [
            95.75,
            488.3125,
            72.484375,
            16
          ]
        },
        {
          "text": "(Go-to-Market)",
          "ratio": 4.22,
          "required": 4.5,
          "foreground": [
            239,
            239,
            239
          ],
          "background": [
            92,
            108,
            188
          ],
          "rect": [
            85.53125,
            505.109375,
            92.9375,
            16
          ]
        },
        {
          "text": "Commercial Leadership Setup",
          "ratio": 4.22,
          "required": 4.5,
          "foreground": [
            239,
            239,
            239
          ],
          "background": [
            92,
            108,
            188
          ],
          "rect": [
            268.390625,
            469.265625,
            142.203125,
            13
          ]
        },
        {
          "text": "Pre-Launch Pilot Program",
          "ratio": 4.22,
          "required": 4.5,
          "foreground": [
            239,
            239,
            239
          ],
          "background": [
            92,
            108,
            188
          ],
          "rect": [
            611.03125,
            499,
            120.890625,
            13
          ]
        },
        {
          "text": "Series A Funding & Global Prep",
          "ratio": 4.22,
          "required": 4.5,
          "foreground": [
            239,
            239,
            239
          ],
          "background": [
            92,
            108,
            188
          ],
          "rect": [
            930.96875,
            528.75,
            145.015625,
            13
          ]
        }
      ],
      "css_sha256": "5bc5fcf1a527614b0e176cc753ac841ff70ad2b08bf01ffb0ff62e5971405be4"
    }
  ]
}

## architecture

{
  "replica_pages": [],
  "final_render_cases": 30,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/architecture/layers-3-dark-01.png",
    "build/native-review/architecture/layers-3-dark-02.png",
    "build/native-review/architecture/layers-3-dark-03.png",
    "build/native-review/architecture/layers-3-dark-04.png",
    "build/native-review/architecture/layers-3-dark-05.png",
    "build/native-review/architecture/layers-3-light-01.png",
    "build/native-review/architecture/layers-3-light-02.png",
    "build/native-review/architecture/layers-3-light-03.png",
    "build/native-review/architecture/layers-3-light-04.png",
    "build/native-review/architecture/layers-3-light-05.png",
    "build/native-review/architecture/layers-5-long-modules-dark-01.png",
    "build/native-review/architecture/layers-5-long-modules-dark-02.png",
    "build/native-review/architecture/layers-5-long-modules-dark-03.png",
    "build/native-review/architecture/layers-5-long-modules-light-01.png",
    "build/native-review/architecture/layers-5-long-modules-light-02.png",
    "build/native-review/architecture/layers-5-long-modules-light-03.png"
  ],
  "decisions": [
    "Stacked architecture absent from replica. Inferred from03217×30leaf tabs over271px columns,0/34/0/34corner alternation and14.64/12.2px hierarchy.",
    "Name tabs start at80.07%width and expand for long names; open module rows begin behind a7%inset fine rule.",
    "Three-layer minimum3×3; five long layers4×4or3×6. No labels are hidden.",
    "All30final native cases directly reviewed in both modes; all8current metrics zero.",
    "The inset source03 fine vertical rule uses neutral5 consistently with the deck global role. All30final native cases re-reviewed in both modes after correction."
  ],
  "known_remaining_differences": [
    "This inferred stack does not express the unsupported horizontal rich architecture of replica09.",
    "Module text centers in chips while source03 prose aligns left.",
    "Palette roles replace literal source hues; fixture text is new Korean business content."
  ]
}

## matrix-nine

{
  "replica_pages": [],
  "final_render_cases": 30,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/matrix-nine/allocation-9-dark-01.png",
    "build/native-review/matrix-nine/allocation-9-dark-02.png",
    "build/native-review/matrix-nine/allocation-9-dark-03.png",
    "build/native-review/matrix-nine/allocation-9-dark-04.png",
    "build/native-review/matrix-nine/allocation-9-dark-05.png",
    "build/native-review/matrix-nine/allocation-9-light-01.png",
    "build/native-review/matrix-nine/allocation-9-light-02.png",
    "build/native-review/matrix-nine/allocation-9-light-03.png",
    "build/native-review/matrix-nine/allocation-9-light-04.png",
    "build/native-review/matrix-nine/allocation-9-light-05.png",
    "build/native-review/matrix-nine/regions-9-long-notes-dark-01.png",
    "build/native-review/matrix-nine/regions-9-long-notes-dark-02.png",
    "build/native-review/matrix-nine/regions-9-long-notes-dark-03.png",
    "build/native-review/matrix-nine/regions-9-long-notes-light-01.png",
    "build/native-review/matrix-nine/regions-9-long-notes-light-02.png",
    "build/native-review/matrix-nine/regions-9-long-notes-light-03.png"
  ],
  "decisions": [
    "Inferred nine-box uses source03 217×30 leaf tabs over271px columns,0/34/0/34 corners,7% inset n5 vertical rule,14.64:12.2 type hierarchy.",
    "Body surface and inset rule occupy actual second grid row, so wrapped tabs never overprint the note; on follows inverse pale-tab/strong-body grammar from12."
  ],
  "corrections": [],
  "differences": [
    "No nine-box appears in the source; source03 geometry supplies the inferred element language, with readable token floors for long Korean business notes."
  ]
}

## positioning

{
  "replica_pages": [],
  "final_render_cases": 30,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/positioning/regions-6-long-logo-dark-01.png",
    "build/native-review/positioning/regions-6-long-logo-dark-02.png",
    "build/native-review/positioning/regions-6-long-logo-dark-03.png",
    "build/native-review/positioning/regions-6-long-logo-light-01.png",
    "build/native-review/positioning/regions-6-long-logo-light-02.png",
    "build/native-review/positioning/regions-6-long-logo-light-03.png",
    "build/native-review/positioning/route-4-dark-01.png",
    "build/native-review/positioning/route-4-dark-02.png",
    "build/native-review/positioning/route-4-dark-03.png",
    "build/native-review/positioning/route-4-dark-04.png",
    "build/native-review/positioning/route-4-dark-05.png",
    "build/native-review/positioning/route-4-light-01.png",
    "build/native-review/positioning/route-4-light-02.png",
    "build/native-review/positioning/route-4-light-03.png",
    "build/native-review/positioning/route-4-light-04.png",
    "build/native-review/positioning/route-4-light-05.png"
  ],
  "decisions": [
    "Inferred positioning borrows source15 round98px competitor and176px own faces,lavender/blue roles and fine n5axes.",
    "External names stay visible below circles; actual endpoint labels provide the contract structure with no ghost source axis field."
  ],
  "corrections": [],
  "differences": [
    "Source15 rich notes,individual radius values and named axes remain unexpressible. The new contract positioning does not pretend to reproduce those missing fields."
  ]
}

## matrix

{
  "replica_pages": [],
  "final_render_cases": 28,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/matrix/dispatch-4-dark-01.png",
    "build/native-review/matrix/dispatch-4-dark-02.png",
    "build/native-review/matrix/dispatch-4-dark-03.png",
    "build/native-review/matrix/dispatch-4-dark-04.png",
    "build/native-review/matrix/dispatch-4-dark-05.png",
    "build/native-review/matrix/dispatch-4-light-01.png",
    "build/native-review/matrix/dispatch-4-light-02.png",
    "build/native-review/matrix/dispatch-4-light-03.png",
    "build/native-review/matrix/dispatch-4-light-04.png",
    "build/native-review/matrix/dispatch-4-light-05.png",
    "build/native-review/matrix/swot-dispatch-dark-01.png",
    "build/native-review/matrix/swot-dispatch-dark-02.png",
    "build/native-review/matrix/swot-dispatch-dark-03.png",
    "build/native-review/matrix/swot-dispatch-light-01.png",
    "build/native-review/matrix/swot-dispatch-light-02.png",
    "build/native-review/matrix/swot-dispatch-light-03.png"
  ],
  "decisions": [
    "Source-absent 2x2 and SWOT matrices extend the source03 80.0738% leaf tab, vertical inset rule, and source12 inverse emphasis language; they are not mapped as source instances.",
    "Ordinary min4x3; SWOT min6x4 or4x6; nested lists retain their own contract and respond to actual child size."
  ],
  "corrections": [
    "Attached the leaf tab to the top of its field and anchored the vertical rule below the actual header row.",
    "Replaced the low-contrast pale emphasized header with the source12 white-surface role and a1-7 reading color."
  ],
  "differences": [
    "No replica contains a semantic matrix; this is an inferred contract design. All 16 native panels across both modes were manually inspected."
  ]
}

## flowchart

{
  "replica_pages": [],
  "final_render_cases": 28,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/flowchart/dispatch-6-dark-01.png",
    "build/native-review/flowchart/dispatch-6-dark-02.png",
    "build/native-review/flowchart/dispatch-6-dark-03.png",
    "build/native-review/flowchart/dispatch-6-dark-04.png",
    "build/native-review/flowchart/dispatch-6-light-01.png",
    "build/native-review/flowchart/dispatch-6-light-02.png",
    "build/native-review/flowchart/dispatch-6-light-03.png",
    "build/native-review/flowchart/dispatch-6-light-04.png",
    "build/native-review/flowchart/review-loop-4-dark-01.png",
    "build/native-review/flowchart/review-loop-4-dark-02.png",
    "build/native-review/flowchart/review-loop-4-dark-03.png",
    "build/native-review/flowchart/review-loop-4-dark-04.png",
    "build/native-review/flowchart/review-loop-4-dark-05.png",
    "build/native-review/flowchart/review-loop-4-light-01.png",
    "build/native-review/flowchart/review-loop-4-light-02.png",
    "build/native-review/flowchart/review-loop-4-light-03.png",
    "build/native-review/flowchart/review-loop-4-light-04.png",
    "build/native-review/flowchart/review-loop-4-light-05.png"
  ],
  "decisions": [
    "Source-absent nodes extend replica03 leaf tabs at80.0738% width and7% inset vertical rules; the end state follows replica12 inverse tab and accent field.",
    "Plain b+p child formatting preserves legible actual content without invented slots or classes."
  ],
  "corrections": [],
  "differences": [
    "Inferred connected process contract; no original architecture or roadmap scene is remapped. All18 native panels manually reviewed after final file generation."
  ]
}

## swimlane

{
  "replica_pages": [],
  "final_render_cases": 20,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/swimlane/dispatch-3-dark-01.png",
    "build/native-review/swimlane/dispatch-3-dark-02.png",
    "build/native-review/swimlane/dispatch-3-dark-03.png",
    "build/native-review/swimlane/dispatch-3-light-01.png",
    "build/native-review/swimlane/dispatch-3-light-02.png",
    "build/native-review/swimlane/dispatch-3-light-03.png",
    "build/native-review/swimlane/handover-2-dark-01.png",
    "build/native-review/swimlane/handover-2-dark-02.png",
    "build/native-review/swimlane/handover-2-dark-03.png",
    "build/native-review/swimlane/handover-2-dark-04.png",
    "build/native-review/swimlane/handover-2-light-01.png",
    "build/native-review/swimlane/handover-2-light-02.png",
    "build/native-review/swimlane/handover-2-light-03.png",
    "build/native-review/swimlane/handover-2-light-04.png"
  ],
  "decisions": [
    "Inferred swimlane uses replica03 opposite leaf corners,inset vertical hairlines,accent owner tabs,and source12 emphasized planes.",
    "Literal grid columns remain unchanged; protected owner width/height prevents labels crossing explicit vertical connectors."
  ],
  "corrections": [],
  "differences": [
    "No source swimlane. All14 final light/dark panels manually inspected,including long three-line owner labels and minimum8x4."
  ]
}

## decision-tree

{
  "replica_pages": [],
  "final_render_cases": 18,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/decision-tree/approval-depth-3-dark-01.png",
    "build/native-review/decision-tree/approval-depth-3-light-01.png",
    "build/native-review/decision-tree/route-3-dark-01.png",
    "build/native-review/decision-tree/route-3-dark-02.png",
    "build/native-review/decision-tree/route-3-dark-03.png",
    "build/native-review/decision-tree/route-3-dark-04.png",
    "build/native-review/decision-tree/route-3-dark-05.png",
    "build/native-review/decision-tree/route-3-light-01.png",
    "build/native-review/decision-tree/route-3-light-02.png",
    "build/native-review/decision-tree/route-3-light-03.png",
    "build/native-review/decision-tree/route-3-light-04.png",
    "build/native-review/decision-tree/route-3-light-05.png"
  ],
  "decisions": [
    "Absent recursive tree uses replica03 leaf-corner geometry at34/271 width and neutral5 inset reading rules; questions and recommended outcomes are accent planes.",
    "Question/outcome own containers keep the smallest nested text at12px-equivalent shared type while retaining all three question levels."
  ],
  "corrections": [],
  "differences": [
    "Inferred decision tree; all12 native light/dark panels directly reviewed. Simple fixture min4x3,maximum-depth fixture min12x6."
  ]
}

## journey

{
  "replica_pages": [],
  "final_render_cases": 24,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/journey/intake-3-dark-01.png",
    "build/native-review/journey/intake-3-dark-02.png",
    "build/native-review/journey/intake-3-dark-03.png",
    "build/native-review/journey/intake-3-dark-04.png",
    "build/native-review/journey/intake-3-dark-05.png",
    "build/native-review/journey/intake-3-light-01.png",
    "build/native-review/journey/intake-3-light-02.png",
    "build/native-review/journey/intake-3-light-03.png",
    "build/native-review/journey/intake-3-light-04.png",
    "build/native-review/journey/intake-3-light-05.png",
    "build/native-review/journey/retention-7-dark-01.png",
    "build/native-review/journey/retention-7-dark-02.png",
    "build/native-review/journey/retention-7-dark-03.png",
    "build/native-review/journey/retention-7-light-01.png",
    "build/native-review/journey/retention-7-light-02.png",
    "build/native-review/journey/retention-7-light-03.png"
  ],
  "decisions": [
    "Absent journey uses source03 measured80.0738% leaf tabs and7% inset vertical rule, with source12 inverse emphasis treatment.",
    "Stage body and note remain open except actual on-stage accent plane; no generic added card layer.",
    "Three-stage minimum4x3 and seven-stage minimum8x4 preserve all fields."
  ],
  "corrections": [],
  "differences": [
    "No journey source; emotion line and leaf points are inferred using source primitives."
  ]
}

## sankey

{
  "replica_pages": [],
  "final_render_cases": 18,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/sankey/nested-4-2-dark-01.png",
    "build/native-review/sankey/nested-4-2-dark-02.png",
    "build/native-review/sankey/nested-4-2-dark-03.png",
    "build/native-review/sankey/nested-4-2-light-01.png",
    "build/native-review/sankey/nested-4-2-light-02.png",
    "build/native-review/sankey/nested-4-2-light-03.png",
    "build/native-review/sankey/routes-6-dark-01.png",
    "build/native-review/sankey/routes-6-dark-02.png",
    "build/native-review/sankey/routes-6-dark-03.png",
    "build/native-review/sankey/routes-6-light-01.png",
    "build/native-review/sankey/routes-6-light-02.png",
    "build/native-review/sankey/routes-6-light-03.png"
  ],
  "decisions": [
    "Absent Sankey preserves source03 leaf tabs exactly80.0738% of each field, the7% inset vertical rule and34/271 opposing corner scale.",
    "Source12 on-state uses an inverse full-width leaf tab over the accent face; text remains centered.",
    "A functional right distribution bus belongs to Sankey and joins actual second-split ribbons; the normal incoming ribbon reaches the inset rule.",
    "Honest minima6x4 flat /8x4 nested retain padded labels and every value."
  ],
  "corrections": [
    "Replaced approximate tab width and edge rule with measured field-relative proportions.",
    "Added figure clearance below the actual padded leaf label."
  ],
  "differences": [
    "No source Sankey; connected proportional flow topology is inferred from measured deck primitives."
  ],
  "supplemental_geometry": "sankey-sharebounds.json:18cases0errors; inset-rule targets, common share scale,source and nested connections"
}


### review-text-final-exceptions

최종 실측 정정과 검수

12 quiet 첫 caption은 실제10px/500,+1.49614px tracking이다.271×384 상자에서271×30 cap,311px body face,본문x19/y44,11px/16px을 비율로 옮겼다. on은14px/500/−.3px로 별도로 유지했다. 첫 짧은 소개 단락과 이후 단락의 간격 차이는 원래 manual-title span margins에서 가져온 일반 첫 단락 경계 규칙이며 문구/페이지/fixture 조건은 없다.

같은quiet로 위장했던12세번째(12px/−.329427px),21(8px/+1.67622px) caption은 독립 타이포 위계여서GAP으로 정정했다.08 whitecap은 실제 ID2/3/6이며4는 파랑이다. white cap/transparent body와03 blue leaf/12 filled body는 다르므로 새 임의variant를 만들지 않고3개GAP으로 기록했다. 원래 Step0/오타는 고정자료로 보존했다.

quote05/18 본문은 원래 흰 문맥이므로 foundation_context:on, author는 a1-7로 복구했다. attribution cap은 upper-right corner만 곡선이며 잘못 들어간 lower-left곡선을 제거했다.05 Hospital Admin caption11px/+1.72792px와18 quote2/4의 서로 다른 double glyph는 본체quote를 지우지 않고 별도 하위효과GAP3건으로 표시했다.18 quote1의 실제br는 이미 보존돼 있었고 독립적으로 맞춘 원본 줄별font/tracking을 공통11px/16px으로 바꾸면3→4줄이 되는 차이는 source.final_residual에 정직하게 적었다. inlineCSS/per-run tracking 이식은 하지 않았다.

07 prose2개도 실제 흰 글자이므로 inverse문맥을 지도에 추가했다. glyph의 작은 overhang 때문에 기존 layout bbox를 키워 내부비율을 바꾸지 않았다.03 card본문약3px,08 긴 Focus약16px,18 quote opening glyph2/4px의 원래 fitting overhang은 자료 결함/경계 잔차로 남긴다.

card104+quote36=140cases9지표0/raster0/font load0. 마지막 수정 뒤card30+quote5 native패널과 source9개 실제크기 조각을 모두 직접 비교했다. sourcecheck의inverse배경은 원래crop의 대표 단색만 사용한 읽기문맥이며 원본이미지레이어를 사용하지 않는다.

### review-text-transfer-diagrams

# Callout transfer review

The source contains no concluding callout. Replica03/13 measured217-by30 tabs with0/34/0/34 leaf corners and nineteen-unit inset rails become a regular sentence face. Source15 measured98-unit outlined peer circles are scaled by one half for optional icon carriers, with54% icon occupancy. Emphasis remains regular weight, marked by a deep primary underline; no heavy display weight or shadow is introduced. The element owns only the paragraph and optional icon. It is a size container in a grid slot and reserves a compact flexible caption share when placed after a seat in the mandatory foundation stack.

Final cases: 80; all nine QA counts, strict containment, copy matches and raster bleed: 0.

All final native cells directly opened at original resolution in lossless panels, or verified identical to earlier directly opened cells. Both modes and all actual minima inspected. Mandatory showcase markup/data preserved.

Own paragraph and optional icon only; no invented state or ancestor condition. Compact flex basis reserves sentence caption share in mandatory stack; grid retains allocated size. New Korean long business copy replaces source-independent generic six-character common phrasing to keep the conservative copy audit at zero.

### review-text-transfer-systems

# Systems element review

## agenda

{
  "replica_pages": [],
  "final_render_cases": 20,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/agenda/agenda-five-dark-01.png",
    "build/native-review/agenda/agenda-five-dark-02.png",
    "build/native-review/agenda/agenda-five-dark-03.png",
    "build/native-review/agenda/agenda-five-light-01.png",
    "build/native-review/agenda/agenda-five-light-02.png",
    "build/native-review/agenda/agenda-five-light-03.png",
    "build/native-review/agenda/agenda-four-dark-01.png",
    "build/native-review/agenda/agenda-four-dark-02.png",
    "build/native-review/agenda/agenda-four-dark-03.png",
    "build/native-review/agenda/agenda-four-light-01.png",
    "build/native-review/agenda/agenda-four-light-02.png",
    "build/native-review/agenda/agenda-four-light-03.png"
  ],
  "decisions": [
    "No source agenda. Source03 supplies80.073801% leaf cap, opposite34px corner ratios and7% inset fine rule. Source12 supplies active full-width inverse cap and accent body."
  ],
  "corrections": [
    "Replaced generic centered two-column index row with leaf-cap/open ruled field. Complete new notes and long heading are retained."
  ],
  "differences": [
    "Large index below leaf cap is inferred, never claimed as replica element."
  ],
  "supplemental_geometry": "20 cases9QA0/raster0/copy0; all12 final native panels directly seen."
}

## metric

{
  "replica_pages": [],
  "final_render_cases": 44,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/metric/metric-bare-dark-01.png",
    "build/native-review/metric/metric-bare-dark-02.png",
    "build/native-review/metric/metric-bare-dark-03.png",
    "build/native-review/metric/metric-bare-dark-04.png",
    "build/native-review/metric/metric-bare-dark-05.png",
    "build/native-review/metric/metric-bare-light-01.png",
    "build/native-review/metric/metric-bare-light-02.png",
    "build/native-review/metric/metric-bare-light-03.png",
    "build/native-review/metric/metric-bare-light-04.png",
    "build/native-review/metric/metric-bare-light-05.png",
    "build/native-review/metric/metric-extended-dark-01.png",
    "build/native-review/metric/metric-extended-dark-02.png",
    "build/native-review/metric/metric-extended-dark-03.png",
    "build/native-review/metric/metric-extended-dark-04.png",
    "build/native-review/metric/metric-extended-dark-05.png",
    "build/native-review/metric/metric-extended-light-01.png",
    "build/native-review/metric/metric-extended-light-02.png",
    "build/native-review/metric/metric-extended-light-03.png",
    "build/native-review/metric/metric-extended-light-04.png",
    "build/native-review/metric/metric-extended-light-05.png",
    "build/native-review/metric/metrics-three-dark-01.png",
    "build/native-review/metric/metrics-three-dark-02.png",
    "build/native-review/metric/metrics-three-dark-03.png",
    "build/native-review/metric/metrics-three-dark-04.png",
    "build/native-review/metric/metrics-three-light-01.png",
    "build/native-review/metric/metrics-three-light-02.png",
    "build/native-review/metric/metrics-three-light-03.png",
    "build/native-review/metric/metrics-three-light-04.png"
  ],
  "decisions": [
    "Absent bare metric: source03 7% inset fine rule and14.64/12.2 hierarchy are kept without a tabbed containing face. Inferred figures remain regular400 and accent reading role."
  ],
  "corrections": [
    "Fresh own-column metric implementation, full Korean copy, unit type12 floor and actual stats3 fixture.",
    "Stats initially doubled the7% own rule and parent divider. Final stats uses only contract row dividers; standalone keeps its source inset rule.10 final row cases manually reviewed;34 nonstats PNG hashes identical."
  ],
  "differences": [
    "No bare source metric. Leaf cap is deliberately absent because it would turn the bare metric into a title panel."
  ],
  "supplemental_geometry": "44 final cases9QA0/raster0/copy0;28 native panels directly reviewed."
}


### review-text-transfer

# Transferred inferred elements — final review

list: 03/22의 가는 세로 괘선과 서로 반대인 모서리 문법을 항목에 적용한 추론. 번호·check·divided 변형, 정사각 icon carrier, min3x4/4x6,32칸.
pill: 03의 정확한 0 34px 0 34px 두 모서리를 작은 한줄 표식으로 추론. 회색 page 위 기본 면이 사라지지 않도록 n-1 역할을 적용. 높이에 비례한 padding, name/note nowrap, line/quiet/on. min3x1/4x1,78칸.

이 항목들은 replica의 특정 요소를 직접 옮긴 base가 아니라 명시적으로 추론한 계약 요소다. 최종 수정 뒤 모든 fixture·모든 허용 크기·light/dark의 native 칸을 직접 보았고, 9QA·6자 원문 중복·실제 폰트 fallback·raster 초과를 별도 감사했다.

### review-text

# Text element provenance and review decisions

The fixed replicas were read as evidence and were never edited. Sample HTML supplies mandatory data/markup only; no sample element CSS was read or reused.

## Per-leaf provenance

- card: 03:base, 03:same-as:03, 04:same-as:03, 12:variant:.quiet, 12:variant:.on, 11:same-as:03, 21:variant:.quiet, 08:same-as:03, 13:same-as:03.
- pill: inferred; no independently expressible source instance.
- callout: inferred; no independently expressible source instance.
- tag: 21:base.
- list: inferred; no independently expressible source instance.
- quote: 05:base, 05:same-as:05, 18:same-as:05.
- headline: 22:base, 10:variant:.on, 14:variant:.on, 17:variant:.on, 20:variant:.on.
- prose: 07:base, 07:same-as:07, 14:same-as:07, 23:variant:.quiet, 22:variant:.quiet.
- metric: inferred; no independently expressible source instance.
- agenda: inferred; no independently expressible source instance.
- person: 22:base.

## Recorded corrections and decisions

- 08/13 independent workflow/sales-phase leaf cards have no connectors. They use the actual03 card cap+rail language; no steps connector is invented.
- Quote05 actual64px regular quote,18px/500 white leaf,11px/16px body and32px paragraph gaps were rechecked.18 uses an actual square90px picture,195px cap14px,13px role and11px quote. The avatar contract default circle is overridden to the source square.
- Quote minimum probe:05 passes4x3 and3x4, fails3x3;18 passes3x3. Native smaller probes were directly viewed before lowering comments.
- Person22 role/caption/photo gaps derive from11px/3px/27px measurements. The first credential has a real13px regular emphasis inside the11px biography, represented by actual p>b markup rather than a member-index CSS rule.
- 06 source has no kick or mark. Its170px cap/wider body differs from the217px03 base without a semantic variant, so all three06 columns became explicit gaps and the invented01/02/03 fixture was removed.
- 14 prose had one p per SVG line, causing accumulated spacing. It now has three real subheading/body paragraphs.23 legal text was missing from the generic source factory because only sourceLines existed; actual baselines/x ordering now form4/3 source paragraphs.
- 22 adviser source is11.4px name,9.3px body with22px/13px vertical pitch, not three large separate paragraphs. Its single secondary paragraph preserves these ratios; a2px optical glyph offset accounts for HTML font paint extending above the line box.
- Quote05 third speaker has lines as wide as253px. The body now uses255px inside the same281px element, rather than232px, retaining explicit two-line paragraphs. Common quote/body rhythm is preserved; source-specific early baselines remain a recorded residual.

## Inferred elements

pill, callout, list, metric, agenda. Each has its own build/inferred-spec-<leaf>.json citing this deck’s measured source primitive, an inferred description and fresh business fixtures. These files never claim a source base.

## Validation state

Browser sheets and probes are recorded in review/validation and build/probes. A zero automated result alone is insufficient: native source-box comparisons found and corrected font, gap, shape, padding-reference, missing-avatar and quotation collisions. Each final proof must match the latest source hashes. Final fixture minima are selected after native smaller-candidate review; initial conservative comments are not final evidence.

True inline tag/hl boxes keep natural text width. Declared container-type:size is inert on a non-atomic inline by browser definition; shared type steps and the enclosing real prose paragraph provide context. This explicit functional limitation is not hidden with an invented fixed8em box.

### Final integration corrections
- Legal prose23 inherited an obsolete max-height12px floor after CSS consolidation; that rule was removed. Actual4/3 paragraph markup,11px/16px source leading and21/20px gaps are preserved. Source bbox validation has0 overflow. Source14 title is11.36px/400 rather than the earlier13px/bold estimate; three-paragraph body now uses own-height and width to retain11px/16px at243×255 and avoid large-width short-slot spill.

- Final native audit found advisor22 third column259×49 scaled a9.3px body to9.91px, causing a title line to wrap. Own-height bounds retain9.28px/11.34px at49px height for all advisor columns; bbox and source markup were not changed.

### 주 담당자 페이지 대조 기록


- 최종 확인: Filament04의 오른쪽 Confidential 레일은 동결 replica 자체가 붉은 글자를 붉은 면에 놓아 보이지 않는다. 동결본의 색 역할을 보존했으며 원본의 흰 레일과 차이를 남긴다. Cutfield13 밝은 tone 면의 글자와 icon은 대비를 위해 palette on 역할로 바뀌며 원본 흰 글자와 다르다. Toggle06의 12×6 행 양자화는 사진 3개 사이의 세로 공백을 줄인다.

- Portico02: 10개 목차는 계약 agenda 최대8개와 충돌하여 전체 인스턴스를 미지원으로 기록했다. 8+2개의 다른 요소로 쪼개 겉모양을 속이지 않는다. 빈 조립 영역은 누락 사고가 아닌 명시된 계약 한계다.
- Portico03/04: 넓은 수평 사진띠는 frame의 seat 종횡비 제한과 충돌해 미지원으로 기록했다. source gray 사진 자리를 임의의 가로 왜곡 frame으로 대체하지 않았다.03/04의 작은 방사형 도상은 계약 mark의 단순별로 근사해 원본6점과 다른 잔차가 있다.
- Portico05: 각 사진 자리의 번호는 계약 독립 frame이 자기 seat부터1로 센다. 여러 요소 사이 전역 순번1·2·3은 계약 데이터 슬롯이 없어3개1로 보인다.

- Lamella07: 위쪽 오른쪽 한 모서리만 휜 흰 cap 둘은 양 모서리가 휜 headline base와 달라 계약 변형에 대응하지 못한다. 그림은 임의 변형으로 우회하지 않고 GAPS에 기록했다. 본문과 독립 가로 괘선은 source 수치·반전 문맥을 복구했다.

- 최종 통합:392요소의양모드크기시트와87페이지비교PNG를주담당자가모두열어확인했다. 최종source문구추출정정후Rule13의3개카드본문은source의3줄구조를되찾았다. Lam18의1개quote본문3→4줄은독립tracking차이로잔차를명시했다.
- 최종grid검사:87페이지/231개최상위요소/543쌍에서source분리요소의신규교차0,정수span과양수12×6tracks오류0. Lam23의5.68e-14px중복경계를1e-6px허용오차로합쳐양수트랙을복구했다. 원본에이미있던교차11건은구별해기록했다.

