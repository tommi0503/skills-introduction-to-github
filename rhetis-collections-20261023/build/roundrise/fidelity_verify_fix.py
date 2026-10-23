from pathlib import Path
import re
B=Path('/workspace/output/roundrise');R=Path('/workspace/output/roundrise-review')
p=B/'foundation/foundation.css';s=p.read_text();s+='''.slide .body:has(>.agenda){padding-inline:0}.slide .body:has(>.agenda)>.agenda{padding-left:calc(var(--pad)*1.8125);padding-right:calc(var(--pad)*1.8125)}''';p.write_text(s)
p=B/'elements/hub/element.css';s=p.read_text();r='.hub[data-el="roundrise-hub"]';s+=r+'''>.core{width:100%;height:auto;aspect-ratio:1;max-width:315px;max-height:100%}'''+r+'''>.spoke{height:100%;width:auto;aspect-ratio:1;max-width:100%;max-height:100%;padding:var(--gap-sm);gap:calc(var(--gap-sm)/2)}'''+r+'''>.spoke>.name{font-size:var(--type-20)}'''+r+'''>.spoke>.note{font-size:var(--type-16)}'''+r+'''>.spoke>.mark{font-size:var(--type-14)}@container (min-width:800px) and (min-height:360px){'''+r+'''>.spoke{width:172px;height:172px;max-height:none;padding:var(--gap-sm);gap:var(--gap-sm)}'''+r+'''>.spoke>.name{font-size:var(--type-26)}'''+r+'''>.spoke>.note{font-size:var(--type-28)}}''';p.write_text(s)
for p in (B/'elements/hub/fixtures').glob('*.html'):
 s=p.read_text();s=re.sub(r'<!-- min:.*?-->','<!-- min: 8x5 -->',s);p.write_text(s)
p=B/'elements/steps/element.css';s=p.read_text();r='.steps[data-el="roundrise-steps"].col:has(>.step:nth-child(4))';s+=r+'''{padding:var(--gap-sm) 0;gap:var(--gap)}''';p.write_text(s)
p=B/'elements/headline/element.css';s=p.read_text();r='.headline[data-el="roundrise-headline"]'
for sel in [r+':has(+.card>.parts>:is(.bars,.areas))',r+'.on:has(+.posmap)',r+'.on:has(+.steps)']:
 s+=sel+'''{gap:calc(var(--gap-sm)*4/3)}'''+sel+'''>.note{margin-top:var(--gap-sm)}'''
s+=r+'''.big:has(+.card>.parts>.areas)>.note{margin-top:calc(var(--gap-sm)/2)}''';k=r+'.big.center:not(.on):has(>.kick>b):has(>h2>b)';s+=k+'''{gap:calc(var(--gap-sm)*3)}'''+k+''' h2{font-size:var(--type-56);line-height:var(--lead-line)}'''+k+'''>.kick>b{display:flex;align-items:center;gap:var(--gap-sm);color:var(--ink);font-weight:var(--name-weight)}'''+k+'''>.kick>b>.icon{width:50px;height:30px;color:var(--a1-7)}'''+k+'''>.note{margin-top:calc(var(--gap-sm)*.75)}''';p.write_text(s)
p=R/'replica/replica.css';s=p.read_text()+'.side-title .kick{margin-bottom:17px}.kind-area .side-title .note{margin-top:21px}.donut-title .note{margin-top:23px}.kind-statement .centerbrand{margin-bottom:39px}.kind-statement .note{margin-top:36px}';p.write_text(s)
p=Path('/workspace/work/roundrise/reassemble.py');s=p.read_text();logo='<svg class="icon" viewBox="0 0 43 24" fill="currentColor"><circle cx="4" cy="18" r="4"/><path d="M8 22 20 2h8L17 22zM22 22 34 2h8L30 22z"/></svg>';s=s.replace("'<b>Miricompany</b>' if k=='statement'", "'<b>"+logo+"Miricompany</b>' if k=='statement'");p.write_text(s)
