from pathlib import Path
import json
B=Path('/workspace/output/roundrise')
p=B/'foundation/foundation.css';p.write_text(p.read_text()+'\n.slide.dark .page{background:linear-gradient(var(--roundrise-dark-surface,var(--page)) 5%,var(--a1-2-soft) 100%)}\n')
p=B/'foundation/foundation.json';o=json.loads(p.read_text());o['tokenDefaults']['--roundrise-dark-surface']='var(--page)';p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
p=Path('/workspace/work/roundrise/reassemble.py');s=p.read_text();s=s.replace("'--a1-on':'#ffffff','--a1-7':'#065de5'","'--a1-on':'#ffffff','--a1-7':'#065de5','--roundrise-dark-surface':'var(--a1)'");p.write_text(s)
p=B/'elements/card/fixtures/card.html';p.write_text(p.read_text().replace('<span class="icon">✹</span>','<span class="icon" data-icon="sparkles"></span>'))
p=B/'elements/hub/element.css';q='.hub[data-el="roundrise-hub"]:not(:has(>.core>span:not(.icon)))';s=f'''\n/* Generic hubs connect node centres behind the circular node surfaces. */
{q}{{isolation:isolate;}}
{q}>.core{{transform:none;}}
{q}>.spoke{{transform:none;z-index:auto;}}
{q}>.spoke::before{{--roundrise-hub-dx:calc(50cqw - (100cqw - 2*var(--gap))/6.4);--roundrise-hub-dy:calc((100cqh + var(--gap))/3);left:50%;right:auto;top:50%;height:var(--stroke);width:hypot(var(--roundrise-hub-dx),var(--roundrise-hub-dy));background:var(--n-7);clip-path:none;transform-origin:0 50%;transform:rotate(atan2(var(--roundrise-hub-dy),var(--roundrise-hub-dx)));z-index:-1;}}
{q}>.spoke:nth-child(odd)::before{{--roundrise-hub-dx:calc(-1*(50cqw - (100cqw - 2*var(--gap))/6.4));left:50%;right:auto;}}
{q}>.spoke:nth-child(n+4)::before{{--roundrise-hub-dy:calc(-1*(100cqh + var(--gap))/3);top:50%;}}
{q}>.spoke:nth-child(n+6)::before{{--roundrise-hub-dy:0px;}}
{q}>.spoke::after{{display:none;}}
''';p.write_text(p.read_text()+s)
p=B/'elements/hub/element.json';o=json.loads(p.read_text());o['tokenDefaults'].update({'--roundrise-hub-dx':'0px','--roundrise-hub-dy':'0px'});p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
