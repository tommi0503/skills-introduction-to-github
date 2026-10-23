from pathlib import Path
import re
P=Path(__file__).parent;C=P/'crossrail'
def replacebody(n,s):
 f=P/f'reassembled/slide_{n:02}.html';h=f.read_text();h=re.sub(r'(?s)(<div class="body">).*(</div></div></section>)',lambda m:m[1]+s+m[2],h);f.write_text(h)
def texts(n):
 a=[]
 for st,t in re.findall(r'<div style="([^"]*)">(.*?)</div>',(P/f'replica/slide_{n:02}.html').read_text()):
  a.append((st,re.sub('<[^>]+>','',t)))
 return a
def txt(n,x,y):
 for st,t in texts(n):
  if f'left:{x}px;' in st and f'top:{y}px;' in st:return t
 raise ValueError((n,x,y))
# Background photos are explicit foundation placeholders, retaining their actual crop regions.
for n,cl in [(3,'back'),(4,'back portrait')]:
 f=P/f'reassembled/slide_{n:02}.html';h=f.read_text().replace('<section class="slide">','<section class="slide"><div class="seat '+cl+'" data-ph="1"></div>',1)
 if n==4:
  h=re.sub(r'<div class="frame " data-el="crossrail-image-frame".*?</div></div>','',h);h=h.replace('grid-column:1 / span 9;grid-row:3 / span 4','grid-column:1 / span 10;grid-row:2 / span 5');h=re.sub(' class="num"','',h)
 f.write_text(h)
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''\n/* Background-photo page families keep their original panel geometry. */
.slide>.seat.back{position:absolute;left:0;right:0;bottom:0;top:auto;height:53.2%;aspect-ratio:auto;background:var(--n-2)}.slide:has(>.seat.back:not(.portrait)){background:var(--a1-7)}.slide:has(>.seat.back:not(.portrait))::before,.slide:has(>.seat.back:not(.portrait))::after{display:none}.slide:has(>.seat.back:not(.portrait)) .page{inset:var(--margin-y) var(--rail-w) calc(var(--margin-y) + 1px) calc(var(--rail-w) - 2px);padding-inline:calc(var(--gap-lg) + var(--gap) + var(--gap-sm)/6);background:var(--page);grid-template-rows:calc(var(--gap-lg)*3 + var(--gap) + var(--gap-sm)*7/12) minmax(0,1fr)}.slide>.seat.back.portrait{left:64.84375%;top:0;bottom:0;right:0;width:auto;height:auto}.slide:has(>.seat.back.portrait)::before{display:none}.slide:has(>.seat.back.portrait)::after{left:var(--rail-w);right:auto}
''')
f=C/'elements/headline/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-headline"]:has(h2>br){margin-top:0}\n')
s='[data-el="crossrail-table"]:not(:has(thead)):has(tr>td:nth-child(4))'
f=C/'elements/table/element.css';f.write_text(f.read_text()+f'''\n{s}{{position:relative;isolation:isolate;align-items:center;justify-content:flex-start}}{s} .table{{position:relative;table-layout:fixed;width:calc(100% - var(--gap-lg));background:var(--page);border:0}}{s} .table::before{{content:"";position:absolute;left:calc(var(--margin-x)*-1);right:calc(var(--gap-sm)*-3/4);top:0;bottom:0;background:var(--page);border-block:1px solid var(--n-3);z-index:-1}}{s} td{{box-sizing:border-box;height:58px;border:0;padding:0;font-size:var(--type-18);text-align:left;font-weight:var(--body-weight);color:var(--n-7)}}{s} td:nth-child(1),{s} td:nth-child(3){{width:122px;color:var(--ink);font-weight:var(--name-weight)}}{s} td:nth-child(2){{width:298px}}@container(max-width:600px){{{s} td:nth-child(1),{s} td:nth-child(3){{width:20%}}{s} td:nth-child(2){{width:30%}}{s} td{{font-size:var(--type-14)}}}}\n''')
# Agenda labels retain regular weight and their source spacing.
f=C/'elements/agenda/element.css';f.write_text(f.read_text()+'''\n[data-el="crossrail-agenda"]{justify-content:flex-start;gap:0;max-width:290px;margin-right:var(--gap-lg)}[data-el="crossrail-agenda"] .entry{height:65px;box-sizing:border-box;padding:0}[data-el="crossrail-agenda"] .name{font-size:var(--type-30);font-weight:var(--body-weight);color:var(--n-7)}[data-el="crossrail-agenda"] .mark{font-family:var(--crossrail-font-label);font-size:var(--type-32);font-weight:var(--title-weight);letter-spacing:0}@container(max-height:350px){[data-el="crossrail-agenda"] .entry{height:auto;min-height:48px}[data-el="crossrail-agenda"] .name{font-size:var(--type-24)}[data-el="crossrail-agenda"] .mark{font-size:var(--type-26)}}\n''')
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide:has(.rail.on)::before{display:none}.slide:has(.rail.on) .rail.on{top:calc(var(--margin-y)*-1);bottom:calc(var(--margin-y)*-1)}.slide:has(.rail.on) .page::after{content:"";position:fixed;left:404px;right:0;top:var(--rail-w);height:calc(var(--gap-lg)*4 + var(--gap-sm)*5/6);border-block:1px solid var(--n-3);pointer-events:none}.slide:has(.rail.on) .head>.title{font-size:var(--type-76)}.slide:has(.rail.on) .body{grid-row:1 / span 2;padding-top:calc(var(--gap-lg)*7);grid-template-rows:repeat(6,minmax(0,1fr))}
''')
f=P/'reassembled/slide_02.html';h=f.read_text().replace('grid-row:2 / span 5','grid-row:1 / span 6');f.write_text(h)
# Four business columns use a real figure (A–D), with their distinct original bullet wording.
cards=[]
for i,x in enumerate([95,376,657,938]):
 description=txt(12,x,429);b1=txt(12,x,541).replace('•　','');b2=txt(12,x,612).replace('•　','')
 cards.append('<div class="card line" data-el="crossrail-card"><div class="parts"><p class="fig">'+'ABCD'[i]+'</p><p class="name">'+txt(12,x,365)+'</p><p class="note">'+description+'<br><br><br>• '+b1+'<br><br>• '+b2+'</p></div></div>')
