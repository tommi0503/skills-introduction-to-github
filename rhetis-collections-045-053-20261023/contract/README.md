# Rhetis 디자인 라이브러리 레퍼런스 팩

이미지를 보고 Rhetis 디자인 라이브러리의 **새 컬렉션**(키트 토큰 + 페이지 foundation + 요소 56개)을
HTML + CSS 원본으로 만들기 위한 계약서입니다. 모든 파일은 Rhetis 저장소의 원본에서 생성되었습니다(taxonomy 2026-10-19.4).
이 문서의 규칙을 어기면 Rhetis 반입(intake)이 그 규칙의 이름으로 거절합니다.

## 들어 있는 것

| 경로 | 내용 |
|---|---|
| `contract/taxonomy.json` | 요소 계약(id, category, roots, structure)과 foundation 계약. 아래 표의 원본 |
| `contract/kit-tokens.json` | 키트가 정하는 공유 토큰과 타입 |
| `contract/palette.json` | 라이브러리 색 토큰의 기준 값(라이트·다크). 미리보기가 이 값으로 그립니다 |
| `contract/measure.json`, `contract/type-steps.json` | 출력 형식, 요소가 쓸 수 있는 `--type-N`의 N 목록 |
| `fonts/` | Rhetis가 불러올 수 있는 글꼴 파일 전부와 `fonts.css` |
| `samples/<컬렉션>/` | 실제 라이브러리 컬렉션(annual, confetti, amethyst). **형식과 구성**의 예시이며 디자인은 따라 하지 않습니다 |
| `samples/<컬렉션>/preview-light.html`, `preview-dark.html` | 그 컬렉션의 모든 fixture를 그린 시트 |
| `tools/preview.py` | 내 컬렉션 폴더를 같은 시트로 그리는 도구 (Python 표준 라이브러리만 사용) |

## 돌려줄 것: 컬렉션 폴더 하나를 담은 zip

```
<collection>/                     영문 소문자·숫자·하이픈, 기존 컬렉션(amethyst, annual, aurora, azure, bastion, beacon, bevel, binder, bracket, breeze, cadence, capsule, cascade, chamfer, chisel, civic, cobalt, confetti, contour, crescent, crimson, crop, cursor, doodle, dossier, ember, facet, fairway, fern, flare, flute, fluted, folio, gallery, glacial, graphite, grove, handset, harbor, hearth, helix, keystone, lattice, ledger, lilac, links, lucid, mauve, meadow, miri, monograph, noir, notch, oblique, orchard, paper, persimmon, pilaster, pitch, rally, regent, ribbon, rill, ripple, rivet, ruled, sage, scarlet, signal, skyline, slate, spire, sprig, sprout, stratum, stride, tabbed, tabby, tally, tangerine, trapeze, trellis, verdant, volt, wedge)과 다른 이름
  kit/kit.json                    schema "rhetis.kit/2": id(=<collection>), label, tokens, description, extensions
  kit/css/tokens.css              .slide {…} 과 .slide.dark {…} 에 아래 공유 토큰 전부
  kit/description.md              이 디자인을 말로 (영어, 형태·구성·인상 위주)
  foundation/foundation.css
  foundation/foundation.json      {"schema": "rhetis.design-library-foundation-source/1", "kit": "<collection>", "registrations": {}, "tokenDefaults": {}}
  foundation/description.md
  foundation/fixtures/*.html      seat 1개 이상 (cover 페이지를 하나 더하면 표지 디자인도 시트에서 볼 수 있음)
  elements/<폴더>/element.css      아래 계약 표의 폴더 이름 그대로, 56개 모두
  elements/<폴더>/element.json     {"schema": "rhetis.design-library-element-source/1", "contract": "<계약 id>", "registrations": {}, "tokenDefaults": {}}
  elements/<폴더>/description.md   이 요소가 어떻게 보이는지 (영어 한 단락)
  elements/<폴더>/fixtures/*.html  2개 이상, 아래 '모범 구성'이 있는 요소는 그 fixture 전부
```

`samples/annual/`이 정확히 이 구조입니다(preview 파일만 빼고). 이 다섯 종류의 파일(.css .json .md .html) 말고는 넣지 않습니다.

## 색: 디자인은 색을 갖지 않습니다

