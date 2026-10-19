# Deck 061 visual review

- Scope: both originals, slides 01–02. Each original inspected individually before implementation.
- Implementation: editable text and centered chips, repeated agenda groups, dotted leaders, authored simple SVG brand mark. Pale background, light blue emphasis and deep blue titles reproduce the source hierarchy.
- Deliberate differences: the complex 3D chart/background on slide 01 and folder/background on slide 02 are light-gray placeholders as requested. The cover placeholder preserves the visual illustration area while leaving the title readable. The small geometric brand mark is redrawn as simple SVG. Exact source font was not supplied; locally loaded Pretendard is used.
- Readability: all main source copy was readable and transcribed. No illegible text was replaced with lines or invented content.

## Review passes

1. Both pages rendered in actual Chromium and compared individually with originals. Corrected title width/height by increasing cover text from 78 to 84 px, adjusting tracking, and raising the contents title.
2. Both pages rendered again and each original/result comparison inspected individually. Confirmed final changes in screenshots. Checked cover title line breaks, copy, chip visual centering, agenda number tiles, group spacing, dotted leaders, page numbers and placeholder edges.

| Slide | Final outcome |
|---|---|
| 01 | Two-color title, logo, explanatory copy and pill position matched closely. Complex 3D imagery deliberately replaced by gray placeholder. |
| 02 | Three white agenda cards, blue centered numeric tiles, two items per section and 0P labels checked. Complex lower-left illustration/background deliberately replaced. |

`review/audit-061-replica.json`: 2/2 pages exactly 1280×720; Pretendard 400/700 loaded; 0 outside-page, width-overflow or height-overflow findings. Final PNGs: `renders/replica/061/`. Individual visual comparisons: `comparisons/061/01.jpg`, `02.jpg`.
