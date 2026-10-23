from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck'
def css(n,t):
 f=C/'elements'/n/'element.css';f.write_text(f.read_text()+'\n'+t+'\n')
def base(t):
 f=C/'foundation/foundation.css';f.write_text(f.read_text()+'\n'+t+'\n')
css('matrix','[data-el="meridian-deck-matrix"].swot .cell{justify-content:flex-start}[data-el="meridian-deck-matrix"].swot .cell:nth-child(n) .kick{background:none;border-radius:0}')
ca='[data-el="meridian-deck-card"]'
css('card',ca+'.card.on.tone-1:not(:has(.mark,.fig,.kick)){width:189px;height:383px;margin:0;align-self:start;justify-self:center;translate:0 -8px;border-radius:999px}'+ca+'.card.quiet:has(.kick) .kick,'+ca+'.card.quiet:has(.kick) .name{align-self:center}'+ca+'.card.quiet:has(.kick) .name{font-size:var(--type-18)}'+ca+'.card.quiet:has(.kick):nth-child(2){margin-top:15px}'+ca+'.card.quiet.tone-2:has(.kick){translate:0 -15.5px}'+ca+'.card.quiet.tone-2:has(.kick):first-child{margin-left:58px}'+ca+'.card.quiet.tone-2:has(.kick):nth-child(n){margin-top:0}'+ca+'.card.on.tone-1::before{content:"";position:absolute;left:100%;top:92px;width:45px;height:199px;background:linear-gradient(to bottom,var(--a1) 0 3px,transparent 3px 196px,var(--a1) 196px 199px)}')
base('.slide .body>.stack:not(:has(>.split)){gap:0}.slide .body>.stack>.group{height:199px;min-height:199px;flex:none}')
css('cycle','[data-el="meridian-deck-cycle"]:has(>.core:empty) .node:nth-child(n){inset:0;left:0;top:0;right:0;bottom:0;translate:0;transform:none;width:100%;height:100%;border:0;background:none;padding:0}')
css('headline','[data-el="meridian-deck-headline"].headline.center{padding:var(--gap-sm) 0;justify-content:start;border:0}[data-el="meridian-deck-headline"].headline.center h2{font-size:var(--type-32);line-height:1.4;font-weight:700}')
css('timeline','[data-el="meridian-deck-timeline"].alt .stop>.kick{display:block;line-height:1.55}[data-el="meridian-deck-timeline"].alt .stop>.kick span{display:inline;font-size:var(--type-30)}')
css('prose','.slide.on .stack>[data-el="meridian-deck-prose"]:last-child{margin-top:calc(var(--gap-sm)*-1 - var(--stroke)*2)}')
