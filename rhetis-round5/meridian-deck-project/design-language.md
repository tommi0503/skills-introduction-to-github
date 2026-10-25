# Meridian Deck design language

Source: the 30-page deck 074. `map.json` covers all 944 measured source parts, including page furniture and backgrounds. Each visible component is mapped to one semantic contract; repeated base designs point to their source page through `same-as:<page>` and preserve an instance `baseRef`.

The language combines straight broad planes, circles and fine rules. Neutral panels use a modest 10px shared corner, while filled emphasis and icon medallions are true circles. Capsules centre one line; picture frames use a fine outline and one small round plus medallion. A line of cards shares a fixed heading register. Circle icons occupy 52–54% of their badge.

Rules use `--stroke` (1px); stronger small geometry uses 2px. The spacing vocabulary is `--gap-sm` 10px, `--gap` 20px, `--pad` 24px and `--gap-lg` 36px. Repeated source geometry is expressed as fractions of the element's own received box through member percentages, cqw and cqh. Page coordinates are recorded in the map, never used as page selectors in element CSS.

The loaded face is Pretendard Variable. Source display headings are 48–88px, body headings 20–40px, running copy 14–20px and secondary labels 10–16px. Shared weight and line tokens separate titles, names, figures and copy. Components use admitted type steps or the explicitly allowed clamp formulas; compact boxes reduce type and spacing before losing essential figures or names. Monospaced source uses Nanum Gothic Coding.

Palette roles, rather than fixed colours, express the hierarchy: the main filled plane is `--a1`, its foreground `--a1-on`; accent headings and small text use `--a1-7`; broad quiet surfaces use `--n-1`/`--n-2`; hairlines use `--n-3`/`--n-4` or `--a1-4-muted`; body copy uses `--n-7`. Dark neutral fills pair `--n-7`/`--n-8` with `--page`. Source blue and greys are supplied only by the external `assets/source-palette.css` provider. The collection itself has no brand colour literals.

Connections belong to the root that owns every connected member. Line and area segments follow actual point anchors, including flat and descending pairs. Stacks and density marks follow numeric data. Tree, process, cycle and network owners draw their complete paths. An unsupported shared junction or grouping is listed in `GAPS.md`, never drawn by an unrelated neighbour.

The source's comparison page 17 is one table with three project columns and three labelled rows. Its lists and trends remain independently contracted nested roots inside cells. The table owns the shared row and column alignment.

The SWOT variant uses four rotated pointed lobes, with pointer tips painted above neighbouring fills. The measured neutral-to-accent process sequence uses quiet, deep-neutral and primary ranks; an explicit active member wins over ordinal defaults. Date/year pairs preserve a22/30 type hierarchy. Foundation cover furniture has a quiet lower-right hemisphere and an accent-medallion closing variant. Grey seats remain numbered per the foundation contract. The exact source limitations and native-grid differences are documented in review-notes.md and GAPS.md.

SWOT cells use registered nested list elements only when the source content is actually a list. Continuous source12 prose is retained as separate prose/headline roots and the missing SWOT prose slot is recorded as a contract gap.


Directly extracted exceptions remain stable across sizes. Legend11 always consists of two small rectangular swatches followed by separate ten-point labels, in vertical reading order. Table19 always uses individual capsule body cells and an unfilled accent-text header; a wide box does not select a rectangular table. Delta20 always uses plain horizontal before/after copy and one fading arrow. Unsupported rectangular table decorations, vertical count connectors and shared multi-row separators are explicit contract gaps, not hidden responsive variants. Miniature source17 line charts own their thin neutral baseline as well as their point-to-point path.
