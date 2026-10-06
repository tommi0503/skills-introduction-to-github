# slice-clone2 brief

Re-create every slide in `public/reference/NN/SS.webp` (34 decks, 459 slides, all 1280×720) with
React + Tailwind v4 + lucide-react. One deck = one folder `src/decks/dNN/`. **`src/decks/d01/` is the worked example
— read it first and follow its structure.**

## Hard rules (from the user)
1. Photos, illustrations, characters, 3D, mockups, maps, logos, textures, graphic/gradient/organic-blob backgrounds,
   hand-drawn doodles and icons lucide can't cover → `ImagePlaceholder` (flat light grey `#e5e7eb`, one colour; a darker
   flat `tone` only where needed for legibility on dark areas). Keep size/position/radius. Don't draw them.
   DO implement as UI: solid backgrounds/panels, text, cards, boxes, pills, lines, frames, tables, simple bar/pie
   charts, progress bars, big numbers, step lists, simple geometric shapes (circles, rectangles), lucide icons.
2. Compare against the reference and fix until text (exact wording, line breaks), positions, sizes, colours and weights
   match. No text overflow / clipping / overlap: run `node scripts/audit.mjs NN` (must report 0, or only overlaps
   that also exist in the reference).
3. Reusable / SOLID: content in typed `data.ts`, tokens (colours, fonts, frame metrics) in `theme.ts`, shared slide
   pieces in `components.tsx`, slides in `index.tsx`. Slides of the same deck share components (header, page
   number, frame, card...). Prefer `.map` over copy-paste. Shared primitives come from `src/ui` (`Slide`, `Abs`,
   `ImagePlaceholder`, `cn`). Do NOT edit `src/ui/`, `src/index.css`, scripts, or other decks.
4. Every slide is a `<Slide>` (exactly 1280×720, flat, upright). Never rotate.

## Fonts (Tailwind `font-<token>`)
Korean sans: `pretendard` (default for clean Korean), `notosans`, `gothica1`, `nanumgothic`, `plexkr`, `sunflower`,
`orbit`. Korean serif: `notoserif`, `myeongjo`, `batang`. Korean display: `blackhan`, `jua`, `dohyeon`, `bagel`,
`gugi`, `dongle`. Korean hand-written: `himelody`, `gaegu`, `pen`, `brush`, `gamja`, `poorstory`, `singleday`,
`yeonsung`, `cute`, `dokdo`, `gowun`. Latin: `inter`, `montserrat`, `poppins`, `oswald`, `bebas`, `anton`,
`archivoblack`, `cormorant`, `playfair`, `times`, `dm`, `manrope`, `outfit`, `jakarta`, `grotesk`, `archivo`, `geist`,
`condensed`, `greatvibes`, `dancing`, `instrument-serif`, `urbanist`, `sora`, `lexend`, ... (see `src/index.css`).
Pick the closest; tune size / weight / `tracking-[..]` to match glyph widths and line breaks.

## Project
- `src/decks/dNN/index.tsx` default-exports `DeckDefinition` `{ id: 'NN', title, slides: [S1, S2, ...] }` with one
  component per reference slide, in order. Auto-registered. `title` = `public/reference/NN/meta.json` title.

## Verify loop (efficient: 1–2 fix rounds per slide group)
```
cd /home/user/skills-introduction-to-github/slice-clone2
python3 scripts/ref.py NN 1 2 3        # -> shots/NN-ref.png  reference slides stacked (full res) — read to measure
npx tsc -p . 2>&1 | grep "decks/dNN"
node scripts/screenshot.mjs NN         # -> shots/NN/SS.png per slide
python3 scripts/view.py NN 1 2         # -> shots/NN-view.png reference (top) vs render (bottom), full res
python3 scripts/view.py NN --half      # all slides, half size, ref above render, 2 per row (overview)
node scripts/audit.mjs NN              # overflow / clip / overlap check
```
Read images with the Read tool. Use Pillow crops of the reference to zoom into small text when needed.
Decks from the same template family (similar look) should share a design language — reuse your own components.

## Budget
The user has limited credit. Be efficient: view 2–4 reference slides per image, write compact data-driven code,
don't over-iterate, no extra tooling, no npm install, no git commands.
