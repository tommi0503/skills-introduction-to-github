from pathlib import Path
import json,re,shutil
BASE=Path('/workspace/work/deliverables/inflexion');C=BASE/'collection/inflexion';REF=Path('/workspace/work/reference');NAME='inflexion'
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def js(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
tokens={'--page':'#f8fbfd','--ink':'#2d2f30','--font-display':"'Pretendard Variable'",'--font-body':"'Pretendard Variable'",'--weight-display':'800','--weight-body':'450','--tracking-display':'-0.035em','--radius':'32px','--radius-sm':'16px','--stroke':'1px','--text-min':'14px','--margin-x':'82px','--margin-y':'52px','--gap':'24px','--gap-sm':'8px','--gap-lg':'32px','--pad':'24px','--furn-edge':'20px','--top-h':'28px','--foot-h':'24px','--furn-gap':'16px','--rail-w':'36px','--rail-gap':'20px'}
for role,weight,line,track in [('title',800,1.16,'-0.035em'),('lead',600,1.45,'-0.025em'),('figure',750,1.3,'-0.04em'),('name',650,1.3,'-0.025em'),('body',450,1.55,'-0.02em'),('label',650,1.25,'-0.015em')]:
 tokens.update({f'--{role}-weight':str(weight),f'--{role}-line':str(line),f'--{role}-track':track})
tokens['--label-track-latin']='0em'
tokens['--inflexion-font-code']="'Nanum Gothic Coding'"
line_tokens={'1':'tight','1.05':'display','1.2':'figure','1.25':'label','1.35':'compact','1.38':'heading','1.4':'copy','1.5':'note','1.55':'body','38px':'header'}
for value,key in line_tokens.items():tokens['--inflexion-line-'+key]=value
write(C/'kit/css/tokens.css','.slide {\n'+''.join(f'  {k}: {v};\n' for k,v in tokens.items())+'}\n.slide.dark { --page: #10151e; --ink: #f1f5fb; }\n')
js(C/'kit/kit.json',{'schema':'rhetis.kit/2','id':NAME,'label':'Inflexion','tokens':'css/tokens.css','description':'description.md','extensions':{'--inflexion-font-code':'font',**{'--inflexion-line-'+v:('length' if k.endswith('px') else 'number') for k,v in line_tokens.items()}}})
write(C/'kit/description.md','An airy investor presentation system with a shallow inward bend in fine horizontal rules, broad rounded panels, capsule labels and orbit-like circular relationships. Strong display figures and compact semantic labels carry the emphasis while quiet secondary surfaces preserve generous breathing room.\n')
F='''
.slide {width:1280px;height:720px;position:relative;overflow:hidden;background:var(--page);color:var(--ink);font-family:var(--font-body);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);box-sizing:border-box;}
.slide .page {height:100%;padding:var(--margin-y) var(--margin-x);box-sizing:border-box;display:flex;flex-direction:column;gap:var(--gap-lg);position:relative;}
.slide .head {flex:none;position:relative;min-height:calc(var(--top-h) + var(--gap));display:flex;align-items:baseline;gap:var(--gap);border-bottom:var(--stroke) solid var(--a1);padding-bottom:var(--furn-gap);}
.slide .head::before,.slide .head::after {content:"";position:absolute;bottom:calc(var(--gap-sm) * -1);width:var(--gap-lg);height:var(--gap-sm);background:var(--page);border-top:var(--stroke) solid var(--a1);}
.slide .head::before {right:50%;border-radius:0 100% 0 0;}.slide .head::after {left:50%;border-radius:100% 0 0 0;}
.slide .head .title {font-family:var(--font-display);font-size:var(--type-36);font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track);margin:0;color:var(--a1);border-left:6px solid var(--a1);padding-left:var(--furn-gap);}
.slide .head .kicker {font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track);margin:0;order:2;}
.slide .head .lead {font-size:var(--type-18);font-weight:var(--lead-weight);line-height:var(--lead-line);margin:0;}
.slide .head.center {justify-content:center;text-align:center;}
.slide .body {flex:1;min-height:0;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));gap:var(--gap);container-type:size;position:relative;}
.slide .group {display:flex;align-items:stretch;gap:var(--gap);min-width:0;min-height:0;container-type:size;}.slide .group>* {flex:1;min-width:0;min-height:0;}.slide .group.col,.slide .stack {display:flex;flex-direction:column;gap:var(--gap);min-width:0;min-height:0;container-type:size;}.slide .stack>* {min-height:0;}.slide .split {display:grid;grid-template-columns:1fr 1.5fr;gap:var(--gap);min-width:0;min-height:0;container-type:size;}.slide .split.wide-left {grid-template-columns:1.5fr 1fr;}.slide .group.two {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));}.slide .group.three {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));}
.slide .seat {background:var(--n-2);color:var(--n-7);display:flex;justify-content:center;align-items:center;min-width:0;min-height:0;aspect-ratio:1;font-size:var(--type-14);font-weight:var(--label-weight);border-radius:var(--radius-sm);}.slide .seat::after {content:attr(data-ph);}.slide .seat.avatar {border-radius:50%;}.slide .seat.portrait {aspect-ratio:3/4;}.slide .seat.logo {aspect-ratio:1;}.slide .seat.back {position:absolute;inset:0;aspect-ratio:auto;z-index:0;}.slide .icon {display:inline-block;width:var(--gap-lg);height:var(--gap-lg);flex:none;}.slide .top,.slide .foot {position:absolute;left:var(--margin-x);right:var(--margin-x);display:flex;justify-content:space-between;align-items:center;font-size:var(--type-12);font-weight:var(--label-weight);color:var(--a1);}.slide .top{top:var(--furn-edge);}.slide .foot{bottom:var(--furn-edge);}.slide .rail{position:absolute;left:var(--furn-edge);top:var(--margin-y);bottom:var(--margin-y);width:var(--rail-w);display:flex;flex-direction:column;gap:var(--gap-sm);}
.slide.cover .page {display:flex;justify-content:center;}.slide.cover .lockup {position:relative;z-index:1;width:62%;}.slide.cover .lockup .title{font-size:var(--type-100);font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track);color:var(--a1);margin:0;}.slide.cover .lockup .lead{font-size:var(--type-28);font-weight:var(--lead-weight);line-height:var(--lead-line);margin:var(--gap) 0 0;}.slide.cover .lockup .kicker{font-size:var(--type-16);font-weight:var(--label-weight);margin:0 0 var(--gap);}.slide.cover .at-center{align-self:center;text-align:center;}.slide.cover .at-bottom-left{margin-top:auto;}.slide.cover .at-top-left{margin-bottom:auto;}.slide.cover .meta{position:absolute;left:var(--margin-x);bottom:var(--margin-y);font-size:var(--type-14);}.slide.cover .deco{position:absolute;right:var(--margin-x);top:25%;width:36%;aspect-ratio:1;border:var(--stroke) solid var(--a1);border-radius:50%;}.slide.cover .deco::before{content:"";position:absolute;inset:16%;border:var(--stroke) solid var(--a1);border-radius:50%;}.slide.cover .deco::after{content:"";position:absolute;left:-20%;right:-20%;top:50%;border-top:var(--stroke) solid var(--a1);transform:rotate(-30deg);}
'''
F+='\n.slide .stack>*{flex:1;} .slide .body>.seat{aspect-ratio:1;width:auto;height:100%;max-width:100%;justify-self:center;} .slide .head .kicker{margin-left:auto;text-align:right;font-size:var(--type-12);color:var(--a1);}.slide.cover .seat.back{left:58%;right:0;top:18%;bottom:0;} .slide.cover .lockup.at-left{transform:translateY(calc(var(--gap-lg)*-2));} .slide.cover .lockup .title{font-size:var(--type-120);} .slide.cover .meta{display:flex;flex-direction:column;gap:var(--gap-sm);width:calc(var(--type-128) + var(--gap));}\n'
F+='''
.slide .page{gap:64px;}.slide .head{height:58px;min-height:58px;padding-bottom:0;align-items:flex-start;gap:16px;}.slide .head .title{line-height:1.05;}.slide .head .lead{line-height:38px;}.slide .head .kicker{border-left:5px solid var(--a1);padding-left:28px;height:30px;line-height:1.55;margin-top:3px;}.slide .head::before,.slide .head::after{width:40px;height:14px;bottom:-14px;}
'''
F+='\n.slide .body{grid-template-rows:35px 35px repeat(4,minmax(0,1fr));}\n'
F=F.replace('color:var(--a1);','color:var(--a1-7);')
F=re.sub(r'line-height:([0-9.]+(?:px)?)',lambda m:'line-height:var(--inflexion-line-'+line_tokens[m.group(1)]+')',F)
write(C/'foundation/foundation.css',F)
js(C/'foundation/foundation.json',{'schema':'rhetis.design-library-foundation-source/1','kit':NAME,'registrations':{},'tokenDefaults':{}})
write(C/'foundation/description.md','An airy twelve-by-six stage with a compact bilingual header, a thin horizontal rule dipping gently at the centre, generous outside margins and optional quiet top and footer furniture. Covers use a large left lockup with a restrained orbital construction.\n')
write(C/'foundation/fixtures/seat.html','<!-- min: 3x3 -->\n<div class="seat" data-ph="1" style="grid-column:1 / span 12; grid-row:1 / span 6"></div>\n')
write(C/'foundation/fixtures/cover.html','<!-- min: 12x6 -->\n<section class="slide cover"><div class="page"><div class="lockup at-left"><p class="kicker">투자자를 위한 새로운 성장 여정</p><h1 class="title">Our Next<br>Inflection</h1><p class="lead">명확한 가치, 검증된 성장</p></div><div class="deco"></div><p class="meta">MIRIH COMPANY · 2080.09</p></div></section>\n')
# Same contract fixtures/data; only the identity prefix changes. No sample CSS is used.
model={'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),'callout':('annual',['callout','callout-icon','callout-stack']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}
contracts=json.loads((REF/'contract/taxonomy.json').read_text())['contracts']
ROOT={}
for c in contracts:
 leaf=c['category'].split('.')[-1];ROOT[leaf]=c['roots'];d=C/'elements'/leaf;d.mkdir(parents=True,exist_ok=True)
 js(d/'element.json',{'schema':'rhetis.design-library-element-source/1','contract':c['id'],'registrations':{},'tokenDefaults':{}})
 write(d/'description.md',f'The {leaf} uses Inflexion’s compact capsule labels, fine orbital rules and broad quiet surfaces. A single primary accent identifies the point; restrained secondary tones and a stepped typographic scale keep long Korean business labels legible in both modes.\n')
 sample,files=model.get(leaf,('annual',None));src=REF/'samples'/sample/'elements'/leaf/'fixtures'
 fs=[src/(f+'.html') for f in files] if files else sorted(src.glob('*.html'))
 for f in fs:
  s=f.read_text();s=re.sub(r'data-el="(?:annual|confetti|amethyst)-',f'data-el="{NAME}-',s)
  # Non-model fixture placement is full slot, as required by the contract.
  if leaf not in model:s=re.sub(r'grid-column:[^;"\n]+;\s*grid-row:[^;"\n]+', 'grid-column:1 / span 12; grid-row:1 / span 6',s,count=1)
  write(d/'fixtures'/f.name,s)
 if leaf=='waffle':
  f=d/'fixtures/waffle-figures.html';s=f.read_text().replace('min: 6x1','min: 8x4');write(f,s)
 if leaf=='tag':
  for f in (d/'fixtures').glob('*.html'):
   s=f.read_text().replace('min: 4x1','min: 8x2').replace('<div class="prose"','<div class="prose" data-el="inflexion-prose"');write(f,s)
 if len(fs)<2:
  s=(d/'fixtures'/fs[0].name).read_text().replace('매출','해외 매출').replace('고객','장기 고객').replace('전환','지속 전환');write(d/'fixtures'/'expanded.html',s)
# Each stylesheet is generated from hand-authored contract-specific geometry.
CSS={}
def rule(k,s):CSS[k]=s
common='''& {position:relative;min-width:0;min-height:0;box-sizing:border-box;container-type:size;font-family:var(--font-body);font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);color:var(--ink);anchor-scope:all;}
& *{box-sizing:border-box;min-width:0;}
& .name{font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);margin:0;}
& .note{font-size:var(--type-16);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);color:var(--n-7);margin:0;}
& .kick{font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track);color:var(--a1);margin:0;}
& .fig{font-size:var(--type-64);font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);margin:0;color:var(--a1);}
& small{color:inherit;margin-left:0;font-size:var(--type-20);font-weight:var(--label-weight);letter-spacing:var(--label-track);}
& .icon{width:var(--gap-lg);height:var(--gap-lg);display:inline-block;flex:none;}
@container (max-width:550px){ & .name{font-size:var(--type-20);} & .fig{font-size:var(--type-48);} & .note{font-size:var(--type-14);} }
@container (max-width:300px){ & .name{font-size:var(--type-16);} & .fig{font-size:var(--type-32);} & .kick{font-size:var(--type-12);} }
@container (max-height:220px){ & .name{font-size:var(--type-18);} & .fig{font-size:var(--type-40);} & .note{font-size:var(--type-14);} }
'''
rule('card','''& {display:flex;align-items:center;padding:var(--pad);border-radius:var(--radius);background:linear-gradient(145deg,var(--page),var(--n-2));border:var(--stroke) solid var(--n-2);}
& .parts{width:100%;display:grid;align-content:center;gap:var(--gap-sm);}
& .mark{width:56px;height:56px;border-radius:50%;border:var(--stroke) solid var(--a1);display:flex;align-items:center;justify-content:center;color:var(--a1);font-size:var(--type-24);font-weight:var(--label-weight);margin-bottom:var(--gap-sm);}
& .mark .icon{width:32px;height:32px;} & .mark.seat{background:var(--n-2);border:0;width:72px;height:72px;} & .name{color:var(--a1);}
&.line{background:var(--page);border-color:var(--a1);border-radius:calc(var(--radius)*1.8);}
&.quiet{background:var(--page);border-color:var(--n-2);}
&.on{background:var(--a1);border-color:var(--a1);}
&.on .name,&.on .fig,&.on .kick,&.on .note,&.on .mark{color:var(--a1-on);border-color:var(--a1-on);}
&.tone-1{background:var(--a1-1-soft);} &.tone-2{background:var(--a2-1-soft);} &.tone-3{background:var(--n-1);} &.tone-4{background:var(--a3-1-soft);} &.tone-5{background:var(--n-2);}
@container (max-width:280px){& .mark{width:40px;height:40px;}& .mark .icon{width:22px;height:22px;}& .parts{gap:var(--gap-sm);}}
''')
rule('pill','''&{padding:var(--gap-sm) var(--pad);border-radius:999px;background:var(--n-1);display:flex;align-items:center;justify-content:center;min-height:var(--gap-lg);border:var(--stroke) solid var(--n-2);}
& .parts{display:flex;align-items:center;justify-content:center;gap:var(--gap-sm);width:100%;}
& .name{font-size:var(--type-18);text-align:center;}& .note{font-size:var(--type-14);}& .mark{display:flex;align-items:center;justify-content:center;width:var(--gap);height:var(--gap);font-size:var(--type-16);font-weight:var(--label-weight);}
&.on{background:var(--a1);color:var(--a1-on);border-color:var(--a1);}&.on .name,&.on .note{color:var(--a1-on);}&.line{background:var(--page);border-color:var(--a1);}&.quiet{background:var(--page);border-color:var(--n-2);}
@container (max-width:450px){& .note{font-size:var(--type-12);}& .name{font-size:var(--type-16);}}
''')
rule('callout','''&{display:flex;align-items:center;justify-content:center;gap:var(--gap);padding:var(--pad);background:linear-gradient(150deg,var(--a1),var(--a1-7));color:var(--a1-on);border-radius:var(--radius) var(--radius) 0 0;}
& p{margin:0;font-size:var(--type-28);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track);} & b{font-weight:var(--title-weight);}
& .icon{width:48px;height:48px;}
@container (max-height:150px){& p{font-size:var(--type-20);}} @container (max-width:500px){& p{font-size:var(--type-20);}& .icon{width:32px;height:32px;}}
''')
rule('tag','''&.tag{display:inline-flex;align-items:center;justify-content:center;vertical-align:middle;background:var(--a1);color:var(--a1-on);border-radius:999px;padding:calc(var(--gap-sm)/2) calc(var(--pad)/2);font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track);}
&.hl{font-weight:var(--name-weight);color:var(--a1);background:var(--a1-1-soft);padding:0 calc(var(--gap-sm)/2);border-bottom:var(--stroke) solid var(--a1);}
''')
rule('headline','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);}
& h2{font-family:var(--font-display);font-size:var(--type-36);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--title-track);margin:0;}
& h2 b{color:var(--a1);font-weight:var(--title-weight);}
&.big h2{font-size:var(--type-56);}&.center{text-align:center;align-items:center;}&.on{background:var(--a1);color:var(--a1-on);border-radius:var(--radius);padding:var(--pad);}&.on h2 b,&.on .kick,&.on .note{color:var(--a1-on);}
@container (max-width:600px){& h2{font-size:var(--type-28);}&.big h2{font-size:var(--type-40);}} @container (max-height:190px){& h2,&.big h2{font-size:var(--type-28);}}
''')
rule('prose','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap);font-size:var(--type-20);}
& p{margin:0;line-height:var(--body-line);}& b{font-weight:var(--name-weight);color:var(--a1);}&.lead{font-size:var(--type-28);}&.quiet{color:var(--n-7);}&.cols{display:block;column-count:2;column-gap:var(--gap-lg);}&.cols p+p{margin-top:var(--gap);}
@container (max-width:550px){&{font-size:var(--type-16);}&.lead{font-size:var(--type-22);}&.cols{column-count:1;}} @container (max-height:220px){&{font-size:var(--type-16);}}
''')
rule('list','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap);counter-reset:item;}
& .item{position:relative;display:grid;grid-template-columns:var(--gap-lg) 1fr;gap:calc(var(--gap-sm)/2) var(--gap);counter-increment:item;}
& .item::before{content:"";grid-column:1;grid-row:1/3;width:8px;height:8px;border-radius:50%;background:var(--a1);align-self:start;margin-top:var(--gap-sm);justify-self:center;}
& .item .name,& .item .note{grid-column:2;}& .item .name{font-size:var(--type-22);color:var(--a1);}
&.num .item::before{content:counter(item,decimal-leading-zero);width:var(--gap-lg);height:var(--gap-lg);margin:0;color:var(--a1-on);display:flex;align-items:center;justify-content:center;font-size:var(--type-16);font-weight:var(--label-weight);}
&.check .item::before{width:14px;height:8px;border-radius:0;border-left:2px solid var(--a1);border-bottom:2px solid var(--a1);background:none;transform:rotate(-45deg);}
&.divided .item+.item{border-top:var(--stroke) solid var(--n-3);padding-top:var(--gap);}
& .mark{position:absolute;left:0;top:0;width:var(--gap-lg);height:var(--gap-lg);display:flex;align-items:center;justify-content:center;background:var(--page);}& .mark .icon{width:24px;height:24px;}
@container (max-height:300px){&{gap:var(--gap-sm);}& .item .name{font-size:var(--type-18);}&.divided .item+.item{padding-top:var(--gap-sm);}} @container (max-width:350px){& .item{column-gap:var(--gap-sm);}& .item .name{font-size:var(--type-16);}}
''')
rule('quote','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap-lg);border-top:var(--stroke) solid var(--a1);border-bottom:var(--stroke) solid var(--a1);padding:var(--pad);border-radius:var(--radius);background:var(--n-1);}
& blockquote{font-size:var(--type-32);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track);margin:0;color:var(--a1);}
&.big blockquote{font-size:var(--type-44);}& .by{display:grid;grid-template-columns:64px 1fr;gap:0 var(--gap);align-items:center;}& .by .seat{width:64px;height:64px;grid-row:1/3;}& .by .name{font-size:var(--type-20);}
@container (max-width:550px){& blockquote,&.big blockquote{font-size:var(--type-26);}} @container (max-height:260px){& blockquote,&.big blockquote{font-size:var(--type-22);}& .by .seat{width:40px;height:40px;}& .by{grid-template-columns:40px 1fr;}}
''')
rule('metric','''&.stats{display:flex;align-items:center;gap:var(--gap);}&.stats>.stat{flex:1;min-height:0;padding:var(--pad);border-left:var(--stroke) solid var(--n-3);}&.stats>.stat:first-child{border-left:0;}
&.stat{display:flex;flex-direction:column;justify-content:center;}& .parts{display:grid;gap:var(--gap-sm);width:100%;}& .fig{font-size:var(--type-80);}& .name{font-size:var(--type-24);}
@container (max-height:160px){& .fig{font-size:var(--type-48);}& .name{font-size:var(--type-18);}& .note{font-size:var(--type-12);}} @container (max-width:600px){& .fig{font-size:var(--type-48);}& .name{font-size:var(--type-18);}}
''')
rule('delta','''&{display:flex;align-items:center;justify-content:center;gap:var(--gap);font-size:var(--type-40);font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);}
& .from{color:var(--n-7);}& .to{color:var(--a1);}& .to::before{content:"";display:inline-block;width:40px;height:14px;background:var(--a1);clip-path:polygon(0 45%,75% 45%,75% 0,100% 50%,75% 100%,75% 55%,0 55%);margin-right:var(--gap);}
@container (max-width:500px){&{font-size:var(--type-28);}& .to::before{width:28px;}}
''')
rule('legend','''&{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:var(--gap);font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);}
& .key{display:flex;align-items:center;gap:var(--gap-sm);}& .key::before{content:"";width:16px;height:16px;border-radius:calc(var(--radius-sm)/4);background:var(--a1);}& .tone-2::before{background:var(--a2);}& .tone-3::before{background:var(--a3);}& .tone-4::before{background:var(--a4);}& .tone-5::before{background:var(--n-4);}
@container (max-width:450px){&{gap:var(--gap-sm);font-size:var(--type-14);}}
''')
rule('chart-bar','''&{display:flex;gap:var(--gap);align-items:stretch;border-bottom:var(--stroke) solid var(--n-4);background:repeating-linear-gradient(to top,var(--n-2) 0 1px,var(--page) 1px 25%);}
& .bar{flex:1;height:100%;position:relative;text-align:center;--inflexion-series:var(--n-3);}
& .bar::before{content:"";position:absolute;left:12%;right:12%;bottom:var(--gap-lg);height:calc((100% - var(--gap-lg)*2)*var(--v)/var(--max));background:var(--inflexion-series);border-radius:var(--radius-sm) var(--radius-sm) 0 0;}
& .bar.on{--inflexion-series:var(--a1);}& .bar.tone-1{--inflexion-series:var(--a1);}& .bar.tone-2{--inflexion-series:var(--a2);}& .bar.tone-3{--inflexion-series:var(--a3);}& .bar.tone-4{--inflexion-series:var(--a4);}
& .bar b{position:absolute;left:0;right:0;bottom:calc(var(--gap-lg) + (100% - var(--gap-lg)*2)*var(--v)/var(--max) + var(--gap-sm));font-size:var(--type-20);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--a1);}
& .bar span{position:absolute;left:0;right:0;bottom:0;font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);color:var(--n-7);}
&.h{display:flex;flex-direction:column;background:none;border:0;gap:var(--gap-sm);}&.h .bar{flex:1;min-height:0;text-align:left;}&.h .bar::before{left:20%;right:auto;top:20%;bottom:20%;width:calc((100% - 30%)*var(--v)/var(--max));height:auto;border-radius:0 var(--radius-sm) var(--radius-sm) 0;}&.h .bar span{left:0;right:auto;top:50%;bottom:auto;transform:translateY(-50%);width:18%;}&.h .bar b{left:calc(22% + 70%*var(--v)/var(--max));right:auto;top:50%;bottom:auto;transform:translateY(-50%);}
@container (max-width:650px){&{gap:var(--gap-sm);}& .bar b{font-size:var(--type-16);}& .bar span{font-size:var(--type-12);}}
''')
rule('chart-line','''&{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr) var(--gap-lg);background:repeating-linear-gradient(to top,var(--n-2) 0 1px,var(--page) 1px 25%);}
& .pt{display:contents;}
& .pt b{grid-row:1;align-self:start;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:calc(100% - var(--v)/var(--max)*(100% - var(--gap-lg)));font-size:var(--type-18);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--a1);anchor-name:var(--inflexion-self);padding-bottom:var(--gap-sm);}
& .pt b::after{content:"";position:absolute;width:8px;height:8px;border-radius:50%;background:var(--a1);bottom:-4px;}
& .pt span{grid-row:2;text-align:center;border-top:var(--stroke) solid var(--n-4);font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);padding-top:var(--gap-sm);color:var(--n-7);}
& .pt::before,& .pt::after{content:"";position:absolute;left:anchor(var(--inflexion-prev) center);right:anchor(var(--inflexion-self) center);pointer-events:none;}
& .pt::before{top:calc(anchor(var(--inflexion-prev) bottom) - 1px);bottom:calc(anchor(var(--inflexion-self) bottom) - 1px);background:linear-gradient(to top right,transparent calc(50% - 1px),var(--a1) 50%,transparent calc(50% + 1px));}
& .pt::after{top:calc(anchor(var(--inflexion-self) bottom) - 1px);bottom:calc(anchor(var(--inflexion-prev) bottom) - 1px);background:linear-gradient(to bottom right,transparent calc(50% - 1px),var(--a1) 50%,transparent calc(50% + 1px));}
& .pt:first-child::before,& .pt:first-child::after{content:none;}
@container (max-width:650px){& .pt b{font-size:var(--type-14);}& .pt span{font-size:var(--type-12);}}
''')
rule('chart-area','''&{background:repeating-linear-gradient(to top,var(--n-2) 0 1px,var(--page) 1px 25%);}
& .series{--inflexion-series:var(--a1);position:absolute;inset:0 0 var(--gap-lg);display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);anchor-scope:all;}
& .series.tone-2{--inflexion-series:var(--a2);}& .series.tone-3{--inflexion-series:var(--a3);}& .series.tone-4{--inflexion-series:var(--a4);}
& .series>.name{position:absolute;top:0;left:0;font-size:var(--type-14);font-weight:var(--label-weight);color:var(--ink);line-height:var(--label-line);border-left:8px solid var(--inflexion-series);padding-left:var(--gap-sm);z-index:5;}
& .series:nth-child(2)>.name{left:25%;}& .series:nth-child(3)>.name{left:50%;}& .series:nth-child(4)>.name{left:75%;}
& .pt{--inflexion-h:calc(100cqh - var(--gap-lg)*2);--inflexion-vh:calc(var(--inflexion-h)*var(--v)/var(--max));align-self:start;justify-self:center;width:0;height:0;margin-top:calc(var(--gap-lg) + var(--inflexion-h) - var(--inflexion-vh));anchor-name:var(--inflexion-self);}
& .pt::before,& .pt::after{content:"";position:absolute;left:anchor(var(--inflexion-prev) center);right:anchor(var(--inflexion-self) center);top:calc(anchor(var(--inflexion-prev) top) - var(--inflexion-h));bottom:0;}
& .pt::before{background:color-mix(in srgb,var(--inflexion-series) 24%,transparent);clip-path:polygon(0 var(--inflexion-h),100% calc(100% - var(--inflexion-vh)),100% 100%,0 100%);}
& .pt::after{background:var(--inflexion-series);clip-path:polygon(0 calc(var(--inflexion-h) - 1px),100% calc(100% - var(--inflexion-vh) - 1px),100% calc(100% - var(--inflexion-vh) + 1px),0 calc(var(--inflexion-h) + 1px));}
& .pt:first-of-type::before,& .pt:first-of-type::after{content:none;}
& .pt b{position:absolute;left:0;bottom:var(--gap-sm);transform:translateX(-50%);font-size:var(--type-16);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--inflexion-series);}
& .pt b::after{content:"";position:absolute;left:calc(50% - 3px);top:100%;width:6px;height:6px;border-radius:50%;background:var(--inflexion-series);}
& .axis{position:absolute;left:0;right:0;bottom:0;height:var(--gap-lg);display:flex;border-top:var(--stroke) solid var(--n-4);align-items:center;}
& .axis span{flex:1;text-align:center;font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);}
&.stacked .pt::before{opacity:.8;}
@container (max-width:600px){& .pt b,& .axis span,& .series>.name{font-size:var(--type-12);}}
''')
rule('chart-donut','''&.donuts{display:flex;align-items:center;justify-content:center;gap:var(--gap);}
& .donut,&.donut{position:relative;flex:1;min-width:0;min-height:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);padding:var(--pad);aspect-ratio:1;}
& .donut::before,&.donut::before{content:"";position:absolute;inset:var(--gap-sm);border-radius:50%;background:conic-gradient(var(--a1) calc(var(--v)*1%),var(--n-2) 0);}
& .donut::after,&.donut::after{content:"";position:absolute;inset:24%;background:var(--page);border-radius:50%;}
& .fig,& .name{position:relative;z-index:1;text-align:center;}& .name{font-size:var(--type-20);max-width:65%;}& .fig{font-size:var(--type-52);}
@container (max-width:650px){& .fig{font-size:var(--type-32);}& .name{font-size:var(--type-14);}} @container (max-height:260px){& .fig{font-size:var(--type-28);}& .name{font-size:var(--type-12);}}
''')
rule('gauge','''&{display:grid;grid-template-columns:1fr auto;align-content:center;gap:var(--gap-sm) var(--gap);padding-bottom:var(--gap-lg);}
& .fig{font-size:var(--type-28);}& .name{font-size:var(--type-22);}&::before,&::after{content:"";position:absolute;left:0;bottom:0;height:12px;border-radius:999px;}&::before{right:0;background:var(--n-2);}&::after{width:calc(var(--v)*1%);background:var(--a1);}
@container (max-height:130px){& .fig{font-size:var(--type-24);}& .name{font-size:var(--type-18);}}
''')
rule('table','''&{display:flex;align-items:center;}
& table{width:100%;border-collapse:separate;border-spacing:0;font-size:var(--type-18);line-height:var(--body-line);}
& th,& td{padding:calc(var(--pad)/2) var(--pad);border-bottom:var(--stroke) solid var(--n-3);text-align:left;}
& thead th{font-weight:var(--label-weight);background:var(--n-1);color:var(--a1);border-top:var(--stroke) solid var(--a1);}& thead th:first-child{border-radius:var(--radius-sm) 0 0 0;}& thead th:last-child{border-radius:0 var(--radius-sm) 0 0;}
& .pick{background:var(--a1-1-soft);color:var(--a1);font-weight:var(--name-weight);}& .num{text-align:right;font-variant-numeric:tabular-nums;}
@container (max-width:700px){& table{font-size:var(--type-14);}& td,& th{padding:var(--gap-sm);}} @container (max-height:300px){& table{font-size:var(--type-14);}& td,& th{padding:var(--gap-sm);}}
''')
rule('steps','''&{display:flex;gap:var(--gap);align-items:center;}
& .step{position:relative;flex:1;text-align:center;display:flex;flex-direction:column;align-items:center;gap:var(--gap);padding:var(--pad) var(--gap-sm);}
& .mark{display:flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;border:var(--stroke) solid var(--a1);color:var(--a1);font-size:var(--type-24);font-weight:var(--label-weight);}
& .step:not(:last-child)::after{content:"";position:absolute;left:calc(50% + 36px);right:calc(-50% - var(--gap) + 36px);top:calc(var(--pad) + 28px);height:1px;background:var(--a1);}
& .name{color:var(--a1);}&.col{flex-direction:column;align-items:stretch;}&.col .step{display:grid;grid-template-columns:56px 1fr;text-align:left;column-gap:var(--gap);row-gap:var(--gap-sm);padding:var(--gap-sm);}&.col .mark{grid-row:1/3;}&.col .step::after{left:36px;right:auto;width:1px;top:calc(100% - var(--gap-sm));height:var(--gap);}
@container (max-width:650px){& .name{font-size:var(--type-18);}& .note{font-size:var(--type-14);}& .step{gap:var(--gap-sm);}& .mark{width:40px;height:40px;font-size:var(--type-18);}& .step:not(:last-child)::after{top:calc(var(--pad) + 20px);}}
''')
rule('timeline','''&{display:flex;align-items:center;gap:var(--gap);}
&::before{content:"";position:absolute;left:0;right:0;top:50%;border-top:var(--stroke) solid var(--a1);}
& .stop{position:relative;flex:1;padding-top:var(--gap-lg);display:grid;gap:var(--gap-sm);align-self:center;background:var(--page);border-top:var(--stroke) solid var(--a1);}
& .stop::before{content:"";position:absolute;left:0;top:-5px;width:10px;height:10px;border-radius:50%;background:var(--a1);}
& .stop.on .name{color:var(--a1);}& .kick{display:inline-flex;justify-content:center;align-items:center;width:max-content;padding:calc(var(--gap-sm)/2) calc(var(--pad)/2);background:var(--a1);color:var(--a1-on);border-radius:999px;}
&.alt .stop:nth-child(even){transform:translateY(-45%);}&.alt .stop:nth-child(odd){transform:translateY(45%);}
&.col{flex-direction:column;align-items:stretch;}&.col::before{top:0;bottom:0;left:4px;right:auto;border-left:var(--stroke) solid var(--a1);border-top:0;}&.col .stop{width:100%;padding:var(--gap-sm) var(--pad);border:0;}&.col .stop::before{left:0;top:var(--gap);}
@container (max-width:700px){& .name{font-size:var(--type-18);}& .note{font-size:var(--type-14);}} @container (max-height:250px){&.alt .stop{transform:none;}& .name{font-size:var(--type-18);}}
''')
# Radial families use circular nodes and one continuous orbital rule.
for k,member in [('cycle','node'),('hub','spoke')]:
 rule(k,f'''&{{display:block;}}
&::before{{content:"";position:absolute;left:20%;right:20%;top:18%;bottom:18%;border:var(--stroke) solid var(--a1);border-radius:50%;}}
& .core{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:24%;aspect-ratio:1;border-radius:50%;background:var(--a1);color:var(--a1-on);display:flex;align-items:center;justify-content:center;text-align:center;font-size:var(--type-24);font-weight:var(--name-weight);padding:var(--gap-sm);}}
& .{member}{{position:absolute;left:calc(50% + 36% * cos(var(--inflexion-angle)));top:calc(50% + 35% * sin(var(--inflexion-angle)));transform:translate(-50%,-50%);width:28%;padding:var(--gap-sm);background:var(--page);text-align:center;display:flex;flex-direction:column;gap:var(--gap-sm);align-items:center;}}
& .{member} .name{{font-size:var(--type-20);color:var(--a1);}}& .{member} .note{{font-size:var(--type-14);}}& .mark{{width:44px;height:44px;display:flex;align-items:center;justify-content:center;border:var(--stroke) solid var(--a1);border-radius:50%;color:var(--a1);}}& .mark .icon{{width:24px;height:24px;}}
@container (max-width:650px){{& .core{{font-size:var(--type-18);}}& .{member} .name{{font-size:var(--type-16);}}& .{member} .note{{font-size:var(--type-12);}}}}
''')
rule('funnel','''&{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);}
& .stage{width:calc(20% + var(--v)*.8%);flex:1;display:flex;align-items:center;justify-content:space-between;gap:var(--gap);padding:var(--gap-sm) var(--pad);background:var(--n-1);border:var(--stroke) solid var(--a1);border-radius:var(--radius-sm);}
& .stage:first-child{background:var(--a1);color:var(--a1-on);}& .stage:first-child .name,& .stage:first-child .fig{color:var(--a1-on);}& .fig{font-size:var(--type-32);}& .name{font-size:var(--type-22);}
@container (max-width:600px){& .name{font-size:var(--type-16);}& .fig{font-size:var(--type-24);}}
''')
rule('pyramid','''&{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);}
& .level{flex:1;width:calc(24% + var(--inflexion-index)*17%);background:var(--n-1);border-bottom:var(--stroke) solid var(--a1);padding:var(--gap-sm) var(--pad);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border-radius:var(--radius-sm) var(--radius-sm) 0 0;gap:var(--gap-sm);}
& .level:first-child{background:var(--a1);color:var(--a1-on);}& .level:first-child .name,& .level:first-child .note{color:var(--a1-on);}
@container (max-width:650px){& .name{font-size:var(--type-18);}& .note{font-size:var(--type-14);}}
''')
rule('matrix','''&{display:grid;grid-template-columns:var(--gap-lg) 1fr 1fr;grid-template-rows:1fr 1fr var(--gap-lg);gap:var(--gap-sm);}
& .cell{padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);background:var(--n-1);display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);}
& .cell:nth-of-type(3){grid-column:2;grid-row:1;}& .cell:nth-of-type(4){grid-column:3;grid-row:1;}& .cell:nth-of-type(5){grid-column:2;grid-row:2;}& .cell:nth-of-type(6){grid-column:3;grid-row:2;}
& .cell.on{background:var(--a1);color:var(--a1-on);border-color:var(--a1);}& .cell.on .name,& .cell.on .note,& .cell.on .kick{color:var(--a1-on);}
& .axis-x{grid-row:3;grid-column:2/4;display:flex;justify-content:space-between;font-size:var(--type-14);color:var(--a1);}& .axis-y{grid-column:1;grid-row:1/3;display:flex;flex-direction:column;justify-content:space-between;font-size:var(--type-14);color:var(--a1);}
&.swot{grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;}&.swot .cell{grid-area:auto;}& .cell>.list{flex:1;}
@container (max-width:650px){& .cell{padding:var(--gap-sm);}& .cell .name{font-size:var(--type-18);}& .cell .note{font-size:var(--type-14);}}
''')
rule('venn','''&{display:flex;align-items:center;justify-content:center;}
& .set{width:40%;aspect-ratio:1;border-radius:50%;border:var(--stroke) solid var(--a1);background:color-mix(in srgb,var(--a1) 8%,var(--page));display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--pad);margin-left:calc(var(--pad)*-1);}
& .set:first-child{margin-left:0;}& .set.on{border-width:2px;background:color-mix(in srgb,var(--a1) 16%,var(--page));}& .set .name{color:var(--a1);font-size:var(--type-24);}& .core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:var(--a1);color:var(--a1-on);padding:var(--gap-sm) var(--pad);border-radius:999px;font-size:var(--type-18);font-weight:var(--label-weight);}
@container (max-width:650px){& .set .name{font-size:var(--type-18);}& .core{font-size:var(--type-14);}}
''')
rule('hierarchy','''&{display:flex;justify-content:center;align-items:stretch;gap:var(--gap);padding-top:calc(var(--pad)*5);}
& .root{position:absolute;left:35%;right:35%;top:var(--gap);padding:var(--gap-sm) var(--pad);border-radius:999px;background:var(--a1);color:var(--a1-on);text-align:center;font-size:var(--type-24);font-weight:var(--name-weight);}
& .root::after{content:"";position:absolute;left:50%;top:100%;height:var(--gap-lg);border-left:var(--stroke) solid var(--a1);}
& .branch{position:relative;flex:1;display:flex;flex-direction:column;gap:var(--gap-sm);border-top:var(--stroke) solid var(--a1);padding-top:var(--gap-lg);}
& .branch::before{content:"";position:absolute;top:0;left:50%;height:var(--gap-lg);border-left:var(--stroke) solid var(--a1);}
& .node{background:var(--n-1);border:var(--stroke) solid var(--a1);border-radius:var(--radius-sm);padding:var(--gap-sm);text-align:center;font-size:var(--type-20);font-weight:var(--name-weight);color:var(--a1);}
& .leaf{padding:var(--gap-sm);text-align:center;border-bottom:var(--stroke) solid var(--n-3);font-size:var(--type-16);}
@container (max-width:650px){& .node{font-size:var(--type-16);}& .root{font-size:var(--type-20);}& .leaf{font-size:var(--type-14);}}
''')
rule('flowchart','''&{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(4,minmax(0,1fr));gap:var(--gap);}
& .node{position:relative;background:var(--n-1);border:var(--stroke) solid var(--a1);border-radius:var(--radius-sm);padding:var(--gap-sm);display:flex;align-items:center;justify-content:center;text-align:center;font-size:var(--type-20);font-weight:var(--name-weight);color:var(--a1);}
& .node.start,& .node.end{background:var(--a1);color:var(--a1-on);border-radius:999px;}& .node.ask{border:2px solid var(--a1);background:var(--a1-1-soft);}
& .node.to-r::after{content:"";position:absolute;left:100%;top:50%;width:var(--gap);height:8px;background:var(--a1);clip-path:polygon(0 40%,70% 40%,70% 0,100% 50%,70% 100%,70% 60%,0 60%);}
& .node.to-l::before{content:"";position:absolute;right:100%;top:50%;width:var(--gap);height:8px;background:var(--a1);clip-path:polygon(100% 40%,30% 40%,30% 0,0 50%,30% 100%,30% 60%,100% 60%);}
& .node.to-d::before{content:"";position:absolute;left:50%;top:100%;height:var(--gap);width:8px;background:var(--a1);clip-path:polygon(40% 0,40% 70%,0 70%,50% 100%,100% 70%,60% 70%,60% 0);}
& .node.to-u::before{content:"";position:absolute;left:50%;bottom:100%;height:var(--gap);width:8px;background:var(--a1);clip-path:polygon(40% 100%,40% 30%,0 30%,50% 0,100% 30%,60% 30%,60% 100%);}
@container (max-width:650px){& .node{font-size:var(--type-16);}}
''')
rule('architecture','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap);}
& .layer{position:relative;flex:1;display:flex;align-items:center;gap:var(--gap);padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--n-1);}
& .layer:first-child{border-color:var(--a1);}& .layer>.name{width:20%;flex:none;color:var(--a1);}& .chip{flex:1;border:var(--stroke) solid var(--a1);border-radius:999px;background:var(--page);padding:var(--gap-sm);text-align:center;font-size:var(--type-18);font-weight:var(--label-weight);line-height:var(--label-line);}
@container (max-width:650px){& .layer{padding:var(--gap-sm);gap:var(--gap-sm);}& .layer>.name{font-size:var(--type-16);}& .chip{font-size:var(--type-14);}}
''')
rule('versus','''&{display:grid;grid-template-columns:1fr auto 1fr;gap:var(--gap);align-items:stretch;}
& .side{padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);display:flex;flex-direction:column;justify-content:center;gap:var(--gap);background:var(--n-1);}
& .side>.name{color:var(--a1);font-size:var(--type-28);}& .side.on{border-color:var(--a1);background:var(--a1-1-soft);}& .vs{align-self:center;display:flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;background:var(--a1);color:var(--a1-on);font-size:var(--type-18);font-weight:var(--label-weight);}
@container (max-width:650px){& .side{padding:var(--gap-sm);}& .side>.name{font-size:var(--type-22);}& .vs{width:32px;height:32px;font-size:var(--type-14);}}
''')
rule('pricing','''&.plans{display:flex;gap:var(--gap);}& .plan,&.plan{position:relative;flex:1;padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);display:flex;flex-direction:column;justify-content:center;gap:var(--gap);background:linear-gradient(145deg,var(--page),var(--n-1));}
& .plan.on,&.plan.on{border-color:var(--a1);border-width:2px;}& .price{display:flex;align-items:baseline;gap:var(--gap-sm);padding-bottom:var(--gap);border-bottom:var(--stroke) solid var(--a1);}& .price .fig{font-size:var(--type-56);}& .plan>.name,&.plan>.name{color:var(--a1);font-size:var(--type-28);}
& .tag{align-self:flex-start;}& .list{flex:none;}
@container (max-width:650px){& .plan{padding:var(--gap-sm);gap:var(--gap-sm);}& .price .fig{font-size:var(--type-36);}& .plan>.name{font-size:var(--type-22);}& small{font-size:var(--type-14);}}
''')
rule('person','''&.people{display:flex;gap:var(--gap);align-items:stretch;}& .person,&.person{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:var(--gap);}
& .seat{width:72%;max-height:48%;aspect-ratio:1;border:2px solid var(--a1);border-radius:50%;flex:none;}& .seat.portrait{border-radius:var(--radius);aspect-ratio:3/4;}& .name{color:var(--a1);font-size:var(--type-24);}& .note{font-size:var(--type-16);}& .list{text-align:left;}
@container (max-width:650px){& .name{font-size:var(--type-18);}& .note{font-size:var(--type-14);}& .person{gap:var(--gap-sm);}}
''')
rule('logo-group','''&{display:flex;flex-wrap:wrap;align-content:center;align-items:center;justify-content:center;gap:var(--gap);}
& .seat.logo{flex:1;min-width:12%;max-width:22%;aspect-ratio:1;border-radius:var(--radius-sm);background:var(--n-1);border:var(--stroke) solid var(--n-3);}
@container (max-width:600px){& .seat.logo{max-width:25%;}}
''')
rule('image-frame','''&{display:flex;align-items:center;justify-content:center;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);padding:var(--gap-sm);background:var(--page);}
&>.seat{width:100%;height:100%;aspect-ratio:auto;border-radius:calc(var(--radius) - var(--gap-sm));}
@container (max-width:300px){&>.seat{font-size:var(--type-12);}}
''')
rule('agenda','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap-lg);}
& .entry{display:grid;grid-template-columns:44px 1fr;gap:var(--gap-sm) var(--gap);align-items:center;position:relative;padding-left:var(--gap-sm);}
& .mark{grid-column:1;grid-row:1/3;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--a1);color:var(--a1-on);font-size:var(--type-20);font-weight:var(--label-weight);line-height:var(--label-line);}
& .name,& .note{grid-column:2;}& .name{font-size:var(--type-24);}& .note{font-size:var(--type-20);color:var(--a1);}& .entry.on .name{color:var(--a1);}
@container (max-height:380px){&{gap:var(--gap);}& .name{font-size:var(--type-20);}& .note{font-size:var(--type-16);}} @container (max-height:240px){&{gap:var(--gap-sm);}& .name{font-size:var(--type-16);}& .note{font-size:var(--type-14);}& .mark{width:32px;height:32px;font-size:var(--type-16);}}
''')
rule('chart-stack','''&{display:flex;align-items:stretch;gap:var(--gap);padding-bottom:var(--gap-lg);border-bottom:var(--stroke) solid var(--n-4);}
& .sbar{flex:1;position:relative;display:flex;flex-direction:column-reverse;justify-content:flex-start;gap:0;padding-top:var(--gap-lg);}
& .sbar>span{position:absolute;top:100%;left:0;right:0;text-align:center;padding-top:var(--gap-sm);font-size:var(--type-14);line-height:var(--label-line);}
& .seg{height:calc((100% - var(--gap-lg))*var(--v)/var(--max));position:relative;display:flex;align-items:center;justify-content:center;background:var(--a1);color:var(--a1-on);font-size:var(--type-16);font-weight:var(--figure-weight);line-height:var(--figure-line);}
&.pct .seg{height:calc((100% - var(--gap-lg))*var(--v)/100);}& .seg.tone-2{background:var(--a2);color:var(--a2-on);}& .seg.tone-3{background:var(--a3);color:var(--a3-on);}& .seg.tone-4{background:var(--a4);color:var(--a4-on);}
&.h{flex-direction:column;padding-bottom:0;border:0;}&.h .sbar{flex-direction:row;padding:0 0 0 20%;}&.h .sbar>span{top:0;bottom:0;left:0;width:18%;display:flex;align-items:center;justify-content:flex-start;padding:0;}&.h .seg{height:100%;width:calc(var(--v)/var(--max)*100%);}&.h.pct .seg{width:calc(var(--v)*1%);}
@container (max-width:600px){&{gap:var(--gap-sm);}& .seg{font-size:var(--type-12);}& .sbar>span{font-size:var(--type-12);}}
''')
rule('chart-waterfall','''&{display:flex;gap:var(--gap);border-bottom:var(--stroke) solid var(--n-4);padding-bottom:var(--gap-lg);}
& .move{flex:1;position:relative;}
& .move::before{content:"";position:absolute;left:12%;right:12%;bottom:calc(min(var(--from),var(--to))/var(--max)*(100% - var(--gap-lg)));height:calc(abs(var(--to) - var(--from))/var(--max)*(100% - var(--gap-lg)));background:var(--n-3);border-radius:var(--radius-sm) var(--radius-sm) 0 0;}
& .move.up::before{background:var(--a1-4-soft);}& .move.down::before{background:var(--n-4);}& .move.total::before{bottom:0;height:calc(var(--to)/var(--max)*(100% - var(--gap-lg)));background:var(--a1);}
& .move:not(:last-child)::after{content:"";position:absolute;left:88%;width:calc(24% + var(--gap));bottom:calc(var(--to)/var(--max)*(100% - var(--gap-lg)));border-top:var(--stroke) dotted var(--a1);}
& b{position:absolute;left:0;right:0;bottom:calc(max(var(--from),var(--to))/var(--max)*(100% - var(--gap-lg)) + var(--gap-sm));text-align:center;font-size:var(--type-18);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--a1);}
& .move>span{position:absolute;top:100%;left:0;right:0;text-align:center;padding-top:var(--gap-sm);font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);}
@container (max-width:600px){&{gap:var(--gap-sm);}& b{font-size:var(--type-14);}& .move>span{font-size:var(--type-12);}}
''')
rule('chart-scatter','''&{border-left:var(--stroke) solid var(--n-4);border-bottom:var(--stroke) solid var(--n-4);background:repeating-linear-gradient(to top,var(--n-2) 0 1px,var(--page) 1px 25%);margin:var(--gap);}
& .axis-x{position:absolute;left:0;right:0;top:calc(100% + var(--gap-sm));text-align:center;font-size:var(--type-14);color:var(--a1);}& .axis-y{position:absolute;left:var(--gap-sm);top:0;font-size:var(--type-14);color:var(--a1);}
& .dot{position:absolute;left:calc(10% + var(--x)/var(--xmax)*80%);bottom:calc(10% + var(--y)/var(--ymax)*80%);width:12px;height:12px;border-radius:50%;background:var(--n-4);transform:translate(-50%,50%);}
& .dot.on{background:var(--a1);}& .dot.tone-2{background:var(--a2);}& .dot.tone-3{background:var(--a3);}&.bubble .dot{width:calc(12px + var(--r)*.7px);height:calc(12px + var(--r)*.7px);background:color-mix(in srgb,var(--a1) 45%,var(--page));border:var(--stroke) solid var(--a1);}
& .dot span{position:absolute;left:50%;bottom:calc(100% + var(--gap-sm));transform:translateX(-50%);font-size:var(--type-14);line-height:var(--label-line);white-space:nowrap;color:var(--n-7);}
@container (max-width:600px){& .dot span{font-size:var(--type-12);}}
''')
rule('sparkline','''&{display:flex;align-items:stretch;gap:calc(var(--gap-sm)/2);color:var(--a1);min-height:var(--gap-lg);}
&>span{flex:1;position:relative;border-bottom:var(--stroke) solid var(--n-3);}
&>span::before{content:"";position:absolute;left:0;right:0;bottom:0;height:calc(var(--v)/var(--max)*100%);background:var(--a1);border-radius:calc(var(--radius-sm)/4) calc(var(--radius-sm)/4) 0 0;}
&.up>span::before{background:var(--good);}&.down>span::before{background:var(--bad);}
&:not(.bars)>span::before{background:color-mix(in srgb,var(--a1) 20%,var(--page));border-top:2px solid var(--a1);}
@container (max-height:100px){&>span::before{border-radius:0;}}
''')
rule('heatmap','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);}
& .heads,& .row{display:grid;grid-template-columns:20% repeat(var(--cols),minmax(0,1fr));gap:var(--gap-sm);align-items:center;}
& .heads>span:first-child{grid-column:2;}& .heads span{font-size:var(--type-14);text-align:center;line-height:var(--label-line);color:var(--n-7);}
& .row .name{font-size:var(--type-18);}& .cell{padding:var(--gap-sm);min-height:var(--gap-lg);display:flex;align-items:center;justify-content:center;background:color-mix(in srgb,var(--a1) calc(var(--v)*.7%),var(--page));border-radius:calc(var(--radius-sm)/2);font-size:var(--type-16);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--ink);}
&.calendar .heads,&.calendar .row{grid-template-columns:repeat(var(--cols),minmax(0,1fr));}&.calendar .heads>span:first-child{grid-column:auto;}&.calendar .cell{aspect-ratio:1;}
@container (max-width:600px){& .heads span{font-size:var(--type-12);}& .row .name{font-size:var(--type-14);}& .cell{font-size:var(--type-12);padding:calc(var(--gap-sm)/2);}}
''')
rule('waffle','''&{display:flex;flex-direction:column;justify-content:center;align-items:center;gap:var(--gap);}
& .units{width:75%;max-height:65%;display:grid;grid-template-columns:repeat(10,minmax(0,1fr));gap:var(--gap-sm);}
& .u{aspect-ratio:1;background:var(--n-2);border-radius:calc(var(--radius-sm)/4);}& .u.on{background:var(--a1);}& .u.tone-2{background:var(--a2);}& .u.tone-3{background:var(--a3);}& .name{text-align:center;}& .fig{font-size:var(--type-48);}
&.figures .u{border-radius:50% 50% 20% 20%;clip-path:polygon(30% 0,70% 0,80% 20%,65% 35%,90% 40%,100% 75%,75% 75%,70% 100%,30% 100%,25% 75%,0 75%,10% 40%,35% 35%,20% 20%);}
@container (max-width:450px){& .units{gap:calc(var(--gap-sm)/2);}& .fig{font-size:var(--type-32);}& .name{font-size:var(--type-18);}}
''')
rule('treemap','''&{display:flex;gap:var(--gap-sm);}
& .branch{flex:var(--v);display:flex;flex-wrap:wrap;align-content:stretch;gap:var(--gap-sm);position:relative;padding-top:var(--gap-lg);}
& .branch>.name{position:absolute;left:0;right:0;top:0;font-size:var(--type-16);color:var(--a1);}
& .tile{flex:var(--v);min-width:25%;background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);padding:var(--gap-sm);display:flex;flex-direction:column;justify-content:center;align-items:center;gap:var(--gap-sm);}
& .tile.on{background:var(--a1);border-color:var(--a1);}& .tile.on .name,& .tile.on .fig{color:var(--a1-on);}& .tile .name{font-size:var(--type-20);}& .tile .fig{font-size:var(--type-36);}
@container (max-width:650px){& .tile .name{font-size:var(--type-14);}& .tile .fig{font-size:var(--type-24);}}
''')
rule('sankey','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap);padding-left:38%;}
& .source{position:absolute;left:0;top:30%;bottom:30%;width:27%;background:var(--a1);border-radius:var(--radius);display:flex;flex-direction:column;justify-content:center;align-items:center;padding:var(--pad);}
& .source .name,& .source .fig{color:var(--a1-on);}& .source .fig{font-size:var(--type-44);}& .source .name{font-size:var(--type-24);}
& .branch{position:relative;flex:var(--v);min-height:var(--gap-lg);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);background:var(--n-1);display:flex;align-items:center;justify-content:space-between;padding:var(--gap-sm) var(--pad);gap:var(--gap-sm);}
&>.branch::before{content:"";position:absolute;right:100%;width:18%;height:calc(6px + var(--v)*.7px);background:var(--a1-2-soft);border-top:var(--stroke) solid var(--a1);border-bottom:var(--stroke) solid var(--a1);transform-origin:right;transform:skewY(calc(var(--inflexion-index)*8deg - 12deg));}
& .branch.on{border-color:var(--a1);background:var(--a1-1-soft);}& .branch.out{background:var(--n-2);}& .branch .name{font-size:var(--type-20);}& .branch .fig{font-size:var(--type-28);}
@container (max-width:650px){& .source .name,& .branch .name{font-size:var(--type-16);}& .source .fig,& .branch .fig{font-size:var(--type-24);}& .branch{padding:var(--gap-sm);}}
''')
rule('radar','''&{position:relative;}
&::before{content:"";position:absolute;inset:12% 20%;border:var(--stroke) solid var(--n-3);border-radius:50%;background:repeating-radial-gradient(circle,var(--page) 0 18%,var(--n-2) 18% 18.5%,var(--page) 18.5% 20%);}
& .axis{position:absolute;left:calc(50% + 43%*sin(var(--inflexion-angle)));top:calc(50% - 43%*cos(var(--inflexion-angle)));transform:translate(-50%,-50%);width:25%;text-align:center;}
& .axis .name{font-size:var(--type-16);color:var(--a1);}
& .series{position:absolute;left:22%;right:22%;top:12%;bottom:12%;background:color-mix(in srgb,var(--a1) 22%,transparent);border:var(--stroke) solid var(--a1);clip-path:polygon(50% calc(50% - var(--v1)/var(--max)*50%),calc(50% + var(--v2)/var(--max)*47.5%) calc(50% - var(--v2)/var(--max)*15.5%),calc(50% + var(--v3)/var(--max)*29.4%) calc(50% + var(--v3)/var(--max)*40.5%),calc(50% - var(--v4)/var(--max)*29.4%) calc(50% + var(--v4)/var(--max)*40.5%),calc(50% - var(--v5)/var(--max)*47.5%) calc(50% - var(--v5)/var(--max)*15.5%));}
& .series.tone-2{background:color-mix(in srgb,var(--a2) 20%,transparent);}& .series .name{position:absolute;bottom:0;font-size:var(--type-14);}
@container (max-width:600px){& .axis .name{font-size:var(--type-12);}}
''')
rule('bullet','''&.bullets{display:flex;flex-direction:column;justify-content:center;gap:var(--gap);}
& .bullet,&.bullet{position:relative;min-height:80px;padding-bottom:var(--gap-lg);display:grid;grid-template-columns:1fr auto;align-items:center;gap:var(--gap-sm);}
& .bullet::before,&.bullet::before{content:"";position:absolute;left:0;right:0;bottom:0;height:20px;border-radius:999px;background:linear-gradient(to right,var(--n-2) calc(var(--low,50)*1%),var(--n-3) 0 calc(var(--high,80)*1%),var(--n-4) 0);}
& .bullet::after,&.bullet::after{content:"";position:absolute;left:0;bottom:6px;width:calc(var(--v)*1%);height:8px;background:var(--a1);border-radius:999px;}
& .fig{font-size:var(--type-28);}& .name{font-size:var(--type-22);}& .note{grid-column:1/3;position:relative;}
& .note::after{content:"";position:absolute;left:calc(var(--target)*1%);bottom:calc(var(--gap-lg)*-1 + 4px);width:2px;height:26px;background:var(--ink);}
@container (max-width:550px){& .name{font-size:var(--type-18);}& .fig{font-size:var(--type-24);}}
''')
rule('slope','''&{padding:var(--pad) 20%;border-bottom:var(--stroke) solid var(--n-3);}
& .heads{position:absolute;left:10%;right:10%;top:0;display:flex;justify-content:space-between;color:var(--a1);font-size:var(--type-16);font-weight:var(--label-weight);}
& .pair{position:absolute;left:20%;right:20%;top:var(--gap-lg);bottom:var(--gap);--inflexion-ay:calc(100% - var(--a)/var(--max)*100%);--inflexion-by:calc(100% - var(--b)/var(--max)*100%);}
& .pair::before{content:"";position:absolute;inset:0;background:var(--n-4);clip-path:polygon(0 calc(var(--inflexion-ay) - 1px),100% calc(var(--inflexion-by) - 1px),100% calc(var(--inflexion-by) + 1px),0 calc(var(--inflexion-ay) + 1px));}
& .pair.on::before{background:var(--a1);}& .pair .name{position:absolute;right:calc(100% + var(--gap));top:var(--inflexion-ay);transform:translateY(-50%);font-size:var(--type-16);width:var(--type-128);text-align:right;}
& .pair b{position:absolute;font-size:var(--type-18);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--a1);background:var(--page);padding:calc(var(--gap-sm)/2);}
& .pair .a{left:0;top:var(--inflexion-ay);transform:translate(-50%,-50%);}& .pair .b{right:0;top:var(--inflexion-by);transform:translate(50%,-50%);}
&.dumbbell{display:flex;flex-direction:column;gap:var(--gap);padding:var(--gap-lg) 20% var(--gap);}&.dumbbell .pair{position:relative;flex:1;inset:auto;}&.dumbbell .pair::before{top:50%;bottom:auto;height:2px;left:calc(var(--a)/var(--max)*100%);right:calc(100% - var(--b)/var(--max)*100%);clip-path:none;}&.dumbbell .pair .name{top:50%;}&.dumbbell .pair .a{left:calc(var(--a)/var(--max)*100%);top:50%;}&.dumbbell .pair .b{left:calc(var(--b)/var(--max)*100%);right:auto;top:50%;transform:translate(-50%,-50%);}
@container (max-width:650px){& .pair .name{font-size:var(--type-14);width:var(--type-80);}& .pair b{font-size:var(--type-14);}}
''')
rule('roadmap','''&{display:flex;flex-direction:column;gap:var(--gap-sm);padding-top:var(--gap-lg);}
& .heads{position:absolute;left:20%;right:0;top:0;display:flex;justify-content:space-around;color:var(--a1);font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);}
& .lane{position:relative;flex:1;background:repeating-linear-gradient(to right,var(--page) 0 calc(100%/var(--cols) - 1px),var(--n-3) 0 calc(100%/var(--cols)));margin-left:20%;border-bottom:var(--stroke) solid var(--n-2);}
& .lane>.name{position:absolute;right:calc(100% + var(--gap));top:50%;transform:translateY(-50%);width:20%;font-size:var(--type-18);text-align:right;}
& .bar{position:absolute;left:calc(var(--from)/var(--cols)*100%);width:calc((var(--to) - var(--from))/var(--cols)*100%);top:25%;height:50%;display:flex;align-items:center;justify-content:center;border-radius:999px;background:var(--n-3);color:var(--ink);padding:0 var(--gap-sm);font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);}
& .bar.on{background:var(--a1);color:var(--a1-on);}& .bar.tone-2{background:var(--a2);color:var(--a2-on);}& .bar.tone-3{background:var(--a3);color:var(--a3-on);}
& .mile{position:absolute;left:calc(var(--at)/var(--cols)*100%);top:0;bottom:0;border-left:2px dotted var(--a1);}& .mile span{position:absolute;left:var(--gap-sm);top:0;white-space:nowrap;color:var(--a1);font-size:var(--type-12);}
@container (max-width:650px){& .lane>.name,& .bar{font-size:var(--type-14);}& .heads{font-size:var(--type-12);}}
''')
rule('swimlane','''&{display:grid;grid-template-columns:var(--type-128) repeat(var(--cols),minmax(0,1fr));grid-auto-rows:minmax(0,1fr);gap:var(--gap);}
& .lane{grid-column:1/-1;background:var(--n-1);border-bottom:var(--stroke) solid var(--n-3);display:flex;align-items:center;padding:var(--gap-sm);}& .lane>.name{width:var(--type-100);font-size:var(--type-18);color:var(--a1);}
& .node{position:relative;z-index:1;align-self:center;min-height:var(--type-64);padding:var(--gap-sm);border:var(--stroke) solid var(--a1);border-radius:var(--radius-sm);background:var(--page);display:flex;align-items:center;justify-content:center;text-align:center;font-size:var(--type-18);font-weight:var(--name-weight);color:var(--a1);}
& .node.start,& .node.end{background:var(--a1);color:var(--a1-on);border-radius:999px;}& .node.ask{border-width:2px;}
& .node.to-r::after{content:"";position:absolute;left:100%;top:50%;width:var(--gap);border-top:var(--stroke) solid var(--a1);}& .node.to-l::after{content:"";position:absolute;right:100%;top:50%;width:var(--gap);border-top:var(--stroke) solid var(--a1);}
& .node.to-d::before{content:"";position:absolute;left:50%;top:100%;height:var(--gap-lg);border-left:var(--stroke) solid var(--a1);}& .node.to-u::before{content:"";position:absolute;left:50%;bottom:100%;height:var(--gap-lg);border-left:var(--stroke) solid var(--a1);}
@container (max-width:650px){& .node{font-size:var(--type-14);}& .lane>.name{font-size:var(--type-14);}}
''')
rule('concentric','''&{display:flex;align-items:center;justify-content:center;}
& .ring{position:absolute;border-radius:50%;border:var(--stroke) solid var(--a1);background:var(--a1-1-soft);display:flex;flex-direction:column;align-items:center;padding-top:var(--gap);gap:var(--gap-sm);text-align:center;}
& .ring:nth-child(1){width:90%;height:90%;top:5%;left:5%;}& .ring:nth-child(2){width:66%;height:66%;top:29%;left:17%;background:var(--a1-2-soft);}& .ring:nth-child(3){width:42%;height:42%;top:53%;left:29%;background:var(--a1);color:var(--a1-on);}& .ring:nth-child(4){width:25%;height:25%;top:70%;left:37.5%;background:var(--a1);}
& .ring .name{font-size:var(--type-24);}& .ring .fig{font-size:var(--type-32);}& .ring.on .name,& .ring.on .fig,& .ring.on .note{color:var(--a1-on);}& .ring.on{background:var(--a1);}
@container (max-width:650px){& .ring{gap:calc(var(--gap-sm)/2);padding-top:var(--gap-sm);}& .ring .name{font-size:var(--type-18);}& .ring .fig{font-size:var(--type-24);}& .ring .note{font-size:var(--type-12);}}
''')
rule('journey','''&{display:flex;gap:var(--gap);align-items:stretch;padding-top:25%;}
& .stage{position:relative;flex:1;background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);padding:var(--pad);display:flex;flex-direction:column;gap:var(--gap-sm);justify-content:center;}
& .stage::before{content:"";position:absolute;left:50%;top:calc(-100cqh*.25 + (100 - var(--mood))*.15cqh);width:10px;height:10px;border-radius:50%;background:var(--a1);}
& .stage:not(:last-child)::after{content:"";position:absolute;left:50%;top:calc(-100cqh*.25 + (100 - var(--mood))*.15cqh + 5px);width:calc(100% + var(--gap));height:2px;background:var(--a1);transform-origin:left;rotate:atan2(calc((var(--mood) - var(--next))* .15cqh),calc(100% + var(--gap)));}
& .stage.on{border-color:var(--a1);}& .name{color:var(--a1);}& .pain{font-size:var(--type-14);line-height:var(--body-line);color:var(--n-7);border-top:var(--stroke) dotted var(--a1);padding-top:var(--gap-sm);}
@container (max-width:700px){& .stage{padding:var(--gap-sm);}& .name{font-size:var(--type-18);}& .note,& .pain{font-size:var(--type-12);}}
''')
rule('mindmap','''&{display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:repeat(3,minmax(0,1fr));gap:var(--gap);}
& .core{grid-column:2;grid-row:2;align-self:center;background:var(--a1);color:var(--a1-on);border-radius:999px;text-align:center;padding:var(--pad);z-index:2;}& .core .name{color:var(--a1-on);}
& .branch{position:relative;background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);padding:var(--gap-sm) var(--pad);display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);}
& .branch.on{border-color:var(--a1);background:var(--a1-1-soft);}& .branch .name{font-size:var(--type-20);color:var(--a1);}& .leaf{font-size:var(--type-14);border-top:var(--stroke) solid var(--n-3);padding-top:calc(var(--gap-sm)/2);}
& .branch::after{content:"";position:absolute;left:100%;width:var(--gap);top:50%;border-top:var(--stroke) solid var(--a1);border-radius:50%;}& .branch:nth-child(even)::after{left:auto;right:100%;}
@container (max-width:650px){& .branch{padding:var(--gap-sm);}& .branch .name{font-size:var(--type-16);}& .leaf{font-size:var(--type-12);}& .core{padding:var(--gap-sm);}& .core .name{font-size:var(--type-18);}}
''')
rule('decision-tree','''&{display:flex;flex-direction:column;justify-content:center;gap:var(--gap-lg);}
& .q{align-self:center;display:flex;align-items:center;justify-content:center;background:var(--a1);padding:var(--gap-sm) var(--pad);color:var(--a1-on);border-radius:999px;position:relative;}
& .q .name{color:var(--a1-on);font-size:var(--type-22);}& .opts{display:flex;gap:var(--gap);align-items:stretch;}
& .opt{position:relative;flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:var(--gap);padding-top:var(--gap);border-top:var(--stroke) solid var(--a1);}
& .opt::before{content:"";position:absolute;left:50%;top:0;height:var(--gap);border-left:var(--stroke) solid var(--a1);}
& .cond{align-self:center;color:var(--a1);font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);}
& .end{padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);text-align:center;background:var(--n-1);}& .end .name{font-size:var(--type-20);}& .end.on{background:var(--a1-1-soft);border-color:var(--a1);}
@container (max-width:700px){& .q .name,& .end .name{font-size:var(--type-16);}& .end{padding:var(--gap-sm);}& .opt{gap:var(--gap-sm);}}
''')
rule('balance','''&{display:grid;grid-template-columns:1fr 1fr;gap:var(--gap-lg);align-items:center;padding-bottom:var(--type-100);}
&::before{content:"";position:absolute;left:10%;right:10%;top:50%;height:2px;background:var(--a1);rotate:calc(var(--tilt)*.08deg);}
& .pan{position:relative;z-index:1;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);padding:var(--pad);background:var(--page);display:flex;flex-direction:column;gap:var(--gap-sm);text-align:center;}
& .pan.on{border-color:var(--a1);background:var(--a1-1-soft);}& .pan>.name{color:var(--a1);}& .item{padding:var(--gap-sm);background:var(--n-1);border-radius:999px;}& .item .name{font-size:var(--type-18);}
& .fulcrum{position:absolute;left:40%;right:40%;bottom:0;text-align:center;padding-top:var(--type-64);font-size:var(--type-16);color:var(--a1);}& .fulcrum::before{content:"";position:absolute;left:25%;right:25%;top:0;height:var(--type-64);background:var(--a1);clip-path:polygon(50% 0,100% 100%,0 100%);}
@container (max-width:650px){& .pan{padding:var(--gap-sm);}& .pan>.name{font-size:var(--type-18);}& .item .name{font-size:var(--type-14);}}
''')
rule('matrix-nine','''&{display:grid;grid-template-columns:var(--gap-lg) repeat(3,minmax(0,1fr));grid-template-rows:repeat(3,minmax(0,1fr)) var(--gap-lg);gap:var(--gap-sm);}
& .axis-x{grid-column:2/5;grid-row:4;display:flex;justify-content:space-between;color:var(--a1);font-size:var(--type-14);}& .axis-y{grid-column:1;grid-row:1/4;display:flex;flex-direction:column;justify-content:space-between;color:var(--a1);font-size:var(--type-14);}
& .cell{background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);padding:var(--pad);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:var(--gap-sm);}
& .cell.on{background:var(--a1);border-color:var(--a1);}& .cell.on .name,& .cell.on .note{color:var(--a1-on);}& .cell.tone-2{background:var(--a2-1-soft);}& .cell.tone-3{background:var(--a3-1-soft);}
@container (max-width:650px){& .cell{padding:var(--gap-sm);}& .cell .name{font-size:var(--type-16);}& .cell .note{font-size:var(--type-12);}}
''')
rule('positioning','''&{border:var(--stroke) solid var(--a1);border-radius:var(--radius);padding:var(--pad);}
&::before{content:"";position:absolute;left:18%;right:18%;top:50%;border-top:2px dotted var(--a1);}&::after{content:"";position:absolute;top:12%;bottom:12%;left:50%;border-left:2px dotted var(--a1);}
& .axis-x{position:absolute;left:var(--gap);right:var(--gap);top:50%;display:flex;justify-content:space-between;transform:translateY(-50%);font-size:var(--type-14);color:var(--a1);font-weight:var(--label-weight);}
& .axis-y{position:absolute;top:var(--gap);bottom:var(--gap);left:50%;transform:translateX(-50%);display:flex;flex-direction:column;justify-content:space-between;text-align:center;font-size:var(--type-14);color:var(--a1);font-weight:var(--label-weight);}
& .mark{position:absolute;left:calc(20% + var(--x)*.6%);bottom:calc(18% + var(--y)*.64%);width:64px;height:64px;border-radius:50%;background:var(--n-2);transform:translate(-50%,50%);display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--gap-sm);z-index:2;}
& .mark.on{width:100px;height:100px;background:var(--a1);color:var(--a1-on);}& .mark .name{font-size:var(--type-14);}& .mark.on .name{color:var(--a1-on);font-size:var(--type-18);}& .mark .seat{width:100%;height:100%;}
@container (max-width:650px){& .mark{width:44px;height:44px;}& .mark.on{width:72px;height:72px;}& .mark .name{font-size:var(--type-12);}& .mark.on .name{font-size:var(--type-14);}& .axis-x,& .axis-y{font-size:var(--type-12);}}
''')
rule('network','''&{position:relative;}
& .link{position:absolute;left:calc(10% + var(--x1)*.8%);top:calc(12% + var(--y1)*.72%);width:hypot(calc((var(--x2) - var(--x1))*.8cqw),calc((var(--y2) - var(--y1))*.72cqh));height:0;border-top:var(--stroke) solid var(--n-3);transform-origin:left;rotate:atan2(calc((var(--y2) - var(--y1))*.72cqh),calc((var(--x2) - var(--x1))*.8cqw));}
& .link.strong{border-color:var(--a1);border-width:2px;}
& .node{position:absolute;left:calc(10% + var(--x)*.8%);top:calc(12% + var(--y)*.72%);transform:translate(-50%,-50%);display:flex;align-items:center;justify-content:center;min-width:64px;height:64px;border-radius:50%;border:var(--stroke) solid var(--a1);background:var(--page);z-index:1;padding:var(--gap-sm);}
& .node.on{background:var(--a1);}& .node.on .name{color:var(--a1-on);}& .node .name{font-size:var(--type-16);color:var(--a1);white-space:nowrap;}
@container (max-width:650px){& .node{min-width:44px;height:44px;}& .node .name{font-size:var(--type-12);}}
''')
rule('code','''&{display:flex;flex-direction:column;justify-content:center;padding:var(--pad);background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);}
&>.name{font-size:var(--type-16);color:var(--a1);border-bottom:var(--stroke) solid var(--n-3);padding-bottom:var(--gap-sm);margin-bottom:var(--gap);}
& .lines{counter-reset:code;font-family:var(--inflexion-font-code);font-variant-numeric:tabular-nums;font-size:var(--type-18);line-height:var(--body-line);letter-spacing:var(--label-track-latin);}
& .lines p{margin:0;white-space:pre;counter-increment:code;position:relative;}
&.numbered .lines p{padding-left:var(--gap-lg);}&.numbered .lines p::before{content:counter(code);position:absolute;left:0;width:var(--gap);text-align:right;color:var(--n-6);font-size:var(--type-14);}
& .k{color:var(--a1);font-weight:var(--name-weight);}& .s{color:var(--good);}& .c{color:var(--n-7);}& .n{color:var(--a2);}
@container (max-width:650px){& .lines{font-size:var(--type-14);}} @container (max-height:300px){& .lines{font-size:var(--type-12);}}
''')
# Topology indices are local implementation variables; all are namespaced.
for k in ['cycle','hub']:
 member='node' if k=='cycle' else 'spoke'
 for n in range(3,7):
  for i in range(n):CSS[k]+=f'&:has(>.{member}:nth-child({n+1}):last-child)>.{member}:nth-child({i+2}){{--inflexion-angle:{-90+i*360/n}deg;}}\n'
