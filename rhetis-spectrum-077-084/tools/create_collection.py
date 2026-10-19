"""Author the Spectrum source collection. No reference artwork is embedded."""
from pathlib import Path
import json

BASE=Path(__file__).resolve().parents[1]
C=BASE/'collection/rhetis-spectrum'
ID='rhetis-spectrum'
def put(p,s):
 p=C/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.strip()+'\n')
def js(p,d):put(p,json.dumps(d,ensure_ascii=False,indent=2))

light={'page':'#ffffff','surface':'#f5f6f7','surface-2':'#edf0f3','ink':'#172432','ink-2':'#34465a','mute':'#5b6471','line':'#bdc6cf','accent':'#ed704c','accent-ink':'#20242a','accent-soft':'#fff0e9','tone-1':'#153e68','tone-1-ink':'#ffffff','tone-2':'#ffdf8a','tone-2-ink':'#282b31','tone-3':'#2469ad','tone-3-ink':'#ffffff','tone-4':'#dce7f1','tone-4-ink':'#173e68','tone-5':'#edf0f3','tone-5-ink':'#34465a','good':'#24704f','warn':'#8d600f','bad':'#b33036','accent-text':'#a33d21'}
dark={'page':'#0c1728','surface':'#142338','surface-2':'#1e3148','ink':'#f6f8fa','ink-2':'#d9e2ed','mute':'#adbccf','line':'#546880','accent':'#ff906d','accent-ink':'#17202b','accent-soft':'#392c2d','tone-1':'#bdd7f3','tone-1-ink':'#10263f','tone-2':'#ffe39e','tone-2-ink':'#282b31','tone-3':'#86bffd','tone-3-ink':'#10263f','tone-4':'#2d4967','tone-4-ink':'#f6f8fa','tone-5':'#26374d','tone-5-ink':'#f6f8fa','good':'#91dab1','warn':'#f0c67d','bad':'#ffa2a6','accent-text':'#ffb097'}
other={'font-display':'"Gmarket Sans", "Pretendard", sans-serif','font-body':'"Pretendard", sans-serif','weight-display':'700','weight-body':'400','tracking-display':'-0.035em','radius':'18px','radius-sm':'6px','stroke':'1px','text-min':'12px','margin-x':'56px','margin-y':'44px','gap':'24px','gap-sm':'12px','gap-lg':'36px','pad':'24px','furn-edge':'20px','top-h':'24px','foot-h':'24px','furn-gap':'12px','rail-w':'40px','rail-gap':'20px','title-weight':'700','title-line':'1.22','title-track':'-0.035em','lead-weight':'400','lead-line':'1.5','lead-track':'-0.02em','figure-weight':'700','figure-line':'1.1','figure-track':'-0.045em','name-weight':'600','name-line':'1.35','name-track':'-0.025em','body-weight':'400','body-line':'1.55','body-track':'-0.015em','label-weight':'600','label-line':'1.25','label-track':'-0.015em','label-track-latin':'0.06em'}
put(Path('kit/css/tokens.css'),'.slide {\n'+''.join(f'  --{k}: {v};\n' for k,v in (light|other).items())+'}\n.slide.dark {\n'+''.join(f'  --{k}: {v};\n' for k,v in dark.items())+'}')
js(Path('kit/kit.json'),{'schema':'rhetis.kit/2','id':ID,'label':'Rhetis Spectrum','tokens':'css/tokens.css','description':'description.md','extensions':{'--accent-text':'color'}})
put(Path('kit/description.md'),'''Spectrum is a crisp business-presentation system combining editorial white space, thin blue-grey rules and squared frames with small softened corners. Warm coral signals action; pale yellow creates a paper-tab emphasis; deep blue carries structure and measured analytical content. Strong Korean display typography, tightly tracked figures and calm body copy establish a deliberate hierarchy. Dark mode uses an independently balanced midnight canvas, pale blue structure and warm luminous accents.''')
js(Path('foundation/foundation.json'),{'schema':'rhetis.design-library-foundation-source/1','kit':ID,'registrations':{},'tokenDefaults':{}})
put(Path('foundation/description.md'),'A clean 16:9 editorial page with a fine top rule, a short coral section marker and a precise twelve-by-six content grid. Covers feature an abstract stepped arrow formed from CSS shapes. Light grey seats reserve space for imagery. Foundation selectors deliberately avoid all element roots.')
put(Path('foundation/foundation.css'),'''
.slide {width:1280px;height:720px;position:relative;box-sizing:border-box;background:var(--page);color:var(--ink);font-family:var(--font-body);font-size:var(--type-20);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);isolation:isolate;}
.slide *, .slide *::before, .slide *::after {box-sizing:border-box;}
.slide .page {position:absolute;inset:var(--margin-y) var(--margin-x);display:flex;flex-direction:column;gap:var(--gap);min-width:0;min-height:0;}
.slide .page::before {content:"";position:absolute;left:0;right:0;top:calc(var(--gap-sm)*-1);height:1px;background:var(--line);}
.slide .head {flex:none;padding-bottom:var(--gap-sm);border-bottom:var(--stroke) solid var(--line);}
.slide .head.center {text-align:center;}
.slide .kicker {font-size:var(--type-14);font-weight:var(--label-weight);letter-spacing:var(--label-track-latin);line-height:var(--label-line);color:var(--accent-text);margin:0 0 var(--gap-sm);}
.slide .title {font-family:var(--font-display);font-size:var(--type-40);font-weight:var(--title-weight);letter-spacing:var(--title-track);line-height:var(--title-line);margin:0;}
.slide .lead {font-size:var(--type-18);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track);color:var(--mute);margin:var(--gap-sm) 0 0;}
.slide .body {flex:1;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));gap:var(--gap);min-width:0;min-height:0;container-type:size;}
.slide .group {display:flex;gap:var(--gap);min-width:0;min-height:0;}
.slide .group > * {flex:1;min-width:0;min-height:0;}
.slide .group.col,.slide .stack {display:flex;flex-direction:column;gap:var(--gap);min-height:0;min-width:0;}
.slide .stack > * {flex:1;min-height:0;min-width:0;}
.slide .group.two {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));}
.slide .group.three {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));}
.slide .split {display:grid;grid-template-columns:1fr 2fr;gap:var(--gap);min-width:0;min-height:0;}
.slide .split.wide-left {grid-template-columns:2fr 1fr;}
.slide .seat {display:flex;align-items:center;justify-content:center;background:var(--surface-2);color:var(--mute);font-size:var(--type-14);min-width:0;min-height:0;position:relative;}
.slide .seat::before {content:attr(data-ph);font-weight:var(--label-weight);}
.slide .seat.avatar {width:80px;height:80px;aspect-ratio:1;border-radius:50%;}
.slide .seat.portrait {aspect-ratio:4/5;}
.slide .seat.logo {aspect-ratio:2.5/1;}
.slide .seat.icon {width:48px;height:48px;aspect-ratio:1;border-radius:var(--radius-sm);}
.slide .seat.back {position:absolute;inset:0;z-index:-1;}
.slide .top,.slide .foot {position:absolute;left:var(--furn-edge);right:var(--furn-edge);display:flex;align-items:center;justify-content:space-between;gap:var(--furn-gap);font-size:var(--type-12);color:var(--mute);line-height:var(--label-line);}
.slide .top {top:var(--furn-edge);height:var(--top-h);}
.slide .foot {bottom:var(--furn-edge);height:var(--foot-h);}
.slide .idx,.slide .deck,.slide .sec,.slide .src,.slide .no,.slide .label {font-size:var(--type-12);font-weight:var(--label-weight);}
.slide .rail {position:absolute;left:var(--furn-edge);top:var(--margin-y);bottom:var(--margin-y);width:var(--rail-w);border-left:var(--stroke) solid var(--line);}
.slide .icon {display:inline-flex;align-items:center;justify-content:center;flex:none;}
.slide.cover .page {justify-content:center;}
.slide.cover .page::before {background:var(--accent);width:80px;height:3px;right:auto;}
.slide.cover .lockup {max-width:75%;position:relative;z-index:1;}
.slide.cover .title {font-size:var(--type-60);max-width:860px;}
.slide.cover .lead {font-size:var(--type-24);}
.slide.cover .at-center {align-self:center;text-align:center;}
.slide.cover .at-left {align-self:flex-start;}
.slide.cover .at-bottom-left {margin-top:auto;margin-bottom:var(--gap-lg);}
.slide.cover .at-top-left {margin-bottom:auto;margin-top:var(--gap-lg);}
.slide.cover .meta {position:absolute;bottom:0;left:0;font-size:var(--type-14);color:var(--mute);}
.slide.cover .deco {position:absolute;right:0;bottom:0;width:380px;height:350px;border:var(--stroke) solid var(--line);background:var(--surface);clip-path:polygon(0 100%,0 65%,25% 65%,25% 40%,55% 40%,55% 15%,80% 15%,80% 0,100% 0,100% 100%);}
.slide.cover .deco::after {content:"";position:absolute;right:0;top:0;width:25%;height:100%;background:var(--accent);}
''')
put(Path('foundation/fixtures/seat.html'),'''<!-- min: 12x6 -->
<section class="slide"><div class="page"><header class="head"><p class="kicker">SPECTRUM / 2026</p><h1 class="title">분명한 구조로, 더 좋은 의사결정</h1><p class="lead">정갈한 여백과 절제된 강조로 핵심 메시지를 전합니다.</p></header><div class="body"><div class="seat" data-ph="01" style="grid-column:1 / span 8; grid-row:1 / span 6"></div><div class="seat portrait" data-ph="02" style="grid-column:9 / span 4; grid-row:1 / span 6"></div></div></div></section>''')
put(Path('foundation/fixtures/cover.html'),'''<!-- min: 12x6 -->
<section class="slide cover"><div class="page"><div class="lockup at-left"><p class="kicker">BUSINESS STRATEGY / 2026</p><h1 class="title">작은 변화에서 시작하는<br>지속 가능한 성장</h1><p class="lead">데이터에서 실행까지, 함께 만드는 다음 단계</p></div><div class="meta">전략기획팀 · 2026년 10월</div><div class="deco"></div></div></section>''')

