# Unexpressible source components

## sm-04-01: page 4, venn

Measured bbox `[116, 337, 1049, 301]`. The source has outline-only circles, an elongated centre set and icon/name/note parts. venn.sets has no line variant and no mark/note slots; the single base is the filled three-set overlap on page16.

Required contract markup:

```html
<div class="venn line"><div class="set"><span class="mark"></span><p class="name"></p><p class="note"></p></div></div> — add explicit .line variant and mark/note set parts.
```

## sm-09-02: page 9, pill

Measured bbox `[465, 292, 352, 128]`. Three cylindrical stores require a database/store shape with top ellipse, side wall and attached label. pill.parts is a one-line capsule; changing it into a cylinder would be a second design without a contract variant.

Required contract markup:

```html
<div class="stores"><div class="store"><p class="name"></p></div></div> — new database-store contract, not a pill variant inferred from an icon name.
```

## sm-14-10: page 14, chart-line

Measured bbox `[668, 370, 3, 130]`. A labelled BEP guide at a chosen x value is an annotation; chart.line has only data points and no annotation/target part.

Required contract markup:

```html
<div class="lines"><div class="annotation" style="--at:3"><span>BEP</span></div></div> — explicit chart annotation slot and data index.
```

## sm-17-02: page 17, timeline

Measured bbox `[94, 402, 1092, 60]`. Three duration bands span one/two/two stops. timeline.stop owns a single date, and sibling/empty-date inference is forbidden. A band with from/to period data is required.

Required contract markup:

```html
<div class="track"><div class="bands"><div class="bar" style="--from:0;--to:1"><span></span></div></div><div class="stop">…</div></div> — explicit owned duration bands.
```

## sm-18-05: page 18, network

Measured bbox `[589, 298, 610, 345]`. The topology is expressible as network positions/links, but its nodes require independently sized 249x69,94x138,94x47 and267x70 footprints. network.node has position data only and no footprint field. No page geometry token is introduced.

Required contract markup:

```html
<div class="network"><div class="node" style="--x:20;--y:10;--w:40;--h:20"><p class="name"></p></div></div> — explicit node footprints in graph coordinates; this is a requested contract addition, not an implemented geometry extension.
```

## sm-20-05: page 20, chart-stack

Measured bbox `[498, 381, 282.985, 80]`. A single four-part allocation bar is not chart.stack: its contract requires 2–12 sbar members. Adding an empty second row would falsify the data.

Required contract markup:

```html
<div class="stacks pct h"><div class="sbar"><span></span><div class="seg" style="--v:40"><b>40%</b></div>…</div></div> — extend the sbar count lower bound from 2 to 1.
```

## sm-21-05: page 21, chart-donut

Measured bbox `[460, 289, 360, 360]`. A four-share pie is not a one-share donut or a row of donuts. The contract has no pie/sector/start-angle form, and overlaying four whole donuts would misrepresent their semantics.

Required contract markup:

```html
<div class="pie"><div class="share" style="--v:40"><p class="fig"></p><p class="name"></p></div>…</div> — new multi-share pie root with automatic cumulative angles.
```


## sm-13-05: page 13, chart-bar

Measured bbox `[674, 312, 522, 337]`. The source owns 6 shared period categories, each with two comparable series (타사 / MIRI COMPANY). Empty alternate labels in a flat `.bars` list would destroy shared category ownership. Page14's previous10-bar extraction also mistakenly discarded real bars while filtering legend rectangles. All measured original values and SVG rectangles remain in map.json, but no flattened chart is assembled.

Required contract markup:

```html
<div class="grouped" style="--max:100"><div class="mgroup"><span class="name">2050년</span><div class="series tone-5" style="--v:10"><b></b></div><div class="series tone-1" style="--v:20"><b></b></div></div>…</div>
```

A new grouped-bar contract must own categories and consistently identified series; this is a proposed contract, not implemented markup.


## sm-14-06: page 14, chart-bar

Measured bbox `[865, 270, 330, 266]`. The source owns 6 shared period categories, each with two comparable series (타사 / MIRI COMPANY). Empty alternate labels in a flat `.bars` list would destroy shared category ownership. Page14's previous10-bar extraction also mistakenly discarded real bars while filtering legend rectangles. All measured original values and SVG rectangles remain in map.json, but no flattened chart is assembled.

Required contract markup:

```html
<div class="grouped" style="--max:100"><div class="mgroup"><span class="name">2050년</span><div class="series tone-5" style="--v:10"><b></b></div><div class="series tone-1" style="--v:20"><b></b></div></div>…</div>
```

A new grouped-bar contract must own categories and consistently identified series; this is a proposed contract, not implemented markup.


## sm-20-bars: page 20, chart-bar

Measured bbox `[875, 347, 286, 274]`. The source owns 5 shared period categories, each with two comparable series (타사 / MIRI COMPANY). Empty alternate labels in a flat `.bars` list would destroy shared category ownership. Page14's previous10-bar extraction also mistakenly discarded real bars while filtering legend rectangles. All measured original values and SVG rectangles remain in map.json, but no flattened chart is assembled.

Required contract markup:

```html
<div class="grouped" style="--max:100"><div class="mgroup"><span class="name">2050년</span><div class="series tone-5" style="--v:10"><b></b></div><div class="series tone-1" style="--v:20"><b></b></div></div>…</div>
```

A new grouped-bar contract must own categories and consistently identified series; this is a proposed contract, not implemented markup.


## sm-13-legend: page13, legend placement

Measured bbox `[689,362,89.473,35]`. The two-line legend itself is admitted and its exact same source shape is the legend base on page14. The immutable initial page13 grid gives both this legend and the22px period copy the same42px row. Their original19px gap cannot also fit. Shrinking text, hiding a key or shifting this page slot would change the source or evade the fixed-map rule, so only this placement is omitted.

Required contract markup:

```html
<div class="grouped"><div class="chart-head"><p class="period"></p><div class="legend"><span class="key"></span><span class="key"></span></div></div><div class="mgroup">…</div></div>
```

The proposed grouped-chart contract needs independently owned period/legend header space; alternatively foundation would need finer vertical placement than the fixed12×6 slots. This markup is a proposed contract addition, not implemented page CSS.
