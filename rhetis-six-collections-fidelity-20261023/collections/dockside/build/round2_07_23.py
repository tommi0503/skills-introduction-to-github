from pathlib import Path
import shutil
from bs4 import BeautifulSoup
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
def edit(n,body):
 p=V/f'reassembled/slide_{n:02}.html';b=BeautifulSoup(p.read_text(),'html.parser');b.select_one('.slide')['class']=['slide','overrides'];b.select_one('.head')['class']=['head'];q=b.select_one('.body');q.clear();q.append(BeautifulSoup(body,'html.parser'));p.write_text(str(b))
#07 exact nested orbit plus numbered problem bands.
h='<div class="orbit" data-el="dockside-concentric" style="grid-column:1 / span 12;grid-row:1 / span 6"><div class="ring"><b class="name">Keyword</b><div class="fig"><div class="seat" data-ph="1"></div></div></div><div class="ring"><b class="name">중심 키워드</b><b class="fig"></b></div></div>'
h+='<div class="list num" data-el="dockside-list" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(f'<div class="item"><b class="name">{t}</b><p class="note">구체적인 불편사항이나 문제상황을 간단히<br>작성합니다.</p></div>' for t in ['시간 소요','비용 부담','정보 부족','접근성 제한'])+'</div>';edit(7,h)
p=C/'elements/concentric/element.css';r='.orbit[data-el="dockside-concentric"]:has(>.ring:nth-child(2):last-child)';s=p.read_text()+f'''
{r}{{position:absolute;left:21px;top:256px;width:366px;height:366px;display:block;container-type:normal}}
{r}::before{{content:"";position:absolute;inset:0;border:2px dashed var(--a1-4);border-radius:50%;background:none}}
{r}>.ring{{position:absolute;left:50%;top:50%;bottom:auto;transform:translate(-50%,-50%);padding:0;display:block;width:314px;height:314px;border:4px solid var(--a1-5);background:linear-gradient(135deg,var(--a1-1-soft),var(--a1-3-soft));box-shadow:none}}
{r}>.ring:nth-child(2){{width:210px;height:210px;border:2px solid var(--page);background:var(--page);box-shadow:0 12px 18px color-mix(in srgb,var(--ink) 6%,transparent)}}
{r}>.ring:first-child>.name{{position:absolute;left:0;top:88px;width:100%;font-size:var(--type-16);font-weight:var(--body-weight);color:var(--n-6);z-index:3}}
{r}>.ring:first-child>.fig{{position:absolute;left:111px;top:116px;width:84px;height:60px;z-index:3}}
{r}>.ring:first-child>.fig>.seat{{width:84px;height:60px;aspect-ratio:auto}}
{r}>.ring:nth-child(2)>.name{{position:absolute;left:0;top:132px;width:100%;font-size:var(--type-24);color:var(--a1-7);font-weight:var(--name-weight)}}
''';p.write_text(s)
p=C/'elements/list/element.css';r='.list[data-el="dockside-list"].num:not(.divided):has(>.item:nth-child(4):last-child)';s=p.read_text()+f'''
{r}{{position:absolute;left:446px;top:184px;width:644px;height:462px;display:flex;flex-direction:column;gap:var(--gap) ;padding:0;container-type:normal;counter-reset:dockside-problem}}
{r}>.item{{position:relative;flex:none;height:96px;padding:0;border:2px solid var(--page);border-radius:var(--radius-sm);background:linear-gradient(135deg,color-mix(in srgb,var(--page) 50%,transparent),var(--n-1));box-shadow:0 5px 10px color-mix(in srgb,var(--ink) 5%,transparent)}}
{r}>.item::before{{counter-increment:dockside-problem;content:"Problem " counter(dockside-problem,decimal-leading-zero);position:absolute;left:18px;top:22px;width:138px;height:46px;display:flex;align-items:center;justify-content:center;background:var(--a1);color:var(--a1-on);font-size:var(--type-18);font-weight:var(--body-weight);border:0;border-radius:999px;box-shadow:0 6px 12px color-mix(in srgb,var(--a1) 35%,transparent)}}
{r}>.item>.name{{position:absolute;left:180px;top:29px;width:115px;font-size:var(--type-24);font-weight:var(--name-weight);color:var(--ink);line-height:var(--name-line);white-space:nowrap}}
{r}>.item>.note{{position:absolute;left:318px;top:19px;width:302px;font-size:var(--type-18);line-height:var(--body-line);color:var(--n-7)}}
{r}>.item::after{{content:"";position:absolute;left:297px;top:20px;width:1px;height:50px;background:var(--n-3)}}
''';p.write_text(s)
#23 five ascending execution cards. mark contains only the icon, step label is automatic.
icons=['lightbulb','settings','clipboard-list','contact-round','users-round'];titles=['아이디어 구체화','프로토타입 개발','베타테스트 진행','정식 서비스 오픈','사용자 피드백 반영']
h='<div class="steps" data-el="dockside-steps" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(f'<div class="step"><span class="mark"><span class="icon" data-icon="{ic}"></span></span><b class="name">{t}</b><p class="note">핵심 시기와 주요 활동과<br>목표를 2~3줄로 작성합니다.</p></div>' for ic,t in zip(icons,titles))+'</div>'
h+='<div class="callout" data-el="dockside-callout" style="grid-column:8 / span 5;grid-row:5 / span 1"><span class="icon" data-icon="bell-ring"></span><p><b>Key Message</b><br>단계별 검증을 통해 리스크를 최소화합니다.</p></div>'
edit(23,h)
p=C/'elements/steps/element.css';r='.steps[data-el="dockside-steps"]:has(>.step:nth-child(5):last-child):has(.mark>.icon)';s=p.read_text()+f'''
{r}{{position:absolute;inset:0;display:block;padding:0;container-type:normal;counter-reset:dockside-step}}
{r}::before{{content:"";position:absolute;left:0;top:220px;width:1094px;height:458px;border:2px solid var(--page);border-radius:var(--radius);background:linear-gradient(135deg,color-mix(in srgb,var(--page) 50%,transparent),var(--a1-1-soft));box-shadow:0 12px 24px color-mix(in srgb,var(--ink) 7%,transparent)}}
{r}>.step{{position:absolute;width:180px;height:212px;display:block;padding:0;border:2px solid var(--page);border-radius:var(--radius);background:linear-gradient(130deg,var(--n-1),var(--a1-2-soft));box-shadow:0 8px 15px color-mix(in srgb,var(--ink) 9%,transparent)}}
'''
for i,(x,y) in enumerate([(28,446),(245,402),(462,358),(679,314),(896,270)],1):s+=f'{r}>.step:nth-child({i}){{left:{x}px;top:{y}px}}\n'
s+=f'''{r}>.step::before{{counter-increment:dockside-step;content:"Step " counter(dockside-step,decimal-leading-zero);position:absolute;left:22px;top:49px;font-size:var(--type-14);color:var(--a1-7);height:auto;width:auto;background:none;border:0}}
{r}>.step::after{{content:"";position:absolute;left:22px;right:22px;bottom:16px;height:8px;background:var(--a1);border:0;border-radius:999px;top:auto;width:auto}}
{r}>.step>.mark{{position:absolute;left:20px;top:-36px;width:66px;height:66px;display:grid;place-items:center;background:var(--a1);color:var(--a1-on);border:2px solid var(--page);border-radius:var(--radius-sm);box-shadow:0 6px 12px color-mix(in srgb,var(--a1) 30%,transparent);margin:0}}
{r}>.step>.mark>.icon{{width:38px;height:38px}}
{r}>.step>.name{{position:absolute;left:22px;top:74px;width:142px;font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line);text-align:left;word-break:keep-all}}
{r}>.step>.note{{position:absolute;left:22px;top:110px;width:138px;font-size:var(--type-14);line-height:var(--body-line);text-align:left;word-break:keep-all}}
''';p.write_text(s)
# Page23 conclusion is a quiet glass message rather than accent fill.
p=C/'elements/callout/element.css';r='.callout[data-el="dockside-callout"]:has(>p>b:first-child)';p.write_text(p.read_text()+f'''\n{r}{{position:relative;left:-78px;top:92px;width:388px;height:72px;min-height:72px;padding:var(--gap-sm) var(--pad);display:flex;align-items:center;gap:var(--gap);background:var(--n-1);color:var(--n-7);border:2px solid var(--page);border-radius:999px;box-shadow:0 6px 12px color-mix(in srgb,var(--ink) 6%,transparent)}}{r}>.icon{{width:42px;height:42px;background:var(--ink);color:var(--page);border-radius:50%;padding:8px}}{r}>p{{font-size:var(--type-14);line-height:var(--body-line)}}{r}>p>b{{font-weight:var(--name-weight)}}\n''')
#05 parent's detailed correction.
p=C/'elements/card/element.css';p.write_text(p.read_text()+'''\n.card[data-el="dockside-card"]:is(.quiet,.line):has(>.parts>.fig):has(>.parts>.mark)>.parts>.note{line-height:var(--label-line)}\n.card[data-el="dockside-card"].quiet:has(>.parts>.fig):has(>.parts>.mark)>.parts>.fig{font-size:var(--type-40);z-index:2}\n.card[data-el="dockside-card"].quiet:has(>.parts>.fig):has(>.parts>.mark)>.parts>.mark{z-index:3}\n.card[data-el="dockside-card"].quiet:has(>.parts>.fig):has(>.parts>.mark)::after{z-index:0}\n.card[data-el="dockside-card"].quiet:has(>.parts>.fig):has(>.parts>.mark)>.parts::after{content:"";position:absolute;left:118px;top:497px;width:190px;height:1px;border-top:2px dashed var(--n-3);transform:rotate(-25deg);transform-origin:left;z-index:0}\n.card[data-el="dockside-card"].quiet:has(>.parts>.fig):has(>.parts>.mark)>.parts>.mark::after{display:none}\n''')
for p in C.rglob('*.css'):shutil.copyfile(p,V/'assets/collection'/p.relative_to(C))
