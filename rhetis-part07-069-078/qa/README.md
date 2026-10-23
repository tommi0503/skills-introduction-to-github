# Independent integration QA

This directory contains independent local audits. It does not run the upstream Rhetis intake, which is not included in the supplied reference pack. No sample design CSS was read or copied by these audits.

- `audit_css.py`: balanced syntax, selector scope, palette and typography token use, supported classes, foundation/root separation, metadata, and the 28 required golden fixtures per collection. Golden comparisons normalize only collection `data-el` identifiers and line endings. Three remaining informational warnings are data-dependent chart geometry, not fixed spacing defaults.
- `browser_audit.py`: actual Chromium selector/declaration support. `!important` is removed from values before `CSS.supports`, because priority is not part of a property value.
- `alignment_audit.py`: title-start alignment across the six golden card fixtures. All five collections now have zero drift.
- `pill_audit.py`: intrinsic capsule dimensions and contained names at the declared minimum and full size; also rejects the invalid descendant `.slide .cover` selector for the same-element cover variant.
- `code_font_audit.py`: loaded allowed font plus measured `iiii`/`WWWW` equal widths, verifying an actual monospaced source font.
- `clipping_audit.py`: text line boxes crossing an ancestor that actually clips overflow. This separates real clipping from harmless glyph ink extending beyond a line box. Tests declared minima, applicable midpoint sizes and 12×6; a zero result only covers the recorded text-overflow cases, not graphic clipping, shape masking, overlap, missing content, or similarity to the reference.
- `contrast_audit.py`: light/dark solid-background text contrast. Backgrounds are composited only where the text is geometrically inside the painted ancestor. This matters for labels intentionally placed outside bars or circular hub members. Absolute pseudo-element paints and polygon masks are considered where supported; gradient backgrounds and text crossing polygon edges still require visual review.

The screenshot files named `*-area-latest.png`, older `*-overflow-summary.md` and `*-contrast-summary.md` were intermediate diagnostics, not final delivery renders. Current machine-readable audit JSON is generated from the current source snapshot. The main renderer owns the final delivery images, PDFs, ZIP validation and upload verification.

The supplied golden `card-4` contains a literal star glyph, and golden `callout-stack` contains agricultural copy. Exact supplied-fixture preservation takes precedence for those two inherited exceptions. New icons use the required empty Lucide placeholders; non-golden agricultural prose was replaced with business copy. Non-golden bullet data outside the 0–100 contract was repaired centrally by the main agent.

- `functional_audit.py` / `functional.js`: selected graphic and semantic probes for ordinal stack distinction, circular donuts, balance direction, target-marker alignment, bare seats, empty heatmap/waffle shapes outside their slot, and polygon clipping. These are functional checks and cannot certify reference fidelity.
- `final_manifest.py`: SHA-256 for every collection source file and audit report, plus audit snapshot/current-sheet matching.

## Visual fidelity gate

A technically valid collection can still differ materially from the source. Final acceptance must compare every original/replica/reassembled page at the same 1280×720 scale. Check main block bounds and whitespace, text baselines/wraps/visual sizes, connector endpoints/directions and shape heights, and missing icon/content rows. Inspect a 50% overlay and a three-column original/replica/reassembled comparison, masking only permitted gray media placeholders. A missing structural row or incorrect diagram connection fails this gate regardless of zero automatic clipping errors. No report here certifies visual identity.

## Later fidelity restoration assignment

After the baseline QA, the main agent explicitly assigned Meridian reassembled pages 25–29 and their separate `fidelity_tail_patch.py` module to the integration agent. See `meridian-tail-review.md`. The collection owner alone merges shared CSS; prior audit snapshots must be treated as historical after this work.

## Final frozen-source audit extensions

- `clipping_dark_audit.py` and `functional_audit.py --dark` retain separate dark-mode results.
- `contrast_min_audit.py` measures declared minimum slot sizes in light/dark, including alternative declared minima when supplied; it is separate from the full 12×6 contrast audit.
- Contrast thresholds follow AA text sizing: 3:1 at 24px and above, or at least 18.667px with weight 700 and above; 4.5:1 otherwise. Thin pseudo-element lines and polygon-edge overlaps remain candidates requiring visual review.
- The explicitly approved Vectorbox quiet-bar source value labels remain in DOM/ARIA as visually hidden annotations. `clipping_audit.py` records those separately as `accessibleValueClips`; it does not suppress other visible text clipping.
- Newly restored triangular or circular compositions can intentionally place names at different vertical offsets. The golden row-card alignment check remains distinct from these source-specific compositions.

- The final static audit now enforces explicit12×6 top-level placement on every nongolden fixture. Only the exact28 supplied filenames are exempted, not all fixtures in their element category. Missing new fixture placement was corrected centrally before the final source snapshots.
- `functional_audit.py --all` checks all56 element types plusfoundation rather than the default selected18 types; `--all --dark` writes a separate all-type dark report. These probes inspect the documented selector/semantic cases, not every possible geometry or visual resemblance.
- `crossrail_native_contrast.py` plus `apply_native_contrast.py` resolve the annotated chart's sibling-panel background using real PNG paint, locked to the same source SHA and exact text/class/font-size. Raw ancestor-only candidates remain available.
- Historical broad reports can remain stale after a narrowly scoped final source-only patch. Current affected-type follow-up reports are separate, with matching SHA. `FINAL-QA-STATUS.md` describes these scopes and `final-source-manifest.json` preserves both current and historical hashes.
