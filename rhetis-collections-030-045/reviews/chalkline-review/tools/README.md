# Browser rendering

Requires Node.js, Playwright and Chromium. Run `node tools/render.cjs` from the review folder (or set CHROMIUM_PATH to your Chromium executable). The script serves the review folder on a temporary loopback HTTP port, loads fonts, renders the two replica pages and two reassembled pages at 1280×720, captures every library fixture in both modes, and builds both library PDFs. It updates render-checks.json. The existing HTML files are the complete portable source.

The element contact sheets combine the native fixture captures in pairs at half size. Their labels state the fixture and mode. Source comparison sheets place the original reference on the left and the corresponding browser output on the right.
