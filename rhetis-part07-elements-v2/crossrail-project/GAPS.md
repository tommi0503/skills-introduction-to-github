# Crossrail 계약상 미표현 영역



지원되는 원문과 공개 수치는 조립본에 보존한다. 미지원 두번째 디자인을 임의 source/fixture 조건으로 숨겨 구현하지 않는다. 계산가능한max축의4tick은GAP이아니며CSS일반수학으로그린다.



## p05-furniture-source-2

원본05 / bbox `[502, 0, 778, 720]`

778×720px, 좌표(502,0)의 The source has a right accent field behind three panels whose top edge begins beside the title. The normal head/body and one sidebar base cannot reserve this independent header-overlap composition without a new layout contract..

The source has a right accent field behind three panels whose top edge begins beside the title. The normal head/body and one sidebar base cannot reserve this independent header-overlap composition without a new layout contract.

필요한 계약 마크업: `<div class="page side-heading"><header class="head">…</header><div class="body">…</div><div class="field"></div></div>`.



## p07-left-explanations-heading-band

원본07 / bbox `[95, 260, 307, 395]`

307×395px, 좌표(95,260)의 The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.. 4개의1px 경계/연결선이 포함된다.

The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.

필요한 계약 마크업: `<div class="headline quiet"><h2>…</h2></div> (new quiet ruled-strip variant)`.



## p07-semicircle

원본07 / bbox `[426, 343, 426, 231]`

426×231px, 좌표(426,343)의 The source has four peer nodes following a semicircular track and a separate lower caption. No spoke connects a central core to the peers, so hub.radial cannot express this relation.. 보이는 텍스트 6개; 글자 16px, 18px, 26px / 굵기 400, 700. 첫 문구는 “정직”. 원 또는 capsule 모서리 4개를 포함한다.

The source has four peer nodes following a semicircular track and a separate lower caption. No spoke connects a central core to the peers, so hub.radial cannot express this relation.

필요한 계약 마크업: `<div class="arc-track"><div class="node">…</div>…<div class="caption">…</div></div> (a contracted semicircular peer-track element)`.



## p07-right-explanations-heading-band

원본07 / bbox `[877, 260, 307, 395]`

307×395px, 좌표(877,260)의 The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.. 4개의1px 경계/연결선이 포함된다.

The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.

필요한 계약 마크업: `<div class="headline quiet"><h2>…</h2></div> (new quiet ruled-strip variant)`.



## p14-forward-three

원본14 / bbox `[95, 260, 1090, 170]`

1090×170px at(95,260): three separate right-facing chevrons with visible gaps, navy/slate/pale ordinal fills, 01/02/03 labels, names and secondary notes below. This is a second steps design unsupported by the source10 continuous-rail base.

This source uses three independently spaced chevrons with three different ordinal fills. The single horizontal steps base from source10 is a continuous same-fill connected rail. Neither the allowed .col variant nor an optional mark/name/note changes that design; treating them as same-as10 was incorrect.

필요한 계약 마크업: `<div class="steps separated"><div class="step tone-1">…</div><div class="step tone-2">…</div><div class="step tone-3">…</div></div> (a separately contracted spaced-chevron design)`.



## p14-reverse-three

원본14 / bbox `[95, 486, 1090, 168]`

1090×168px, 좌표(95,486)의 The sequence contract supplies horizontal and downward flow, but no reverse-flow variant. RTL text direction is not a visual design variant.. 보이는 텍스트 9개; 글자 18px, 26px / 굵기 400, 700. 첫 문구는 “06”. 3개의1px 경계/연결선이 포함된다.

The sequence contract supplies horizontal and downward flow, but no reverse-flow variant. RTL text direction is not a visual design variant.

필요한 계약 마크업: `<div class="steps reverse"><div class="step"><b class="mark">…</b><b class="name">…</b><p class="note">…</p></div>…</div>`.



## p17-central-icon-orbit

원본17 / bbox `[491, 309, 298, 298]`

