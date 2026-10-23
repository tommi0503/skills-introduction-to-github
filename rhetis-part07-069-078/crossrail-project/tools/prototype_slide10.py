from pathlib import Path
import re,json
p=Path(__file__).parent;c=p/'crossrail'
# Functional blockers retained from the independent last review.
f=c/'elements/heatmap/element.css';s=f.read_text();s+='\n[data-el="crossrail-heatmap"].calendar .heads{flex:none;line-height:var(--body-line)}[data-el="crossrail-heatmap"].calendar .row{flex:none;width:min(100%,calc((100cqh - var(--type-16)*var(--body-line) - var(--gap-sm)*(var(--crossrail-heat-rows) + 1))*var(--cols)/var(--crossrail-heat-rows) + var(--gap-sm)*(var(--cols) - 1)))}\n';f.write_text(s)
f=c/'elements/chart-stack/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-chart-stack"] .seg:nth-child(3 of .seg):not([class*="tone-"]){background:var(--a3-7);color:var(--page)}\n')
f=p/'replica/replica.css';s=f.read_text().replace('../../assets/','../assets/').replace("woff2')}","woff2');font-weight:100 900;font-style:normal}");f.write_text(s)
# Restore the deck's actual typographic and page coordinates as shared tokens.
f=c/'kit/css/tokens.css';s=f.read_text();s+='\n.slide{--title-line:1.34;--title-track:-0.0109375em;--body-line:1.34;--name-line:1.34;--crossrail-head-padding:calc(var(--gap) + var(--gap-sm)*5/6);--crossrail-head-height:calc(var(--gap-lg)*4 + var(--gap-sm)*1.25)}\n';f.write_text(s)
f=c/'kit/kit.json';d=json.loads(f.read_text());d['extensions'].update({'--crossrail-head-padding':'length','--crossrail-head-height':'length'});f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f=c/'foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide:not(.cover) .page{grid-template-rows:var(--crossrail-head-height) minmax(0,1fr)}.slide:not(.cover) .head{padding-top:var(--crossrail-head-padding);gap:0}.slide:not(.cover) .kicker{font-weight:var(--body-weight);line-height:var(--body-line);color:var(--n-5);letter-spacing:var(--body-track)}.slide:not(.cover) .no{top:var(--crossrail-head-padding);font-size:var(--type-20);width:50px;right:calc(var(--gap-sm)*-1);text-align:center}.slide::before{background:linear-gradient(90deg,var(--a1-7) calc(100% - var(--rail-w)),transparent 0),repeating-linear-gradient(135deg,var(--a1-7) 0 2px,var(--n-3) 2px 3px)}.slide .page:has(>.body):not(:has(>.head)){grid-template-rows:minmax(0,1fr)}\n''')
f=c/'elements/headline/element.css';f.write_text(f.read_text()+'''\n[data-el="crossrail-headline"]:not(.big){justify-content:flex-start}[data-el="crossrail-headline"]:not(.big) h2{font-size:var(--type-28);line-height:var(--body-line);letter-spacing:var(--body-track)}\n''')
s='[data-el="crossrail-steps"]:has(.name>.icon):not(.col)'
css=f'''\n/* Rich sequence: connected chevrons and a retained icon/title/text panel. */
{s}{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:calc(var(--gap-sm)/2)}}
{s} .step{{padding-top:calc(var(--gap-lg) + var(--gap-sm)*17/12);display:flex;flex-direction:column;justify-content:flex-start;gap:0;border:0}}
{s} .mark{{position:relative;left:calc(var(--crossrail-step-index)*var(--gap-sm)*-5/6);width:calc(100% + var(--gap) + var(--gap-sm)/3);height:calc(var(--gap-lg)*2);min-height:calc(var(--gap-lg)*2);flex:none;font-size:var(--type-18);font-weight:var(--title-weight);clip-path:polygon(0 0,calc(100% - var(--gap-lg)) 0,100% 50%,calc(100% - var(--gap-lg)) 100%,0 100%,var(--gap-lg) 50%)}}
{s} .name{{position:relative;display:grid;grid-template-rows:calc(var(--gap-lg) + var(--gap-sm)*5/3) calc(var(--gap-lg) + var(--gap-sm)*7/6);row-gap:calc(var(--gap-sm)*13/12);align-items:center;flex:none;box-sizing:border-box;height:calc(var(--gap-lg)*3 + var(--gap-sm)*7/12);margin-top:calc(var(--gap-sm)*1.25);padding:0 calc(var(--gap-sm)*2/3);font-size:var(--type-28);line-height:calc(var(--gap-lg) + var(--gap-sm)*7/6);border-bottom:1px solid var(--n-3)}}
{s} .name::before{{content:"";position:absolute;left:0;right:0;top:calc(var(--gap-lg) + var(--gap-sm)*11/4);border-top:1px solid var(--n-3)}}
{s} .name>.icon{{box-sizing:border-box;width:60px;height:60px;margin-left:calc(var(--gap-sm)*-2/3);padding:calc(var(--gap-sm)*9/8);border-radius:50%;background:var(--n-1);stroke-width:2}}
{s} .note{{box-sizing:border-box;flex:none;height:calc(var(--gap-lg)*2 + var(--gap-sm)*3/4);min-height:0;margin-top:var(--gap);padding:0 calc(var(--gap-sm)*2/3);font-size:var(--type-18);line-height:var(--body-line);color:var(--n-7);border-bottom:1px solid var(--n-3)}}
'''
for i in range(1,9):css+=f'{s} .step:nth-child({i}){{--crossrail-step-index:{i-1}}}'
css+=f'@container(max-height:300px){{{s} .step{{padding-top:0}}{s} .mark{{height:var(--gap-lg);min-height:var(--gap-lg)}}{s} .name{{margin-top:var(--gap-sm);height:auto;grid-template-rows:40px 36px;row-gap:var(--gap-sm);font-size:var(--type-22);line-height:var(--name-line)}}{s} .name>.icon{{width:40px;height:40px;padding:var(--gap-sm)}}{s} .name::before{{top:calc(var(--gap-lg) + var(--gap-sm))}}{s} .note{{height:auto;flex:1;margin-top:var(--gap-sm);font-size:var(--type-14)}}}}'
f=c/'elements/steps/element.css';f.write_text(f.read_text()+css+'\n')
f=c/'elements/steps/element.json';d=json.loads(f.read_text());d['tokenDefaults']['--crossrail-step-index']=0;f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f=p/'reassembled/slide_10.html';h=f.read_text().replace('grid-row:2 / span 5','grid-row:1 / span 6')
for i,(name,icon) in enumerate(zip(['노출','실행','점검','개선'],['goal','lightbulb','search','chart-no-axes-combined']),1):
 h=h.replace(f'<span class="mark">0{i}</span>',f'<span class="mark">{i} STEP</span>');h=h.replace(f'<p class="name">{name}</p>',f'<p class="name"><span class="icon" data-icon="{icon}"></span>{name}</p>')
f.write_text(h)
# These are palette roles supplied by the source style, outside the design CSS.
f=p/'assets/source-palette.css';h=f.read_text().replace('--n-5:#969fb7','--n-5:#99a3b9').replace('--n-7:#656565','--n-7:#8c8c8c');f.write_text(h)
print('slide 10 prototype source complete')
