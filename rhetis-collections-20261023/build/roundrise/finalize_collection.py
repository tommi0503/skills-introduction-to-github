from pathlib import Path
B=Path('/workspace/output/roundrise')
for p in B.rglob('*.css'):
 s=p.read_text().replace('transparent','color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%)').replace('margin-bottom:-5px','margin-bottom:calc(var(--gap-sm)*-5/12)').replace('gap:2px','gap:calc(var(--gap-sm)/6)')
 p.write_text(s)
p=B/'elements/chart-donut/element.css';s=p.read_text();s+='''.donut[data-el="roundrise-chart-donut"]:before{inset:auto;left:50%;top:50%;width:min(100cqw,100cqh);height:min(100cqw,100cqh);transform:translate(-50%,-50%)}.donut[data-el="roundrise-chart-donut"]:after{inset:auto;left:50%;top:50%;width:calc(min(100cqw,100cqh)*.72);height:calc(min(100cqw,100cqh)*.72);transform:translate(-50%,-50%)}''';p.write_text(s)
