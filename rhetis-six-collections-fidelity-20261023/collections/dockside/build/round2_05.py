from pathlib import Path
import shutil
from bs4 import BeautifulSoup
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
(V/'round2').mkdir(exist_ok=True)
for n in [5,7,23]:
 p=V/f'reassembled/slide_{n:02}.png';q=V/f'round2/before-{n:02}.png'
 if p.exists() and not q.exists():shutil.copyfile(p,q)
# Source host palette, separate from the portable palette-free collection.
p=V/'assets/environment.css';s=p.read_text();s+='''\n.slide{--page:#fafafa;--ink:#303231;--n-1:#f7f7f7;--n-2:#eeeeee;--n-3:#dddddd;--n-4:#c6c6c6;--n-5:#aaaaaa;--n-6:#909090;--n-7:#737777;--n-8:#555858;--n-9:#383b3b;--a1:#3299f4;--a1-on:#ffffff;--a1-1-soft:#f1f8fc;--a1-2-soft:#e2f0fb;--a1-3-soft:#b4d9f5;--a1-4:#8ac2f4;--a1-5:#61aff5;--a1-6:#429ee6;--a1-7:#348bd0;--a1-8:#23669e;--a1-9:#174b79;--a2:#dafa81;--a2-on:#303231;--a3:#85c9c0;--a4:#b9a8e0}\n''';p.write_text(s)
p=C/'foundation/foundation.css';s=p.read_text();s+='''
/* Canvas foundation follows the source's fixed editorial margins. */
.slide.overrides{background:radial-gradient(ellipse at 110% 95%,var(--a1-2-soft),transparent 45%),radial-gradient(ellipse at 100% 3%,var(--a2-1-soft),transparent 25%),var(--page)}
.slide.overrides::before{display:none}
.slide.overrides .page{display:block;padding:0}
.slide.overrides .head{position:absolute;left:143px;top:65px;gap:calc(var(--gap) + 2px);z-index:3;max-width:1090px}
.slide.overrides .head.overrides{top:109px}
.slide.overrides .kicker{width:121px;height:39px;min-height:39px;padding:0;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 10px color-mix(in srgb,var(--ink) 15%,transparent)}
.slide.overrides .title{font-size:var(--type-60);line-height:var(--title-line)}
.slide.overrides .top{position:absolute;right:47px;top:35px;height:auto;display:block;font-size:var(--type-14);color:var(--n-7)}
.slide.overrides .top .deck{display:none}
.slide.overrides .body{position:absolute;left:143px;top:0;width:1090px;height:720px;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));gap:0}
.slide.overrides .rail{width:104px;border-left:17px solid var(--a1);background:var(--n-2);padding:0;display:block}
.slide.overrides .rail .seat{position:absolute;left:18px;width:50px;height:50px;border:2px solid var(--page);border-radius:var(--radius-sm);background:var(--n-2);font-size:var(--type-10)}
.slide.overrides .rail .seat:nth-child(1){top:9px;width:72px;height:72px}
'''
for i,y in enumerate([9,99,179,257,336,415,493,572,652],1):s+=f'.slide.overrides .rail .seat:nth-child({i}){{top:{y}px}}\n'
s+='''.slide.overrides .rail::after{content:"";position:absolute;left:0;top:36px;width:16px;height:20px;background:var(--a1);clip-path:polygon(0 0,100% 50%,0 100%)}\n''';p.write_text(s)
# Two distinct statistical visual grammars: stacked growth column and comparison bubbles.
p=C/'elements/card/element.css';s=p.read_text();r='.card[data-el="dockside-card"]'
for variant,x in [('line',302),('quiet',702)]:
 q=f'{r}.{variant}:has(>.parts>.fig):has(>.parts>.mark)'
 s+=f'''\n{q}{{position:absolute;left:{x}px;top:0;width:362px;height:720px;max-width:none;display:block;padding:0;border:0;border-radius:0;box-shadow:none;background:none;container-type:normal;flex:none}}
{q}::before{{content:"";position:absolute;left:0;top:196px;width:362px;height:414px;border:2px solid var(--page);border-radius:var(--radius);background:linear-gradient(150deg,color-mix(in srgb,var(--page) 50%,transparent),var(--n-1));box-shadow:0 16px 28px color-mix(in srgb,var(--ink) 8%,transparent)}}
{q}>.parts{{position:absolute;inset:0;display:block;padding:0;text-align:center}}
{q}>.parts>.kick{{position:absolute;left:32px;top:169px;width:300px;height:60px;padding:0 var(--gap-sm);display:flex;align-items:center;justify-content:center;gap:var(--gap-sm);font-size:var(--type-22);font-weight:var(--body-weight);color:var(--a1-on);background:var(--a1);border:0;border-radius:999px;box-shadow:0 8px 15px color-mix(in srgb,var(--a1) 35%,transparent)}}
{q}>.parts>.kick .icon{{width:20px;height:20px}}
{q}>.parts>.note{{position:absolute;left:25px;top:534px;width:312px;margin:0;font-size:var(--type-18);color:var(--n-7);line-height:var(--body-line);text-align:center}}
{q}>.parts>.name{{position:absolute;font-size:var(--type-16);font-weight:var(--body-weight);height:34px;padding:0 var(--gap-sm);display:flex;align-items:center;justify-content:center;background:var(--ink);color:var(--page);border-radius:999px;box-shadow:0 4px 8px color-mix(in srgb,var(--ink) 20%,transparent)}}
'''
q=f'{r}.line:has(>.parts>.fig):has(>.parts>.mark)'
s+=f'''{q}>.parts>.fig{{position:absolute;left:85px;top:283px;width:110px;height:222px;display:block;padding-top:38px;border-radius:var(--radius-sm) var(--radius-sm) 0 0;background:linear-gradient(var(--a1),var(--a1-2-soft));font-size:var(--type-20);font-weight:var(--name-weight);color:var(--page);line-height:var(--name-line)}}
{q}>.parts>.fig small{{font-size:var(--type-16);font-weight:var(--body-weight)}}
{q}>.parts>.mark{{position:absolute;left:85px;top:423px;width:110px;height:82px;display:grid;place-items:center;font-size:var(--type-20);color:var(--n-8);background:linear-gradient(var(--n-3),var(--n-2));border-radius:var(--radius-sm) var(--radius-sm) 0 0;box-shadow:none}}
{q}>.parts>.name{{left:205px;top:379px;width:102px}}
{q}::after{{content:"";position:absolute;left:43px;top:502px;width:276px;height:1px;background:var(--n-3)}}
'''
q=f'{r}.quiet:has(>.parts>.fig):has(>.parts>.mark)'
s+=f'''{q}>.parts>.fig{{position:absolute;left:126px;top:279px;width:173px;height:173px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);font-size:var(--type-44);font-weight:var(--name-weight);color:var(--page);background:linear-gradient(var(--a1) 0%,var(--a1-2-soft) 100%);border-radius:50%;line-height:var(--figure-line)}}
{q}>.parts>.fig small{{font-size:var(--type-20)}}
{q}>.parts>.mark{{position:absolute;left:58px;top:394px;width:106px;height:106px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(var(--n-3),var(--n-2));border-radius:50%;font-size:var(--type-28);font-weight:var(--name-weight);box-shadow:none;color:var(--n-8)}}
{q}>.parts>.mark small{{font-size:var(--type-16)}}
{q}>.parts>.name{{left:199px;top:453px;width:91px}}
{q}::after{{content:"";position:absolute;left:105px;top:372px;width:220px;height:1px;border-top:2px dashed var(--n-3);transform:rotate(-52deg);transform-origin:left}}
''';p.write_text(s)
p=V/'reassembled/slide_05.html';b=BeautifulSoup(p.read_text(),'html.parser');b.select_one('.slide')['class']=['slide','overrides'];b.select_one('.head')['class']=['head','overrides'];body=b.select_one('.body');body.clear()
def card(variant,fig,mark,name,kick,note):
 return f'<div class="card {variant}" data-el="dockside-card"><div class="parts"><p class="kick"><span class="icon" data-icon="check"></span>{kick}</p><b class="fig">{fig}</b><div class="mark">{mark}</div><b class="name">{name}</b><p class="note">{note}</p></div></div>'
