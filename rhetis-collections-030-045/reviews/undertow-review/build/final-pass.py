from pathlib import Path
import json,re
C=Path('/workspace/work/deliverables/undertow');R=Path('/workspace/work/deliverables/undertow-review')
def add(f,s):
 p=C/'elements'/f/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('chart-area','''
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] {background-size:calc(100% - 36px) 100%;background-position:28px 0;background-repeat:no-repeat;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt b {position:fixed;left:anchor(var(--undertow-self) center);top:calc(anchor(var(--undertow-self) top) - 24px);transform:none;width:40px;margin-left:calc(var(--gap)*-5/6);text-align:center;}
''')
add('card','''
.card[data-el="undertow-card"].quiet:has(>.parts>.note):not(:has(.fig)):not(:has(.mark)) .name {white-space:normal;}
@container (max-width:280px) {.card[data-el="undertow-card"].on .name {font-size:var(--type-16);padding-bottom:0;}}
''')
add('hub','.hub[data-el="undertow-hub"]:has(>.spoke:nth-child(5)):not(:has(>.spoke:nth-child(6))) .core .icon {width:64px;height:64px;}')
# Correct the independent replica source without resetting its loaded fonts or past fixes.
p=R/'replica/replica.css';s=p.read_text().replace('font-size:40px;letter-spacing:-1.3px','font-size:44px;letter-spacing:-1.3px');p.write_text(s)
for i in range(1,14):
 p=R/f'replica/{i:02}.html';s=p.read_text()
 if i in [1,2]:
  s=s.replace('#529f8b','#9bffd4')
 if i==1:
  s=s.replace('top:139px;font-size:110px','top:137px;font-size:112px').replace('line-height:.92','line-height:.84')
 if i==4:
  s=s.replace('</main>','<div style="position:absolute;left:83px;top:577px;width:84px;height:84px;color:#529f8b"><svg width="84" height="84" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M9 18h6m-5 4h4m-5-7a6 6 0 1 1 6 0l-1 3h-4Z"/></svg></div></main>')
 if i==6:
  s=s.replace('top:400px;width:480px;height:480px;border-radius:50%;background:#ccc;text-align:center;padding-top:58px','top:400px;width:480px;height:480px;border-radius:50%;background:#ccc;text-align:center;padding-top:38px').replace('top:572px;width:285px;height:285px;border-radius:50%;background:#7a7a7a;text-align:center;padding-top:58px','top:572px;width:285px;height:285px;border-radius:50%;background:#7a7a7a;text-align:center;padding-top:28px')
 if i==7:
  s=s.replace('font-size:21px;padding:20px 27px','font-size:18px;padding:20px 27px')
 if i==8:
  s=s.replace('width:78px;height:78px','width:64px;height:64px').replace('font-size:37px','font-size:36px').replace('font-size:15px;width:230px','font-size:14px;width:230px')
  s=s.replace('class="icon"','class="icon" style="width:64px;height:64px"')
 if i==9:
  s=s.replace('</svg></div><div class="circle"','<rect x="84" y="34" width="10" height="10" fill="#999"/><text x="98" y="44" font-size="12">누적 판매량</text><rect x="172" y="34" width="10" height="10" fill="#529f8b"/><text x="186" y="44" font-size="12">재구매율</text><path d="M473 217Q523 212 536 171L521 167L564 152L567 192L549 183Q528 217 473 217Z" fill="white" opacity=".9"/></svg></div><div class="circle"')
  # General insertion in case class order was changed by the previous replica fix.
  if '<rect x="84" y="34"' not in s:
   idx=s.find('</svg>',s.find('viewBox="0 0 700 410"'))
   if idx>=0:s=s[:idx]+'<rect x="84" y="34" width="10" height="10" fill="#999"/><text x="98" y="44" font-size="12">누적 판매량</text><rect x="172" y="34" width="10" height="10" fill="#529f8b"/><text x="186" y="44" font-size="12">재구매율</text><path d="M473 217Q523 212 536 171L521 167L564 152L567 192L549 183Q528 217 473 217Z" fill="white" opacity=".9"/>'+s[idx:]
 if i==12:
  s=s.replace('font-size:16px;line-height:1.35','font-size:14px;line-height:1.45').replace('font-size:17px;margin-top:1px','font-size:14px;margin-top:1px')
 if i==13:
  s=s.replace('left:526px;top:308px;font-size:29px','left:528px;top:316px;font-size:22px')
  s=s.replace('text-align:center;font-size:21px;line-height:1.2','text-align:center;font-size:18px;line-height:1.2')
  s=s.replace('</main>','<div style="position:absolute;left:219px;top:354px;width:46px;height:25px;clip-path:polygon(0 0,100% 0,50% 100%);background:#f0f0f0"></div></main>')
 p.write_text(s)
print('final pass source and replica corrections')
