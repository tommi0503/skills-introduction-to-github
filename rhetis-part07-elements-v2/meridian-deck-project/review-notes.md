# Meridian Deck v2 review notes

## Scope and provenance

Deck074 has30 source images. The immutable replica files were read, measured and compared, but were not changed in this v2 work. `map-measurements.json` records944 source parts with layout boxes, text ink boxes, original HTML, parent fonts and paint. Inline b/strong, small text and explicit line breaks were also inspected; a parent font alone was not treated as the full type hierarchy. `map.json` groups these parts into336 mapped units including furniture/backgrounds. There is one base provenance per mapped leaf, with `same-as:<page>` and a separate baseRef for reuse.

All56 element CSS files were rewritten. Samples supplied contract metadata and fixture structure/data only; no sample design CSS was copied. The collection uses shared type/weight/line/spacing tokens and palette roles. Original blue/grey values are external style input in `assets/source-palette.css`.

## Specimens and copy

There are195 element fixtures, including all28 golden fixtures and source-shaped `replica-NN` specimens. Source-shaped specimens preserve member counts, meaningful numeric data, text length, emphasis runs and explicit line breaks while using new Korean business language. Proper profile roles were rewritten as plausible people/departments rather than generic filler. The two-character high/low axis values remain semantic direction data; replacing both with the same filler word was corrected.

The latest no-six-character-source-copy instruction took priority over earlier exact-copy text requirements. Four overlapping golden phrases are listed in `fixture-copy-changes.json`. The code identifier division became team_key; the foundation title uses OPERATIONS in place of BUSINESS. Markup and numeric chart data were retained. The audit compares visible text nodes and parent phrases across inline elements, case-folds English and removes whitespace; it includes foundation fixtures.

The original images themselves contain presentation placeholder wording, anonymised names, XX amounts and 20XX dates. These remain source data in reassembled pages. No additional factual business assertions were invented for the original pages. Where the immutable replica had already substituted tiny unreadable copy, that existing interpretation was retained and was not represented as a reliable transcription of the image.

## Review and corrections

The review used element-specific light/dark sheets with every admitted native-grid size, fixture-specific size montages, native cell PNGs and the30 individual original | immutable replica | assembly PNGs. The comparison work had three main passes: initial element extraction; native-box quality correction; final source-text/child-style and composed-box verification. Targeted rerenders followed identified failures.

Material issues corrected in the element rules included:

- True circular radar, scatter/bubble, cycle and timeline geometry; no independent x/y stretching.
- Continuous ascending, descending and flat line/area segments using actual point anchors; distinct stack series and correct running totals.
- Mindmap curves physically touching their owned core/branches, full-height Sankey source connections, and hierarchy forks connecting every owned leaf.
- Donut names inside the ring opening, long-name four-donut minimum8x3, complete seven-row calendars, four-by-two eight-logo layout and non-overlapping calendar cells in tall narrow boxes.
- Label pills with a stable shared-token box, centred text, and adequate vertical padding; compact step icons remaining inside their heading band.
- Square bare foundation seats, portrait/member-specific photo sizing with captions aligned under their own photo, and image-frame plus signs centred in their medallions at every aspect ratio.
- Original source10 long note collisions, source11 narrow legend wrapping, source23 bottom notes outside the element, source26 stack padding squeezing two-line notes, and source28 nested bullet boxes.
- Original68px/56px chapter hierarchy,36px filled-plane headline, source06 grey number/title runs, source04 title/body and portrait caption hierarchy, source23 date/year hierarchy and upper-note reading order.
- SWOT pointed-lobe silhouettes and foreground tip layering in the inferred contract-valid list specimen; default neutral-to-accent step rank; compact before/after changing to a vertical capsule pair by its own received aspect ratio.
- Opening-cover quiet hemisphere furniture and closing-cover accent medallions as explicit foundation device designs.

The minimum annotations were increased where the actual count/length could not honestly fit: four long-name donuts8x3, three metric figures6x2, three full pill labels6x1, source-shaped dense compositions as indicated in their fixture comments. Figures and names were not hidden to claim a smaller minimum.

## Assembly method and visible differences