for k,member in [('pyramid','level'),('sankey','branch')]:
 for i in range(1,7):CSS[k]+=f'&>.{member}:nth-child({i}){{--inflexion-index:{i};}}\n'
for k in ['chart-line','chart-area']:
 for i in range(1,13):
  child=f'>.pt:nth-child({i})' if k=='chart-line' else f'>.series>.pt:nth-child({i} of .pt)'
  CSS[k]+=f'& {child}{{--inflexion-self:--inflexion-p{i};--inflexion-prev:--inflexion-p{max(1,i-1)};}}\n'
for n in range(3,9):
 for i in range(n):CSS['radar']+=f'&[style*="--n:{n}"]>.axis:nth-child({i+1}){{--inflexion-angle:{i*360/n}deg;}}\n'
for i in range(9):CSS['matrix-nine']+=f'& .cell:nth-child({i+3}){{grid-column:{2+i%3};grid-row:{1+i//3};}}\n'
for i in range(6):CSS['mindmap']+=f'&>.branch:nth-child({i+2}){{grid-column:{1 if i%2==0 else 3};grid-row:{1+i//2};}}\n'

CSS['card']+="""@container (min-height:350px){& .name{font-size:var(--type-24);}& .fig{font-size:var(--type-64);}& .note{font-size:var(--type-16);}& .parts{gap:var(--gap);}} @container (min-width:440px) and (min-height:350px){& .name{font-size:var(--type-28);}& .fig{font-size:var(--type-80);}& .note{font-size:var(--type-18);}}"""
CSS['chart-line']+="""& .pt b{position:relative;}"""
CSS['chart-area']+="""& .pt b{position:relative;left:auto;bottom:auto;display:block;width:max-content;transform:translate(-50%,calc(-100% - var(--gap-sm)));}& .series:nth-child(2){--inflexion-series:var(--a2);}& .series:nth-child(3){--inflexion-series:var(--a3);}& .series:nth-child(4){--inflexion-series:var(--a4);}"""
CSS['chart-donut']+="""&.donut{aspect-ratio:auto;padding:var(--gap-sm);}&.donut::before,& .donut::before{inset:auto;left:50%;top:50%;width:min(92cqw,92cqh);height:min(92cqw,92cqh);transform:translate(-50%,-50%);}&.donut::after,& .donut::after{inset:auto;left:50%;top:50%;width:min(50cqw,50cqh);height:min(50cqw,50cqh);transform:translate(-50%,-50%);}& .donut{aspect-ratio:auto;align-self:stretch;container-type:size;}& .name{max-width:42%;font-size:var(--type-18);}& .fig{font-size:var(--type-44);}@container (max-width:600px){&.donuts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:repeat(2,minmax(0,1fr));}& .donut{width:100%;height:100%;}& .fig{font-size:var(--type-28);}& .name{font-size:var(--type-12);}}"""


