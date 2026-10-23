from pathlib import Path
import json,re
C=Path('/workspace/work/deliverables/undertow');R=Path('/workspace/work/deliverables/undertow-review');P=R/'reassembled'
MARK='/* UNDERTOW PRECISE COMPOSITIONS */'
def append(path,s):
 old=path.read_text().split(MARK)[0].rstrip();path.write_text(old+'\n\n'+MARK+'\n'+s+'\n')
def meta(folder,defaults):
 p=C/'elements'/folder/'element.json';d=json.loads(p.read_text());d['tokenDefaults'].update(defaults);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
used={'headline':'headline','prose':'prose','card':'card','agenda':'agenda','architecture':'arch','concentric':'orbit','list':'list','steps':'steps','callout':'callout','hub':'hub','chart-area':'areas','metric':'stat','positioning':'posmap','person':'people','chart-donut':'donut','chart-bar':'bars'}
for f,cl in used.items():
 p=C/'elements'/f/'element.css';old=p.read_text().split(MARK)[0].rstrip();p.write_text(old+'\n')
 meta(f,{'--undertow-x':'0px','--undertow-y':'0px','--undertow-width':'100%','--undertow-height':'100%','--undertow-layout':'standard'})
 s=f'.{cl}[data-el="undertow-{f}"] {{position:relative;left:var(--undertow-x);top:var(--undertow-y);width:var(--undertow-width);height:var(--undertow-height);align-self:start;justify-self:start;}}'
 append(p,s)
def add(f,s):
 p=C/'elements'/f/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
