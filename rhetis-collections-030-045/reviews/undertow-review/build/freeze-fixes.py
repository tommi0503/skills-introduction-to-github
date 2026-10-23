from pathlib import Path
import json,re
C=Path('/workspace/work/deliverables/undertow');S=Path('/workspace/work/agents/031')
p=C/'elements/card/element.css';s=p.read_text();a,sep,b=s.partition('/* UNDERTOW PRECISE COMPOSITIONS */')
b='\n'.join(l for l in b.splitlines() if '.quiet:has(>.parts>.note):not(:has(.fig)):not(:has(.mark))' not in l)
b=b.replace(':has(>.parts>.kick)', '.line:has(>.parts>.kick)')
b=b.replace('.line:has(>.parts>.mark):not(:has(.icon))','.line:has(>.parts>.mark):not(:has(.icon)):not(:has(.note))')
p.write_text(a+sep+b+'\n')
# Radial label geometry is computed from each share and start angle, not arbitrary coordinates.
p=C/'elements/chart-donut/element.css';s=p.read_text();s+='''
.donut[data-el="undertow-chart-donut"][style*="--undertow-start-angle:"] {--undertow-sector-mid:calc((var(--undertow-start-angle) + var(--v)*1.8)*1deg);}
.donut[data-el="undertow-chart-donut"][style*="--undertow-start-angle:"] .fig {left:calc(50% + sin(var(--undertow-sector-mid))*var(--undertow-label-radius));top:calc(50% - cos(var(--undertow-sector-mid))*var(--undertow-label-radius) - 22px);transform:translateX(-50%);}
.donut[data-el="undertow-chart-donut"][style*="--undertow-start-angle:"] .name {left:calc(50% + sin(var(--undertow-sector-mid))*var(--undertow-label-radius));top:calc(50% - cos(var(--undertow-sector-mid))*var(--undertow-label-radius) + 10px);transform:translateX(-50%);}
''';p.write_text(s)
p=C/'elements/chart-donut/element.json';d=json.loads(p.read_text());d['tokenDefaults'].pop('--undertow-label-x',None);d['tokenDefaults'].pop('--undertow-label-y',None);d['tokenDefaults']['--undertow-label-radius']='29%';p.write_text(json.dumps(d,indent=2)+'\n')
p=S/'precision-pages.py';s=p.read_text();s=s.replace("+card('80억 원 투자 유치!','이번 투자를 통해 시장 점유율을 확대하고 장기적 성장을 실현하고자 합니다.',cl='quiet')","+headline('<b>80억 원 투자 유치!</b>','이번 투자를 통해 시장 점유율을 확대하고 장기적 성장을 실현하고자 합니다.',cl='center')")
s=s.replace("+';--undertow-label-x:'+str(x)+'px;--undertow-label-y:'+str(y)+'px'", "+';--undertow-label-radius:29%'")
p.write_text(s)
print('freeze fixes applied')