298×298px, 좌표(491,309)의 The source contains icon-only nodes without member names or notes. Empty semantic hub members would distort the contract.. 보이는 텍스트 1개; 글자 16px / 굵기 400. 첫 문구는 “시장 매력도”. 2개의1px 경계/연결선이 포함된다. 원 또는 capsule 모서리 2개를 포함한다.

The source contains icon-only nodes without member names or notes. Empty semantic hub members would distort the contract.

필요한 계약 마크업: `<div class="hub icon-orbit"><div class="core">…</div><div class="spoke"><span class="icon" data-icon="…"></span></div>…</div> (icon-only spokes on a circular orbit without required member labels)`.



## p18-left-strengths-heading-band

원본18 / bbox `[95, 279, 307, 376]`

307×376px, 좌표(95,279)의 The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.. 2개의1px 경계/연결선이 포함된다.

The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.

필요한 계약 마크업: `<div class="headline quiet"><h2>…</h2></div> (new quiet ruled-strip variant)`.



## p18-pentagon

원본18 / bbox `[442, 257, 394, 398]`

394×398px, 좌표(442,257)의 A pentagonal outline with icon-only vertices is a different hub design. The chosen base is an open semicircle; the hub contract has no polygon variant.. 보이는 텍스트 2개; 글자 18px, 26px / 굵기 700. 첫 문구는 “우리의 강점”. 원 또는 capsule 모서리 5개를 포함한다.

A pentagonal outline with icon-only vertices is a different hub design. The chosen base is an open semicircle; the hub contract has no polygon variant.

필요한 계약 마크업: `<div class="hub icon-orbit"><div class="core">…</div><div class="spoke"><span class="icon" data-icon="…"></span></div>…</div> (icon-only spokes and explicit orbit geometry)`.



## p18-right-strengths-heading-band

원본18 / bbox `[882, 226, 307, 429]`

307×429px, 좌표(882,226)의 The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.. 3개의1px 경계/연결선이 포함된다.

The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.

필요한 계약 마크업: `<div class="headline quiet"><h2>…</h2></div> (new quiet ruled-strip variant)`.



## p20-highlighted-row

원본20 / bbox `[95, 394, 567, 84]`

567×84px, 좌표(95,394)의 The source emphasizes a complete row, while table.pick denotes a column focus. A row-focus extension is required..

The source emphasizes a complete row, while table.pick denotes a column focus. A row-focus extension is required.

필요한 계약 마크업: `<table class="table"><tbody><tr class="pick-row"><th scope="row">…</th><td>…</td>…</tr></tbody></table>`.



## p22-background-columns

원본22 / bbox `[798, 322, 356, 303]`

356×303px, 좌표(798,322)의 The two unlabeled background columns are a mixed-chart layer whose independent labels and values are not supplied by the source..

The two unlabeled background columns are a mixed-chart layer whose independent labels and values are not supplied by the source.

필요한 계약 마크업: `<div class="lines mixed"><div class="bands"><div class="band" style="--at:N;--v:N"></div>…</div><div class="pt" style="--v:N">…</div>…</div>`.



## p22-furniture-source-16

원본22 / bbox `[1021, 261, 162, 31]`

162×31px top-right plot caption panel: navy rectangular fill and a white18px title, 일별 생산량 추세. A separate chart-panel header is required.

The chart has a separate small rectangular title panel above its plot. The line-chart contract provides data points, series and axes but no title-panel slot. The single tag base is the source15 circular/pill badge; using it as a separate square title-panel design would be an undocumented second design.

필요한 계약 마크업: `<div class="chart-panel"><div class="panel-title">…</div><div class="lines" data-el="crossrail-chart-line">…</div></div> (a contracted chart title panel)`.



## p23-annotated-comparison

원본23 / bbox `[95, 260, 1090, 395]`

1090×395px, 좌표(95,260)의 A standard bar root cannot move its values into external text capsules or hide values while independent pills repeat them. An annotated-bar contract needs caption, unit and note parts.. 보이는 텍스트 13개; 글자 16px, 18px, 24px, 26px / 굵기 400, 700. 첫 문구는 “0”. 3개의1px 경계/연결선이 포함된다. 원 또는 capsule 모서리 4개를 포함한다.

