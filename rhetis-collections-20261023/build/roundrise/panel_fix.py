from pathlib import Path
B=Path('/workspace/output/roundrise')
for k,root in [('chart-bar','bars'),('chart-area','areas')]:
 p=B/f'elements/{k}/element.css';p.write_text(p.read_text()+f'.{root}[data-el="roundrise-{k}"]{{background-color:var(--page);border-radius:var(--radius);}}')
p=B/'elements/card/element.css';p.write_text(p.read_text()+'''.card[data-el="roundrise-card"]:has(>.parts>:is(.bars,.areas))>.parts{height:100%;display:grid;grid-template-rows:auto minmax(0,1fr);align-content:stretch;gap:var(--gap)}.card[data-el="roundrise-card"]:has(>.parts>:is(.bars,.areas))>.parts>.name{font-size:var(--type-28);min-height:calc(2em*var(--name-line))}''')
p=B/'foundation/foundation.css';p.write_text(p.read_text()+'''.slide.dark .page{background:linear-gradient(var(--a1),var(--a1-2-soft))}.slide.dark .head,.slide.dark .head .title,.slide.dark .head .kicker,.slide.dark .head .lead,.slide.dark .top{color:var(--a1-on)}''')