CSS['balance']+="""& .fulcrum{top:50%;bottom:auto;padding-top:var(--type-80);}& .fulcrum::before{height:var(--type-80);}& .pan:first-child{transform:translateY(calc(var(--tilt)*-.25px));}& .pan:nth-child(2){transform:translateY(calc(var(--tilt)*.25px));}"""
CSS['bullet']+="""& .bullet::after,&.bullet::after{width:min(100%,calc(var(--v)*1%));}&.bullet{align-content:center;}&.bullet .note::after{bottom:calc(var(--gap-lg)*-1 + 4px);}"""
CSS['hierarchy']+="""& .branch{padding-top:var(--type-100);}& .branch::before{height:var(--type-100);}@container (max-height:300px){& .branch{padding-top:var(--gap-lg);}& .branch::before{height:var(--gap-lg);}}"""
CSS['journey']+="""& .stage:not(:last-child)::after{width:hypot(calc(100cqw / var(--inflexion-count)),calc((var(--mood) - var(--next))*.15cqh));rotate:atan2(calc((var(--mood) - var(--next))*.15cqh),calc(100cqw / var(--inflexion-count)));}"""
for n in range(3,8): CSS['journey']+=f'&:has(>.stage:nth-child({n}):last-child){{--inflexion-count:{n};}}'
CSS['radar']+="""& .series{clip-path:none;background:none;border:0;}& .series::before{content:"";position:absolute;inset:0;background:color-mix(in srgb,var(--a1) 24%,transparent);}& .series.tone-2{background:none;}& .series.tone-2::before{background:color-mix(in srgb,var(--a2) 24%,transparent);}& .series>.name{top:calc(var(--gap)*-1);bottom:auto;left:0;white-space:nowrap;color:var(--a1);}& .series:nth-of-type(2)>.name{left:50%;color:var(--a2);}"""
import math
for n in range(3,9):
 poly=','.join(f'calc(50% + var(--v{i+1})/var(--max)*{math.sin(i*2*math.pi/n)*50:.5f}%) calc(50% - var(--v{i+1})/var(--max)*{math.cos(i*2*math.pi/n)*50:.5f}%)' for i in range(n))
 CSS['radar']+=f'&:is([style*="--n:{n}"],[style*="--n: {n}"]) .series::before{{clip-path:polygon({poly});}}'
