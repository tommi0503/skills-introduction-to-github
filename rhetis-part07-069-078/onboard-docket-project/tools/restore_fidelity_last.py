from pathlib import Path
P=Path(__file__).parent;C=P/'onboard-docket'
def add(n,t):
 p=C/'elements'/n/'element.css';s=p.read_text().split('/* Source text and ink calibration */')[0].rstrip();p.write_text(s+'\n\n/* Source text and ink calibration */\n'+t+'\n')
add('list','[data-el="onboard-docket-list"].num{gap:21px}@container(min-height:321px){[data-el="onboard-docket-list"].num .item>.name{font-size:var(--type-20);padding-left:31px;line-height:var(--name-line)}[data-el="onboard-docket-list"].num .item>.note{font-size:var(--type-18);line-height:var(--body-line)}[data-el="onboard-docket-list"].num .item::before{font-size:var(--type-20);left:48px}}@container(max-height:320px){[data-el="onboard-docket-list"].num{gap:var(--gap-sm)}}')
add('headline','[data-el="onboard-docket-headline"]:has(>.kick){padding-right:0}')
add('prose','[data-el="onboard-docket-prose"].columns:not(.quiet) p{letter-spacing:-.05em}[data-el="onboard-docket-prose"].columns:not(.quiet):has(p>br+br){padding-top:27px}[data-el="onboard-docket-prose"].columns:not(.quiet):not(:has(p>br+br)){padding-right:0}')
add('card','[data-el="onboard-docket-card"].quiet:has(.name):not(:has(.mark,.fig,.kick)) .note{font-size:var(--type-14);line-height:1.4;letter-spacing:-.08em}')
add('quote','[data-el="onboard-docket-quote"].big blockquote::before,[data-el="onboard-docket-quote"].big blockquote::after{content:"";width:42px;height:42px;background:var(--ink)}[data-el="onboard-docket-quote"].big blockquote::before{left:-47px;top:0;clip-path:polygon(0 76%,0 40%,21% 7%,43% 7%,26% 40%,43% 40%,43% 76%,0 76%,52% 76%,52% 40%,74% 7%,95% 7%,79% 40%,95% 40%,95% 76%)}[data-el="onboard-docket-quote"].big blockquote::after{left:544px;right:auto;top:57px;bottom:auto;clip-path:polygon(0 5%,43% 5%,43% 40%,21% 74%,0 74%,17% 40%,0 40%,0 5%,52% 5%,95% 5%,95% 40%,74% 74%,52% 74%,69% 40%,52% 40%)}')
f=C/'foundation/foundation.css';s=f.read_text();s+='\n.slide .body:has(>.steps.col){padding-bottom:var(--pad)}\n';f.write_text(s)
