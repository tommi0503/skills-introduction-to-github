# Deck 008 — Sage Business Presentation

## Source scope and design reading
- All 30 original 1280×720 PNGs were opened individually at native resolution before implementation, slides 01–30.
- The reference kit README was read in full. Its library contract is distinguished from the user's broader recreation, rendering, and submission requirements.
- Design: 40 px sage frame, square white sheet, 1146 px content width; restrained #7f8d8a headings, #9baca9 frame, #acbdb9 emphasis, #e3e8e7 and #f1f3f2 panels, charcoal text; straight thin dividers and square corners.
- Fonts inferred from image shapes: Pretendard Korean/body, Inter Latin titles/numerals. Original font metadata is unavailable, so the inference is recorded rather than asserted as exact.
- Shared helpers produce page headers, sections, list markers, panels, placeholders, and data-driven chart segments. Every page is composed of editable text, geometric primitives, and Lucide icon data; no original raster is embedded.

## Deliberate substitutions and interpretation
- The plant photo background on slide 10 is a flat light gray placeholder. Its original white text is darkened for readable contrast on that required placeholder.
- All cosmetic photographs on slides 12–17 and circular portrait photos on slide 25 are flat light gray placeholders with the same bounds.
- The small MIRI logo mark is represented by a simple circle and vertical stripe construction. No raster logo is reused.
- Lucide equivalents replace the original simple icon drawings. Stroke and sizes are matched approximately to the source.
- The three interlocking Venn lobes on slide 19 and semicircular layered benefit diagram on slide 18 are native SVG geometry; exact source control points are unavailable.
- Original instructional placeholder prose is recreated as content; it does not modify the task's instructions. No unreadable text was represented as strokes.

## Individual review records
Completed: all 30 original images, all 30 round 1 comparisons, and all 30 round 2 comparisons were individually opened. Two visual refinement rounds were used.

## Round 1: all 30 individual comparisons opened
The complete `comparisons/1/clone/008-slide_01.jpg` through `008-slide_30.jpg` were opened individually. The first rendering attempt was interrupted by Vite navigation while another deck was edited; it was repeated in the same round after hot reload was disabled. No source changes were made between those attempts.

| Slides | Findings and changes for round 2 |
|---|---|
| 01–03 | Main English titles were too narrow and 7–10 px high; increased weight/tracking and shifted the title blocks. Cover Korean pretitle enlarged. Section numeral repositioned. |
| 04–30 | Shared Korean titles and lead text were slightly small; 44 px title / 20 px lead selected. Header geometry, panel colors and dividers remained aligned. |
| 05, 07, 20, 26, 28 | Source directional arrows have a fade; replaced flat triangles with clipped CSS gradient geometry. |
| 06–08, 11–17, 19–20, 23, 26, 28, 30 | Original Korean wraps inside words; enabled break-all and adjusted body text to 18 px so text density follows the original. Five-forces items now state explicit source line breaks. |
| 09 | Numeric figures and Korean currency units had equal sizes; split them into 54 px figures / 34 px units with a shared baseline. |
| 10 | Message enlarged to 40 px. Required gray background substitution and readable dark message remain a documented difference. |
| 18–19 | Semicircular layers and interlocking SVG Venn regions were reviewed against source shape bounds; no raster source used. |
| 21–22 | Bar coordinates, values, ring proportions, leader lines and chart labels were checked individually against originals. |
| 23 | Area fill was too flat; replaced with a clipped vertical gradient, preserving the exact four data values. |
| 24–25 | Organization connectors/card bounds and portrait placeholder circles were inspected. Icon outlines and missing photographs remain deliberate differences. |
| 27 | Comparison table cell alignment and divider positions were retained after individual review. |
| 29 | Positioning axes and source point placement retained; no extra data invented. |
| 30 | Lower-right bullets wrapped and overlapped; expanded the text slot leftward to its source x-coordinate and applied Korean character wrapping. |

Source-backed library assembly metadata was added to 11 key data/diagram pages: 04, 09, 18–24, 27–28. Source text remains in the primitive model for content preservation.


## Round 2: final individual review and automatic validation
- Opened every individual side-by-side image `comparisons/2/clone/008-slide_01.jpg` through `008-slide_30.jpg`; no contact-sheet-only review was used.
- The round 1 text overlap on slide 30 is resolved. Paragraph bounds on 13/16/23, figure/unit hierarchy on 09, and page-title/cover-title corrections are visible in the actual round 2 captures.
- Automatic browser audit: **30 slides, zero findings, zero missing fonts, zero failed requests, zero page errors**, all canvases **1280×720**, no embedded original rasters.
- All 30 PNG SHA-256 hashes match their capture audit records. Deck definition hash was checked against the final source so the inspected renders correspond to the last source changes.
- Round 2 is the final accepted recreation render. A third visual round was not needed.

## Remaining visible differences
Photographs and profile imagery are intentionally flat light gray. The slide 10 message is dark for contrast on its required gray placeholder. Font identification was inferred, so small glyph-width/kerning and line-break differences remain. Lucide icon geometry, the simplified MIRI logo and source Venn curve control points are approximations. No unreadable prose is represented by false glyph strokes; all visible content is actual editable text.