CSS['treemap']+="""& .branch{flex-direction:column;flex-wrap:nowrap;}& .tile{min-width:0;width:100%;min-height:0;}"""


CSS['card']+="""& .mark .icon{font-size:var(--type-20);line-height:var(--body-line);display:flex;align-items:center;justify-content:center;}& .mark .seat{width:32px;height:32px;border-radius:50%;font-size:var(--type-12);}@container (max-height:170px){& .parts{gap:var(--gap-sm);}& .note{font-size:var(--type-12);}& .name{font-size:var(--type-18);}}"""
CSS['architecture']+="""@container (max-height:380px){& .layer{padding:var(--gap-sm);gap:var(--gap-sm);}& .layer>.name{font-size:var(--type-16);}& .chip{font-size:var(--type-14);}}"""
CSS['callout']+="""&{container-type:inline-size;flex:0 0 auto;}@container (max-height:200px){&{padding:var(--gap-sm);}& p{font-size:var(--type-18);}}"""
CSS['chart-line']+="""& .pt b{line-height:var(--body-line);}"""
CSS['chart-area']+="""& .pt b{line-height:var(--body-line);}"""
CSS['metric']+="""@container (max-height:140px){&.stats>.stat{padding:0 var(--gap-sm);}& .parts{gap:calc(var(--gap-sm)/2);}& .fig{font-size:var(--type-28);line-height:var(--body-line);}& .name{font-size:var(--type-14);}& .note{display:none;}}"""
CSS['tag']+="""&{container-type:normal;}&.tag{line-height:var(--body-line);}"""
CSS['pill']+="""&{container-type:inline-size;flex:0 0 auto;}"""
CSS['timeline']+="""&.col .stop{display:grid;grid-template-columns:80px 1fr;padding:var(--gap-sm);gap:calc(var(--gap-sm)/2) var(--gap);align-content:center;}&.col .kick{grid-column:1;grid-row:1/3;font-size:var(--type-12);align-self:start;}&.col .name,&.col .note{grid-column:2;}&.col .name{font-size:var(--type-18);}&.col .note{font-size:var(--type-14);}@container (max-height:400px){&.col{gap:var(--gap-sm);}&.col .stop{grid-template-columns:64px 1fr;padding:calc(var(--gap-sm)/2);}&.col .name{font-size:var(--type-16);}&.col .note{font-size:var(--type-12);}}"""
CSS['image-frame']+="""&{width:auto;height:auto;max-width:100%;max-height:100%;overflow:visible;}&>.seat{font-size:var(--type-12);}"""
CSS['pyramid']+="""& .level{width:min(100%,calc(18% + var(--inflexion-index)*16%));padding:var(--gap-sm);gap:calc(var(--gap-sm)/2);}@container (max-height:400px){& .level .name{font-size:var(--type-16);}& .level .note{font-size:var(--type-12);}}"""
CSS['heatmap']+="""&.calendar .cell{min-height:0;padding:0;}&.calendar{gap:calc(var(--gap-sm)/2);}&.calendar .row{gap:calc(var(--gap-sm)/2);}"""
CSS['prose']+="""@container (max-width:450px) and (max-height:230px){&{font-size:var(--type-14);gap:var(--gap-sm);}}"""
CSS['person']+="""@container (max-height:300px){&.person,& .person{gap:var(--gap-sm);}& .name{font-size:var(--type-18);}& .note{font-size:var(--type-14);}& .seat{max-height:40%;width:45%;}}"""
CSS['quote']+="""& .by>.name{white-space:normal;font-size:var(--type-18);}"""
CSS['steps']+="""&.col .step::after{top:100%;height:var(--gap);} &.col .step{row-gap:calc(var(--gap-sm)/2);flex:1;}"""