Assembly uses only collection foundation classes and contractual data-el roots. Inline styles contain grid placement or admitted chart values. There are no per-page CSS blocks, page-id selectors, arbitrary absolute placements or source/fixture/sibling context overrides in the elements. Source bbox placement is translated with one reproducible nearest-cell rule in `assemble.py`; it is not hand-adjusted page by page. Semantic stacks keep the three source06 project rows and source26 legend/notes together.

**The assembly is not a pixel-identical replica.** The comparison PNGs show the following remaining differences, rather than hiding them behind a success claim:

| Pages | Visible difference |
| --- | --- |
|01,30 | Complex world imagery is a plain grey foundation placeholder; Lucide paths differ from image artwork. The closing text band and title register follow shared device tokens. |
|02–03 | Grid quantisation changes agenda row centres and chapter descriptive-copy width/alignment; supporting copy and the grey map placeholder use the shared placement geometry. |
|04 | Portrait width and the four body row positions follow native cells; they do not coincide with all original pixel coordinates. |
|05 | Three circles are cell-sized; their original heavy drop shadows are not reproduced. The addition operators are a documented contract gap. |
|06–10 | Native slots shift photo/card/badge groups and alter some wrapping. Source09 cards start higher/are shorter; source10 copy retains all text with a compact readable measure. |
|11 | Paired-bar plot is explicitly absent as a contract gap; captions, two explanatory panels and legend remain. |
|12 | The four complete prose paragraphs and headings remain as separate semantic elements. The four-lobe SWOT owner is explicitly absent because the contract requires nested list items rather than continuous prose; see the additional contract gap. |
|13 | Two goals and three action panels remain. The shared many-to-many arrow is explicitly absent as a contract gap. |
|14 | The15-observation area plot is explicitly absent as a contract gap; headings and explanation remain. |
|15 | Every branch/leaf is represented as a semantic tree. Forks expose all leaf relations, whereas the source visually points to the action group. Header rail endpoints and circle/leaf sizes follow the reusable element. |
|16–17 | Three full media rows and the comparison table retain their information. Grid quantisation changes row centres and the graph/photo dimensions; small note typography follows the collection. |
|18 | White text over a source photograph becomes readable neutral ink over the plain grey seat. Source18 ruled notes stop at the medallion edge, and its own box controls circle position. |
|19–21 | Financial/comparison table cell widths and some card heights are regularised by the shared component. Source20 independently mapped label and horizontal delta columns do not share all original row centres; its two shared row rules require an additional owner and are explicit gaps. |
|22 | The independent four-category fan is explicitly absent as a contract gap; the leading statement remains. |
|23 | Alternating dates and every note are retained. Reusable circles, note measures and thin connectors differ from original shadows and exact registers. |
|24–27 | Full paragraphs, lists, axis names, values, frames and captions remain. Native cells alter row/photo/card dimensions; simple frames and seats use the contract placement structure; assembly-only temporary indices are empty so photographs remain plain grey. |
|28 | All four stages, both actual count-state captions, repeated capsules, organisation and summary are present. The two spanning phase labels/rail are explicitly absent as a contract gap. |
|29 | Four people, names/roles, explanatory copy and sample-image note remain. Grid proportions alter photo and caption sizes. |

The fifteen genuinely unexpressible owners are the only entries in `GAPS.md`, with measured boxes, reasons and proposed necessary markup. They are not replaced with semantically unrelated elements. In particular, the15-point path is not split between separate owners, and the paired category axis is not simulated with blank labels.

## Checks and interpretation

`tools/audit.py` checks56 folders/CSS files, scoped selectors, tokens, admitted type sizes, map base uniqueness, fixture minima and source-copy overlap. `tools/sheets.py` uses rendererVersion `v2-grid-paint-font-parts-1` and records real font-face declaration/loading, ink clipping/overlap, component/part bounds, chips and paint-based contrast. All source CSS edits are followed by current-fingerprint sheet rerenders. The final actual counts/results are stored in `final-verification.json`; the detailed evidence remains in `sheets/*-checks.json` and `reassembly-checks.json`.