CONTRACTS=json.loads((BASE/'contract/taxonomy.json').read_text())['contracts']
def root(n,cls,body,style='',mn='6x3'):
 return f'<!-- min: {mn} -->\n<div class="{cls}" data-el="{ID}-{n}" style="grid-column:1 / span 12; grid-row:1 / span 6{("; "+style) if style else ""}">{body}</div>'
def el(n,css,fixtures,desc):
 contract=next(x for x in CONTRACTS if x['category'].split('.')[-1]==n)
 d=Path('elements')/n
 js(d/'element.json',{'schema':'rhetis.design-library-element-source/1','contract':contract['id'],'registrations':{},'tokenDefaults':{}})
 put(d/'description.md',desc)
 # All selectors are compiled from the collection-specific root. No unscoped utility selectors.
 roots=','.join(f'.{r}[data-el="{ID}-{n}"]' for r in contract['roots'])
 scope=f':is({roots})'
 common='''ROOT {min-width:0;min-height:0;container-type:size;position:relative;color:var(--ink);font-family:var(--font-body);font-size:var(--type-20);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);}
ROOT .name {font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);}
ROOT .note {font-size:var(--type-16);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);color:var(--mute);}
ROOT .kick {font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track-latin);color:var(--accent-text);}
ROOT .fig {font-family:var(--font-display);font-size:var(--type-64);font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);font-variant-numeric:tabular-nums;}
ROOT .fig small {font-size:var(--type-24);font-weight:var(--label-weight);margin-left:calc(var(--gap-sm)/2);}
ROOT .mark {display:flex;align-items:center;justify-content:center;font-size:var(--type-20);font-weight:var(--label-weight);color:var(--accent-text);}
ROOT p, ROOT blockquote {margin:0;}
@container (max-width:640px) { ROOT .name {font-size:var(--type-18);} ROOT .fig {font-size:var(--type-40);} ROOT .fig small {font-size:var(--type-18);} ROOT .note {font-size:var(--type-14);} }
@container (max-height:220px) { ROOT .name {font-size:var(--type-16);} ROOT .fig {font-size:var(--type-32);} ROOT .note {font-size:var(--type-12);} ROOT .kick {display:none;} }
'''
 put(d/'element.css',(common+css).replace('ROOT',scope))
 for name,content in fixtures.items():put(d/'fixtures'/f'{name}.html',content)

parts=lambda kick,fig,name,note,mark='':f'<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<div class="mark">{mark}</div>' if mark else '')+(f'<p class="fig">{fig}</p>' if fig else '')+f'<p class="name">{name}</p><p class="note">{note}</p></div>'
names=['고객의 목소리','제품 경험 개선','데이터 기반 실행','운영 체계 고도화','지속 가능한 성장','성과 공유']
notes=['고객의 실제 사용 맥락에서 다음 기회를 발견합니다.','작은 불편을 먼저 해결해 일관된 경험을 제공합니다.','가설을 검증하고 결과를 다음 실행에 반영합니다.','책임과 역할을 명확히 정해 협업의 속도를 높입니다.','핵심 지표를 함께 살피고 성장을 이어갑니다.','팀의 배움을 공유하고 더 나은 기준을 만듭니다.']
el('card','''ROOT {display:flex;align-items:stretch;border:var(--stroke) solid var(--line);border-top:3px solid var(--accent);background:var(--surface);border-radius:var(--radius-sm);}
ROOT .parts {display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);padding:var(--pad);width:100%;}
ROOT.on {background:var(--accent);color:var(--accent-ink);border-color:var(--accent-text);}
ROOT.on :is(.name,.fig,.note,.kick,.mark) {color:var(--accent-ink);}
ROOT.line {background:var(--page);border-top-color:var(--tone-1);}
ROOT.quiet {border-color:var(--surface);background:var(--surface);}
ROOT .mark {width:48px;height:48px;border:var(--stroke) solid currentColor;border-radius:50%;}
ROOT .fig {color:var(--tone-1);}
'''+''.join(f'ROOT.tone-{i} {{background:var(--tone-{i});border-color:var(--tone-{i});}} ROOT.tone-{i} :is(.name,.fig,.note,.kick,.mark) {{color:var(--tone-{i}-ink);}}\n' for i in range(1,6)),
{v:root('card','card '+v,parts('GROWTH / 2026','32<small>%</small>','고객 경험이 만드는 성장','데이터와 현장의 목소리를 연결해 고객이 체감하는 변화를 만듭니다.','↗')) for v in ['line','on','quiet','tone-1','tone-2','tone-3','tone-4','tone-5']},'A measured rectangular card with a fine outline, a coral top rule and generous internal rhythm. Figures use deep blue; filled emphasis and five semantic tones preserve the same hierarchy.')
el('pill','''ROOT {display:flex;align-items:center;justify-content:center;background:var(--surface);border:var(--stroke) solid var(--line);border-radius:999px;padding:var(--pad);}
ROOT .parts {display:flex;align-items:center;justify-content:center;gap:var(--gap-sm);min-width:0;}
ROOT .mark {width:36px;height:36px;flex:none;border-radius:50%;background:var(--accent-soft);}
ROOT .name {font-size:var(--type-22);text-align:center;}
ROOT.on {background:var(--accent);border-color:var(--accent-text);}
ROOT.on :is(.name,.note) {color:var(--accent-ink);}
ROOT.line {background:var(--page);border-color:var(--tone-1);}
ROOT.quiet {border-color:var(--surface);}
@container (max-width:540px) {ROOT .note {display:none;} ROOT .name {font-size:var(--type-18);}}
''',{v:root('pill','pill '+v,parts('', '', '함께 만드는 다음 단계','실행 준비 완료','✓'),mn='6x2') for v in ['on','line','quiet']},'A one-line capsule balances a circular mark, centred label and secondary note. Its warm fill and thin-line variants have the same optical alignment.')
el('callout','''ROOT {display:flex;align-items:center;justify-content:center;gap:var(--gap);padding:var(--pad);background:var(--accent-soft);border-left:4px solid var(--accent);border-top:var(--stroke) solid var(--line);border-bottom:var(--stroke) solid var(--line);}
ROOT p {font-size:var(--type-32);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track);}
ROOT b {font-weight:var(--title-weight);color:var(--tone-2-ink);background:var(--tone-2);}
ROOT .icon {font-size:var(--type-36);color:var(--accent-text);}
@container (max-width:680px) {ROOT p {font-size:var(--type-22);}}
@container (max-height:180px) {ROOT p {font-size:var(--type-20);}}
''',{'conclusion':root('callout','callout','<p>변화를 이어가는 힘은 <b>명확한 실행</b>에서 시작됩니다.</p>',mn='8x2'),'icon':root('callout','callout','<span class="icon">↗</span><p>고객의 작은 불편이 <b>다음 성장의 기회</b>입니다.</p>',mn='8x2')},'An editorial conclusion strip uses a coral edge and pale ground, with a yellow underline carrying the key phrase.')
el('tag','''ROOT.tag {display:inline-flex;align-items:center;justify-content:center;align-self:center;justify-self:center;min-height:48px;min-width:180px;width:max-content;white-space:nowrap;container-type:normal;padding:var(--gap-sm) var(--pad);background:var(--tone-2);color:var(--tone-2-ink);border:var(--stroke) solid var(--line);font-size:var(--type-18);font-weight:var(--label-weight);line-height:var(--label-line);text-align:center;border-radius:var(--radius-sm);}
ROOT.hl {display:inline;align-self:center;justify-self:start;container-type:normal;width:max-content;max-width:100%;padding:0 calc(var(--gap-sm)/3);font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--body-line);vertical-align:baseline;box-decoration-break:clone;-webkit-box-decoration-break:clone;background:var(--tone-2);color:var(--tone-2-ink);}
@container (max-width:420px) {ROOT.tag {font-size:var(--type-16);} ROOT.hl {font-size:var(--type-20);}}
''',{'label':root('tag','tag','핵심 실행 과제',mn='3x1'),'highlight':root('tag','hl','고객 중심의 의사결정',mn='6x2')},'A compact pale-yellow label and a true inline text highlight carry the paper-tab language into running copy. The highlight uses intrinsic sizing, shallow token padding and baseline alignment so it never turns the sentence into a panel.')