A standard bar root cannot move its values into external text capsules or hide values while independent pills repeat them. An annotated-bar contract needs caption, unit and note parts.

필요한 계약 마크업: `<div class="bars annotated"><div class="axis-y">…</div><div class="plot"><div class="bar" style="--v:N">…</div>…</div><div class="captions"><div class="caption"><b class="fig">N</b><b class="name">…</b><p class="note">…</p></div>…</div></div>`.



## p24-multi-share-pie

원본24 / bbox `[673, 247, 597, 374]`

597×374px, 좌표(673,247)의 A one-share donut does not encode five jointly partitioned segments or per-segment leaders. Transparent overlaid roots would fabricate a new contract design.. 보이는 텍스트 11개; 글자 16px, 18px / 굵기 400, 700. 첫 문구는 “글로벌 매출 Global”. 원 또는 capsule 모서리 2개를 포함한다.

A one-share donut does not encode five jointly partitioned segments or per-segment leaders. Transparent overlaid roots would fabricate a new contract design.

필요한 계약 마크업: `<div class="pie" style="--max:100"><div class="seg" style="--v:N"><b class="fig">N%</b><span class="name">segment</span></div>…<div class="core">…</div><div class="leader">…</div></div>`.



## p26-first-underlay

원본26 / bbox `[274, 343, 455, 79]`

455×79px, 좌표(274,343)의 The image reference has a pale time-rail field behind the first coloured bar. The coloured bar and its label are ordinary roadmap data and are not omitted. Only this additional underlay field lacks a contract part..

The image reference has a pale time-rail field behind the first coloured bar. The coloured bar and its label are ordinary roadmap data and are not omitted. Only this additional underlay field lacks a contract part.

필요한 계약 마크업: `<div class="roadmap"><div class="lane"><b class="name">…</b><div class="range" style="--from:N;--to:N"></div><div class="bar" style="--from:N;--to:N">…</div></div>…</div>`.



## p26-final-underlay

원본26 / bbox `[729, 575, 455, 80]`

455×80px, 좌표(729,575)의 Only the pale time-rail field behind the final coloured bar is unsupported. The final bar and its label are restored as normal roadmap data..

Only the pale time-rail field behind the final coloured bar is unsupported. The final bar and its label are restored as normal roadmap data.

필요한 계약 마크업: `<div class="roadmap"><div class="lane"><b class="name">…</b><div class="range" style="--from:N;--to:N"></div><div class="bar" style="--from:N;--to:N">…</div></div>…</div>`.



## p27-two-line-capsules

원본27 / bbox `[95, 261, 545, 86]`

545×86px, 좌표(95,261)의 The pill contract is a one-line capsule; date and event are stacked in the source. A stacked-pill variant is required.. 보이는 텍스트 2개; 글자 26px / 굵기 700. 첫 문구는 “15일 리드 회의”. 원 또는 capsule 모서리 2개를 포함한다.

The pill contract is a one-line capsule; date and event are stacked in the source. A stacked-pill variant is required.

필요한 계약 마크업: `An explicit named contract part is required for this visual role; no supplied part has this meaning. See why and sourceMeasurements for the exact omitted shape.`.



## p27-calendar

원본27 / bbox `[662, 260, 523, 395]`

523×395px, 좌표(662,260)의 The calendar needs day-cell layout, a contiguous date-range highlight and event captions. These are not table column-pick semantics.. 보이는 텍스트 46개; 글자 14px, 16px / 굵기 400. 첫 문구는 “SUN”. 1개의1px 경계/연결선이 포함된다.

The calendar needs day-cell layout, a contiguous date-range highlight and event captions. These are not table column-pick semantics.

필요한 계약 마크업: `<div class="calendar"><div class="weekdays">…</div><div class="dates"><div class="date" style="--day:N">N</div>…<div class="range" style="--from:N;--to:N">event</div></div></div>`.



## p29-progress-arrow

원본29 / bbox `[304, 350, 190, 164]`