CSS['card']+="""& .parts>.name{min-height:calc(var(--type-24)*var(--name-line)*2);}& .parts>.note{min-height:calc(var(--type-16)*var(--body-line)*3);}&.on{border-radius:calc(var(--radius)*4) 0 0 0;}&.quiet:has(.mark.seat){border-color:var(--page);}&.quiet:has(.mark.seat) .parts{align-items:center;text-align:center;}&.quiet .mark.seat{width:140px;height:140px;border-radius:var(--radius-sm);}&.quiet:has(.mark.seat) .name{min-height:0;align-self:center;background:var(--a1);color:var(--a1-on);border-radius:999px;padding:calc(var(--gap-sm)/2) var(--pad);font-size:var(--type-18);display:flex;align-items:center;justify-content:center;}@container (max-height:300px){& .parts>.name{min-height:0;}& .parts>.note{min-height:0;}}"""
CSS['headline']+="""@container (min-height:400px){&.big h2{font-size:var(--type-56);}}"""
CSS['chart-bar']+="""@container (min-height:400px){&.h .bar b{font-size:var(--type-28);}}"""
CSS['matrix-nine']+="""&>.cell:nth-child(1 of .cell){grid-column:2;grid-row:1;}&>.cell:nth-child(2 of .cell){grid-column:3;grid-row:1;}&>.cell:nth-child(3 of .cell){grid-column:4;grid-row:1;}&>.cell:nth-child(4 of .cell){grid-column:2;grid-row:2;}&>.cell:nth-child(5 of .cell){grid-column:3;grid-row:2;}&>.cell:nth-child(6 of .cell){grid-column:4;grid-row:2;}&>.cell:nth-child(7 of .cell){grid-column:2;grid-row:3;}&>.cell:nth-child(8 of .cell){grid-column:3;grid-row:3;}&>.cell:nth-child(9 of .cell){grid-column:4;grid-row:3;}"""
CSS['person']+="""& .seat{width:min(72cqw,44cqh);height:min(72cqw,44cqh);max-height:none;flex:none;}& .seat.portrait{width:min(65cqw,33cqh);height:min(86cqw,44cqh);aspect-ratio:3/4;}"""
CSS['pricing']+="""& .plan,&.plan{justify-content:flex-start;}& .plan>.name,&.plan>.name{min-height:var(--type-40);}& .price{min-height:var(--type-80);}& .plan>.tag,&.plan>.tag{position:absolute;right:var(--pad);top:var(--gap-sm);}& .plan>.list,&.plan>.list{flex:1;justify-content:center;}"""
CSS['pill']+="""&.quiet{background:var(--ink);color:var(--page);border-color:var(--ink);}&.quiet .name,&.quiet .note{color:var(--page);}"""
CSS['radar']+="""& .series:nth-child(2 of .series)>.name{left:40%;color:var(--a2);}& .series:nth-child(3 of .series)>.name{left:75%;color:var(--a3);}& .series:nth-child(3 of .series)::before{background:color-mix(in srgb,var(--a3) 24%,transparent);}"""
# Topology-aware branch positioning and inward connectors.
for n in [2,4,6]:
 rows=([2,2] if n==2 else [1,1,3,3] if n==4 else [1,1,2,2,3,3])
 for i,row in enumerate(rows):
  left=i%2==0;sel=f'&:has(>.branch:nth-child({n} of .branch):last-child)>.branch:nth-child({i+1} of .branch)'
  CSS['mindmap']+=sel+f'{{grid-column:{1 if left else 3};grid-row:{row};}}'
  CSS['mindmap']+=sel+f'::after{{left:{"100%" if left else "auto"};right:{"auto" if left else "100%"};width:var(--gap);top:50%;height:1px;border:0;border-top:var(--stroke) solid var(--a1);}}'
  if row!=2:
   side='right' if left else 'left';vert='top' if row==1 else 'bottom'
   CSS['mindmap']+=sel+f'::after{{top:{"50%" if row==1 else "auto"};bottom:{"auto" if row==1 else "50%"};height:calc(100% + var(--gap));border-{side}:var(--stroke) solid var(--a1);border-{vert}:var(--stroke) solid var(--a1);border-radius:var(--radius-sm);}}'