색은 사용자의 style이 공급합니다. 디자인은 **어느 색인지가 아니라 어디의 색인지**만 말합니다.

- `--page`, `--ink`: 페이지 바탕과 기본 글자. `kit/css/tokens.css`에는 이 둘만 색으로 적습니다(라이트·다크 모두, 미리보기용).
- `--n-1` … `--n-9`: 무채색 단계. 1은 바탕 쪽, 9는 글자 쪽(다크에서도 같은 뜻이라 다크를 따로 고칠 필요가 없음).
- `--a1` … `--a4`: 순위별 강조색(1이 주 강조). `--aN-on`: 그 강조색 위에 올릴 글자색(page 또는 ink 중 대비가 높은 쪽).
- `--aN-S`, `--aN-S-soft`, `--aN-S-muted`(S = 1…9): 강조색의 깊이 단계와 채도(선명·soft·muted). 옅은 면은 `--a1-2-soft`처럼
  바탕 쪽 단계에 낮은 채도를 씁니다.
- `--good`, `--warn`, `--bad`: 상태 색(의미이지 브랜드가 아님).

규칙: 색 리터럴(`#…`, `rgb()`, `oklch()`, 색 이름)과 위 목록에 없는 색 토큰은 쓰지 않습니다. 진한 강조 채움 위의 글자는
`--aN-on`(그 채움이 `--aN`일 때) 또는 `--a1-7` 같은 깊은 단계 위의 `--page`처럼 **두 모드 모두에서** 대비가 나는 짝으로 씁니다.
시리즈 색은 `--a1`, `--a2` … 순위로 고르고, 강조 하나를 빼면 나머지는 `--n-*`이나 soft 단계로 조용하게 둡니다.

## 글꼴

`--font-display`, `--font-body`에는 아래 이름만 씁니다(`'Pretendard Variable'`처럼 따옴표 포함). 다른 이름은 Rhetis에서 그려지지 않습니다.
`fonts/fonts.css`를 미리보기가 자동으로 불러옵니다.

| family | 굵기 |
|---|---|
| `'Pretendard Variable'` | 100–900 |
| `'NanumMyeongjo'` | 400 |
| `'Nanum Pen'` | 400 |
| `'SUITE'` | 300, 400, 500, 600, 700, 800, 900 |
| `'Freesentation'` | 100, 200, 300, 400, 500, 600, 700, 800, 900 |
| `'ChosunIlboMyungjo'` | 400 |
| `'JoseonGulim'` | 400 |
| `'JoseonPalace'` | 400 |
| `'Noto Sans'` | 100–900 |
| `'Noto Sans KR'` | 100–900 |
| `'Pretendard'` | 400, 700 |
| `'Do Hyeon'` | 400 |
| `'Montserrat'` | 100–900 |
| `'Nanum Gothic Coding'` | 400, 700 |

## CSS 규칙

- **범위**: 요소 CSS의 모든 선택자는 그 요소 안에만 닿습니다. root 클래스에 `[data-el="<collection>-<폴더>"]`를 붙이고, 부품 규칙도
  그 root 아래로 씁니다(예: `.card[data-el="<collection>-card"] .name`, `.parts:is([data-el="…"], [data-el="…"] *)`).
  foundation CSS는 요소의 root 클래스를 건드리지 않습니다.
- **토큰**: 폰트·굵기·행간·자간·radius·간격은 공유 토큰으로만 씁니다. 폰트 이름, `font-weight: 600` 같은 숫자는 쓰지 않습니다.
  1–2px 선, 999px 알약, 장식 도형의 지름 같은 모양 값은 리터럴이어도 됩니다.
- **글자 크기**: 항상 `var(--type-N)`입니다. N은 `contract/type-steps.json`의 값(32px까지 2px 단위, 그 위 4px 단위: 8–128)이고, `font-size: 18px` 같은 px는 쓰지 않습니다.
  요소는 자기 기본 크기를 갖습니다. 역할 크기(`--text-title` 등)는 페이지 작성 에이전트가 고르는 것이므로 요소 CSS에서 쓰지 않습니다.
