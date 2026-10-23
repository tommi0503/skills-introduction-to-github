from pathlib import Path
C=Path('/workspace/output/nightchamfer');p=Path('/workspace/work/nightchamfer/reassemble.py');t=p.read_text()
start=t.index("contents.append(callout('<b>고객 수요");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append(callout('<b>고객 수요 충족 목적</b><br>AI 성능 향상과 고객 요구 증대에 따른 실서비스 적용 시점이 도래',1,1,12,6)+el('headline','headline center','<h2>다음 성장 동력 발굴</h2><p class="note">쌓인 업무 데이터와 생성형 AI 기술을 결합해,<br>자연스러운 신규 성장 기회를 확보합니다.</p>',1,5,6,2)+el('headline','headline center','<h2>고객의 요구</h2><p class="note">사용자의 약 70%가 ‘반복 업무 자동화’ 기능을 요청<br>(회의록 정리·문서 작성에 주당 평균 5시간 소모)</p>',7,5,6,2))'''+t[end:]
start=t.index("contents.append(bar([300");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append(el('headline','headline center','<h2>국내 생산성 도구 시장 규모 추이</h2>',1,1,6,1)+el('chart-bar','bars',''.join(f'<div class="bar {"on"if i==3 else ""}" style="--v:{v}"><b>{v:,}억</b><span>{l}</span></div>'for i,(v,l)in enumerate(zip([300,520,820,1300],['1Q','2Q','3Q','4Q']))),1,1,6,4,';--max:1500')+el('headline','headline center','<h2>국내 시장 성장성 포인트</h2>',7,1,6,1)+items([('AI 대중화','업무에 AI를 쓰는 것이 당연한 환경으로 전환'),('기업 도입 확대','생산성 향상을 위한 기업의 AI 도구 도입이 가속'),('자동화 ROI 입증','업무 시간 절감 효과가 수치로 증명되며 수요 견인')],'list divided',7,2,6,3)+callout('AI 업무 도구 시장은 <b>연 60% 이상 고성장</b> 중이며, 협업툴 시장 대비 성장률이 2배를 넘습니다.'))'''+t[end:]
start=t.index("contents.append(card('미리AI");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append('<div class="split wide-left" style="'+grid(1,1,12,6)+'">'+el('card','card','<div class="parts"><b class="name">미리AI (MiriAI)</b><div class="note"><p>미리워크에 내장되는 AI 비서로 회의록 요약, 문서 초안,<br>할 일 추출, 업무 검색을 대화 한 번으로 처리합니다.</p>'+items([('회의록 자동 요약','녹취·메모를 핵심 요약과 할 일로 자동 변환'),('문서 초안 작성','주제만 입력하면 보고서·기획서 초안을 생성'),('업무 검색·질문','흩어진 문서·대화를 물어보면 AI가 즉시 답변')])+'</div></div>')+el('image-frame','frame','<div class="seat" data-ph="1"></div>')+'</div>')'''+t[end:];p.write_text(t)
# Background-panel conclusion, and a vertically rising conclusion used when a sentence has a leading badge.
p=C/'elements/callout/element.css';s='[data-el="nightchamfer-callout"]';p.write_text(p.read_text()+f'''
{s}{{border:0;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);isolation:isolate}}
{s}::before{{content:"";position:absolute;inset:22px 3px 20px;z-index:-1;border:var(--stroke) solid var(--n-4);border-radius:var(--radius-sm);background:var(--n-1)}}{s}>p{{font-size:var(--type-20);line-height:var(--body-line)}}
{s}:has(>p>br)::before{{display:none}}{s}:has(>p>br)>p{{position:absolute;left:38px;right:38px;top:33px;height:169px;padding:30px var(--pad);border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:var(--n-1);font-size:var(--type-22);font-weight:var(--label-weight);line-height:var(--body-line)}}
{s}:has(>p>br)>p>b{{display:inline-flex;align-items:center;justify-content:center;width:233px;height:45px;margin-bottom:20px;border-radius:999px;background:linear-gradient(90deg,var(--a1-4),var(--a1-5));color:var(--ink);font-size:var(--type-24);line-height:var(--label-line)}}
{s}:has(>p>br)::after{{content:"";position:absolute;left:calc(50% - 74px);top:184px;width:148px;height:140px;background:linear-gradient(var(--a1),color-mix(in srgb,var(--page) 0%,var(--ink) .001%));clip-path:polygon(50% 0,100% 50%,77% 50%,77% 100%,23% 100%,23% 50%,0 50%)}}
@container(max-width:700px){{{s}>p{{font-size:var(--type-16)}}}}
@container(max-height:150px){{{s}::before{{inset:6px 0}}}}
''')
p=C/'elements/headline/element.css';s='[data-el="nightchamfer-headline"]';p.write_text(p.read_text()+f'\n{s}.center:not(.big){{justify-content:flex-start;gap:var(--gap-sm)}}{s}.center:not(.big)>h2{{font-size:var(--type-24)}}{s}.center:not(.big)>.note{{font-size:var(--type-20)}}\n')
# The source 4-series business chart uses a broad plotting field below its own title.
p=C/'elements/chart-bar/element.css';s='[data-el="nightchamfer-chart-bar"]';p.write_text(p.read_text()+f'''
{s}:not(.h):has(>.bar:nth-child(4):last-child){{padding:100px 55px 4px 32px;gap:0;border:0;background:none;isolation:isolate}}
{s}:not(.h):has(>.bar:nth-child(4):last-child)::before{{content:"";position:absolute;inset:100px 55px 4px 32px;background:repeating-linear-gradient(to top,var(--n-4) 0,var(--n-4) 1px,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) 1px,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) 33.333%);border-bottom:1px solid var(--n-5);z-index:-1}}
{s}:not(.h):has(>.bar:nth-child(4):last-child)>.bar{{flex:none;width:16.67%;height:calc(var(--v)/var(--max)*100%);background:var(--n-7)}}{s}:not(.h):has(>.bar:nth-child(4):last-child)>.bar.on{{background:var(--a1)}}{s}:not(.h):has(>.bar:nth-child(4):last-child)>.bar>b{{font-size:var(--type-14);margin-bottom:4px}}{s}:not(.h):has(>.bar:nth-child(4):last-child)>.bar>span{{font-size:var(--type-14);margin-top:4px}}
''')
# Three rows: accent badges in outlined panels; plain rows: neutral badges for feature descriptions.
p=C/'elements/list/element.css';s='[data-el="nightchamfer-list"]';p.write_text(p.read_text()+f'''
{s}:not(.num):not(.check){{padding:0;gap:18px;justify-content:center}}
{s}:not(.num):not(.check)>.item{{padding:0;min-height:35px;display:flex;align-items:center;gap:22px}}
{s}:not(.num):not(.check)>.item::before{{display:none}}
{s}:not(.num):not(.check)>.item>.name{{flex:0 0 146px;display:flex;align-items:center;justify-content:center;min-height:35px;padding:calc(var(--gap-sm)/2);font-size:var(--type-18);line-height:var(--label-line);background:var(--n-2);border-radius:var(--radius-sm);text-align:center}}
{s}:not(.num):not(.check)>.item>.note{{flex:1;min-width:0;margin:0;font-size:var(--type-18);line-height:var(--body-line)}}
{s}.divided:not(.num):not(.check)>.item{{border:var(--stroke) solid var(--n-4);border-radius:var(--radius-sm);background:var(--n-1);padding:14px;min-height:64px;gap:22px}}
{s}.divided:not(.num):not(.check)>.item>.name{{background:linear-gradient(90deg,var(--a1-4),var(--a1-5));color:var(--ink);font-size:var(--type-18);font-weight:var(--label-weight)}}
{s}.divided:not(.num):not(.check)>.item>.note{{font-size:var(--type-16)}}
@container(max-width:450px){{{s}:not(.num):not(.check)>.item{{gap:var(--gap-sm)}}{s}:not(.num):not(.check)>.item>.name{{flex-basis:110px;font-size:var(--type-14)}}{s}:not(.num):not(.check)>.item>.note{{font-size:var(--type-14)}}}}
''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.split.wide-left:has(>.card):has(>.frame){padding:26px 28px 16px 0;grid-template-columns:7fr 5fr;gap:50px}\n''')
p=C/'elements/card/element.css';s='[data-el="nightchamfer-card"]';p.write_text(p.read_text()+f'''
{s}:has(.list){{background:var(--n-1)}}{s}:has(.list)>.parts{{position:absolute;inset:0;display:block}}
{s}:has(.list)>.parts>.name{{position:absolute;left:55px;top:44px;display:block;padding:0;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);min-height:0;font-size:var(--type-28);line-height:var(--name-line)}}
{s}:has(.list)>.parts>.note{{position:absolute;inset:0;max-width:none;min-height:0;text-align:left;font-size:var(--type-20);line-height:var(--body-line)}}
{s}:has(.list)>.parts>.note>p{{position:absolute;left:55px;top:102px;font-size:var(--type-20);font-weight:var(--label-weight)}}
{s}:has(.list)>.parts>.note>.list{{position:absolute;left:51px;right:67px;top:196px;height:215px;padding-top:34px;border-top:1px dotted var(--n-4);gap:20px;justify-content:flex-start;container-type:normal}}
''')
p=C/'elements/image-frame/element.css';s='[data-el="nightchamfer-image-frame"]';p.write_text(p.read_text()+f'\n{s}{{border:0;background:none;padding:0}}{s}>.seat{{width:100%;height:100%;max-height:none;aspect-ratio:auto;border-radius:var(--radius);background:var(--n-7);color:var(--n-4)}}\n')
