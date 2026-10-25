# Round 5 — user-authorized contract amendments (2026-10-25)

This file records the user's current instructions. These amendments override conflicting older briefs and the reference README.

## Essential requirements
1. Build each element from replica HTML's actual dimensions, convert dimensions to ratios, then make it responsive with root container-type:size, cqw/cqh, and @container from an honest min through 12x6. Transfer elements, not entire scenes. Rewrite changed CSS files completely; do not append overrides.
2. Arrows, connectors, notches and tabs belong to the element. One connected compound owns all members and their connectors.
3. Fixtures use newly written realistic Korean business text, never replica phrases or companies. Only reassembled verification pages may use original words.
4. Use palette roles only. Font sizes use var(--type-N) or clamp(var(--type-A), calc(...), var(--type-B)). Tokens now cover 8–256px, every 2px below32, every4px from32.
5. Render size sheets per element, one fixture per row, size columns, both themes. Inspect every supported cell and correct visible issues immediately.

## Multiple designs
Keep any number of elements/<leaf>--<design>/ alongside elements/<leaf>/. Design names use lowercase letters, digits and hyphens, no double hyphens. Independent key is <collection>-<leaf>--<design>; data-el and CSS scope use it. Root class and contract ID remain those of <leaf>. English description must explain this particular appearance concretely. A second source design is NOT a gap: create its independent design folder.

## Completeness and fixtures
Collections contain actual source designs only. All56 contracts are no longer required. Remove generic inferred designs not present in the replica, except needed nested dependencies. Shared registry/states.json fixture IDs are optional; if used, markup/data/text must match that state. Unregistered source-derived fixture names may use original shape and fresh Korean text. Keep at least two useful fixtures per design, honest min, varied member counts/long copy.

## Classes and nesting
Element-owned parts and variants are free: .cut .notch .badge .rule .cap etc. Preserve the contract root and the semantics of name/note/fig/mark/kick and values such as --v. Do not reuse another contract's root name for an unrelated local part. Nested elements from the same collection may use their own data-el, establishing a dependency.

## Foundation panels
A title band or surface wrapping other elements belongs to foundation .panel, e.g.
<div class="panel" data-slot="..." style="grid-column:...;grid-row:...">
 <div class="bar"><span class="kick">Input</span><b class="name">현황 분석</b></div>
 ...one element or group/stack/split...
</div>
Foundation owns .panel/.bar appearance and its own variants (.on .line .tip-r etc.), responsively. Parent agent owns foundations; element owners propose map.panels entries with page, bbox, classes, bar, children IDs and source geometry.

## Chart extensions
- chart.donut: .donut.pie > .slice ×2–6. Each slice has --v:N (sum100), .name, b value, optional .slice.on. Central .fig optional. Multi-slice doughnuts and pies belong here.
- chart.bar: .bars.grouped > .group ×2–8. Each group has span label and .bar ×2–4 with --v and .tone-N. Combo charts add .line > .pt ×n with --v inside .bars.
- chart.line: .lines > .series ×1–4 (.tone-N, .name) > .pt.
- Any chart point/bar/slice may contain .at short annotation. Annotation badges, bubbles and curved arrows are drawn by element CSS. Element derives y ticks from --max.
- positioning.map: .mark accepts --r 0–100 for size and .note 2–3 lines. One axis label means the axis name.

## Seats and shapes
Foundation draws seat.wide (long photograph strip), .tall (portrait crop), .device (device screen), .round (circle). Freely draw cut corners, droplets, pentagons, leaf tabs with clip-path/masks/radii/gradients. Shared shape values may use collection-prefixed tokenDefaults or kit extension tokens.

## Strict gap policy
Map from top to bottom: find meaningful element instances on each replica page FIRST. Do not fit DOM nodes to contracts and call the remainder gaps. Type styles, captions, labels, measurement dumps (font=...;size=...), and text fragments are NEVER gaps. They belong to an owner element or page furniture. Whole-page bands/slants/large shapes are background vectors, not gaps. Any genuine gap must state a concrete reason that remains after all extensions above, e.g. 9 members above a contract maximum of6. Group repeated instances of the same unresolved design in one gap entry.

## Workflow and reporting
Reclassify old gaps; implement additional independent designs, panels, expanded charts, typography/seats; remove generic filler; reassemble source pages and compare. Report per collection: new folders ← source pages; panel use; chart extensions; deleted generic folders; remaining gaps with concrete reasons; actual sheets and comparisons inspected after final edits.

No git commands. No nested subagents. User reports in Korean. Preserve all replica files. Existing prior work stays intact; Round5 is built in its own folder.
