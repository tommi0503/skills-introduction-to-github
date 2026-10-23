from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck'
f=C/'elements/headline/element.css';f.write_text(f.read_text().replace('font-weight:inherit','font-weight:var(--meridian-deck-font-weight-650)'))
f=C/'elements/hub/element.css';s=f.read_text();start=s.rfind('/* FINAL FIDELITY DETAIL */');s=s[:start]+s[start:].replace(':has(>.spoke:nth-child(5):last-child)',':has(>.spoke:nth-child(4 of .spoke):last-child)');f.write_text(s)
f=C/'elements/chart-area/element.css';f.write_text(f.read_text()+'''\n.split.wide-left>.group:first-child>[data-el="meridian-deck-chart-area"]::after{top:-14px;content:counter(maximum) "\\A" counter(upper) "\\A" counter(middle) "\\A" counter(lower) "\\A" "0"}.split.wide-left>.group>[data-el="meridian-deck-chart-area"] .pt::before{background:color-mix(in srgb,currentColor 30%,var(--page))}\n''')
print('Microfixes: inherited weight, ruled hub, area axis/opaque fill')
