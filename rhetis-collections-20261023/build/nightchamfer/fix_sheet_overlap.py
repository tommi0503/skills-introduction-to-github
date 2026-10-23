from pathlib import Path
C=Path('/workspace/output/nightchamfer')
p=C/'elements/timeline/element.css';t=p.read_text();i=t.index('@container (min-width:900px)');t=t[:i]+t[i:].replace('[data-el="nightchamfer-timeline"]:not(.col):not(.alt)','[data-el="nightchamfer-timeline"]:not(.col):not(.alt):has(>.stop:nth-child(4):last-child)');s='[data-el="nightchamfer-timeline"]:not(.col):not(.alt):has(>.stop:nth-child(5):last-child)';t+=f'\n@container(min-height:380px){{{s}>.stop:nth-child(1){{height:52%}}{s}>.stop:nth-child(2){{height:64%}}{s}>.stop:nth-child(3){{height:76%}}{s}>.stop:nth-child(4){{height:88%}}{s}>.stop:nth-child(5){{height:100%}}}}\n';p.write_text(t)
p=C/'elements/sparkline/element.css';p.write_text(p.read_text()+'\n[data-el="nightchamfer-sparkline"].bars>span{align-self:flex-end}\n')
# Keep comparison values at the actual line endpoints in each metric row.
p=C/'elements/slope/element.css';s='[data-el="nightchamfer-slope"]:not(.dumbbell)';p.write_text(p.read_text()+f'''
{s}>.heads{{padding-left:45%;padding-right:7%}}
{s}>.pair{{display:block;position:relative;anchor-scope:all;padding:0}}
{s}>.pair>.name{{position:absolute;left:0;top:50%;transform:translateY(-50%);width:35%;font-size:var(--type-16)}}
{s}>.pair>.a,{s}>.pair>.b{{position:absolute;margin:0;padding:0 var(--gap-sm);font-size:var(--type-18);line-height:var(--label-line);white-space:nowrap}}
{s}>.pair>.a{{left:45%;top:calc(var(--gap-sm) + (1 - var(--a)/var(--max))*(100% - var(--gap)) - 10px);transform:translate(-50%,-100%);anchor-name:--nc-slope-a}}
{s}>.pair>.b{{left:93%;top:calc(var(--gap-sm) + (1 - var(--b)/var(--max))*(100% - var(--gap)) + 10px);transform:translateX(-50%);anchor-name:--nc-slope-b}}
{s}>.pair>.a::after,{s}>.pair>.b::after{{content:"";position:absolute;left:50%;width:10px;height:10px;transform:translateX(-50%);border-radius:50%;background:var(--n-5)}}
{s}>.pair>.a::after{{top:calc(100% + 5px)}}{s}>.pair>.b::after{{bottom:calc(100% + 5px)}}
{s}>.pair.on>.a::after,{s}>.pair.on>.b::after{{background:var(--a1)}}
{s}>.pair::before,{s}>.pair::after{{content:"";position:absolute;left:anchor(--nc-slope-a center);right:calc(100% - anchor(--nc-slope-b center));height:auto;transform:none;pointer-events:none}}
{s}>.pair::before{{top:calc(anchor(--nc-slope-b top) - 10px);bottom:calc(100% - anchor(--nc-slope-a bottom) - 10px);background:linear-gradient(to top right,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% - 1px),var(--n-5) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% + 1px))}}
{s}>.pair::after{{top:calc(anchor(--nc-slope-a bottom) + 10px);bottom:calc(100% - anchor(--nc-slope-b top) + 10px);background:linear-gradient(to bottom right,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% - 1px),var(--n-5) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% + 1px))}}
{s}>.pair.on::before{{height:auto;background:linear-gradient(to top right,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% - 1px),var(--a1) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% + 1px))}}{s}>.pair.on::after{{background:linear-gradient(to bottom right,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% - 1px),var(--a1) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% + 1px))}}
''')
