# Confluence source build

Run from any working directory in this workspace:

```sh
python /workspace/work/deliverables/confluence/build/replica.py
python /workspace/work/deliverables/confluence/build/collection.py
python /workspace/work/deliverables/confluence/build/reassemble.py
python /workspace/work/deliverables/confluence/build/refine.py
python /workspace/work/deliverables/confluence/build/finalize.py
python /workspace/work/deliverables/confluence/build/minimum_fixes.py
python /workspace/work/deliverables/confluence/build/normalize_lists.py
python /workspace/work/deliverables/confluence/build/radar_queries.py
python /workspace/work/deliverables/confluence/build/diagram_fixes.py
python /workspace/work/tools/check_contract.py /workspace/work/deliverables/confluence/collection/confluence --out /workspace/work/deliverables/confluence/review/audit-contract.json
```

The scripts consume the supplied reference pack for taxonomy, allowed type steps, fonts, and fixture markup. They never read sample component CSS; each component’s CSS is independently authored. The line/area implementations use CSS anchor positioning to read point geometry, a rendering technique rather than a copied visual design.

`collection.py` always recreates the base source; run the four collection stages once in the order above. `refine.py` and `finalize.py` apply the recorded browser-review repairs, including compact geometry, readable accent text, a monospaced code font, preview namespace isolation and portable review assets.

Use the parent renderer in `/workspace/work/tools/render_review.py` for pages and library. It needs Chromium and network-enabled sandbox permissions for localhost sockets. Review HTML uses relative font and collection CSS paths; the review bundle can be opened after extraction. The collection ZIP itself contains only CSS, JSON, Markdown and HTML, with no font binaries or scripts.

The fidelity rework requested after the first review adds these ordered stages after diagram_fixes.py:

```sh
python /workspace/work/deliverables/confluence/build/fidelity_v2.py
python /workspace/work/deliverables/confluence/build/fidelity_complete.py
python /workspace/work/deliverables/confluence/build/fidelity_polish.py
python /workspace/work/deliverables/confluence/build/fidelity_contract.py
python /workspace/work/deliverables/confluence/build/fidelity_final.py
python /workspace/work/deliverables/confluence/build/fidelity_validation.py
python /workspace/work/deliverables/confluence/build/fidelity_finish.py
python /workspace/work/deliverables/confluence/build/fidelity_palette_roles.py
python /workspace/work/deliverables/confluence/build/fidelity_resolve.py
```

The final canonical source is collection/confluence/. The fidelity stages restore measured source geometry and host palette rather than retaining the earlier normalization differences. The source display font remains an allowed family approximation; the exact original family is unconfirmed. Render the final pages and complete library after all source stages. Preserve radial contrast evidence rather than replacing the original-like background to silence the checker.

After the final fidelity stages, fidelity_sheet_fix.py removes placement attributes from the three metric cards inside their fixture group, restores readable number marks, and chooses a contrasting badge depth. It preserves original host colors. A full library render followed by the final card/hub/agenda rerender is merged by finalize_review_v2.py; that script also refreshes source hashes and artifact verification.
