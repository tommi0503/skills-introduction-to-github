# Revised submission: integrated visual review

## Scope and review evidence

32 supplied reference images, 113 observed panels. Every individual export is upright and 1280 × 720. Native-layout board exports preserve each reference's actual panel positions, surrounding margins and cropped edges; their dimensions are twice the reference dimensions. The source r31 panels have a different aspect ratio, which is explicitly represented in the data while individual exports retain the requested uniform size.

For this revision, each deck underwent two independent comparison/correction passes (review-1, review-2), followed by the parent's third integrated visual review. The parent inspected all 32 source/implementation board pairs and the individual crops associated with remaining detector findings. Corrections from that third pass were exported again so the delivered images contain the final source. There was no fourth comparison/correction round.

The ZIP includes 32 board comparison images and 113 individual comparison images, plus the three detailed per-deck review records. These images are the evidence; no pixel-equivalence percentage is claimed.

## Concrete repairs

- Replaced cropped-strip stretching with measured full slide rectangles. Restored original collage layout instead of placing every deck into an arbitrary two-column grid.
- Added the missing far-left clipped financial panel in r11: five panels, increasing the submission from 112 to 113 screens.
- Replaced inflated global font multipliers with source-pixel measurements. Corrected serif compression and explicit line breaks in r05; pixel typography and colored heading spans in r12–r15; numeric sizing, captions, rows and connectors throughout.
- Restored actual simple charts, tables, progress bars and diagram connectors. Corrected the shared curve renderer's horizontal tangents, which created visible steps between data samples; neighboring segments now share continuous tangents.
- Corrected the gray plus sign after 190K in r06. Preserved the reference's partial clipping instead of shrinking the visible metric to fit.
- Restored the inset white card and gray surrounding in r26, source coordinates for the clipped r28 panels, and the thin-ring outline and yellow arc in r31.
- Removed speculative prices and generic replacement paragraphs where the supplied small text cannot be read reliably.
- Masked portions lying outside the original image to a flat slide background. No unseen slide content is claimed to be reconstructed.

## Layout detector findings: visual classification

The Range-based detector reports nine text findings in the final export. All were checked visually, rather than treating an automatic count as proof of fidelity:

- r06/s02, two findings: the headline and 190K+ reach the clipped right source edge. The visible source itself cuts them off. The data records explicit clipping reasons.
- r11/s04, one finding: the far-right narrow financial panel contains part of an oversized O. The original viewport cuts off the continuation. The data records this reason.
- r13/s02, two findings: the large 8 and 0 have font selection line boxes extending below the canvas; their rendered ink remains inside it. The paired image shows the complete visible glyphs.
- r14/s01–s02, four findings: SYNTH/STORY/NTH/TORY span the original two-panel boundary. Their intentional edge clipping is recorded explicitly.

## Verification

The accompanying verification.json records the production-browser checks: 32 gallery cards, deck navigation, loading the reference comparison image, Korean screen content, restored five-panel r11 board, 1280 × 720 canvas, and source-data plus shared-renderer hashes matching all final renders. The rendering script waits for fonts and fails on uncaught browser page errors. Packaging checks every slide's dimensions and PNG integrity, every board's dimensions, all 145 comparison files and ZIP integrity. TypeScript and production build pass; Vite reports a bundle-size advisory.

## Remaining differences

Photos, device interfaces, complex illustrations, custom brand symbols and graphic backgrounds use the requested solid light-gray placeholders. White text over those placeholders can have lower contrast than in a dark photograph. Original font files were not supplied: the closest installed typefaces still differ in glyph shapes and spacing. Curves follow sampled source coordinates and remain approximate.

Some 3–4 px source fine print and cropped text cannot be reliably transcribed. Material omissions include the r21 app-planning bullets, r29 business-branch fine print, r30 small price qualifiers/footnotes, and r32 training rationale, program explanations, illustration captions and long quotations. These are listed in the per-deck records and remain visible differences, not claimed matches.

The forbidden slides-clone directory was not inspected. Existing unrelated repository files were not changed.
