# Surface component review

Scope: card, pill, callout, tag, list, quote, headline, prose, metric, delta, legend, agenda, person and logo-group.

The frozen replica HTML supplies the geometry. Source images and logos remain empty neutral seats. New Korean fixtures preserve the structural roles and use original data only in the mandatory examples; they do not reproduce company names or source copy.

## Observed bases

| Element | Source | Box | Status |
|---|---|---|---|
| card | slide_14 | [70, 204, 369, 215] | Observed independent base |
| pill | Not observed | — | Inferred extension |
| callout | slide_11 | [70, 567, 1140, 82] | Observed independent base |
| tag | Not observed | — | Inferred extension |
| list | slide_12 | [644, 349, 541, 178] | Observed independent base |
| quote | Not observed | — | Inferred extension |
| headline | slide_05 | [468, 98, 720, 96] | Observed independent base |
| prose | slide_05 | [468, 253, 720, 270] | Observed independent base |
| metric | slide_18 | [110, 286, 220, 34.8] | Observed independent base |
| delta | Not observed | — | Inferred extension |
| legend | slide_10 | [742, 342, 320, 23] | Observed independent base |
| agenda | slide_02 | [588, 57, 635, 607] | Observed independent base |
| person | Not observed | — | Inferred extension |
| logo-group | slide_18 | [403, 270, 473, 199] | Observed independent base |

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
| card | 60 | 0 | True | Observed |
| pill | 24 | 0 | True | Inferred |
| callout | 52 | 0 | True | Observed |
| tag | 40 | 0 | True | Inferred |
| list | 40 | 0 | True | Observed |
| quote | 20 | 0 | True | Inferred |
| headline | 56 | 0 | True | Observed |
| prose | 18 | 0 | True | Observed |
| metric | 30 | 0 | True | Observed |
| delta | 36 | 0 | True | Inferred |
| legend | 32 | 0 | True | Observed |
| agenda | 10 | 0 | True | Observed |
| person | 8 | 0 | True | Inferred |
| logo-group | 20 | 0 | True | Observed |
