# Implementation brief (for every showcase)

Goal: re-create each reference image in `public/reference/NN.jpg` **pixel-faithfully** with
React + Tailwind CSS v4 + lucide-react. One reference image = one showcase folder `src/showcases/sNN/`.

## Hard rules (from the user)
1. **Photos, illustrations, logos, 3D renders, maps, mascots, product shots, brand marks, blurred photo
   backgrounds and anything lucide can't express → `ImagePlaceholder`** (flat light grey `#e5e7eb`, single
   colour, no gradients, no drawing). Keep the placeholder's exact size/position/radius. Don't try to draw them.
   On a dark/coloured stage background area that is a *photo*, still use the placeholder (you may pass
   a slightly different light grey `tone` only if needed for legibility, but keep it light & flat).
   Plain UI surfaces (solid or gradient card backgrounds, buttons, chips, bars, progress, calendars, charts made of simple bars,
   toggles, text) must be implemented as UI.
2. **Visually verify** – screenshot, compare with the reference, fix, repeat until it matches: layout, positions,
   sizes, radii, colours, font family/size/weight, letter-spacing, line breaks, icon choice/size/stroke, shadows.
3. **Reusable, SOLID, no hard-coding**: screens are composed from components; content lives in typed data
   (`data.ts`) and is mapped over; components take props (Single Responsibility, Open/Closed via props /
   render props / className injection, small interfaces). No giant JSX blobs with copy-pasted rows.

## Project layout
- `src/ui/` — shared library (Stage, Placed, PhoneFrame, StatusBar, DynamicIsland, HomeIndicator,
  ImagePlaceholder, Avatar, IconButton, Button, ChipGroup, SearchField, SegmentedControl, Toggle, TabBar,
  IconLabelTab, cn). Import from `../../ui`. **Do not edit `src/ui/`** (other agents use it concurrently).
  If you need a generic primitive, create it inside your own showcase folder.
- `src/showcases/sNN/index.tsx` — default-exports a `ShowcaseDefinition`
  `{ id: 'NN', title, width, height, Component }` where width/height = reference image pixel size.
  It's auto-registered (import.meta.glob) — don't edit registry/App.
- Suggested inside each folder: `index.tsx` (stage composition: background + Placed phones),
  `screens/*.tsx` (one component per phone screen), `components/*.tsx` (app-specific reusable pieces),
  `data.ts` (content), `theme.ts` (colours/fonts tokens for that app).
- If several of your showcases are the same app family (e.g. the Korean Naver Pay screens), put the shared
  components in a shared folder you own, e.g. `src/showcases/shared-naver/` (no `index.tsx` there).

## Geometry approach
- `Stage` = exact reference size. Place each device with `<Placed x y>` at the pixel position measured in the reference.
- `PhoneFrame` takes outer stage-pixel size + `logicalWidth` (e.g. 375/390/393) and scales the screen content
  so you design screens in iOS points. Use `bezel` for devices with a visible black/graphite body.
  Rotated/tilted phones: use `Placed rotate`. Stage decorations (big background text, captions, floating cards)
  are positioned with `Placed` too.
- Measure precisely: write small Python (Pillow is installed) snippets to sample pixel colours and find
  edges/bounding boxes in the reference instead of guessing. Use those colours exactly.

## Fonts
Available Tailwind font utilities (see `src/index.css`): font-inter, font-pretendard (Korean UI — use for all
Korean screens), font-jakarta, font-dm, font-manrope, font-outfit, font-urbanist, font-sora, font-figtree,
font-bricolage, font-grotesk, font-archivo, font-geist, font-onest, font-instrument, font-playfair,
font-condensed, font-spacemono, font-plexmono, font-montalt, font-poppins, font-lilita, font-times.
Pick the closest match to the reference typography.

## Lucide
`lucide-react` v1.x. Check an icon exists: `ls node_modules/lucide-react/dist/esm/icons | grep -i <name>`.
Brand icons (instagram, tiktok…) may not exist → use a close generic icon or a placeholder.

## Verify loop
```
cd /home/user/skills-introduction-to-github/app-ui-clone
npx tsc -p . 2>&1 | grep -E "showcases/(sNN|shared-xxx)"     # only your folders matter; others are WIP
node scripts/screenshot.mjs NN                      # -> shots/NN.png, shots/NN-side.png, shots/NN-blend.png
node scripts/screenshot.mjs NN --crop x,y,w,h       # -> shots/NN-crop.png zoomed ref|impl for a region
```
Look at the images with the Read tool. The `-side` image is downscaled when you read it, so **use `--crop`
on every phone / region** to check details at zoom. The blend image reveals misalignment (ghosting).
Iterate many times: per phone, compare header, each section, typography and spacing. Don't stop at "roughly similar".

## Don'ts
- Don't `git commit`, don't touch other showcase folders, `src/ui`, `package.json` (no new deps).
- Don't run `npm install`.
