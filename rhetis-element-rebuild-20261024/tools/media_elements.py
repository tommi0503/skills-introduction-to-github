"""Fresh media carriers and inferred legend designs, owned by root after explicit handoff."""
from pathlib import Path
from html import escape
import json, math, sys
R=Path('/workspace/work/rebuild')
NAMES=['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark']
ORIGINS={
 'tide-tab':'replica05 floating779×261 faces,21px corners and source06 soft blue shadows',
 'cutfield':'replica05 lower-right28/268 chamfers and source03 light figures',
 'filament':'replica04 five70×60 logo seats at105px pitch in a490×60 row',
 'portico':'replica02 orthogonal dividers and source08 sand headings above ruled fields',
 'toggle-grid':'replica06 circular40px marks and capsule outlines, with exposed black rules',
 'lamella':'replica03 opposite upper-right/lower-left cap corners and fine vertical rails',
 'rulemark':'replica05 straight black rules and source13 square evidence faces'}

def save(n,leaf,css,contract,description,fixtures):
 d=R/n/n/'elements'/leaf
 (d/'element.css').write_text('/* '+ORIGINS[n]+'.\n   '+('Measured source element.'if n=='filament'and leaf=='logo-group'else'This contract is absent; inferred from the measured material, not from an old kit.')+' */\n'+css+'\n')
 (d/'element.json').write_text(json.dumps({'schema':'rhetis.design-library-element-source/1','contract':contract,'registrations':{},'tokenDefaults':{}},indent=2))
 (d/'description.md').write_text(description+'\n')
 for stem,minimum,html in fixtures:(d/'fixtures'/(stem+'.html')).write_text('<!-- min: '+minimum+' -->\n'+html+'\n')

def logos(n):
 s='.logos[data-el="'+n+'-logo-group"]';v='--'+n+'-logos-';ratio='7/6'if n=='filament'else'1';scale='1.1666666667'if n=='filament'else'1'
 gap='calc(var(--gap)*1.75)'if n=='filament'else'var(--gap)'
 base=f'min(calc((100cqw - (var({v}count) - 1)*var({v}gap))/var({v}count)),calc(100cqh*{scale}))'
 half=f'min(calc((100cqw - (var({v}half) - 1)*var({v}gap))/var({v}half)),calc((100cqh - var({v}gap))*.5*{scale}))'
 narrow=f'min(calc((100cqw - var({v}gap))*.5),calc((100cqh - (var({v}half) - 1)*var({v}gap))/var({v}half)*{scale}))'
 css=f'''{s}{{{v}count:4;{v}half:2;{v}gap:{gap};container-type:size;position:relative;display:flex;flex-wrap:wrap;align-items:center;align-content:center;justify-content:center;gap:var({v}gap);width:100%;height:100%;min-width:0;min-height:0}}
{s}>.seat.logo{{position:relative;isolation:isolate;display:grid;place-items:center;flex:0 0 {base};width:{base};height:auto;aspect-ratio:{ratio};min-width:0;min-height:0;background:var(--n-2);color:var(--n-7);font-family:var(--font-body);font-size:clamp(var(--type-12),min(4cqw,12cqh),var(--type-20));font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}}
{s}>.seat.logo::after{{position:relative;z-index:1;content:attr(data-ph);display:block;text-align:center}}
'''
 for count in range(3,13):css+=f'{s}:has(>.seat.logo:nth-child({count}):last-child){{{v}count:{count};{v}half:{math.ceil(count/2)}}}\n'
 if n=='tide-tab':css+=f'{s}{{padding:var(--gap)}}{s}>.seat.logo{{border-radius:min(var(--radius),12%);box-shadow:0 calc(var(--gap-sm)*.6) var(--gap) color-mix(in srgb,var(--a2-3-soft) 22%,transparent)}}\n'
 elif n=='cutfield':css+=f'{s}>.seat.logo{{clip-path:polygon(0 0,100% 0,100% 89.5522388%,89.5522388% 100%,0 100%);font-weight:var(--figure-weight)}}\n'
 elif n=='portico':css+=f'{s}>.seat.logo{{border:var(--stroke) solid var(--n-4)}}{s}>.seat.logo::before{{content:"";position:absolute;left:0;right:0;top:0;height:10%;background:var(--n-3)}}\n'
 elif n=='toggle-grid':css+=f'{s}>.seat.logo{{border:var(--stroke) solid var(--ink);border-radius:999px;color:var(--ink)}}\n'
 elif n=='lamella':css+=f'{s}>.seat.logo{{border-left:var(--stroke) solid var(--n-5);border-radius:0 14% 0 14%}}{s}>.seat.logo::before{{content:"";position:absolute;left:0;right:0;top:0;height:13.8248848%;background:var(--a1-2-soft);border-radius:0 100% 0 100%}}\n'
 elif n=='rulemark':css+=f'{s}>.seat.logo{{border-top:var(--stroke) solid var(--ink);border-bottom:var(--stroke) solid var(--ink);font-weight:var(--body-weight)}}\n'
 css+=f'@container(max-aspect-ratio:3/1){{{s}>.seat.logo{{flex-basis:{half};width:{half}}}}}\n@container(max-width:220px){{{s}>.seat.logo{{flex-basis:{narrow};width:{narrow};font-size:var(--type-12)}}}}\n'
 # Width, height, line and gap calculations above share one source box. No page or fixture selector.
 def markup(count):return '<div class="logos" data-el="'+n+'-logo-group" style="grid-column:1 / span 12; grid-row:1 / span 6">'+''.join('<div class="seat logo" data-ph="'+str(i+1)+'"></div>'for i in range(count))+'</div>'
 fixtures=[('replica-04'if n=='filament'else'logos-four','1x2 | 3x1'if n=='filament'else('2x2'if n=='tide-tab'else'1x1'),markup(5 if n=='filament'else 4)),('logos-three'if n=='filament'else'logos-six','1x1'if n=='filament'else('2x2'if n=='tide-tab'else'1x2 | 3x1'),markup(3 if n=='filament'else 6))]
 description=('Five neutral logo openings reproduce the source70:60 face and105px pitch at490×60. 'if n=='filament'else'Logo carriers infer the '+ORIGINS[n]+'. ')+ 'Member count determines equal openings; tall allocations wrap into two rows and narrow allocations into two columns. All placeholders keep their numbers centered. The picture material stays neutral; corners, rules and enclosure treatment distinguish this collection.'
 save(n,'logo-group',css,'logos.row@1',description,fixtures)

