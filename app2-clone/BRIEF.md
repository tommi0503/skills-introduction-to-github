# App2 implementation brief

Goal: re-create the app screens in `public/reference/NN.jpg` (recordings of real iOS apps, several phones side by side)
with React + Tailwind v4 + lucide-react, as faithfully as possible. One reference image = one folder `src/apps/aNN/`.

## Hard rules (from the user)
1. **Photos, map tiles, satellite/globe imagery, illustrations, 3D art, mascots, product shots, avatars, logos/brand
   marks, graphic/blurred/gradient-photo backgrounds and icons lucide can't cover → `ImagePlaceholder`** (flat light grey
   `#e5e7eb`, one colour). Keep the area's size/position/shape (radius, circle, clip-path). Don't draw them.
   On dark screens or under white text you may pass a different flat `tone` for legibility (still a single flat colour).
   Plain UI must be implemented: backgrounds, cards, lists, buttons, chips, tabs, inputs, toggles, tables, charts made
   of simple bars/lines (SVG paths are fine for line/area charts), keyboards, text and lucide icons.
2. **Visually verify** repeatedly (screenshot → compare → fix) until text, sizes, positions, colours, weights,
   line breaks and spacing match.
3. **Reusable, SOLID, no hard-coding**: content in typed `data.ts`, mapped over; screens composed from components;
   style via props / className injection; one responsibility per component; share components between screens of
   the same app.
4. **Every screen is exactly the same size** — `SCREEN` = 390×844 (logical iOS points, radius 44) from
   `src/ui/board/geometry.ts`. Screens are upright (never tilted), side by side in a `ScreenBoard`
   (padding 40, gap 40, background #111). No device bezels / perspective.

## The "Highlight" chip
Most references show a grey "Highlight" capsule over the status-bar time. Reproduce it with `<HighlightChip />`
(adjust position/size via className if needed) and keep the status bar (time hidden under the chip, signal/wifi/battery on the right).

## Project
- `src/ui/` shared library (copied skeleton): `ScreenBoard`, `AppScreen`, `SCREEN`, `HighlightChip`, `StatusBar`,
  `SignalBars`, `Battery`, `HomeIndicator`, `DynamicIsland`, `ImagePlaceholder`, `Avatar`, `IconButton`, `Button`,
  `ChipGroup`, `SearchField`, `SegmentedControl`, `Toggle`, `TabBar`, `IconLabelTab`, `Placed`, `cn`.
  Import from `../../ui`. **Do not edit `src/ui/`** (other agents work concurrently) — put new generic pieces in your folder.
- `src/apps/aNN/index.tsx` default-exports `AppDefinition` `{ id: 'NN', title, screens, Component }`; Component returns
  `<ScreenBoard>` with exactly `screens` `<AppScreen>` children. Auto-registered — don't edit registry/App.
- Suggested per folder: `index.tsx`, `screens/*.tsx`, `components/*.tsx`, `data.ts`, `theme.ts`.
- Partially visible content at screen edges (cards cut off by the screen, scroll positions) must be reproduced as in
  the reference (content overflows and is clipped by the screen).

## Fonts (Tailwind utilities, see src/index.css)
font-inter (default SF-like), font-pretendard (Korean), font-jakarta, font-dm, font-manrope, font-outfit, font-urbanist,
font-sora, font-figtree, font-bricolage, font-grotesk, font-archivo, font-geist, font-onest, font-instrument,
font-playfair, font-condensed, font-spacemono, font-plexmono, font-montalt, font-poppins, font-lilita, font-times,
font-instrument-serif, font-hanken, font-work, font-lexend. Pick the closest match.

## Reference extraction (already prepared)
`public/flat/NN.png` holds the reference screens cut out and scaled to exactly 390×844 each, laid out in the same
board geometry your implementation renders (so they can be compared 1:1). Boxes are in `scripts/boxes/NN.json`.
**Check the flat image first.** If a screen is cut wrongly (e.g. a phone partially off-image, wrong top/bottom),
fix the boxes: `python3 scripts/extract.py NN --boxes "x,y,w,h x,y,w,h ..."` (screen outer edges in the reference;
each phone is ~270×582 px in the reference, i.e. ×1.445 to logical points).
For a phone that is cut off by the image edge, still render a full 390×844 screen and complete the cut part
plausibly from the visible design.

## Verify loop
```
cd /home/user/skills-introduction-to-github/app2-clone
npx tsc -p . 2>&1 | grep -E "apps/aNN"
node scripts/screenshot.mjs NN                     # shots/NN.png, NN-side.png (ref above / impl below), NN-blend.png
node scripts/screenshot.mjs NN --crop x,y,w,h      # zoomed ref|impl of a region (board coordinates) -> shots/NN-crop.png
```
Screen i (0-based) spans x = 40 + i*430 … +390, y = 40 … 884 on the board.
The side image is downscaled when read — use --crop on every screen/section. Iterate many rounds.

## Don'ts
No git commits, no edits outside your folders, no package.json changes / npm install.
