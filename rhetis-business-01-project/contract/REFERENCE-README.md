# Rhetis 키트 레퍼런스 팩

이미지를 보고 Rhetis 디자인 라이브러리의 **새 컬렉션**(키트 토큰 + 페이지 foundation + 요소 31개)을
HTML + CSS 원본으로 만들기 위한 자료입니다. 계약 파일은 Rhetis 저장소의 원본에서 생성되었습니다(taxonomy 2026-10-18.1).

## 들어 있는 것

| 경로 | 내용 |
|---|---|
| `contract/taxonomy.json` | 요소 계약(id, category, roots, structure)과 foundation 계약. 아래 표의 원본 |
| `contract/kit-tokens.json` | style이 공급하는 공유 토큰과 타입 |
| `contract/measure.json` | 출력 형식과 글자 크기 단계 |
| `contract/type-steps.json` | 요소가 쓸 수 있는 `--type-N`의 N 목록 |
| `samples/<컬렉션>/` | 완성된 컬렉션 예시 (atlas, miri). **형식** 예시이며 디자인을 따라 하지 않습니다 |
| `samples/<컬렉션>/preview-light.html`, `preview-dark.html` | 예시 컬렉션의 모든 fixture를 그린 시트 |
| `tools/preview.py` | 내 컬렉션 폴더를 같은 시트로 그리는 도구 (Python 표준 라이브러리만 사용) |

## 돌려줄 것: 컬렉션 폴더 하나를 담은 zip

```
<collection>/                     영문 소문자·숫자·하이픈, 기존 컬렉션(atlas, fairway, folio, meadow, miri, pitch)과 다른 이름
  kit/kit.json                    schema "rhetis.kit/2": id(=<collection>), label, tokens, description, extensions
  kit/css/tokens.css              .slide {…} 과 .slide.dark {…} 에 공유 토큰 전부 (색은 두 모드, 나머지는 .slide에만)
  kit/description.md              이 디자인을 말로 (영어, 형태·구성·인상 위주)
  foundation/foundation.css
  foundation/foundation.json      {"schema": "rhetis.design-library-foundation-source/1", "kit": "<collection>", "registrations": {}, "tokenDefaults": {}}
  foundation/description.md
  foundation/fixtures/*.html      seat 1개 이상 (cover 페이지를 하나 더하면 표지 디자인도 시트에서 볼 수 있음)
  elements/<폴더>/element.css      아래 계약 표의 폴더 이름 그대로, 31개 모두
  elements/<폴더>/element.json     {"schema": "rhetis.design-library-element-source/1", "contract": "<계약 id>", "registrations": {}, "tokenDefaults": {}}
  elements/<폴더>/description.md   이 요소가 어떻게 보이는지 (영어 한 단락)
  elements/<폴더>/fixtures/*.html  2개 이상
```

`samples/atlas/`이 정확히 이 구조입니다(preview 파일만 빼고).

## CSS 규칙

- **범위**: 요소 CSS의 모든 선택자는 그 요소 안에만 닿습니다. root 클래스에 `[data-el="<collection>-<폴더>"]`를 붙이고, 부품 규칙도
  그 root 아래로 씁니다(예: `.card[data-el="<collection>-card"] .name`, `.parts:is([data-el="…"], [data-el="…"] *)`).
  foundation CSS는 요소의 root 클래스를 건드리지 않습니다.
- **토큰**: 색·폰트·굵기·행간·자간·radius·간격은 공유 토큰으로만 씁니다. 색 리터럴, 폰트 이름, `font-weight: 600` 같은 숫자는 쓰지 않습니다.
  1–2px 선, 999px 알약, 장식 도형의 지름 같은 모양 값은 리터럴이어도 됩니다.
- **글자 크기**: 항상 `var(--type-N)`입니다. N은 `contract/type-steps.json`의 값(32px까지 2px 단위, 그 위 4px 단위: 8–128)이고, `font-size: 18px` 같은 px는 쓰지 않습니다.
  요소는 자기 기본 크기를 갖습니다. 역할 크기(`--text-title` 등)는 페이지 작성 에이전트가 고르는 것이므로 요소 CSS에서 쓰지 않습니다.
  출력에서는 style의 최소 글자 크기 아래로 내려가지 않게 자동으로 받쳐집니다.