def rulemark_legend():
 n='rulemark';s='.legend[data-el="rulemark-legend"]'
 css=f'''{s}{{container-type:size;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;width:100%;height:100%;min-width:0;min-height:0;padding-bottom:calc(var(--gap-sm)*1.45);gap:0;color:var(--ink);font-family:var(--font-body)}}
{s}>.key{{display:flex;align-items:center;gap:min(var(--gap-sm),5.3333333333cqw);max-width:100%;min-width:0;font-size:clamp(var(--type-12),9.3333333333cqw,var(--type-24));font-weight:var(--body-weight);line-height:calc(var(--body-line)*.8666666667);letter-spacing:calc(var(--body-track)*1.2857142857);overflow-wrap:anywhere;--rulemark-legend-fill:var(--n-5)}}
{s}>.key::before{{content:"";flex:none;width:min(6cqw,var(--type-16));aspect-ratio:1;background:var(--rulemark-legend-fill)}}
{s}>.key.tone-1{{color:var(--n-7);--rulemark-legend-fill:var(--n-5)}}
{s}>.key.tone-2{{--rulemark-legend-fill:var(--ink)}}
{s}>.key.tone-3{{--rulemark-legend-fill:var(--n-3)}}
{s}>.key.tone-4{{--rulemark-legend-fill:var(--n-7)}}
{s}>.key.tone-5{{--rulemark-legend-fill:var(--n-9)}}
@container(max-width:120px){{{s}>.key{{font-size:var(--type-12)}}}}
'''
 def markup(labels):return '<div class="legend" data-el="rulemark-legend" style="grid-column:1 / span 12; grid-row:1 / span 6">'+''.join('<span class="key tone-'+str(i+1)+'">'+escape(t)+'</span>'for i,t in enumerate(labels))+'</div>'
 fs=[('replica-12','1x1',markup(['운영 수요','검토 단계'])),('keys-long','2x2',markup(['정기 이용 고객','신규 유입 경로','현장 상담 요청','협력 부서 지원']))]
 save(n,'legend',css,'legend.keys@1','Replica12 has two14px/400 labels with18.2px line pitch in a150×48 box. The source square glyph is replaced by a9px CSS swatch. The quiet first label uses the readable neutral7 role; the second uses ink. A measured11.6px bottom reserve preserves the original first-row position while large allocations center the key stack. Source glyph-specific advances remain a small documented difference.',fs)
 d=R/n/n/'elements/legend/element.css';d.write_text('/* Replica12:150×48 stacked legend,14px/400 text and18.2px row pitch.\n   Nine-pixel CSS squares replace the source square glyph; quiet label depth increases for contrast. */\n'+css)

