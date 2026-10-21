# Six EONU concepts — implementation contract

Each concept contains 12 slides following `shared/content.js` and the newest source MD. Slide 06 is a demo flow, per user confirmation. All six concepts must be visibly different in composition, diagram grammar and hierarchy, not merely palette.

## Owned files
Work ONLY in `concepts/<your-id>/`. Deliver `deck.js`, `style.css`, `concept.json`, `references.md`. Do not spawn any agents. Root owns shared viewer, exports, package and Git operations.

## Runtime contract
`shared/content.js` loads first. `deck.js` must be a classic script, no DOM or network dependencies, and assign `window.CONCEPT = {slides, renderSlide}`. slides is an array of exactly 12 objects with `id` (two digit string), `title`, `section`, `talk`, `note`, `content`. Preserve substantive facts and full talk/notes from IR_CONTENT; titles may improve. `renderSlide(slide, mode='design')` returns one `<article class="slide design page-01">` (or wireframe) with data-slide="01". Root evaluates this via Node VM and builds static HTML. All diagrams must be actual SVG/HTML, not placeholder charts.

Canvas is exactly 1280 × 720. `.slide` must be position:relative;overflow:hidden;box-sizing:border-box. CSS selectors must be scoped to `.slide` except font declarations. Root provides local Pretendard @font-face, font-family inheritance and border-box reset. No external asset dependency. Any fonts, fixed dimensions, line heights, radius, margins, padding, border widths are multiples of 2px, primarily 4px. Use 0 freely, no 1px rules. Unitless line-height allowed but prefer exact even px. Letter spacing can be 0; do not use fractional negative pixels.

Cover 01 and closing 12 have NO `.section-label`, `.slide-header`, `.page-number` or slide footer. Body 02–11 have identical `.section-label` coordinates within each concept. Use `.heading` for heading block and `.slide-footer` for tiny source labels. Root checks bounds and even font values.

Images are solid light-gray #e5e5e5 `.placeholder` blocks with short descriptive Korean labels, no photos or generated image content. Provide generous and intentional image real estate on cover, problem, use case, product, team and closing. Labels may be discreet. Product UI illustrations are separate and should be implemented properly as explanatory HTML, clearly labeled. Never invent business numbers, traction, price, allocation or market size.

Wireframe mode must preserve geometry and charts, simplify color through CSS `.slide.wireframe`. Do not reuse old v3 deck layout. All 12 pages must be fully designed.

`concept.json`: {"id":"a","name":"Korean name","tagline":"short visual idea","accent":"#hex","references":["repo folder names"]}. references.md must identify actual inspected image/template paths, concrete borrowed layout/components and deliberate adaptation. Read actual source and preview images from assigned reference folders. Inspect final renders when root gives paths.

## Factual guardrails
1. Intro: patient/guardian/clinician AI communication.
2. Child alone clinic is reconstructed illustrative case; no frequency claims.
3. Three roles → EONU → care plan to daily life.
4. Efficiency/clinical value/revenue are hypotheses. Revenue focus: unresolved concern → clinic info → voluntary consultation. AI does not determine treatment necessity.
5. Clinician config first, questions/info/care plan → patient QR entry.
6. Config → diary/voice/check → AI draft → user checks original/summary/sharing → clinician author/status → care plan back. Explanation UI, not actual EMR integration.
7. B2B first → validate paid → B2B2C later; B2G separate procurement route. No signed contracts claimed.
8. TAM/SAM/SOM conceptual nested scope; NO invented quantities. Institution×annual price, users×conversion×annual spend, purchases×contract. Values unconfirmed. Exclude hardware/grants/double counting.
9. Patient-first future EMR/apps/devices/research, ADHD/elderly future. No completed integration.
10. MD states psychiatrist feedback, research-institute contact, youth-depression volunteer participation confirmed. Other pilots/contracts unconfirmed. Distinguish evidence levels.
11. Founder plans/builds/iterates. Planned total funding 1억 원; no allocation percentages, timing or institution targets. Build/security/trials/acquisition/ops.
12. Closing triangle and concise hook. No invented name/contact.