listbody=lambda n:''.join(f'<div class="item"><p class="name">{names[i%6]}</p><p class="note">{notes[i%6]}</p></div>' for i in range(n))
el('list','''ROOT {display:flex;flex-direction:column;justify-content:center;gap:var(--gap);counter-reset:spectrum-item;}
ROOT .item {position:relative;padding-left:calc(var(--pad)*2);counter-increment:spectrum-item;}
ROOT .item::before {content:"";position:absolute;left:var(--gap-sm);top:.65em;width:7px;height:7px;background:var(--accent);border-radius:50%;}
ROOT .name {margin-bottom:calc(var(--gap-sm)/2);}
ROOT.check .item::before {content:"✓";background:var(--accent-soft);border-radius:var(--radius-sm);width:28px;height:28px;top:0;left:0;display:flex;align-items:center;justify-content:center;color:var(--accent-text);font-size:var(--type-18);font-weight:var(--label-weight);}
ROOT.num .item::before {content:counter(spectrum-item,decimal-leading-zero);width:32px;height:32px;top:0;left:0;border-radius:var(--radius-sm);background:var(--tone-2);color:var(--tone-2-ink);font-size:var(--type-16);font-weight:var(--label-weight);display:flex;align-items:center;justify-content:center;}
ROOT.divided .item {padding-bottom:var(--gap-sm);border-bottom:var(--stroke) solid var(--line);}
ROOT:has(.item:nth-child(7)) {gap:var(--gap-sm);}
ROOT:has(.item:nth-child(7)) .name {font-size:var(--type-18);}
ROOT:has(.item:nth-child(7)) .note {font-size:var(--type-14);}
@container (max-height:420px) {ROOT {gap:var(--gap-sm);} ROOT .name {font-size:var(--type-18);} ROOT .note {font-size:var(--type-14);}}
@container (max-height:260px) {ROOT .note {display:none;}}
''',{'two':root('list','list',listbody(2),mn='6x2'),'checks':root('list','list check',listbody(4),mn='6x4'),'eight':root('list','list num divided',listbody(8),mn='8x6')},'A clear vertical list uses coral dots, optically centred ticks or automatically generated yellow number tabs. Dividers provide a denser operational variant.')
el('quote','''ROOT {display:flex;flex-direction:column;justify-content:center;gap:var(--gap-lg);padding:var(--pad);border-left:3px solid var(--accent);background:var(--surface);}
ROOT blockquote {font-family:var(--font-display);font-size:var(--type-36);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track);position:relative;}
ROOT blockquote::before {content:"“";display:block;color:var(--accent-text);font-size:var(--type-64);font-weight:var(--figure-weight);line-height:var(--figure-line);}
ROOT .by {display:grid;grid-template-columns:auto 1fr;column-gap:var(--gap-sm);align-items:center;}
ROOT .by .seat {grid-row:span 2;}
ROOT.big blockquote {font-size:var(--type-48);}
@container (max-width:640px) {ROOT blockquote,ROOT.big blockquote {font-size:var(--type-24);} ROOT .by .seat {width:56px;height:56px;}}
@container (max-height:260px) {ROOT {gap:var(--gap-sm);} ROOT blockquote,ROOT.big blockquote {font-size:var(--type-20);} ROOT blockquote::before {display:none;}}
''',{'voice':root('quote','quote','<blockquote>고객의 질문을 끝까지 이해했을 때, 해결해야 할 일이 더 분명해졌습니다.</blockquote><div class="by"><div class="seat avatar" data-ph="01"></div><p class="name">김민지 · 고객경험팀</p><p class="note">서비스 개선 인터뷰 중에서</p></div>',mn='6x4'),'large':root('quote','quote big','<blockquote>같은 목표를 바라보는 팀이<br>더 멀리 나아갑니다.</blockquote><div class="by"><div class="seat avatar" data-ph="02"></div><p class="name">박준호 · 사업전략실</p><p class="note">2026년 하반기 전략 워크숍</p></div>',mn='8x4')},'An oversized editorial quotation is anchored by a coral rule and a quietly structured attribution with a grey avatar seat.')

stat=lambda i:f'<div class="stat" data-el="{ID}-metric">'+parts('',f'{[32,95,128,24,68,3][i]}<small>{["%","%","억","개","%","배"][i]}</small>',names[i],notes[i])+'</div>'
el('metric','''ROOT.stats {display:flex;align-items:stretch;gap:var(--gap);}
ROOT.stat {display:flex;flex-direction:column;justify-content:center;padding:var(--pad);border-top:3px solid var(--tone-1);}
ROOT.stats > .stat .parts {display:grid;grid-template-rows:var(--type-48) calc(var(--type-18)*3) calc(var(--type-14)*5);align-content:center;height:100%;}
ROOT.stats > .stat {flex:1;border-left:var(--stroke) solid var(--line);padding:var(--pad);min-width:0;}
ROOT .parts {display:flex;flex-direction:column;gap:var(--gap-sm);}
ROOT .fig {color:var(--tone-1);}
@container (max-width:800px) {ROOT.stats {flex-wrap:wrap;} ROOT.stats > .stat {flex-basis:28%;} ROOT .fig {font-size:var(--type-40);} ROOT .name {font-size:var(--type-18);}}
@container (max-height:300px) {ROOT .note {display:none;}}
''',{'one':root('metric','stat',parts('','128<small>억</small>','새로운 성장의 규모','핵심 사업의 누적 성과를 함께 확인합니다.'),mn='4x3'),'three':root('metric','stats',''.join(stat(i) for i in range(3)),mn='9x3'),'six':root('metric','stats',''.join(stat(i) for i in range(6)),mn='12x5')},'Bare figures sit on a precise top rule with no surrounding surface. A row divides metrics with thin vertical rules, using deep blue figures and muted explanatory copy.')
el('delta','''ROOT {display:flex;align-items:center;justify-content:center;gap:var(--gap-lg);font-family:var(--font-display);font-size:var(--type-56);font-weight:var(--figure-weight);letter-spacing:var(--figure-track);line-height:var(--figure-line);}
ROOT::before {content:"→";order:1;color:var(--accent-text);font-size:var(--type-44);}
ROOT .from {color:var(--mute);font-size:var(--type-40);}
ROOT .to {order:2;color:var(--tone-2-ink);padding:var(--pad);background:var(--tone-2);border-bottom:3px solid var(--accent);}
@container (max-width:680px) {ROOT {gap:var(--gap-sm);font-size:var(--type-36);} ROOT .from {font-size:var(--type-28);} ROOT::before {font-size:var(--type-28);}}
''',{'growth':root('delta','delta','<span class="from">12.1억</span><span class="to">15.6억</span>',mn='7x2'),'time':root('delta','delta','<span class="from">8.4일</span><span class="to">3.2일</span>',mn='7x2')},'A restrained before-and-after comparison uses a thin coral arrow and a warm paper highlight beneath the destination figure.')