- **반응형**: 받은 칸 크기에 맞춰 `@container`로 크기·간격·배치 단계를 요소마다 직접 설계합니다. 작은 칸에서는 단계를 내리고,
  정말 좁을 때만 kick → note 순서로 숨기며, fig와 name은 숨기지 않습니다. 글자 크기는 단계로 바꾸고 vw나 clamp로 연속해서 변하게 하지 않습니다.
- **허용 at-rule**: `@container`, `@media`, `@supports`. `@property`가 필요하면 `element.json`의 `registrations`에 규칙 전체를 넣습니다
  (`{"--x": "@property --x { syntax: '<length>'; inherits: true; initial-value: 0px; }"}`).
  `@import`, `url()`, `@font-face`, `@keyframes`, 이미지, 외부 리소스는 쓰지 않습니다. `@container` 규칙은 앞의 `@`을 빠뜨리지 않습니다.
- **요소 전용 변수의 페이지 기본값**: 이름은 `--<collection>-…`로 하고 `tokenDefaults`에 넣습니다. 값에도 색 리터럴은 쓰지 않습니다.

## 마크업과 fixture 규칙

- 클래스와 구조는 아래 계약 표의 structure를 그대로 따르고, 새 클래스 이름을 만들지 않습니다.
- fixture 파일 하나에는 body 자식 하나만 둡니다. root에는 `data-el="<collection>-<폴더>"`를 달고, 최상위에 `style="grid-column:1 / span 12; grid-row:1 / span 6"`을 둡니다.
  첫 줄에는 이 배치가 견디는 최소 칸을 `<!-- min: 6x3 | 3x6 -->`(열x행, 12x6 그리드)로 적습니다.
- 다른 요소를 품는 요소는 품은 요소에도 그 요소의 `data-el`을 답니다(샘플의 pricing, versus 참고).
- 아이콘은 `<span class="icon" data-icon="rocket"></span>`처럼 Lucide 이름(kebab-case)으로 비워 둡니다. Rhetis가 그 칸을 아이콘으로
  100% 채우므로 **칸의 크기를 CSS로 정해야 합니다**. ✓ ✹ ↗ ★ 같은 글자나 `::before { content: "✓" }`로 아이콘을 흉내 내지 않습니다.
- 사진·일러스트 자리는 `<div class="seat" data-ph="1"></div>`입니다. 정사각에 가깝게, 번호는 가운데에 둡니다(가로로만 긴 띠 금지).
- 내용은 실제 같은 한국어 비즈니스 문장으로 씁니다. 변형마다, 멤버 수가 의미 있게 달라질 때마다 fixture를 하나씩 만들고, 긴 이름과 긴 note를 섞습니다.
- 차트 값은 style 숫자로 줍니다. `.bars`·`.lines`에는 `--max`, 각 `.bar`·`.pt`·funnel `.stage`·`.donut`·`.meter`에는 `--v`(funnel·donut·meter는 0–100).
  데이터는 실제 같은 추세로 씁니다. `20 33 46 59 72 20 33 …` 같은 반복 톱니 데이터는 쓰지 않습니다.

## 모범 구성 (리뷰에서 확정)

아래 요소는 이 fixture들을 **같은 마크업과 데이터로** 반드시 포함하고, 내 컬렉션의 CSS로 잘 그려지게 만듭니다. 원본은 표의 샘플에 있습니다.

| 요소 | 원본 | fixture |
|---|---|---|
| `card` | `samples/confetti/elements/card/fixtures/` | `card-2-quiet` `card-3-icon3d` `card-3-line` `card-3-on` `card-4` `card-5-tone` |
| `callout` | `samples/annual/elements/callout/fixtures/` | `callout` `callout-icon` `callout-stack` |
| `chart-area` | `samples/annual/elements/chart-area/fixtures/` | `area-1` `areas-2` `areas-stacked-3` `area-3pt` |
| `chart-bar` | `samples/confetti/elements/chart-bar/fixtures/` | `bars-12` `bars-6` `bars-3` `bars-h-5` `bars-h-8` `bars-2` |
| `chart-donut` | `samples/amethyst/elements/chart-donut/fixtures/` | `donut` `donuts-3` `donuts-4` `donut-0` `donut-100` |
| `chart-line` | `samples/amethyst/elements/chart-line/fixtures/` | `lines-12` `lines-6` `lines-3` `lines-flat` |

## 품질 기준 (리뷰에서 실제로 거절된 것들)

