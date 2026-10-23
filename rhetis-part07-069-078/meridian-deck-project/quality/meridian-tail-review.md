# Meridian Deck 25–29 fidelity restoration

Five original/replica/reassembled comparisons were opened individually. The previous reassemblies changed component proportions and omitted source structures. Automatic overflow results were not used as evidence of fidelity.

The integration agent owns only reassembled HTML 25–29 and `meridian-deck-project/fidelity_tail_patch.py`. Shared CSS is merged and normalized by the collection owner. No new page class, page-local CSS, or inline position/size escape was added to HTML. The body remains the foundation's 12×6 grid; composition wrappers and contracted nested elements supply the rest.

| Page | Actual source structure restored | Native 1280×720 reference targets |
|---|---|---|
| 25 | Four neutral category capsules with actual three-item lists; compact title capsule; continuous-gradient positioning map with all four original two-line labels | Categories x94/y205,323,441,559; map x551/y273/633×324; map labels 89×40; title x767/y202/188×39 |
| 26 | Full two-line heading; four neutral-to-accent keyword capsules, two-line descriptions and four 80/70/75/91 one-share donuts | Donuts x102,396,690,984/y437/192×192; capsules y307/192×41; descriptions y365 |
| 27 | Three bordered image seats with geometric plus badges and three flat text panels; all three lines of body copy retained | Frames x95,472,849/y228/350×203; panels y439/350×164; titles y456 and separators y491 |
| 28 | Two captions on the upper timeline; four connected chevron headers; two observations in each detail panel; 2→5 expansion, AI pair, carrier-to-A/B/C hierarchy, shipping pair; rectangular investment/effect conclusion | Timeline y195; headers y227/44h; panels y280/275h; component top y385; footer x83/y561/1115×72 |
| 29 | Full heading and sample-photo note; four source-sized image seats; department/name/role text with separators | Image seats x62,361,660,959/y248/262×218; department y495; separator y566; role text y582 |

The provisional Chromium probe measured the new source 26 donut boxes, 27 frame/card boxes and 29 portrait boxes at these exact target coordinates. It also exposed and led to repair of the old delta arrow leaking beside the new vertical 2→5 diagram, chevron gaps, badge offset, paragraph line-height and role-text spacing.

Remaining intentional interpretation: source media is replaced by light gray seats with centered `data-ph` numbers under the library contract. The source's 27px percent unit uses the closest allowed 28px typography step. The library's CSS continues to refer to palette roles; original blue gradient colors must be mapped by the separate source-palette provider, not hardcoded into collection CSS. Shared header furniture and final normalized CSS require the collection owner's final render before acceptance.

`meridian-tail-25…29-compare.png` are provisional original-versus-assembly diagnostics using in-memory CSS before the owner's merge. They are not the final delivery renders.

The first merged-source render revealed two integration regressions that were absent in the in-memory isolated patch: the existing three-column KPI wrapper added 37px horizontal and 22px vertical padding to page 27, and a percentage/min height cycle reduced page 29's size-contained person boxes to zero, activating the compact note-hiding rule. The handoff module was narrowed to the image-frame composition signature, explicitly reset wrapper padding, and assigned a definite grid row plus 100% person heights. These fixes require re-merge and targeted verification; the first merged PNGs are retained as diagnostic evidence, not accepted output.

After re-merge, the targeted actual-source page 27 and 29 browser renders restored the target frame/card boxes and all four 390px person boxes; names and role descriptions were visible again. One residual KPI wrapper `overflow:hidden` still clipped page 27's intentionally protruding plus badge. The tail wrapper now explicitly requests `overflow:visible` and zero corner radius, communicated for final merge. Gray image replacements retain centered numbers per the seat contract.

Final targeted page 27 render used the merged collection CSS without injected styles. The protruding plus badges are fully visible after the wrapper overflow reset, and the measured frame/card positions remain at the reference targets. Page 29's restored names and role descriptions were verified in the prior actual-source targeted render. HTML/module ownership was returned to the Meridian collection owner; the integration agent resumes read-only independent QA. Module SHA-256 at handoff: `b3cbe5c310b0236afd09be2df1b0287d4976b978fab51945426b62c89203db7b`.
