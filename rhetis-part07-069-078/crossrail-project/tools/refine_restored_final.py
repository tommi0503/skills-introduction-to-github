from pathlib import Path
from bs4 import BeautifulSoup as B
import re,json
P=Path(__file__).parent; E=P/'crossrail/elements'
def app(el,s):p=E/el/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
def edit(n,fn):p=P/f'reassembled/slide_{n:02}.html';s=B(p.read_text(),'html.parser');fn(s);p.write_text(str(s))
# Keep semantic source captions and whole paragraphs, including meaningful hard breaks.
text9='숫자의 크기는 곧 자신감입니다. 핵심 지표 서너 개만 골라 과감하게 키워 보여주는 게 좋습니다.'
def nine(s):s.select('[data-el="crossrail-card"] .note')[1].string=text9
edit(9,nine)
f=P/'replica/slide_09.html';h=f.read_text();a=list(re.finditer('타이포그래피 자체가 디자인이 되도록 폰트 굵기를 조절하여 세련된 느낌을 연출해 보세요.',h));m=a[1];f.write_text(h[:m.start()]+text9+h[m.end():])
# Correct a source label that was legible, not speculative copy.
for folder in ['replica','reassembled']:
 f=P/f'{folder}/slide_29.html';h=f.read_text();h=h.replace('유사한 특징을 가진 항목들을 군집화합니다.','유사한 특징을 가진 점들을 클러스터로 군집화합니다.').replace('유사한 특징을 가진 점들을 클러스터로 관리화합니다.','유사한 특징을 가진 점들을 클러스터로 군집화합니다.');f.write_text(h)
