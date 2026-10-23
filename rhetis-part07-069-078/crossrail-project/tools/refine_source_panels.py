from pathlib import Path
import re,json
p=Path(__file__).parent;c=p/'crossrail'
# The source's ordinary prose is 18px, gray, and aligned to the top of its slot.
f=c/'elements/prose/element.css';f.write_text(f.read_text()+'''\n[data-el="crossrail-prose"]{justify-content:flex-start;color:var(--n-7)}[data-el="crossrail-prose"] p{font-size:var(--type-18);letter-spacing:var(--body-track)}[data-el="crossrail-prose"].lead p{font-size:var(--type-26);color:var(--ink)}[data-el="crossrail-prose"]:has(>p:first-child>b:only-child){padding-top:var(--pad);gap:calc(var(--gap-sm)*1.5)}[data-el="crossrail-prose"]>p:first-child:has(>b:only-child){font-size:var(--type-26);font-weight:var(--name-weight);color:var(--ink)}\n''')
# Explicit source line breaks are content, not a layout substitute.
f=p/'reassembled/slide_05.html';s=f.read_text();s=s.replace('고객과 함께성장하자','고객과 함께<br>성장하자').replace('최고의 품질을추구하자','최고의 품질을<br>추구하자').replace('정직함으로진심을 다하자','정직함으로<br>진심을 다하자');f.write_text(s)
# Source figure panels use the same compact 2-column figure/title header at every card size.
s='[data-el="crossrail-card"].quiet:has(.fig):not(:has(.mark,.kick))'
f=c/'elements/card/element.css';f.write_text(f.read_text()+f'''\n{s}{{border:0;background:var(--page)}}{s} .parts{{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:56px 1fr;align-content:start;align-items:center;padding:var(--pad);gap:var(--gap-sm)}}{s} .fig{{grid-column:1;grid-row:1;font-size:var(--type-44);line-height:var(--figure-line)}}{s} .name{{grid-column:2;grid-row:1;font-size:var(--type-26);text-align:right;min-height:0;padding:0;border:0}}{s} .note{{grid-column:1/-1;grid-row:2;align-self:start;min-height:0;border-top:1px solid var(--n-3);padding-top:calc(var(--gap-sm)*1.5);font-size:var(--type-18)}}@container(min-width:500px){{{s} .parts{{padding-inline:var(--gap-lg)}}}}@container(max-width:330px){{{s} .parts{{padding:var(--gap-sm);grid-template-rows:40px 1fr}}{s} .fig{{font-size:var(--type-32)}}{s} .name{{font-size:var(--type-20)}}{s} .note{{font-size:var(--type-14);padding-top:var(--gap-sm)}}}}\n''')
# A leading achievement card is visibly distinct from the 2x2 supporting panels.
s='[data-el="crossrail-card"].on:has(.mark):not(:has(.fig,.kick))'
f.write_text(f.read_text()+f'''\n{s}{{background:transparent;border:0;transform:translateY(calc(var(--gap-sm)/-4))}}{s} .parts{{padding:0;width:calc(100% - var(--gap) - var(--gap-sm)/2);justify-content:flex-start;gap:0}}{s} .mark{{display:flex;width:113px;height:113px;border:1px solid var(--page);color:var(--page);font-size:var(--type-40)}}{s} .name{{margin-top:calc(var(--gap-lg) + var(--gap) + var(--gap-sm)/4);font-size:var(--type-26);min-height:0;border:0;padding:0}}{s} .note{{margin-top:calc(var(--gap) - var(--gap-sm)*5/12);font-size:var(--type-18);min-height:0;line-height:var(--body-line)}}\n''')
f=p/'reassembled/slide_21.html';s=f.read_text();m=re.search(r'<div class="stat" data-el="crossrail-metric"[^>]*><div class="parts"><b class="fig">1위</b><p class="name">업계 순위</p><p class="note">(.*?)</p></div></div>',s)
if m:
 lead='<div class="card on" data-el="crossrail-card" style="grid-column:1 / span 3;grid-row:1 / span 6"><div class="parts"><span class="mark">1위</span><p class="name">업계 순위</p><p class="note">'+m[1]+'</p></div></div>';s=s[:m.start()]+lead+s[m.end():]
 # Four supporting cards are one regular two-column group, within the 9-column right region.
 start=s.index('<div class="card quiet"',s.index('<div class="body">')+1);end=s.index('</div></div></section>',start)
 cards=s[start:end];cards=re.sub(r' style="grid-column:[^"]*"','',cards);s=s[:start]+'<div class="group two" style="grid-column:4 / span 9;grid-row:1 / span 6">'+cards+'</div>'+s[end:]
 f.write_text(s)