bars=lambda n,h=False:root('chart-bar','bars'+(' h' if h else ''),''.join(f'<div class="bar {"on" if i==n-1 else "tone-4"}" style="--v:{25+i*60//max(1,n-1)}"><b>{25+i*60//max(1,n-1)}</b><span>{i+1}월</span></div>' for i in range(n)),style='--max:100',mn=('12x4' if n>6 else '6x3'))
el('chart-bar','''ROOT {display:flex;align-items:stretch;justify-content:space-around;gap:var(--gap);padding:var(--gap-lg) var(--gap) var(--gap-lg);border-bottom:var(--stroke) solid var(--line);background:repeating-linear-gradient(to top,var(--line) 0,var(--line) 1px,transparent 1px,transparent 25%);}
ROOT .bar {flex:1;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;min-width:0;}
ROOT .bar::before {content:"";width:65%;height:calc(var(--v)/var(--max)*100%);background:var(--tone-4);border-top:2px solid var(--tone-1);}
ROOT .bar.on::before {background:var(--accent);border-top-color:var(--accent-text);}
ROOT .bar.tone-1::before {background:var(--tone-1);border-top-color:var(--tone-1);}
ROOT .bar.tone-2::before {background:var(--tone-2);border-top-color:var(--tone-2);}
ROOT .bar.tone-3::before {background:var(--tone-3);border-top-color:var(--tone-3);}
ROOT .bar.tone-4::before {background:var(--tone-4);border-top-color:var(--tone-4);}
ROOT .bar.tone-5::before {background:var(--tone-5);border-top-color:var(--tone-5);}

ROOT .bar b {position:absolute;bottom:calc(var(--v)/var(--max)*100% + var(--gap-sm));font-size:var(--type-20);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--ink);}
ROOT .bar span {position:absolute;top:calc(100% + var(--gap-sm));font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);white-space:nowrap;}
ROOT.h {flex-direction:column;padding:var(--gap) var(--gap-lg);background:none;gap:var(--gap-sm);}
ROOT.h .bar {flex-direction:row;justify-content:flex-start;margin-left:calc(var(--pad)*2);margin-right:var(--pad);}
ROOT.h .bar::before {width:calc(var(--v)/var(--max)*100%);height:55%;border-top:0;border-left:2px solid var(--tone-1);}
ROOT.h .bar b {bottom:auto;left:calc(var(--v)/var(--max)*100% + var(--gap-sm));font-size:var(--type-18);}
ROOT.h .bar span {top:auto;left:calc(var(--pad)*-2);}
@container (max-width:640px) {ROOT {gap:var(--gap-sm);} ROOT .bar b,ROOT .bar span {font-size:var(--type-14);}}
''',{'three':bars(3),'twelve':bars(12),'horizontal':bars(5,True),'tones':root('chart-bar','bars',''.join(f'<div class="bar tone-{i}" style="--v:{30+i*10}"><b>{30+i*10}</b><span>유형 {i}</span></div>' for i in range(1,6)),style='--max:100',mn='8x3')},'Vertical and horizontal bars share thin analytical rules, soft blue history and a coral current value. Values remain real text and all lengths derive from numeric data.')

# Anchor-positioned CSS segments connect the actual point centres, including falling segments.
linecss='''ROOT {display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr) auto;padding:var(--gap-lg) var(--gap) var(--gap-sm);background:repeating-linear-gradient(to top,var(--line) 0,var(--line) 1px,transparent 1px,transparent 25%);isolation:isolate;anchor-scope:all;}
ROOT .pt {display:contents;}
ROOT .pt b {grid-row:1;position:relative;align-self:start;height:calc((100% - var(--gap-lg))*(1 - var(--v)/var(--max)));display:flex;flex-direction:column;justify-content:flex-end;font-size:var(--type-20);font-weight:var(--figure-weight);line-height:var(--figure-line);text-align:center;anchor-name:var(--rhetis-spectrum-self);}
ROOT .pt b::after {content:"";position:absolute;left:50%;bottom:-6px;width:10px;height:10px;transform:translateX(-50%);background:var(--accent);border:2px solid var(--page);border-radius:50%;z-index:2;}
ROOT .pt span {grid-row:2;text-align:center;border-top:var(--stroke) solid var(--line);padding-top:var(--gap-sm);font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);}
ROOT .pt::before,ROOT .pt::after {content:"";position:absolute;left:anchor(var(--rhetis-spectrum-prev) center);right:anchor(var(--rhetis-spectrum-self) center);pointer-events:none;z-index:-1;}
ROOT .pt::before {top:anchor(var(--rhetis-spectrum-prev) bottom);bottom:anchor(var(--rhetis-spectrum-self) bottom);background:linear-gradient(to top right,transparent calc(50% - 1px),var(--tone-1) calc(50% - 1px),var(--tone-1) calc(50% + 1px),transparent calc(50% + 1px));}
ROOT .pt::after {top:anchor(var(--rhetis-spectrum-self) bottom);bottom:anchor(var(--rhetis-spectrum-prev) bottom);background:linear-gradient(to bottom right,transparent calc(50% - 1px),var(--tone-1) calc(50% - 1px),var(--tone-1) calc(50% + 1px),transparent calc(50% + 1px));}
ROOT .pt:first-child::before,ROOT .pt:first-child::after {content:none;}
@container (max-width:640px) {ROOT .pt b,ROOT .pt span {font-size:var(--type-14);}}
'''
for i in range(1,13):linecss+=f'ROOT .pt:nth-child({i}) {{--rhetis-spectrum-self:--spectrum-point-{i};'+(f'--rhetis-spectrum-prev:--spectrum-point-{i-1};' if i>1 else '')+'}\n'
el('chart-line',linecss,{f'{n}-points':root('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b><span>{i+1}월</span></div>' for i,v in enumerate(([24,65,42] if n==3 else [18,24,39,31,48,55,47,62,73,68,80,90]))),style='--max:100',mn=('6x3' if n==3 else '12x4')) for n in [3,12]},'A real connected line chart uses CSS anchor-positioned segments between numeric data points. Coral points and dark-blue segments show rising and falling values over a quiet ruled field.')

donut=lambda v,n:f'<div class="donut" data-el="{ID}-chart-donut" style="--v:{v}"><p class="fig">{v}<small>%</small></p><p class="name">{n}</p></div>'
el('chart-donut','''ROOT.donuts {display:flex;align-items:center;justify-content:center;gap:var(--gap-lg);}
ROOT.donut {aspect-ratio:1;max-height:100%;justify-self:center;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:var(--gap-sm);border-radius:50%;background:conic-gradient(var(--accent) calc(var(--v)*1%),var(--surface-2) 0);padding:var(--pad);isolation:isolate;}
ROOT.donut::before {content:"";position:absolute;inset:var(--pad);background:var(--page);border-radius:50%;z-index:-1;border:var(--stroke) solid var(--line);}
ROOT.donuts > .donut {flex:1;min-width:0;}
ROOT .fig {font-size:var(--type-48);}
ROOT .name {font-size:var(--type-20);text-align:center;max-width:70%;}
@container (max-width:360px) {ROOT .fig {font-size:var(--type-28);} ROOT .fig small {font-size:var(--type-14);} ROOT .name {font-size:var(--type-14);}}
''',{'single':root('chart-donut','donut','<p class="fig">68<small>%</small></p><p class="name">목표 달성률</p>',style='--v:68',mn='4x4'),'four':root('chart-donut','donuts',''.join(donut(v,n) for v,n in zip([30,40,55,78],['신규 고객','재구매율','전환율','목표 달성'])),mn='12x4')},'A precise coral ring surrounds a large figure and a centred label. Its pale neutral remainder remains distinct in both modes; rows compare up to four shares.')
el('gauge','''ROOT {display:grid;grid-template-columns:1fr auto;align-content:center;gap:var(--gap-sm);padding:var(--pad);}
ROOT::before,ROOT::after {content:"";position:absolute;left:var(--pad);bottom:var(--pad);height:12px;border-radius:999px;}
ROOT::before {right:var(--pad);background:var(--surface-2);}
ROOT::after {width:calc((100% - var(--pad)*2)*var(--v)/100);background:var(--accent);}
ROOT .fig {font-size:var(--type-40);color:var(--tone-1);}
ROOT .name {align-self:center;}
@container (max-height:180px) {ROOT {align-content:start;} ROOT .fig {font-size:var(--type-28);}}
''',{'progress':root('gauge','meter','<p class="name">핵심 실행 과제 완료율</p><p class="fig">72%</p>',style='--v:72',mn='6x2'),'complete':root('gauge','meter','<p class="name">고객 인터뷰 목표 달성</p><p class="fig">100%</p>',style='--v:100',mn='6x2')},'A slim horizontal coral progress line sits beneath a left-aligned task and a right-aligned blue percentage.')