CSS['code']+="""& .lines{font-family:var(--inflexion-font-code);}"""
CSS['quote']+="""& .by>.name{overflow-wrap:anywhere;}"""
CSS['chart-area']+="""& .series.tone-2{--inflexion-series:var(--a2);}& .series.tone-3{--inflexion-series:var(--a3);}& .series.tone-4{--inflexion-series:var(--a4);}"""


CSS['person']+="""&>.list,& .person>.list{align-self:stretch;flex:1;}& .list .item{grid-template-columns:var(--gap-sm) 1fr;column-gap:var(--gap-sm);}& .list .name{font-size:var(--type-14);font-weight:var(--body-weight);color:var(--n-7);}& .list{gap:var(--gap-sm);}& .note:empty{display:none;}"""
CSS['versus']+="""& .side>.list{flex:1;}& .list .item{grid-template-columns:var(--gap-sm) 1fr;column-gap:var(--gap-sm);}& .list .name{font-size:var(--type-16);font-weight:var(--body-weight);color:var(--ink);}"""
CSS['matrix']+="""& .cell>.list{flex:1;}& .list{gap:var(--gap-sm);}& .list .item{grid-template-columns:var(--gap-sm) 1fr;column-gap:var(--gap-sm);}& .list .name{font-size:var(--type-14);font-weight:var(--body-weight);color:var(--ink);}& .cell.on .list .name{color:var(--a1-on);}"""
CSS['pricing']+="""& .list{gap:var(--gap-sm);}& .list .item{grid-template-columns:var(--gap) 1fr;column-gap:var(--gap-sm);}& .list .name{font-size:var(--type-16);font-weight:var(--body-weight);color:var(--ink);}"""
CSS['concentric']+="""& .ring:nth-child(3){background:var(--a1-2-soft);color:var(--ink);}& .ring:nth-child(4){background:var(--a1-3-soft);}& .ring.on{background:var(--a1);color:var(--a1-on);}"""
CSS['code']+="""& .s{color:var(--a3-7);}"""


