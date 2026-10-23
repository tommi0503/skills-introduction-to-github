from pathlib import Path
C=Path('/workspace/output/glasspulse')
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('headline','''
.headline[data-el="glasspulse-headline"].big.center{display:block;position:relative;padding:0}.headline[data-el="glasspulse-headline"].big.center>.kick{display:block;position:absolute;top:calc(var(--gap) - var(--stroke)*4);left:0;right:0;font-size:var(--type-28);line-height:var(--label-line)}.headline[data-el="glasspulse-headline"].big.center>h2{position:absolute;top:calc(var(--gap)*3 - var(--stroke)*3);left:0;right:0;font-size:var(--type-64)}.headline[data-el="glasspulse-headline"]:has(>.seat.back){position:fixed;inset:0;width:100%;height:100%}.headline[data-el="glasspulse-headline"]:has(>.seat.back)>.kick{position:absolute;top:calc(var(--gap)*5);left:0;right:0;margin:0}.headline[data-el="glasspulse-headline"]:has(>.seat.back)>h2{position:absolute;top:calc(var(--gap)*8);left:0;right:0;line-height:var(--body-line)}
''')
add('steps','''
.steps[data-el="glasspulse-steps"]:not(:has(.icon)){justify-content:space-between;padding:0}.steps[data-el="glasspulse-steps"]>.step:not(:has(.icon)){max-width:calc(var(--gap)*11 + var(--gap-sm));height:calc(var(--gap)*11 + var(--gap-sm));align-self:flex-start;flex:none;width:calc((100% - var(--gap)*2)/3)}
''')
# Restore a horizontal panel for the wide metric version while keeping left-side quiet metric bare.
add('card','''
@container (min-width:500px){.card[data-el="glasspulse-card"].quiet:has(>.parts>.mark){border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);padding:var(--pad);height:calc(100% - var(--gap)*1.5);align-self:center}.card[data-el="glasspulse-card"].quiet:has(>.parts>.mark)>.parts>.mark{right:var(--gap);bottom:0}.card[data-el="glasspulse-card"].quiet:has(>.parts>.mark)>.parts>.name{font-size:var(--type-26)}}
.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.stat .parts{display:flex;flex-direction:column;align-items:flex-start}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.stat .parts>.name{justify-content:flex-start;display:block;min-height:0}.card[data-el="glasspulse-card"]:has(>.parts>.stat):has(>.parts>.areas)>.parts>.stat .parts>.fig{text-align:left}
''')
add('callout','''
.callout[data-el="glasspulse-callout"].on{border:var(--stroke) solid var(--a1-3);background:var(--n-1);color:var(--ink);border-radius:var(--radius-sm);height:min(100%,calc(var(--gap)*4));align-self:end;position:relative}.callout[data-el="glasspulse-callout"].on>p{font-size:var(--type-28)}.callout[data-el="glasspulse-callout"].on>p>b{font-size:var(--type-28);color:var(--a1-7)}.callout[data-el="glasspulse-callout"].on::before{content:'';position:absolute;width:calc(var(--gap)*3);height:calc(var(--gap)*3);top:calc(var(--gap)*-2.5);left:60%;background:linear-gradient(0deg,var(--a1) 40%,transparent);clip-path:polygon(5% 0,95% 0,78% 50%,100% 50%,50% 100%,0 50%,22% 50%)}
''')
# Alter only composition data / documented variants.
p=Path('/workspace/work/glasspulse/reassemble.py');s=p.read_text();s=s.replace("for n,(k,t,lead,body) in P.items():",'''P[16]=(P[16][0],P[16][1],P[16][2],P[16][3].replace('class="callout"','class="callout on"'))
for n,(k,t,lead,body) in P.items():''');p.write_text(s)
