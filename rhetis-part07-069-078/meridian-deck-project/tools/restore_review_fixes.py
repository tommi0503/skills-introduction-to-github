from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck'
def css(n,t):
 f=C/'elements'/n/'element.css';marker='/* MEASURED RESTORATION REVIEW */';f.write_text(f.read_text().split(marker)[0]+'\n'+marker+'\n'+t)
f=C/'foundation/foundation.css';s=f.read_text();marker='/* MEASURED RESTORATION REVIEW */';f.write_text(s.split(marker)[0]+'\n'+marker+'''\n.slide .body>.stack:has(>[data-el="meridian-deck-pill"]):not(:has(.group)){padding-top:0;gap:7px;align-items:center;justify-content:start}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-chart-line"]){display:flex;transform:none;width:auto;height:auto;gap:14px;padding:22px 35px 0 37px}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-chart-line"])>.stack{display:flex;flex-direction:column;flex:1;min-width:0;width:0;height:373px;min-height:373px;gap:0}
''')
cy='[data-el="meridian-deck-cycle"]'
css('cycle',cy+':has(>.core:empty):has(>.node:nth-child(5):last-child)>.node:nth-child(n){left:0;top:0;translate:0;transform:none;inset:0;width:100%;height:100%}')
ca='[data-el="meridian-deck-card"]'
css('card',ca+'.card.line:has(.kick) .kick{display:block;position:absolute;left:0;right:0;top:0;padding:9px 0 0;height:44px;min-height:44px;text-align:center;border-radius:0;background:var(--a1-2-soft)}'+ca+'.card.on:has(.mark)>.parts>.mark>.icon{width:48px;height:48px}'+ca+'.card.on:has(.mark)>.parts>.mark{display:grid;place-items:center}'+ca+'.card.quiet.tone-2:has(.kick) .note{white-space:normal;font-size:var(--type-14);width:148px;line-height:1.55}'+ca+'.card.quiet:has(.kick):not(.tone-2)::after{content:"→";position:absolute;left:100%;top:50%;width:50px;color:var(--n-7);font-size:var(--type-30);font-weight:400;translate:0 -50%}')
a='[data-el="meridian-deck-chart-area"]'
css('chart-area','.split.wide-left>.group>'+a+' .axis>span:nth-child(n){visibility:visible}.split.wide-left>.group>'+a+' .axis>span:empty{visibility:hidden}.split.wide-left>.group>'+a+' .pt::before{border:0}.split.wide-left>.group>'+a+'::before{top:20px;bottom:36px}')
h='[data-el="meridian-deck-hub"]'
css('hub',h+':has(>.core>.seat.avatar)>.spoke>.note{width:300px}'+h+':has(>.core>.seat.avatar):has(>.spoke:nth-child(5):last-child)>.spoke:nth-child(2 of .spoke)>.note,'+h+':has(>.core>.seat.avatar):has(>.spoke:nth-child(5):last-child)>.spoke:nth-child(4 of .spoke)>.note{left:144px}')
pi='[data-el="meridian-deck-pill"]'
css('pill','.slide .body>'+pi+'.on{height:38px;min-height:38px;max-height:38px;align-self:start;translate:18px 47px;padding:0}.slide .body>.stack>'+pi+'{flex:none;width:172px;height:83px;min-height:83px;border-radius:var(--radius);padding:0;background:var(--n-6);color:var(--page)}.slide .body>.stack>'+pi+':first-child{background:var(--a1)}.slide .body>.stack>'+pi+':last-child{height:135px;min-height:135px;background:var(--n-7)}.slide .body>.stack>'+pi+' .name{font-size:var(--type-18);color:var(--page);font-weight:600}')
l='[data-el="meridian-deck-legend"]'
css('legend',l+':has(>.key:nth-child(3):last-child){display:flex;flex-direction:column;align-items:start;justify-content:start;gap:4px;padding:26px 0 0 41px}'+l+':has(>.key:nth-child(3):last-child) .key{display:flex;height:13px;min-height:13px;gap:5px}'+l+':has(>.key:nth-child(3):last-child) .key::before{height:8px;width:42px;background:var(--n-7)}'+l+':has(>.key:nth-child(3):last-child) .key:nth-child(2)::before{background:var(--a1)}'+l+':has(>.key:nth-child(3):last-child) .key:last-child::before{display:none}'+l+':has(>.key:nth-child(3):last-child) .name{font-size:var(--type-8);font-weight:400}')
b='[data-el="meridian-deck-chart-bar"]'
css('chart-bar',b+':has(>.bar>span:empty){padding-top:31px}'+b+':has(>.bar>span:empty)>.bar:nth-child(odd){background:var(--n-7)}')
li='[data-el="meridian-deck-list"]'
css('list',li+'.num.divided .name{font-weight:400}')
he='[data-el="meridian-deck-headline"]'
css('headline','.slide .body>'+he+':not(.big):not(.center){border-left:0;padding-top:18px;padding-left:24px;height:58px;justify-content:start}.slide .body>'+he+':not(.big):not(.center) h2{font-size:var(--type-18);font-weight:400}.slide .body>'+he+':not(.big):not(.center) h2>b{font-size:var(--type-22);font-weight:650}')
css('headline','.slide .body>[data-el="meridian-deck-headline"].headline:has(>h2>b:only-child){border-left:0;border-bottom:1px solid var(--n-6);height:50px;align-self:start;padding:9px 0 0 32px;justify-content:start}\n.slide .body>[data-el="meridian-deck-headline"].headline:has(>h2>b:only-child)::after{content:"";position:absolute;left:0;bottom:-4px;width:7px;height:7px;background:var(--page);border:1px solid var(--n-6);border-radius:50%}\n')
d='[data-el="meridian-deck-delta"]'
css('delta','.slide .body>.stack>.group>'+d+':has(>.from:empty)>.to::before{content:none}.slide .body>.stack>.group>'+d+':has(>.from:empty){background:linear-gradient(to right,var(--page),var(--a1-4-muted));clip-path:polygon(0 17%,65% 17%,65% 0,100% 50%,65% 100%,65% 83%,0 83%)}')
# Normalized base furniture and full-colour prose avoid inherited HTML margins.
f=C/'foundation/foundation.css';f.write_text(f.read_text()+"\n.slide .meta{margin:0;box-sizing:border-box}.slide .deco>.icon{box-sizing:border-box}.slide .head{border-left-color:var(--n-3)}.slide .head .lead{padding-top:20px;margin-left:-8px}.slide.on .head{border-left-color:var(--page)}\n")
p='[data-el="meridian-deck-prose"]'
css('prose','.slide.on .body>.stack>'+p+'{height:104px;min-height:104px;padding:0;margin:0;flex:none;gap:0;justify-content:start}.slide.on .body>.stack>'+p+' p{color:var(--a1-on);font-size:var(--type-16);line-height:1.8}.slide.on .body>.stack>'+p+':nth-child(2){margin-top:35px}.slide.on .body>.stack>'+p+':last-child{margin-top:-27px}.slide .body>'+p+'.quiet:not(:has(span)){padding:0;justify-content:start;align-items:center;translate:0 -12px}.slide .body>'+p+'.quiet p{width:100%;text-align:center}')
print('Measured restoration review fixes')