CSS['bullet']+="""&.bullets{gap:var(--gap-sm);}&.bullets>.bullet{flex:1;min-height:0;padding-bottom:var(--gap);align-content:center;gap:0;}& .note::after{content:none;}& .bullet::before,&.bullet::before{background:linear-gradient(to right,transparent calc(var(--target)*1% - 1px),var(--ink) calc(var(--target)*1% - 1px) calc(var(--target)*1% + 1px),transparent calc(var(--target)*1% + 1px)),linear-gradient(to right,var(--n-2) calc(var(--low,50)*1%),var(--n-3) 0 calc(var(--high,80)*1%),var(--n-4) 0);}@container (max-height:90px){& .note{display:none;}& .fig{font-size:var(--type-24);}& .name{font-size:var(--type-16);}}"""
CSS['heatmap']+="""&.calendar .heads,&.calendar .row{width:min(100%,calc((100cqh - var(--gap-lg))*12/7));align-self:center;}"""
CSS['chart-scatter']+="""& .dot span{background:var(--page);color:var(--ink);padding:0 calc(var(--gap-sm)/2);}"""
CSS['roadmap']+="""& .bar:not(.on){background:var(--n-1);color:var(--ink);border:var(--stroke) solid var(--n-3);}& .bar span{color:inherit;}"""
CSS['chart-donut']+="""&.donuts:has(>.donut:nth-child(4)){display:grid;grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:repeat(2,minmax(0,1fr));}&.donuts:has(>.donut:nth-child(4))>.donut{padding:0;}&.donuts:has(>.donut:nth-child(4))>.donut::before{top:40%;width:min(80cqw,70cqh);height:min(80cqw,70cqh);}&.donuts:has(>.donut:nth-child(4))>.donut::after{top:40%;width:min(44cqw,39cqh);height:min(44cqw,39cqh);}&.donuts:has(>.donut:nth-child(4))>.donut>.fig{position:absolute;left:0;right:0;top:40%;transform:translateY(-50%);font-size:var(--type-24);}&.donuts:has(>.donut:nth-child(4))>.donut>.name{position:absolute;top:76%;left:0;right:0;max-width:none;font-size:var(--type-12);} """
CSS['waffle']+="""& .units{width:min(75cqw,58cqh);max-height:none;}"""
CSS['concentric']+="""&:has(>.ring:nth-child(4))>.ring:nth-child(3){top:47%;height:48%;}&:has(>.ring:nth-child(4))>.ring:nth-child(4){top:72%;height:23%;}"""
CSS['positioning']+="""& .mark{padding:0;}& .mark .name{word-break:keep-all;}@container (max-width:650px){& .mark{width:64px;height:64px;}& .mark.on{width:88px;height:88px;}}"""
for n in range(3,9):
 for i in range(n):CSS['radar']+=f'&:is([style*="--n:{n}"],[style*="--n: {n}"])>.axis:nth-child({i+1}){{--inflexion-angle:{i*360/n}deg;}}'

CSS['pill']+=""".group>&{flex:1 1 0;}"""
CSS['steps']+="""& .name,& .note{word-break:keep-all;}"""

CSS['metric']+="""&.stats{align-items:stretch;}"""
CSS['concentric']+="""& .ring:nth-child(4):not(.on) .fig{color:var(--ink);}"""
CSS['roadmap']+="""& .mile span{background:var(--page);color:var(--ink);}"""

