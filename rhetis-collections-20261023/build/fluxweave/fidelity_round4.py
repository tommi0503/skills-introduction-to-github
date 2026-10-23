from pathlib import Path
import shutil
O=Path('/workspace/output/fluxweave');V=Path('/workspace/output/fluxweave-review')
def add(p,s):
 f=O/p;f.write_text(f.read_text()+'\n'+s+'\n')
p=O/'kit/css/tokens.css';p.write_text(p.read_text().replace("--font-display:'Pretendard Variable'","--font-display:'Montserrat','Pretendard Variable'"))
shutil.copy('/workspace/work/reference/fonts/artifacts/montserrat/Montserrat.woff2',V/'assets/Montserrat.woff2')
p=V/'assets/fonts.css';p.write_text(p.read_text()+"\n@font-face{font-family:'Montserrat';src:url('Montserrat.woff2') format('woff2');font-weight:100 900;font-style:normal;font-display:block;}\n")
add('foundation/foundation.css','''
.slide .head .title{font-family:var(--font-body);font-size:var(--type-52);line-height:calc(var(--title-line) - .05);}
.slide.cover .title{font-family:var(--font-display);font-weight:var(--weight-display);}
.slide.cover .at-bottom-left{bottom:calc(var(--margin-y) - var(--gap-sm)*1.3);}
.slide .group:has(>.card>.parts>.mark>.icon):not(.col):not(.two){height:194px;align-self:start;}
.slide .rail>.deco{inset:auto auto -40px -135px;width:470px;height:260px;transform:rotate(22deg);z-index:-1;}
.slide .rail>.deco>svg{height:100%;width:100%;}
''')
add('elements/headline/element.css','''
.headline.big[data-el="fluxweave-headline"]>h2{font-family:var(--font-display);}
''')
add('elements/list/element.css','''
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item::after{right:auto;width:50%;}
''')
add('elements/table/element.css','''
.tablebox[data-el="fluxweave-table"]:has(th:empty){height:270px;}
@container(min-width:800px){
.tablebox[data-el="fluxweave-table"]:not(:has(th:empty)) th{height:54px;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(4)) th{height:65px;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(3):last-child) th{height:50px;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(3):last-child) th:last-child{background:var(--a1-8);}
}
''')
add('elements/timeline/element.css','''
@container(min-width:400px) and (min-height:650px){.track.col[data-el="fluxweave-timeline"]>.stop>.name{display:block;margin:0;}}
''')
add('elements/card/element.css','''
.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon):not(:has(>.parts>.fig))>.parts{position:relative;width:100%;height:100%;display:block;}
.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon):not(:has(>.parts>.fig))>.parts>.mark{position:absolute;top:0;left:calc(50% - 20px);width:40px;height:40px;margin:0;}
.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon):not(:has(>.parts>.fig))>.parts>.name{position:absolute;top:50px;left:0;right:0;min-height:0;height:auto;margin:0;font-size:var(--type-24);line-height:var(--name-line);}
.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon):not(:has(>.parts>.fig))>.parts>.note{position:absolute;top:87px;left:0;right:0;min-height:0;height:auto;margin:0;font-size:var(--type-18);line-height:calc(var(--body-line) - .15);}
.group.two>.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon)>.parts>.mark{top:calc(var(--gap-sm)*.8);}
.group.two>.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon)>.parts>.name{top:60px;}
.group.two>.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon)>.parts>.note{top:90px;}
.card[data-el="fluxweave-card"]:has(>.parts>.kick:last-child):not(:has(>.parts>.fig))>.parts>.note{font-size:var(--type-16);line-height:var(--body-line);}
.card[data-el="fluxweave-card"]>.parts>.bars[style*="--max:200"]::after{content:"200명\\A 150명\\A 100명\\A 50명\\A 0명";}
.card[data-el="fluxweave-card"]>.parts>.bars[style*="--max:100"]::after{content:"100건\\A 80건\\A 60건\\A 40건\\A 20건\\A 0건";line-height:calc(100cqh/(var(--fluxweave-axis-steps) + 1));}
.card[data-el="fluxweave-card"]>.parts>.bars[style*="--max:100"]::before{background:repeating-linear-gradient(to top,var(--n-3) 0 1px,color-mix(in srgb,var(--page) 0%,var(--page) 1%) 1px 20%);}
''')
add('elements/image-frame/element.css','''
.group>.frame[data-el="fluxweave-image-frame"]:has(>.seat){padding:0;background:none;justify-content:center;align-items:flex-start;}
.group>.frame[data-el="fluxweave-image-frame"]:has(>.seat)>.seat{width:218px;height:242px;aspect-ratio:auto;transform:none;}
''')
p=Path('/workspace/work/fluxweave/reassemble.py');s=p.read_text().replace("'OUR<br>BUSINESS'+ari","'OUR'+ari+'<br>BUSINESS'");s=s.replace("'<span class=\"logo\"></span></aside>'","'<span class=\"logo\"></span><div class=\"deco\">'+wave_svg(1)+'</div></aside>'");s=s.replace("'--a1-7':'#9e3cff'","'--a1-7':'#9e3cff','--a1-8':'#7d1dcc'")
s=s.replace("'데이터 활용','비즈니스 데이터를 분석해<br>의사결정 지원'","'데이터 활용','비즈니스 데이터를 분석해<br>의사결정 지원'")
s=s.replace("]),1,1,12,3)+slot(table(['핵심 효과'", "]),1,1,12,4)+slot(table(['핵심 효과'")
p.write_text(s)
print('round4')
