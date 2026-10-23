from pathlib import Path
import re,json
C=Path('/workspace/work/deliverables/undertow')
def add(f,s):
 p=C/('foundation/foundation.css' if f=='foundation' else 'elements/'+f+'/element.css');p.write_text(p.read_text()+'\n'+s+'\n')
# Foundation changes only its furniture, body grid and composition holders.
p=C/'foundation/foundation.css';s=p.read_text();s='\n'.join(l for l in s.splitlines() if not ('>[data-el="undertow-callout"] {' in l or '>[data-el="undertow-card"] {' in l or '~* {display:none' in l));p.write_text(s+'\n')
add('foundation','''
.slide:has(>.page>.top) .page::after {background:var(--a1-1-muted);}
.slide:has(>.page>.top) .head .kicker {width:136px;padding:calc(var(--gap-sm)/3) var(--gap-sm);white-space:nowrap;}
.slide.cover .seat.back::after {content:none;}
.slide.cover .foot>p:nth-child(2) {margin-left:calc(var(--gap-lg)/2);}
.slide .page:has(>.body>[data-el="undertow-card"] .kick)>.seat.back {top:242px;left:0;right:auto;bottom:auto;width:1194px;height:478px;}
.slide:has(>.page>.top) .body:has(>.stack .donut)>.stack>.split {padding-top:37px;gap:52px;}
''')
add('headline','''
.headline[data-el="undertow-headline"].big:has(>.kick) .kick {background:none;color:var(--ink);border:0;border-radius:0;padding:0;font-weight:var(--body-weight);line-height:var(--label-line);}
.headline[data-el="undertow-headline"].big:has(>.kick) h2 {line-height:var(--undertow-flat-line);}
.headline[data-el="undertow-headline"].center:has(>h2>b) .note {text-align:center;}
''')
add('agenda','.agenda[data-el="undertow-agenda"] {justify-content:flex-start;}')
add('prose','.prose[data-el="undertow-prose"].lead {display:block;}')
add('architecture','.arch[data-el="undertow-architecture"] {justify-content:flex-start;} .arch[data-el="undertow-architecture"] .layer {flex:none;} .arch[data-el="undertow-architecture"] .layer .name {width:100%;}')
add('concentric','.orbit[data-el="undertow-concentric"][style*="--undertow-diameter:"] .ring {transform:none;}')
add('list','''
.list[data-el="undertow-list"].divided:has(>.item>.note) {justify-content:flex-start;}
.list[data-el="undertow-list"]:not(.check):not(.divided):not(.num) {width:calc(100% - 70px);margin-left:42px;margin-right:28px;justify-content:flex-start;}
.list[data-el="undertow-list"]:not(.check):not(.divided):not(.num) .name {font-size:var(--type-16);}
''')
add('card','''
.card[data-el="undertow-card"].line:has(>.parts>.mark .icon) .name {padding:0;border:0;min-height:0;}
.card[data-el="undertow-card"]:has(>.parts>.seat) .name {min-height:0;display:block;font-size:var(--type-24);margin-top:calc(var(--gap-sm)*4/3);padding-bottom:calc(var(--gap-sm)*.75);}
.card[data-el="undertow-card"]:has(>.parts>.seat) .note {min-height:0;font-size:var(--type-14);line-height:var(--body-line);margin-top:calc(var(--gap-sm)*4/3);}
.card[data-el="undertow-card"].line:has(>.parts>.fig) .name {padding:0;border:0;min-height:0;}
.card[data-el="undertow-card"].line:has(>.parts>.mark):not(:has(.icon)) {height:80px;align-self:end;}
.card[data-el="undertow-card"].line:has(>.parts>.mark):not(:has(.icon)) .name {padding-bottom:0;border:0;min-height:0;}
.card[data-el="undertow-card"]:has(>.parts>.kick) {height:263px;}
.card[data-el="undertow-card"]:has(>.parts>.kick) .name {padding-bottom:0;border:0;min-height:0;display:block;}
.card[data-el="undertow-card"]:has(>.parts>.kick) .note {min-height:0;font-size:var(--type-16);padding:20px 30px;}
.card[data-el="undertow-card"].on:has(>.parts>.kick) {width:246px;margin-left:18px;}
.card[data-el="undertow-card"].quiet:has(>.parts>.fig) .name {padding:0;border:0;min-height:0;}
.card[data-el="undertow-card"].quiet:has(>.parts>.fig):not(.on) {color:var(--n-5);}
.card[data-el="undertow-card"].quiet:has(>.parts>.note):not(:has(.fig)):not(:has(.mark)) .name {padding:0;border:0;min-height:0;display:block;}
.card[data-el="undertow-card"].line:not(:has(.fig)):not(:has(.mark)):not(:has(.kick)):not(:has(.note)) .name {padding:0;border:0;min-height:0;}
.card[data-el="undertow-card"].quiet:not(:has(.fig)):not(:has(.note)) .name {padding:0;border:0;min-height:0;}
''')
add('steps','''
.steps[data-el="undertow-steps"]:not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4))) .step {align-content:start;}
.steps[data-el="undertow-steps"]:not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4))) .mark {justify-self:start;font-size:var(--type-40);}
.steps[data-el="undertow-steps"]:not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4))) .name {font-size:var(--type-16);}
.steps[data-el="undertow-steps"]:not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4))) .note {font-size:var(--type-16);}
''')
add('callout','.callout[data-el="undertow-callout"]:not(:has(.icon)) {height:66px;align-self:end;}')
add('positioning','.posmap[data-el="undertow-positioning"] {margin:0;}')
add('person','''
.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5)))>.person {justify-content:flex-start;}
.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5))) .seat {flex:none;}
.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5))) .name {margin-top:16px;}
.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5))) .note>b {background:none;color:inherit;padding:0;margin-top:0;}
''')
add('chart-bar','.bars[data-el="undertow-chart-bar"]:not(.h):has(>.bar:nth-child(4)):not(:has(>.bar:nth-child(5))) {width:calc(100% - 46px);margin-left:27px;}')
p=C/'kit/kit.json';d=json.loads(p.read_text());d['extensions']['--undertow-flat-line']='number';p.write_text(json.dumps(d,indent=2)+'\n')
p=C/'kit/css/tokens.css';p.write_text(p.read_text()+'\n.slide {--undertow-flat-line:1;}\n')
# Prefer an icon already included in the portable Lucide harness.
p=Path('/workspace/work/agents/031/precision-pages.py');s=p.read_text().replace("icon('presentation')","icon('chart-no-axes-combined')").replace("'--a1-8':'#377461'","'--a1-8':'#529f8b','--a1-1-muted':'#dce1df'");p.write_text(s)
print('precision corrections applied')
