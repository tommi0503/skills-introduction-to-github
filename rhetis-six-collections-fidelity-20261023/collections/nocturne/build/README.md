# Nocturne authoring source

The authoritative collection is `../collection/nocturne/`; it contains 56 element CSS files, metadata, descriptions, and 170 fixtures. Review assets are separate. No example design CSS was copied.

The initial generators (`library.py`, `refine.py`, `final_adjust.py`, `quality_patch.py`) and fidelity scripts record the authoring history. Do not rerun those initialization steps over the final source files without reapplying the later revisions. The complete final CSS and fixtures are the deliverable source.

To update review pages after changing the collection:
1. `python build/reassemble.py` copies current collection CSS and restores the measured, contract-only markup in `build/templates/reassembled/`. The template host CSS contains palette and type tokens only.
2. `python build/render_fresh.py pages --root . --kind reassembled --original-dir <original-image-folder>` renders each page at 1280×720; use `--kind replica` for the independent replica sources.
3. `python /workspace/work/tools/render_review.py library --root . --name nocturne` generates reference-palette light/dark sheets, per-element PNGs, complete PDFs, and minimum/full-size audits.
4. `python /workspace/work/tools/check_contract.py collection/nocturne --out review/audit-contract.json` runs the reference static contract aid.

Chromium requires the supported network-enabled execution sandbox and a localhost HTTP server. The review pages themselves use local font and icon assets. The rendering tools use an HTTP server because managed Chromium blocks file:// navigation. Final visual proofs use SHA-specific filenames to avoid stale-image display caches.

`review/revision-heading-bboxes.json` records the measured original/replica/reassembled heading ink bounds. Replica sources remain independent; their final CSS includes the user-authorized fidelity revision.
