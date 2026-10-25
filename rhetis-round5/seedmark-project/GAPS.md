# Genuine residual limitation

## Single-observation allocation bar — page20

`sm-20-05`, bbox `[498,381,282.985,80]`, contains exactly one stacked allocation observation, whose four segments are40%,20%,30%,10%. `chart.stack@1` still explicitly requires2–12 `.sbar` members; round5 adds grouped/pie/annotation forms but does not amend that lower bound. No second empty observation is invented, and this single design is not rendered. A card decoration would hide quantitative chart semantics.

Proposed compatible extension:

```html
<div class="stacks pct h"><div class="sbar"><span></span><div class="seg" style="--v:40"><b>40%</b></div><div class="seg" style="--v:20"><b>20%</b></div><div class="seg" style="--v:30"><b>30%</b></div><div class="seg" style="--v:10"><b>10%</b></div></div></div>
```

Required change: permit one `.sbar`; every existing meaning and numeric datum remains unchanged. All other previously recorded GAPs are restored as independent designs, chart-owned parts or a foundation panel. Grid rounding differences are review notes, never new GAPs.