if __name__=='__main__':
 for n in sys.argv[1:]or NAMES:logos(n)

def inferred_legend(n):
 s='.legend[data-el="'+n+'-legend"]';v='--'+n+'-legend-fill'
 css=f'''{s}{{container-type:size;display:flex;flex-wrap:wrap;justify-content:center;align-items:center;align-content:center;gap:var(--gap-sm) var(--gap);width:100%;height:100%;min-width:0;min-height:0;color:var(--ink);font-family:var(--font-body)}}
{s}>.key{{{v}:var(--a1);position:relative;display:flex;align-items:center;gap:var(--gap-sm);max-width:100%;min-width:0;font-size:clamp(var(--type-12),2.2cqw,var(--type-20));font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);overflow-wrap:anywhere}}
{s}>.key::before{{content:"";display:block;flex:none;width:min(var(--type-16),6cqw);aspect-ratio:1;background:var({v})}}
{s}>.key.tone-1{{{v}:var(--a1)}}{s}>.key.tone-2{{{v}:var(--a2)}}{s}>.key.tone-3{{{v}:var(--n-5)}}{s}>.key.tone-4{{{v}:var(--n-8)}}{s}>.key.tone-5{{{v}:var(--n-3)}}
'''
 if n=='tide-tab':css+=f'{s}>.key::before{{border-radius:50%;box-shadow:0 0 0 var(--stroke) color-mix(in srgb,var(--a2) 25%,transparent)}}\n'
 elif n=='filament':css+=f'{s}>.key::before{{border:var(--stroke) solid var({v});border-radius:min(var(--radius),12%);background:color-mix(in srgb,var({v}) 20%,var(--page))}}\n'
 elif n=='portico':css+=f'{s}>.key::before{{clip-path:polygon(50% 0,58% 33%,85% 15%,67% 42%,100% 50%,67% 58%,85% 85%,58% 67%,50% 100%,42% 67%,15% 85%,33% 58%,0 50%,33% 42%,15% 15%,42% 33%);width:min(var(--type-20),7cqw)}}\n'
 elif n=='toggle-grid':css+=f'{s}>.key::before{{border-radius:999px;border:var(--stroke) solid var(--ink);background:var(--page)}}{s}>.key.tone-1::before{{background:var(--a1)}}{s}>.key.tone-2::before{{background:var(--ink)}}{s}>.key.tone-3::before{{background:var(--n-3)}}\n'
 elif n=='lamella':css+=f'{s}>.key::before{{width:min(var(--type-24),8cqw);aspect-ratio:1.8;border-radius:0 70% 0 70%;border-left:var(--stroke) solid var(--n-5)}}\n'
 css+=f'@container(max-width:240px){{{s}{{column-gap:var(--gap-sm)}}{s}>.key{{font-size:var(--type-12)}}}}\n'
 def markup(labels):return '<div class="legend" data-el="'+n+'-legend" style="grid-column:1 / span 12; grid-row:1 / span 6">'+''.join('<span class="key tone-'+str(i+1)+'">'+escape(t)+'</span>'for i,t in enumerate(labels))+'</div>'
 save(n,'legend',css,'legend.keys@1','No legend is mapped in this deck. The keys infer '+ORIGINS[n]+'. Distinct swatch geometry belongs to this collection; labels remain readable at the minimum allocation. Neutral depth separates additional series without introducing arbitrary accent colors. Narrow boxes wrap complete keys rather than shrinking their text below the type scale.',[('keys-three','1x1',markup(['유료 전환','상담 접수','운영 개선'])),('keys-five','2x2',markup(['신규 방문 경로','정기 구매 전환','지역 협력 채널','고객 문의 처리','운영 점검 결과']))])
