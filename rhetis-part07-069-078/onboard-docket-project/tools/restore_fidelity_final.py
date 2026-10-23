from pathlib import Path
import json,re
P=Path(__file__).parent;C=P/'onboard-docket'
def append(rel,css):
 p=C/rel;s=p.read_text();mark='/* Final source coordinate review */';s=s.split(mark)[0].rstrip();p.write_text(s+'\n\n'+mark+'\n'+css+'\n')
p=C/'kit/css/tokens.css';s=p.read_text().replace('--title-track: -.054em;','--title-track: 0em;');p.write_text(s)
append('elements/headline/element.css','[data-el="onboard-docket-headline"].big.center h2{top:84px;font-size:var(--type-80);line-height:.96;letter-spacing:var(--label-track)}[data-el="onboard-docket-headline"].big.center h2 b{font-size:var(--type-76)}')
append('elements/prose/element.css','[data-el="onboard-docket-prose"].quiet:not(.lead,.columns):has(>p+p){padding-left:79px;padding-right:0}[data-el="onboard-docket-prose"].quiet:not(.lead,.columns):has(>p+p) p{font-size:var(--type-18);line-height:1.6}[data-el="onboard-docket-prose"].quiet:not(.lead,.columns):has(>p+p) p+p{margin-top:var(--pad)}')
append('elements/list/element.css','[data-el="onboard-docket-list"].divided{padding:6px var(--pad) 13px}[data-el="onboard-docket-list"].divided .item::before{width:6px;height:6px}[data-el="onboard-docket-list"].line .item,[data-el="onboard-docket-list"].line.quiet .item{grid-template-columns:132px minmax(0,1fr);column-gap:27px}')
append('elements/steps/element.css','@container(min-height:341px){[data-el="onboard-docket-steps"]:not(.col) .mark .icon{width:80px;height:80px}[data-el="onboard-docket-steps"]:not(.col) .name{margin-bottom:var(--gap)}}')
append('elements/metric/element.css','[data-el="onboard-docket-metric"].stats.bands>.stat{position:relative;border-right:0}[data-el="onboard-docket-metric"].stats.bands>.stat:not(:last-child)::after{content:"";position:absolute;right:0;top:var(--pad);bottom:var(--pad);width:var(--stroke);background:var(--n-7)}')
# Bare shape styles stay in the collection; the source provider contains variable values only.
defaults={}
for f in sorted(C.glob('**/*.json')):defaults.update(json.loads(f.read_text()).get('tokenDefaults',{}))
(P/'assets/source-defaults.css').write_text('.slide{'+''.join(k+':'+str(v)+';' for k,v in sorted(defaults.items()))+'}\n')
for f in (P/'reassembled').glob('slide*.html'):
 s=f.read_text()
 if 'source-defaults.css' not in s:s=s.replace('<title>','<link rel="stylesheet" href="../assets/source-defaults.css"><title>',1)
 f.write_text(s)
print('Defaults',len(defaults),'linked in 19 pages')