190×164px, 좌표(304,350)의 The positioning contract has point coordinates but no links or trajectory data. A relation part is required.. 2개의1px 경계/연결선이 포함된다.

The positioning contract has point coordinates but no links or trajectory data. A relation part is required.

필요한 계약 마크업: `<div class="posmap"><div class="trajectory" style="--from-x:N;--from-y:N;--to-x:N;--to-y:N"></div>existing marks</div>`.



## p29-highlighted-row

원본29 / bbox `[681, 610, 504, 44]`

504×44px, 좌표(681,610)의 The complete final row is highlighted; column-pick cannot represent a row emphasis without changing its semantics.. 1개의1px 경계/연결선이 포함된다.

The complete final row is highlighted; column-pick cannot represent a row emphasis without changing its semantics.

필요한 계약 마크업: `<table class="table"><tbody><tr class="pick-row"><th scope="row">…</th><td>…</td>…</tr></tbody></table>`.



## p19-header-direction-arrow

원본19 / bbox `[95, 260, 1090, 65]`

1090×65px, 좌표(95,260)의 The directional comparison mark is supported by versus and drawn inside its root. The source puts it between two independent header bands above the fixed body slot; that position cannot be represented without a comparison-panel composition. The page grid is not shifted..

The directional comparison mark is supported by versus and drawn inside its root. The source puts it between two independent header bands above the fixed body slot; that position cannot be represented without a comparison-panel composition. The page grid is not shifted.

필요한 계약 마크업: `<div class="comparison-panel"><div class="headers"><div class="from">…</div><div class="mark"></div><div class="to">…</div></div><div class="faces">…</div></div> (a contracted header-and-faces comparison composition)`.



## p21-foundation-independent-metrics

원본21 / bbox `[367, 260, 817, 394]`

817×394px, 좌표(367,260)의 The source has a 235px rank area and two equal 402px metric columns. With body x95 width1090 and pitch(1090+12)/12=91.833px, source x367/w402 rounds to col4/span5 while x782/w402 rounds to col8/span5. The resulting one-column overlap hides text. Shrinking one span would be a page-specific visual correction rather than faithful bbox mapping. Four independently valid card fixtures therefore remain in the library, but their unsupported simultaneous page layout is omitted from this assembly..

The source has a 235px rank area and two equal 402px metric columns. With body x95 width1090 and pitch(1090+12)/12=91.833px, source x367/w402 rounds to col4/span5 while x782/w402 rounds to col8/span5. The resulting one-column overlap hides text. Shrinking one span would be a page-specific visual correction rather than faithful bbox mapping. Four independently valid card fixtures therefore remain in the library, but their unsupported simultaneous page layout is omitted from this assembly.

필요한 계약 마크업: `<div class="body metric-summary"><div class="rank">…</div><div class="metric-grid">…</div></div> (a contracted foundation layout with independent rank and equal two-column metric region)`.



## p11-panel-separator

원본11 / bbox `[640, 260, 1, 396]`

1×396px, 좌표(640,260)의 The source has one continuous vertical divider at the centre of the body. The contracted foundation rail is an edge rail and the four independent cards cannot own this full-height page separator without sibling or page geometry conditions.. 1개의1px 경계/연결선이 포함된다.

The source has one continuous vertical divider at the centre of the body. The contracted foundation rail is an edge rail and the four independent cards cannot own this full-height page separator without sibling or page geometry conditions.

필요한 계약 마크업: `<div class="body ruled-columns">…</div> (a contracted foundation two-column body divider)`.



## p18-left-strengths-list-2-single-marker

원본18 / bbox `[103, 353, 5.33, 26]`

5.33×26px, 좌표(103,353)의 A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker..

A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker.

필요한 계약 마크업: `<div class="prose marked"><p>…</p></div> (a contracted single-paragraph marker variant)`.



## p18-left-strengths-list-3-single-marker

원본18 / bbox `[103, 569, 5.33, 26]`

5.33×26px, 좌표(103,569)의 A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker..

A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker.

필요한 계약 마크업: `<div class="prose marked"><p>…</p></div> (a contracted single-paragraph marker variant)`.