replacebody(12,'<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(cards)+'</div>')
s='[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick))'
f=C/'elements/card/element.css';f.write_text(f.read_text()+f'''\n{s}{{background:var(--page);border:0}}{s} .parts{{padding:0;justify-content:flex-start;gap:0}}{s} .fig{{box-sizing:border-box;flex:none;height:calc(var(--gap-lg)*2);padding-top:var(--gap);font-size:var(--type-40);line-height:var(--name-line);border-bottom:1px solid var(--n-3)}}{s} .name{{min-height:0;font-size:var(--type-26);margin-top:var(--gap);border:0;padding:0}}{s} .note{{font-size:var(--type-18);min-height:0;margin-top:var(--gap);line-height:var(--body-line)}}@container(max-height:300px){{{s} .fig{{height:56px;padding-top:var(--gap-sm);font-size:var(--type-28)}}{s} .name{{margin-top:var(--gap-sm);font-size:var(--type-22)}}{s} .note{{margin-top:var(--gap-sm);font-size:var(--type-14)}}}}\n''')
# Source cover positions and weights are independent from the interior header.
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide.cover .lockup.at-top-left{top:calc(var(--gap-lg)*2 + var(--gap) + 1px);gap:calc(var(--gap) + var(--gap-sm))}.slide.cover .lockup.at-top-left .kicker{font-size:var(--type-36);font-weight:var(--body-weight);color:var(--a1-5);line-height:var(--label-line)}.slide.cover .lockup.at-top-left .title{font-size:var(--type-76);line-height:1.25;letter-spacing:var(--body-track);font-weight:var(--body-weight)}.slide.cover .meta{font-family:var(--crossrail-font-label);bottom:calc(var(--margin-y) + var(--gap-sm));font-size:var(--type-18)}.slide.cover .lockup.at-left{top:282px;gap:var(--gap)}.slide.cover .lockup.at-left .kicker{font-family:var(--crossrail-font-label);font-size:var(--type-18);color:var(--a1-5);line-height:var(--label-line)}.slide.cover .lockup.at-left .title{font-size:var(--type-48);line-height:1.34;font-weight:var(--body-weight)}.slide.cover .lockup.at-left .lead{margin-top:calc(var(--gap-lg)*2);font-size:var(--type-18)}\n''')
print('photo families, agenda, cover, and business columns restored')
