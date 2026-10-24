# Surface component review

Scope: card, pill, callout, tag, list, quote, headline, prose, metric, delta, legend, agenda, person and logo-group.

The frozen replica HTML supplies the geometry. Source images and logos remain empty neutral seats. New Korean fixtures preserve the structural roles and use original data only in the mandatory examples; they do not reproduce company names or source copy.

## Observed bases

| Element | Source | Box | Status |
|---|---|---|---|
| card | slide_10 | [376.55, 230, 232.56, 422] | Observed independent base |
| pill | slide_10 | [644.11, 546, 192.56, 36] | Observed independent base |
| callout | Not observed | — | Inferred extension |
| tag | slide_08 | [814.59, 232, 279.81, 36] | Observed independent base |
| list | slide_06 | [129, 230, 628, 422] | Observed independent base |
| quote | Not observed | — | Inferred extension |
| headline | Not observed | — | Inferred extension |
| prose | slide_04 | [129, 230, 721, 347.83] | Observed independent base |
| metric | Not observed | — | Inferred extension |
| delta | Not observed | — | Inferred extension |
| legend | slide_11 | [129, 467.5, 1093, 51.16] | Observed independent base |
| agenda | slide_02 | [99, 280, 1086, 372] | Observed independent base |
| person | Not observed | — | Inferred extension |
| logo-group | slide_14 | [675, 230, 547, 422] | Observed independent base |

## Decisions and limits

- Source KPI panels with an actual frame belong to card.fig; bare metric never silently recreates their panel.
- Different source typography is not automatically the same prose. A source caption or heading lacking a meaningful contract variant is recorded as unexpressible, with its measured design and required markup. Compound-owned text is absorbed into the parent component during integration.
- Source imagery and complex illustrations remain placeholders. Empty Lucide icon slots replace image icons or glyph imitations.
- Mandatory card fixtures retain their data except the explicitly required 엔터프라이즈 → 대규모조직 text replacement and ✹ → empty data-icon="sparkles" icon correction.
- Overflow is corrected by size-aware child geometry or an honest fixture minimum; source text is not shortened to pass checks.

## Verification

The official audits/<element>.json files are the authoritative current render record: complete declared slot sizes, light/dark, loaded fonts, DOM overflow and text overlap, hidden figures, background contrast, optical chip alignment, real painted overflow and CSS fingerprints. Source-size crop comparisons are additionally stored in the working exact/ records. No change is made to frozen replica HTML or PNG.

## Final official render

| Element | States | Flags | Fresh | Origin |
|---|---:|---:|---|---|
| card | 100 | 0 | True | Observed |
| pill | 18 | 0 | True | Observed |
| callout | 56 | 0 | True | Inferred |
| tag | 38 | 0 | True | Observed |
| list | 18 | 0 | True | Observed |
| quote | 20 | 0 | True | Inferred |
| headline | 28 | 0 | True | Inferred |
| prose | 18 | 0 | True | Observed |
| metric | 14 | 0 | True | Inferred |
| delta | 36 | 0 | True | Inferred |
| legend | 22 | 0 | True | Observed |
| agenda | 10 | 0 | True | Observed |
| person | 8 | 0 | True | Inferred |
| logo-group | 20 | 0 | True | Observed |
