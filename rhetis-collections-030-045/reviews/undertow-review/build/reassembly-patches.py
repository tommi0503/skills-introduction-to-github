from pathlib import Path
C=Path('work/deliverables/undertow');R=Path('work/deliverables/undertow-review')
def add(n,t):p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n'+t)
add('steps','''.steps[data-el="undertow-steps"]:has(> .step:nth-child(3):last-child):not(.col) .step { grid-template-rows:200px auto 1fr; }
.steps[data-el="undertow-steps"]:has(> .step:nth-child(3):last-child):not(.col) .mark { width:200px; height:200px; font-size:var(--type-32); }
@container (max-width:800px) { .steps[data-el="undertow-steps"]:has(> .step:nth-child(3):last-child):not(.col) .step { grid-template-rows:96px auto 1fr; } .steps[data-el="undertow-steps"]:has(> .step:nth-child(3):last-child):not(.col) .mark { width:96px; height:96px; font-size:var(--type-20); } }
''')
root='.hub[data-el="undertow-hub"]:has(> .spoke:nth-child(4 of .spoke):last-child)'
add('hub',root+' { grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:repeat(2,minmax(0,1fr)); }\n'+root+' .core { position:absolute; left:50%;top:50%;transform:translate(-50%,-50%);width:min(34%,280px); }\n'+root+' .core .name {font-size:var(--type-24);}\n'+''.join(root+f' .spoke:nth-child({i} of .spoke) {{ grid-area:{a}/{b};text-align:{"left" if b==1 else "right"};align-items:{"flex-start" if b==1 else "flex-end"};padding:var(--pad);}}\n' for i,(a,b) in enumerate([(1,1),(1,2),(2,1),(2,2)],1))+root+' .spoke .note {width:70%;}\n@container (max-width:700px) { '+root+' .spoke .note {font-size:var(--type-12);} '+root+' .core .name {font-size:var(--type-16);} '+root+' .core .note {font-size:var(--type-10);} }')
add('person','''.people[data-el="undertow-person"] .person .seat.portrait { width:100%; max-height:200px; }
.person[data-el="undertow-person"] .note b {display:block;background:var(--n-6);color:var(--page);padding:var(--gap-sm);margin-top:var(--gap-sm);font-weight:var(--label-weight);}
''')
p=Path('work/agents/031/reassemble.py');s=p.read_text();s=s.replace("slides[4]=head(4,'PROBLEM','해결하려는 문제의 핵심을 간결하게 정의하세요.','02 │ 시장의 문제점')", "slides[4]='<section class=\"slide\"><div class=\"page\"><div class=\"top\"><span>02 │ 시장의 문제점</span><b>MIRI COMPANY</b></div><div class=\"rail\">투자 유치를 위한 IR 덱 상세 템플릿<span>02</span></div><div class=\"body\">'")
s=s.replace("(1,5,1,6))+group(''.join(card(f'[ 문제점", "(1,5,1,3),'big')+group(''.join(card(f'[ 문제점")
s=s.replace('현재 담당 업무와 전문 분야를 간단하게 소개해 주세요. 현재 담당 업무와 전문 분야를 간단하게 소개해 주세요.','현재 담당 업무와 전문 분야를 간단하게 소개해 주세요. 현재 담당 업무와 전문 분야를 간단하게 소개해 주세요.<b>핵심 메시지 한 줄로 입력</b>')
s=s.replace('<body>\'+body+\'</body>','<body>\'+body+\'<script src="../icons.js"></script></body>')
p.write_text(s)