Official light/dark palette contrast is reviewed independently from source reproduction. The external source palette intentionally preserves the original low-contrast small grey text and white footer on photo placeholders, so source-page contrast candidates can remain even when the same elements pass official library palettes. Empty data-icon rings on official library sheets are the reference preview convention; assembled pages load actual Lucide.

## Supplemental integrated contract review
A second read-only contract audit found reference-derived non-golden markup that had survived the first CSS/visual checks. The fixes register each nested pricing/versus/SWOT list and pricing tag as its actual element, convert real list entries to `item/name/note`, remove seven non-golden inline design declarations, register the tag specimen's enclosing prose, and add the required nine-box axis labels. Golden fixture markup and numeric data remain unchanged. The inferred SWOT specimen retains real list members; source12 retains continuous prose separately and records the unsupported SWOT owner as a seventh gap. These structural changes were followed by fresh size-sheet and full-page renders. The two material issues exposed by the new nested render were also corrected: SWOT lobe diameters are capped by the received height, and pricing reserves the same optional-tag row so plan names and prices align. All affected size cells were rendered again and visually reviewed.

The integrated audit keeps20 auxiliary-slot omissions as review candidates rather than invented required content:11 hub spokes without an icon mark, five agenda entries without a note, and four list entries without a note. Their names and primary content are present. The taxonomy has no separate required-part array for these supporting slots, the reference examples omit some, and the user permits child-existence handling. No icon, image or explanatory sentence was fabricated to fill those absent source parts. This interpretation does not waive explicit member limits or the nested-element data-el rule.


## Final source-copy and map-field verification

The30 reassembled pages were independently checked against all529 non-empty text-bearing parts measured from the immutable replica. Every actual assembly text node occurs in that same source page: no new specimen business wording entered an original-page assembly. Paragraphs and nested list sentences were compared after removing only whitespace and drawn bullet markers. The two source13 precise strategic-direction sentences, full source12/16/24 prose, all source17 table wording, source25 nested actions and source29 profile names were retained.

The text-presence check intentionally does not pretend that generic numeral substrings prove chart coverage. Source11 paired bars, source14's15-point chart, source22's fan body and source28's two phase labels are absent owners already recorded in GAPS.md. The source05 two addition operators are also an explicit gap. Source08 numbers01–03 are generated by the numbered-list counter; source15 arrows are drawn by the hierarchy, and source27 plus medallions are drawn as two perpendicular rules by image-frame. These are drawings rather than missing body copy. No new factual sentences were inserted into the assemblies. Fixed grid placement and element copy were unchanged by this final content verification.

All336 top-level map instances now have a measured `design` description. Base18 records name the actual membership, surfaces, connections and type hierarchy. Repeated same-as records retain page references with actual dimensions, count and type differences. Furniture and backgrounds include their measured line/shape/text details. The duplicate page-instance and furniture views carry the same description. The deck-level20-entry `roles` dictionary maps the source palette positions to admitted palette tokens; original color literals remain evidence in sourceMeasurements and the external style provider, not design CSS.

The cover fixture's lower-right grey hemisphere was previously cropped by the page while its placement box extended beyond1280×720. Its visible seat root is now exactly inside the remaining50%×41% page region. A clipped internal pseudo retains the original60%×70% ellipse, curvature and painted crop. The number remains at the center of that original ellipse, as opposed to the center of its clipped visible bounding rectangle. The avatar background variant is excluded by its own class. Both mode-specific foundation renders show the same crop with outsideParts0; this is a real bounded root rather than a waiver of overflowing placements.

The shallow hierarchy's carrier→A/B/C tree was corrected at its owning org root. A continuous horizontal bus terminates exactly at the first/last actual node centers, the parent stem meets it, and each child stem meets its actual node top. No page CSS or assembly placement was added. The same leaf's single-leaf branch incoming edge now stops at the real node border in compact cells instead of crossing its label. Existing multi-leaf forks retain their separate owned branches. All four hierarchy fixtures were rerendered in both modes and reviewed at every admitted size.

