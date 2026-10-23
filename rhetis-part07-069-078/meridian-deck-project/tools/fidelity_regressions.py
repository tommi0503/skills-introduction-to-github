from pathlib import Path
import re
P=Path(__file__).parent;C=P/'meridian-deck'
f=C/'elements/card/element.css';s=f.read_text();s=s.replace('.quiet:has(.kick)', '.quiet:has(.kick):is(.tone-2,:has(.note:empty))').replace('.card:has(.kick):not(.quiet)', '.card:has(.kick):not(.quiet):not(:has(.fig))');f.write_text(s)
f=C/'elements/prose/element.css';s=f.read_text();s=s.replace('.lead:has(>p:nth-child(2):last-child)', '.lead:has(>p:nth-child(2):last-child):has(>p:first-child>b:only-child)').replace(':not(.lead):not(.quiet)', ':not(.lead):not(.quiet):not(.cols)');f.write_text(s)
f=C/'elements/matrix/element.css';s=f.read_text().replace('.cell .name','.cell>.name');f.write_text(s)
f=C/'foundation/foundation.css';s=f.read_text().replace('.body>.stack:has(>[data-el="meridian-deck-pill"]):not(:has(.group))','.body>.stack:has(>[data-el="meridian-deck-pill"]:nth-child(3):last-child):not(:has(.group))');s+='\n.slide.cover .meta small,.slide.cover .lockup.at-center .lead{color:var(--n-7)}\n';f.write_text(s)
f=C/'elements/pill/element.css';s=f.read_text().replace('.body>.stack>[data-el="meridian-deck-pill"]', '.body>.stack>[data-el="meridian-deck-pill"]:not(:has(.mark,.note))');f.write_text(s)
def css(n,t):
 f=C/'elements'/n/'element.css';f.write_text(f.read_text()+'\n/* RESTORATION REGRESSION AUDIT */\n'+t+'\n')
h='[data-el="meridian-deck-hub"]'
css('hub',h+':has(>.core>.seat.avatar) .spoke .name small{color:var(--n-7)}'+h+':has(>.core>.seat.avatar):has(>.spoke:nth-child(4 of .spoke):last-child)>.core>.note{color:var(--n-7);text-shadow:none}'+h+':has(>.core>.seat.avatar):has(>.spoke:nth-child(4 of .spoke):last-child)>.core>.name{color:var(--ink);text-shadow:none}')
m='[data-el="meridian-deck-matrix"].swot:has(>.cell>[data-el="meridian-deck-list"])'
css('matrix',m+'>.cell:nth-child(2)>.kick,'+m+'>.cell:nth-child(3)>.kick{color:var(--a1-on)}')
l='[data-el="meridian-deck-list"]'
css('list','[data-el="meridian-deck-matrix"].swot '+l+' .name{color:var(--n-7)}')
ca='[data-el="meridian-deck-card"]'
css('card',ca+'.quiet:has(.note:empty) .kick{color:var(--page)}'+ca+'.card.on:has(.fig) .fig small{color:inherit}')
pi='[data-el="meridian-deck-pill"]'
css('pill','.slide .body>.stack>'+pi+':not(:has(.mark,.note)):not(:last-child) .name{color:var(--a1-on)}.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(-n+2)>'+pi+' .name{color:var(--a1-on)}')
pr='[data-el="meridian-deck-prose"]'
css('prose',pr+'.quiet p{color:var(--n-7)}'+pr+'.cols p{white-space:normal}'+pr+'.lead:not(:has(>p:first-child>b:only-child)){display:flex;flex-direction:column;text-align:left;padding:var(--gap);align-items:stretch;gap:var(--gap)}'+pr+'.lead:not(:has(>p:first-child>b:only-child))>p:first-child{width:auto;flex:none;padding:0}'+pr+'.lead:not(:has(>p:first-child>b:only-child)) p{white-space:normal}')
pe='[data-el="meridian-deck-person"]'
css('person',pe+'.person>.note{color:var(--n-7)}')
he='[data-el="meridian-deck-headline"]'
css('headline','.slide .body>'+he+'.center.on h2{color:inherit}')
t='[data-el="meridian-deck-timeline"]'
css('timeline',t+'.alt:has(>.stop:nth-child(5):last-child) .stop:nth-child(odd)>.kick,'+t+'.alt:has(>.stop:nth-child(5):last-child) .stop:nth-child(odd)>.kick small{color:var(--a1-on)}'+t+'.alt:has(>.stop:nth-child(5):last-child) .stop>.note{color:var(--n-7)}'+t+'.col{display:grid;grid-template-rows:repeat(4,minmax(0,1fr));gap:var(--gap-sm);padding:var(--gap)}'+t+'.col .stop{position:relative;display:grid;grid-template-columns:100px minmax(0,1fr);grid-template-rows:auto auto;align-content:center;align-items:center;gap:var(--gap-sm);height:auto;min-height:0;width:auto;flex:1;padding:0;left:auto;top:auto}'+t+'.col .stop>.kick{grid-row:1 / span 2;position:relative;inset:auto;margin:0;padding:var(--gap-sm);width:auto;height:auto}'+t+'.col .stop>.name,'+t+'.col .stop>.note{grid-column:2;position:relative;inset:auto;padding:0;margin:0;width:auto;height:auto;white-space:normal}'+t+'.col .stop>.name{font-size:var(--type-18)}'+t+'.col .stop>.note{font-size:var(--type-14);line-height:1.3}')
print('Scoped rich source geometry away from compact fixtures; fixed audit text roles')
