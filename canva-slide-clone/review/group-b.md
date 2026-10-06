# Canva c07–c11 visual review

Owned 62 slides: c07 10, c08 14, c09 11, c10 11, c11 16. Every original 1600×900 image was opened individually before implementation. Every individual original/render comparison was opened in review-1 and review-2 (124 comparisons total); source contacts were only navigation aids. Exactly two own render/comparison passes per deck. Root final synchronized capture is the third reserved pass. No source JPEG is embedded in the slide output; complex backgrounds, photographs and custom illustrations use #e5e5e5 placeholders.

## c07 — 10 slides

First-pass defects: headline weights were missing because the initial static Korean face only exposed weight400; paragraphs wrapped too widely (s04 7 instead of6 lines, s05 4 instead of3), s09 caption wrapped with a dangling final syllable, and the gray cover parallelograms used an incorrectly shallow slope. Changed body face to Pretendard after inspecting glyph appearance and widths; review-2 paragraphs closely matched source line density and restored weights. Measured gray native cover bands now slope112 pixels over193 pixels height, rather than31 pixels. Restored readable history label '[회사명]이(가)'. Review-2 led to selecting Noto Sans KR for the visibly taller/wider large source headings while retaining Pretendard body. Rebuilt s09 blue corner with source elbow x1475/y545 and bottom start1184; corrected s10 gray band x360–640. Two source chart panels remain real grid/line/bar primitives with readable axes and captions.

Limits: decorative dotted image-background patterns are not reproduced; source blue photographic/gradient areas are flattened. Building silhouette cutouts are polygon placeholders, so their photo-specific skyline outline is simplified. Source fine typography can still differ by a few pixels.

## c08 — 14 slides

First-pass defects: missing heavy/thin font weights; subtitle position calculated from a generic text-length multiplier put captions too far right; c09 smooth-chart data points started50 pixels inside a grid requiring127. Table detail text in s06 and captions in s05/s09 wrapped excessively. Replaced subtitle anchors with measured native x530/552/538/641/475/593/602/608/534/649/478 by title. Chart now uses127px inset,3px source stroke and7px source markers. Shared centered chips retain actual-painted-glyph centering. Corrected dark-circle budget check to yellow so it is visible. Review-2 showed table text/4-line chart caption fit and no renderer range/centering findings. Large source headings/cover use Noto, bodies remain Pretendard.

Limits: three illustrative icons use nearest Lucide equivalents, which differ in internal artwork from source. Complex Q&A/folder and contents illustrations are gray rectangles in source bounds. Some budget header checks remain black rather than source violet; blue/yellow graphic colors and fonts are close approximations.

## c09 — 11 slides

First-pass defects: overview and shared top text wrapped to 4/5 lines instead of3/4; narrow white lower body columns in s06 extended too low; competitive chip text overlapped arrows; vertical cover email had wrong size/origin. Email is now native23px rotated -90 at x1511/y356. Competitive label gets its own215px centered region, leaving arrow x845 separate. Photo step card explicit breaks use nowrap to prevent extra lines. Lower columns19→18px, implementation paragraphs20→19px with measured27px leading. Review-2 body face correction made shared top text too small; restored native29px and1.45 leading as a late fix. Contact27px/1.24 leading matches source spacing more closely. Financial graphic remains grouped primitive bars; last gray series peaks were corrected20→19 to match source top.

Limits: DM Sans is an approximation of source English lettering (proposal cover second line and section titles have small width differences). Gray photographic backgrounds make source white overlaid text low contrast, intentionally following the placeholder rule. Bar values were visually inferred from the source, which has no printed individual values. Rounded image cards retain text overlays and original white text.

## c10 — 11 slides

First-pass defects: strategy bullets overflowed the four cards; market card copy had an extra line; small statistic descriptions cropped at bottom; large paragraph s03 had8/9 lines instead of7. Pretendard restored compact readable body text. Strategy19px/1.6 leading and tracking-.5 now fits source7-ish lines; market21→19px, s03 body28→26px/1.5, statistic fine print19→18→17px targeted to printed source size. Native card dimensions, rules, outlined circle labels, comparison columns and future-plan row controls are preserved. Review-2 had one s03 width warning; the late targeted26px correction addresses it.

Capture note: review-2 pair s05/s06/s08 appeared to omit leading0 while data and raw render contain '02./03./05.'. Root checked raw c10-s05 and confirmed it is intact; root strengthened capture synchronization by exact deck/slide IDs for final export. The source-header check was corrected by the parent in the reserved third pass: s10 DOES contain its template header, and head10 is present in the final source.

Limits: source gradient graphic backgrounds become gray rectangles, not reproduced gradients. Lucide icon internals are approximate. English DM Sans headings and Roboto Condensed labels differ slightly from source glyphs.

## c11 — 16 slides

First-pass defects: all large headings/keyword labels were regular; long two-column body overflowed; album descriptions took4 lines rather than source2; subtitle overlap after shorter heading widths; line graph strokes/dots too thin. Pretendard body matches density significantly better. Album now native24px, explicit breaks+nowrap. Header subtitles use source Korean-character width56px (spaces excluded). Large headings choose Noto Sans KR700, cover thin200/heavy900; source tiny title checks restored with Lucide. Graph now59px inset,4px source strokes and8px markers. Shared card/chip widths and centers unchanged. Source inline bold phrases in s02/s07 restored via text runs. s05 lower description width688→699 and height170 prevents width warning.

Limits: exact source fonts are unknown; selected face by visible glyph width/height. Long text still differs in individual line break positions. Lucide replacements for source hand/lightbulb/chart/screen icons preserve bounds and stroke color but not internal illustrated details. Review-2 remaining s05 width warning is addressed by the late width adjustment; parent final must verify. Timeline top heading/body were moved15 native pixels up after review-2; lower-body line density still differs slightly.

## Validation

TypeScript noEmit passes after all late edits. Review-2 renderer reported c07=0,c08=0,c09=1,c10=1,c11=1 findings; those three paragraph cases were subsequently corrected. No claim of pixel-perfect equivalence. No additional own render round has been run after late fixes; root final validates the frozen latest data.

Parent third-pass correction: direct inspection of public/reference/c10/s10.jpg confirms the original DOES include the 05. 성과 분석 title, company name and top rule. The removed shared header was restored. The earlier no-header observation was incorrect. Leading zeros are also present in source and raw render. Final synchronized capture is authoritative.
