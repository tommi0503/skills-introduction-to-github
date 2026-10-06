# Handoff — UI clone projects

Repo: `tommi0503/skills-introduction-to-github` (default branch `main`).
Every project is React + Tailwind CSS v4 + lucide-react (Vite + TypeScript), one folder per project, each self-contained
(`npm install && npm run dev`). Reference images live in each project's `public/reference/`.

| Folder | What | Fixed size / unit | Per-item folder |
|---|---|---|---|
| `app-ui-clone/` | 26 mobile app showcase images | reference image size (Stage) | `src/showcases/sNN` |
| `leaflet-clone/` | 35 tri/quad-fold leaflets | panel 480×1018 (3단 1440, 4단 1920) | `src/leaflets/lNN` |
| `app2-clone/` | 20 app recordings | screen 390×844, board of screens | `src/apps/aNN` |
| `app3-clone/` | 24 app recordings ("Highlight" chip NOT rendered) | screen 390×844 | `src/apps/aNN` |
| `web-clone/` | 13 live websites (ada.cx blocked by bot check) | frame 1440×4500 | `src/sites/wNN` |
| `slides-clone/` | 32 presentation references → 98 slides | slide 1280×720, 2-col board | `src/decks/dNN` |
| `slice-clone2/` | 34 MiriCanvas decks → 459 slides (one webp per slide) | slide 1280×720, PNG per slide | `src/decks/dNN` |

Rules applied everywhere (from the user):
1. Photos, illustrations, graphic/gradient backgrounds, logos, mockups and icons lucide can't cover → flat light-grey
   `ImagePlaceholder` (single colour; a darker flat tone only for legibility on dark areas). Don't draw them.
2. Visually compare against the reference and fix until text, positions, sizes, colours and line breaks match.
3. Reusable/SOLID: content in typed `data.ts`, tokens in `theme.ts`, layouts as components; shared primitives in `src/ui/`.
4. Every screen/slide/page of a project has exactly the same size; nothing tilted.
5. Deliverable: render all items and send a zip of the PNGs.

Tooling per project (`scripts/`): slice-clone2 renders one PNG per slide (`shots/NN/SS.png`), `view.py NN [S..] [--half]`
stacks reference above render, `ref.py NN S..` stacks references; Korean font tokens (handwriting, display, serif) in its `src/index.css`.
Other projects: `screenshot.mjs [NN]` → `shots/NN.png`; comparison helpers (`compare.py`,
`view.py`, `extract.py`, `rectify.py`, `capture.mjs` depending on project); `slides-clone/scripts/audit.mjs [NN]`
detects text leaving the slide, spilling its box, clipped by a parent, or overlapping other text.
Chromium: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. For live websites in a cloud session, the proxy CA must be
trusted by Chromium: `certutil -A -n ccr-agent-proxy -t "C,," -i /root/.ccr/agent-proxy-ca.crt -d sql:/root/.pki/nssdb`
(install `libnss3-tools` first) and the environment needs network access to the sites.
