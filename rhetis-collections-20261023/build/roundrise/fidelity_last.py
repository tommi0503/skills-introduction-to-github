from pathlib import Path
B=Path('/workspace/output/roundrise');R=Path('/workspace/output/roundrise-review')
p=B/'elements/chart-bar/element.css';s=p.read_text();s+='''.bars[data-el="roundrise-chart-bar"].h>.bar>span{width:calc(var(--pad)*4.5);max-width:none}''';p.write_text(s)
p=B/'elements/chart-donut/element.css';s=p.read_text();r='.donut[data-el="roundrise-chart-donut"]';s+=r+'''>.name{width:min(58cqw,calc(min(100cqw,100cqh,398px)*.6));max-width:100%;overflow-wrap:anywhere}'''+r+'''>.fig:before,'''+r+'''>.fig:after{opacity:clamp(0,var(--v),1)}''';p.write_text(s)
p=B/'elements/hub/element.css';s=p.read_text();r='.hub[data-el="roundrise-hub"]:has(>.spoke:nth-child(7))';s+=r+'''>.spoke{transform:none}'''+r+'''>.spoke>.name{font-size:var(--type-22)}'''+r+'''>.spoke>.note{font-size:var(--type-20)}'''+r+'''>.core{transform:none}@container (min-width:800px) and (min-height:360px){'''+r+'''>.spoke:before{height:calc(100cqh/3 - var(--gap-lg)*1.5)}'''+r+'''>.spoke:nth-child(n+4):before{top:calc(50% - (100cqh/3 - var(--gap-lg)*1.5))}'''+r+'''>.spoke:nth-child(n+6):before{top:50%;height:var(--stroke);clip-path:none}'''+r+'''>.spoke:after{top:calc(50% + 100cqh/3 - var(--gap-lg)*1.5 - 5px)}'''+r+'''>.spoke:nth-child(n+4):after{top:calc(50% - (100cqh/3 - var(--gap-lg)*1.5) - 5px)}'''+r+'''>.spoke:nth-child(n+6):after{top:calc(50% - 5px)}}''';p.write_text(s)
p=B/'elements/agenda/element.css';s=p.read_text()+'.agenda[data-el="roundrise-agenda"]>.entry>.name{font-weight:var(--weight-body)}';p.write_text(s)
p=B/'elements/card/element.css';s=p.read_text()+'.card[data-el="roundrise-card"]:has(>.parts>.note>.pill)>.parts>.fig small{font-size:var(--type-32);font-weight:var(--name-weight)}';p.write_text(s)
p=B/'foundation/foundation.css';s=p.read_text().replace('.body>.group>.card>.parts>.kick:not(:has(.pill))','.body>.group>.card>.parts>.mark.seat+.kick');s+='''.slide.cover .deco:before{content:"";position:absolute;left:1003px;top:-199px;width:137px;height:137px;border-radius:50%;background:var(--n-2)}''';boxes=[(-190,410,650,650),(924,83,93,93),(1110,560,180,260)]
for j,(x,y,w,h) in enumerate(boxes,1):s+=f'.slide:not(.cover) .page:has(>.body>.headline.big.center>.kick>b)>.deco:nth-of-type({j})'+'{'+f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;'+'}'
p.write_text(s)
p=Path('/workspace/work/roundrise/reassemble.py');s=p.read_text().replace('{2: 3, 3: 2, 5: 2','{2: 3, 3: 2, 4: 3, 5: 2').replace('data-ph="3D graphic"','data-ph=""');p.write_text(s)
p=R/'replica/replica.css';s=p.read_text()+'.kind-bar .legend:before{border-radius:5px}.centerbrand{color:#050608}.centerbrand svg{color:#065de5}';p.write_text(s)
for p in (R/'replica').glob('slide_*.html'):
 s=p.read_text();import re;s=re.sub(r'(<div class="ph">)\d+(</div>)',r'\1\2',s);p.write_text(s)
