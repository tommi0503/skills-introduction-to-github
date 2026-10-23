from pathlib import Path
C=Path('/workspace/output/nightchamfer');R=Path('/workspace/output/nightchamfer-review')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.page{gap:calc(var(--gap-sm)/2)}.head{column-gap:var(--gap)}.head .kicker{width:27px;height:27px;display:flex;align-items:center;justify-content:center;flex:none}.page::after{inset:0;background:radial-gradient(ellipse 100% 28% at 50% 105%,var(--a1-6-muted) 0%,var(--a1-3-muted) 48%,var(--a1-1-muted) 72%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) 100%)}\n''')
s='[data-el="nightchamfer-hierarchy"]';p=C/'elements/hierarchy/element.css';p.write_text(p.read_text()+f'''\n{s}{{padding:0;gap:var(--gap);align-items:flex-start}}
{s}>.root{{width:176px;max-width:30%;height:auto;aspect-ratio:1;top:0;left:50%;transform:translateX(-50%);border:18px solid var(--a1-2-muted);background:linear-gradient(135deg,var(--a1-5),var(--a1-4));color:var(--ink);font-size:var(--type-24);line-height:var(--name-line)}}
{s}>.root .name{{font-size:var(--type-24);color:var(--ink)}}{s}>.root::after{{top:100%;height:35px;border-left:1px dotted var(--n-5)}}
{s}>.branch{{margin-top:244px;height:calc(100% - 244px);align-self:flex-start;gap:var(--pad);justify-content:flex-start;align-items:center;min-width:0}}
{s}>.branch>.node{{width:min(173px,90%);height:48px;min-height:48px;padding:calc(var(--gap-sm)/2);display:flex;align-items:center;justify-content:center;border-radius:var(--radius-sm);background:linear-gradient(90deg,var(--a1-5),var(--a1-4));color:var(--ink);font-size:var(--type-22);line-height:var(--name-line)}}
{s}>.branch>.node .name{{font-size:var(--type-22);color:var(--ink)}}
{s}>.branch>.leaf{{width:min(220px,95%);height:117px;flex:0 0 117px;display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--gap-sm);font-size:var(--type-20);line-height:var(--body-line);color:var(--n-7);background:linear-gradient(var(--n-1),var(--a1-1-muted));border-radius:var(--radius-sm)}}
{s}>.branch>.leaf .name{{font-size:var(--type-20)}}
{s}>.branch::before{{left:50%;top:-33px;height:33px}}{s}>.branch::after{{top:-33px;left:calc(var(--gap)/-2);right:calc(var(--gap)/-2)}}{s}>.branch:nth-child(2)::after{{left:50%}}{s}>.branch:last-child::after{{right:50%}}
{s}>.branch:has(>.leaf:nth-child(3)){{gap:var(--gap-sm)}}{s}>.branch:has(>.leaf:nth-child(3))>.leaf{{height:auto;flex:1;min-height:0}}{s}>.branch:has(>.leaf:nth-child(3))>.leaf .name{{font-size:var(--type-16)}}
@container(max-height:420px){{{s}>.root{{width:120px;border-width:12px;font-size:var(--type-18)}}{s}>.root .name{{font-size:var(--type-18)}}{s}>.root::after{{height:16px}}{s}>.branch{{margin-top:42cqh;height:54cqh;gap:var(--gap-sm)}}{s}>.branch>.node{{height:36px;min-height:36px;font-size:var(--type-16)}}{s}>.branch>.node .name{{font-size:var(--type-16)}}{s}>.branch>.leaf{{flex:1;height:auto;font-size:var(--type-16)}}{s}>.branch>.leaf .name{{font-size:var(--type-16)}}{s}>.branch::before{{top:-20px;height:20px}}{s}>.branch::after{{top:-20px}}}}
@container(max-width:900px){{{s}>.branch>.node .name{{font-size:var(--type-16)}}{s}>.branch>.leaf .name{{font-size:var(--type-14)}}}}
''')
