from pathlib import Path
import re
P=Path(__file__).parent;C=P/'meridian-deck'
# Narrow measured source shapes to the source structure; the existing compact fixtures keep their normal layout.
f=C/'elements/matrix/element.css';s=f.read_text();a=s.index('/* Restored source diagram geometry. */');s=s[:a]+s[a:].replace('[data-el="meridian-deck-matrix"].swot','[data-el="meridian-deck-matrix"].swot:has(>.cell>[data-el="meridian-deck-list"])');f.write_text(s)
f=C/'elements/timeline/element.css';s=f.read_text();a=s.index('/* Restored source diagram geometry. */');s=s[:a]+s[a:].replace('[data-el="meridian-deck-timeline"].alt','[data-el="meridian-deck-timeline"].alt:has(>.stop:nth-child(5):last-child)');f.write_text(s)
def css(n,t):
 f=C/'elements'/n/'element.css';f.write_text(f.read_text()+'\n/* FINAL FIDELITY DETAIL */\n'+t+'\n')
p='[data-el="meridian-deck-prose"]'
css('prose','.slide.on .body>.stack>'+p+':last-child{margin-top:5px}')
h='[data-el="meridian-deck-hub"]:has(>.core>.seat.avatar):has(>.spoke:nth-child(5):last-child)'
css('hub',h+'>.spoke:nth-child(n)>.note{width:300px}'+h+'>.spoke:nth-child(2 of .spoke)>.note,'+h+'>.spoke:nth-child(4 of .spoke)>.note{left:144px}')
l='[data-el="meridian-deck-chart-line"]'
q='.slide .body>.group.three>.stack>'+l
css('chart-line',q+'{padding-top:0;padding-bottom:15px}'+q+' .pt>b{height:calc(100% - var(--v)/var(--max,100)*100%);line-height:1}'+q+' .pt>b::after{width:12px;height:12px;border:1px solid var(--a1-4-muted)}'+q+' .pt::before,'+q+' .pt::after{opacity:.65}')
hd='[data-el="meridian-deck-headline"]'
css('headline','.slide .body>'+hd+'.center{padding:0;justify-content:start}.slide .body>'+hd+'.center h2{font-size:var(--type-32);line-height:1.4;color:var(--n-7);font-weight:650}')
# Serialize complete source compositions as foundation fixtures. No page-local CSS is introduced.
for f in (C/'foundation/fixtures').glob('source-tail-*.html'):f.unlink()
for n in range(1,31):
 s=(P/'reassembled'/f'slide_{n:02d}.html').read_text();m=re.search(r'<section class="slide\b',s);end=s.find('</section>',m.start())+10;page=s[m.start():end];(C/'foundation/fixtures'/f'source-composition-{n:02d}.html').write_text('<!-- min: 12x6 -->\n'+page+'\n')
# An element-only specimen keeps each new rich contract root testable in isolation.
def extract(s,start):
 tags=re.compile(r'<(/?)div\b[^>]*>');level=0
 for m in tags.finditer(s,start):
  level+=-1 if m[1] else 1
  if level==0:return s[start:m.end()]
for n,folder in [(10,'hub'),(12,'matrix'),(18,'hub'),(22,'cycle'),(23,'timeline')]:
 s=(P/'reassembled'/f'slide_{n:02d}.html').read_text();x=s.index(f'data-el="meridian-deck-{folder}"');start=s.rfind('<div',0,x);root=extract(s,start);root=re.sub(r' style="[^"]*"','',root,count=1);root=root.replace('>',' style="grid-column:1 / span 12;grid-row:1 / span 6">',1);(C/'elements'/folder/'fixtures'/f'source-rich-{n}.html').write_text('<!-- min: 12x6 -->\n'+root+'\n')
print('Restoration specimens registered: 30 foundation compositions + 5 rich roots')