# Placeholders are flat gray in slide reconstructions; fixture preview identifiers remain intact.
for f in (P/'reassembled').glob('slide_*.html'):f.write_text(re.sub(r'data-ph="[^"]*"','data-ph=""',f.read_text()))
# A bare pill expands to its assigned slot; compact standalone and circular badge variants stay bounded.
app('pill','''[data-el="crossrail-pill"]:not(.line):not(:has(.mark,.note)){width:100%;max-width:100%;height:calc(var(--gap-lg)*1.65);max-height:calc(var(--gap-lg)*1.65)}[data-el="crossrail-pill"]:not(.line):not(:has(.mark,.note)) .name{white-space:nowrap}:where(.group.col)>[data-el="crossrail-pill"]:not(.line):not(:has(.mark,.note)){width:calc(var(--gap-lg)*2.45)}''')
# Source08 stack the name and paragraph in one column even in a wide short slot.
app('list','''[data-el="crossrail-list"].divided>.item{display:block;min-height:0;padding:0 0 var(--gap)}[data-el="crossrail-list"].divided>.item>.name{grid-column:auto;grid-row:auto;white-space:normal;margin:0;font-size:var(--type-26)}[data-el="crossrail-list"].divided>.item>.note{grid-column:auto;grid-row:auto;margin:calc(var(--gap-sm)*1.25) 0 0;font-size:var(--type-18)}''')
# Agenda's five rows use 52 px rules and 13 px between entries; this also fills the source's 312 px slot.
app('agenda','''[data-el="crossrail-agenda"]:has(>.entry:nth-child(5):last-child){gap:calc(var(--gap-sm)*13/12);transform:translateY(calc(var(--gap-sm)*-1/12))}[data-el="crossrail-agenda"]:has(>.entry:nth-child(5):last-child)>.entry{flex:none;height:calc(var(--gap-lg)*1.3);min-height:0;align-items:start;padding:0}[data-el="crossrail-agenda"]:has(>.entry:nth-child(5):last-child) .name{font-size:var(--type-30);font-weight:var(--body-weight);color:var(--n-7);padding-left:calc(var(--gap-sm)/3)}[data-el="crossrail-agenda"]:has(>.entry:nth-child(5):last-child) .mark{font-size:var(--type-32);padding-right:calc(var(--gap-sm)*1.5)}''')
# Source pyramid has unequal tier heights and horizontal construction rules.
app('pyramid','''[data-el="crossrail-pyramid"]:not(:has(.note)){position:relative}[data-el="crossrail-pyramid"]:not(:has(.note)) .level:first-child{flex:0 0 calc(var(--gap-lg)*2.5);padding-top:var(--gap-lg)}[data-el="crossrail-pyramid"]:not(:has(.note)) .level:nth-child(2){flex:0 0 calc(var(--gap-lg)*2)}[data-el="crossrail-pyramid"]:not(:has(.note)) .level:nth-child(3){flex:0 0 calc(var(--gap-lg)*2.2)}[data-el="crossrail-pyramid"]:not(:has(.note)) .level:nth-child(4){flex:1}[data-el="crossrail-pyramid"]:not(:has(.note))::before{content:"";position:absolute;left:calc(var(--gap-lg)*-2.6);right:calc(var(--gap-lg)*-14.15);top:calc(var(--gap-lg)*2.1);bottom:0;background:repeating-linear-gradient(to bottom,var(--n-3) 0 1px,transparent 1px calc(var(--gap-lg)*2.55));pointer-events:none}''')
# Correct reverse-reading order: dir=rtl already reverses flex main-axis order.
app('steps','''[data-el="crossrail-steps"]:not(.col):not(:has(.name>.icon))[dir="rtl"]{flex-direction:row}''')
# Source12 A-D are column headers, with construction rules that continue to the page foot.
app('card','''[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick)):not(:has(.fig>b)){position:relative;border-top:calc(var(--gap-sm)*.9) solid var(--a1-7);transform:translateY(calc(var(--gap-sm)*-.25))}[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick)):not(:has(.fig>b)) .fig{height:calc(var(--gap-lg)*2);padding-top:calc(var(--gap-sm)*.75)}[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick)):not(:has(.fig>b)) .name{margin-top:0;height:calc(var(--gap-lg)*1.35);display:flex;align-items:center;border-bottom:1px solid var(--n-3)}[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick)):not(:has(.fig>b)) .note{margin-top:calc(var(--gap-sm)*1.5)}[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick)):not(:has(.fig>b)):not(:last-child)::after{content:"";position:absolute;top:0;bottom:calc(var(--margin-y)*-1);right:calc(var(--gap-sm)*-.5);border-right:1px solid var(--n-3)}''')
# Fix conflicting small-height generic figure-card tracks for the outlined score panel.
s='[data-el="crossrail-card"].line:has(.parts>.fig>b):not(:has(.mark,.kick))'
app('card',s+'{height:100%;border-top:0}'+s+'>.parts{display:grid;grid-template-columns:minmax(0,1fr) calc(var(--gap-lg)*5.3);grid-template-rows:calc(var(--gap-lg)*1.8) 1fr;align-content:start;justify-content:start;padding:var(--pad) calc(var(--gap-sm)*1.75);gap:var(--gap) 0}'+s+' .fig{grid-column:2;grid-row:1;height:calc(var(--gap-lg)*1.8);padding:0;margin:0;font-size:var(--type-40);border:2px solid var(--n-3)}'+s+' .name{grid-column:1;grid-row:1;font-size:var(--type-26);height:auto;min-height:0;text-align:left;align-self:start;padding:0;margin:0;border:0}'+s+' .note{grid-column:1 / span 2;grid-row:2;font-size:var(--type-18);margin:0;padding:0;border:0;min-height:0}')
# Fully annotated comparison: the numeric chart b occupies the capsule, followed by unit text once.
s='[data-el="crossrail-card"].quiet.on:has(.parts>.fig):not(:has(.mark,.kick))'
app('card',s+'{color:var(--ink);flex:0 0 calc(var(--gap-lg)*6.1);width:calc(var(--gap-lg)*6.1)}'+s+'>.parts{display:flex;flex-direction:column;justify-content:flex-start;align-content:start;align-items:stretch;gap:0;padding:0}'+s+' .fig{height:calc(var(--gap-lg)*1.65);flex:none;margin:0;padding-top:0;align-self:stretch;padding-right:calc(var(--gap-lg)*1.55);font-size:var(--type-26)}'+s+' .name{color:var(--ink);font-size:var(--type-26);min-height:0;height:auto;margin-top:calc(var(--gap-lg)*.5);padding:0;border:0}'+s+' .note{margin-top:calc(var(--gap-sm)*1.5);font-size:var(--type-18);padding:0;border:0;min-height:0}'+s+':first-child{margin-left:calc(var(--gap-lg)*1.675);margin-right:calc(var(--gap-sm)*13/12)}'+s+':last-child{margin-right:0}')
app('chart-bar','''[data-el="crossrail-chart-bar"].quiet:not(.h):has(>.bar:nth-child(2):last-child)>.bar b{left:calc(var(--gap-lg)*15.15);top:calc(var(--gap-lg)*3.675)}[data-el="crossrail-chart-bar"].quiet:not(.h):has(>.bar:nth-child(2):last-child)>.bar:nth-child(2) b{left:calc(var(--gap-lg)*22.025)}''')
def axis23(s):
 for k in s.select('.legend .key'):k['class']=['key','tone-1']