- **반응형**: 받은 칸 크기에 맞춰 `@container`로 크기·간격·배치 단계를 요소마다 직접 설계합니다. 작은 칸에서는 단계를 내리고,
  정말 좁을 때만 kick → note 순서로 숨기며, fig와 name은 숨기지 않습니다. 글자 크기는 단계로 바꾸고 vw나 clamp로 연속해서 변하게 하지 않습니다.
- **허용 at-rule**: `@container`, `@media`, `@supports`. `@property`가 필요하면 `element.json`의 `registrations`에 규칙 전체를 넣습니다
  (`{"--x": "@property --x { syntax: '<length>'; inherits: true; initial-value: 0px; }"}`).
  `@import`, `url()`, `@font-face`, `@keyframes`, 이미지, 외부 리소스는 쓰지 않습니다.
- **요소 전용 변수의 페이지 기본값**: 이름은 `--<collection>-…`로 하고 `tokenDefaults`에 넣습니다.

## 마크업과 fixture 규칙

- 클래스와 구조는 아래 계약 표의 structure를 그대로 따르고, 새 클래스 이름을 만들지 않습니다.
- fixture 파일 하나에는 body 자식 하나만 둡니다. root에는 `data-el="<collection>-<폴더>"`를 달고, 최상위에 `style="grid-column:1 / span 12; grid-row:1 / span 6"`을 둡니다.
  첫 줄에는 이 배치가 견디는 최소 칸을 `<!-- min: 6x3 | 3x6 -->`(열x행, 12x6 그리드)로 적습니다.
- 다른 요소를 품는 요소는 품은 요소에도 그 요소의 `data-el`을 답니다(샘플의 pricing, versus 참고).
- 내용은 실제 같은 한국어 비즈니스 문장으로 씁니다. 변형마다, 멤버 수가 의미 있게 달라질 때마다 fixture를 하나씩 만들고, 긴 이름과 긴 note를 섞습니다.
- 차트 값은 style 숫자로 줍니다. `.bars`·`.lines`에는 `--max`, 각 `.bar`·`.pt`·funnel `.stage`·`.donut`·`.meter`에는 `--v`(funnel·donut·meter는 0–100).

## 품질 기준

- 모든 요소가 최소 칸부터 12x6까지, 라이트·다크 모두에서 잘리거나 겹치거나 비좁지 않아야 합니다.
- 텍스트 대비는 4.5 이상이어야 합니다(28px 이상은 3 이상).
- 다크 모드는 반전이 아니라 따로 디자인합니다.
- 31개 요소와 foundation이 하나의 디자인처럼 보여야 합니다. 선 굵기, 모서리, 강조 방식이 같아야 합니다.

## 미리보기

```
python tools/preview.py <collection> contract/type-steps.json --out light.html
python tools/preview.py <collection> contract/type-steps.json --dark --out dark.html
```
폰트는 브라우저에 설치된 것으로 대체될 수 있습니다. 미리보기는 검사를 하지 않으며, 검사는 Rhetis로 반입할 때 합니다.

## 공유 토큰 (`contract/kit-tokens.json`)

| 타입 | 토큰 |
|---|---|
| color | `--page` `--surface` `--surface-2` `--ink` `--ink-2` `--mute` `--line` `--accent` `--accent-ink` `--accent-soft` `--tone-1` `--tone-1-ink` `--tone-2` `--tone-2-ink` `--tone-3` `--tone-3-ink` `--tone-4` `--tone-4-ink` `--tone-5` `--tone-5-ink` `--good` `--warn` `--bad` |
| font | `--font-display` `--font-body` |
| weight | `--weight-display` `--weight-body` `--title-weight` `--lead-weight` `--figure-weight` `--name-weight` `--body-weight` `--label-weight` |
| tracking | `--tracking-display` `--title-track` `--lead-track` `--figure-track` `--name-track` `--body-track` `--label-track` `--label-track-latin` |
| length | `--radius` `--radius-sm` `--stroke` `--text-min` `--margin-x` `--margin-y` `--gap` `--gap-sm` `--gap-lg` `--pad` `--furn-edge` `--top-h` `--foot-h` `--furn-gap` `--rail-w` `--rail-gap` |
| number | `--title-line` `--lead-line` `--figure-line` `--name-line` `--body-line` `--label-line` |

