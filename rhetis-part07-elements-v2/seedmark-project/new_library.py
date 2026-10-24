"""A new implementation from measured source proportions. No previous collection CSS is loaded."""
from pathlib import Path
import json,re,shutil,hashlib
from lxml import html
P=Path(__file__).parent;R=Path('/workspace/work/reference');C=P/'seedmark';C.mkdir(exist_ok=True)
T=json.loads((R/'contract/taxonomy.json').read_text())['contracts']
tokens={'--page':'#ffffff','--ink':'#2b2b2a','--font-display':"'Noto Sans KR'",'--font-body':"'Noto Sans KR'",'--weight-display':350,'--weight-body':400,'--title-weight':350,'--lead-weight':400,'--figure-weight':700,'--name-weight':700,'--body-weight':400,'--label-weight':500,'--tracking-display':'-.035em','--title-track':'-.035em','--lead-track':'-.025em','--figure-track':'-.03em','--name-track':'-.025em','--body-track':'-.025em','--label-track':'-.02em','--label-track-latin':'-.015em','--radius':'16px','--radius-sm':'7px','--stroke':'1.5px','--text-min':'14px','--margin-x':'84px','--margin-y':'64px','--gap':'24px','--gap-sm':'12px','--gap-lg':'36px','--pad':'32px','--furn-edge':'64px','--top-h':'28px','--foot-h':'24px','--furn-gap':'12px','--rail-w':'0px','--rail-gap':'0px','--title-line':1.4,'--lead-line':1.6,'--figure-line':1.15,'--name-line':1.4,'--body-line':1.6,'--label-line':1.3,'--seedmark-code-font':"'Nanum Gothic Coding'"}
(C/'kit/css').mkdir(parents=True,exist_ok=True)
(C/'kit/css/tokens.css').write_text('.slide{'+''.join(f'{k}:{v};'for k,v in tokens.items())+'}\n.slide.dark{--page:#191817;--ink:#f5f4f1;}\n')
description='Seedmark uses fine outlines, white space, soft rounded rectangles and ink capsules. A highlighted phrase is bounded by two vertical ticks with circular endpoints at opposite corners. Strong noun labels and figures contrast with light display headings. Modular surfaces keep aligned headings and generous breathing room; connectors describe relationships and never act as page decoration. Its visual identity is geometric and restrained, with palette roles supplying all surfaces and emphasis.'
(C/'kit/description.md').write_text(description+'\n');(C/'kit/kit.json').write_text(json.dumps({'schema':'rhetis.kit/2','id':'seedmark','label':'Seedmark','tokens':'css/tokens.css','description':'description.md','extensions':{'--seedmark-code-font':'font'}},ensure_ascii=False,indent=2))
F=C/'foundation';(F/'fixtures').mkdir(parents=True,exist_ok=True)
(F/'foundation.json').write_text(json.dumps({'schema':'rhetis.design-library-foundation-source/1','kit':'seedmark','registrations':{},'tokenDefaults':{}},indent=2))
(F/'foundation.css').write_text('''
.slide{position:absolute;inset:0;width:1280px;height:720px;overflow:hidden;background:var(--page);color:var(--ink);font-family:var(--font-body);font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track)}.slide *{box-sizing:border-box}.slide :is(p,h1,h2,h3,blockquote){margin:0}.page{position:absolute;inset:var(--margin-y) var(--margin-x);display:flex;flex-direction:column;gap:var(--pad)}.head{height:170px;flex:none;display:flex;flex-direction:column;align-items:center;gap:calc(var(--gap)+var(--gap-sm)/3);padding-top:calc(var(--gap-sm)*5/6);border-bottom:2px solid var(--n-3);text-align:center}.head:has(.title br){height:230px}.page:has(.head .title br){gap:calc(var(--pad)-var(--gap-sm)/2)}.head:not(:has(.title)){height:42px;border:0}.kicker{height:32px;display:inline-flex;align-items:center;justify-content:center;padding:0 calc(var(--gap)*.75);background:var(--n-7);color:var(--page);border-radius:var(--radius-sm);font-size:var(--type-22);font-weight:var(--label-weight);letter-spacing:var(--label-track-latin);line-height:var(--label-line)}.title{font-family:var(--font-display);font-size:var(--type-44);font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track)}.title b{position:relative;background:var(--a1-2-soft);font-weight:var(--name-weight);border-inline:2px solid var(--ink);padding-inline:calc(var(--gap-sm)/2)}.title b:before,.title b:after{content:'';position:absolute;width:14px;height:14px;border-radius:50%;background:var(--ink);top:-7px;left:-8px}.title b:after{top:auto;left:auto;bottom:-7px;right:-8px}.lead{font-size:var(--type-24);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track)}.body{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));gap:var(--gap);flex:1;min-height:0;margin-bottom:calc(var(--gap-sm)*1.5);container-type:size}.body>*{min-width:0;min-height:0;container-type:size}.group{display:flex;gap:var(--gap);min-width:0;min-height:0}.group>*{flex:1;min-width:0;min-height:0;container-type:size}.group.col,.stack{display:flex;flex-direction:column;gap:var(--gap);min-height:0;min-width:0}.stack>*{flex:1;min-width:0;min-height:0;container-type:size}.stack>.seat{height:0;min-height:0;aspect-ratio:1;width:auto;flex:1 1 0;align-self:flex-start;}.group.two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}.group.three{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:var(--gap)}.split.wide-left{grid-template-columns:minmax(0,1.2fr) minmax(0,1fr)}.split>*{min-width:0;min-height:0;container-type:size}.seat{width:min(100%,100cqh);aspect-ratio:1;max-width:100%;max-height:100%;background:var(--n-1);border-radius:var(--radius);display:flex;align-items:center;justify-content:center;color:var(--n-7);font-size:var(--type-16)}.seat:after{content:attr(data-ph)}.seat.avatar{border-radius:50%}.seat.portrait{aspect-ratio:4/5}.seat.logo{aspect-ratio:1}.seat.icon{width:80px;height:80px}.icon{display:inline-flex;flex:none;width:32px;height:32px}.top,.foot{position:absolute;left:var(--margin-x);right:var(--margin-x);display:flex;justify-content:space-between;align-items:center;font-size:var(--type-12);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track);color:var(--n-7)}.top{top:var(--furn-edge)}.foot{bottom:calc(var(--furn-edge)/2)}.cover .page{display:block}.lockup{position:absolute;max-width:52%;z-index:1}.at-left{left:0;top:calc(var(--pad)*3.375)}.at-top-left{left:0;top:var(--gap)}.at-bottom-left{left:0;bottom:var(--gap)}.at-center{inset:15%;max-width:none;text-align:center}.lockup .kicker{background:none;color:var(--n-7);padding:0;font-size:var(--type-32);font-weight:var(--title-weight);height:auto}.lockup .title{font-size:var(--type-100);font-weight:var(--figure-weight);line-height:var(--title-line)}.lockup .title b:before,.lockup .title b:after{width:30px;height:30px;left:-16px;top:-15px}.lockup .title b:after{left:auto;top:auto;right:-16px;bottom:-15px}.cover .seat.back,.cover .deco{position:absolute;right:calc(var(--margin-x)*-1);top:calc(var(--pad)*1.9375);width:55.5%;height:528px;border-radius:999px 0 0 999px;background:var(--n-1);aspect-ratio:auto;max-width:none;max-height:none}.cover .seat.back:after{content:none}.cover .meta{position:absolute;bottom:calc(var(--gap-sm)/2);font-size:var(--type-16);font-weight:var(--name-weight)}.rail{position:absolute;left:0;top:var(--margin-y);bottom:var(--margin-y);width:var(--rail-w)}
''')
(F/'description.md').write_text('The page is a twelve by six grid within broad margins. Small top labels, a centred capsule kicker and a light display heading form the page furniture. A fine horizontal rule closes the heading. Groups, stacks and splits only place children; they never inspect or restyle element roots. The cover uses one large phrase highlight and a pale media seat with an open capsule edge.\n')
(F/'fixtures/seat.html').write_text('<!-- min: 2x2 -->\n<div class="seat" data-ph="1" style="grid-column:1 / span 12;grid-row:1 / span 6"></div>')
(F/'fixtures/cover.html').write_text('<!-- min: 12x6 -->\n<section class="slide cover" style="grid-column:1 / span 12;grid-row:1 / span 6"><div class="page"><div class="lockup at-left"><p class="kicker">사업 성장을 잇는 이야기</p><h1 class="title">함께 여는<br><b>새로운 도약</b></h1></div><div class="seat back" data-ph="1"></div><div class="meta">세움 파트너스</div></div></section>')
CSS={}
CSS['card']='''
$ {display:flex;align-items:stretch;justify-content:center;padding:0;isolation:isolate;}
$::before{content:'';position:absolute;inset:0;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);z-index:-1;}
$.line::before{border-color:var(--ink)}$.quiet::before{background:var(--n-1);border-color:var(--n-1)}$.on::before{background:var(--a1);border-color:var(--a1)}$.on{color:var(--a1-on)}$.on .parts>.note{color:var(--a1-on)}
$.tone-1::before{background:var(--a1-2-soft);}$.tone-2::before{background:var(--a2-2-soft);}$.tone-3::before{background:var(--a3-2-soft);}$.tone-4::before{background:var(--a4-2-soft);}$.tone-5::before{background:var(--n-1);}
$ .parts{width:100%;height:100%;min-width:0;min-height:0;padding:min(var(--pad),8cqw);display:grid;grid-auto-rows:auto;align-content:center;gap:var(--gap-sm);}
$ .parts>.kick{font-size:var(--type-14);line-height:var(--label-line);font-weight:var(--label-weight)}
$ .parts>.fig{font-size:var(--type-44)}$ .parts>.name{font-size:var(--type-28);line-height:var(--name-line);font-weight:var(--name-weight)}
$ .parts>.note{font-size:var(--type-18);line-height:var(--body-line);color:var(--ink)}
$ .parts>.mark{width:min(54px,18cqw,18cqh);height:min(54px,18cqw,18cqh);display:flex;align-items:center;justify-content:center;border-radius:50%;background:var(--ink);color:var(--page);}
$ .parts>.mark .icon{width:56%;height:56%;}$ .parts>.seat{width:min(88px,24cqw,26cqh);height:auto;aspect-ratio:1;justify-self:center;}
$:has(>.parts>.mark):has(>.parts>.kick){padding:0;}
$:has(>.parts>.mark):has(>.parts>.kick)::before{top:7.26cqh}
$ .parts:has(>.mark):has(>.kick){padding:min(calc(var(--pad)*3.9),21.77cqh) min(calc(var(--pad)*3.9),11.8cqw) min(var(--gap),8cqh);grid-template-rows:min(7.9cqh,44px) minmax(0,21cqh) minmax(0,1fr);align-content:stretch;gap:var(--gap-sm);}
$ .parts:has(>.mark):has(>.kick)>.mark{position:absolute;top:0;left:50%;transform:translateX(-50%)}
$ .parts:has(>.mark):has(>.kick)>.name{border-bottom:var(--stroke) solid var(--n-3);font-size:clamp(var(--type-24),min(9cqw,10cqh),var(--type-60));text-align:center;}
$ .parts:has(>.mark):has(>.kick)>.kick{text-align:center;font-size:clamp(var(--type-12),min(4cqw,4.4cqh),var(--type-24));}
$ .parts:has(>.mark):has(>.kick)>.note{font-size:clamp(var(--type-16),min(5.06cqw,5.68cqh),var(--type-28));}
$ .parts>.list{min-height:0;}
$ .parts:has(>.fig){height:min(100%,calc(var(--pad)*9));align-self:center;grid-template-rows:24px 52px 80px minmax(0,1fr);padding:0;gap:var(--gap-sm);}
$ .parts:has(>.fig)>.kick{grid-row:1;}$ .parts:has(>.fig)>.fig{grid-row:2;}$ .parts:has(>.fig)>.name{grid-row:3;}$ .parts:has(>.fig)>.note{grid-row:4;}
@container(max-height:350px){$ .parts:has(>.fig){height:100%;grid-template-rows:18px 34px 56px minmax(0,1fr);gap:calc(var(--gap-sm)/2);}$ .parts:has(>.fig)>.name{font-size:var(--type-20);}$ .parts:has(>.fig)>.fig{font-size:var(--type-28);}$ .parts:has(>.fig)>.note{font-size:var(--type-16);}}

@container (min-aspect-ratio:2.5/1){$ .parts{display:grid;grid-template-columns:28% minmax(0,1fr);grid-template-rows:auto auto;gap:calc(var(--gap-sm)/2) var(--gap-sm);align-content:center;}$ .parts>.kick{grid-column:1;grid-row:1;}$ .parts>.name{grid-column:1;grid-row:2;font-size:var(--type-28);}$ .parts>.note{grid-column:2;grid-row:1/span 2;}$ .parts>.mark{grid-column:1;grid-row:1/span 2;}$ .parts:has(>.mark):not(:has(>.kick)){grid-template-columns:54px minmax(0,1fr);}$ .parts:has(>.mark):not(:has(>.kick))>.name{grid-column:2;grid-row:1;font-size:var(--type-22);}$ .parts:has(>.mark):not(:has(>.kick))>.note{grid-column:2;grid-row:2;}}
@container (max-width:300px){$ .parts>.name{font-size:var(--type-22)}$ .parts>.note{font-size:var(--type-16)}$ .parts>.fig{font-size:var(--type-32)}}
@container (max-height:180px){$ .parts>.name{font-size:var(--type-20)}$ .parts>.note{font-size:var(--type-14)}$ .parts>.fig{font-size:var(--type-28)}}
'''
CSS['pill']='''
${display:flex;align-items:center;justify-content:center;padding:var(--gap-sm) var(--gap);border:var(--stroke) solid var(--n-3);border-radius:999px;background:var(--page);}
$.line{border-color:var(--ink)}$.quiet{background:var(--n-1);border-color:var(--n-1)}$.on{background:var(--a1);border-color:var(--a1);color:var(--a1-on)}
$ .parts{display:flex;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);min-width:0;width:100%;}
$ .name{font-size:clamp(var(--type-18),min(10cqw,35cqh),var(--type-26));font-weight:var(--name-weight);line-height:var(--name-line);}
$ .note{font-size:var(--type-18);line-height:var(--body-line);color:inherit;}
$ .mark{min-width:26px;min-height:26px;display:flex;align-items:center;justify-content:center;font-size:var(--type-14);line-height:var(--label-line);}
$ .mark .icon{width:28px;height:28px;}
$.on .parts:has(>.note){flex-direction:column;gap:calc(var(--gap-sm)/2)}$.on .parts:has(>.note)>.name{font-size:clamp(var(--type-18),min(11.24cqw,24.54cqh),var(--type-40));}
@container(min-aspect-ratio:3/1){$ .parts,$.on .parts:has(>.note){flex-direction:row;}$ .note{font-size:var(--type-14);}}
@container(max-width:500px){$ .parts{flex-wrap:wrap}$ .note{font-size:var(--type-16)}}
@container(max-height:100px){$ .note{font-size:var(--type-14)}}
'''
CSS['headline']='''
${display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);padding:0;}
$ h2{font-family:var(--font-display);font-size:var(--type-44);font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track);}
$.big h2{font-size:var(--type-64);font-weight:var(--name-weight)}$.center{text-align:center;align-items:center}$.on{background:var(--a1);color:var(--a1-on);padding:var(--pad);border-radius:var(--radius);}
$ .kick{font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);}$ .note{font-size:var(--type-24);line-height:var(--lead-line);}
$ h2 b{position:relative;font-weight:var(--name-weight);background:var(--a1-2-soft);color:var(--ink);border-inline:2px solid var(--ink);padding-inline:calc(var(--gap-sm)/2);}
$ h2 b:before,$ h2 b:after{content:'';position:absolute;left:-8px;top:-7px;width:14px;height:14px;background:var(--ink);border-radius:50%;}$ h2 b:after{left:auto;top:auto;right:-8px;bottom:-7px;}
@container(max-width:500px){$ h2{font-size:var(--type-32)}$.big h2{font-size:var(--type-44)}$ .note{font-size:var(--type-20)}}
@container(max-height:120px){$ h2{font-size:var(--type-28)}$.big h2{font-size:var(--type-36)}$ .note{font-size:var(--type-16)}}
'''
CSS['prose']='''
${display:flex;flex-direction:column;justify-content:center;gap:var(--gap);padding:0;}
$ p{font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);word-break:keep-all;overflow-wrap:anywhere;}
$ b{font-weight:var(--name-weight)}$.lead p{font-size:var(--type-28);font-weight:var(--lead-weight);line-height:var(--lead-line)}$.quiet{color:var(--n-7)}$.cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--gap-lg);align-content:center;}$.cols p{grid-column:auto;}
@container(max-width:500px){$ p{font-size:var(--type-16)}$.lead p{font-size:var(--type-24)}$.cols p{grid-column:span 2}}
@container(max-height:150px){$ p{font-size:var(--type-14)}$.lead p{font-size:var(--type-20)}}
'''
CSS['metric']='''
$.stat{padding:var(--gap-sm) 0;border-bottom:var(--stroke) solid var(--n-3);display:flex;align-items:center;}
$ .parts{display:grid;width:100%;grid-template-columns:28% minmax(0,1fr);grid-template-rows:auto auto;gap:calc(var(--gap-sm)/2) var(--gap-sm);align-content:center;}
$ .fig{grid-column:1;grid-row:1;font-size:clamp(var(--type-28),min(12cqw,33.33cqh),var(--type-40));line-height:var(--name-line);font-weight:var(--figure-weight);letter-spacing:var(--figure-track);}
$ .name{grid-column:1;grid-row:2;font-size:var(--type-16);line-height:var(--name-line);}
$ .note{grid-column:2;grid-row:1/span 2;font-size:clamp(var(--type-14),min(5cqw,18cqh),var(--type-18));line-height:var(--body-line);}
$.stats{display:flex;align-items:stretch;gap:var(--gap)}$.stats>.stat{flex:1;min-width:0;container-type:size;display:flex;align-items:center;padding:var(--gap);border-right:var(--stroke) solid var(--n-3);}
$.stats>.stat:last-child{border-right:0}
@container(max-aspect-ratio:3/1){$ .parts{grid-template-columns:28% minmax(0,1fr);grid-template-rows:auto auto;}$ .name{grid-column:2;grid-row:1;align-self:center;}$ .note{grid-column:1/span 2;grid-row:2;}}
@container(max-width:300px){$ .name{font-size:var(--type-14)}}
'''
CSS['tag']='''
$.tag{display:inline-flex;align-items:center;justify-content:center;align-self:center;justify-self:center;width:min(100%,96px);max-width:100%;min-height:26px;height:26px;padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)*.833333);border:1px solid var(--ink);border-radius:var(--radius-sm);font-size:var(--type-12);font-weight:var(--label-weight);line-height:var(--label-line);text-align:center;}
$.hl{display:inline;position:relative;background:var(--a1-2-soft);border-inline:2px solid var(--ink);padding-inline:calc(var(--gap-sm)/2);font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line);}
$.hl:before,$.hl:after{content:'';position:absolute;width:10px;height:10px;left:-6px;top:-5px;border-radius:50%;background:var(--ink)}$.hl:after{left:auto;top:auto;right:-6px;bottom:-5px;}
'''
CSS['callout']='''
${display:flex;align-items:center;justify-content:center;gap:var(--gap);padding:var(--gap-sm) var(--gap);background:var(--n-1);border-radius:var(--radius);text-align:center;}
$ p{font-size:var(--type-24);line-height:var(--lead-line);font-weight:var(--lead-weight);}
$ b{font-weight:var(--name-weight);background:var(--a1-2-soft);color:var(--ink);border-inline:2px solid var(--ink);padding-inline:calc(var(--gap-sm)/2);}
$>.icon{width:40px;height:40px;flex:none;}
@container(max-width:650px){$ p{font-size:var(--type-20)}}@container(max-height:130px){$ p{font-size:var(--type-16)}}
'''
CSS['list']='''
${display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);padding:var(--gap-sm);counter-reset:item;}
$ .item{position:relative;display:grid;grid-template-columns:minmax(0,1fr);gap:calc(var(--gap-sm)/2);padding-left:var(--gap);counter-increment:item;}
$ .item:before{content:'';position:absolute;left:calc(var(--gap-sm)/3);top:.65em;width:5px;height:5px;border-radius:50%;background:var(--ink);}
$.num .item:before{content:counter(item,decimal-leading-zero);background:none;width:auto;height:auto;top:0;font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--name-line);}
$.check .item:before{top:.45em;width:12px;height:8px;border-radius:0;background:none;border-left:2px solid var(--ink);border-bottom:2px solid var(--ink);transform:rotate(-45deg);}
$.divided{gap:0;padding:0}$.divided .item{flex:1;border-top:var(--stroke) solid var(--n-3);padding-top:var(--gap-sm);padding-bottom:var(--gap-sm);align-content:center;}$.divided .item:last-child{border-bottom:var(--stroke) solid var(--n-3)}
$ .name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line)}$ .note{font-size:var(--type-18);color:var(--n-7);line-height:var(--body-line)}
$ .item:has(>.mark){padding-left:calc(var(--pad)*2.1875);min-height:64px;}
$ .item:has(>.mark):before{display:none}$ .item>.mark{position:absolute;left:0;top:50%;transform:translateY(-50%);width:54px;height:54px;border-radius:50%;background:var(--ink);color:var(--page);display:flex;align-items:center;justify-content:center;}$ .mark>.icon{width:56%;height:56%;}
@container(max-width:500px){$ .name{font-size:var(--type-18)}$ .note{font-size:var(--type-16)}}@container(max-height:350px){$ .item{padding-top:calc(var(--gap-sm)/6);padding-bottom:calc(var(--gap-sm)/6);gap:calc(var(--gap-sm)/4);}$ .name{font-size:var(--type-16)}$ .note{font-size:var(--type-14)}}
'''
CSS['legend']='''
${display:flex;flex-direction:column;align-items:flex-start;justify-content:center;gap:calc(var(--gap-sm)/6);padding:calc(var(--gap-sm)/2);}
$ .key{display:flex;align-items:center;gap:calc(var(--gap-sm)/2);font-size:var(--type-12);line-height:var(--label-line);color:var(--ink)}$ .key:before{content:'';width:8px;height:8px;border-radius:calc(var(--radius-sm)/3);background:var(--a1);flex:none;}
@container(max-height:100px){$ .key{font-size:var(--type-10);}}
$ .key.tone-2:before{background:var(--a2)}$ .key.tone-3:before{background:var(--a3)}$ .key.tone-4:before{background:var(--a4)}$ .key.tone-5:before{background:var(--n-4)}
'''
# End of the first source-derived base set. More complete modules are emitted by the same single-write generator.
def common(folder):
 return '''${position:relative;box-sizing:border-box;min-width:0;min-height:0;container-type:size;color:var(--ink);font-family:var(--font-body);font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);} $ *{box-sizing:border-box;} $ :is(p,h2,h3,blockquote){margin:0;} $ .icon{display:inline-flex;flex:none;width:32px;height:32px;} $ .fig{font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);} $ .fig small{font-size:var(--type-20);color:inherit;margin:0;} $ .seat{display:flex;align-items:center;justify-content:center;aspect-ratio:1;background:var(--n-1);color:var(--n-7);font-size:var(--type-14);border-radius:var(--radius);} $ .seat:after{content:attr(data-ph);}'''
