# Leaflet implementation brief

Goal: re-create each leaflet in `public/reference/NN.jpg` with React + Tailwind v4 + lucide-react, as faithfully as
possible, as a **flat, unfolded sheet**. One reference image = one folder `src/leaflets/lNN/`.

## Hard rules (from the user)
1. **Image areas, photos, illustrations, graphic backgrounds/patterns/textures (crumpled paper, waves, leaves, hills,
   maps drawn as art, mascots, decorative shapes that are artwork), logos, QR codes and icons lucide can't cover →
   `ImagePlaceholder`** (flat light grey `#e5e7eb`, one colour). Keep the region's size/position/shape (radius,
   circle, arch via border-radius or clip-path). Don't try to draw them. If white text sits on top of a photo you may use a slightly
   darker light grey `tone` (e.g. `#c9ccd1`) for legibility — still flat.
   Plain UI must be implemented: solid/gradient panel backgrounds, colour bands, boxes, cards, pills, buttons, tables,
   dividers, lines, simple frames/borders, bullet markers, numbering, text, lucide icons.
2. **Visually verify** repeatedly (screenshot → compare → fix) until text, sizes, positions, colours, weights,
   line breaks, spacing match.
3. **Reusable, SOLID, no hard-coding**: content in typed `data.ts`, mapped over; screens composed from components;
   style via props / className injection; one responsibility per component.
4. **Every panel has exactly the same size** — `PANEL` = 480×1018 px (from `src/ui/core/geometry.ts`).
   A 3-panel leaflet is 1440×1018, a 4-panel 1920×1018. No tilt/perspective/folds/shadows/mockup background —
   render the unfolded sheet only. Count the panels in the reference (image 02 is 4 panels; check each).

## Project
- `src/ui/` shared library — `Leaflet` (sheet; `panels`, `background`, `underlay`/`overlay` for elements spanning
  panels, optional `folds`), `Panel` (one fold, fixed size), `Placed`, `ImagePlaceholder`, `Pill`, `Divider`,
  `IconBadge`, `DataTable`, `KeyValueList`, `BulletList`, `VerticalText`, `cn`, `PANEL`. Import from `../../ui`.
  **Do not edit `src/ui/`** (other agents work concurrently). Put new generic pieces in your own folder.
- `src/leaflets/lNN/index.tsx` default-exports `LeafletDefinition` `{ id: 'NN', title, panels, Component }`;
  Component returns `<Leaflet panels={n}>` with exactly n `<Panel>` children. Auto-registered — don't edit
  registry/App.
- Suggested per folder: `index.tsx`, `panels/*.tsx` (one component per panel), `components/*.tsx`, `data.ts`,
  `theme.ts`. Leaflets that are the outside/inside of the same brochure (same design system, e.g. 13/14, 15/16,
  17/18, 20/21, 22/23, 26/27, 28/29, 30/31, 32/33, 34/35) should share a theme/components folder you own, e.g.
  `src/leaflets/shared-2021/` (no index.tsx there).

## Fonts (Tailwind utilities, see src/index.css)
Korean: font-pretendard (default), font-noto-sans, font-noto-serif, font-myeongjo, font-gowun-batang,
font-gowun-dodum, font-blackhan, font-dohyeon, font-jua, font-nanum-pen, font-gaegu, font-sunflower, font-gothic-a1,
font-plex-kr, font-song-myung, font-yeon-sung, font-nanum-gothic, font-hahmlet, font-dongle, font-single-day,
font-hi-melody, font-dela. Latin: font-inter, font-poppins, font-dm, font-montserrat, font-anton, font-archivo-black,
font-bebas, font-oswald. Pick the closest match.

## Reference flattening (most references are photos of a printed leaflet, some angled)
Measure the sheet's TOP edge points (left corner, each fold, right corner) and BOTTOM edge points in the reference
(write Pillow snippets to find edges; zoom crops to be precise), then:
```
cd /home/user/skills-introduction-to-github/leaflet-clone
python3 scripts/rectify.py NN --top x,y x,y x,y x,y --bottom x,y x,y x,y x,y   # -> public/flat/NN.png (1440x1018 / 1920x1018)
```
Check the flat image looks right (Read it). Points are saved to scripts/corners/NN.json. Folds in the photo are
not always at exact thirds — measure them; your implementation still uses equal panels.
(If the design clearly has content that doesn't fit equal panels after flattening, follow the design proportions within each panel.)

## Verify loop
```
npx tsc -p . 2>&1 | grep -E "leaflets/(lNN|shared-xx)"
node scripts/screenshot.mjs NN                    # shots/NN.png, NN-side.png (flat ref above / impl below), NN-blend.png
node scripts/screenshot.mjs NN --crop x,y,w,h     # zoomed ref|impl region -> shots/NN-crop.png
```
The side image is downscaled when read — use --crop on every panel/section to check details. Iterate many rounds.

## Don'ts
No git commits, no edits outside your folders, no package.json changes / npm install.