- **잘림·겹침**: 모든 요소가 최소 칸부터 12x6까지, 라이트·다크 모두에서 잘리거나 겹치거나 비좁지 않아야 합니다. 그림자·탭·바깥으로
  튀어나온 원도 칸 안에 있어야 합니다.
- **대비**: 텍스트 대비 4.5 이상(28px 이상은 3 이상). 강조 채움 위의 검은 글자, 중간 톤 위의 흰 글자는 거절됩니다.
- **아이콘 크기**: 원·배지 안의 아이콘은 그 원의 50–60%. 아이콘이 카드 폭을 꽉 채우면 거절됩니다.
- **정렬**: 한 줄에 놓인 카드들은 제목(또는 숫자)이 같은 높이에서 시작합니다. 설명 길이에 따라 제목이 오르내리면 안 됩니다. 그렇다고
  내용을 위에 붙여 큰 칸의 70%를 비워 두지도 않습니다. 정렬과 무게 중심을 함께 맞춥니다.
- **남은 장식**: 원본 이미지의 장식(모서리 사각형, 잎, 별, 따옴표, 라벨)이 내용과 겹치거나 의미 없이 남으면 거절됩니다.
  장식은 디자인 언어로 꼭 필요할 때만, 내용을 피해서 둡니다.
- **차트**: 라벨은 선·점·막대·서로와 겹치지 않습니다. 시리즈 이름은 위 범례나 자기 선 끝(선 아래가 아니라 위)에 두고, 오른쪽에 두면
  플롯이 그만큼 줄어듭니다. 좁은 칸에서 축 라벨은 줄바꿈 대신 솎습니다. 강조(`.on`)는 하나만 분명하게.
- **한 디자인**: 56개 요소와 foundation이 하나의 디자인처럼 보여야 합니다. 선 굵기, 모서리, 강조 방식, 글자 위계가 같아야 합니다.
- **다크 모드**는 반전이 아니라 따로 디자인합니다(색 단계 체계 덕에 대부분 그대로 맞지만 반드시 확인합니다).
- **중복 금지**: 기존 컬렉션과 디자인(형태, 선, 채움, 라벨 처리, 배치)이 비슷하면 쓸모가 없습니다. 데이터가 같은지는 상관없습니다.

## 미리보기

```
python tools/preview.py <collection> contract/type-steps.json --out light.html
python tools/preview.py <collection> contract/type-steps.json --dark --out dark.html
```
색은 `contract/palette.json`의 기준 style로, 글꼴은 `fonts/`로 그립니다. 아이콘 칸은 점선 원으로 보입니다. 미리보기는 검사를 하지 않으며,
검사는 Rhetis로 반입할 때 합니다.

## 공유 토큰 (`contract/kit-tokens.json`)

| 타입 | 토큰 |
|---|---|
| color | `--page` `--ink` |
| font | `--font-display` `--font-body` |
| weight | `--weight-display` `--weight-body` `--title-weight` `--lead-weight` `--figure-weight` `--name-weight` `--body-weight` `--label-weight` |
| tracking | `--tracking-display` `--title-track` `--lead-track` `--figure-track` `--name-track` `--body-track` `--label-track` `--label-track-latin` |
| length | `--radius` `--radius-sm` `--stroke` `--text-min` `--margin-x` `--margin-y` `--gap` `--gap-sm` `--gap-lg` `--pad` `--furn-edge` `--top-h` `--foot-h` `--furn-gap` `--rail-w` `--rail-gap` |
| number | `--title-line` `--lead-line` `--figure-line` `--name-line` `--body-line` `--label-line` |

## 페이지 foundation (`foundation.page@1`)

