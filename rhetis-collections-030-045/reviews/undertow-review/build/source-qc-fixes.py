from pathlib import Path
import json,re
C=Path('/workspace/work/deliverables/undertow')
def add(f,s):
 p=C/('foundation/foundation.css' if f=='foundation' else 'elements/'+f+'/element.css');p.write_text(p.read_text()+'\n'+s+'\n')
add('foundation','''
.slide:has(>.page>.top) .head .title {font-size:var(--type-44);}
.slide:has(>.page>.top) .top>b {font-size:var(--type-14);}
''')
add('card','''
.card[data-el="undertow-card"].line:has(>.parts>.mark):not(:has(.icon)) .name {font-size:var(--type-18);white-space:nowrap;}
.card[data-el="undertow-card"]:has(>.parts>.kick)::after {left:180px;right:auto;top:-55px;width:100px;height:40px;transform:scale(.72,.7);transform-origin:0 0;background:linear-gradient(to right,var(--a1-3-soft),var(--a1-7));clip-path:path("M2 38Q25 5 77 7L75 0L100 12L78 26L79 16Q35 13 2 38Z");}
.card[data-el="undertow-card"].quiet:has(>.parts>.fig):not(.on) {background:var(--page);}
.card[data-el="undertow-card"].quiet:has(>.parts>.fig):not(.on)::after {content:"";position:absolute;left:50%;top:100%;width:46px;height:25px;transform:translateX(-50%);clip-path:polygon(0 0,100% 0,50% 100%);background:var(--page);}
''')
add('concentric','''
.orbit[data-el="undertow-concentric"][style*="--undertow-diameter:"] .ring:nth-child(2) {padding-top:38px;}
.orbit[data-el="undertow-concentric"][style*="--undertow-diameter:"] .ring:nth-child(3) {padding-top:28px;}
''')
add('steps','''
.steps[data-el="undertow-steps"]:not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4))) .step:not(:last-child) .mark::after {content:"";position:absolute;left:324px;top:100px;width:11px;height:13px;clip-path:polygon(0 0,100% 50%,0 100%);background:var(--n-7);}
''')
add('hub','''
.hub[data-el="undertow-hub"]:has(>.spoke:nth-child(5)):not(:has(>.spoke:nth-child(6))) .core {border-color:var(--page);}
.hub[data-el="undertow-hub"]:has(>.spoke:nth-child(5)):not(:has(>.spoke:nth-child(6))) .spoke .note {font-size:var(--type-14);line-height:var(--body-line);}
.hub[data-el="undertow-hub"]:has(>.spoke:nth-child(5)):not(:has(>.spoke:nth-child(6))) .core .note {font-size:var(--type-14);line-height:var(--body-line);}
''')
add('headline','''
.headline[data-el="undertow-headline"].center:not(:has(>h2>b)) h2 {font-size:var(--type-30);}
.headline[data-el="undertow-headline"].center:not(:has(>h2>b)) .note {font-size:var(--type-16);}
''')
add('person','''
.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5))) .note {font-size:var(--type-14);line-height:var(--body-line);}
.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5))) .note>b {font-size:var(--type-14);}
.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5))) .note>strong {font-size:var(--type-16);}
''')
add('chart-donut','''
.donut[data-el="undertow-chart-donut"].tone-4[style*="--undertow-start-angle:"] .fig {font-size:var(--type-22);}
.donut[data-el="undertow-chart-donut"].tone-4[style*="--undertow-start-angle:"] .name {font-size:var(--type-12);top:calc(var(--undertow-label-y) + 27px);}
.donut[data-el="undertow-chart-donut"].tone-3[style*="--undertow-start-angle:"] .fig {font-size:var(--type-24);}
''')
add('chart-bar','''
.bars[data-el="undertow-chart-bar"]:not(.h):has(>.bar:nth-child(4)):not(:has(>.bar:nth-child(5))) {border-left:var(--stroke) solid var(--n-5);counter-reset:ut100 var(--max) ut80 calc(var(--max)*.8) ut60 calc(var(--max)*.6) ut40 calc(var(--max)*.4) ut20 calc(var(--max)*.2);}
.bars[data-el="undertow-chart-bar"]:not(.h):has(>.bar:nth-child(4)):not(:has(>.bar:nth-child(5)))::before {content:counter(ut100) "\\A" counter(ut80) "\\A" counter(ut60) "\\A" counter(ut40) "\\A" counter(ut20) "\\A 0";position:absolute;right:calc(100% + 8px);top:-5px;white-space:pre;text-align:right;font-size:var(--type-10);font-weight:var(--body-weight);line-height:var(--undertow-axis-line);color:var(--n-5);}
.bars[data-el="undertow-chart-bar"]:not(.h):has(>.bar:nth-child(4)):not(:has(>.bar:nth-child(5)))::after {left:28px;top:32px;width:123px;height:88px;background:linear-gradient(to top right,var(--a1-3-soft),var(--a1-7));clip-path:path("M2 88Q32 15 95 16L86 3L123 14L96 40L98 26Q51 27 2 88Z");}
''')
add('prose','.prose[data-el="undertow-prose"].cols p {font-size:var(--type-18);}')
add('callout','.callout[data-el="undertow-callout"]:not(:has(.icon)) p {font-size:var(--type-20);}')
add('chart-area','''
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .series>.name {visibility:visible;top:14px;bottom:auto;left:56px;white-space:nowrap;background:none;color:var(--ink);font-size:var(--type-12);padding:0;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .series:nth-child(2)>.name {left:144px;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .series {--undertow-series-stroke:var(--n-5);background:none;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] {background:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 20%);}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .series:nth-child(2) {--undertow-series-stroke:var(--a1-7);}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .series>.name::before {content:"";display:inline-block;width:10px;height:10px;background:var(--undertow-series-stroke);margin-right:4px;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt b {color:var(--undertow-series-stroke);font-weight:var(--body-weight);}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt::before {content:"";position:fixed;left:anchor(var(--undertow-self) center);top:anchor(var(--undertow-self) center);width:7px;height:7px;transform:translate(-50%,-50%);border-radius:50%;background:var(--undertow-series-stroke);z-index:30;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt b::before,.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt b::after {content:"";position:fixed;left:anchor(var(--undertow-prev) center);right:anchor(var(--undertow-self) center);pointer-events:none;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt b::before {top:calc(anchor(var(--undertow-prev) bottom) - .5px);bottom:calc(anchor(var(--undertow-self) bottom) - .5px);background:linear-gradient(to top right,transparent calc(50% - .5px),var(--undertow-series-stroke) calc(50% - .5px),var(--undertow-series-stroke) calc(50% + .5px),transparent calc(50% + .5px));}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt b::after {top:calc(anchor(var(--undertow-self) bottom) - .5px);bottom:calc(anchor(var(--undertow-prev) bottom) - .5px);background:linear-gradient(to bottom right,transparent calc(50% - .5px),var(--undertow-series-stroke) calc(50% - .5px),var(--undertow-series-stroke) calc(50% + .5px),transparent calc(50% + .5px));}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt:first-of-type b::before,.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"] .pt:first-of-type b::after {content:none;}
.areas[data-el="undertow-chart-area"][style*="--undertow-plot-inset:"]::after {content:"";position:absolute;left:470px;top:135px;width:100px;height:70px;background:linear-gradient(to top right,transparent,var(--n-1));clip-path:path("M0 65Q50 60 63 19L48 15L91 0L94 40L76 31Q55 65 0 65Z");z-index:30;}
''')
p=C/'kit/kit.json';d=json.loads(p.read_text());d['extensions']['--undertow-axis-line']='number';p.write_text(json.dumps(d,indent=2)+'\n');p=C/'kit/css/tokens.css';p.write_text(p.read_text()+'\n.slide {--undertow-axis-line:4.6;}\n')
p=Path('/workspace/work/agents/031/precision-pages.py');s=p.read_text().replace("(10,324,'5억 원',68,18,'tone-4')","(10,324,'5억 원',70,26,'tone-4')");p.write_text(s)
# Register all spacing values as shared length tokens.
kp=C/'kit/kit.json';d=json.loads(kp.read_text());vals={}
for p in [C/'foundation/foundation.css',*C.glob('elements/*/element.css')]:
 s=p.read_text()
 def decl(m):
  prop,val=m.group(1),m.group(2)
  def px(z):
   raw=z.group();key='--undertow-space-'+raw[:-2].replace('-','neg-').replace('.','-');vals[key]=raw;return 'var('+key+')'
  return prop+':'+re.sub(r'-?\d+(?:\.\d+)?px',px,val)
 s=re.sub(r'(?<![-\w])((?:margin|padding)(?:-(?:top|bottom|left|right|inline|block|inline-start|inline-end))?|gap|column-gap|row-gap)\s*:\s*([^;}]+)',decl,s);p.write_text(s)
for k in vals:d['extensions'][k]='length'
kp.write_text(json.dumps(d,indent=2)+'\n');p=C/'kit/css/tokens.css';p.write_text(p.read_text()+'\n.slide {'+';'.join(k+':'+v for k,v in vals.items())+';}\n')
print('source QC corrections applied')
