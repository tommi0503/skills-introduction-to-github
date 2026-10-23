# Afterglow build sources

Inputs are `/workspace/work/reference` and the 9-image deck under `/workspace/work/deck`.

1. Run `python replica.py` and `python render_replica.py` for the uncontracted replicas. The measured chapter title loads SUITE Regular at 176px.
2. Run `python collection.py`, then `python fidelity.py`, `python fidelity-refine.py`, `python fidelity-final.py`, `python fidelity-measure.py`, `python fidelity-contract.py`, `python fidelity-polish.py`, `python tokenize-fidelity.py` in order. These preserve all required fixture markup/data and apply the source-measured geometry without adding page CSS.
3. Run `python reassembled.py` to create contract markup on the 12×6 foundation and copy byte-identical collection CSS into the portable review assets.
4. Run `/workspace/work/tools/check_contract.py` on `../collection/afterglow` with `--out ../review/audit-contract.json`.
5. Run `/workspace/work/tools/render_review.py library --root .. --name afterglow`.
6. Run `/workspace/work/tools/render_review.py pages --root .. --kind reassembled --original-dir <original-folder>` and the same with `--kind replica`.
7. Run `python finalize_review.py` to verify dimensions, hashes, PDFs and portable previews.

The supplied Chromium runner needs network-enabled sandbox permissions for local HTTP sockets. Large 2560px comparison PNGs can lose apparent regions in automatic image-tool previews; compare the actual pixels, use original-detail mode, or inspect a manually resized copy. The saved comparison PNG and standalone page are pixel-identical in their corresponding half.
