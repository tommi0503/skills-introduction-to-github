# Build sources

The canonical collection CSS/HTML/JSON is the sibling `undertow/` collection. The final replica HTML/CSS and all reassembled HTML are canonical review sources. They load local fonts and a local Lucide runtime; no external network resources are required for viewing.

`precision-pages.py` generates the final reassembled HTML from the final collection source. `finalize-library.py` invokes the reference preview CLI, makes font links relative, and scopes the tool’s presentation-only `.frame` / `small` rules to avoid collisions with contract parts. `library.js` renders all fixtures and checks minimum/intermediate/full grid sizes in both modes. `render.js replica` and `render.js reassembled` capture deck pages. These browser servers bind loopback and serve only this review directory. `package-review.py` builds element sheets, PDFs, and comparisons; `refresh-checks.py` updates the manifest.

The authoring scripts (`replica.py`, `reassemble.py`, `collection.py`, and individual correction scripts) are historical steps, not a one-command installer. Do not rerun an earlier authoring step over the final source: the initial replica generator also resets its font stylesheet. Exact reuse starts with the final collection and final replica source files. Scripts retain the workspace paths used for the build and reference the extracted reference pack and original deck; update those paths when reproducing elsewhere.

`audit-final.cjs undertow` uses the lead reviewer’s text-range/slot-boundary/overlap/contrast algorithm, with output isolated to the author’s scratch directory. `library/boundary-audit.json` records the final result: 522 cases per mode, no overlap/overflow or contrast candidates. The lead reviewer performs the final integration audit independently.
