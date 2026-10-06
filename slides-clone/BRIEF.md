# Presentation clone brief

Re-create the presentation slides in `public/reference/NN.jpg` with React + Tailwind v4 + lucide-react.
One reference image = one deck folder `src/decks/dNN/`.

## Hard rules (from the user)
1. Photos, illustrations, 3D renders, device/phone mockups, screenshots, charts drawn as artwork, graphic or
   gradient-art backgrounds, logos and icons lucide can't cover → `ImagePlaceholder` (flat light grey `#e5e7eb`,
   one colour; a darker flat `tone` is OK on dark slides). Keep size/position/radius. Don't draw them.
   Implement as UI: solid backgrounds, text, cards, boxes, pills, lines, tables, simple bar charts/progress bars,
   big numbers, step lists, lucide icons.
2. Visually compare and fix until text, sizes, positions, colours, weights, line breaks match.
3. Reusable / SOLID: content in typed `data.ts`, slide layouts as components, shared pieces in `components/`,
   tokens in `theme.ts`. Slides of the same deck share components.
4. Every slide is exactly `SLIDE` = 1280×720, flat and upright (`<Slide>`), never tilted.

## Reading the references
Some references are a single slide. Many are **boards/collages showing several slides** (sometimes tilted or in
perspective, sometimes partially cut off). For a board: identify each distinct slide, rebuild each one as its own
flat 1280×720 `<Slide>` (un-tilted, complete; plausibly complete parts cut off by the board edge, using the same
design language). Skip a slide only if almost nothing of it is visible. Order slides left→right, top→bottom.
Reference slides that aren't 16:9 → still fit the content into 1280×720 keeping its proportions/layout.
Korean text: use `font-pretendard`. Latin: choose closest (font-inter, font-geist, font-dm, font-manrope,
font-jakarta, font-outfit, font-grotesk, font-archivo, font-playfair, font-times, font-instrument-serif,
font-poppins, font-condensed, font-spacemono, font-bricolage, font-urbanist, font-sora ...; see src/index.css).

## Project
- `src/ui/`: `Slide`, `Abs` (absolute box), `ImagePlaceholder`, `SLIDE`, `cn`. Do NOT edit `src/ui/`.
- `src/decks/dNN/index.tsx` default-exports `DeckDefinition` `{ id: 'NN', title, slides: [SlideA, SlideB, ...] }`
  (array of components each returning a `<Slide>`). Auto-registered.

## Verify loop (keep it efficient: ~2-3 rounds per deck)
```
cd /home/user/skills-introduction-to-github/slides-clone
npx tsc -p . 2>&1 | grep "decks/dNN"
node scripts/screenshot.mjs NN          # -> shots/NN.png (all slides on a 2-column board)
python3 scripts/view.py NN [i]          # -> shots/NN-view.png: reference (left) | rendered board or slide i (right)
```
Read the view image, fix, repeat. Use Pillow crops of the reference to zoom into small text when needed.

## Budget
The user has limited credit. Be efficient: write compact data-driven code, do not over-iterate, no extra tooling.
No git commits, no edits outside your folders, no npm install.