def emit():
 for con in T:
  folder=con['category'].split('.')[-1]
  # Category names differ from source folders; ids map through the README root table ordering.
  folder=FOLDERS[con['id']]
  if folder not in CSS:continue
  E=C/'elements'/folder;(E/'fixtures').mkdir(parents=True,exist_ok=True)
  from scope_css import compile_css
  maps=json.loads((P/'map.json').read_text())['instances'];base=next((i for i in maps if i['leaf']==folder and i['use']=='base'),None)
  origin=f"Measured base: page {base['page']}, bbox {base['bbox']}."if base else'Inferred from the Seedmark outline, capsule and typographic grammar.'
  (E/'element.css').write_text('/* '+origin+' Own-container geometry; no page or fixture condition. */\n'+compile_css(common(folder)+'\n'+CSS[folder],con['roots'],folder)+'\n')
  (E/'element.json').write_text(json.dumps({'schema':'rhetis.design-library-element-source/1','contract':con['id'],'registrations':{},'tokenDefaults':{}},indent=2))
  (E/'description.md').write_text(f'This {folder} follows the measured Seedmark grammar of fine neutral rules, rounded surfaces and deliberate empty space. Its content hierarchy separates strong names and figures from light supporting text. It responds to its own allotted width and height through container queries, while every exposed member remains readable. Palette roles supply the surfaces, boundaries and emphasis in both modes; the component never relies on a page identifier or neighbouring element.\n')
FOLDERS={}
for f in (R/'samples/annual/elements').iterdir():
 meta=json.loads((f/'element.json').read_text());FOLDERS[meta['contract']]=f.name
if __name__=='__main__':emit();print('Fresh source base CSS:',','.join(CSS))
