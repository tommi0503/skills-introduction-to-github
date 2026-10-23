from pathlib import Path
import re,json,hashlib
B=Path('/workspace/output/roundrise')
p=B/'elements/timeline/element.css';s=p.read_text();r='.track[data-el="roundrise-timeline"].alt'
s+=r+'{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:1fr 1fr;gap:var(--gap-lg) var(--gap)}'+r+'>.stop{padding:var(--gap-sm);gap:calc(var(--gap-sm)/2);align-self:start;min-height:0}'+r+'>.stop>.name{font-size:var(--type-20)}'+r+'>.stop>.note{font-size:var(--type-14)}'+r+'>.stop>.kick{font-size:var(--type-14)}'+r+'>.stop:nth-child(odd){grid-row:1;align-self:end}'+r+'>.stop:nth-child(even){grid-row:2;align-self:start}'+r+'>.stop:nth-child(odd):before{top:auto;bottom:calc(var(--gap-lg)/-2 - 7px)}'+r+'>.stop:nth-child(even):before{top:calc(var(--gap-lg)/-2 - 7px);bottom:auto}'+r+'>.stop:after{content:"";position:absolute;left:var(--pad);width:var(--stroke);height:calc(var(--gap-lg)/2);background:var(--a1-3-soft)}'+r+'>.stop:nth-child(odd):after{top:100%}'+r+'>.stop:nth-child(even):after{bottom:100%}'
for i in range(1,13):s+=r+f'>.stop:nth-child({i}){{grid-column:{i};}}'
p.write_text(s)
p=B/'elements/slope/element.css';s=p.read_text();r='.slope[data-el="roundrise-slope"].dumbbell'
s+=r+'{gap:var(--gap-sm);padding:var(--pad)}'+r+'>.pair{min-height:48px;display:block}'+r+'>.pair>.name{position:absolute;left:0;top:50%;transform:translateY(-50%);width:22%;text-align:left;background:none;padding:0;font-size:var(--type-18)}'+r+'>.pair>.a,'+r+'>.pair>.b{position:absolute;grid-column:auto;grid-row:auto;justify-self:auto;font-size:var(--type-16);line-height:var(--figure-line);font-weight:var(--figure-weight);white-space:nowrap}'+r+'>.pair>.a{left:calc(25% + var(--a)/var(--max)*65%);top:calc(50% + var(--gap-sm)*2/3);transform:translateX(-50%);color:var(--n-7)}'+r+'>.pair>.b{left:calc(25% + var(--b)/var(--max)*65%);top:calc(50% - var(--gap-sm)*2/3);transform:translate(-50%,-100%);color:var(--a1-7)}'+r+'>.pair>.a:after,'+r+'>.pair>.b:after{content:"";position:absolute;left:calc(50% - 5px);width:10px;height:10px;border-radius:50%}'+r+'>.pair>.a:after{top:calc(var(--gap-sm)*-2/3 - 5px);background:var(--n-5)}'+r+'>.pair>.b:after{top:calc(100% + var(--gap-sm)*2/3 - 5px);background:var(--a1)}'+r+'>.pair:before{left:calc(25% + min(var(--a),var(--b))/var(--max)*65%);right:calc(10% + (1 - max(var(--a),var(--b))/var(--max))*65%);width:auto;transform:none;top:calc(50% - 1px);height:2px;background:var(--n-4)}'+r+'>.pair.on:before{background:var(--a1)}'
p.write_text(s)
for k,sub,mn in [('timeline','track alt','10x5'),('slope','dumbbell','8x5')]:
 for p in (B/'elements'/k/'fixtures').glob('*.html'):
  s=p.read_text()
  if sub in s:p.write_text(re.sub(r'\A<!--.*?-->','<!-- min: '+mn+' -->',s,flags=re.S))
m={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.rglob('*') if p.is_file()};Path('/workspace/work/roundrise/frozen-source-manifest.json').write_text(json.dumps(m,indent=2))