# A value-bearing legend is drawn as the original two-column capsule list.
f=p/'reassembled/slide_24.html';s=f.read_text();a=s.index('<div class="body">')+len('<div class="body">');b=s.index('<div class="prose ',a)
legend='<div class="legend" data-el="crossrail-legend" style="grid-column:1 / span 6;grid-row:1 / span 4">'+''.join('<span class="key tone-'+str(t)+'">'+n+'<b>'+str(v)+'%</b></span>' for n,v,t in [('북미',20,1),('아시아',10,4),('남미',25,2),('아프리카',30,5),('유럽',15,3)])+'</div>'
s=s[:a]+legend+s[b:];f.write_text(s)
f=c/'elements/legend/element.css';s='[data-el="crossrail-legend"]:has(.key>b)';css=f'''\n{s}{{display:grid;grid-template-columns:244px 244px;grid-auto-rows:65px;align-content:start;justify-content:start;gap:calc(var(--gap-sm)*3/4) calc(var(--gap-sm)*19/12);transform:translateY(calc(var(--gap-sm)/-4));container-type:size}}{s} .key{{box-sizing:border-box;position:relative;display:flex;align-items:center;gap:var(--gap-sm);border:2px solid var(--n-3);border-radius:999px;padding-inline:calc(var(--gap-sm)*4/3);font-size:var(--type-26);font-weight:var(--name-weight)}}{s} .key::before{{width:12px;height:12px;flex:none}}{s} .key>b{{font-size:var(--type-26);font-weight:var(--name-weight);color:var(--n-5);margin-left:auto}}@container(max-width:520px){{{s}{{grid-template-columns:repeat(2,minmax(0,1fr))}}{s} .key{{font-size:var(--type-20);padding-inline:var(--gap-sm)}}{s} .key>b{{font-size:var(--type-20)}}}}'''
for i,var in enumerate(['--a1-3','--a1-4','--a1-5','--a1-6','--a1-7'],1):css+=f'{s} .tone-{i}::before{{background:var({var})}}'
f.write_text(f.read_text()+css+'\n')
# Rich sequence count controls its own joined-chevron geometry for 3–8 steps.
f=c/'elements/steps/element.css';s='[data-el="crossrail-steps"]:has(.name>.icon):not(.col)';css=f'\n{s}{{--crossrail-step-count:4;grid-template-columns:repeat(var(--crossrail-step-count),minmax(0,1fr))}}'
for n in range(3,9):css+=f'{s}:has(>.step:nth-child({n}):last-child){{--crossrail-step-count:{n}}}'
css+=f'{s} .mark{{width:calc(100% + (var(--crossrail-step-count) - 1)*var(--gap-sm)*5/6 - 2px);clip-path:polygon(0 0,calc(100% - var(--crossrail-step-count)*var(--gap-sm)*5/6) 0,100% 50%,calc(100% - var(--crossrail-step-count)*var(--gap-sm)*5/6) 100%,0 100%,calc(var(--crossrail-step-count)*var(--gap-sm)*5/6) 50%)}}'
f.write_text(f.read_text()+css+'\n');f=c/'elements/steps/element.json';d=json.loads(f.read_text());d['tokenDefaults']['--crossrail-step-count']=4;f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('source panels refined')