# Generic placement extensions preserve the 12x6 grid and are optional on all fixtures.
fd=C/'foundation/foundation.json';d=json.loads(fd.read_text());d['tokenDefaults'].update({'--undertow-page-mode':'standard','--undertow-rail-size':'86px'});fd.write_text(json.dumps(d,indent=2)+'\n')
append(C/'foundation/foundation.css','''
.slide[style*="--undertow-page-mode:precise"] .page {padding:0;display:block;gap:0;}
.slide[style*="--undertow-page-mode:precise"] .body {position:absolute;inset:0;gap:0;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));}
.slide[style*="--undertow-page-mode:precise"] .page::after {width:var(--undertow-rail-size);background:var(--n-2);z-index:10;}
.slide[style*="--undertow-page-mode:precise"] .head {position:absolute;left:50px;top:85px;width:1094px;z-index:3;}
.slide[style*="--undertow-page-mode:precise"] .head .kicker {height:26px;min-width:136px;display:table;align-content:center;padding:calc(var(--gap-sm)/3) var(--gap);font-size:var(--type-14);margin:0 auto var(--gap-sm);background:var(--ink);color:var(--page);line-height:var(--label-line);}
.slide[style*="--undertow-page-mode:precise"] .head .title {font-size:var(--type-40);line-height:var(--title-line);font-weight:var(--title-weight);}
.slide[style*="--undertow-page-mode:precise"] .top {left:60px;right:132px;top:34px;font-size:var(--type-14);z-index:20;font-weight:var(--label-weight);}
.slide[style*="--undertow-page-mode:precise"] .top>b {font-size:var(--type-16);color:var(--n-7);font-weight:var(--figure-weight);}
.slide[style*="--undertow-page-mode:precise"] .top>b::before {content:"";display:inline-block;width:20px;height:15px;background:currentColor;clip-path:polygon(0 90%,30% 0,48% 0,23% 100%,45% 100%,75% 0,94% 0,68% 100%,100% 80%,100% 100%);margin-right:calc(var(--gap-sm)/4);}
.slide[style*="--undertow-page-mode:precise"] .rail {left:1194px;right:auto;top:0;bottom:0;width:86px;align-items:center;justify-content:center;color:var(--ink);font-size:var(--type-12);z-index:20;}
.slide[style*="--undertow-page-mode:precise"] .rail>span {position:absolute;bottom:36px;}
.slide[style*="--undertow-page-mode:precise"] .seat.back {position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto;background:var(--n-2);}
.slide[style*="--undertow-page-mode:precise"] .seat.back::after {content:none;}
.slide.cover[style*="--undertow-page-mode:precise"] .page::after {display:none;}
.slide.cover[style*="--undertow-page-mode:precise"] .lockup.at-top-left {left:94px;top:92px;max-width:90%;}
.slide.cover[style*="--undertow-page-mode:precise"] .lockup .kicker {font-size:var(--type-30);margin:0 0 var(--gap-sm);line-height:var(--lead-line);}
.slide.cover[style*="--undertow-page-mode:precise"] .title {font-size:var(--type-108);font-weight:var(--weight-display);line-height:var(--undertow-cover-line);letter-spacing:var(--tracking-display);}
.slide.cover[style*="--undertow-page-mode:precise"] .title b {color:var(--a1-8);}
.slide.cover[style*="--undertow-page-mode:precise"] .meta {height:118px;top:602px;bottom:auto;padding:var(--gap-lg) 54px var(--gap-lg) 94px;}
.slide.cover[style*="--undertow-page-mode:precise"] .foot {position:relative;gap:var(--gap-lg);font-size:var(--type-14);}
.slide.cover[style*="--undertow-page-mode:precise"] .foot>p {border-left:2px solid;padding-left:var(--gap-sm);line-height:var(--body-line);}
.slide.cover[style*="--undertow-page-mode:precise"] .foot>p:nth-child(2) {margin-left:var(--gap-lg);}
.slide.cover[style*="--undertow-page-mode:precise"] .foot>b {margin-left:auto;font-size:var(--type-20);font-weight:var(--figure-weight);}
.slide.cover[style*="--undertow-page-mode:precise"] .deck {position:absolute;right:54px;top:68px;font-size:var(--type-14);}
''')
# Shared token extension for source's compressed title leading.
p=C/'kit/kit.json';d=json.loads(p.read_text());d['extensions']['--undertow-cover-line']='number';p.write_text(json.dumps(d,indent=2)+'\n')
p=C/'kit/css/tokens.css';append(p,'.slide {--undertow-cover-line:.92;}')
# Composition-specific treatments are semantic APIs rather than per-page rules.
add('headline','''
.headline[data-el="undertow-headline"][style*="--undertow-layout:contents"] {background:var(--n-2);padding:0;display:flex;flex-direction:column;justify-content:flex-start;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:contents"] .kick {font-size:var(--type-22);position:absolute;left:87px;top:83px;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:contents"] h2 {font-size:var(--type-76);font-weight:var(--weight-body);line-height:var(--figure-line);position:absolute;left:87px;top:116px;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:contents"] h2 b {color:var(--a1-8);font-weight:var(--figure-weight);}
.headline[data-el="undertow-headline"][style*="--undertow-layout:vision"] {padding:0;background:none;display:block;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:vision"] h2 {font-size:var(--type-56);line-height:var(--lead-line);font-weight:var(--figure-weight);}
.headline[data-el="undertow-headline"][style*="--undertow-layout:problem"] {background:var(--n-2);padding:119px 30px 0 83px;display:block;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:problem"] h2 {font-size:var(--type-36);line-height:var(--lead-line);font-weight:var(--figure-weight);}
.headline[data-el="undertow-headline"][style*="--undertow-layout:problem"] .note {font-size:var(--type-18);color:var(--a1-8);margin-top:var(--gap);line-height:var(--lead-line);max-width:359px;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:market"] {padding:0;background:none;text-align:center;display:block;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:market"] h2 {font-size:var(--type-30);font-weight:var(--figure-weight);line-height:var(--lead-line);color:var(--n-8);}
.headline[data-el="undertow-headline"][style*="--undertow-layout:market"] h2 b {color:var(--a1-8);}
.headline[data-el="undertow-headline"][style*="--undertow-layout:market"] .note {font-size:var(--type-14);margin-top:var(--gap-sm);text-align:right;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:competition"] {padding:0;display:block;background:none;text-align:center;}
.headline[data-el="undertow-headline"][style*="--undertow-layout:competition"] h2 {font-size:var(--type-28);font-weight:var(--name-weight);color:var(--a1-8);}
.headline[data-el="undertow-headline"][style*="--undertow-layout:competition"] .note {font-size:var(--type-18);line-height:var(--lead-line);margin:var(--gap) var(--gap-sm) 0;}
''')
add('prose','''
.prose[data-el="undertow-prose"][style*="--undertow-layout:vision"] {padding:0;background:none;border-top:2px solid var(--n-1);border-bottom:var(--stroke) solid var(--n-1);}
.prose[data-el="undertow-prose"][style*="--undertow-layout:vision"] p {font-size:var(--type-16);line-height:var(--body-line);padding-top:var(--gap-lg);max-width:415px;}
.prose[data-el="undertow-prose"][style*="--undertow-layout:axis"] {padding:0;background:none;display:block;}
.prose[data-el="undertow-prose"][style*="--undertow-layout:axis"] p {font-size:var(--type-14);line-height:var(--label-line);}
.prose[data-el="undertow-prose"][style*="--undertow-layout:forecast"] {padding:0;background:none;text-align:center;}
.prose[data-el="undertow-prose"][style*="--undertow-layout:forecast"] p {font-size:var(--type-22);line-height:var(--title-line);}
''')
add('agenda','''
.agenda[data-el="undertow-agenda"][style*="--undertow-layout:contents"] {display:flex;flex-direction:column;gap:10px;padding:0;background:none;}
.agenda[data-el="undertow-agenda"][style*="--undertow-layout:contents"] .entry {height:56px;min-height:56px;flex:none;display:grid;grid-template-columns:32px auto 1fr;gap:var(--gap-sm);padding:calc(var(--gap-sm)*.75);background:var(--n-1);border:0;align-items:center;}
.agenda[data-el="undertow-agenda"][style*="--undertow-layout:contents"] .entry .mark {height:32px;width:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--ink);color:var(--page);font-size:var(--type-14);padding:0;}
.agenda[data-el="undertow-agenda"][style*="--undertow-layout:contents"] .entry .name {font-size:var(--type-20);white-space:nowrap;}
.agenda[data-el="undertow-agenda"][style*="--undertow-layout:contents"] .entry .note {font-size:var(--type-14);text-align:right;padding-right:var(--gap-sm);margin:0;}
''')
add('architecture','''
.arch[data-el="undertow-architecture"][style*="--undertow-layout:vision"] {display:flex;flex-direction:column;gap:9px;padding:0;}
.arch[data-el="undertow-architecture"][style*="--undertow-layout:vision"] .layer {height:101px;min-height:101px;display:grid;grid-template-columns:143px 1fr;gap:0;padding:0;border:0;background:var(--n-1);}
.arch[data-el="undertow-architecture"][style*="--undertow-layout:vision"] .layer .name {align-self:stretch;display:flex;align-items:center;justify-content:center;background:var(--a1);color:var(--a1-on);font-size:var(--type-30);margin:0;}
.arch[data-el="undertow-architecture"][style*="--undertow-layout:vision"] .chip {display:flex;align-items:center;justify-content:center;text-align:center;border:0;border-radius:0;background:none;font-size:var(--type-22);padding:var(--gap-sm);line-height:var(--lead-line);}
''')
add('card','''
.card[data-el="undertow-card"][style*="--undertow-layout:"] .parts {width:100%;height:100%;}
.card[data-el="undertow-card"][style*="--undertow-layout:problem"] {padding:15px;background:var(--n-1);border:0;}
.card[data-el="undertow-card"][style*="--undertow-layout:problem"] .parts {display:grid;grid-template-columns:143px 1fr;grid-template-rows:1fr 1fr;column-gap:var(--gap);row-gap:0;align-items:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:problem"] .mark {grid-column:1;grid-row:1 / span 2;width:143px;height:143px;border-radius:0;background:var(--a1);color:var(--a1-on);margin:0;display:flex;align-items:center;justify-content:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:problem"] .mark .icon {width:78px;height:78px;}
.card[data-el="undertow-card"][style*="--undertow-layout:problem"] .name {grid-column:2;grid-row:1;font-size:var(--type-22);text-align:center;align-self:center;color:var(--n-8);}
.card[data-el="undertow-card"][style*="--undertow-layout:problem"] .note {grid-column:2;grid-row:2;font-size:var(--type-16);text-align:center;line-height:var(--body-line);align-self:start;color:var(--n-7);margin:0;padding:0 var(--gap-sm);}
.card[data-el="undertow-card"][style*="--undertow-layout:solution"] {padding:18px 17px;background:var(--n-1);border:0;border-top:6px solid var(--n-3);}
.card[data-el="undertow-card"][style*="--undertow-layout:solution"] .parts {display:flex;flex-direction:column;align-items:stretch;justify-content:flex-start;gap:0;text-align:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:solution"] .seat {width:100%;height:160px;aspect-ratio:auto;flex:none;background:var(--n-2);}
.card[data-el="undertow-card"][style*="--undertow-layout:solution"] .seat::after {content:none;}
.card[data-el="undertow-card"][style*="--undertow-layout:solution"] .name {font-size:var(--type-24);margin:var(--gap-sm) 0 0;padding-bottom:var(--gap-sm);border-bottom:var(--stroke) solid var(--n-5);color:var(--n-8);}
.card[data-el="undertow-card"][style*="--undertow-layout:solution"] .note {font-size:var(--type-16);line-height:var(--lead-line);margin:var(--gap-sm) 0 0;color:var(--ink);}
.card[data-el="undertow-card"][style*="--undertow-layout:kpi"] {padding:0;border:0;background:var(--n-1);}
.card[data-el="undertow-card"][style*="--undertow-layout:kpi"] .parts {display:flex;flex-direction:column;align-items:stretch;justify-content:flex-start;gap:0;text-align:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:kpi"] .name {order:0;display:flex;align-items:center;justify-content:center;height:33px;min-height:33px;background:var(--n-3);font-size:var(--type-18);}
.card[data-el="undertow-card"][style*="--undertow-layout:kpi"] .fig {order:1;font-size:var(--type-40);margin-top:var(--gap);white-space:nowrap;}
.card[data-el="undertow-card"][style*="--undertow-layout:kpi"] .note {order:2;font-size:var(--type-12);margin-top:calc(var(--gap-sm)*.5);color:var(--ink);}
.card[data-el="undertow-card"][style*="--undertow-layout:band"] {padding:0;border:0;background:var(--n-3);}
.card[data-el="undertow-card"][style*="--undertow-layout:band"] .parts {display:flex;align-items:center;justify-content:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:band"] .name {font-size:var(--type-20);text-align:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:phase"] {padding:0;border:0;background:var(--n-1);text-align:center;overflow:visible;}
.card[data-el="undertow-card"][style*="--undertow-layout:phase"] .parts {display:flex;flex-direction:column;justify-content:flex-start;gap:0;}
.card[data-el="undertow-card"][style*="--undertow-layout:phase"] .kick {display:flex;align-items:flex-end;justify-content:center;height:46px;min-height:46px;width:100%;padding-bottom:calc(var(--gap-sm)*.75);text-decoration:underline;font-size:var(--type-18);background:var(--n-5);color:var(--page);}
.card[data-el="undertow-card"][style*="--undertow-layout:phase"] .name {height:56px;min-height:56px;width:100%;font-size:var(--type-24);background:var(--n-5);color:var(--page);padding:0 var(--gap-sm);}
.card[data-el="undertow-card"][style*="--undertow-layout:phase"] .note {width:100%;font-size:var(--type-18);line-height:var(--lead-line);padding:var(--gap-sm) var(--gap);margin:0;color:var(--ink);}
.card[data-el="undertow-card"][style*="--undertow-layout:phase"] .note+ .note {border-top:var(--stroke) solid var(--n-3);}
.card[data-el="undertow-card"].tone-2[style*="--undertow-layout:phase"] .name,.card[data-el="undertow-card"].tone-2[style*="--undertow-layout:phase"] .kick {background:var(--n-6);}
.card[data-el="undertow-card"].tone-3[style*="--undertow-layout:phase"] .name,.card[data-el="undertow-card"].tone-3[style*="--undertow-layout:phase"] .kick {background:var(--n-7);}
.card[data-el="undertow-card"].on[style*="--undertow-layout:phase"] .name,.card[data-el="undertow-card"].on[style*="--undertow-layout:phase"] .kick {background:var(--ink);color:var(--page);}
.card[data-el="undertow-card"][style*="--undertow-layout:phase"]::after {content:"";position:absolute;right:-6px;top:-54px;width:72px;height:28px;background:var(--a1-3-soft);clip-path:polygon(0 100%,17% 43%,43% 15%,76% 15%,74% 0,100% 30%,78% 65%,79% 40%,45% 35%,20% 60%);}
.card[data-el="undertow-card"].on[style*="--undertow-layout:phase"]::after {content:none;}
.card[data-el="undertow-card"][style*="--undertow-layout:panel"] {padding:0;border:0;background:var(--n-1);}
.card[data-el="undertow-card"][style*="--undertow-layout:panel"] .parts {display:block;}
.card[data-el="undertow-card"][style*="--undertow-layout:panel"] .name {height:46px;display:flex;align-items:center;justify-content:center;background:var(--n-3);font-size:var(--type-20);text-align:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:ask"] {padding:0;border:0;background:var(--n-1);text-align:center;}
.card[data-el="undertow-card"][style*="--undertow-layout:ask"] .parts {display:flex;flex-direction:column;justify-content:flex-end;gap:0;padding:var(--gap) var(--gap-lg);}
.card[data-el="undertow-card"][style*="--undertow-layout:ask"] .name {font-size:var(--type-32);color:var(--a1-8);white-space:nowrap;}
.card[data-el="undertow-card"][style*="--undertow-layout:ask"] .note {font-size:var(--type-16);line-height:var(--lead-line);margin-top:var(--gap);color:var(--ink);}
.card[data-el="undertow-card"][style*="--undertow-layout:investment"] {padding:0;border:0;background:var(--n-2);text-align:center;color:var(--n-7);}
.card[data-el="undertow-card"][style*="--undertow-layout:investment"] .parts {display:flex;flex-direction:column;justify-content:center;align-items:center;gap:calc(var(--gap-sm)*.5);}
.card[data-el="undertow-card"][style*="--undertow-layout:investment"] .name {font-size:var(--type-18);}
.card[data-el="undertow-card"][style*="--undertow-layout:investment"] .fig {font-size:var(--type-48);}
.card[data-el="undertow-card"].on[style*="--undertow-layout:investment"] {background:var(--a1-2-soft);color:var(--ink);}
''')
add('concentric','''
.orbit[data-el="undertow-concentric"][style*="--undertow-layout:bottom-nested"] {overflow:visible;}
.orbit[data-el="undertow-concentric"][style*="--undertow-layout:bottom-nested"] .ring {position:absolute;inset:auto;left:0;top:0;width:100%;height:100%;border:0;border-radius:50%;padding-top:58px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;background:var(--n-1);color:var(--ink);}
.orbit[data-el="undertow-concentric"][style*="--undertow-layout:bottom-nested"] .ring:nth-child(2) {left:13.58%;top:26.27%;width:71.64%;height:71.64%;background:var(--n-3);color:var(--ink);}
.orbit[data-el="undertow-concentric"][style*="--undertow-layout:bottom-nested"] .ring:nth-child(3) {left:27.91%;top:51.94%;width:42.54%;height:42.54%;background:var(--n-6);color:var(--page);}
.orbit[data-el="undertow-concentric"][style*="--undertow-layout:bottom-nested"] .ring .name {position:static;font-size:var(--type-20);transform:none;}
.orbit[data-el="undertow-concentric"][style*="--undertow-layout:bottom-nested"] .ring .fig {position:static;font-size:var(--type-40);margin-top:calc(var(--gap-sm)*.5);transform:none;}
''')
add('list','''
.list[data-el="undertow-list"][style*="--undertow-layout:market"] {padding:0;display:flex;flex-direction:column;gap:0;background:none;}
.list[data-el="undertow-list"][style*="--undertow-layout:market"] .item {height:85px;flex:none;display:grid;grid-template-columns:78px 1fr;gap:var(--gap-sm);align-items:center;padding:0 10px;border:0;border-bottom:2px solid var(--n-5);}
.list[data-el="undertow-list"][style*="--undertow-layout:market"] .item::before {content:none;}
.list[data-el="undertow-list"][style*="--undertow-layout:market"] .name {width:78px;height:36px;border-radius:999px;background:var(--n-1);display:flex;align-items:center;justify-content:center;font-size:var(--type-16);}
.list[data-el="undertow-list"][style*="--undertow-layout:market"] .item:nth-child(2) .name {background:var(--n-3);}
.list[data-el="undertow-list"][style*="--undertow-layout:market"] .item:nth-child(3) .name {background:var(--n-6);color:var(--page);}
.list[data-el="undertow-list"][style*="--undertow-layout:market"] .note {font-size:var(--type-18);line-height:var(--title-line);margin:0;color:var(--n-8);}
.list[data-el="undertow-list"][style*="--undertow-layout:competition"] {padding:0;display:flex;flex-direction:column;gap:9px;background:none;}
.list[data-el="undertow-list"][style*="--undertow-layout:competition"] .item {height:52px;min-height:52px;display:flex;align-items:center;justify-content:center;background:var(--n-1);padding:0 var(--gap-sm);border:0;}
.list[data-el="undertow-list"][style*="--undertow-layout:competition"] .item::before {content:none;}
.list[data-el="undertow-list"][style*="--undertow-layout:competition"] .name {font-size:var(--type-18);text-align:center;color:var(--a1-8);}
.list[data-el="undertow-list"][style*="--undertow-layout:funds"] {padding:0;display:flex;flex-direction:column;gap:0;background:none;}
.list[data-el="undertow-list"][style*="--undertow-layout:funds"] .item {display:block;padding:0 0 0 var(--gap-sm);border:0;position:relative;}
.list[data-el="undertow-list"][style*="--undertow-layout:funds"] .item::before {content:"";position:absolute;left:0;top:var(--gap-sm);width:4px;height:4px;border-radius:50%;background:var(--ink);}
.list[data-el="undertow-list"][style*="--undertow-layout:funds"] .name {font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);}
''')
add('steps','''
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] {display:grid;grid-template-columns:repeat(3,249px);justify-content:space-between;gap:0;padding:0;border:0;background:none;}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"]::before {content:none;}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] .step {display:block;position:relative;padding:0;border:0;background:none;text-align:center;}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] .mark {position:relative;left:9px;top:0;width:225px;height:225px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:var(--type-36);padding-bottom:var(--gap);background:var(--n-1);color:var(--a1-8);margin:0;}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] .step.on .mark {background:var(--a1);color:var(--a1-on);}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] .name {position:absolute;left:9px;top:127px;width:225px;font-size:var(--type-18);color:var(--a1-8);}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] .step.on .name {color:var(--a1-on);}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] .note {font-size:var(--type-18);line-height:var(--lead-line);margin:var(--gap) 0 0;color:var(--ink);}
.steps[data-el="undertow-steps"][style*="--undertow-layout:technology"] .step:not(:last-child)::after {content:"";position:absolute;left:250px;top:105px;width:90px;height:3px;border-top:3px dotted var(--n-7);}
''')
add('callout','''
.callout[data-el="undertow-callout"][style*="--undertow-layout:solution"] {padding:0 var(--gap);display:flex;align-items:center;justify-content:center;background:var(--a1);color:var(--a1-on);border:0;}
.callout[data-el="undertow-callout"][style*="--undertow-layout:solution"] p {font-size:var(--type-22);font-weight:var(--name-weight);line-height:var(--label-line);}
.callout[data-el="undertow-callout"][style*="--undertow-layout:solution"]::before {content:"";width:18px;height:22px;clip-path:polygon(0 0,100% 50%,0 100%);background:currentColor;margin-right:var(--gap-sm);flex:none;}
.callout[data-el="undertow-callout"][style*="--undertow-layout:result"] {padding:0;display:block;background:var(--n-1);color:var(--ink);border:0;}
.callout[data-el="undertow-callout"][style*="--undertow-layout:result"] p {display:flex;align-items:center;height:100%;font-size:var(--type-22);line-height:var(--lead-line);font-weight:var(--body-weight);}
.callout[data-el="undertow-callout"][style*="--undertow-layout:result"] p b {width:134px;min-width:134px;height:100%;display:flex;align-items:center;justify-content:center;background:var(--n-4);color:var(--page);font-size:var(--type-24);margin-right:var(--gap);}
''')
add('hub','''
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] {display:block;padding:0;background:none;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke {position:absolute;width:510px;height:204px;left:0;top:0;padding:var(--gap-lg) 31px var(--gap);background:var(--n-1);border:0;display:block;text-align:left;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke:nth-child(3),.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke:nth-child(5) {left:524px;text-align:right;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke:nth-child(4),.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke:nth-child(5) {top:218px;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke::before,.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke::after {content:none;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke .name {display:block;font-size:var(--type-28);padding-bottom:var(--gap-sm);border-bottom:var(--stroke) solid var(--n-5);}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke .note {font-size:var(--type-16);line-height:var(--body-line);width:330px;margin-top:var(--gap);color:var(--ink);}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke:nth-child(3) .note,.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .spoke:nth-child(5) .note {margin-left:auto;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .core {position:absolute;left:363px;top:52px;width:318px;height:318px;transform:none;display:flex;flex-direction:column;align-items:center;justify-content:center;border:11px solid var(--n-1);border-radius:50%;padding:var(--gap);background:var(--a1);color:var(--a1-on);z-index:2;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .core .icon {width:78px;height:78px;}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .core .name {font-size:var(--type-36);white-space:nowrap;margin-top:var(--gap-sm);}
.hub[data-el="undertow-hub"][style*="--undertow-layout:revenue"] .core .note {font-size:var(--type-16);width:230px;text-align:center;line-height:var(--lead-line);margin-top:var(--gap-sm);color:inherit;}
''')
add('metric','''
.stat[data-el="undertow-metric"][style*="--undertow-layout:badge"] {border:3px solid var(--n-1);border-radius:50%;padding:0;display:block;background:var(--a1);color:var(--a1-on);}
.stat[data-el="undertow-metric"][style*="--undertow-layout:badge"] .parts {height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)*.5);text-align:center;}
.stat[data-el="undertow-metric"][style*="--undertow-layout:badge"] .name {order:0;font-size:var(--type-16);}
.stat[data-el="undertow-metric"][style*="--undertow-layout:badge"] .fig {order:1;font-size:var(--type-32);white-space:nowrap;}
''')
add('chart-area','''
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] {border:0;overflow:visible;background:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 20%);}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .series {inset:0;container-type:size;transform:translate(0);overflow:hidden;}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .series:nth-child(1) {--undertow-area-color:var(--n-3);}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .series:nth-child(2) {--undertow-area-color:var(--a1-3-soft);}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .pt {margin-top:calc(100cqh*(1 - var(--v)/var(--max)));}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .pt::after {clip-path:polygon(0 100cqh,100% calc(100% - 100cqh*var(--v)/var(--max)),100% 100%,0 100%);opacity:.45;}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .pt b {font-size:var(--type-14);transform:translate(-50%,-150%);}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .series>.name {top:auto;bottom:0;left:0;background:none;padding:0;font-size:var(--type-12);visibility:hidden;}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .axis {bottom:-30px;height:24px;}
.areas[data-el="undertow-chart-area"][style*="--undertow-layout:sales"] .axis span {visibility:visible;font-size:var(--type-14);}
''')
add('positioning','''
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"] {padding:0;background:var(--n-1);border:0;}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"]::before {content:"";position:absolute;left:50%;top:28px;bottom:28px;width:1.5px;height:auto;background:var(--n-6);}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"]::after {content:"";position:absolute;left:29px;right:29px;top:50%;height:1.5px;width:auto;background:var(--n-6);}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"] .axis-x {position:absolute;inset:50% 29px auto;display:flex;justify-content:space-between;padding-top:var(--gap-sm);font-size:var(--type-14);border:0;}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"] .axis-y {position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:calc(var(--gap-sm)/2) 0;font-size:var(--type-14);border:0;}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"] .mark {position:absolute;left:calc(var(--x)*1%);top:calc((100 - var(--y))*1%);width:20px;height:20px;border:0;border-radius:50%;background:var(--n-3);padding:0;transform:translate(-50%,-50%);}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"] .mark .name {position:absolute;top:30px;left:50%;transform:translateX(-50%);width:90px;text-align:center;font-size:var(--type-14);white-space:nowrap;}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"] .mark.on {width:128px;height:128px;background:var(--a1);border:2px solid var(--n-2);color:var(--a1-on);display:flex;align-items:center;justify-content:center;}
.posmap[data-el="undertow-positioning"][style*="--undertow-layout:competition"] .mark.on .name {position:static;transform:none;width:auto;font-size:var(--type-20);white-space:normal;}
''')
add('person','''
.people[data-el="undertow-person"][style*="--undertow-layout:team"] {display:grid;grid-template-columns:repeat(4,244px);gap:17px;padding:0;}
.people[data-el="undertow-person"][style*="--undertow-layout:team"]>.person {display:flex;flex-direction:column;align-items:stretch;text-align:center;padding:16px 16px 58px;background:var(--n-1);border:0;position:relative;gap:0;}
.people[data-el="undertow-person"][style*="--undertow-layout:team"]>.person.on {background:var(--a1-2-soft);color:var(--ink);}
.people[data-el="undertow-person"][style*="--undertow-layout:team"] .seat {width:212px;height:194px;aspect-ratio:auto;min-height:194px;border:2px solid var(--n-6);background:var(--n-2);}
.people[data-el="undertow-person"][style*="--undertow-layout:team"] .seat::after {content:none;}
.people[data-el="undertow-person"][style*="--undertow-layout:team"] .name {font-size:var(--type-30);margin-top:var(--gap-sm);}
.people[data-el="undertow-person"][style*="--undertow-layout:team"] .note {font-size:var(--type-16);line-height:var(--lead-line);color:var(--ink);margin:0;}
.people[data-el="undertow-person"][style*="--undertow-layout:team"] .note>b {font-size:var(--type-18);font-weight:var(--body-weight);display:block;margin-bottom:var(--gap-sm);}
.people[data-el="undertow-person"][style*="--undertow-layout:team"] .note>strong {position:absolute;left:0;bottom:0;width:100%;height:58px;background:var(--n-6);color:var(--page);display:flex;align-items:center;justify-content:center;font-size:var(--type-16);font-weight:var(--label-weight);}
.people[data-el="undertow-person"][style*="--undertow-layout:team"] .person.on .note>strong {background:var(--a1);color:var(--a1-on);}
''')
add('chart-donut','''
.donut[data-el="undertow-chart-donut"][style*="--undertow-layout:sector"] {display:block;padding:0;background:none;border:0;}
.donut[data-el="undertow-chart-donut"][style*="--undertow-layout:sector"]::before {content:"";position:absolute;inset:0;width:100%;height:100%;border-radius:50%;background:conic-gradient(from calc(var(--undertow-start-angle)*1deg),var(--a1-2-soft) 0 calc(var(--v)*1%),transparent 0);mask:radial-gradient(circle,transparent 0 calc(var(--undertow-hole-size)*1%),var(--ink) 0);}
.donut[data-el="undertow-chart-donut"].tone-2[style*="--undertow-layout:sector"]::before {background:conic-gradient(from calc(var(--undertow-start-angle)*1deg),var(--n-4) 0 calc(var(--v)*1%),transparent 0);}
.donut[data-el="undertow-chart-donut"].tone-3[style*="--undertow-layout:sector"]::before {background:conic-gradient(from calc(var(--undertow-start-angle)*1deg),var(--n-5) 0 calc(var(--v)*1%),transparent 0);}
.donut[data-el="undertow-chart-donut"].tone-4[style*="--undertow-layout:sector"]::before {background:conic-gradient(from calc(var(--undertow-start-angle)*1deg),var(--n-7) 0 calc(var(--v)*1%),transparent 0);}
.donut[data-el="undertow-chart-donut"][style*="--undertow-layout:sector"]::after {content:none;}
.donut[data-el="undertow-chart-donut"][style*="--undertow-layout:sector"] .fig {position:absolute;left:var(--undertow-label-x);top:var(--undertow-label-y);font-size:var(--type-28);font-weight:var(--figure-weight);transform:none;color:var(--ink);line-height:var(--figure-line);}
.donut[data-el="undertow-chart-donut"][style*="--undertow-layout:sector"] .name {position:absolute;left:var(--undertow-label-x);top:calc(var(--undertow-label-y) + 32px);font-size:var(--type-14);font-weight:var(--label-weight);color:var(--ink);transform:none;white-space:nowrap;}
.donut[data-el="undertow-chart-donut"].tone-2[style*="--undertow-layout:sector"] .fig,.donut[data-el="undertow-chart-donut"].tone-2[style*="--undertow-layout:sector"] .name,.donut[data-el="undertow-chart-donut"].tone-3[style*="--undertow-layout:sector"] .fig,.donut[data-el="undertow-chart-donut"].tone-3[style*="--undertow-layout:sector"] .name,.donut[data-el="undertow-chart-donut"].tone-4[style*="--undertow-layout:sector"] .fig,.donut[data-el="undertow-chart-donut"].tone-4[style*="--undertow-layout:sector"] .name {color:var(--page);}
''')
meta('chart-donut',{'--undertow-start-angle':'0','--undertow-hole-size':'0','--undertow-label-x':'0px','--undertow-label-y':'0px'})
add('chart-bar','''
.bars[data-el="undertow-chart-bar"][style*="--undertow-layout:financial"] {display:flex;align-items:stretch;gap:7px;padding:0;background:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 20%);border:0;}
.bars[data-el="undertow-chart-bar"][style*="--undertow-layout:financial"] .bar {position:relative;flex:1;align-self:stretch;display:block;background:none;padding:0;border:0;}
.bars[data-el="undertow-chart-bar"][style*="--undertow-layout:financial"] .bar::before {content:"";position:absolute;left:0;right:0;bottom:0;height:calc(var(--v)/var(--max)*100%);background:var(--n-6);}
.bars[data-el="undertow-chart-bar"][style*="--undertow-layout:financial"] .bar b {position:absolute;left:50%;top:calc(100% - var(--v)/var(--max)*100% - 22px);transform:translateX(-50%);font-size:var(--type-12);font-weight:var(--body-weight);color:var(--n-6);}
.bars[data-el="undertow-chart-bar"][style*="--undertow-layout:financial"] .bar span {position:absolute;left:50%;bottom:-24px;transform:translateX(-50%);font-size:var(--type-12);color:var(--n-7);white-space:nowrap;}
.bars[data-el="undertow-chart-bar"][style*="--undertow-layout:financial"]::after {content:"";position:absolute;left:40px;top:32px;width:123px;height:88px;background:var(--a1-3-soft);clip-path:polygon(0 100%,15% 55%,43% 20%,80% 15%,74% 0,100% 12%,79% 39%,81% 23%,48% 33%,25% 58%);}
''')
print('precision CSS registered')
# Expose only contract variants and semantic chart geometry; no free-canvas placement API.
for f,cl in used.items():
 p=C/'elements'/f/'element.css';s=p.read_text();s=re.sub(r'\.'+cl+r'\[data-el="undertow-'+f+r'"\] \{position:relative;left:var\(--undertow-x\).*?\}\n?', '',s);p.write_text(s)
 p=C/'elements'/f/'element.json';d=json.loads(p.read_text());
 for k in ['--undertow-x','--undertow-y','--undertow-width','--undertow-height','--undertow-layout']:d['tokenDefaults'].pop(k,None)
 p.write_text(json.dumps(d,indent=2)+'\n')
