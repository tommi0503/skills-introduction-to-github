from pathlib import Path
C=Path('/workspace/output/nightchamfer');p=C/'kit/css/tokens.css';p.write_text(p.read_text().replace('--lead-line: 1.6','--lead-line: 1.5'))
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'\n.head .lead{font-size:var(--type-22)}\n')
p=Path('/workspace/work/nightchamfer/reassemble.py');t=p.read_text().replace('기존 고객을 대상으로 회의록·문서 요약 기능을 우선 공개합니다.','기존 고객을 대상으로 회의록·<br>문서 요약 기능을 우선 공개합니다.').replace('사용량 기반 과금 모델을 적용한 정식 서비스를 출시합니다. 핵심 기능을 고도화하고 안정적인 수익 모델을 구축합니다.','사용량 기반 과금 모델을 적용<br>한 정식 서비스를 출시합니다.<br><br>핵심 기능을 고도화하고 안정<br>적인 수익 모델을 구축합니다.').replace('AI 기능을 활용한 마케팅을 강화하여 신규 가입을 확대합니다. 다양한 프로모션과 콘텐츠를 통해 서비스 이용률을 높입니다.','AI 기능을 활용한 마케팅을 강화<br>하여 신규 가입을 확대합니다.<br><br>다양한 프로모션과 콘텐츠를 통<br>해 서비스 이용률을 높입니다.').replace('기업 전용 모델과 보안 패키지를 기반으로 B2B 시장을 공략합니다. 대규모 고객사를 확보하며 사업을 확대합니다.','본격적으로 기업 전용 모델과 보<br>안 패키지를 기반으로 B2B 시장<br>을 공략합니다.<br><br>대규모 고객사를 확보하며 엔터프<br>라이즈 사업을 본격 확대합니다.');p.write_text(t)
s='[data-el="nightchamfer-timeline"]:not(.col):not(.alt)';p=C/'elements/timeline/element.css';p.write_text(p.read_text()+f'''
@container (min-width:900px) and (min-height:420px){{
{s}>.stop{{position:absolute;left:0;top:0;bottom:0;width:24.1906475%;height:auto;display:block;padding:0;border:0;--nightchamfer-stop-y:244px}}
{s}>.stop:nth-child(2){{left:24.1906475%;height:auto;--nightchamfer-stop-y:166px}}{s}>.stop:nth-child(3){{left:48.381295%;height:auto;--nightchamfer-stop-y:88px}}{s}>.stop:nth-child(4){{left:72.5719425%;height:auto;--nightchamfer-stop-y:10px}}
{s}>.stop>.kick{{position:absolute;left:0;top:var(--nightchamfer-stop-y);margin:0;display:flex;align-items:center;justify-content:center;width:63px;height:63px;min-width:0;min-height:0;padding:0;border:0;border-radius:50%;background:linear-gradient(135deg,var(--a1-5),var(--a1-4));font-size:var(--type-18);line-height:var(--label-line);color:var(--ink)}}
{s}>.stop>.name{{position:absolute;left:77px;top:calc(var(--nightchamfer-stop-y) - 7px);width:240px;font-size:var(--type-22);line-height:var(--label-line)}}
{s}>.stop>.note{{position:absolute;left:69px;top:calc(var(--nightchamfer-stop-y) + 65px);width:237px;font-size:var(--type-18);line-height:var(--body-line);color:var(--n-7)}}
{s}>.stop::before{{display:block;position:absolute;left:30px;top:calc(var(--nightchamfer-stop-y) + 63px);bottom:45px;width:0;height:auto;border:0;border-left:1px dotted var(--n-4);background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);box-shadow:none;border-radius:0}}
{s}>.stop::after{{left:63px;right:auto;top:calc(var(--nightchamfer-stop-y) + 35px);width:230px;height:1px;background:var(--n-7)}}
}}
{s}:has(>.stop:nth-child(4):last-child)::after{{content:"";position:absolute;left:79.1366906%;bottom:57px;width:19.7841727%;height:77px;background:linear-gradient(90deg,color-mix(in srgb,var(--page) 0%,var(--ink) .001%),var(--a1));clip-path:polygon(0 25%,83% 25%,83% 0,100% 50%,83% 100%,83% 75%,0 75%)}}
@container (max-height:419px){{{s}:has(>.stop:nth-child(4):last-child)::after{{display:none}}}}
''')
