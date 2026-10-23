from pathlib import Path
from lxml import html,etree
from copy import deepcopy
P=Path(__file__).parent;C=P/'vectorbox'
def write(folder,name,body,min='12x6'):
 target=C/folder/'fixtures'/name;target.write_text(f'<!-- min: {min} -->\n'+body+'\n')
def document(n):return html.fromstring((P/'reassembled'/f'slide_{n:02}.html').read_text())
def markup(e):return etree.tostring(e,encoding='unicode',method='html')
def page(n):return document(n).xpath('//section')[0]
def root(n,kind,index=0):return document(n).xpath('//*[@data-el="vectorbox-'+kind+'"]')[index]
def standalone(e):
 e=deepcopy(e);e.set('style','grid-column:1 / span 12;grid-row:1 / span 6'+(';'+';'.join(x for x in e.get('style','').split(';') if x.strip().startswith('--')) if '--' in e.get('style','') else ''));return markup(e)
def group(elements):return '<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(markup(e) for e in elements)+'</div>'
# Complete pages belong to foundation. All twelve restore different composition rules.
for n in range(2,14):write('foundation',f'source-{n:02}.html',markup(page(n)))
# Remove earlier full-page prototypes from element directories; preserve all original fixtures.
for f in (C/'elements').glob('*/fixtures/source-*.html'):f.unlink()
for f in (C/'foundation/fixtures').glob('source-*.html'):
 if not f.stem[-2:].isdigit():f.unlink()
for n,label in [(3,'outline-icons-four'),(5,'ring-icons-four'),(8,'results-four')]:
 cards=document(n).xpath('//*[@data-el="vectorbox-card"]');write('elements/card','source-'+label+'.html',group(cards),'12x5')
write('elements/card','source-budget-trailing-mark.html',standalone(root(10,'card',1)),'5x5')
write('elements/card','source-profile.html',standalone(root(12,'card')),'4x5')
write('elements/card','source-caption-pair.html',group(document(4).xpath('//*[@data-el="vectorbox-card" and not(contains(concat(" ",@class," ")," on "))]')),'6x4')
write('elements/chart-bar','source-paired-eight.html',standalone(root(4,'chart-bar')),'8x4')
write('elements/chart-donut','source-one-share.html',standalone(root(10,'chart-donut')),'8x5')
write('elements/card','source-burst-pair.html',group(document(4).xpath('//*[@data-el="vectorbox-card" and contains(concat(" ",@class," ")," on ")]')),'6x3')
write('elements/card','source-icon-mark.html',standalone(document(10).xpath('//*[@data-el="vectorbox-card" and contains(concat(" ",@class," ")," quiet ")]')[0]),'3x3')
write('elements/hub','source-four-spoke-fold.html',standalone(root(6,'hub')),'12x6')
write('elements/callout','source-framed-pair.html',standalone(root(11,'callout')),'10x4')
write('elements/list','source-five-contact.html',standalone(root(12,'list')),'9x6')
write('elements/headline','source-closing.html',standalone(root(13,'headline')),'9x4')
write('elements/prose','source-footer.html',standalone(root(13,'prose')),'6x2')
print('12 foundation pages +15 canonical single-root/group element fixtures added.')