edit(23,axis23)
app('legend','''[data-el="crossrail-legend"]:has(>.key>small)>.key.tone-1{color:var(--page)}[data-el="crossrail-legend"]:has(>.key>strong){z-index:5;position:relative}[data-el="crossrail-legend"]>.key:has(>strong){width:calc(var(--gap-lg)*4.05);height:calc(var(--gap-lg)*.775);box-sizing:border-box;display:flex;align-items:center;justify-content:center;padding:0}''')
# Move source17's optional icon vertices without colliding with the ordinary radial-hub angle.
app('hub','''[data-el="crossrail-hub"]:has(.core>.name>br) .spoke{left:calc(50% + cos(var(--crossrail-cross-angle))*126px);top:calc(50% + sin(var(--crossrail-cross-angle))*105px)}[data-el="crossrail-hub"]:has(.core>.name>br) .spoke:nth-child(1 of .spoke){--crossrail-cross-angle:-135deg}[data-el="crossrail-hub"]:has(.core>.name>br) .spoke:nth-child(2 of .spoke){--crossrail-cross-angle:-45deg}[data-el="crossrail-hub"]:has(.core>.name>br) .spoke:nth-child(3 of .spoke){--crossrail-cross-angle:135deg}[data-el="crossrail-hub"]:has(.core>.name>br) .spoke:nth-child(4 of .spoke){--crossrail-cross-angle:45deg}''')
# Typography roles: longer paragraphs have a wider baseline than compact step notes.
f=P/'crossrail/kit/css/tokens.css';f.write_text(f.read_text()+'\n.slide{--lead-line:1.4}\n')
app('prose','''[data-el="crossrail-prose"] p{line-height:var(--lead-line)}''')
app('headline','''[data-el="crossrail-headline"] .note{font-size:var(--type-18);font-weight:var(--body-weight);color:var(--n-7);line-height:var(--lead-line);margin-top:calc(var(--gap-sm)*1.25)}[data-el="crossrail-headline"]:has(h2>br){position:relative}[data-el="crossrail-headline"]:has(h2>br)::after{content:"";position:absolute;top:calc(var(--gap-lg)*2.45);left:0;right:0;border-top:1px solid var(--n-3)}''')
# Source24 hard line breaks are visible in the source, and preserve the source's four lines.
text24=['원 그래프와 유사하지만 중앙 공간 활용도가 높아 정보 전달과 디자인을 동','시에 잡을 수 있는 레이아웃입니다. 그래프 옆이나 하단에는 데이터가 시사','하는 핵심 내용을 요약해 적어주세요. 그래프에서 도출된 결론을 텍스트로','보완하면 읽는 이에게 더욱 강력한 설득력을 줍니다.']
def twentyfour(s):
 pr=s.select_one('[data-el="crossrail-prose"]');pr.select('p')[1].clear();pr.select('p')[1].extend(B('<br/>'.join(text24),'html.parser').contents)
edit(24,twentyfour)
# Do not let generic circle-map narrow-screen rules replace the source map's geometry.
app('positioning','''[data-el="crossrail-positioning"]{width:calc(100% - var(--gap))}[data-el="crossrail-positioning"] .mark:nth-child(1 of .mark)::before{content:"";position:absolute;width:calc(var(--gap-lg)*7.25);height:calc(var(--gap-sm)*1.5);background:var(--n-3);clip-path:polygon(0 25%,87% 25%,87% 0,100% 50%,87% 100%,87% 75%,0 75%);transform:rotate(-39deg);transform-origin:left center;left:50%;bottom:50%;z-index:-1}''')
def twentynine(s):
 xy=[(23.1,22),(31,51.7),(57.6,26.6),(49.3,73.4),(88.8,44.6),(88.8,85)]
 for m,(x,y) in zip(s.select('.posmap>.mark'),xy):m['style']=f'--x:{x};--y:{y}'
