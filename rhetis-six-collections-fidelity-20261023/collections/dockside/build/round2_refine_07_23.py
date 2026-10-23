from pathlib import Path
from bs4 import BeautifulSoup
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
p=V/'reassembled/slide_07.html';b=BeautifulSoup(p.read_text(),'html.parser');a=b.select('.ring');a[0].clear();a[0].append(BeautifulSoup('<b class="name"></b><div class="fig"><span class="icon" data-icon="plus"></span></div>','html.parser'));a[1].clear();a[1].append(BeautifulSoup('<p class="note">Keyword</p><div class="fig"><div class="seat" data-ph="1"></div></div><b class="name">중심 키워드</b>','html.parser'));p.write_text(str(b))
p=C/'elements/concentric/element.css';r='.orbit[data-el="dockside-concentric"]:has(>.ring:nth-child(2):last-child)';p.write_text(p.read_text()+f'''\n{r}>.ring:first-child>.fig{{left:225px;top:15px;width:43px;height:43px;display:grid;place-items:center;background:var(--ink);color:var(--page);border-radius:50%;box-shadow:0 5px 10px color-mix(in srgb,var(--ink) 20%,transparent)}}{r}>.ring:first-child>.fig>.icon{{width:24px;height:24px}}{r}>.ring:nth-child(2)>.note{{position:absolute;top:39px;left:0;width:100%;font-size:var(--type-16);color:var(--n-6)}}{r}>.ring:nth-child(2)>.fig{{position:absolute;left:61px;top:67px;width:84px;height:60px}}{r}>.ring:nth-child(2)>.fig>.seat{{width:84px;height:60px;aspect-ratio:auto}}\n''')
p=C/'elements/list/element.css';r='.list[data-el="dockside-list"].num:not(.divided):has(>.item:nth-child(4):last-child)';p.write_text(p.read_text()+f'\n{r}{{gap:calc(var(--gap) + 2px)}}\n')
p=V/'reassembled/slide_23.html';b=BeautifulSoup(p.read_text(),'html.parser')
for n in b.select('.step>.note'):n.clear();n.append('해당 시기의 주요 활동과 목표를 2~3줄로 작성합니다.')
intro='<div class="prose quiet" data-el="dockside-prose" style="grid-column:1 / span 12;grid-row:1 / span 6"><p>아이디어를 서비스로 발전시키는 단계별 실행 흐름을 보여주는 페이지<br>입니다. 구체화부터 개선까지의 추진 과정을 순서대로 제시합니다.</p></div>'
b.select_one('.body').append(BeautifulSoup(intro,'html.parser'));p.write_text(str(b))
p=C/'elements/steps/element.css';r='.steps[data-el="dockside-steps"]:has(>.step:nth-child(5):last-child):has(.mark>.icon)';s=p.read_text()
for i,(x,y) in enumerate([(17,447),(236,403),(454,357),(672,312),(890,266)],1):s+=f'\n{r}>.step:nth-child({i}){{left:{x}px;top:{y}px}}'
s+=f'''\n{r}::after{{content:"";position:absolute;left:217px;top:250px;width:873px;height:398px;background:repeating-linear-gradient(to right,var(--n-3) 0 1px,transparent 1px 218px);z-index:0}}{r}>.step{{width:188px;height:213px;z-index:1;background:linear-gradient(130deg,var(--n-1),color-mix(in srgb,var(--a1-2-soft) 35%,var(--page)))}}{r}>.step>.mark{{left:12px;top:-35px}}{r}>.step::before{{left:18px;top:56px}}{r}>.step>.name{{left:18px;top:78px;width:154px}}{r}>.step>.note{{left:18px;top:110px;width:154px}}\n''';p.write_text(s)
p=C/'elements/callout/element.css';p.write_text(p.read_text()+'\n.callout[data-el="dockside-callout"]:has(>p>b:first-child){left:36px}\n')
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'''\n.prose[data-el="dockside-prose"].quiet:not(:has(>p>b:first-child)){position:absolute;left:569px;top:141px;width:490px;height:auto;padding:0;font-size:var(--type-16);line-height:var(--body-line);display:block}\n''')
for p in C.rglob('*.css'):shutil.copyfile(p,V/'assets/collection'/p.relative_to(C))