selectors={
'headline':{'contents':'.big:has(>.kick)','vision':'.big:not(:has(>.kick)):not(:has(>.note))','problem':'.big:has(>.note)','market':'.center:has(>h2>b)','competition':'.center:not(:has(>h2>b))'},
'prose':{'vision':'.lead','axis':'.quiet','forecast':'.cols'},
'agenda':{'contents':''},'architecture':{'vision':''},
'card':{'problem':'.line:has(>.parts>.mark .icon)','solution':':has(>.parts>.seat)','kpi':'.line:has(>.parts>.fig)','band':'.quiet:not(:has(.fig)):not(:has(.note))','phase':':has(>.parts>.kick)','panel':'.line:not(:has(.fig)):not(:has(.mark)):not(:has(.kick)):not(:has(.note))','ask':'.quiet:has(>.parts>.note):not(:has(.fig)):not(:has(.mark))','investment':'.quiet:has(>.parts>.fig)'},
'concentric':{'bottom-nested':'[style*="--undertow-diameter:"]'},
'list':{'market':'.divided:has(>.item>.note)','competition':'.check','funds':':not(.check):not(.divided):not(.num)'},
'steps':{'technology':':not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4)))'},
'callout':{'solution':':not(:has(.icon))','result':'[hidden]'},
'hub':{'revenue':':has(>.spoke:nth-child(5)):not(:has(>.spoke:nth-child(6)))'},
'metric':{'badge':'[style*="--undertow-diameter:"]'},
'chart-area':{'sales':'[style*="--undertow-plot-inset:"]'},
'positioning':{'competition':''},'person':{'team':':has(>.person:nth-child(4)):not(:has(>.person:nth-child(5)))'},
'chart-donut':{'sector':'[style*="--undertow-start-angle:"]'},'chart-bar':{'financial':':not(.h)'} }
for f,subs in selectors.items():
 p=C/'elements'/f/'element.css';s=p.read_text()
 for k,v in subs.items():s=s.replace('[style*="--undertow-layout:'+k+'"]',v)
 s=s.replace('[style*="--undertow-layout:"]','')
 if f=='concentric':
  s=s.replace('width:100%;height:100%;border:0;border-radius:50%;padding-top:58px','width:var(--undertow-diameter);height:var(--undertow-diameter);border:0;border-radius:50%;padding-top:58px')
  s=s.replace('left:13.58%;top:26.27%;width:71.64%;height:71.64%;','left:calc(var(--undertow-diameter)*.1358);top:calc(var(--undertow-diameter)*.2627);width:calc(var(--undertow-diameter)*.7164);height:calc(var(--undertow-diameter)*.7164);')
  s=s.replace('left:27.91%;top:51.94%;width:42.54%;height:42.54%;','left:calc(var(--undertow-diameter)*.2791);top:calc(var(--undertow-diameter)*.5194);width:calc(var(--undertow-diameter)*.4254);height:calc(var(--undertow-diameter)*.4254);')
 if f=='metric':s=s.replace('border:3px solid var(--n-1);','width:var(--undertow-diameter);height:var(--undertow-diameter);border:3px solid var(--n-1);')
 p.write_text(s)
