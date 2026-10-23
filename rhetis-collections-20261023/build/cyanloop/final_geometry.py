from pathlib import Path
W=Path('/workspace/work/cyanloop');C=Path('/workspace/output/cyanloop')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide .page.overrides .head:has(.label) .title .label{width:calc-size(max-content,size * .86);flex:none;}
.slide .page.overrides .head:has(.label) .title .lead{margin-left:0;}
.slide .page.overrides .head:has(.label) .title .lead::before{content:'|';margin-right:var(--gap-sm);}
.slide.cover .page.at-center::before{z-index:1;}
''')
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'''\n.prose[data-el="cyanloop-prose"].on{justify-content:flex-start;padding-top:var(--gap-sm);border-right:var(--stroke) solid var(--n-5);}.prose[data-el="cyanloop-prose"].on p{font-size:var(--type-24);}\n''')
p=C/'elements/agenda/element.css';p.write_text(p.read_text()+'''
.agenda[data-el="cyanloop-agenda"].quiet .entry>.note .list{display:flex;flex-direction:column;gap:calc(var(--gap-sm)/3);justify-content:flex-start;}
.agenda[data-el="cyanloop-agenda"].quiet .entry>.note .item{padding-left:var(--gap);}
.agenda[data-el="cyanloop-agenda"].quiet .entry>.note .item::before{left:0;top:var(--gap-sm);background:var(--n-9);}
.agenda[data-el="cyanloop-agenda"].quiet .entry>.note .item .name{font-size:var(--type-20);font-weight:var(--body-weight);color:var(--n-9);}
.agenda[data-el="cyanloop-agenda"].quiet.line .entry>.name{position:relative;padding-left:var(--gap);font-weight:var(--body-weight);}
.agenda[data-el="cyanloop-agenda"].quiet.line .entry>.name::before{content:'';position:absolute;left:0;top:var(--gap-sm);width:6px;height:6px;border-radius:50%;background:var(--page);}
''')
p=W/'reassembly.py';s=p.read_text().replace('if n not in (1,2,3,6,18) else titles[n-1]', 'if n not in (1,2,3,18) else titles[n-1]')
s=s.replace("'<div class=\"note\">'+b+'</div></div>'", "'<div class=\"note\">'+listel([(v,'') for v in b.split('<br>')])+'</div></div>'")
p.write_text(s)
