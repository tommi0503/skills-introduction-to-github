from pathlib import Path
import json,re
C=Path('/workspace/work/deliverables/undertow');S=Path('/workspace/work/agents/031')
def add(f,s):
 p=C/('foundation/foundation.css' if f=='foundation' else 'elements/'+f+'/element.css');p.write_text(p.read_text()+'\n'+s+'\n')
# Primary display accent and deeper panel accent are independent palette ranks.
for p in [C/'foundation/foundation.css',*C.glob('elements/*/element.css')]:
 s=p.read_text();a,sep,b=s.partition('/* UNDERTOW PRECISE COMPOSITIONS */')
 b=b.replace('background:var(--a1);color:var(--a1-on)','background:var(--a1-7);color:var(--page)')
 b=b.replace('background:var(--a1);border:2px solid var(--n-2);color:var(--a1-on)','background:var(--a1-7);border:2px solid var(--n-2);color:var(--page)')
 b=b.replace('background:var(--a1);color:var(--a1-on);','background:var(--a1-7);color:var(--page);')
 s=a+sep+b;p.write_text(s)
add('foundation','''
.slide.cover .lockup .kicker {line-height:var(--label-line);}
.slide.cover .lockup .title {font-size:var(--type-112);line-height:var(--undertow-cover-line);}
.slide.cover .lockup .title b {color:var(--a1);}
.slide.cover .foot>b::before {content:"";display:inline-block;width:24px;height:18px;background:currentColor;clip-path:polygon(0 90%,30% 0,48% 0,23% 100%,45% 100%,75% 0,94% 0,68% 100%,100% 80%,100% 100%);margin-right:calc(var(--gap-sm)/4);}
.slide:has(>.page>.top) .body:has(>[data-el="undertow-headline"]):has(>.group>[data-el="undertow-card"]) {grid-template-rows:127px 173px 14px 173px 14px 219px;}
''')
add('headline','.headline[data-el="undertow-headline"].big:has(>.kick) h2 b {color:var(--a1);}')
add('prose','.prose[data-el="undertow-prose"].lead {margin:0;}')
add('card','''
.card[data-el="undertow-card"]:has(>.parts>.mark:only-child) {background:none;border:0;padding:0;}
.card[data-el="undertow-card"]:has(>.parts>.mark:only-child) .parts {display:flex;align-items:center;justify-content:center;}
.card[data-el="undertow-card"]:has(>.parts>.mark:only-child) .mark {width:84px;height:84px;background:none;border:0;color:var(--a1-7);}
.card[data-el="undertow-card"]:has(>.parts>.mark:only-child) .icon {width:84px;height:84px;}
''')
p=C/'kit/css/tokens.css';s=p.read_text().replace('--undertow-cover-line:.92','--undertow-cover-line:.84');p.write_text(s)
p=S/'precision-pages.py';s=p.read_text().replace("'--a1':'#529f8b'","'--a1':'#9bffd4','--a1-7':'#529f8b'")
s=s.replace("(7,5,1,6),'col')+end()","(7,5,1,6),'col')+card('',slot=(1,2,6,1),mark=icon('lightbulb'))+end()")
p.write_text(s)
# Include the directly implementable source lightbulb in the portable review harness.
icons=Path('/workspace/work/deliverables/undertow-review/icons.js');s=icons.read_text();s=s.replace('const icons={','const icons={"Lightbulb":[["path",{"d":"M9 18h6m-5 4h4m-5-7a6 6 0 1 1 6 0l-1 3h-4Z"}]],');icons.write_text(s)
# All spacing and radii use typed shared kit extension tokens, even measured asymmetrical insets.
kp=C/'kit/kit.json';d=json.loads(kp.read_text());vals={}
for p in [C/'foundation/foundation.css',*C.glob('elements/*/element.css')]:
 s=p.read_text()
 def decl(m):
  prop,val=m.group(1),m.group(2)
  if not re.search(r'-?\d+(?:\.\d+)?px',val):return m.group(0)
  def px(z):
   raw=z.group();num=raw[:-2];key='--undertow-space-'+num.replace('-','neg-').replace('.','-');vals[key]=raw;return 'var('+key+')'
  return prop+':'+re.sub(r'-?\d+(?:\.\d+)?px',px,val)
 s=re.sub(r'(?<![-\w])((?:margin|padding)(?:-(?:top|bottom|left|right|inline|block|inline-start|inline-end))?|gap|column-gap|row-gap)\s*:\s*([^;}]+)',decl,s)
 p.write_text(s)
for k in vals:d['extensions'][k]='length'
kp.write_text(json.dumps(d,indent=2)+'\n');p=C/'kit/css/tokens.css';p.write_text(p.read_text()+'\n.slide {'+';'.join(k+':'+v for k,v in vals.items())+';}\n')
print('source accents and final spacing tokens',len(vals))
