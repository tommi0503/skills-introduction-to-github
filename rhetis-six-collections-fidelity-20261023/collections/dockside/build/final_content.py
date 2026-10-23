from pathlib import Path
from bs4 import BeautifulSoup
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
p=C/'elements/mindmap/element.css';s=p.read_text();r='.mindmap[data-el="dockside-mindmap"]:has(>.branch:nth-child(5):last-child)'
s+=f'\n{r}>.branch::after{{position:absolute;width:calc(50% + var(--gap));height:calc(100% + var(--gap));background:none;border:0}}\n'
for n,left,top in [(2,True,True),(3,True,False),(4,False,True),(5,False,False)]:
 s+=f'{r}>.branch:nth-child({n})::after{{left:{"100%" if left else "auto"};right:{"auto" if left else "100%"};top:{"50%" if top else "auto"};bottom:{"auto" if top else "50%"};border-{"top" if top else "bottom"}:1px solid var(--n-4);border-{"right" if left else "left"}:1px solid var(--n-4);border-radius:var(--radius)}}\n'
p.write_text(s)
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'\n.slide.cover .body{width:100%;height:100px;flex:none;z-index:1}\n')
p=V/'reassembled/slide_30.html';b=BeautifulSoup(p.read_text(),'html.parser');body=b.new_tag('div',attrs={'class':'body'})
for i,(icon,t) in enumerate([('mail','contact@miridih.com'),('phone','연락처를 입력하세요.'),('messages-square','SNS를 입력하세요.')]):
 h=f'<div class="pill" data-el="dockside-pill" style="grid-column:{1+i*4} / span 4;grid-row:1 / span 6"><div class="parts"><span class="mark"><span class="icon" data-icon="{icon}"></span></span><b class="name">{t}</b></div></div>'
 body.append(BeautifulSoup(h,'html.parser'))
b.select_one('.lockup').insert_after(body);p.write_text(str(b))
for p in C.rglob('*.css'):
 q=V/'assets/collection'/p.relative_to(C);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