edit(29,twentynine)
app('table','''[data-el="crossrail-table"]:not(:has(thead)):has(tr:nth-child(6)) td:first-child{width:calc(var(--gap-lg)*6.325)}''')
# Headered equipment specification tables have a 65 px header, then a 26 px spacer row.
s='[data-el="crossrail-table"]:has(thead th:nth-child(2)):not(:has(thead th:nth-child(3)))'
app('table',s+'{background:linear-gradient(to bottom,var(--page) 0 calc(var(--gap-lg)*1.975),var(--n-1) calc(var(--gap-lg)*1.975));transform:translateY(calc(var(--gap-sm)*-.25))}'+s+' .table{height:auto;align-self:flex-start;background:transparent}'+s+' thead th{box-sizing:border-box;height:calc(var(--gap-lg)*1.625);padding:0 var(--gap)}'+s+' tbody::before{content:"";display:table-row;height:calc(var(--gap)*13/12)}'+s+' tbody td{box-sizing:border-box;height:calc(var(--gap-lg)*1.175);padding:0 calc(var(--gap-sm)*1.5)}'+':where(.group)>'+s+'{flex:none;width:calc(50% - var(--gap-lg)*.75)}'+':where(.group)>'+s+':first-child{margin-right:calc(var(--gap-lg)*1.15)}')
# Original cover and divider use different hierarchy and separate geometric rails.
f=P/'crossrail/foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide.cover .lockup.at-top-left{gap:calc(var(--gap-sm)*1.75)}.slide.cover .lockup.at-top-left .kicker{font-size:var(--type-32)}.slide.cover .lockup.at-left{gap:var(--gap-sm)}.slide.cover .lockup.at-left .title{font-size:var(--type-44);font-weight:var(--title-weight)}.slide.cover .lockup.at-left .lead{margin-top:calc(var(--gap-lg)*1.7)}.slide.cover:has(.lockup.at-left) .page::before{top:calc(var(--gap-lg)*11.85);bottom:auto;height:calc(var(--gap-lg)*4.5)}.slide.cover:has(.lockup.at-left) .page::after{width:calc(var(--gap-lg)*7.5)}.slide.cover:has(.lockup.at-left) .deco{width:calc(var(--gap-lg)*7.5);height:calc(var(--gap-lg)*4.5);bottom:calc(var(--margin-y) + var(--gap-sm)/6)}.slide.cover:has(.lockup.at-left) .lockup::before{content:"";position:fixed;left:var(--rail-w);top:0;bottom:0;border-left:1px solid var(--n-4)}.slide.cover .deco>.icon{position:absolute;right:var(--gap);bottom:var(--gap);box-sizing:border-box;width:calc(var(--gap-sm)*3);height:calc(var(--gap-sm)*3);padding:calc(var(--gap-sm)*.5);border-radius:50%;background:var(--page);color:var(--a1-7)}.slide.cover .deco>.icon svg{width:100%;height:100%}\n''')
def twentyfive(s):s.select_one('.deco').append(B('<span class="icon" data-icon="chevron-right" aria-hidden="true"></span>','html.parser').find())
edit(25,twentyfive)
# Annual guide is one gray panel assembled from a title and list in the same 12x6 cell.
def twentyseven(s):
 s.select_one('[data-el="crossrail-headline"]')['style']='grid-column:1 / span 6;grid-row:3 / span 4';s.select_one('[data-el="crossrail-headline"]')['class']=['headline','quiet'];s.select_one('[data-el="crossrail-list"]')['style']='grid-column:1 / span 6;grid-row:3 / span 4'
edit(27,twentyseven)
app('headline','''[data-el="crossrail-headline"].quiet{box-sizing:border-box;background:var(--n-1);padding:var(--gap) calc(var(--gap-sm)*1.75)}[data-el="crossrail-headline"].quiet h2{font-size:var(--type-26)}''')
app('list','''[data-el="crossrail-list"].check:not(:has(.note)){padding-top:calc(var(--gap-lg)*1.7);gap:var(--gap);background:transparent;padding-left:calc(var(--gap-sm)*1.75)}''')
# Source05 paragraph breaks have been measured with the actual Noto font, rather than synthetic bold.
app('card','''[data-el="crossrail-card"].quiet:has(.parts>.kick):not(:has(.mark,.fig)) .note{letter-spacing:calc(var(--body-track)*1.5)}''')
f=P/'replica/slide_05.html';h=f.read_text().replace('font-size:18px;color:#8c8c8c;font-weight:400;line-height:1.22;letter-spacing:-0.8px','font-size:18px;color:#8c8c8c;font-weight:400;line-height:1.22;letter-spacing:-1.2px');f.write_text(h)
# Geometry defaults remain explicit chart data; ordinary fixture values are unaffected.
f=E/'hub/element.json';j=json.loads(f.read_text());j.setdefault('tokenDefaults',{})['--crossrail-cross-angle']='0deg';f.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
