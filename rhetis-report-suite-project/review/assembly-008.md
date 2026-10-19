# Deck 008 — library assembly QA

## Scope
This checks the standardized Rhetis library assembly separately from the original-layout recreation. The clone source stays frozen. The shared assembly code is maintained by the main agent.

## Expected source meaning and library roots
- All 30 pages retain their own title and source business text, reflowed into the shared foundation grid.
- Pages 04 / 21 / 27: table comparison roots must retain A/B company, product percentages, and before/after rows respectively.
- Page 09: metric root must retain all five numeric figures and their currency units.
- Page 18: card root must retain three benefit categories.
- Page 19: venn root must retain 시간 / 비용 / 품질.
- Page 20: steps root must retain 인지 / 탐색 / 구매 / 리뷰 and their notes.
- Page 22: chart-bar root must retain six values 300, 250, 90, 60, 50, 35. The source market-share percentages 20%, 10%, 70% must remain readable in the remaining text.
- Page 23: chart-line root must retain 10, 12, 8, 15 across the four quarters.
- Page 24: hierarchy root must retain 대표이사, four departments and their members. 전무이사 / 상무 remain in the remaining source text.
- Page 28: architecture root must retain 비용 절감 / 효율화 / 최적화 and source formula notes.
- Pages without primary metadata use source text list roots; photo pages additionally use image-frame / seat placeholders.

## Actual rendered inspection
All 30 actual `renders/2/assembled/008-slide_01.png` through `008-slide_30.png` were opened individually. The assembly source was read to check contract roots and source text treatment. The captured deck audit contains 30 pages, all 1280×720, with zero reported text-bound findings, zero missing fonts, zero runtime errors, and zero failed requests. Visual checks found issues not covered by that numeric audit.


| Page(s) | Actual individual visual result |
|---|---|
| 01–03 | Readable text, no severe overlap or clipping. Cover/agenda content is reformatted into the library list grid. |
| 04–08 | Table and all long paragraphs fit. Generic list pages retain text but present source labels and notes in sequential grid chunks, so some original label-to-note adjacency is weaker. No missing prose was identified. |
| 09 | All five metrics and currency units are readable. |
| 10–17 | Message text, paragraphs, repeated notes and rectangular gray image seats fit. No severe clipping or overlap. |
| 18 | Three benefit cards and remaining conclusion label fit. |
| 19 | **Found:** explicit Venn core overlaps and masks the lower part of 비용. The core was unnecessary because its text belongs to the source left panel. Removed the page's `library.core` metadata with main-agent authorization. Confirmed resolved in the final production capture. |
| 20 | All four steps and notes are readable. |
| 21 | All five A/B comparison percentage rows are retained and readable. |
| 22 | **Found:** market-share A/B/other labels and 20% / 10% / 70% disappeared from remaining text because normalization reduced percentages to filtered two-digit strings. Main agent changed the deduplication filter. With explicit authorization, added a secondary chart-donut using the same values and labels. Confirmed resolved in the final production capture. |
| 23 | Four quarterly line values are correct and readable; annotation text fits. |
| 24 | **Found:** short title 상무 was filtered out while 전무이사 remained. Main agent changed the short-text deduplication rule. Confirmed resolved in the final production capture. |
| 25 | All team names/roles/notes remain readable. The four source circular portrait placeholders are not detected by assembly's initial placeholder-only photo selector, so photo seats are absent here; reported to the main agent. |
| 26–27 | All cause/result text and before/after comparison rows fit. |
| 28 | **Found:** five chips squeezed 비용 절감 into a roughly 18 px name column, forcing four vertical syllables. Main agent applied a name minimum width and disabled flex shrinking. Confirmed resolved in the final production capture. |
| 29–30 | Positioning labels/conclusion and all SWOT text remain readable. Generic list presentation loses spatial relations from the original diagram, but source phrases remain present. |

## Source freeze and authorization
The original recreation primitives and coordinates were unchanged during assembly QA. Only two library metadata changes were authorized by the main agent: remove page 19's unnecessary core, and add page 22's source-backed secondary donut. After those changes, `node --check src/decks/deck-008.mjs` passed and the deck was frozen again. Shared assembly/CSS fixes are owned by the main agent.


## Final production capture confirmation
Individually opened the five corrected production PNGs under `renders/final/assembled/`: `008-slide_19.png`, `008-slide_22.png`, `008-slide_24.png`, `008-slide_25.png`, and `008-slide_28.png`.

- **19:** 시간 / 비용 / 품질 are fully visible; no central core masks 비용. The panel heading 공통점과 차이점 remains in the source-text cards below.
- **22:** The six bar values remain correct. Three actual contract donut roots visibly restore 회사 A **20%**, 회사 B **10%**, 기타 **70%** alongside the bars.
- **24:** Both 전무이사 and 상무 are visible beneath the readable organization chart.
- **25:** All four circular gray portrait seats are now visible beneath the retained role/name/note text.
- **28:** 비용 절감 now reads horizontally at a stable name width; all five chips fit without masking the name. The other layer names remain readable.

All issues reported during this assembly QA are resolved in the final production captures. No severe clipping, overlap or unreadable text was found in these five rechecked pages. Source and shared code remained frozen during this final review; only this QA record was updated.
