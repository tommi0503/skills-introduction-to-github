from pathlib import Path
C=Path('/workspace/output/nightchamfer')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.page::after{z-index:2;mix-blend-mode:screen;background:radial-gradient(ellipse 140% 28% at 50% 105%,var(--a1-6-muted) 0%,var(--a1-3-muted) 48%,var(--a1-1-muted) 72%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) 100%)}.head .kicker>.seat{background:var(--n-7);color:var(--n-4)}\n''')
p=C/'elements/hub/element.css';p.write_text(p.read_text()+'\n[data-el="nightchamfer-hub"]>.spoke{background:var(--n-1)}\n')
p=C/'elements/hierarchy/element.css';p.write_text(p.read_text()+'''\n[data-el="nightchamfer-hierarchy"]>.branch>.leaf{background:var(--n-1)}
@container (min-width:900px) and (min-height:420px){[data-el="nightchamfer-hierarchy"]>.root{font-size:var(--type-22)}[data-el="nightchamfer-hierarchy"]>.branch>.node{font-size:var(--type-20)}[data-el="nightchamfer-hierarchy"]>.branch>.leaf{font-size:var(--type-18)}}\n''')