CSS['treemap']+="""& .tile{min-height:48px;padding:2px;gap:0;}& .tile .fig{font-size:var(--type-24);white-space:nowrap;}& .tile .name{font-size:var(--type-14);word-break:keep-all;}@container(max-width:850px){& .tile .fig{font-size:var(--type-16);}& .tile .name{font-size:var(--type-12);}}"""
CSS['sankey']+="""& .source{top:0;bottom:0;}&>.branch::before{width:18cqw;top:50%;translate:0 -50%;transform:none;}& .branch .fig{font-size:var(--type-24);white-space:nowrap;}& .branch>.branch{flex-direction:column;justify-content:center;}& .branch>.branch .name{font-size:var(--type-14);}& .branch>.branch .fig{font-size:var(--type-16);}@container(max-width:850px){& .branch .name{font-size:var(--type-14);}& .branch .fig{font-size:var(--type-20);}& .branch>.branch .fig{font-size:var(--type-12);}& .branch>.branch{padding:2px;}}"""
CSS['radar']+="""&::before,& .series{inset:auto;left:50%;top:50%;right:auto;bottom:auto;width:min(68cqw,68cqh);height:min(68cqw,68cqh);translate:-50% -50%;}&::before{position:absolute;left:50%;top:50%;}& .axis{left:calc(50% + min(42cqw,42cqh)*sin(var(--inflexion-angle)));top:calc(50% - min(42cqw,42cqh)*cos(var(--inflexion-angle)));}& .series>.name{top:-12%;left:-25%;}& .series:nth-of-type(2)>.name{left:75%;}& .series:nth-of-type(3)>.name{top:100%;left:75%;}"""
CSS['headline']+="""&{justify-content:flex-start;}& h2{font-size:var(--type-32);line-height:1.38;}@container(max-width:600px){& h2{font-size:var(--type-32);}}@container(max-height:190px){& h2{font-size:var(--type-32);}}"""
CSS['prose']+="""&{justify-content:flex-start;font-size:var(--type-16);line-height:1.55;}"""
CSS['pyramid']+="""&.line{display:block;overflow:visible;}&.line .level{position:absolute;bottom:calc(-1*var(--margin-y));padding:0;clip-path:none;border:0;border-radius:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;width:72%;height:410px;background:linear-gradient(100deg,var(--a1-4),var(--a1-2));}&.line .level:nth-child(1){left:calc(-1*var(--margin-x));height:420px;width:72%;}&.line .level:nth-child(2){left:22%;height:360px;width:72%;background:var(--a1-6);}&.line .level:nth-child(3){left:64%;height:290px;width:55%;background:var(--a1);}&.line .level>.name{margin-top:90px;font-size:var(--type-44);line-height:1.2;color:var(--a1-7);}&.line .level:nth-child(n+2)>.name{color:var(--a1-on);}&.line .level:nth-child(3)>.name{margin-top:90px;}&.line .note{text-align:center;color:var(--ink);font-size:var(--type-18);line-height:1.4;max-width:65%;}&.line .level:nth-child(n+2) .note{color:var(--a1-on);font-size:var(--type-16);}&.line .level .pill{margin:8px auto;min-height:40px;font-size:var(--type-24);}&.line .level:nth-child(n+2) .pill{font-size:var(--type-18);}&.line .level:nth-child(3) .pill{background:var(--page);color:var(--a1-7);}&.line .stat{position:absolute;left:30px;right:30px;bottom:-15px;height:100px;padding:0;border:0;background:none;}&.line .stat .parts{align-items:flex-start;}&.line .stat .fig{font-size:var(--type-80);color:var(--a1-7);}&.line .level:nth-child(n+2) .stat .fig{color:var(--a1-on);}&.line .stat small{font-size:var(--type-28);}&.line .stat .name,&.line .stat .note{display:none;}"""
CSS['pyramid']+="""&.line .level:first-child>.name,&.line .level:first-child>.note{translate:-50px 0;}&.line .level:nth-child(2)>.name,&.line .level:nth-child(2)>.note{translate:-30px 0;}&.line .level:first-child>.note{color:var(--ink);}&.line .level .pill{display:inline-flex;width:auto;padding:6px 16px;min-height:40px;}&.line .level .pill .parts{display:block;}&.line .level .pill .name{margin:0;font-size:var(--type-24);line-height:1;}&.line .level:nth-child(n+2) .pill .name{font-size:var(--type-18);}&.line .level:nth-child(3) .pill .name{color:var(--a1-7);}&.line .level .stat{display:block;height:95px;bottom:0;}&.line .level .stat .parts{display:block;text-align:left;}&.line .level .stat .fig{text-align:left;line-height:1;}&.line::after{content:"";position:absolute;left:calc(50% - 48px);top:32px;width:96px;height:18px;background:radial-gradient(circle at 8px 9px,var(--a1) 0 6px,transparent 6.5px),radial-gradient(circle at 42px 9px,var(--a1) 0 6px,transparent 6.5px),radial-gradient(circle at 76px 9px,var(--a1) 0 6px,transparent 6.5px);}"""
CSS['prose']+="""&.quiet{text-align:right;color:var(--ink);font-size:var(--type-16);}"""
CSS['pyramid']+="""&.line .level{mask-image:none;isolation:isolate;background:none;}&.line .level::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(100deg,var(--a1-4),var(--a1-2));clip-path:shape(from 0% 100%,line to 0% 76%,line to 36.25% 11.4%,curve to 51.25% 11.4% with 43.75% -2%,line to 100% 90%,line to 100% 100%,close);}&.line .level:nth-child(2){background:none;}&.line .level:nth-child(3){background:none;}&.line .level:nth-child(2)::before{background:var(--a1-6);}&.line .level:nth-child(3)::before{background:var(--a1);}"""
CSS['cycle']+="""&.line{border:var(--stroke) solid var(--n-3);border-radius:calc(var(--radius)*1.5);background:linear-gradient(var(--page),var(--n-1));height:270px;width:calc(100% + var(--gap-lg));align-self:end;margin-bottom:var(--gap-sm);}&.line::before,&.line::after{content:none;}&.line .core{position:absolute;left:39%;top:-10px;width:154px;height:28px;border:0;border-radius:999px;background:var(--a1);color:var(--a1-on);font-size:var(--type-16);display:flex;align-items:center;justify-content:center;transform:none;translate:none;}&.line .node{position:absolute;left:32px;top:50px;width:171px;height:74px;transform:none;translate:none;border:0;border-radius:0;padding:0;background:none;display:flex;align-items:center;justify-content:center;isolation:isolate;}&.line .node::before,&.line .node::after{content:"";position:absolute;inset:0;z-index:-2;background:var(--a1);clip-path:polygon(0 0,91% 0,100% 50%,91% 100%,0 100%,9% 50%);}&.line .node::after{inset:2px;z-index:-1;background:var(--page);}&.line .node .name{font-size:var(--type-18);font-weight:var(--name-weight);line-height:1.35;color:var(--ink);margin:0;max-width:145px;}&.line .node .note{display:none;}&.line .node:nth-child(3){left:210px;top:50px;}&.line .node:nth-child(4){left:388px;top:50px;}&.line .node:nth-child(5){left:299px;top:154px;}&.line .node:nth-child(6){left:121px;top:154px;}&.line .node:nth-child(n+5)::before,&.line .node:nth-child(n+5)::after{clip-path:polygon(9% 0,100% 0,91% 50%,100% 100%,9% 100%,0 50%);}"""
CSS['headline']+="""&.line{width:calc(100% + var(--gap-lg)*2);gap:var(--gap);}&.line .note{font-size:var(--type-16);line-height:var(--body-line);color:var(--ink);}"""
CSS['list']+="""&.line{justify-content:space-between;gap:0;width:calc(100% + var(--gap-lg));}&.line .item{height:110px;grid-template-columns:72px 1fr;column-gap:var(--gap);row-gap:var(--gap-sm);align-content:start;}&.line .item::before{position:absolute;left:44px;top:14px;width:34px;height:0;border-top:2px dotted var(--ink);border-radius:0;margin:0;background:none;}&.line .item .name{font-size:var(--type-22);line-height:var(--label-line);}&.line .item .name small{font-size:var(--type-14);font-weight:var(--body-weight);color:var(--a1-6);margin-left:var(--gap-sm);}&.line .item .note{font-size:var(--type-16);line-height:1.5;color:var(--ink);}&.line .mark{background:none;}&.line .mark .icon{width:30px;height:30px;color:var(--a1-7);}&.line .mark:has([data-icon="chevrons-down"]){top:130px;left:210px;}&.line .mark:has([data-icon="chevrons-down"]) .icon{width:24px;height:24px;}"""
CSS['timeline']+="""&.line{display:flex;align-items:stretch;gap:0;padding-top:50px;border-bottom:var(--stroke) solid var(--a1);height:calc(100% - var(--gap-sm));align-self:start;}&.line::before,&.line::after{content:none;}&.line .stop{flex:1;position:relative;top:auto;bottom:auto;padding:62px var(--gap-sm) 0;border-left:2px dotted var(--a1);text-align:center;display:block;color:var(--a1-7);}&.line .stop:first-child{border-left:0;}&.line .stop::before,&.line .stop::after{content:none;}&.line .stop .kick{display:flex;height:44px;align-items:center;justify-content:center;margin:0;color:inherit;}&.line .stop .kick .icon{width:44px;height:44px;}&.line .stop .name{font-size:var(--type-22);line-height:1.25;color:inherit;margin-top:var(--gap);white-space:nowrap;}&.line .stop .note{font-size:var(--type-16);line-height:1.35;color:var(--ink);margin-top:var(--gap);}&.line .stop:nth-child(n+4){color:var(--a1-6);}&.line .stop:nth-child(n+7){color:var(--a1-5);}"""
CSS['pill']+="""&.line{height:50px;min-height:50px;align-self:flex-start;border-radius:0;margin-left:calc(var(--gap)*-.5);margin-right:calc(var(--gap)*-.5);background:var(--a1);color:var(--a1-on);border:0;padding:0;}&.line:first-child{border-radius:999px 0 0 999px;margin-left:0;}&.line:last-child{border-radius:0 999px 999px 0;margin-right:0;}&.line.tone-2{background:var(--a1-6);}&.line.tone-3{background:var(--a1-5);}&.line .parts{display:block;}&.line .name{font-size:var(--type-16);color:inherit;line-height:var(--label-line);}"""
CSS['pyramid']+="""&.line .level .pill{container-type:normal;flex:none;width:max-content;max-width:none;white-space:nowrap;}&.line .level .pill .parts{width:auto;}&.line .level .stat{bottom:-25px;}&.line .level:first-child .stat .fig{font-size:var(--type-92);}&.line .level:nth-child(2) .stat{left:92px;bottom:-38px;}&.line .level:nth-child(2) .stat .fig{font-size:var(--type-76);}&.line .level:nth-child(3) .stat{left:75px;bottom:-52px;}&.line .level:nth-child(3) .stat .fig{font-size:var(--type-64);}"""
CSS['timeline']+="""&.line .stop{align-self:stretch;border-top:0;background:none;}&.line .stop .kick{background:none;border:0;border-radius:0;padding:0;width:auto;}&.line .stop .name{font-size:var(--type-20);}&.line .stop .note{margin-top:calc(var(--gap-sm)*2);}"""
CSS['pill']+="""&.line .parts{text-align:center;}"""
CSS['cycle']+="""&.line{width:calc(100% + var(--gap-lg) + 4px);margin-bottom:calc(var(--gap-sm)*2);}"""
CSS['list']+="""&.line .item{height:118px;}"""
CSS['prose']+="""&.line{font-size:var(--type-14);text-align:right;}"""
exec((BASE/'build/fidelity_rules.py').read_text())
# Coverage assertion: a missing visual rule is a build failure.
assert len(CSS)==56,(len(CSS),set(ROOT)-set(CSS))
for leaf,roots in ROOT.items():
 scope=':is('+','.join(f'.{r}[data-el="{NAME}-{leaf}"]' for r in roots)+')'
 s=(common+CSS[leaf]).replace('&',scope)
 s=re.sub(r'line-height:([0-9.]+(?:px)?)',lambda m:'line-height:var(--inflexion-line-'+line_tokens[m.group(1)]+')',s)
 s=s.replace('color:var(--a1);','color:var(--a1-7);').replace('color:var(--a2);','color:var(--a2-7);').replace('color:var(--a3);','color:var(--a3-7);')
 if leaf=='chart-area':s=s.replace('color:var(--inflexion-series);','color:var(--ink);')
 if leaf=='callout':s=s.replace('linear-gradient(150deg,var(--a1),var(--a1-7))','var(--a1)')
 write(C/'elements'/leaf/'element.css',s)
print('Built',len(CSS),'elements and foundation')
# Repair non-model legacy list markup while preserving every Korean phrase.
for leaf in ROOT:
 if leaf in model:continue
 for f in (C/'elements'/leaf/'fixtures').glob('*.html'):
  text=f.read_text()
  def normalize_list(m):
   cls='list check' if leaf=='pricing' else 'list'
   content=re.sub(r'<li>(.*?)</li>',lambda z:'<div class="item"><span class="name">'+z.group(1)+'</span></div>',m.group(1),flags=re.S)
   return '<div class="'+cls+'" data-el="inflexion-list">'+content+'</div>'
  text=re.sub(r'<ul class="list">(.*?)</ul>',normalize_list,text,flags=re.S)
  text=re.sub(r'class="(tag|hl)"(?! data-el)',r'class="\1" data-el="inflexion-tag"',text)
  if leaf=='person' and f.stem=='person':text=text.replace('min: 6x3','min: 8x4')
  f.write_text(text)
write(C/'elements/legend/fixtures/expanded.html','''<!-- min: 6x1 -->
<div class="legend" data-el="inflexion-legend" style="grid-column:1 / span 12; grid-row:1 / span 6"><span class="key tone-1">기존 고객 매출</span><span class="key tone-2">신규 고객 매출</span><span class="key tone-3">해외 파트너 매출</span></div>
''')
write(C/'elements/tag/fixtures/expanded.html','''<!-- min: 8x2 -->
<div class="prose" data-el="inflexion-prose" style="grid-column:1 / span 12; grid-row:1 / span 6"><p>핵심 지표인 <b class="hl" data-el="inflexion-tag">분기별 반복 매출</b>이 안정적으로 늘었습니다. <span class="tag" data-el="inflexion-tag">검증 완료</span> 고객의 실제 사용 결과를 반영해 서비스를 개선하고 있습니다. <span class="tag" data-el="inflexion-tag">확대 예정</span></p></div>
''')
write(C/'elements/pricing/fixtures/expanded.html','''<!-- min: 8x4 -->
<div class="plans" data-el="inflexion-pricing" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="plan on" data-el="inflexion-pricing"><span class="tag" data-el="inflexion-tag">빠른 도입</span><b class="name">성장하는 운영팀</b><div class="price"><b class="fig">39만</b><small>원 / 월</small></div><div class="list check" data-el="inflexion-list"><div class="item"><span class="name">설비 3대의 실시간 상태 확인</span></div><div class="item"><span class="name">주간 운영 분석 리포트</span></div></div></div><div class="plan" data-el="inflexion-pricing"><b class="name">확장형 글로벌 운영</b><div class="price"><b class="fig">89만</b><small>원 / 월</small></div><div class="list check" data-el="inflexion-list"><div class="item"><span class="name">해외 사업장 통합 모니터링</span></div><div class="item"><span class="name">전담 매니저와 운영 기준 설계</span></div><div class="item"><span class="name">월별 개선 계획 점검</span></div></div></div></div>
''')
write(C/'elements/versus/fixtures/expanded.html','''<!-- min: 8x4 -->
<div class="versus" data-el="inflexion-versus" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="side on"><b class="name">통합 운영 2057</b><div class="list" data-el="inflexion-list"><div class="item"><span class="name">고객 요청부터 생산까지 연결</span></div><div class="item"><span class="name">변경 이력과 책임자를 함께 기록</span></div><div class="item"><span class="name">재고 회전일 24일</span></div><div class="item"><span class="name">반복 업무를 자동으로 처리</span></div></div></div><b class="vs">VS</b><div class="side"><b class="name">기존 개별 운영</b><div class="list" data-el="inflexion-list"><div class="item"><span class="name">부서별로 분리된 정보</span></div><div class="item"><span class="name">담당자에게 직접 확인</span></div><div class="item"><span class="name">재고 회전일 41일</span></div></div></div></div>
''')

for f in (C/'elements/treemap/fixtures').glob('*.html'):
 text=f.read_text().replace('min: 4x3','min: 4x4').replace('min: 6x3','min: 8x4').replace('min: 8x3','min: 10x4')
 f.write_text(text)