table=lambda rows,cols:'<table class="table"><thead><tr>'+''.join(f'<th class="{"pick" if c==cols-1 else ""}">{["핵심 지표","현재","목표","달성률","담당"][c]}</th>' for c in range(cols))+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td class="{"pick " if c==cols-1 else ""}{"num" if c else ""}">{([names[r%6],str(32+r*7),str(50+r*8),str(64+r*3)+"%","전략기획팀"])[c]}</td>' for c in range(cols))+'</tr>' for r in range(rows))+'</tbody></table>'
el('table','''ROOT {display:flex;align-items:center;border-top:3px solid var(--tone-1);border-bottom:var(--stroke) solid var(--line);}
ROOT .table {width:100%;height:100%;border-collapse:collapse;table-layout:fixed;font-size:var(--type-20);line-height:var(--body-line);}
ROOT th {background:var(--surface-2);font-weight:var(--name-weight);}
ROOT th,ROOT td {padding:var(--gap-sm);border-bottom:var(--stroke) solid var(--line);text-align:left;overflow-wrap:anywhere;}
ROOT .num {text-align:right;font-variant-numeric:tabular-nums;}
ROOT .pick {background:var(--accent-soft);font-weight:var(--name-weight);color:var(--ink);border-left:var(--stroke) solid var(--accent);}
ROOT th.pick {background:var(--accent);color:var(--accent-ink);}
@container (max-width:760px) {ROOT .table {font-size:var(--type-16);} ROOT th,ROOT td {padding:calc(var(--gap-sm)/2);}}
@container (max-height:340px) {ROOT .table {font-size:var(--type-14);}}
''',{'small':root('table','tablebox',table(3,3),mn='6x3'),'operations':root('table','tablebox',table(6,5),mn='10x5')},'A clean business table uses a strong blue header rule, light neutral column headings and a coral highlighted decision column. Numeric values align to the right.')
el('legend','''ROOT {display:flex;flex-wrap:wrap;align-content:center;align-items:center;justify-content:center;gap:var(--gap);}
ROOT .key {display:flex;align-items:center;gap:var(--gap-sm);font-size:var(--type-18);font-weight:var(--label-weight);line-height:var(--label-line);}
ROOT .key::before {content:"";width:14px;height:14px;border-radius:var(--radius-sm);background:var(--tone-1);border:var(--stroke) solid var(--line);}
'''+''.join(f'ROOT .key.tone-{i}::before {{background:var(--tone-{i});}}\n' for i in range(1,6))+'''@container (max-width:560px) {ROOT .key {font-size:var(--type-14);} ROOT {gap:var(--gap-sm);}}
''',{str(n):root('legend','legend',''.join(f'<span class="key tone-{i+1}">{names[i]}</span>' for i in range(n)),mn='6x2') for n in [3,5]},'Small square colour keys and carefully aligned labels supply a compact, orderly chart legend.')

stepbody=lambda n:''.join(f'<div class="step"><div class="mark">{i+1:02}</div><p class="name">{names[i]}</p><p class="note">{notes[i]}</p></div>' for i in range(n))
el('steps','''ROOT {display:flex;align-items:stretch;gap:var(--gap);}
ROOT .step {flex:1;min-width:0;display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);position:relative;padding:var(--pad);background:var(--surface);border:var(--stroke) solid var(--line);}
ROOT .step:not(:last-child)::after {content:"→";position:absolute;left:100%;top:50%;width:var(--gap);text-align:center;transform:translateY(-50%);color:var(--accent-text);font-size:var(--type-20);}
ROOT .mark {width:48px;height:48px;border-radius:50%;background:var(--tone-2);color:var(--tone-2-ink);border:var(--stroke) solid var(--line);}
ROOT.col {flex-direction:column;}
ROOT.col .step {display:grid;grid-template-columns:48px 1fr;align-items:center;column-gap:var(--gap);padding:var(--gap-sm) var(--pad);}
ROOT.col .mark {grid-row:span 2;}
ROOT.col .step:not(:last-child)::after {content:"↓";left:50%;top:100%;transform:translateX(-50%);height:var(--gap);}
@container (max-width:820px) {ROOT .step {padding:var(--gap-sm);} ROOT .name {font-size:var(--type-16);} ROOT .note {font-size:var(--type-14);}}
@container (max-height:300px) {ROOT .note {display:none;}}
''',{'two':root('steps','steps',stepbody(2),mn='6x3'),'six':root('steps','steps',stepbody(6),mn='12x4'),'vertical':root('steps','steps col',stepbody(4),mn='6x5')},'Numbered paper-yellow discs lead a sequence of ruled business cards. Coral arrows connect stages; the vertical form preserves the same mark and title rhythm.')
stopbody=lambda n:''.join(f'<div class="stop {"on" if i==n-1 else ""}"><p class="kick">2026.{i+1:02}</p><p class="name">{names[i%6]}</p><p class="note">{notes[i%6]}</p></div>' for i in range(n))
el('timeline','''ROOT {display:flex;align-items:center;gap:var(--gap);padding:var(--gap) 0;}
ROOT::before {content:"";position:absolute;left:0;right:0;top:50%;height:1px;background:var(--line);}
ROOT .stop {flex:1;min-width:0;position:relative;padding:var(--pad) var(--gap-sm);border:var(--stroke) solid var(--line);background:var(--page);display:flex;flex-direction:column;gap:var(--gap-sm);}
ROOT .stop::before {content:"";position:absolute;left:var(--gap-sm);top:-6px;width:10px;height:10px;border-radius:50%;background:var(--tone-1);border:2px solid var(--page);}
ROOT .stop.on {background:var(--accent-soft);border-color:var(--accent-text);}
ROOT.alt .stop:nth-child(even) {align-self:flex-end;}
ROOT.alt .stop:nth-child(odd) {align-self:flex-start;}
ROOT.col {flex-direction:column;align-items:stretch;padding-left:var(--pad);}
ROOT.col::before {left:calc(var(--gap-sm)/2);top:0;bottom:0;width:1px;height:auto;right:auto;}
ROOT.col .stop {display:grid;grid-template-columns:100px 1fr;align-content:center;column-gap:var(--gap);padding:var(--gap-sm);}
ROOT.col .stop::before {left:calc(var(--pad)*-1);top:50%;}
ROOT.col .kick {grid-row:span 2;align-self:center;}
@container (max-width:900px) {ROOT .name {font-size:var(--type-16);} ROOT .note {font-size:var(--type-12);} ROOT .kick {font-size:var(--type-12);}}
@container (max-height:300px) {ROOT .note {display:none;}}
''',{'three':root('timeline','track',stopbody(3),mn='8x3'),'eight':root('timeline','track alt',stopbody(8),mn='12x6'),'vertical':root('timeline','track col',stopbody(4),mn='6x5')},'A fine blue-grey time rail carries dated rectangular milestones, with a warm current stage. Alternating and vertical variants support both strategy and execution stories.')