The final source freeze includes the bounded cover, hierarchy connections and two directly extracted details: the headline base has no invented underline; the three-spoke hub retains its fine core outline, neutral middle badge and smaller inline caption. The latter caption span was also restored in the source10 assembly and its new-language specimen. The three genuine source06 heading rules are separate unsupported owners in map/GAPS rather than unnamed base decoration. Source24 normalises the drawn leading bullet character to the contractual list marker, preserving every actual sentence with a single marker. Earlier native-grid renders remain historical evidence; the current final outputs carry their own source fingerprints in the generated checks.

The final56-element library contains195 fixtures and2,224 native cells across both official palettes. All cells have current fingerprints, declared/loaded fonts and zero automatic geometry, clipping, overlap, part-bound or paint-contrast failures. Headline's16 fixtures/188 cells and hub's4 fixtures/28 cells were additionally viewed in complete per-fixture native-size montages after the final correction. All30 latest source assemblies were individually reviewed at1280×720; the final targeted changes were inspected again on pages05,10,18 and24. Every assembly was rerendered in a fresh browser context, and all four foundation fixture/mode outputs were regenerated. The source palette intentionally retains its disclosed low-contrast source-copy candidates independently of the official library results.


## Final assembly placeholder data normalisation

The contract demonstration fixtures retain numbered seats, including the source-shaped element specimens. Actual reassembled photographs and graphical backgrounds use empty `data-ph` attributes: the marker is temporary library data, not text in the source image. This removes only generated numbers from the source-page grey placeholders. The required seat attribute, admitted classes, CSS, component geometry and grid placements remain unchanged. All30 assemblies were then rendered again in separate browser contexts and their HTML hashes were refreshed.


## Correction of source25 extraction ownership

The two independent axis names were initially grouped incorrectly into two paragraphs of one prose owner. This was a map extraction defect, rather than a new CSS design or a page-coordinate adjustment. Each actual source node now has its own measured ink/layout box and its own existing prose.quiet root; only their initial slots were recomputed through the unchanged nearest-cell formula. All other source25 roots keep their grid coordinates. The source-shaped fixture also contains two independent prose roots with its unchanged new business wording, rather than a fictitious continuous paragraph. The prose size sheets and all30 assembly reports were regenerated after this correction.


## Final direct-base design correction

The final mapped comparison exposed four mistakes in extraction rather than extra responsive variants. Legend11 had been changed into capsules at large widths, table19 had become a rectangular table at large widths, delta20 had become a vertical capsule pair in tall boxes, and chart-line17 lacked its owned baseline. The four CSS files were rewritten as single bases: vertical 42×8 swatches with10px labels, capsule table cells with plain header text, a horizontal fading-arrow comparison at every size, and connected point geometry with a continuous first-to-last-point baseline. No kit or foundation rule changed.

Source26 keyword captions are now four independent pill roots, not a legend. Their first two neutral shades share the admitted quiet fill role, the third is base neutral and the last is on accent; the remaining source shade difference is disclosed rather than implemented with a forbidden tone class. Source28's actual count states use pill base/on; its vertical triangle is an explicit gap. Source17 and21 keep every original cell value and nested list/trend as a semantic capsule-table fallback. Their rectangular decoration is separately unexpressible, their map no longer says same-as19, and no source-shaped specimen claims that unsupported appearance. Their former new-language stress data remain only in inferred fixtures with different names. Two delta20 inter-row rules also have an explicit absent shared-owner contract.

The map contains336 visible owners with design descriptions,20 palette roles and15 unexpressible owners. Previous unsupported source-shaped/native artifacts were preserved outside the collection while the final cache contains only current fixture/size renders. The final checks and hashes in final-verification.json supersede earlier counts from intermediate snapshots.

The source19 category capsule is160px wide beneath a74px text register and is partly covered by the first150px data capsule. The final table base preserves this measured overlap through an owned category-cell background; it is not a generic round cell drawn only at small widths.


The final count-state composition uses two direct pill children of the existing steps note, just like its other panels. An unnecessary stack wrapper had no assigned height and collapsed both root boxes; removing that wrapper restores valid owned pill boxes without changing CSS, page-grid values or original count text. The matching source-shaped steps fixture now exercises the same two-state composition with new business wording.
