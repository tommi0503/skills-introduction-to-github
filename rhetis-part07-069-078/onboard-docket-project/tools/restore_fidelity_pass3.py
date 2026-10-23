from pathlib import Path
import re
P=Path(__file__).parent;C=P/'onboard-docket';R=P/'reassembled'
def q(n):return '[data-el="onboard-docket-'+n+'"]'
def add(n,t):
 p=C/'elements'/n/'element.css';s=p.read_text().split('\n/* Source measured pass three */')[0];p.write_text(s+'\n/* Source measured pass three */\n'+t+'\n')
def edit(n,fn):p=R/f'slide_{n:02}.html';p.write_text(fn(p.read_text()))
edit(6,lambda s:s.replace('grid-column:3 / span 8;grid-row:1 / span 5','grid-column:1 / span 12;grid-row:1 / span 5'))
edit(9,lambda s:s.replace('class="body"','class="body overrides"'))
edit(14,lambda s:s.replace('grid-column:3 / span 8;grid-row:1 / span 4','grid-column:3 / span 8;grid-row:1 / span 5'))
p=C/'foundation/foundation.css';s=p.read_text().split('\n/* Source measured pass three */')[0];s+='''
/* Source measured pass three */
.slide .body.overrides:has(>.org){padding-top:var(--gap);padding-bottom:var(--gap)}
.slide .body:has(>.frame>.seat.portrait)>.prose.quiet{padding-top:0}
.slide .group.on{container-type:size}
''';p.write_text(s)
s=q('hierarchy');add('hierarchy',s+':has(>.branch>.org){width:min(1120px,calc(100% - 32px));margin-left:16px;margin-top:16px;height:calc(100% - 16px)}')
s=q('card');add('card',s+':is(.tone-1,.tone-2):has(.kick):not(:has(.mark,.fig))::before{width:min(100%,calc(100cqh - 69px));height:min(100cqw,calc(100cqh - 69px));aspect-ratio:1;left:50%;transform:translateX(-50%)}'+s+':is(.tone-1,.tone-2):has(.kick):not(:has(.mark,.fig)) .parts{z-index:1}'+s+'.quiet:not(:has(.mark,.fig,.kick)) .note{display:block!important}')
# Keep source figure bounds independent of surrounding flex min-content tracks.
s=q('image-frame');add('image-frame',s+'.frame{width:100%;min-width:0;align-self:stretch;justify-self:stretch}'+s+' .seat:not(.portrait){flex:none}@container(min-width:301px) and (max-width:349px){'+s+' .seat:not(.portrait){width:100%;height:100%;margin:0;transform:none}}')
# Core rings and description labels are three semantic fields; their figures remain intentionally blank.
s=q('chart-donut');add('chart-donut',s+'.donut[class*="tone-"]{pointer-events:none}'+s+'.donut[class*="tone-"] .name{pointer-events:auto}')
print('Pass three geometry and slot bounds applied.')
