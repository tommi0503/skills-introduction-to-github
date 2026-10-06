# slice-clone2

34 MiriCanvas presentation templates (459 slides, 1280×720) re-created with React + Tailwind CSS v4 + lucide-react.

```
npm install && npm run dev        # http://localhost:5173  (index of decks; #/NN opens one deck)
node scripts/screenshot.mjs [NN]  # shots/NN/SS.png per slide
python3 scripts/view.py NN [S..] [--half]   # reference vs render
node scripts/audit.mjs [NN]       # text overflow / clipping / overlap check
```

- `public/reference/NN/SS.webp` — reference slides (`meta.json` = template title)
- `src/decks/dNN/` — `data.ts` (content) · `theme.ts` (tokens) · `components.tsx` (deck layouts) · `index.tsx` (slides)
- `src/ui/` — shared `Slide` (fixed 1280×720), `Abs`, `ImagePlaceholder`, `Board`
- Photos, illustrations, logos, graphic backgrounds and non-lucide icons are flat light-grey placeholders.
