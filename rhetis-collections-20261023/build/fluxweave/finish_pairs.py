from pathlib import Path
O=Path('/workspace/output/fluxweave');p=O/'elements/card/element.css';s=p.read_text().replace('.mark>.icon)', '.mark>.icon[data-icon])').replace('>.mark>.icon{','>.mark>.icon[data-icon]{');s+='''
.card[data-el="fluxweave-card"]>.parts>.lines>.pt:not(:first-child)::after{display:none;}
.card[data-el="fluxweave-card"]>.parts>.areas{grid-area:2/1;min-height:0;padding:calc(var(--gap-sm)*2.3) calc(var(--gap-sm)*1.5) calc(var(--gap-lg)*1.8) calc(var(--gap)*2.5);border:0;z-index:0;}
.card[data-el="fluxweave-card"]>.parts>.bars{z-index:1;}
.card[data-el="fluxweave-card"]>.parts>.lines{z-index:2;}
.card[data-el="fluxweave-card"]>.parts>.areas>.series{inset:calc(var(--gap-sm)*2.3) calc(var(--gap-sm)*1.5) calc(var(--gap-lg)*1.8) calc(var(--gap)*2.5);}
.card[data-el="fluxweave-card"]>.parts>.areas>.series>.pt{--fluxweave-height:calc(var(--v)/var(--max)*100cqh);margin-top:calc(100cqh - var(--fluxweave-height));}
.card[data-el="fluxweave-card"]>.parts>.areas>.series>.name,.card[data-el="fluxweave-card"]>.parts>.areas>.axis,.card[data-el="fluxweave-card"]>.parts>.areas>.series>.pt>b{display:none;}
.card[data-el="fluxweave-card"]>.parts>.areas>.series>.pt::before{background:color-mix(in srgb,var(--a2) 28%,var(--n-1));}
.card[data-el="fluxweave-card"]>.parts>.areas>.series>.pt::after{display:none;}
''';p.write_text(s)
p=O/'foundation/foundation.css';s=p.read_text().replace('.group:has(>.card>.parts>.mark>.icon)', '.group:has(>.card>.parts>.mark>.icon[data-icon])');p.write_text(s)
p=Path('/workspace/work/fluxweave/reassemble.py');s=p.read_text();s=s.replace("return el('card','card','<div class=\"parts\"><p class=\"name\">'+title+'</p>'+b+l+leg+'</div>')", "a=el('areas','chart-area','<div class=\"series tone-2\"><b class=\"name\">'+('고객사 수' if unit=='명' else '재계약률')+'</b>'+''.join(f'<div class=\"pt\" style=\"--v:{v}\"></div>' for v in linevals)+'</div><div class=\"axis\">'+''.join('<span>'+str(2080+i)+'</span>' for i in range(len(linevals)))+'</div>',style=f'--max:{maximum}')\n return el('card','card','<div class=\"parts\"><p class=\"name\">'+title+'</p>'+a+b+l+leg+'</div>')")
p.write_text(s)
