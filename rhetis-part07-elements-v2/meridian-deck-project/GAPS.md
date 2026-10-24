# Gaps in the current element contracts

Only genuinely unexpressible reference units are listed. Existing components remain mapped separately.

## Page 05: Addition operators between vision cards
The operators add three peer concepts. No existing contract owns a row of cards and mathematical operators; versus denotes comparison, not addition.

Needed markup/contract: `<div class="sum"> <div class="term">…card…</div> ×3 </div>`; the sum root owns the plus operators.
Bounding box: `{'x': 453.27, 'y': 378, 'w': 370.45, 'h': 55}`.

## Page 11: Paired bars with four shared quarter labels
chart.bar assigns one axis label per bar. This reference has eight values grouped under four shared category labels; representing the paired category axis needs a group part rather than blank labels or inferred sibling pairing.

Needed markup/contract: `<div class="bars grouped"><div class="group"><span class="name">category</span><div class="bar">…</div> ×2</div> ×4</div>`; the group owns one shared axis label.
Bounding box: `{'x': 556, 'y': 318, 'w': 667, 'h': 317}`.

## Page 13: Many-to-many strategy connector
One broad upward arrow relates three lower execution areas to two upper goals. Flowchart directional classes cannot encode this shared many-to-many junction without a connector/junction part.

Needed markup/contract: `<div class="strategy-flow"><div class="goals">…</div><div class="junction"></div><div class="actions">…</div></div>`; one owner connects both sets.
Bounding box: `{'x': 527, 'y': 438, 'w': 225, 'h': 65}`.

## Page 14: Fifteen-observation filled time series
chart.area@1 permits only 3–12 points per series. This chart has 15 observations and 15 labels. Splitting the continuous series between roots would divide ownership of its single connected path.

Needed markup/contract: Keep `.areas > .series > .pt` markup and extend the allowed observation count from12 to15 or24.
Proposed markup: `<div class="areas" style="--max:100"><div class="series"><div class="pt" style="--v:38"></div><!-- 15 real observations --></div><div class="axis"><span>1월</span><!-- 15 labels --></div></div>`.
Bounding box: `{'x': 145, 'y': 339.8, 'w': 973, 'h': 304.9}`.

## Page 22: Four-sector open fan with category badges
The sectors categorise four independent topics. It is neither a cyclic process nor SWOT, shares, inclusion, nor overlap. Current taxonomy has no independent fan-sector/category diagram contract.

Needed markup/contract: `<div class="fan"><div class="sector"><b class="mark">…</b><b class="name">…</b><p class="note">…</p></div> ×4</div>`; sectors have no arrows or cycle semantics.
Bounding box: `{'x': 105, 'y': 294, 'w': 1081.73, 'h': 370}`.

## Page 28: Phase span annotation above a four-step process
The two phase labels span respectively three and one process stages along one connected rail. steps has no phase-span part; roadmap requires multiple duration lanes, which this single process grouping is not.

Needed markup/contract: Add `<div class="phase" style="--from:0;--to:3">…</div>` parts to `.steps`; the steps root owns the continuous phase rail.
Bounding box: `{'x': 83, 'y': 184, 'w': 1115, 'h': 26}`.

## Page 12: SWOT cells with continuous prose
The four captions describe SWOT categories, but their bodies are uninterrupted paragraphs rather than lists. The current `.matrix.swot` structure requires `.cell > .list`, and `list.items@1` requires at least two real items. Breaking physical lines into made-up list members would misrepresent the prose. Treating `.list` as an unregistered private wrapper would evade the nested-element contract.

Needed markup/contract: allow `.matrix.swot > .cell > .prose[data-el="<collection>-prose"]` as an alternative to the existing nested list. The complete SWOT owner can then retain its four lobes, letters, headings and paragraphs.

Unsupported motif bbox: `(418.89, 182.89, 444.22, 445.22)`. All four actual headings and all four full paragraphs remain separately assembled using `headline` and `prose`, with their measured map boxes. The four-lobe owner is explicitly absent; no fake markers or invented list members were added.

## Page 06: Three ruled numbered headings

Each numbered heading owns a separate 618×1px grey bottom rule. The sole directly extracted headline base, source05 VISION, has no bottom rule. The admitted `big`, `center` and `on` variants do not name a ruled numbered heading. Keeping an arbitrary rule on every base headline would invent source05 decoration; assigning a page or fixture condition would evade the component contract. The three original text runs remain assembled as normal headlines; only their three separate thin rules are absent.

Needed markup/contract: explicitly admit a ruled headline variant such as `<div class="headline line" data-el="<collection>-headline"><h2>…</h2></div>`, where the headline owns its bottom rule. `.line` is a proposed extension here, not markup used in the current collection.

Measured rule boxes: `(581,223,618,1)`, `(581,385,618,1)` and `(581,547,618,1)`. Map owners: `p06-17`, `p06-18`, `p06-19`.

## Pages 17 and 21: Rectangular table decoration

The source17 comparison table has rounded header panels and rectangular column surfaces; source21 uses a rectangular grid. The one extracted table base19 consists of individual capsule cells beneath plain header text. `table.grid` has no named visual variant for either second design. A width breakpoint or detecting a nested chart cannot select a different table design.

Needed contract: named `table.panel` and `table.gridlined` appearance variants, keeping the existing semantic thead/tbody/cell and nested data-el structure. These names are proposals only and are not used as current classes.
Proposed markup: `<div class="tablebox panel"><table class="table"><thead>…</thead><tbody>…</tbody></table></div>` or `<div class="tablebox gridlined"><table class="table"><thead>…</thead><tbody>…</tbody></table></div>`.

All original cell wording, numbers, row/column relationships and source17 nested lists/trends remain in an explicitly disclosed semantic table fallback using the capsule base. The rectangular decoration is unexpressible; these pages are not marked same-as19 or verified as source-shaped fixtures. Their previous source-shaped table specimens are kept only as renamed inferred stress tests (`nested-contracts.html`, `budget-grid.html`), with the same new business copy and data.

Measured visual owner boxes: source17 `(103,277,1060,373)` and source21 `(65,195,1153,437)`.

## Page 20: Two shared comparison-row rules

The rules at `(333,411,800,1)` and `(333,536,800,1)` separate three independent before/after comparisons. A delta owns one from/to pair, not its siblings. Reading sibling position to suppress only the last border would violate the ownership rule, while drawing a border on every delta would invent a third rule.

Needed contract: `<div class="comparison-rows"><div class="row"><div class="delta" data-el="<collection>-delta">…</div></div> ×3</div>`. This new owner would draw its two shared rules. Every actual comparison paragraph and its horizontal gradient arrow remains assembled.

## Page 28: Vertical count-transition triangle

The downward gradient triangle between two count capsules is a second visual design compared with the plain horizontal delta base20. `delta.change` has no named vertical/capsule variant. The real 2개소/5개소 states remain as separate semantic pill base/on roots; only the connecting triangle is absent.

Needed contract: an admitted vertical count-transition variant or a transition owner containing both pill states and owning their connector. A tall box alone cannot trigger that unrelated design. The source node and measured box remain recorded in `p28-nested-delta` in map.json.
Proposed markup: `<div class="count-transition col"><div class="pill" data-el="meridian-deck-pill"><div class="parts"><p class="name">2개소</p></div></div><div class="pill on" data-el="meridian-deck-pill"><div class="parts"><p class="name">5개소</p></div></div></div>`; the proposed transition root owns the downward triangle.