`<section class="slide [dark]"><div class="page"><header class="head [center]"><p class="kicker">…</p><h1 class="title">…</h1><p class="lead">…</p></header><div class="body">…grid children…</div></div></section>`. `.body` is a 12-column x 6-row grid; each body child states only `style="grid-column:A / span N; grid-row:B / span M"`. `.group` (a row of equal members; `.group.col` `.group.two` `.group.three`), `.stack` (a column), `.split` (two columns, first narrower; `.split.wide-left` reverses) hold several members of one slot. A cover is `class="slide cover"`: no head/body; `.page` holds a `.lockup` (`.kicker` + `.title` + `.lead`) placed with `.at-center` `.at-left` `.at-bottom-left` `.at-top-left`, an optional `.meta` line, and optional `.deco` (the foundation's cover graphic) or `.seat.back`.

- 클래스: `.slide` `.dark` `.cover` `.page` `.head` `.center` `.kicker` `.title` `.lead` `.body` `.group` `.col` `.two` `.three` `.stack` `.split` `.wide-left` `.icon` `.top` `.rail` `.foot` `.idx` `.deck` `.sec` `.src` `.no` `.label` `.on` `.seat` `.avatar` `.portrait` `.logo` `.back` `.lockup` `.at-center` `.at-left` `.at-bottom-left` `.at-top-left` `.meta` `.deco` `.overrides`
- 부품: `seat` — `.seat[data-ph="N"]` — a numbered seat for what the page cannot draw (an image, a 3D model); variants `.seat.avatar` `.seat.portrait` `.seat.logo` `.seat.back` `.seat.icon`. A seat is a placement, not a material.

## 요소 계약 (56개)

| 계약 | 폴더 | root | 구조 |
|---|---|---|---|
| `card.parts@1` | `elements/card/` | `.card` | `.card` > `.parts` — variants `.on` (emphasis: accent fill) `.quiet` `.line` (outlined) `.tone-1…5`. Text parts inside `.parts`: `.kick` (small line above) `.fig` (the figure; `<small>` for its unit) `.name` `.note` `.mark` (icon or number). |
| `pill.parts@1` | `elements/pill/` | `.pill` | `.pill` > `.parts` — a one-line capsule (mark + name + note); variants `.on` `.quiet` `.line`. |
| `callout.sentence@1` | `elements/callout/` | `.callout` | `.callout` — one sentence that concludes the page, written as `<p>문장 <b>핵심 구절</b></p>`, optional `.icon` before it. |
| `tag.inline@1` | `elements/tag/` | `.tag` `.hl` | `.tag` — a small label inside a part; `.hl` — a highlight inside running text. |
| `list.items@1` | `elements/list/` | `.list` | `.list` > `.item` (`.name` + `.note`) — the element draws each item's marker: a dot, a tick on `.list.check`, the item's number on `.list.num`; `.list.divided` rules the items apart. Never write numbers into the items. An item's own `.mark` holds only an icon. |
| `quote.voice@1` | `elements/quote/` | `.quote` | `.quote` > `<blockquote>` + `.by` (`.seat.avatar` + `.name` + `.note`) — variant `.quote.big`. |
| `headline.block@1` | `elements/headline/` | `.headline` | `.headline` > `.kick` (optional small line above) + `<h2>` (the heading; `<b>` on the words that carry it) + `.note` (optional one-line subhead) — a heading set inside the body, apart from the page head; variants `.headline.big` (a statement-size heading that is the page's point), `.headline.center`, `.headline.on` (on the accent ground). |
| `prose.text@1` | `elements/prose/` | `.prose` | `.prose` > `<p>` × 1–4 (running text; `<b>` for emphasis) — body copy set as paragraphs; variants `.prose.lead` (a larger opening paragraph), `.prose.cols` (paragraphs flow into two columns), `.prose.quiet` (secondary text). |
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
| `matrix.quadrants@1` | `elements/matrix/` | `.matrix` | `.matrix` > `.axis-x` (2 labels) `.axis-y` (2 labels) + `.cell` × 4 (`.cell.on`) — a 2×2 — variant `.matrix.swot`: no axes; the four cells are Strengths, Weaknesses, Opportunities, Threats in that order, each with `.kick` (S/W/O/T) + `.name` + `.list`. |
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
| `chart.stack@1` | `elements/chart-stack/` | `.stacks` | `.stacks` `style="--max:N"` > `.sbar` × 2–12 (`<span>` label + `.seg` × 2–5, each `style="--v:N"` with `<b>` value and `.tone-N`; `.sbar.on`) — segments stacked in order; `.stacks.pct` 100% bars (each bar's segments sum to 100, --max unused); `.stacks.h` horizontal. Pair with a `.legend` for the segment names. |
| `chart.waterfall@1` | `elements/chart-waterfall/` | `.waterfall` | `.waterfall` `style="--max:N"` > `.move` × 3–10 (`<b>` value + `<span>` label), each `style="--from:A; --to:B"` (the running total before and after this step) and one of `.up` `.down` `.total` (a total bar stands from 0 to --to) — the element draws floating bars and the connectors between consecutive steps. |
| `chart.area@1` | `elements/chart-area/` | `.areas` | `.areas` `style="--max:N"` > `.series` × 1–4 (`.tone-N`; `.name`) > `.pt` × 3–12 `style="--v:N"` (`<b>` value optional) + `.axis` > `<span>` × the point count (labels) — filled areas over equal steps, drawn by the element the way it draws a line; `.areas.stacked` stacks the series: on it each point's --v is the running total up to and including its series, series listed bottom first. |
| `chart.scatter@1` | `elements/chart-scatter/` | `.scatter` | `.scatter` `style="--xmax:N; --ymax:M"` > `.axis-x` (`<span>` name) + `.axis-y` (`<span>` name) + `.dot` × 3–24 `style="--x:A; --y:B"` (`<span>` label optional; `.dot.on`, `.dot.tone-N`) — points on two value axes from 0; `.scatter.bubble` sizes each dot by its `--r` (0–100). |
| `spark.trend@1` | `elements/sparkline/` | `.spark` | `.spark` `style="--max:N"` > `<span>` × 5–24 each `style="--v:N"` — a mini trend with no axes or labels, set inline beside a figure: nests inside a `.stat` or `.card` `.parts` (after `.fig`) or stands alone in a small cell; `.spark.bars` mini bars; `.spark.up` / `.spark.down` colours the trend as good or bad. |
| `heatmap.grid@1` | `elements/heatmap/` | `.heat` | `.heat` `style="--cols:N"` > `.heads` (`<span>` × N column labels) + `.row` × 2–12 (`.name` + `.cell` × N each `style="--v:N"` 0–100, `<b>` value optional) — density by colour strength; `.heat.calendar` square day cells with no row names (rows are weekdays, `.heads` the weeks). |
| `waffle.units@1` | `elements/waffle/` | `.waffle` | `.waffle` > `.units` > `<span class="u">` × 10–100 (`.u.on` the counted share, `.u.tone-N` a second share) + `.fig` + `.name` — a share as counted units, '10명 중 3명'; `.waffle.figures` draws each unit as a person pictogram. Several stand side by side in a `.group`. |
| `treemap.tiles@1` | `elements/treemap/` | `.treemap` | `.treemap` > `.branch` × 1–5 `style="--v:N"` (its share of the whole, 0–100; `.name`) > `.tile` × 1–8 `style="--v:N"` (its share of the branch, 0–100; `.name` + `.fig`; `.tile.on`) — nested rectangles whose areas follow the shares; with one branch the tiles fill the whole. |
| `sankey.flows@1` | `elements/sankey/` | `.sankey` | `.sankey` > `.source` (`.name` + `.fig`) + `.branch` × 2–6 `style="--v:N"` (share of the source, 0–100; `.name` + `.fig`; `.branch.on` the main path, `.branch.out` a drop-off) — bands as thick as their share flow from the source to each branch; a `.branch` may itself hold `.branch` × 2–4 for a second split. |
| `radar.axes@1` | `elements/radar/` | `.radar` | `.radar` `style="--max:N; --n:K"` (K = 3–8 axes) > `.axis` × K (`.name`) + `.series` × 1–3 (`.tone-N`; `.name`) `style="--v1:A; --v2:B; …; --vK:Z"` — each series a filled polygon over K spokes, first axis at the top, clockwise. |
| `bullet.target@1` | `elements/bullet/` | `.bullet` `.bullets` | `.bullet` `style="--v:N; --target:T"` (0–100; optional `--low:L; --high:H` qualitative bands) > `.name` + `.fig` (+ `.note` for the target) — actual against target and bands in one row; `.bullets` > `.bullet` × n stacks them. |
| `slope.pairs@1` | `elements/slope/` | `.slope` | `.slope` `style="--max:N"` > `.heads` (`<span>` before + `<span>` after) + `.pair` × 2–8 `style="--a:A; --b:B"` (`.name` + `<b class="a">` + `<b class="b">`; `.pair.on`) — each item's change between two moments; `.slope.dumbbell` draws horizontal dumbbells instead of slope lines. |
| `roadmap.lanes@1` | `elements/roadmap/` | `.roadmap` | `.roadmap` `style="--cols:N"` > `.heads` (`<span>` × N periods) + `.lane` × 2–6 (`.name` + `.bar` × 1–4 `style="--from:A; --to:B"` in periods, 0-based start and exclusive end, each `<span>` label, `.bar.on` `.bar.tone-N`; optional `.mile` `style="--at:A"` with `<span>` — a milestone point) — durations on tracks; a timeline marks moments, a roadmap spans periods. |
| `swimlane.flow@1` | `elements/swimlane/` | `.swimlane` | `.swimlane` `style="--cols:N"` > `.lane` × 2–5 `style="grid-row:L"` (`.name` — the owner) + `.node` (`.start` `.ask` `.end`) placed with `style="grid-column:C; grid-row:L"` in its lane and connector classes `to-r to-d to-l to-u` — a flowchart whose rows are owners; connectors and arrowheads drawn by the element. |
| `orbit.nested@1` | `elements/concentric/` | `.orbit` | `.orbit` > `.ring` × 2–4, outermost first (`.name` + `.fig`, `.note` optional; `.ring.on`) — each set contains the next, e.g. TAM ⊃ SAM ⊃ SOM; inclusion, not overlap (that is a venn). |
| `journey.map@1` | `elements/journey/` | `.journey` | `.journey` > `.stage` × 3–7 `style="--mood:M; --next:X"` (0–100, 100 delighted; --next is the following stage's mood, omitted on the last) (`.name` + `.note` the touchpoint + `.pain` optional pain point; `.stage.on`) — stages in a row with the emotion curve drawn across them by the element. |
| `mindmap.branches@1` | `elements/mindmap/` | `.mindmap` | `.mindmap` > `.core` (`.name`) + `.branch` × 2–6 (`.name` + `.leaf` × 0–4; `.branch.on`) — branches radiate left and right of the centre with curved links drawn by the element; freer than a hierarchy. |
| `decision.tree@1` | `elements/decision-tree/` | `.dtree` | `.dtree` > `.q` (`.name` — the question) + `.opts` > `.opt` × 2–3 (`.cond` the answer on the branch + either a nested `.q` + `.opts` or an `.end` outcome with `.name`; `.end.on` the recommended outcome) — at most three questions deep; branches drawn by the element. |
| `balance.scale@1` | `elements/balance/` | `.balance` | `.balance` `style="--tilt:T"` (−100…100, negative = the left pan weighs more) > `.pan` × 2 (`.name` + `.item` × 1–4 each `.name`; `.pan.on`) + `.fulcrum` (`<span>` verdict, optional) — two sides weighed on a beam the element tilts by --tilt. |
| `matrix.nine@1` | `elements/matrix-nine/` | `.grid9` | `.grid9` > `.axis-x` (3 labels, low → high) + `.axis-y` (3 labels, low → high) + `.cell` × 9 row by row from the top (`.name` + `.note`; `.cell.on`, `.cell.tone-N`) — a nine-box such as GE-McKinsey. |
| `positioning.map@1` | `elements/positioning/` | `.posmap` | `.posmap` > `.axis-x` (2 labels: low, high) + `.axis-y` (2 labels: low, high) + `.mark` × 2–12 `style="--x:A; --y:B"` (0–100; `.seat.logo` or `.name`; `.mark.on` ours) — competitors placed on two axes crossing at the centre. |
| `network.graph@1` | `elements/network/` | `.network` | `.network` > `.node` × 3–12 `style="--x:A; --y:B"` (0–100 of the box; `.name`; `.node.on`, `.node.tone-N`) + `.link` × 2–20 `style="--x1:A; --y1:B; --x2:C; --y2:D"` (its two nodes' positions; `.link.strong`) — many-to-many relations; the element draws each link as a line between its points. |
| `code.block@1` | `elements/code/` | `.code` | `.code` > `.name` (optional file name) + `.lines` > `<p>` × 1–24 (one source line each, leading spaces kept; tokens wrapped as `<span class="k">` keyword, `<span class="s">` string, `<span class="c">` comment, `<span class="n">` number) — monospaced source; `.code.numbered` draws line numbers. |