h='<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+card('line','20XX<br><small>XXX,XXX명</small>','20XX','+150% 증가','전년 대비 이용자수 증가율','이용자 수 150% 증가로 운영 부담과<br>매출 가능성이 높아졌습니다.')+card('quiet','<small>20XX</small>40%','<small>20XX</small>20%','2배 증가','고객 중 불편을 느끼는 비율','불편 경험 비율이 2배 증가하며 서비스 개선<br>필요성이 분명해졌습니다.')+'</div>'
h+='<div class="prose quiet" data-el="dockside-prose" style="grid-column:1 / span 3;grid-row:5 / span 2"><p><b>Current Situation</b><br>현재 상황을 보여주는 주요 지표에<br>대해 그래프로 나타냅니다.</p></div>'
body.append(BeautifulSoup(h,'html.parser'));p.write_text(str(b))
# Quiet editorial aside uses the same source baseline in every slide.
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'''\n.prose[data-el="dockside-prose"].quiet:has(>p>b:first-child){padding:var(--gap-lg) 0 0;display:block;font-size:var(--type-16);line-height:var(--body-line)}\n.prose[data-el="dockside-prose"].quiet>p>b:first-child{display:block;font-size:var(--type-20);font-weight:var(--body-weight);color:var(--a1-7);margin-bottom:var(--gap)}\n.prose[data-el="dockside-prose"].quiet>p>b:first-child::after{content:"";display:block;width:30px;height:2px;background:var(--a1-7);margin-top:var(--gap-sm)}\n''')
for p in C.rglob('*.css'):
 q=V/'assets/collection'/p.relative_to(C);shutil.copyfile(p,q)
print('Source05 rebuilt')
