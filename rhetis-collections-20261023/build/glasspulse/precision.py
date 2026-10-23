from pathlib import Path
C=Path('/workspace/output/glasspulse');W=Path('/workspace/work/glasspulse')
def add(f,s):
 p=C/f'elements/{f}/element.css';p.write_text(p.read_text()+'\n'+s+'\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide .head.low:not(.center){padding-top:calc(var(--gap)*2 - var(--stroke))}.slide .head.mid:not(.center){padding-top:calc(var(--gap)*1.5)}.slide .head.low.center{padding-top:calc(var(--gap-sm)*1.5)}
''')
add('headline','''
.headline[data-el="glasspulse-headline"]:not(.center){gap:var(--gap-sm)}.headline[data-el="glasspulse-headline"]:not(.big):not(.center)>h2{font-size:var(--type-52)}.headline[data-el="glasspulse-headline"]:not(.center)>.note{margin-top:var(--gap-sm)}.headline[data-el="glasspulse-headline"].big:not(.center)>h2{line-height:var(--name-line)}.headline[data-el="glasspulse-headline"].big:not(.center)>.note{margin-top:auto}
''')
add('prose','''
.prose[data-el="glasspulse-prose"].lead:has(p>br){justify-content:flex-start;padding:0 calc(var(--gap-sm)*1.5);transform:translateY(calc(var(--gap-sm)*-0.5))}.prose[data-el="glasspulse-prose"].lead:has(p>br)>p{font-size:var(--type-40);line-height:var(--lead-line);color:var(--n-7)}.prose[data-el="glasspulse-prose"].lead p strong{font-weight:var(--name-weight);color:var(--ink)}
''')
r='.card[data-el="glasspulse-card"]:has(>.parts>.areas):not(:has(>.parts>.stat))'
add('card',f'''
{r}{{width:calc(100% - var(--gap-sm)*2);margin-left:calc(var(--gap-sm) - var(--stroke));height:min(100%,calc(var(--gap)*18 + var(--gap-sm)));transform:translateY(calc(var(--stroke)*4));padding:0}}{r}>.parts{{position:relative;display:block;height:100%;width:100%}}{r}>.parts>.areas{{position:absolute;left:calc(var(--gap)*2 - var(--gap-sm) + var(--stroke));top:calc(var(--gap) - var(--stroke)*2);width:calc(100% - var(--gap)*3 - var(--gap-sm));height:calc(var(--gap)*12);border:0;background:none;box-shadow:none}}{r}>.parts>.areas>.series{{left:calc(var(--gap-sm)*1.5);right:calc(var(--gap-sm)*1.5);top:calc(var(--gap) - var(--stroke));bottom:calc(var(--gap)*1.5 + var(--stroke)*2);--glasspulse-h:calc(100cqh - var(--gap)*2.5)}}{r}>.parts>.areas>.axis{{bottom:calc(var(--gap-sm)/2);left:0;right:0}}{r}>.parts>.areas>.axis span{{font-size:var(--type-18)}}{r}>.parts>.callout{{position:absolute;left:calc(var(--pad)*2 + var(--stroke)*2);top:calc(var(--gap)*14 - var(--stroke)*2);width:calc(100% - var(--pad)*4 - var(--stroke)*4);height:calc(var(--gap)*3);padding:0}}{r}>.parts>.callout p{{font-size:var(--type-36)}}{r}>.parts>.callout b{{font-size:var(--type-56)}}
''')
add('chart-area','''
.areas[data-el="glasspulse-chart-area"]:has(.series>.name){height:min(100%,calc(var(--gap)*8 + var(--gap-sm) + var(--stroke)*2))}.areas[data-el="glasspulse-chart-area"]:has(.series>.name)>.series{left:calc(var(--gap)*2 - var(--stroke)*2);right:calc(var(--gap)*2 - var(--stroke)*2);top:calc(var(--gap-sm) + var(--stroke)*2);bottom:calc(var(--gap) + var(--gap-sm));--glasspulse-h:calc(100cqh - var(--gap)*2 - var(--stroke)*1.5)}.areas[data-el="glasspulse-chart-area"]:has(.series>.name) .series>.name{top:calc(var(--gap-sm)*2);font-size:var(--type-28);font-weight:var(--label-weight)}
''')
# Measured card internals use existing title/figure/note roles.
r='.card[data-el="glasspulse-card"]:has(>.parts>.mark>.icon[data-icon="arrow-down"])'
add('card',f'''
{r}{{padding:0;height:min(100%,calc(var(--gap)*16 + var(--stroke)*2));transform:translateY(calc(var(--gap-sm)*-1))}}{r}>.parts{{position:relative;display:block;height:100%}}{r}>.parts>.kick{{position:absolute;left:var(--gap);top:calc(var(--gap-sm)*1.5);height:calc(var(--gap)*1.5 + var(--stroke)*4);display:flex;align-items:center;justify-content:center}}{r}>.parts>.note{{position:absolute;left:var(--gap);right:var(--gap);top:calc(var(--pad)*2);font-size:var(--type-36);line-height:var(--label-line)}}{r}>.parts>.mark{{position:absolute;left:50%;top:calc(var(--gap)*5 - var(--stroke)*2);transform:translateX(-50%);height:calc(var(--gap)*4 + var(--gap-sm))}}{r}>.parts>.name{{position:absolute;left:var(--gap);right:var(--gap);top:calc(var(--gap)*9 + var(--gap-sm));font-size:var(--type-44);line-height:var(--name-line)}}
''')
add('card','''
.card[data-el="glasspulse-card"]>.parts:has(>.kick):not(:has(>.fig,.mark)){gap:var(--gap)}.card[data-el="glasspulse-card"]:has(>.parts>.kick):not(:has(>.parts>.fig,>.parts>.mark)){height:min(100%,calc(var(--gap)*14 + var(--gap-sm) + var(--stroke)));margin-top:calc(var(--gap-sm)/2);padding:var(--gap)}.card[data-el="glasspulse-card"]>.parts:has(>.kick):not(:has(>.fig,.mark))>.note{text-align:left;max-width:12em;font-size:var(--type-22);line-height:var(--body-line)}
@container (min-width:600px) and (max-height:180px){.card[data-el="glasspulse-card"]>.parts:not(:has(.fig,.kick,.mark)){grid-template-columns:27% 1fr;gap:calc(var(--gap)*2)}.card[data-el="glasspulse-card"]>.parts:not(:has(.fig,.kick,.mark))>.note{font-size:var(--type-24)}.card[data-el="glasspulse-card"]>.parts:not(:has(.fig,.kick,.mark))>.name{height:calc(var(--gap)*3 + var(--gap-sm));font-size:var(--type-32)}.card[data-el="glasspulse-card"] .note .icon{width:var(--gap);height:var(--gap);vertical-align:middle;color:var(--a1-7);margin-right:var(--gap-sm)}}
''')
# Portrait sequence keeps its own role line before the two-line name.
add('person','''
.person[data-el="glasspulse-person"]:has(>.seat.portrait){position:relative;display:block;padding:0}.person[data-el="glasspulse-person"]:has(>.seat.portrait)>.seat{position:absolute;left:calc(var(--gap-sm)*1.5);top:calc(var(--gap-sm)*1.5);width:calc(100% - var(--gap-sm)*3);height:auto;aspect-ratio:1.05}.person[data-el="glasspulse-person"]:has(>.seat.portrait)>.role{position:absolute;top:calc(var(--gap)*9 + var(--gap-sm)/2);left:var(--gap-sm);right:var(--gap-sm);font-size:var(--type-18);line-height:var(--label-line);color:var(--a1-7)}.person[data-el="glasspulse-person"]:has(>.seat.portrait)>.name{position:absolute;top:calc(var(--gap)*10 + var(--gap-sm));left:var(--gap-sm);right:var(--gap-sm);font-size:var(--type-30);line-height:var(--name-line)}.person[data-el="glasspulse-person"]:has(>.seat.portrait)>.note{position:absolute;top:calc(var(--gap)*14 + var(--gap-sm)/2);left:var(--gap);right:var(--gap);padding-top:var(--gap);font-size:var(--type-18);line-height:var(--body-line)}
''')
add('steps','.steps[data-el="glasspulse-steps"]:has(.icon[data-icon="circle-check"]){transform:translateY(calc(var(--gap) - var(--stroke)*4))}\n')
add('callout','.callout[data-el="glasspulse-callout"].on{transform:translateY(calc(var(--pad)*-1))}.callout[data-el="glasspulse-callout"].quiet{transform:translateY(calc(var(--gap)*-0.75))}\n')
# Refined quadrant axes and coordinate mapping, independent of content labels.
add('positioning','''
.posmap[data-el="glasspulse-positioning"]{width:calc(100% - var(--gap-sm)*2 + var(--stroke));height:min(100%,calc(var(--gap)*19 - var(--stroke)*2))}.posmap[data-el="glasspulse-positioning"]::before{left:calc(var(--gap)*2 - var(--stroke)*2);right:calc(var(--gap)*2 - var(--stroke)*2);top:50%}.posmap[data-el="glasspulse-positioning"]::after{top:calc(var(--gap)*3 - var(--gap-sm));bottom:calc(var(--gap)*3 - var(--gap-sm));left:50%}.posmap[data-el="glasspulse-positioning"]>.axis-x{left:calc(var(--gap)*2 - var(--stroke)*2);right:calc(var(--gap)*2 - var(--stroke)*2);top:calc(50% + var(--gap-sm));font-size:var(--type-16)}.posmap[data-el="glasspulse-positioning"]>.axis-y{top:var(--gap);bottom:var(--gap);font-size:var(--type-16)}.posmap[data-el="glasspulse-positioning"]>.mark{left:calc(var(--gap)*2 - var(--stroke)*2 + (100% - var(--gap)*4 + var(--stroke)*4)*var(--x)/100);bottom:calc(var(--gap)*3 - var(--gap-sm) + (100% - var(--gap)*6 + var(--gap-sm)*2)*var(--y)/100);font-size:var(--type-18)}.posmap[data-el="glasspulse-positioning"]>.mark.on::before{width:var(--pad);height:var(--pad);box-shadow:0 0 0 calc(var(--gap) - var(--stroke)*2) var(--a1-3)}.posmap[data-el="glasspulse-positioning"]>.mark.on{gap:var(--gap);font-size:var(--type-22)}
''')
add('venn','.venn[data-el="glasspulse-venn"]::after{content:"";position:absolute;left:calc(100% + var(--gap-sm));top:50%;width:var(--gap);border-top:var(--stroke) dotted var(--n-7)}\n')
# Compact landscape summary keeps the capsule tall and optically centered.
add('card','''
@container (min-width:400px) and (max-width:600px) and (max-height:240px){.card[data-el="glasspulse-card"]>.parts:has(>.kick):has(>.fig):not(:has(>.note))>.kick{width:calc(var(--gap)*5);min-height:calc(var(--gap)*2);padding:var(--gap-sm);font-size:var(--type-24);border-color:var(--a1)}.card[data-el="glasspulse-card"]>.parts:has(>.kick):has(>.fig):not(:has(>.note))>.name{font-size:var(--type-32)}.card[data-el="glasspulse-card"]>.parts:has(>.kick):has(>.fig):not(:has(>.note))>.fig{font-size:var(--type-64)}}
''')
# Data and existing contract role markup only.
p=W/'reassemble.py';s=p.read_text().replace("'--a1':'#349cea'","'--a1':'#3aa1ff'").replace("else:val='#349cea'","else:val='#3aa1ff'")
s=s.replace('한 번 함께한<br>고객은 <b>미리컴퍼니<br>서비스에 만족해<br>다시 돌아</b>옵니다.','한 번 함께한<br>고객은 <b>미리컴퍼니<br>서비스</b>에 <strong>만족해<br>다시 돌아</strong>옵니다.').replace('area([35,20,43,35,89],','area([36,21,43.5,36,89],')
s=s.replace("f'<div class=\"seat portrait\" data-ph=\"{i}\"></div><b class=\"name\">{t}</b><p class=\"note\">overview. 0{i}<br>","f'<div class=\"seat portrait\" data-ph=\"\"></div><p class=\"role\">overview. 0{i}</p><b class=\"name\">{t}</b><p class=\"note\">" )
s=s.replace('[(20,70,\'A사\'),(35,25,\'B사\'),(68,40,\'C사\'),(82,85,\'미리컴퍼니\')]',"[(17,64,'A사'),(34,9,'B사'),(71,23,'C사'),(88,79,'미리컴퍼니')]")
s=s.replace('head=f\'<header class="head {"" if n in [9,12,17,18] else "center"}">\'', 'head=f\'<header class="head {"low" if n in [12,17] else "mid" if n==18 else "" if n==9 else "center low" if n==14 else "center"}">\'')
insert='''
# Original team proof points retain their check marks and selective emphasis.
checks=[('영업팀','신규 계약 000건 / <b>목표 대비 00% 달성</b>'),('마케팅팀','리드 000건 / <b>캠페인 00개 집행</b>'),('운영팀','고객 만족도 00점 / <b>처리 건수 000건</b>')]
P[9]=(P[9][0],P[9][1],P[9][2],group([card(t,'','<span class="icon" data-icon="check"></span>'+n+'<br><span class="icon" data-icon="check"></span>이곳에 각 팀별 핵심 성과 키워드 수치를 입력해 보세요.','') for t,n in checks],(1,12,1,6),'stack'))
'''
s=s.replace('for n,(k,t,lead,body) in P.items():',insert+'\nfor n,(k,t,lead,body) in P.items():')
p.write_text(s)
