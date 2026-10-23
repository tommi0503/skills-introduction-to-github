from pathlib import Path
import re
C=Path('/workspace/output/glasspulse');R=Path('/workspace/output/glasspulse-review')
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('chart-area','''
.areas[data-el="glasspulse-chart-area"]:has(>.series>.pt>b)>.series{top:calc(var(--gap) + var(--gap-sm));--glasspulse-h:calc(100cqh - var(--gap)*3)}.areas[data-el="glasspulse-chart-area"] .pt{box-shadow:0 0 0 var(--stroke) currentColor;border-radius:50%}.areas[data-el="glasspulse-chart-area"]>.axis>span:last-child{color:var(--a1-7);font-weight:var(--name-weight)}
''')
add('card','''
.card[data-el="glasspulse-card"].quiet>.parts>.mark,.card[data-el="glasspulse-card"].line:has(>.parts>.mark)>.parts>.mark{mask-image:linear-gradient(0deg,color-mix(in srgb,var(--page) 0.001%,var(--page) 0%),var(--page) 65%)}.card[data-el="glasspulse-card"]>.parts:has(>.mark>.icon[data-icon="arrow-down"])>.name{font-weight:var(--title-weight);top:calc(var(--gap)*9 + var(--gap-sm) + var(--gap-sm)/2)}
''')
# The original uses overlapping translucent disks inside an outlined capsule.
add('venn','''
.venn[data-el="glasspulse-venn"]{transform:translateY(calc(var(--gap-sm)*-2))}.venn[data-el="glasspulse-venn"]>.set{margin-left:calc(var(--gap)*-1);background:color-mix(in srgb,var(--n-4) 65%,color-mix(in srgb,var(--page) 0.001%,var(--page) 0%));mix-blend-mode:screen}.venn[data-el="glasspulse-venn"]>.set:first-child{margin-left:0}
''')
# Replica corrections are independent, literal source measurements.
css=R/'replica/replica.css';s=css.read_text();s+='''
[data-page="1"] .title{font-size:96px!important;letter-spacing:1px!important}[data-page="1"] .cap{font-weight:400}
[data-page="2"].slide{background:radial-gradient(ellipse 65% 65% at -10% 100%,#174165,transparent 80%),radial-gradient(ellipse 65% 65% at 110% 100%,#174165,transparent 80%),#000}
[data-page="3"]::before,[data-page="3"]::after{content:"";position:absolute;top:428px;width:35px;border-top:3px dotted #c1c5ca}[data-page="3"]::before{left:426px}[data-page="3"]::after{left:826px}
[data-page="4"]::after{content:"";position:absolute;left:635px;top:596px;width:10px;height:10px;border-radius:50%;background:#38a2fe}[data-page="4"] .logo,[data-page="4"] .deck{color:#111}
[data-page="5"] .cap{min-height:54px;line-height:1;align-items:center}
[data-page="6"] .head .title{transform:translateY(-10px);letter-spacing:-.7px}
[data-page="12"] .panel{border-color:#566472!important;background:linear-gradient(0deg,#17222e,#14191e 26%)!important}[data-page="12"] .panel:nth-of-type(3n){border-color:#348bcb!important;background:#202733!important}
[data-page="14"] .head .title{transform:translateY(-11px)}[data-page="14"] .panel .note{text-align:left}
[data-page="16"] .panel:last-of-type{border-color:#2c6c9c!important;border-radius:14px!important}
[data-page="17"] .panel{background:transparent!important}[data-page="17"] .panel>div>div{opacity:.72;mix-blend-mode:screen}[data-page="17"] .panel::after{content:"";position:absolute;left:100%;top:50%;width:35px;border-top:3px dotted #c1c5ca}
[data-page="18"] .cap{font-weight:400;width:140px;min-width:140px;justify-content:center;padding-left:0;padding-right:0}[data-page="18"] .big{transform:translateY(-4px)}
''';s=s.replace('#339eec','#38a2fe').replace('#349ce9','#38a2fe').replace('#369de9','#38a2fe');css.write_text(s)
# Fix source comparison panels explicitly rather than alternating emphasis.
p=R/'replica/slide-12.html';s=p.read_text();ix=[0]
def panel(m):
 ix[0]+=1;style=m.group(1);style+=';border-color:'+('#348bcb;background:#202733' if ix[0]%2==0 else '#566472;background:linear-gradient(0deg,#17222e,#14191e 26%)');return '<div class="panel " style="'+style+'">'
s=re.sub(r'<div class="panel " style="([^"]*)">',panel,s);p.write_text(s)
# Inline panel selector above is now literal; cancel the old alternating CSS entirely.
s=css.read_text();s=re.sub(r'\[data-page="12"\] \.panel:nth-of-type\(2n\)\{[^}]+\}', '',s);s=re.sub(r'\[data-page="12"\] \.panel\{[^}]+!important[^}]+\}\[data-page="12"\] \.panel:nth-of-type\(3n\)\{[^}]+\}', '',s);css.write_text(s)
# A reusable SVG area plot with the measured vertices.
def svg(w,h,xs,ys,base,labels):
 pts=' '.join(f'{x},{y}' for x,y in zip(xs,ys));poly=f'{xs[0]},{base} '+pts+f' {xs[-1]},{base}'
 return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><linearGradient id="g" x1="0" x2="0" y1="0" y2="1"><stop stop-color="#38a2fe" stop-opacity=".3"/><stop offset="1" stop-color="#38a2fe" stop-opacity="0"/></linearGradient></defs><polygon points="{poly}" fill="url(#g)"/><polyline points="{pts}" fill="none" stroke="#388bcd" stroke-width="1"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="2" fill="#38a2fe"/>' for x,y in zip(xs,ys))+(f'<path d="M6 {base} H{w-5}" stroke="#626d77"/>'+''.join(f'<text x="{x}" y="{h-7}" text-anchor="middle" fill="#c1c5ca" font-size="18" font-family="Pretendard Variable">20XX</text>' for x in xs) if labels else '')+'</svg>'
p=R/'replica/slide-08.html';s=p.read_text();s=re.sub(r'<svg width="603".*?</svg>',svg(603,185,[20,160.75,301.5,442.25,583],[97.5,124.5,83.5,97.5,.5],140,False),s,flags=re.S).replace('left:32px;top:35px;width:603px','left:30px;top:35px;width:603px');p.write_text(s)
p=R/'replica/slide-11.html';s=p.read_text();s=re.sub(r'<svg width="988".*?</svg>',svg(980,275,[20,255,490,725,960],[153,168,121,137,22],235,True),s,flags=re.S).replace('left:48px;top:35px;width:988px','left:52px;top:35px;width:980px').replace('top:585px','top:570px');p.write_text(s)
p=R/'replica/slide-07.html';s=p.read_text();ms=list(re.finditer(r'<text [^>]*>20XX</text>',s));m=ms[-1];t=m.group().replace('fill="#c1c5ca"','fill="#38a2fe" font-weight="700"');s=s[:m.start()]+t+s[m.end():];p.write_text(s)
p=R/'replica/slide-06.html';p.write_text(p.read_text().replace('#339eec','#38a2fe'))
# Restore exact note breaks in the assembled positioning page.
p=Path('/workspace/work/glasspulse/reassemble.py');s=p.read_text().replace("P[14]=(P[14][0]", "P[13]=(P[13][0],P[13][1],P[13][2],P[13][3].replace('해당 장표의 핵심 주제나 요약 내용을 입력해 보세요.','해당 장표의 핵심 주제나<br>요약 내용을 입력해 보세요.'))\nP[14]=(P[14][0]");p.write_text(s)
