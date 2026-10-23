# Dockside build notes

Delivered collection and review HTML/CSS are the canonical final sources. Python files record incremental authoring and review repairs; do not concatenate all scripts because some edits are deliberately one-time transformations.

Re-render the committed source using `/workspace/work/tools/render_review.py pages --root <this-root> --kind replica|reassembled --original-dir <deck-dir>` and `library --root <this-root> --name dockside`. The library renderer calls the unchanged reference `tools/preview.py` with `contract/type-steps.json` and the light/dark flags, then captures each element folder.

Review CSS snapshots must remain byte-identical to collection CSS. Review assets supply only the contract palette/type steps, actual fonts, and the Lucide rendering runtime.
