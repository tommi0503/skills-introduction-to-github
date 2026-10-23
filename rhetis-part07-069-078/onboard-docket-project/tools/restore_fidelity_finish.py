from pathlib import Path
import re
P=Path(__file__).parent;C=P/'onboard-docket';R=P/'reassembled'
def q(n):return '[data-el="onboard-docket-'+n+'"]'
def add(n,t):
 p=C/'elements'/n/'element.css';s=p.read_text().split('\n/* Source restoration responsive finish */')[0];p.write_text(s+'\n/* Source restoration responsive finish */\n'+t+'\n')
# Source label-only colored cards and two-line explanatory cards are distinct structures.
p=C/'elements/card/element.css';s=p.read_text().replace(':not(:has(.mark,.note,.kick,.fig))',':not(:has(.mark,.note,.kick,.fig,.name>br))');p.write_text(s)
s=q('card');add('card',s+'.quiet:has(.name):not(:has(.mark,.fig,.kick)) .note{font-size:var(--type-12);line-height:1.5}'+s+':is(.tone-3,.tone-4,.on):not(:has(.mark,.note,.kick,.fig,.name>br)) .parts>.name{align-self:center}'+s+'.quiet:not(:has(.name,.mark,.fig,.kick)){padding:23px 27px 16px}'+s+'.tone-3:not(:has(.mark,.kick,.fig)):has(.name>br){background:var(--a1-2-soft);color:var(--a1-7)}'+s+'.tone-3:not(:has(.mark,.kick,.fig)):has(.name>br) .name{font-size:var(--type-18);color:var(--a1-7)}')
p=C/'foundation/foundation.css';s=p.read_text().split('\n/* Source restoration responsive finish */')[0];s+='\n/* Source restoration responsive finish */\n.slide .group.on{width:761px;max-width:100%}\n';
for n in [2,3,4,5,6]:s+='.slide .group.on:has(>:nth-child('+str(n)+'):last-child)>*{flex-basis:calc((100% + var(--gap-lg)*'+str((n-1)*1.25)+')/'+str(n)+')}\n'
p.write_text(s)
s=q('hierarchy');add('hierarchy',s+':has(>.branch>.org){margin-left:19px}'+s+':has(>.branch>.org)::before{left:300px;right:299px}'+s+':has(>.branch>.org)::after{left:109px;right:111px}'+s+':has(>.branch>.org)>.branch:nth-child(1 of .branch)>.org>.root{left:calc(50% - 117px)}'+s+':has(>.branch>.org)>.branch:nth-child(2 of .branch)>.org>.root{left:calc(50% - 175px)}')
s=q('list');add('list',s+'{container-type:size}'+s+'.line .name{justify-content:flex-start;padding-left:var(--gap-sm)}'+s+'.num{padding-top:17px;padding-bottom:29px;gap:clamp(var(--gap-sm),calc((100% - 250px)*.14),21px)}'+s+'.num .item{flex:1;height:auto;min-height:0;grid-template-rows:minmax(0,1fr)}'+s+'.num .item>.name{height:100%}@container(max-height:360px){'+s+'.num .item>.name{font-size:var(--type-14);line-height:1.2;padding-left:var(--pad)}'+s+'.num .item>.note{font-size:var(--type-12);line-height:1.2}'+s+'.num .item::before{font-size:var(--type-12);left:var(--gap-sm)}}')
s=q('steps');add('steps',s+':not(.col){gap:7.73%}@container(max-height:340px){'+s+':not(.col) .mark{width:72px;height:72px;margin-bottom:var(--gap-sm)}'+s+':not(.col) .mark .icon{width:40px;height:40px}'+s+':not(.col) .name{font-size:var(--type-18);margin-bottom:var(--gap-sm)}'+s+':not(.col) .note{font-size:var(--type-14);line-height:1.45;white-space:normal}'+s+':not(.col) .step::after{top:25px;right:calc(var(--gap)*-1);height:24px;width:10px}'+s+'.col .step{grid-template-columns:25% 1fr;column-gap:var(--gap)}'+s+'.col .mark{font-size:var(--type-18)}'+s+'.col .name{font-size:var(--type-14);padding-top:0;margin-bottom:4px}'+s+'.col .note{font-size:var(--type-12);line-height:1.45;margin-bottom:0}}@container(max-height:220px){'+s+' .note{display:none}}')
# Expand the actual assigned source slot to contain the three-circle arrangement.
p=R/'slide_08.html';s=p.read_text().replace('grid-column:1 / span 5;grid-row:1 / span 6','grid-column:1 / span 6;grid-row:1 / span 6');p.write_text(s)
# Add exact composition fixtures, preserving every original golden fixture.
def body(n):s=(R/f'slide_{n:02}.html').read_text();return re.search(r'<div class="body[^\"]*">(.*)</div></div></section>',s).group(1)
def fixture(folder,name,n,minimum='12x6'):
 b=body(n)
 # A single fixture child holds all legal element roots; placements on its members remain meaningful.
 h='<!-- min: '+minimum+' -->\n<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+b+'</div>\n'
 # Source has several grid roots: make a foundation grid wrapper through group.two would change source geometry.
 # For one-root compositions retain the root as-is instead.
 if n in[9,14,16]:
  if n==14:b=re.search(r'(<div class="group on".*?</div></div></div></div></div>)',b).group(1) if False else b
  if n==9:h='<!-- min: '+minimum+' -->\n'+b+'\n'
  if n==16:h='<!-- min: '+minimum+' -->\n'+b+'\n'
 (C/'elements'/folder/'fixtures'/name).write_text(h)
fixture('hierarchy','org-nested-five-source.html',9)
fixture('list','tabs-three-source.html',16)
# Four overlapping circle cards are already a single source wrapper; extract its balanced div.
def firstdiv(s):
 starts=list(re.finditer(r'</?div\b[^>]*>',s));d=0
 for m in starts:
  d+=-1 if m.group().startswith('</')else 1
  if d==0:return s[:m.end()]
fixture14=firstdiv(body(14));(C/'elements/card/fixtures/circles-four-source.html').write_text('<!-- min: 12x6 -->\n'+fixture14+'\n')
# One foundation group can hold three overlapping donor roots through its grid modifier.
ring=''.join(re.findall(r'<div class="donut tone-[123]".*?</div>',body(6)))
(C/'elements/chart-donut/fixtures/three-share-source.html').write_text('<!-- min: 12x6 -->\n<div class="group two" style="grid-column:1 / span 12;grid-row:1 / span 6">'+ring+'</div>\n')
# Include the icon-circle variant, not just its page composition.
circle=firstdiv(body(8));(C/'elements/card/fixtures/three-icon-circles-source.html').write_text('<!-- min: 6x6 -->\n'+circle.replace('grid-column:1 / span 6','grid-column:1 / span 12')+'\n')
print('Responsive controls and five source composition fixtures added.')
