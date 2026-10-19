# Deck 009 — 2056 미리시 주요 성과 보고

## Reference inspection

All eight original 1280×720 PNGs were opened individually at full resolution before implementation: `slide_01` through `slide_08`. The kit README and shared presentation model were read in full. The repeated language is a white canvas, black 1 px outlines with small corner radii, lime and cobalt highlights, cool gray surfaces, heavy Korean sans titles, and fine outline icons.

The dominant non-antialiased palette was sampled from all eight originals: lime `#d8ff27`, blue `#2c4ffe`, cool surface `#f2f4f5`, and outer canvas `#f0f0f0`.

## Interpretation decisions

- The original sans font is not named in the supplied raster. Individual browser comparisons showed Pretendard Korean titles were approximately 5% narrower than the source; Noto Sans KR is the closer loaded family and is used at explicit 400, 600, and 700 weights. Titles, figures, line spacing, and explicit line breaks are set independently in native 1280×720 coordinates.
- Person illustrations on pages 1, 2, 4, and 8 are flat light gray placeholders as requested. Their enclosing simple lime panels are retained. No original bitmap is placed inside a result slide.
- The handshake mark and outline business pictograms use Lucide equivalents; the custom banknote with won symbol, ladder, petal diagram, and curved growth arrow are live primitive geometry.
- All visible Korean business copy was readable. The presentation year, figures, labels, and footer dates are transcribed rather than invented. The no-space text `전년比` is retained.
- The first two pages use a slim footer strip, while pages 3–8 share the framed header and framed body arrangement. The eight-page set is preserved rather than adding inferred later chapters.

## Known differences

- Detailed person artwork is intentionally replaced with placeholders; this is the largest visible difference on pages 1 and 2.
- Lucide outlines differ modestly from the original custom icons and logo. Typography is a reasoned font match, not a claim that the font was identified from metadata.

## Browser rounds

Round 1: all eight full-size original PNGs and every individual 2560×760 side-by-side comparison were inspected. The card, header, footer, and chart geometry match closely. Fixes identified: use Noto Sans KR to better match Korean glyph widths; reduce the cover year and investment figure; keep the investment caption above its illustration placeholder; correct two large text box heights. A shared Lucide renderer defect was reported to the integrator and fixed before round 2: explicit width, height, color, and line width now reach the SVG instead of the library's 24 px defaults.

Round 2: all eight comparisons were opened individually. Noto closely matched the main mixed-language heading widths. Four Korean-only headings were still wider than the references and were sized independently using measured black-pixel bounding boxes. The header brand wrapped after the font change; its size and available box were corrected. Economic figure baselines, chapter label widths, and investment caption layering were adjusted. The source monitor and building icons were reconstructed as simple outline SVG paths.

Round 3: all eight individual comparisons were opened and inspected. All eight canvases are 1280×720, no rendered text overflow is reported, and no JavaScript or failed network requests are reported. Capture definition SHA-256 `1b1f62741d071ca3394d4b0dab4d04f0e742517e5af5b9539951132fa75bd56f` matched the model before the final explicit font selection below. The deliberate illustration placeholders and modest custom-icon/font differences remain as documented. Numbered circles and framed headers were individually checked for visible alignment.

The Noto 600 Latin-only text faces returned false in the font availability check, so the English annual-report line and blue chapter numbers were explicitly assigned loaded Pretendard 600. The integration final capture must include this final font-only repair. The clone underwent exactly three full individual visual comparison rounds; an interrupted second-round capture was discarded after unrelated hot reload navigation destroyed its browser context.

## Reassembly data

All eight slides include original-content semantic `library` data using card, agenda, metric, or steps collections. The data contains the supplied copy, figures, and footnotes for genuine contract-element reassembly by the shared adapter.
