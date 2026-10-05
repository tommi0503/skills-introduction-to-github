# Web clone brief

Goal: re-create live marketing websites as faithfully as possible with React + Tailwind v4 + lucide-react.
One site = one folder `src/sites/wNN/`. Reference = the real page, already captured for you.

## Hard rules (from the user)
1. **Photos, videos, illustrations, 3D renders, product screenshots/mockups, maps/globes, graphic or gradient-art
   backgrounds, logo marks and customer-logo strips, and icons lucide can't cover → `ImagePlaceholder`** (flat light grey
   `#e5e7eb`, one colour). Keep each region's exact size/position/radius. Don't draw them. On dark sections you may
   pass a darker flat `tone` so it reads (still one flat colour). Text-only wordmarks may be rendered as text.
   Plain UI must be implemented: nav bars, buttons, pills, cards, section backgrounds (solid colours), grids,
   tabs, pricing tables, stats, footers, dividers, text, lucide icons.
2. **Visually verify** repeatedly (screenshot → compare → fix) until text, sizes, positions, colours, weights,
   line breaks and spacing match.
3. **Reusable, SOLID, no hard-coding**: content in typed `data.ts` mapped over; sections are components in
   `sections/`; shared pieces in `components/`; tokens in `theme.ts`; props / className injection for variants.
4. **Every render has exactly the same size**: `FRAME` = 1440×4500 (desktop width 1440, the first 4500px of the
   page). Wrap the site in `<PageFrame background=...>`; content beyond 4500px is clipped — implement everything
   visible in the first 4500px (a section cut by the bottom edge must be cut at the same place). Never tilted.

## References (already captured with a real browser at 1440×900 viewport, scrolled once to trigger lazy content)
- `public/flat/NN.png` — the first 4500px of the live page = your comparison target (pages shorter than 4500
  are padded with their bottom colour).
- `public/reference/NN.png` — full page, for context only.
- `reference-dom/NN.json` — **use this**: every visible text/media element in the frame with exact x, y, w, h,
  font family, size, weight, line-height, letter-spacing, colour, background, radius. `reference-dom/NN.html` is
  the full DOM. Use these to get exact copy text, fonts and metrics instead of guessing. Do NOT load anything from
  the live site at runtime (no remote images/fonts/scripts) — the clone must be self-contained.
- Re-capture one site if needed: `node scripts/capture.mjs NN` (only if the capture is clearly broken).
- Animations were frozen at capture time; reproduce the captured state.

## Project
- `src/ui/` shared library: `PageFrame`, `Container`, `FRAME`, `ImagePlaceholder`, `cn`. Import from `../../ui`.
  **Do not edit `src/ui/`** (other agents work concurrently) — put generic pieces in your own folder.
- `src/sites/wNN/index.tsx` default-exports `SiteDefinition` `{ id: 'NN', title, url, Component }`. Auto-registered.
- Fonts: Tailwind utilities from `src/index.css` (font-inter, font-geist, font-dm, font-manrope, font-jakarta,
  font-outfit, font-figtree, font-sora, font-grotesk, font-archivo, font-onest, font-instrument, font-instrument-serif,
  font-playfair, font-times, font-poppins, font-spacemono, font-plexmono, font-hanken, font-work, font-lexend,
  font-urbanist, font-bricolage, font-condensed, font-montalt, font-lilita, font-pretendard ...). Pick the closest to the
  reference font named in reference-dom JSON. You may add a site-local CSS file with @font-face pointing into
  node_modules/@fontsource* files if needed (no new packages / npm install).

## Verify loop
```
cd /home/user/skills-introduction-to-github/web-clone
npx tsc -p . 2>&1 | grep -E "sites/wNN"
node scripts/screenshot.mjs NN                    # shots/NN.png, NN-side.png (ref | impl), NN-blend.png
node scripts/screenshot.mjs NN --crop x,y,w,h     # zoomed ref (top) / impl (bottom) -> shots/NN-crop.png
```
The side image is downscaled heavily when read — always use --crop (e.g. 0,0,1440,900 then 0,900,1440,900 …)
section by section. Iterate many rounds.

## Don'ts
No git commits, no edits outside your folders, no package.json changes / npm install.
