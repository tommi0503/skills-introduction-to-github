from pathlib import Path
W=Path('/workspace/work/cyanloop');C=Path('/workspace/output/cyanloop')
def css(folder,s):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+'\n'+s)
p=C/'elements/card/element.css';s=p.read_text().replace('.on.quiet:not(.on):not(.line).tone-', '.on.quiet.tone-');p.write_text(s)
css('card','''
.card[data-el="cyanloop-card"].quiet.line{height:181px;margin-top:9px;align-self:start;padding:var(--gap) 0 var(--gap) var(--gap-lg);}
.card[data-el="cyanloop-card"].quiet.line .parts{height:100%;}
.card[data-el="cyanloop-card"].quiet.line .name{white-space:nowrap;}
.card[data-el="cyanloop-card"].on.quiet.tone-3 .note{margin-top:calc(var(--gap-lg)*2);}
''')
css('hub','''
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(5){left:479px;}
.hub[data-el="cyanloop-hub"].quiet.line .core .note{font-family:var(--font-body);font-weight:var(--body-weight);}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(2)::before{transform:rotate(-22deg);transform-origin:right center;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(3)::before{transform:rotate(-8deg);transform-origin:right center;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(4)::before{transform:rotate(8deg);transform-origin:right center;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(5)::before{transform:rotate(22deg);transform-origin:right center;}
''')
css('metric','.stat[data-el="cyanloop-metric"].on .fig{color:var(--a1-6);}')
css('table','.tablebox[data-el="cyanloop-table"].on th{height:70px;}')
css('roadmap','.roadmap[data-el="cyanloop-roadmap"].on .bar{padding:4px;}.roadmap[data-el="cyanloop-roadmap"].on .bar span{font-size:var(--type-16);}')
css('person','.people[data-el="cyanloop-person"].on>.person>:is(.name,.note,.list){z-index:2;}.people[data-el="cyanloop-person"].on>.person>.note .kick{top:calc(30cqh + var(--gap-sm));}')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide.cover .page.at-center .body>.prose{color:var(--page);}
.slide.cover .page.at-center .deco{height:358px;background:radial-gradient(circle at 39px 179px,var(--a2) 0 39px,transparent 40px),conic-gradient(from 90deg,var(--a1-7),var(--a2) 180deg,transparent 180deg);}
.slide.cover .page.at-center::before{background:radial-gradient(circle at 362px 200px,var(--a3) 0 39px,transparent 40px),conic-gradient(from 330deg,var(--a1-7),var(--a3) 120deg,transparent 120deg);}
.slide.cover .page.at-center::after{top:97px;height:401px;background:radial-gradient(circle at 362px 200px,var(--a3-7) 0 39px,transparent 40px),conic-gradient(from 90deg,var(--a3-7),var(--a1-7) 180deg,transparent 180deg);}
.slide.cover .page.at-bottom-left .deco{height:330px;background:radial-gradient(circle at 289px 164px,var(--a3-7) 0 39px,transparent 40px),conic-gradient(from 90deg,var(--a3-7),var(--a1-7) 180deg,transparent 180deg);}
.slide.cover .page.at-bottom-left::before{background:radial-gradient(circle at 196px 336px,var(--a3) 0 39px,transparent 40px),conic-gradient(from 180deg,var(--a3),var(--a1-7) 180deg,transparent 180deg);}
.slide.cover .page.at-bottom-left .foot span{font-weight:var(--body-weight);}
''')
p=W/'reassembly.py';s=p.read_text().replace('--a3:#00eee2;--a3-7:#2bd4c8;}', '--a1-6:#00a9ee;--a3:#00eee2;--a3-7:#2bd4c8;}');p.write_text(s)
# Replica corrections use source SVG vectors, not source bitmaps.
p=W/'replicas.py';s=p.read_text()
s=s.replace("<linearGradient id=\"blue\">", "<linearGradient id=\"blue\" gradientUnits=\"userSpaceOnUse\" x1=\"0\" y1=\"633\" x2=\"1034\" y2=\"633\">")
s=s.replace('<linearGradient id="vert" x1="0" y1="0" x2="0" y2="1">', '<linearGradient id="vert" gradientUnits="userSpaceOnUse" x1="1192" y1="0" x2="1192" y2="461">')
s=s.replace('<circle cx="170" cy="215" r="107"', '<circle cx="213" cy="215" r="100"')
s=s.replace("tx(816,161,'교육 설계부터", "tx(796,161,'교육 설계부터").replace("18,'#111',400,'',400)", "18,'#111',400,'',420)",1)
s=s.replace("x=539 if i==0 else 577", "x=539 if i in(0,3) else 577")
s=s.replace("line(440,y+43,x,y+43,'#888',True)", "line(440,454,x,y+43,'#888',True)")
s=s.replace("th{background:#0753d6;", "th{height:70px;background:#0753d6;")
s=s.replace(".display{font-family:'Anton';", ".display{font-family:'Anton';")
s=s.replace("font-weight:400}\\n\")", "font-weight:400}\\n@font-face{font-family:'Oswald';src:url('Oswald.ttf');font-weight:200 700}\\n\")")
# Source KPI figures are narrower and lighter than its display headings.
s=s.replace("130,cyan,400,'display'", "130,cyan,500,'display thin'")
s=s.replace("48,blue,400,'display'", "48,blue,500,'display thin'")
s=s.replace(".thin{font-weight:400}", ".thin{font-family:'Oswald';font-weight:500}")
p.write_text(s)
