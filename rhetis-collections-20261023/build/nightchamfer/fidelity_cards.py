from pathlib import Path
p=Path('/workspace/work/nightchamfer/reassemble.py');t=p.read_text()
# Replace source-page card slots with the canonical card .mark image seat.
start=t.index("contents.append(group([innercard('업무 맥락");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append(group([f'<div class="card" data-el="nightchamfer-card"><div class="parts"><span class="mark"><span class="seat icon" data-ph="{i}"></span></span><b class="name">{n}</b><p class="note">{d}</p></div></div>' for i,(n,d) in enumerate([('업무 맥락 이해','우리 팀의 문서·대화를 바탕으로<br>맥락에 맞게 답변'),('끊김 없는 통합','업무 데이터를 외부 학습에<br>쓰지 않고 격리 처리'),('안전한 보안','미리워크 안에서 앱 전환 없이<br>곧바로 사용')],1)]))'''+t[end:]
start=t.index("contents.append(group([innercard('신규 매출'");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append(group([f'<div class="card" data-el="nightchamfer-card"><div class="parts"><p class="kick">Benefit 0{i}</p><b class="name">{n}</b><span class="mark"><span class="seat icon" data-ph="{i}"></span></span><p class="note">{d}</p></div></div>' for i,(n,d) in enumerate([('신규 매출','기존 유료 고객의 25%가 AI 애드온을<br>추가 구독해, 신규 획득 비용 없이 하반기<br>30억 원의 추가 매출을 확보합니다.'),('고객 생산성 향상','반복 업무를 자동화해 팀당 주 5시간<br>이상을 절감합니다. 고객 만족도와<br>재구독률 (리텐션) 상승으로 이어집니다.'),('경쟁 우위',"'AI가 내장된 협업툴'이라는 차별화로 신규<br>가입 전환을 끌어올리고, 전환 비용을 높여<br>고객 이탈을 방어합니다.")],1)]))'''+t[end:];p.write_text(t)
C=Path('/workspace/output/nightchamfer');p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.group:has(>.card .mark>.seat.icon):has(>.card:nth-child(3):last-child){gap:40px}.group:has(>.card .mark>.seat.icon):has(>.card:nth-child(3):last-child):not(:has(.kick)){gap:54px}\n''')
p=C/'elements/card/element.css';s='[data-el="nightchamfer-card"]';p.write_text(p.read_text()+f'''
{s}:has(.mark>.seat.icon){{border:0;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);isolation:isolate}}
{s}:has(.mark>.seat.icon)>.parts::before{{content:"";position:absolute;inset:0;z-index:-1;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:var(--n-1)}}
@container (min-width:250px) and (min-height:350px){{
{s}:has(.mark>.seat.icon)>.parts{{position:absolute;inset:0;display:block}}
{s}:has(.mark>.seat.icon)>.parts::before{{inset:44px 0 29px}}
{s}:has(.mark>.seat.icon)>.parts>.name{{position:absolute;left:36px;top:79px;width:auto;max-width:calc(100% - 60px);min-height:43px;height:auto;display:flex;align-items:center;font-size:var(--type-20);line-height:var(--label-line);padding:calc(var(--gap-sm)/2) var(--gap-sm);background:var(--n-2)}}
{s}:has(.mark>.seat.icon)>.parts>.note{{position:absolute;left:40px;right:20px;top:147px;font-size:var(--type-20);line-height:var(--body-line);text-align:left;min-height:0}}
{s}:has(.mark>.seat.icon)>.parts>.mark{{position:absolute;left:calc(100% - 176px);top:254px;width:135px;height:143px;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);border-radius:var(--radius-sm)}}
{s}:has(.mark>.seat.icon)>.parts>.mark>.seat.icon{{width:135px;height:143px;max-height:none;background:var(--n-7);color:var(--n-4);font-size:var(--type-16)}}
{s}:has(.mark>.seat.icon):has(.kick)>.parts::before{{inset:39px 0 27px}}
{s}:has(.mark>.seat.icon):has(.kick)>.parts>.kick{{position:absolute;left:0;right:0;top:77px;font-size:var(--type-16);line-height:var(--label-line);text-align:center}}
{s}:has(.mark>.seat.icon):has(.kick)>.parts>.name{{left:0;right:0;top:113px;min-height:0;max-width:none;width:100%;padding:0;font-size:var(--type-24);text-align:center;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%)}}
{s}:has(.mark>.seat.icon):has(.kick)>.parts>.mark{{left:50%;top:165px;transform:translateX(-50%);width:123px;height:123px}}
{s}:has(.mark>.seat.icon):has(.kick)>.parts>.mark>.seat.icon{{width:123px;height:123px}}
{s}:has(.mark>.seat.icon):has(.kick)>.parts>.note{{left:18px;right:18px;top:313px;font-size:var(--type-18);line-height:var(--body-line);text-align:center}}
}}
''')
