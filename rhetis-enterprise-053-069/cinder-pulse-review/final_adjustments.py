from pathlib import Path
import json,re,shutil
B=Path(__file__).parent;C=B.parent/'cinder-pulse';R=Path('/workspace/work/ref')
def add(n,s):
 p=C/f'elements/{n}/element.css';p.write_text(p.read_text()+'\n'+s)
add('architecture','@container (max-height:420px){.arch[data-el="cinder-pulse-architecture"] .layer{padding:var(--gap-sm);gap:var(--gap-sm);}.arch[data-el="cinder-pulse-architecture"] .name{font-size:var(--type-18);}.arch[data-el="cinder-pulse-architecture"] .chip{font-size:var(--type-14);}}')
add('bullet',':is(.bullet,.bullets)[data-el="cinder-pulse-bullet"] .bullet{padding-bottom:calc(var(--gap-lg)*1.3);}:is(.bullet,.bullets)[data-el="cinder-pulse-bullet"] .bullet::after,.bullet[data-el="cinder-pulse-bullet"]::after{max-width:calc(100% - var(--gap-sm)*2);}.bullet[data-el="cinder-pulse-bullet"]::before,.bullet[data-el="cinder-pulse-bullet"]::after{bottom:0;}@container (max-height:300px){.bullets[data-el="cinder-pulse-bullet"]{gap:var(--gap-sm);}.bullets[data-el="cinder-pulse-bullet"] .bullet{padding:0 0 var(--gap);}.bullets[data-el="cinder-pulse-bullet"] .note{font-size:var(--type-12);}}')
add('chart-donut','.donuts[data-el="cinder-pulse-chart-donut"]{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:var(--gap-sm);align-content:center;justify-items:center;}.donuts[data-el="cinder-pulse-chart-donut"]>.donut{width:min(100%,calc((100cqh - var(--gap-sm))/2));height:auto;max-height:none;aspect-ratio:1;}.donuts[data-el="cinder-pulse-chart-donut"]>.donut .fig{line-height:var(--name-line);}@container (max-width:160px){.donut[data-el="cinder-pulse-chart-donut"] .fig{font-size:var(--type-22);}.donut[data-el="cinder-pulse-chart-donut"] .name{font-size:var(--type-12);}}')
add('funnel','@container (max-height:420px){.funnel[data-el="cinder-pulse-funnel"] .stage{padding:calc(var(--gap-sm)/2);min-height:0;}.funnel[data-el="cinder-pulse-funnel"] .name{font-size:var(--type-14);}.funnel[data-el="cinder-pulse-funnel"] .fig{font-size:var(--type-20);}}')
add('heatmap','.heat.calendar[data-el="cinder-pulse-heatmap"]{display:grid;grid-template-rows:auto repeat(7,minmax(0,1fr));}.heat.calendar[data-el="cinder-pulse-heatmap"] .heads{padding-left:0;}.heat.calendar[data-el="cinder-pulse-heatmap"] .row{min-height:0;}.heat.calendar[data-el="cinder-pulse-heatmap"] .cell{min-height:0;aspect-ratio:auto;height:100%;}')
add('logo-group','.logos[data-el="cinder-pulse-logo-group"]{grid-auto-rows:minmax(0,1fr);align-content:stretch;}.logos[data-el="cinder-pulse-logo-group"] .seat{height:100%;width:auto;max-height:100%;aspect-ratio:1;}')
add('chart-stack','.stacks[data-el="cinder-pulse-chart-stack"] .seg:nth-of-type(2){background:var(--n-4);color:var(--ink);}.stacks[data-el="cinder-pulse-chart-stack"] .seg:nth-of-type(3){background:var(--a1-2-soft);color:var(--ink);}.stacks[data-el="cinder-pulse-chart-stack"] .seg:nth-of-type(4){background:var(--a1-4-muted);color:var(--ink);}')
# Code's real monospace family is a declared kit font token.
p=C/'kit/css/tokens.css';s=p.read_text().replace('.slide {','.slide {\n  --cinder-pulse-code-font: \'Nanum Gothic Coding\';',1);p.write_text(s)
p=C/'kit/kit.json';j=json.loads(p.read_text());j['extensions']['--cinder-pulse-code-font']='font';p.write_text(json.dumps(j,ensure_ascii=False,indent=2))
add('code','.code[data-el="cinder-pulse-code"] .lines{font-family:var(--cinder-pulse-code-font);}')
mandatory={'card','callout','chart-area','chart-bar','chart-donut','chart-line'}
for p in (C/'elements').glob('*/fixtures/*.html'):
 if p.parent.parent.name in mandatory:continue
 s=p.read_text();s=re.sub(r'grid-column:\s*\d+\s*/\s*span\s*\d+;\s*grid-row:\s*\d+\s*/\s*span\s*\d+','grid-column:1 / span 12; grid-row:1 / span 6',s,count=1)
 p.write_text(s)
# Portable review fonts: only actual loaded families, no external requests.
f=B/'fonts';f.mkdir(exist_ok=True);css=[]
for fam,src,weight in [('Pretendard Variable','pretendard/PretendardVariable.woff2','100 900'),('Nanum Pen','nanum-pen-script/NanumPenScript-Regular.woff2','400'),('Nanum Gothic Coding','nanum-gothic-coding/NanumGothicCoding-Regular.woff2','400')]:
 source=R/'fonts/artifacts'/src
 if not source.exists():
  source=next((R/'fonts/artifacts/nanum-gothic-coding').glob('*Regular*'))
 shutil.copy2(source,f/source.name);css.append(f"@font-face{{font-family:'{fam}';src:url('{source.name}') format('woff2');font-weight:{weight};font-style:normal;}}")
(f/'fonts.css').write_text('\n'.join(css))
for p in [B/'build_replica.py',B/'build_library.py',B/'build_reassembled.py']:
 s=p.read_text().replace('http://127.0.0.1:8765/fonts/fonts.css','../fonts/fonts.css');p.write_text(s)
# Explicit source heading line breaks preserve Korean word grouping.
p=B/'build_reassembled.py';s=p.read_text().replace("title=D[n-1]['title'];k=", "title={4:'미션과 비전,<br>핵심 가치',5:'미리컴퍼니<br>대표 인사말',8:'조직문화와<br>인재상',10:'사업 성과<br>한눈에 보기',13:'미리컴퍼니<br>주력 사업',16:'표준 프로젝트<br>일정',19:'성장 전략과<br>향후 계획'}.get(n,D[n-1]['title']);k=")
p.write_text(s)
print('Final geometry / portable font pass')
