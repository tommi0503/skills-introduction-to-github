from pathlib import Path
p=Path('/workspace/work/nightchamfer/reassemble.py');t=p.read_text();start=t.index("contents.append(el('pyramid'");end=t.index("\ncontents.append",start)
t=t[:start]+'''contents.append(el('pyramid','pyramid',''.join(f'<div class="level"><b class="name">{n}</b><p class="note"><b>{k}</b>　|　{d}</p></div>'for n,k,d in [('4단계','외부 확장','레퍼런스와 입소문을 지렛대로 신규, 기업 고객까지 확대'),('3단계','조직 표준화','팀을 넘어 회사 표준 도구로 정착시켜 객단가 상승'),('2단계','팀 확산','한 명의 사용 경험이 팀 전체로 번지는 협업 기반 자연 확산'),('1단계','내부 침투','기존 유저에게 무료로 노출해 진입 비용 최소화')])))'''+t[end:]
t=t.replace("PAL=';'", "pal['--a1-6-muted']='#4082F0'\nPAL=';'")
p.write_text(t)
p=Path('/workspace/output/nightchamfer/elements/pyramid/element.css');s='[data-el="nightchamfer-pyramid"]';p.write_text(p.read_text()+f'''
/* A wide four-level pyramid uses the same level/name/note contract as a compact stack. */
@container (min-width:900px) and (min-height:420px){{
{s}:has(>.level:nth-child(4):last-child)>.level{{position:absolute;inset:0;display:block;width:auto;height:auto;min-height:0;max-height:none;padding:0;border:0;border-radius:0;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);--nightchamfer-ellipse-width:19.2446043cqw;--nightchamfer-ellipse-height:72px;--nightchamfer-ellipse-top:74px;--nightchamfer-text-top:91px;--nightchamfer-floor:color-mix(in srgb,var(--n-3) 75%,var(--a1-2-muted))}}
{s}:has(>.level:nth-child(4):last-child)>.level:nth-child(2){{--nightchamfer-ellipse-width:29.1366906cqw;--nightchamfer-ellipse-height:106px;--nightchamfer-ellipse-top:139px;--nightchamfer-text-top:184px;--nightchamfer-floor:color-mix(in srgb,var(--n-5) 60%,var(--a1-2-muted))}}
{s}:has(>.level:nth-child(4):last-child)>.level:nth-child(3){{--nightchamfer-ellipse-width:37.9496403cqw;--nightchamfer-ellipse-height:136px;--nightchamfer-ellipse-top:207px;--nightchamfer-text-top:277px;--nightchamfer-floor:color-mix(in srgb,var(--n-7) 60%,var(--a1-4-muted))}}
{s}:has(>.level:nth-child(4):last-child)>.level:nth-child(4){{--nightchamfer-ellipse-width:45.323741cqw;--nightchamfer-ellipse-height:156px;--nightchamfer-ellipse-top:280px;--nightchamfer-text-top:369px;--nightchamfer-floor:color-mix(in srgb,var(--n-9) 70%,var(--a1-3-muted))}}
{s}:has(>.level:nth-child(4):last-child)>.level::before{{content:"";position:absolute;left:calc(22.6618705cqw - var(--nightchamfer-ellipse-width)/2);top:var(--nightchamfer-ellipse-top);width:var(--nightchamfer-ellipse-width);height:var(--nightchamfer-ellipse-height);border-radius:50%;background:linear-gradient(var(--page),var(--nightchamfer-floor))}}
{s}:has(>.level:nth-child(4):last-child)>.level::after{{content:"";position:absolute;left:calc(22.6618705cqw + var(--nightchamfer-ellipse-width)/2 + 24px);right:50.5395683%;top:calc(var(--nightchamfer-text-top) + 12px);border-top:2px dotted var(--n-5)}}
{s}:has(>.level:nth-child(4):last-child)>.level:nth-child(4)::after{{left:calc(22.6618705cqw + var(--nightchamfer-ellipse-width)/2 + 15px)}}
{s}:has(>.level:nth-child(4):last-child)>.level>.name{{position:absolute;left:calc(22.6618705cqw - var(--nightchamfer-ellipse-width)/2);top:var(--nightchamfer-text-top);width:var(--nightchamfer-ellipse-width);font-size:var(--type-20);line-height:var(--label-line);font-weight:var(--label-weight);text-align:center;color:var(--ink)}}
{s}:has(>.level:nth-child(4):last-child)>.level>.note{{display:block;position:absolute;left:52.6978417%;right:0;top:calc(var(--nightchamfer-text-top) - 1px);max-width:none;font-size:var(--type-20);line-height:var(--label-line);color:var(--n-7);text-align:left;white-space:normal}}
{s}:has(>.level:nth-child(4):last-child)>.level>.note>b{{font-weight:var(--name-weight)}}
}}
''')
