from pathlib import Path
import re,json
c=Path('/workspace/work/rebuild-20261024/nocturne/collection/nocturne')
vals={'--nocturne-head-weight':'780','--nocturne-head-track':'.008897em','--nocturne-kicker-weight':'450','--nocturne-brand-weight':'650','--nocturne-brand-track':'0em','--nocturne-year-track':'.014286em','--nocturne-cover-font':"'Montserrat'",'--nocturne-cover-weight':'700','--nocturne-cover-track':'-.015em','--nocturne-cover-line':'1.2','--nocturne-head-line':'1.2'}
p=c/'kit/css/tokens.css';s=p.read_text()
for k,v in vals.items():
 if k+':'in s:s=re.sub(re.escape(k)+r':[^;}]+',k+':'+v,s)
 else:s=s.replace('.slide{','.slide{'+k+':'+v+';',1)
p.write_text(s);p=c/'kit/kit.json';d=json.loads(p.read_text())
for k in vals:d['extensions'][k]='font'if 'font'in k else'tracking'if'track'in k else'number'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
p=c/'foundation/foundation.css';s=p.read_text().split('.slide{background:')[0]
s+='''/* Source furniture from frozen pages20–22 and cover24. */
.slide{background:radial-gradient(ellipse 790px 450px at 0 0,color-mix(in srgb,var(--a1) 28%,var(--page)),transparent 82%),radial-gradient(ellipse 700px 560px at 100% 100%,color-mix(in srgb,var(--a1) 22%,var(--page)),transparent 80%),var(--page)}
.slide .top{position:absolute;left:-29px;right:-29px;top:-11px;height:20px;font-size:var(--type-16);letter-spacing:var(--nocturne-brand-track);font-weight:var(--nocturne-brand-weight);color:var(--n-7)}
.slide .top .src{font-size:var(--type-14);font-weight:var(--body-weight);letter-spacing:var(--nocturne-year-track);color:var(--n-6)}
.slide .top .seat{width:17px;height:18px;aspect-ratio:auto;background:var(--a1);border-radius:0}
.slide .head{position:relative;height:143px;display:block;text-align:center}
.slide .head .kicker{position:absolute;left:0;right:0;top:17px;font-size:var(--type-28);font-weight:var(--nocturne-kicker-weight);line-height:var(--label-line);letter-spacing:var(--nocturne-brand-track);color:var(--a1)}
.slide .head .title{position:absolute;left:0;right:0;top:76px;font-size:clamp(var(--type-56),4.390625cqw,var(--type-60));font-weight:var(--nocturne-head-weight);line-height:var(--nocturne-head-line);letter-spacing:var(--nocturne-head-track);color:var(--ink)}
.slide.cover .lockup{left:-68px;right:-68px;top:201px;width:auto;max-width:none;transform:none;gap:29px;text-align:center;align-items:center}
.slide.cover .lockup .title{font-family:var(--nocturne-cover-font);font-size:var(--type-100);font-weight:var(--nocturne-cover-weight);line-height:var(--nocturne-cover-line);letter-spacing:var(--nocturne-cover-track);background:linear-gradient(to right,var(--a1) 17%,color-mix(in srgb,var(--ink) 80%,var(--a1-7)) 43%,var(--ink) 70%);color:transparent;background-clip:text}
.slide.cover .lockup .lead{font-size:var(--type-32);font-weight:var(--body-weight);line-height:var(--lead-line);letter-spacing:var(--body-track)}
.slide.cover .lockup .lead b{font-weight:var(--title-weight)}
.slide .meta{position:absolute;right:-26px;bottom:1px;font-size:var(--type-20);color:var(--n-8)}
.slide .deco{inset:-45px -68px;z-index:0}.slide .deco>.seat{background:color-mix(in srgb,var(--ink) 85%,var(--page))}
.slide .deco>.seat:first-child{position:absolute;right:0;top:0;width:360px;height:186px;aspect-ratio:auto;border-radius:0 0 0 100%}
.slide .deco>.seat:last-child{position:absolute;left:0;bottom:0;width:430px;height:286px;aspect-ratio:auto;border-radius:0 100% 0 0}
.slide .body>.seat.back{position:relative;inset:auto;aspect-ratio:auto;background:color-mix(in srgb,var(--ink) 85%,var(--page))}
.slide .seat[data-ph]:empty::after{content:attr(data-ph);font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line)}
''';p.write_text(s)
print('nocturne source furniture refreshed')