meta('concentric',{'--undertow-diameter':'min(100cqw,100cqh)'})
meta('metric',{'--undertow-diameter':'min(100cqw,100cqh)'})
meta('chart-area',{'--undertow-plot-inset':'0px'})
# Furniture identifies actual slide compositions; sheet fixtures have no top furniture.
p=C/'foundation/foundation.css';s=p.read_text();s=s.replace('.slide[style*="--undertow-page-mode:precise"]','.slide:has(>.page>.top)').replace('.slide.cover[style*="--undertow-page-mode:precise"]','.slide.cover');s=s.replace('inset:0;gap:0;grid-template','inset:auto;gap:0;grid-template');p.write_text(s)
p=C/'foundation/foundation.json';d=json.loads(p.read_text());d['tokenDefaults'].pop('--undertow-page-mode',None);p.write_text(json.dumps(d,indent=2)+'\n')
# Every composition still uses a 12-column, six-row grid. Nonuniform tracks align repeated source boundaries.
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide:has(>.page>.top) .body:has(>[data-el="undertow-agenda"]) {left:0;top:0;width:1280px;height:720px;grid-template-columns:repeat(6,minmax(0,100.3333px)) repeat(6,minmax(0,113px));}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-architecture"]) {left:0;top:0;width:1280px;height:720px;grid-template-columns:58px 13px repeat(3,138.3333px) 106px repeat(5,116.8px) 104px;grid-template-rows:160px 225px 10px 40px 242px 43px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-headline"]):has(>.group>[data-el="undertow-card"]) {left:0;top:0;width:1194px;height:720px;grid-template-columns:repeat(5,98.6px) 33px repeat(5,119.6px) 70px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-card"] .seat):has(>[data-el="undertow-callout"]) {left:114px;top:201px;width:964px;height:447px;grid-template-columns:repeat(3,102.3333px) 22px repeat(3,102.3333px) 22px repeat(3,102px) 0px;grid-template-rows:repeat(5,72.2px) 86px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-concentric"]) {left:-59px;top:224px;width:1193px;height:496px;grid-template-columns:repeat(6,111.6667px) 36px repeat(5,97.4px);grid-template-rows:19px 100px 53px 85px 85px 154px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-steps"]) {left:124px;top:208px;width:943px;height:437px;grid-template-rows:repeat(5,67.4px) 100px;}
.slide:has(>.page>.top) .body:has(>.group>[data-el="undertow-hub"]) {left:75px;top:226px;width:1034px;height:422px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-chart-area"]) {left:127px;top:213px;width:950px;height:441px;grid-template-columns:28px repeat(4,121.5px) 147px 4px 0px 41px repeat(3,81.3333px);grid-template-rows:39px 38px repeat(4,91px);}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-positioning"]) {left:90px;top:244px;width:1001px;height:389px;grid-template-columns:repeat(7,83px) 31px repeat(4,97.25px);grid-template-rows:155px repeat(5,46.8px);}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-card"] .kick):not(:has(>[data-el="undertow-chart-area"])) {left:72px;top:196px;width:1038px;height:470px;grid-template-columns:repeat(3,82px) 18px repeat(3,82px) 18px repeat(3,82px) 264px;grid-template-rows:69px 69px 69px 56px 138px 69px;}
.slide:has(>.page>.top) .body:has(>.group>[data-el="undertow-person"]) {left:85px;top:211px;width:1027px;height:440px;}
.slide:has(>.page>.top) .body:has(>.stack .donut) {left:94px;top:214px;width:999px;height:441px;grid-template-columns:repeat(3,99px) 12px repeat(3,113px) 12px repeat(3,113px) 0px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-headline"]):has(>.group>[data-el="undertow-card"])>.group.col {padding-top:127px;padding-bottom:46px;gap:14px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-card"] .seat):has(>[data-el="undertow-callout"])>[data-el="undertow-callout"] {align-self:end;height:66px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-steps"])>[data-el="undertow-card"] {align-self:end;height:80px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-chart-area"])>.group.col {gap:15px;}
.slide:has(>.page>.top) .body:has(>.stack .donut)>.stack {background:var(--n-1);gap:0;}
.slide:has(>.page>.top) .body:has(>.stack .donut)>.stack:first-child {padding:21px 23px 23px;gap:32px;}
.slide:has(>.page>.top) .body:has(>.stack .donut)>.stack:first-child>:nth-child(-n+2) {flex:0 0 119px;}
.slide:has(>.page>.top) .body:has(>.stack .donut)>.stack:first-child>:last-child {flex:1;}
.slide:has(>.page>.top) .body:has(>.stack .donut)>.stack:not(:first-child)>:first-child {height:46px;flex:0 0 46px;}
.slide .group.overrides {display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr);width:228px;height:228px;flex:0 0 228px;margin:30px auto 23px;gap:0;}
.slide .group.overrides>* {grid-column:1;grid-row:1;}
.slide:has(>.page>.top) .body:has(>.stack .donut)>.stack>.split {display:flex;flex-direction:column;padding:37px 28px 0;gap:40px;}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-agenda"])~* {display:none;}
.slide .page:has(>.body>[data-el="undertow-agenda"]) .top {top:70px;right:89px;}
.slide .page:has(>.body>[data-el="undertow-architecture"]) .top {right:38px;}
.slide .page:has(>.body>[data-el="undertow-architecture"])::after,.slide .page:has(>.body>[data-el="undertow-agenda"])::after {display:none;}
''')
# Own-element refinements for semantic parts and their measured source proportions.
add('agenda','.agenda[data-el="undertow-agenda"] {padding:213px 96px 0 101px;}')
add('prose','.prose[data-el="undertow-prose"].lead {width:1157px;} .prose[data-el="undertow-prose"].quiet {width:28px;display:block;} .prose[data-el="undertow-prose"].quiet p {display:flex;flex-direction:column;justify-content:space-between;height:100%;} .prose[data-el="undertow-prose"].cols {column-count:1;}')
add('list','.list[data-el="undertow-list"].divided:has(>.item>.note) {padding:0 42px 0 47px;} .list[data-el="undertow-list"]:not(.check):not(.divided):not(.num) {margin:0 42px;width:calc(100% - 84px);}')
add('card','''
.card[data-el="undertow-card"].line:has(>.parts>.mark):not(:has(.icon)) {padding:0;border:0;background:var(--n-1);}
.card[data-el="undertow-card"].line:has(>.parts>.mark):not(:has(.icon)) .parts {display:flex;align-items:center;justify-content:flex-start;gap:var(--gap);height:100%;}
.card[data-el="undertow-card"].line:has(>.parts>.mark):not(:has(.icon)) .mark {width:134px;min-width:134px;height:100%;border:0;border-radius:0;background:var(--n-4);color:var(--page);display:flex;align-items:center;justify-content:center;font-size:var(--type-24);margin:0;}
.card[data-el="undertow-card"].line:has(>.parts>.mark):not(:has(.icon)) .name {font-size:var(--type-22);font-weight:var(--body-weight);line-height:var(--lead-line);padding-right:var(--gap);}
.card[data-el="undertow-card"].quiet:has(>.parts>.note):not(:has(.fig)):not(:has(.mark)) .parts {padding:0;}
@container (max-height:160px) {.card[data-el="undertow-card"].quiet:has(>.parts>.note):not(:has(.fig)):not(:has(.mark)) .name {font-size:var(--type-30);} .card[data-el="undertow-card"].quiet:has(>.parts>.note):not(:has(.fig)):not(:has(.mark)) .note {font-size:var(--type-16);margin-top:var(--gap-sm);}}
''')
add('chart-area','''
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] {height:355px;background:none;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .series {left:28px;right:8px;background:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 20%);}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .axis {left:28px;right:8px;}
''')
add('metric','.stat[data-el="undertow-metric"][style*="--undertow-diameter:"] {margin-top:8px;}')
add('chart-bar','.bars[data-el="undertow-chart-bar"]:not(.h) {min-height:235px;}')
print('contract-based compositions installed')