## p18-right-strengths-list-2-single-marker

원본18 / bbox `[889, 300, 5.33, 26]`

5.33×26px, 좌표(889,300)의 A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker..

A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker.

필요한 계약 마크업: `<div class="prose marked"><p>…</p></div> (a contracted single-paragraph marker variant)`.



## p18-right-strengths-list-3-single-marker

원본18 / bbox `[889, 454, 5.33, 26]`

5.33×26px, 좌표(889,454)의 A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker..

A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker.

필요한 계약 마크업: `<div class="prose marked"><p>…</p></div> (a contracted single-paragraph marker variant)`.



## p18-right-strengths-list-4-single-marker

원본18 / bbox `[889, 609, 5.33, 26]`

5.33×26px, 좌표(889,609)의 A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker..

A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker.

필요한 계약 마크업: `<div class="prose marked"><p>…</p></div> (a contracted single-paragraph marker variant)`.



## p22-maximum-outline

원본22 / bbox `[320, 494, 212, 72]`

212×72px, 좌표(320,494)의 The number/name/note remain a bare metric. The source puts a capsule outline around the number, but metric.bare explicitly has no surface; this ornament is not hidden in metric CSS..

The number/name/note remain a bare metric. The source puts a capsule outline around the number, but metric.bare explicitly has no surface; this ornament is not hidden in metric CSS.

필요한 계약 마크업: `<div class="numeric-badge"><span class="fig">…</span></div> (a separate contracted numeric badge)`.



## p17-four-market-panels-1-boundary

원본17 / bbox `[95, 260, 527, 181]`

527×181px independent enclosing rectangle at(95,260), one-pixel pale border and slate fill. It is additional furniture around the supported card name/note.

The source11/12 line-card design has an open accent rule, not a complete enclosing box. Adding this second outline design by an undocumented part/source condition would violate the one-design-per-variant rule. Text remains supported in the line card; only the extra enclosing rectangle is omitted.

필요한 계약 마크업: `<div class="outlined-panel"><div class="card line" data-el="crossrail-card">…</div></div> (a contracted enclosing panel distinct from the open line card)`.



## p17-four-market-panels-2-boundary

원본17 / bbox `[657, 260, 527, 181]`

527×181px independent enclosing rectangle at(657,260), one-pixel pale border. It is additional furniture around the supported card name/note.

The source11/12 line-card design has an open accent rule, not a complete enclosing box. Adding this second outline design by an undocumented part/source condition would violate the one-design-per-variant rule. Text remains supported in the line card; only the extra enclosing rectangle is omitted.

필요한 계약 마크업: `<div class="outlined-panel"><div class="card line" data-el="crossrail-card">…</div></div> (a contracted enclosing panel distinct from the open line card)`.



## p17-four-market-panels-3-boundary

원본17 / bbox `[95, 473, 527, 181]`

527×181px independent enclosing rectangle at(95,473), one-pixel pale border. It is additional furniture around the supported card name/note.

The source11/12 line-card design has an open accent rule, not a complete enclosing box. Adding this second outline design by an undocumented part/source condition would violate the one-design-per-variant rule. Text remains supported in the line card; only the extra enclosing rectangle is omitted.

필요한 계약 마크업: `<div class="outlined-panel"><div class="card line" data-el="crossrail-card">…</div></div> (a contracted enclosing panel distinct from the open line card)`.



## p17-four-market-panels-4-boundary

원본17 / bbox `[657, 473, 527, 181]`

527×181px independent enclosing rectangle at(657,473), one-pixel pale border. It is additional furniture around the supported card name/note.

The source11/12 line-card design has an open accent rule, not a complete enclosing box. Adding this second outline design by an undocumented part/source condition would violate the one-design-per-variant rule. Text remains supported in the line card; only the extra enclosing rectangle is omitted.

필요한 계약 마크업: `<div class="outlined-panel"><div class="card line" data-el="crossrail-card">…</div></div> (a contracted enclosing panel distinct from the open line card)`.


