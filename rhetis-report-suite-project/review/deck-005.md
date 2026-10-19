# Deck 005 visual review

- Scope: all 23 original 1280×720 images `slide_08` through `slide_30`.
- Read the reference kit README completely and the shared model contract before implementation.
- Inspected every original individually at full resolution. The deck uses a repeated light-blue screw-mounted header, pale gray double frame, white inset, black hairline rules and slanted fluorescent title highlights. Built with shared editable text/vector primitives and data-driven repeated structures.
- Font inference: Pretendard is used for Korean typography, Inter for the English tab, dates and English numerals. The supplied images do not carry font metadata, so exact source typeface is inferred. Body 20–23 px; main title 48 px; English closing message 108 px. Font widths were compared against the rendered originals and corrected in round 2.
- Photos on slide 08, device screen contents on 24/29, the wooden pedestal material and circular photo magnifications on 29 are flat `#e5e5e5` placeholders according to the user request. The phones' rounded black outlines, side buttons and black notches are editable vector shapes; the pedestal's outer silhouette is a clipped gray seat. Circular magnifications keep their original circular seats and editable dotted annotations. Lucide approximates simple line icons; slide 12 uses directly drawn document/presentation/network vectors. The central Miri mark on 23 uses a simple aperture icon because the original brand mark is not supplied as vector artwork.
- All readable reference text was transcribed. No reference text required invented unreadable labels in this deck. Intentional oddities in source text (`01` repeated on the checklist and fifth quarter on slide 20) are retained.
- Browser render and individual comparison review: completed three rounds, within the requested maximum. Every one of the 23 original/render comparisons was opened individually in rounds 1, 2 and 3, including the final phone-frame changes.

## Changes and remaining differences

- Round 1 → 2: widened headline typography to match source character proportions; tuned the top tab size/spacing; moved two-line side notes down to the source baseline; used equal category centers in the quarterly line chart; redrew slide 12 line icons; corrected the closing highlight slant and quote width.
- Round 2 → 3: preserved the simple phone hardware outlines on slides 24/29 while retaining gray screen placeholders; enlarged the small network member circles. Final renderer outputs were then inspected individually without further slide changes.
- All source text is editable. Chart percentages, timeline labels, calendar dates, table contents, connectors and checkmarks remain vector/text objects. Reference raster images are never used as slide backgrounds.
- Remaining differences are inferred font details, the exact brand glyph on slide 23, and the shape details of Lucide substitutions. Photo and screen omissions are intentional user-requested placeholders.
- Reassembly semantic JSON is supplied on all 23 slides through the `library` property. It contains the primary card, steps, cycle, timeline, agenda, hierarchy, table or line-chart module and its data.

## Final clone verification

- `renders/3/clone/005-slide_08.png` through `005-slide_30.png`: **23 / 23 images, all 1280×720**.
- `review/captures/005-3-clone.json`: **0 findings on every slide**, no browser errors, no failed requests, fonts loaded.
- Every saved PNG SHA-256 matches the corresponding final browser audit. The current exported deck definition also matches the captured definition hash; the last source changes are present in the final renders.

## Reassembly review

- Individually opened all 23 images in `renders/1/assembled/005-*.png`.
- Reported primary-card width collapse on 08/29/30 to the main agent; this was caused by the assembly flex/container layout and the main agent has applied a shared grid-width fix.
- Reported slide 22's first-item root handling and missing fifth hierarchy item; the main agent has changed the assembly renderer to use the first item as root and retain four branches.
- Other round 1 assembled slides had no severe clipping or overlap on individual visual inspection. Main integration review and final assembly capture are owned by the main agent.
