from pathlib import Path
C=Path('/workspace/output/nightchamfer');p=Path('/workspace/work/nightchamfer/reassemble.py');t=p.read_text()
start=t.index("contents.append(el('flowchart'");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append(el('architecture','arch','<div class="layer"><b class="name">시장의 문제</b><span class="chip">범용 AI 도구는 업무 맥락을 모르고, 별도 구독·보안<br>우려로 기업 도입이 어렵습니다.</span></div><div class="layer"><b class="name">당사 전략</b><span class="chip">미리워크 유료 플랜에 ‘미리AI’를 추가로 제공해,<br>기존 고객 기반에서 즉시 매출을 확장합니다.</span></div>',1,1,6,6)+el('architecture','arch','<div class="layer"><b class="name">미리 AI 추가 제공</b></div><div class="layer"><b class="name">기존 플랜에 추가 과금</b><span class="chip">사용량<br>기반</span><span class="chip">팀 단위<br>정액</span><span class="chip">엔터프라<br>이즈 맞춤</span></div>',7,1,6,6))'''+t[end:]
start=t.index("contents.append(el('positioning'");end=t.index('\ncontents.append',start)
t=t[:start]+'''contents.append(el('positioning','posmap','<div class="axis-x"><span>업무 맥락 이해도 낮음</span><span>업무 맥락 이해도 높음</span></div><div class="axis-y"><span>협업툴 통합도 낮음</span><span>협업툴 통합도 높음</span></div>'+''.join(f'<div class="mark {"on"if n=="미리 AI"else "tone-1"if n=="경쟁사 C"else ""}" style="--x:{x};--y:{y}"><b class="name">{n}</b></div>'for n,x,y in [('경쟁사 A',24,73.65),('경쟁사 B',38.22,26.69),('경쟁사 C',69.33,65.87),('경쟁사 D',76.78,12.16),('미리 AI',95.28,89.53)])))'''+t[end:];p.write_text(t)
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.head .title:has(>.label){position:relative;width:max-content}.head .title>.label{position:absolute;left:100%;top:4px;width:max-content;line-height:var(--title-line)}\n''')
p=C/'elements/card/element.css';p.write_text(p.read_text()+'''\n[data-el="nightchamfer-card"]{background:var(--n-1)}@container (max-height:300px){[data-el="nightchamfer-card"]:has(.fig):not(:has(.mark))>.parts>.fig{left:auto;right:40px;text-align:right}}\n''')
s='[data-el="nightchamfer-architecture"]';p=C/'elements/architecture/element.css';p.write_text(p.read_text()+f'''
@container (min-width:500px) and (min-height:400px){{
{s}>.layer{{position:absolute;left:7px;right:11px;top:35px;height:191px;display:block;padding:0;border-radius:var(--radius);background:var(--n-1)}}{s}>.layer:nth-child(2){{top:263px;height:192px}}
{s}>.layer>.name{{position:absolute;left:50%;top:33px;transform:translateX(-50%);display:flex;align-items:center;justify-content:center;min-width:0;width:max-content;max-width:90%;height:43px;padding:0 var(--gap);border-radius:var(--radius-sm);background:var(--n-2);color:var(--ink);font-size:var(--type-20);line-height:var(--label-line)}}
{s}>.layer>.chip{{position:absolute;left:35px;right:35px;top:92px;display:block;padding:0;background:none;min-height:0;border-radius:0;font-size:var(--type-20);font-weight:var(--body-weight);line-height:var(--body-line);color:var(--n-7);text-align:center}}
{s}>.layer:first-child::after{{content:"";position:absolute;left:calc(50% - 32px);top:193px;width:64px;height:55px;background:linear-gradient(color-mix(in srgb,var(--page) 0%,var(--ink) .001%),var(--a1));clip-path:polygon(23% 0,77% 0,77% 50%,100% 50%,50% 100%,0 50%,23% 50%)}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:first-child{{left:0;right:9px;top:35px;height:420px}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:first-child>.name{{width:197px}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:first-child::after{{top:81px}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:nth-child(2){{left:36px;right:45px;top:160px;height:260px;border:0;background:var(--n-2)}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:nth-child(2)>.name{{left:29px;right:29px;top:33px;transform:none;width:auto;height:61px;background:linear-gradient(90deg,var(--a1-5),var(--a1-4));font-size:var(--type-24)}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:nth-child(2)>.chip{{left:29px;right:auto;top:119px;width:112px;height:112px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:linear-gradient(135deg,var(--a1-5),var(--a1-4));color:var(--ink);font-size:var(--type-18);font-weight:var(--label-weight);line-height:var(--label-line)}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:nth-child(2)>.chip:nth-child(3){{left:176px}}{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:nth-child(2)>.chip:nth-child(4){{left:323px}}
{s}:has(>.layer:nth-child(2)>.chip:nth-child(4))>.layer:nth-child(2)>.chip:not(:last-child)::after{{content:"";position:absolute;left:calc(100% + 8px);top:50%;width:19px;border-top:1px dotted var(--n-7)}}
}}
''')
s='[data-el="nightchamfer-positioning"]';p=C/'elements/positioning/element.css';p.write_text(p.read_text()+f'''
{s}{{border:0;background:none}}
{s}::before{{inset:22px 9px -1px 1px;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:var(--n-1);z-index:-1}}
{s}::after{{top:98px;bottom:73px;left:50%;border-left:1px dotted var(--n-5)}}
{s}>.axis-x{{left:48px;right:48px;top:223px;display:flex;align-items:center;font-size:var(--type-16)}}
{s}>.axis-x::before{{content:"";position:absolute;left:35px;right:35px;top:20px;border-top:1px dotted var(--n-5);z-index:-1}}
{s}>.axis-x>span{{height:41px;min-width:176px;display:flex;align-items:center;justify-content:center;color:var(--n-7)}}
{s}>.axis-x>span:last-child{{background:linear-gradient(90deg,var(--a1-5),var(--a1-4));color:var(--ink)}}
{s}>.axis-y{{left:0;right:0;top:57px;bottom:36px;align-items:center;font-size:var(--type-16)}}
{s}>.axis-y>span{{height:39px;width:159px;display:flex;align-items:center;justify-content:center;line-height:var(--label-line)}}
{s}>.axis-y>span:last-child{{background:linear-gradient(90deg,var(--a1-5),var(--a1-4));color:var(--ink)}}
{s}>.mark{{left:calc(83px + var(--x)/100*(100% - 212px));bottom:calc(73px + var(--y)/100*(100% - 171px));width:14px;height:14px;background:var(--n-3)}}
{s}>.mark.tone-1{{background:var(--a1)}}{s}>.mark>.name{{font-weight:var(--body-weight);color:var(--n-7);font-size:var(--type-16)}}
{s}>.mark.on{{width:25px;height:25px;background:var(--a1);box-shadow:0 0 0 13px var(--a1-1-muted)}}{s}>.mark.on>.name{{color:var(--ink);font-size:var(--type-24);font-weight:var(--name-weight);bottom:calc(100% + 21px)}}
{s}>.mark.on::after{{content:"높은 맥락 이해 +\\A 완전 통합으로 차별화";white-space:pre;position:absolute;left:50%;top:calc(100% + 21px);transform:translateX(-50%);font-size:var(--type-14);line-height:var(--body-line);color:var(--n-7);text-align:center;width:180px}}
@container(max-width:850px){{{s}>.mark.on::after{{display:none}}}}
''')