def radial(n,kind):return root(kind,kind,'<div class="core">지속 가능한<br>성장</div>'+''.join((f'<div class="node">{names[i]}</div>' if kind=='cycle' else f'<div class="spoke"><div class="mark">{i+1:02}</div><p class="name">{names[i]}</p><p class="note">{notes[i]}</p></div>') for i in range(n)),mn='10x6')
for kind in ['cycle','hub']:
 member='node' if kind=='cycle' else 'spoke'
 css='''ROOT {display:block;isolation:isolate;}
ROOT .core {position:absolute;left:40%;top:39%;width:20%;height:22%;display:flex;align-items:center;justify-content:center;text-align:center;border-radius:50%;background:var(--tone-1);color:var(--tone-1-ink);font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);border:var(--stroke) solid var(--tone-1);}
ROOT MEMBER {position:absolute;width:28%;height:26%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);background:var(--surface);border:var(--stroke) solid var(--line);border-top:3px solid var(--accent);font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}
ROOT MEMBER::before {content:"";position:absolute;z-index:-1;left:50%;top:50%;width:65%;height:1px;background:var(--line);transform-origin:left;}
ROOT MEMBER:nth-child(2) {left:0;top:0;} ROOT MEMBER:nth-child(3) {right:0;top:0;} ROOT MEMBER:nth-child(4) {right:0;bottom:0;} ROOT MEMBER:nth-child(5) {left:0;bottom:0;} ROOT MEMBER:nth-child(6) {left:0;top:37%;} ROOT MEMBER:nth-child(7) {right:0;top:37%;}
ROOT MEMBER:nth-child(2)::before {transform:rotate(35deg);width:130%;}
ROOT MEMBER:nth-child(3)::before {transform:rotate(145deg);width:130%;}
ROOT MEMBER:nth-child(4)::before {transform:rotate(215deg);width:130%;}
ROOT MEMBER:nth-child(5)::before {transform:rotate(325deg);width:130%;}
ROOT MEMBER:nth-child(6)::before {width:120%;}
ROOT MEMBER:nth-child(7)::before {transform:rotate(180deg);width:120%;}
ROOT:has(MEMBER:nth-child(4):last-child) MEMBER:nth-child(2) {left:36%;top:0;}
ROOT:has(MEMBER:nth-child(4):last-child) MEMBER:nth-child(2)::before {transform:rotate(90deg);width:80%;}
ROOT:has(MEMBER:nth-child(4):last-child) MEMBER:nth-child(3) {right:0;top:auto;bottom:0;}
ROOT:has(MEMBER:nth-child(4):last-child) MEMBER:nth-child(3)::before {transform:rotate(215deg);}
ROOT:has(MEMBER:nth-child(4):last-child) MEMBER:nth-child(4) {left:0;right:auto;bottom:0;}
ROOT:has(MEMBER:nth-child(4):last-child) MEMBER:nth-child(4)::before {transform:rotate(325deg);}
ROOT .mark {font-size:var(--type-16);}
ROOT .name {font-size:var(--type-20);}
ROOT .note {font-size:var(--type-14);}
@container (max-width:800px) {ROOT MEMBER,ROOT .core {font-size:var(--type-18);} ROOT .name {font-size:var(--type-16);} ROOT .note {display:none;}}
'''.replace('MEMBER','.'+member)
 if kind=='cycle':css+='''ROOT::before {content:"";position:absolute;left:23%;right:23%;top:14%;bottom:14%;border:2px solid var(--line);border-radius:50%;z-index:-1;}
ROOT .node::after {content:"→";position:absolute;right:calc(var(--gap)*-1);color:var(--accent-text);font-size:var(--type-24);}
'''
 el(kind,css,{str(n):radial(n,kind) for n in [3,4,5,6]},'A central deep-blue disc anchors '+('a continuing cycle of warm-edged rectangular actions, with a circular rail and directional arrows.' if kind=='cycle' else 'a network of ruled spoke cards, each with a numbered mark, title and explanation. Thin connectors make the relationship explicit.'))

