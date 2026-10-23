from pathlib import Path
from bs4 import BeautifulSoup
import shutil
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
def add(folder,s):
 p=C/('foundation/foundation.css' if folder=='foundation' else f'elements/{folder}/element.css');p.write_text(p.read_text()+'\n'+s+'\n')
def edit(n,fn):
 p=V/f'reassembled/slide_{n:02}.html';b=BeautifulSoup(p.read_text(),'html.parser');fn(b);p.write_text(str(b))
def contacts(b):
 for p in b.select('.body>.pill'):p['style']='grid-column:1 / span 12;grid-row:1 / span 6'
edit(30,contacts)
def partial(b):
 p=b.select('.card')[-1]
 for q in p.select('.name,.note'):q.clear()
edit(6,partial)
r='.hub[data-el="dockside-hub"]:has(>.spoke:nth-child(5):last-child)'
add('hub',r+'::before{display:none}'+r+'>.spoke>.name{font-size:var(--type-18)}'+r+'>.spoke>.note{font-size:var(--type-16);line-height:var(--body-line);letter-spacing:var(--dockside-detail-track)}')
r='.steps[data-el="dockside-steps"]:has(>.step:nth-child(3):last-child)'
add('steps',r+'>.step>.note{font-size:var(--type-16);line-height:var(--body-line)}')
r='.list[data-el="dockside-list"].divided:not(.num):has(>.item:nth-child(3):last-child):has(.mark>.icon):not(:has(.name>.icon))'
add('list',r+'::before{content:"";position:absolute;left:665px;top:165px;width:78px;height:90px;background:var(--a1-3-soft);clip-path:polygon(0 0,100% 50%,0 100%)}')
r='.card[data-el="dockside-card"].line:has(.kick):has(.parts>.list)'
add('card',r+':first-child::before{top:160px}'+r+':first-child .list::after{content:"";position:absolute;left:162px;top:145px;width:14px;height:14px;border-right:4px solid var(--a1);border-bottom:4px solid var(--a1);transform:rotate(45deg)}')
add('list','.card>.parts>.note>.list[data-el="dockside-list"]>.item>.name,.card.line>.parts>.list[data-el="dockside-list"]>.item>.name{text-align:left}')
def badges(b):
 for p in b.select('.card>.parts>.mark,.card>.parts>.kick'):p.append(BeautifulSoup('<span class="icon" data-icon="circle-check"></span>','html.parser'))
edit(29,badges)
r='.card[data-el="dockside-card"].line:has(.mark>.icon):has(.note>.list)'
add('card',r+'>.parts>.mark>.icon:nth-of-type(2),'+r+'>.parts>.kick>.icon:nth-of-type(2){position:absolute;left:58px;top:55px;width:23px;height:23px;padding:0;border:0;border-radius:50%;background:var(--a1);color:var(--a1-on);box-shadow:none}')
r='.mindmap[data-el="dockside-mindmap"]:has(.person):has(>.branch:nth-child(5):last-child)'
s=r+'>.branch::after{content:"";position:absolute;left:243px;right:auto;top:56px;bottom:auto;width:46px;height:108px;border:0;border-top:2px solid var(--n-3);border-right:2px solid var(--n-3);border-radius:0 16px 0 0;background:none;z-index:-1;transform:none}'+r+'>.branch::before{content:"";position:absolute;left:289px;right:auto;top:164px;bottom:auto;width:34px;height:0;border:0;border-top:2px solid var(--n-3);background:none;transform:none;z-index:-1}'
s+=r+'>.branch:nth-child(3)::after{top:auto;bottom:56px;border-top:0;border-bottom:2px solid var(--n-3);border-radius:0 0 16px 0}'+r+'>.branch:nth-child(3)::before{top:-52px}'
s+=r+'>.branch:nth-child(4)::after,'+r+'>.branch:nth-child(5)::after{left:auto;right:243px;width:114px;border-right:0;border-left:2px solid var(--n-3);border-radius:16px 0 0 0}'+r+'>.branch:nth-child(4)::before,'+r+'>.branch:nth-child(5)::before{left:-147px;right:auto;width:33px}'+r+'>.branch:nth-child(5)::after{top:auto;bottom:56px;border-top:0;border-bottom:2px solid var(--n-3);border-radius:0 0 0 16px}'+r+'>.branch:nth-child(5)::before{top:-52px}'
add('mindmap',s)
def arrow(b):
 p=b.select_one('.prose:not(.quiet)>p')
 if p:p.append(BeautifulSoup('<span class="icon" data-icon="arrow-right"></span>','html.parser'))
edit(10,arrow)
add('prose','.prose[data-el="dockside-prose"]:not(.quiet):not(.lead):has(p>.icon){position:absolute}.prose[data-el="dockside-prose"]:not(.quiet):not(.lead)>p>.icon{position:absolute;left:684px;top:-56px;width:54px;height:54px;padding:15px;color:var(--page);background:var(--ink);border-radius:50%;box-shadow:0 5px 10px color-mix(in srgb,var(--ink) 15%,transparent)}')
add('foundation','.slide.cover.overrides:has(.lead) .meta{margin:0;top:354px;font-size:var(--type-16)}.slide.cover.overrides:has(.lead) .lockup .lead{margin:0}.slide.overrides .rail::after{display:none}.slide.overrides .rail>.seat{width:50px;height:50px}.slide.overrides .rail>.seat:first-child{top:20px}.slide.overrides .rail>.seat.on{width:72px;height:72px}.slide.overrides .rail>.seat.on::before{content:"";position:absolute;left:-20px;top:26px;width:16px;height:20px;clip-path:polygon(0 0,100% 50%,0 100%);background:var(--a1)}')
# Gray placeholders preserve each source dock icon's measured bounding box.
for n in range(4,30):
 active=0 if n<=7 else 1 if n<=11 else 2 if n<=16 else 3 if n<=18 else 4 if n==19 else 5 if n<=23 else 6 if n<=26 else 7 if n<=28 else 8
 def f(b):
  for j,p in enumerate(b.select('.rail>.seat')):
   p['class']=['seat']+(['on'] if j==active else [])
 edit(n,f)
for i,t in enumerate([9,87,166,245,324,403,482,561,640],1):add('foundation',f'.slide.overrides .rail>.seat.on:nth-child({i}){{top:{t}px}}')
for p in C.rglob('*.css'):shutil.copyfile(p,V/'assets/collection'/p.relative_to(C))
p=R/'build/round2_preview.py';p.write_text(p.read_text().replace('load(page,f);out=', 'load(page,f);page.wait_for_timeout(600);out='))