## 페이지 foundation (`foundation.page@1`)

`<section class="slide [dark]"><div class="page"><header class="head [center]"><p class="kicker">…</p><h1 class="title">…</h1><p class="lead">…</p></header><div class="body">…grid children…</div></div></section>`. `.body` is a 12-column x 6-row grid; each body child states only `style="grid-column:A / span N; grid-row:B / span M"`. `.group` (a row of equal members; `.group.col` `.group.two` `.group.three`), `.stack` (a column), `.split` (two columns, first narrower; `.split.wide-left` reverses) hold several members of one slot. A cover is `class="slide cover"`: no head/body; `.page` holds a `.lockup` (`.kicker` + `.title` + `.lead`) placed with `.at-center` `.at-left` `.at-bottom-left` `.at-top-left`, an optional `.meta` line, and optional `.deco` (the foundation's cover graphic) or `.seat.back`.

- 클래스: `.slide` `.dark` `.cover` `.page` `.head` `.center` `.kicker` `.title` `.lead` `.body` `.group` `.col` `.two` `.three` `.stack` `.split` `.wide-left` `.icon` `.top` `.rail` `.foot` `.idx` `.deck` `.sec` `.src` `.no` `.label` `.on` `.seat` `.avatar` `.portrait` `.logo` `.back` `.lockup` `.at-center` `.at-left` `.at-bottom-left` `.at-top-left` `.meta` `.deco` `.overrides`
- 부품: `seat` — `.seat[data-ph="N"]` — a numbered seat for what the page cannot draw (an image, a 3D model); variants `.seat.avatar` `.seat.portrait` `.seat.logo` `.seat.back` `.seat.icon`. A seat is a placement, not a material.

## 요소 계약 (31개)

| 계약 | 폴더 | root | 구조 |
|---|---|---|---|
| `card.parts@1` | `elements/card/` | `.card` | `.card` > `.parts` — variants `.on` (emphasis: accent fill) `.quiet` `.line` (outlined) `.tone-1…5`. Text parts inside `.parts`: `.kick` (small line above) `.fig` (the figure; `<small>` for its unit) `.name` `.note` `.mark` (icon or number). |
| `pill.parts@1` | `elements/pill/` | `.pill` | `.pill` > `.parts` — a one-line capsule (mark + name + note); variants `.on` `.quiet` `.line`. |
| `callout.sentence@1` | `elements/callout/` | `.callout` | `.callout` — one sentence that concludes the page, written as `<p>문장 <b>핵심 구절</b></p>`, optional `.icon` before it. |
| `tag.inline@1` | `elements/tag/` | `.tag` `.hl` | `.tag` — a small label inside a part; `.hl` — a highlight inside running text. |
| `list.items@1` | `elements/list/` | `.list` | `.list` > `.item` (`.name` + `.note`) — the element draws each item's marker: a dot, a tick on `.list.check`, the item's number on `.list.num`; `.list.divided` rules the items apart. Never write numbers into the items. An item's own `.mark` holds only an icon. |
| `quote.voice@1` | `elements/quote/` | `.quote` | `.quote` > `<blockquote>` + `.by` (`.seat.avatar` + `.name` + `.note`) — variant `.quote.big`. |
| `metric.figure@1` | `elements/metric/` | `.stat` `.stats` | `.stat` > `.parts` (`.fig` + `.name` + `.note`) — a bare figure without a surface; `.stats` > `.stat` × n a row of them with dividers. |
| `delta.change@1` | `elements/delta/` | `.delta` | `.delta` — `<span class="from">12.1억</span><span class="to">15.6억</span>` before → after; the arrow is drawn by the element. |
| `chart.bar@1` | `elements/chart-bar/` | `.bars` | `.bars` `style="--max:N"` > `.bar` `style="--v:N"` (`<b>` value + `<span>` label; `.bar.on`, `.bar.tone-N`) — vertical bars; `.bars.h` horizontal. |
| `chart.line@1` | `elements/chart-line/` | `.lines` | `.lines` `style="--max:N"` > `.pt` `style="--v:N"` (`<b>` + `<span>`) — a line over equal steps, drawn by the element from the points. |
| `chart.donut@1` | `elements/chart-donut/` | `.donut` `.donuts` | `.donut` `style="--v:N"` (0–100) > `.fig` + `.name` — one share of a whole; `.donuts` > `.donut` × n a row of them. |
| `gauge.meter@1` | `elements/gauge/` | `.meter` | `.meter` `style="--v:N"` (0–100) > `.name` + `.fig` — a horizontal progress bar; several stack in a `.stack`. |
| `table.grid@1` | `elements/table/` | `.tablebox` | `.tablebox` > `<table class="table">` with explicit `<thead>`/`<tbody>`; `.pick` on the cells of the column that is the point; `.num` on numeric cells. |
| `legend.keys@1` | `elements/legend/` | `.legend` | `.legend` > `.key.tone-N` — a chart legend. |
| `steps.sequence@1` | `elements/steps/` | `.steps` | `.steps` > `.step` (`.mark` number + `.name` + `.note`) — joined left to right by the element's connector; `.steps.col` downward. |
| `timeline.track@1` | `elements/timeline/` | `.track` | `.track` > `.stop` (`.kick` date + `.name` + `.note`; `.stop.on`) — points on a line; `.track.alt` alternates above/below; `.track.col` runs downward. |
| `cycle.nodes@1` | `elements/cycle/` | `.cycle` | `.cycle` > `.core` + `.node` × 3–6 — members around a centre, arrows drawn by the element. |
| `hub.spokes@1` | `elements/hub/` | `.hub` | `.hub` > `.core` + `.spoke` × 3–6 (`.mark` + `.name` + `.note`) — a centre with members on spokes. |
| `funnel.stages@1` | `elements/funnel/` | `.funnel` | `.funnel` > `.stage` × 3–6 (`.name` + `.fig`), each `style="--v:N"` (0–100) for its width. |
| `pyramid.levels@1` | `elements/pyramid/` | `.pyramid` | `.pyramid` > `.level` × 3–5 (`.name` + `.note`). |
| `matrix.quadrants@1` | `elements/matrix/` | `.matrix` | `.matrix` > `.axis-x` (2 labels) `.axis-y` (2 labels) + `.cell` × 4 (`.cell.on`) — a 2×2. |
| `venn.sets@1` | `elements/venn/` | `.venn` | `.venn` > `.set` × 2–3 (`.name`; `.set.on`) + optional `.core`. |
| `hierarchy.org@1` | `elements/hierarchy/` | `.org` | `.org` > `.root` + `.branch` × 2–4 (`.node` + `.leaf` …) — a tree; connectors drawn by the element. |
| `flowchart.nodes@1` | `elements/flowchart/` | `.flowchart` | `.flowchart` > `.node` (`.start` `.ask` `.end`) placed with `style="grid-column; grid-row"` and connector classes `to-r to-d to-l to-u` — connectors and arrowheads drawn by the element. |
| `architecture.layers@1` | `elements/architecture/` | `.arch` | `.arch` > `.layer` × 2–5 (`.name` + `.chip` …) — stacked architecture layers. |
| `versus.pair@1` | `elements/versus/` | `.versus` | `.versus` > `.side` × 2 (+ `.side.on`) each `.name` + `.list`, with a `<b class="vs">` mark between. |
| `pricing.plans@1` | `elements/pricing/` | `.plan` `.plans` | `.plan` > `.name` + `.price` (`.fig` + `<small>`) + `.list.check` (+ `.tag`; `.plan.on`) — `.plans` > `.plan` × n a row. |
| `person.profile@1` | `elements/person/` | `.person` `.people` | `.person` > `.seat.avatar|.seat.portrait` + `.name` + `.note` (+ `.list`) — `.people` > `.person` × n a row. |
| `logos.row@1` | `elements/logo-group/` | `.logos` | `.logos` > `.seat.logo` × n. |
| `frame.picture@1` | `elements/image-frame/` | `.frame` | `.frame` > `.seat[data-ph]` — the element's picture frame around one seat. |
| `agenda.entries@1` | `elements/agenda/` | `.agenda` | `.agenda` > `.entry` (`.mark` number + `.name` + `.note`; `.entry.on`) — the contents list. |
