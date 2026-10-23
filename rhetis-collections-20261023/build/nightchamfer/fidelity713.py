from pathlib import Path
C=Path('/workspace/output/nightchamfer');p=Path('/workspace/work/nightchamfer/reassemble.py');t=p.read_text()
start=t.index("contents.append(card('미리워크 사용 팀'");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append(el('card','card','<div class="parts"><span class="mark"><span class="seat logo" data-ph="1"></span></span><b class="name">미리워크 사용 팀</b><b class="fig">120,000</b><div class="note">'+el('gauge','meter','<b class="name">AI 미사용 고객</b><b class="fig"></b>',data=';--v:50')+el('gauge','meter','<b class="name">AI 사용 고객</b><b class="fig"></b>',data=';--v:100')+'</div></div>',1,1,12,3)+el('card','card quiet','<div class="parts"><b class="name">주요 타깃: 반복 업무가 많은 운영·기획 팀</b><div class="note">'+items([('회의·문서 작업 비중이 높음',''),('인력 대비 업무량이 과다',''),('AI 도입 의향은 높으나 진입 장벽을 느낌',''),('이곳에 주요 타깃 특징에 대한 내용을 작성해주세요.','')])+'</div></div>',1,3,6,4)+el('card','card quiet','<div class="parts"><b class="name">이곳에 고객 분석 페인포인트를 작성하세요.</b><div class="note">'+items([('시간 낭비','회의록·보고서 정리에 반복적으로<br>시간 소모된 시간을 작성해보세요'),('도구 이중화','별도 AI 툴을 따로 쓰며 미리워크와는<br>단절된 데이터 도출')])+'</div></div>',7,3,6,4))'''+t[end:]
start=t.index("contents.append('<div class=\"stack\"");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append('<div class="stack" style="'+grid(1,1,5,6)+'">'+innercard('AI 서비스 신규 매출','이곳에 해당 수치<br>관련 상세 내용을<br>입력해 보세요.','30억 원')+innercard('유료 고객 비율','이곳에 해당 수치<br>관련 상세 내용을<br>입력해 보세요.','25%')+'</div>'+el('card','card','<div class="parts"><b class="name">객단가 상승</b><div class="note"><p>AI 도입 전 대비<br>330% 상승</p>'+el('chart-bar','bars','<div class="bar" style="--v:15"><b>월 약1.5만 원</b><span>도입 전</span></div><div class="bar on" style="--v:50"><b>월 약5만 원</b><span>도입 후</span></div>',data=';--max:50')+'</div></div>',6,1,7,6))'''+t[end:]
t=t.replace("body=top+(f'<header", "body=top+(f'<header")
# Inline source head for the two compact header pages, preserving the foundation's title and label parts.
needle="html=f'<!doctype html>"
pos=t.index(needle)
t=t[:pos]+'''if i in (7,13):
  old=f'<header class="head"><p class="kicker"><span class="seat avatar" data-ph="1"></span></p><h1 class="title">{t}</h1><p class="lead">{l}</p></header>'
  new=f'<header class="head"><p class="kicker"><span class="seat avatar" data-ph="1"></span></p><h1 class="title">{t} <span class="label">{l}</span></h1></header>'
  body=body.replace(old,new)
 '''+t[pos:];p.write_text(t)
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.head .title>.label{font-size:var(--type-20);font-weight:var(--body-weight);line-height:var(--lead-line);letter-spacing:var(--body-track);color:var(--n-7);margin-left:32px}.stack:has(>.card .fig){padding:36px 5px 18px 10px;gap:26px}\n''')
p=C/'elements/card/element.css';s='[data-el="nightchamfer-card"]';p.write_text(p.read_text()+f'''
{s}:has(.meter){{border:0;background:none}}{s}:has(.meter)>.parts{{position:absolute;inset:22px 8px auto;height:162px;display:block}}
{s}:has(.meter)>.parts::before{{content:"";position:absolute;inset:0;z-index:-1;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:var(--n-1)}}
{s}:has(.meter)>.parts>.mark{{position:absolute;left:28px;top:24px;width:124px;height:112px;background:none;border-radius:var(--radius-sm)}}{s}:has(.meter)>.parts>.mark>.seat{{width:124px;height:112px;background:var(--n-7);color:var(--n-4);max-height:none}}
{s}:has(.meter)>.parts>.name{{position:absolute;left:190px;top:41px;background:none;padding:0;min-height:0;font-size:var(--type-22)}}
{s}:has(.meter)>.parts>.fig{{position:absolute;left:191px;top:76px;font-size:var(--type-40);line-height:var(--figure-line);color:var(--ink)}}
{s}:has(.meter)>.parts>.note{{position:absolute;left:481px;right:66px;top:37px;display:flex;flex-direction:column;gap:16px;min-height:0;max-width:none}}
{s}:has(.meter)>.parts>.note::before{{content:"";position:absolute;left:-73px;top:-5px;height:97px;border-left:1px dotted var(--n-4)}}
{s}:has(.meter) .meter{{height:37px;flex:none;padding:0;display:flex;align-items:center;justify-content:center;container-type:normal}}
{s}:has(.meter) .meter::before,{s}:has(.meter) .meter::after{{height:37px}}
{s}:has(.meter) .meter:first-child::after{{background:var(--n-5)}}{s}:has(.meter) .meter>.name{{position:relative;z-index:2;color:var(--ink);font-size:var(--type-16);font-weight:var(--label-weight)}}{s}:has(.meter) .meter>.fig:empty{{display:none}}
{s}.quiet:has(.list){{border:0;background:none}}{s}.quiet:has(.list)>.parts{{inset:31px 0 13px 8px}}{s}.quiet:has(.list):last-child>.parts{{inset:31px 8px 13px 0}}
{s}.quiet:has(.list)>.parts::before{{content:"";position:absolute;inset:0;z-index:-1;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:var(--n-1)}}
{s}.quiet:has(.list)>.parts>.name{{left:54px;top:31px;font-size:var(--type-22);max-width:calc(100% - 72px)}}
{s}.quiet:has(.list)>.parts>.note>.list{{left:43px;right:31px;top:85px;height:190px;padding-top:26px;border-top:1px dotted var(--n-4);gap:0}}
{s}.quiet:has(.list) .list>.item{{display:block;min-height:36px;padding:0 0 0 14px}}
{s}.quiet:has(.list) .list>.item>.name{{display:block;padding:0;background:none;font-size:var(--type-18);line-height:var(--body-line);font-weight:var(--body-weight);min-height:0;text-align:left}}
{s}.quiet:has(.list) .list>.item>.note:empty{{display:none}}{s}.quiet:has(.list) .list>.item::before{{content:"";display:block;position:absolute;left:0;top:11px;width:6px;height:6px;border-radius:50%;background:var(--n-7)}}
{s}.quiet:has(.list) .list:has(.item>.note:not(:empty)){{padding-top:26px;gap:25px}}
{s}.quiet:has(.list) .list>.item:has(>.note:not(:empty)){{display:flex;gap:30px;padding:0;min-height:57px}}
{s}.quiet:has(.list) .list>.item:has(>.note:not(:empty))::before{{display:none}}
{s}.quiet:has(.list) .list>.item:has(>.note:not(:empty))>.name{{display:flex;align-items:center;justify-content:center;flex-basis:136px;min-height:37px;background:var(--n-2);font-size:var(--type-18);font-weight:var(--label-weight);text-align:center}}
{s}.quiet:has(.list) .list>.item:has(>.note:not(:empty))>.note{{font-size:var(--type-18);line-height:var(--lead-line)}}
@container (max-height:300px){{
{s}:has(.fig):not(:has(.mark))>.parts{{position:absolute;inset:0;display:block}}
{s}:has(.fig):not(:has(.mark))>.parts>.name{{position:absolute;left:39px;top:31px;min-height:43px;padding:calc(var(--gap-sm)/2) var(--gap-sm);font-size:var(--type-18);line-height:var(--label-line)}}
{s}:has(.fig):not(:has(.mark))>.parts>.note{{position:absolute;left:45px;top:96px;min-height:0;width:183px;text-align:left;font-size:var(--type-18);line-height:var(--lead-line)}}
{s}:has(.fig):not(:has(.mark))>.parts>.fig{{position:absolute;left:240px;top:124px;width:180px;font-size:var(--type-48);line-height:var(--figure-line);background:linear-gradient(90deg,var(--ink) 0%,var(--ink) 35%,var(--a1) 100%);background-clip:text;color:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);text-align:left}}
}}
{s}:has(.bars){{border:0;background:none}}{s}:has(.bars)>.parts{{position:absolute;inset:36px 22px 18px 1px;display:block}}
{s}:has(.bars)>.parts::before{{content:"";position:absolute;inset:0;z-index:-1;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:var(--n-1)}}
{s}:has(.bars)>.parts>.name{{position:absolute;left:46px;top:31px;font-size:var(--type-18);min-height:43px;padding:calc(var(--gap-sm)/2) var(--gap-sm);line-height:var(--label-line)}}
{s}:has(.bars)>.parts>.note{{position:absolute;inset:0;min-height:0;text-align:left;max-width:none}}
{s}:has(.bars)>.parts>.note>p{{position:absolute;left:53px;top:97px;font-size:var(--type-20);line-height:var(--lead-line)}}
{s}:has(.bars)>.parts>.note>.bars{{position:absolute;left:37px;right:37px;top:152px;height:240px;padding:0;border-bottom:1px solid var(--n-5);background:none;gap:0}}
{s}:has(.bars) .bars>.bar{{flex:none;width:26.3%;height:calc(var(--v)/var(--max)*100%);background:var(--n-7)}}{s}:has(.bars) .bars>.bar.on{{background:var(--a1)}}
{s}:has(.bars) .bars>.bar>b{{font-size:var(--type-18);margin-bottom:8px}}{s}:has(.bars) .bars>.bar>span{{font-size:var(--type-18);margin-top:10px}}
{s}:has(.bars)>.parts::after{{content:"";position:absolute;left:163px;top:65px;width:182px;height:194px;background:linear-gradient(var(--a1),color-mix(in srgb,var(--page) 0%,var(--ink) .001%));clip-path:polygon(47% 0,72% 24%,60% 24%,59% 42%,53% 60%,43% 76%,28% 89%,10% 98%,0 100%,18% 86%,31% 68%,39% 48%,42% 24%,29% 24%)}}
''')
