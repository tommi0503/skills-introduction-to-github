"""Restore only the final source divider and pie-separator findings."""
from pathlib import Path
P=Path(__file__).parent;C=P/'seedmark';M='/* SOURCE_FINAL_RULES */'
def add(rel,css):
 p=C/rel;p.write_text(p.read_text().split(M)[0]+'\n'+M+'\n'+css+'\n')
add('foundation/foundation.css','''
.slide.src .head:has(>.title){border-bottom:2px solid var(--n-3);}
''')
add('elements/card/element.css','''
.slide.src [data-el="seedmark-card"].card .parts:has(>.list):not(:has(>.stacks))>.name{position:relative;width:calc(100% - var(--stroke)*1.3333333333);border:0;}
.slide.src [data-el="seedmark-card"].card .parts:has(>.list):not(:has(>.stacks))>.name:after{content:'';display:block;position:absolute;left:0;right:0;bottom:calc(var(--gap-sm)/3);height:2px;background:var(--n-3);}
''')
add('elements/metric/element.css','''
.slide.src .stack>.stack>[data-el="seedmark-metric"]:first-child:before{content:'';position:absolute;left:calc(var(--pad)*-.4375);right:0;top:calc(var(--gap-sm)/-3);height:2px;background:var(--n-3);}
''')
add('elements/chart-donut/element.css','''
.slide.src [data-el="seedmark-chart-donut"].donut:has(.name>.icon):before{content:'';display:block;position:absolute;inset:auto;left:50%;top:var(--seedmark-donut-cy);width:4px;height:min(50cqw,50cqh);border-radius:0;transform:translate(-50%,-100%) rotate(var(--seedmark-donut-start));transform-origin:50% 100%;background:var(--page);z-index:5;}
.slide.src [data-el="seedmark-chart-donut"].donut.tone-1:has(.name>.icon):after{background-image:conic-gradient(from var(--seedmark-donut-start),var(--a1) calc(var(--v)*1%),transparent 0);}
.slide.src [data-el="seedmark-chart-donut"].donut.tone-2:has(.name>.icon):after{background-image:conic-gradient(from var(--seedmark-donut-start),var(--n-7) calc(var(--v)*1%),transparent 0);}
.slide.src [data-el="seedmark-chart-donut"].donut.tone-3:has(.name>.icon):after{background-image:conic-gradient(from var(--seedmark-donut-start),var(--n-4) calc(var(--v)*1%),transparent 0);}
.slide.src [data-el="seedmark-chart-donut"].donut.tone-5:has(.name>.icon):after{background-image:conic-gradient(from var(--seedmark-donut-start),var(--n-3) calc(var(--v)*1%),transparent 0);}
.slide.src [data-el="seedmark-chart-donut"].donut.tone-3:has(.name>.icon)>.name,.slide.src [data-el="seedmark-chart-donut"].donut.tone-3:has(.name>.icon)>.fig{color:var(--page);}
''')
print('Final source rules restored.')
