from pathlib import Path
C=Path('/workspace/output/glasspulse');W=Path('/workspace/work/glasspulse')
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s+'\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.slide .head.high{transform:translateY(calc(var(--gap-sm)*-1))}.slide .group.two.compact{margin-left:calc(var(--gap-sm)/2 + var(--stroke));width:calc(100% - var(--gap-sm) - var(--stroke)*2)}\n''')
add('headline','''
.headline[data-el="glasspulse-headline"].big.quiet{gap:var(--gap);padding-top:calc(var(--gap)*3 - var(--gap-sm) + var(--stroke)*2)}.headline[data-el="glasspulse-headline"].big.quiet>h2{font-size:var(--type-60);line-height:var(--title-line)}.headline[data-el="glasspulse-headline"].big.quiet>.note{margin-top:0;margin-bottom:0}
''')
add('card','''
.card[data-el="glasspulse-card"]:has(>.parts>.kick):not(:has(>.parts>.fig,>.parts>.mark)){padding:0}.card[data-el="glasspulse-card"]>.parts:has(>.kick):not(:has(>.fig,.mark)){position:relative;display:block;height:100%;width:100%}.card[data-el="glasspulse-card"]>.parts:has(>.kick):not(:has(>.fig,.mark))>.kick{position:absolute;top:var(--gap-lg);left:50%;transform:translateX(-50%);color:var(--a1-7);min-height:calc(var(--gap)*1.5 + var(--stroke)*3);display:flex;align-items:center;justify-content:center;font-size:var(--type-24)}.card[data-el="glasspulse-card"]>.parts:has(>.kick):not(:has(>.fig,.mark))>.name{position:absolute;left:var(--gap);right:var(--gap);top:calc(var(--gap)*4 + var(--gap-sm));font-size:var(--type-36);line-height:var(--name-line);min-height:0}.card[data-el="glasspulse-card"]>.parts:has(>.kick):not(:has(>.fig,.mark))>.note{position:absolute;left:var(--gap-lg);right:var(--gap-lg);top:calc(var(--gap)*7 + var(--stroke)*2);max-width:none;padding-top:var(--gap-lg);font-size:var(--type-22);line-height:var(--body-line);min-height:0;text-align:left}.card[data-el="glasspulse-card"] .kick{justify-content:center;align-items:center}.card[data-el="glasspulse-card"].on:not(:has(.fig,.kick,.mark)){transform:translateY(calc(var(--gap-sm)*-2))}
''')
add('venn','.venn[data-el="glasspulse-venn"]{transform:translateY(calc(var(--gap-sm)*-1))}\n')
p=W/'reassemble.py';s=p.read_text().replace("[(17,64,'A사'),(34,9,'B사'),(71,23,'C사'),(88,79,'미리컴퍼니')]","[(15,70,'A사'),(32,15,'B사'),(69,29,'C사'),(86,85,'미리컴퍼니')]")
s=s.replace('else "center low" if n==14 else "center"','else "center low" if n==14 else "center high" if n==11 else "center"')
s=s.replace('for n,(k,t,lead,body) in P.items():','''P[14]=(P[14][0],P[14][1],P[14][2],P[14][3].replace('이곳에 해당 주제에 맞는 하반기 핵심 전략 방향을 요약하여 입력해 보세요','이곳에 해당 주제에 맞는<br>하반기 핵심 전략 방향을<br>요약하여 입력해 보세요'))
for i in [15,16]:P[i]=(P[i][0],P[i][1],P[i][2],P[i][3].replace('class="headline "','class="headline big quiet"'))
for n,(k,t,lead,body) in P.items():''');p.write_text(s)
p=C/'foundation/description.md';s=p.read_text();s=s.split('가로 제목 공용 변형:')[0];s+='Shared heading variants: `.head.low` offsets an inline heading by 26px; `.head.mid` by 14px; `.head.center.low` offsets the centered heading by 18px; `.head.high` moves the heading upward by 12px without changing body placement. `.stack.tight` uses an 18px member gap. `.stack.compact` uses three 112px comparison rows with a 28px gap. `.group.two.compact` uses two 213px rows for landscape goal cards. These modifiers preserve the page/head/body grid structure.\n';p.write_text(s)