el('funnel','''ROOT {display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);}
ROOT .stage {width:calc(var(--v)*1%);flex:1;min-height:0;display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);padding:var(--gap-sm) var(--pad);background:var(--tone-4);border:var(--stroke) solid var(--line);clip-path:polygon(0 0,100% 0,96% 100%,4% 100%);}
ROOT .stage:first-child {background:var(--tone-1);color:var(--tone-1-ink);}
ROOT .stage:last-child {background:var(--accent);color:var(--accent-ink);}
ROOT .fig {font-size:var(--type-32);}
ROOT .name {font-size:var(--type-22);}
@container (max-width:640px) {ROOT .name {font-size:var(--type-16);} ROOT .fig {font-size:var(--type-24);}}
''',{str(n):root('funnel','funnel',''.join(f'<div class="stage" style="--v:{100-i*9}"><p class="name">{["방문 고객","관심 고객","상담 신청","제품 경험","구매 전환","핵심 고객"][i]}</p><p class="fig">{[100,82,65,48,32,21][i]}%</p></div>' for i in range(n)),mn=('8x4' if n==3 else '8x6')) for n in [3,4,5,6]},'A measured funnel uses shallow trapezoids, cool intermediate stages and a warm conversion endpoint. Every width is controlled by its stage value.')
el('pyramid','''ROOT {display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);}
ROOT .level {flex:1;min-height:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);background:var(--surface-2);border-bottom:var(--stroke) solid var(--line);clip-path:polygon(8% 0,92% 0,100% 100%,0 100%);padding:var(--gap-sm) var(--pad);text-align:center;width:100%;}
ROOT .level:nth-child(1) {width:38%;background:var(--accent);color:var(--accent-ink);}
ROOT .level:nth-child(2) {width:54%;background:var(--tone-2);color:var(--tone-2-ink);}
ROOT .level:nth-child(3) {width:70%;}
ROOT .level:nth-child(4) {width:86%;}
ROOT .level .name {font-size:var(--type-22);}
ROOT .level:first-child .note {color:var(--accent-ink);}
ROOT .level:nth-child(2) .note {color:var(--tone-2-ink);}
@container (max-width:760px) {ROOT .level .name {font-size:var(--type-16);} ROOT .note {font-size:var(--type-12);}}
@container (max-height:350px) {ROOT .note {display:none;}}
''',{str(n):root('pyramid','pyramid',''.join(f'<div class="level"><p class="name">{["성장 비전","핵심 전략","실행 과제","운영 체계","공통 기반"][i]}</p><p class="note">{["고객과 함께 만드는 미래","선택과 집중으로 방향 설정","작은 단위로 빠르게 검증","일관된 협업 기준 마련","데이터와 조직 역량 확보"][i]}</p></div>' for i in range(n)),mn='8x5') for n in [3,4,5]},'A stepped pyramid widens through pale structural levels to a coral strategic peak. Each trapezoid retains live centred labels and supporting text.')
el('matrix','''ROOT {display:grid;grid-template-columns:var(--pad) 1fr 1fr;grid-template-rows:1fr 1fr var(--pad);gap:var(--gap-sm);padding:var(--pad);}
ROOT .cell {padding:var(--pad);display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);background:var(--surface);border:var(--stroke) solid var(--line);font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}
ROOT .cell:nth-of-type(3) {grid-area:1/2;} ROOT .cell:nth-of-type(4) {grid-area:1/3;} ROOT .cell:nth-of-type(5) {grid-area:2/2;} ROOT .cell:nth-of-type(6) {grid-area:2/3;}
ROOT .cell.on {background:var(--accent-soft);border-color:var(--accent-text);border-top:3px solid var(--accent);}
ROOT .axis-x {grid-area:3/2/4/4;display:flex;justify-content:space-between;align-items:center;font-size:var(--type-14);font-weight:var(--label-weight);}
ROOT .axis-y {grid-area:1/1/3/2;display:flex;flex-direction:column;justify-content:space-between;align-items:center;font-size:var(--type-14);font-weight:var(--label-weight);writing-mode:vertical-rl;}
@container (max-width:640px) {ROOT .cell {font-size:var(--type-18);padding:var(--gap-sm);}}
''',{name:root('matrix','matrix',f'<div class="axis-x"><span>실행 난이도 낮음</span><span>실행 난이도 높음</span></div><div class="axis-y"><span>기대 효과 낮음</span><span>기대 효과 높음</span></div>'+''.join(f'<div class="cell {"on" if i==pick else ""}">{s}</div>' for i,s in enumerate(['빠른 성과 확보','전략적 투자','운영 효율 개선','장기 검토 과제'])),mn='8x4') for name,pick in [('priority',0),('investment',1)]},'Four quiet quadrants sit inside carefully separated horizontal and vertical axis labels. A single coral-edged warm cell identifies the current strategic choice.')
el('venn','''ROOT {display:flex;align-items:center;justify-content:center;isolation:isolate;padding:var(--pad);}
ROOT .set {width:40%;aspect-ratio:1;border-radius:50%;background:color-mix(in srgb,var(--tone-2) 65%,transparent);border:var(--stroke) solid var(--line);display:flex;align-items:center;justify-content:center;position:relative;padding:var(--pad);}
ROOT .set + .set {margin-left:-12%;}
ROOT .set {color:var(--tone-2-ink);}
ROOT .set.on {background:color-mix(in srgb,var(--accent) 45%,transparent);color:var(--ink);}
ROOT .name {text-align:center;font-size:var(--type-28);}
ROOT .core {position:absolute;left:44%;top:44%;width:12%;height:12%;background:var(--page);display:flex;align-items:center;justify-content:center;text-align:center;font-size:var(--type-16);font-weight:var(--label-weight);border:var(--stroke) solid var(--line);border-radius:var(--radius-sm);}
ROOT:has(.set:nth-child(3)) .set {width:34%;}
ROOT:has(.set:nth-child(3)) .set:nth-child(2) {transform:translateY(-18%);}
@container (max-width:760px) {ROOT .name {font-size:var(--type-18);} ROOT .core {font-size:var(--type-12);}}
''',{str(n):root('venn','venn',''.join(f'<div class="set {"on" if i==n-1 else ""}"><p class="name">{["고객 가치","실행 역량","성장 기회"][i]}</p></div>' for i in range(n))+'<div class="core">핵심<br>전략</div>',mn='8x5') for n in [2,3]},'Translucent yellow and coral circles express overlap while retaining thin analytic outlines. A small white central label identifies the shared strategic area.')
org=lambda n:root('hierarchy','org','<div class="root">사업전략실</div>'+''.join(f'<div class="branch"><div class="node">{["고객경험팀","제품기획팀","데이터분석팀","운영혁신팀"][i]}</div>'+''.join(f'<div class="leaf">{["기획 및 실행","성과 분석","현장 운영"][j]}</div>' for j in range(2+(i%2)))+'</div>' for i in range(n)),mn='10x5')
el('hierarchy','''ROOT {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-flow:column;grid-template-rows:auto 1fr;gap:var(--gap-lg);padding:var(--pad);}
ROOT:has(.branch:nth-child(4)) {grid-template-columns:repeat(3,minmax(0,1fr));}
ROOT:has(.branch:nth-child(5)) {grid-template-columns:repeat(4,minmax(0,1fr));}
ROOT .root {grid-row:1;grid-column:1/-1;justify-self:center;min-width:30%;padding:var(--gap-sm) var(--pad);text-align:center;background:var(--tone-1);color:var(--tone-1-ink);font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);position:relative;}
ROOT .root::after {content:"";position:absolute;left:50%;top:100%;height:var(--gap-lg);width:1px;background:var(--line);}
ROOT .branch {grid-row:2;display:flex;flex-direction:column;gap:var(--gap-sm);position:relative;padding-top:var(--gap);}
ROOT .branch::before {content:"";position:absolute;top:0;left:calc(var(--gap-lg)*-.5);right:calc(var(--gap-lg)*-.5);height:var(--gap);border-top:var(--stroke) solid var(--line);background:linear-gradient(to right,transparent calc(50% - .5px),var(--line) calc(50% - .5px),var(--line) calc(50% + .5px),transparent calc(50% + .5px));}
ROOT .node {padding:var(--gap-sm);background:var(--tone-2);color:var(--tone-2-ink);text-align:center;border:var(--stroke) solid var(--line);font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line);}
ROOT .leaf {padding:var(--gap-sm);background:var(--surface);border-left:var(--stroke) solid var(--line);font-size:var(--type-18);line-height:var(--body-line);}
@container (max-width:760px) {ROOT .node,ROOT .leaf {font-size:var(--type-14);} ROOT .root {font-size:var(--type-20);}}
''',{str(n):org(n) for n in [2,3,4]},'A deep-blue leadership node connects through a clean ruled tree to pale-yellow teams and neutral leaf roles. Connector geometry is drawn by CSS rather than image assets.')
el('flowchart','''ROOT {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(3,minmax(0,1fr));gap:var(--gap-lg);padding:var(--pad);}
ROOT .node {position:relative;display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--gap-sm);border:var(--stroke) solid var(--line);background:var(--surface);font-size:var(--type-22);font-weight:var(--name-weight);line-height:var(--name-line);}
ROOT .start,ROOT .end {border-radius:999px;background:var(--tone-1);color:var(--tone-1-ink);}
ROOT .ask {background:var(--tone-2);color:var(--tone-2-ink);border-color:var(--accent-text);}
ROOT .node::after {position:absolute;color:var(--accent-text);font-size:var(--type-28);font-weight:var(--label-weight);}
ROOT .to-r::after {content:"→";left:100%;width:var(--gap-lg);}
ROOT .to-l::after {content:"←";right:100%;width:var(--gap-lg);}
ROOT .to-d::after {content:"↓";top:100%;height:var(--gap-lg);}
ROOT .to-u::after {content:"↑";bottom:100%;height:var(--gap-lg);}
@container (max-width:760px) {ROOT .node {font-size:var(--type-16);} ROOT .node::after {font-size:var(--type-22);}}
''',{'approval':root('flowchart','flowchart','<div class="node start to-r" style="grid-column:1;grid-row:1">요청 접수</div><div class="node ask to-r" style="grid-column:2;grid-row:1">기준 충족?</div><div class="node to-d" style="grid-column:3;grid-row:1">실행 계획 수립</div><div class="node to-l" style="grid-column:3;grid-row:2">담당자 검토</div><div class="node to-d" style="grid-column:2;grid-row:2">실행 및 확인</div><div class="node end" style="grid-column:2;grid-row:3">결과 공유</div>',mn='10x5'),'feedback':root('flowchart','flowchart','<div class="node start to-d" style="grid-column:1;grid-row:1">고객 의견 수집</div><div class="node to-r" style="grid-column:1;grid-row:2">문제 정의</div><div class="node ask to-r" style="grid-column:2;grid-row:2">검증 결과 확인</div><div class="node end" style="grid-column:3;grid-row:2">다음 실행 결정</div>',mn='10x5')},'A gridded flowchart places capsule endpoints, yellow decision nodes and neutral actions on an explicit three-by-three grid. Directional arrows are CSS-generated and remain attached to the correct node.')
el('architecture','''ROOT {display:flex;flex-direction:column;gap:var(--gap-sm);justify-content:center;}
ROOT .layer {flex:1;min-height:0;display:flex;align-items:center;gap:var(--gap);padding:var(--gap-sm) var(--pad);border:var(--stroke) solid var(--line);background:var(--surface);}
ROOT .layer:first-child {border-top:3px solid var(--accent);}
ROOT .layer .name {width:22%;flex:none;color:var(--tone-1);font-size:var(--type-22);}
ROOT .chip {flex:1;display:flex;align-items:center;justify-content:center;align-self:stretch;text-align:center;padding:var(--gap-sm);border:var(--stroke) solid var(--line);border-radius:var(--radius-sm);font-size:var(--type-18);font-weight:var(--label-weight);line-height:var(--label-line);background:var(--page);}
ROOT .layer:last-child {background:var(--tone-4);}
@container (max-width:760px) {ROOT .layer {gap:var(--gap-sm);padding:var(--gap-sm);} ROOT .layer .name {font-size:var(--type-16);} ROOT .chip {font-size:var(--type-14);}}
''',{str(n):root('architecture','arch',''.join(f'<div class="layer"><p class="name">{["고객 접점","서비스 경험","업무 플랫폼","데이터 기반","운영 인프라"][i]}</p><div class="chip">{["웹 서비스","사용자 경험","실행 관리","통합 분석","보안 관리"][i]}</div><div class="chip">{["모바일 앱","개인화 지원","협업 도구","공통 지표","지속 운영"][i]}</div></div>' for i in range(n)),mn=('8x3' if n==2 else '10x5')) for n in [2,3,4,5]},'Horizontal architecture layers align a blue category label with optically centred outlined chips. The coral top rule and blue foundation layer indicate the direction from experience to infrastructure.')
el('versus','''ROOT {display:grid;grid-template-columns:1fr auto 1fr;gap:var(--gap);align-items:stretch;}
ROOT .side {border:var(--stroke) solid var(--line);padding:var(--pad);background:var(--surface);display:flex;flex-direction:column;justify-content:center;gap:var(--gap);min-width:0;}
ROOT .side.on {background:var(--accent-soft);border-top:3px solid var(--accent);}
ROOT .side > .name {padding-bottom:var(--gap-sm);border-bottom:var(--stroke) solid var(--line);}
ROOT .vs {align-self:center;font-family:var(--font-display);font-size:var(--type-28);font-weight:var(--figure-weight);color:var(--mute);}
ROOT .list {flex:1;container-type:normal;}
@container (max-width:760px) {ROOT .side {padding:var(--gap-sm);} ROOT .vs {font-size:var(--type-20);}}
''',{str(n):root('versus','versus',f'<div class="side"><p class="name">현재의 운영 방식</p><div class="list" data-el="{ID}-list">'+listbody(n)+'</div></div><b class="vs">VS</b>'+f'<div class="side on"><p class="name">다음 단계의 실행 체계</p><div class="list check" data-el="{ID}-list">'+listbody(n)+'</div></div>',mn='10x5') for n in [2,4]},'Two clear comparison panels are separated by a modest VS mark. The proposed approach receives the warm coral emphasis while nested semantic lists retain their independent collection scope.')
plan=lambda i,n:f'<div class="plan {"on" if i==n-1 else ""}" data-el="{ID}-pricing"><p class="name">{["시작하기","함께 성장","조직 확장","맞춤 도입"][i]}</p><div class="price"><span class="fig">{["0","29","79","문의"][i]}</span><small>{"만원 / 월" if i in [1,2] else ""}</small></div><div class="list check" data-el="{ID}-list">'+''.join(f'<div class="item"><p class="name">{s}</p></div>' for s in ['기본 분석 제공','팀 협업 지원','실행 결과 공유'][:2+(i%2)])+'</div></div>'
el('pricing','''ROOT.plans {display:flex;gap:var(--gap);}
ROOT.plan {flex:1;display:flex;flex-direction:column;justify-content:center;gap:var(--gap);border:var(--stroke) solid var(--line);padding:var(--pad);background:var(--page);}
ROOT.plan.on {border-top:4px solid var(--accent);background:var(--accent-soft);}
ROOT .price {display:flex;align-items:baseline;flex-wrap:wrap;gap:calc(var(--gap-sm)/2);padding-bottom:var(--gap);border-bottom:var(--stroke) solid var(--line);}
ROOT .price .fig {font-size:var(--type-52);color:var(--tone-1);}
ROOT .price small {font-size:var(--type-16);font-weight:var(--label-weight);color:var(--mute);}
ROOT .list {flex:1;container-type:normal;gap:var(--gap-sm);}
ROOT .list .name {font-size:var(--type-18);}
ROOT .tag {font-size:var(--type-14);}
@container (max-width:850px) {ROOT.plan {padding:var(--gap-sm);} ROOT .price .fig {font-size:var(--type-36);} ROOT .list .name {font-size:var(--type-14);}}
''',{str(n):root('pricing','plans',''.join(plan(i,n) for i in range(n)),mn=('6x4' if n==1 else '12x5')) for n in [1,2,3,4]},'Pricing panels use clear plan names, strongly tracked blue prices and real nested check lists. A coral top border and warm field mark the recommended plan without changing its alignment.')
person=lambda i:f'<div class="person" data-el="{ID}-person"><div class="seat avatar" data-ph="{i+1:02}"></div><p class="name">{["김민지","박준호","이서연","최도윤","정하린","한지우"][i]}</p><p class="note">{["고객경험 총괄","제품전략 리드","데이터 분석가","운영혁신 매니저","서비스 디자이너","사업개발 리드"][i]}</p></div>'
el('person','''ROOT.people {display:flex;align-items:stretch;gap:var(--gap);}
ROOT.person {flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:var(--gap-sm);padding:var(--pad);border-bottom:var(--stroke) solid var(--line);}
ROOT .seat {width:120px;height:120px;flex:none;border:var(--stroke) solid var(--line);}
ROOT .name {margin-top:var(--gap-sm);}
ROOT .list {container-type:normal;text-align:left;}
@container (max-width:850px) {ROOT .seat {width:80px;height:80px;} ROOT .name {font-size:var(--type-18);} ROOT .note {font-size:var(--type-14);} ROOT.person {padding:var(--gap-sm);}}
''',{str(n):root('person','people',''.join(person(i) for i in range(n)),mn=('4x4' if n==1 else '12x4')) for n in [1,3,6]},'Centred profile blocks use pale grey avatar seats, confident names and quieter role labels, linked by a baseline rule rather than heavy cards.')
el('logo-group','''ROOT {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));align-content:center;gap:var(--gap);}
ROOT .seat.logo {width:100%;height:100%;min-height:64px;border:var(--stroke) solid var(--line);background:var(--surface);}
ROOT:has(.seat:nth-child(7)) {grid-template-columns:repeat(4,minmax(0,1fr));}
@container (max-width:640px) {ROOT {gap:var(--gap-sm);} ROOT .seat.logo {min-height:48px;}}
''',{str(n):root('logo-group','logos',''.join(f'<div class="seat logo" data-ph="{i+1:02}"></div>' for i in range(n)),mn=('6x2' if n==3 else '10x5')) for n in [3,6,12]},'An orderly grid of thin-outlined light grey logo seats uses generous consistent spacing. No brand mark or external image is embedded.')
el('image-frame','''ROOT {display:flex;padding:var(--gap-sm);border:var(--stroke) solid var(--line);background:var(--page);position:relative;}
ROOT::before {content:"";position:absolute;left:var(--gap);top:-1px;width:48px;height:5px;background:var(--accent);}
ROOT .seat {flex:1;width:100%;height:100%;background:var(--surface-2);}
@container (max-width:480px) {ROOT {padding:calc(var(--gap-sm)/2);}}
''',{'landscape':root('image-frame','frame','<div class="seat" data-ph="01"></div>',mn='6x3'),'portrait':root('image-frame','frame','<div class="seat portrait" data-ph="02"></div>',mn='4x5')},'A fine rectangular picture frame and a short coral edge accent surround one uniformly grey image seat. The frame remains a reusable UI component without embedded reference imagery.')
agenda=lambda n:root('agenda','agenda',''.join(f'<div class="entry {"on" if i==1 else ""}"><div class="mark">{i+1:02}</div><p class="name">{["배경과 추진 방향","고객과 시장의 변화","핵심 전략과 실행 과제","성과 지표와 운영 체계","추진 일정 및 역할","리스크와 대응 계획","기대 효과","다음 단계"][i]}</p><p class="note">{notes[i%6]}</p></div>' for i in range(n)),mn=('6x3' if n==2 else '10x6'))
el('agenda','''ROOT {display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);}
ROOT .entry {display:grid;grid-template-columns:64px 1fr;column-gap:var(--gap);align-content:center;position:relative;padding:var(--gap-sm) var(--pad);border-bottom:var(--stroke) solid var(--line);flex:1;min-height:0;}
ROOT .entry.on {background:var(--accent-soft);border-left:3px solid var(--accent);}
ROOT .mark {grid-row:span 2;font-family:var(--font-display);font-size:var(--type-32);font-weight:var(--figure-weight);color:var(--tone-1);border-right:var(--stroke) solid var(--line);}
ROOT .name {font-size:var(--type-24);}
ROOT .note {margin-top:calc(var(--gap-sm)/2);}
@container (max-width:760px) {ROOT .entry {grid-template-columns:40px 1fr;gap:var(--gap-sm);} ROOT .name {font-size:var(--type-18);} ROOT .mark {font-size:var(--type-24);}}
@container (max-height:420px) {ROOT .note {display:none;} ROOT .name {font-size:var(--type-18);} ROOT .mark {font-size:var(--type-24);}}
''',{str(n):agenda(n) for n in [2,4,8]},'An editorial contents list pairs tightly tracked blue section numbers with strong titles and quiet explanatory lines. The active entry receives a pale coral field and a fine left marker.')
print('Created',len(list((C/'elements').iterdir())),'elements;',len(list(C.glob('**/fixtures/*.html'))),'fixtures')
