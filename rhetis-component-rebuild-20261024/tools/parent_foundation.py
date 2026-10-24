from pathlib import Path
import json,re
B=Path('/workspace/work/rebuild-20261024')
def tokens(n,vals):
 c=B/n/'collection'/n;p=c/'kit/css/tokens.css';s=p.read_text()
 for k,v in vals.items():
  if k+':'in s:s=re.sub(re.escape(k)+r':[^;}]+',k+':'+v,s)
  else:s=s.replace('.slide{','.slide{'+k+':'+v+';',1)
 p.write_text(s);p=c/'kit/kit.json';d=json.loads(p.read_text())
 for k in vals:
  if k.startswith('--'+n+'-'):d['extensions'][k]='tracking'if 'track'in k else 'number'if 'line'in k or 'weight'in k else 'length'
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
def foundation(n,tail):
 p=B/n/'collection'/n/'foundation/foundation.css';s=p.read_text();s=s.split('.slide{background:')[0]
 s+='\n.slide .seat[data-ph]:empty::after{content:attr(data-ph);font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line)}\n'+tail
 p.write_text(s)
tokens('confluence',{'--confluence-cover-track':'-.0625em','--confluence-cover-subtrack':'-.055319em','--confluence-caps-track':'.311111em','--confluence-side-track':'.035em','--confluence-cover-line':'.92','--confluence-sub-line':'1.05','--confluence-side-line':'1','--confluence-side-note-track':'-.030769em','--confluence-tiny-track':'0em','--confluence-cover-weight':'900','--confluence-cover-subweight':'400','--confluence-head-weight':'850','--confluence-side-weight':'800','--confluence-center-track':'-.0625em','--confluence-cover-note-track':'-.040625em'})
foundation('confluence','''/* Source furniture: cover 01, central head 02, left rail 03. */
.slide{background:linear-gradient(var(--a1-1-soft),var(--a2-1-soft))}.slide::after{content:"";position:absolute;bottom:0;left:0;right:0;height:8px;background:linear-gradient(to right,var(--a1) 0 50%,var(--a2) 50%)}
.slide .page{inset:75px 94px;gap:0}
.slide .head.center{position:absolute;left:0;right:0;top:76px;gap:0}
.slide .head.center .title{font-size:var(--type-64);font-weight:var(--confluence-head-weight);line-height:var(--title-line);letter-spacing:var(--confluence-center-track);color:var(--a1)}
.slide .head.center .title b{color:var(--a2)}
.slide .head.center .kicker{order:2;margin-top:6px;font-size:var(--type-10);letter-spacing:var(--confluence-caps-track);color:var(--n-7)}
.slide .head.center .seat{position:absolute;left:465px;top:-127px;width:160px;height:126px}
.slide .head.center::before,.slide .head.center::after{content:"";position:absolute;top:40px;width:36.3%;border-top:var(--stroke) solid var(--n-3)}
.slide .head.center::before{left:0}.slide .head.center::after{right:0}
.slide .head.center+.body{margin-top:197px}
.slide.cover .page{inset:0}
.slide.cover .lockup{left:701px;top:166px;width:525px;max-width:none;transform:none;gap:0;display:block}
.slide.cover .lockup>.kicker{font-size:var(--type-8);letter-spacing:var(--confluence-caps-track);color:var(--n-5);margin-bottom:8px}
.slide.cover .lockup>.lead{font-size:clamp(var(--type-44),3.671875cqw,var(--type-48));line-height:var(--confluence-sub-line);letter-spacing:var(--confluence-cover-subtrack);font-weight:var(--confluence-cover-subweight);color:var(--n-7)}
.slide.cover .lockup>.title{font-size:var(--type-128);font-weight:var(--confluence-cover-weight);line-height:var(--confluence-cover-line);letter-spacing:var(--confluence-cover-track);height:253px;margin-top:8px;color:var(--ink)}
.slide.cover .lockup>.title>b{color:var(--a1)}.slide.cover .lockup>.title>b>b{color:var(--a2)}
.slide.cover .lockup>.label{display:block;font-size:var(--type-16);letter-spacing:var(--confluence-cover-note-track);margin-top:-1.5px;line-height:var(--body-line)}
.slide.cover .lockup>.src{display:block;margin-top:8px;width:433px;font-size:var(--type-8);line-height:var(--body-line);letter-spacing:var(--confluence-tiny-track);color:var(--n-7)}
.slide.cover .seat.portrait{position:absolute;left:108px;top:111px;width:510px;height:520px;border-radius:0}
.slide.cover .seat.logo{position:absolute;right:23px;top:22px;width:35px;height:36px;border-radius:0}
.slide:has(.rail) .page{left:420px}
.slide .rail{position:absolute;left:-326px;top:0;bottom:0;width:232px;display:block}
.slide .rail::after{content:"";position:absolute;left:279px;top:1px;bottom:1px;border-left:var(--stroke) solid var(--n-3)}
.slide .rail>.seat{width:130px;height:145px;border-radius:0}
.slide .rail>.title{margin-top:17px;font-size:var(--type-60);font-weight:var(--confluence-side-weight);line-height:var(--confluence-side-line);letter-spacing:var(--confluence-side-track);color:var(--a1);height:125px}
.slide .rail>.title b{color:var(--a2)}
.slide .rail>.kicker{font-size:var(--type-10);letter-spacing:var(--confluence-caps-track);margin-top:8px;color:var(--a1-3)}
.slide .rail>.lead{font-size:clamp(var(--type-12),1.015625cqw,var(--type-14));line-height:var(--body-line);letter-spacing:var(--confluence-side-note-track);margin-top:21px;color:var(--n-7)}
''')
tokens('afterglow',{'--afterglow-section-line':'1.1','--afterglow-meta-line':'1.65','--afterglow-cover-track':'-.021739em','--afterglow-cover-line':'1.35','--afterglow-cover-weight':'300','--afterglow-cover-boldweight':'750','--afterglow-header-track':'0em','--afterglow-section-track':'-.01em','--afterglow-cover-lead-track':'-.028571em'})
foundation('afterglow','''/* Source frame, three-part top line, split covers and central closing. */
.slide{background:var(--n-5)}
.slide .page{inset:27px;border:var(--stroke) solid var(--ink);border-radius:var(--radius);padding:100px 32px 32px;background:linear-gradient(to top,var(--a1),var(--n-2) 30px,var(--page) 64px);box-shadow:16px 19px 25px color-mix(in srgb,var(--n-9) 32%,transparent);overflow:hidden;gap:0}
.slide .top{position:absolute;top:17px;left:32px;right:32px;height:14px;font-size:var(--type-12);font-weight:var(--body-weight);letter-spacing:var(--afterglow-header-track);color:var(--a1)}
.slide .top .sec{position:absolute;left:50%;transform:translateX(-50%)}
.slide .head{gap:12px;height:320px;flex:none;padding-top:30px}.slide .head .title{font-size:clamp(var(--type-44),3.59375cqw,var(--type-48));font-weight:var(--afterglow-cover-weight);line-height:var(--afterglow-cover-line);letter-spacing:var(--afterglow-cover-track);color:var(--ink)}.slide .head .title b{font-weight:var(--afterglow-cover-boldweight);color:inherit}
.slide .head:has(>.lead){position:absolute;left:32px;right:32px;top:130px;height:100px;padding-top:0;gap:0}
.slide .head:has(>.lead) .title{font-size:var(--type-56);line-height:var(--afterglow-section-line);letter-spacing:var(--afterglow-section-track);font-weight:var(--body-weight)}
.slide .head:has(>.lead) .lead{font-size:var(--type-32);line-height:var(--afterglow-section-line)}.slide .head:has(>.title:empty) .lead{margin-top:134px}
.slide .head:has(>.lead)+.body{margin-top:0}
.slide.cover .lockup{left:32px;top:130px;transform:none;max-width:100%;gap:0;display:block}
.slide.cover .lockup>.title{font-size:clamp(var(--type-44),3.59375cqw,var(--type-48));font-weight:var(--afterglow-cover-weight);line-height:var(--afterglow-cover-line);letter-spacing:var(--afterglow-cover-track);color:var(--ink)}
.slide.cover .lockup>.title b{font-weight:var(--afterglow-cover-boldweight);color:inherit}
.slide.cover .body{position:absolute;left:32px;right:32px;top:421px;bottom:32px;border-top:var(--stroke) solid var(--n-6)}
.slide.on .page{background:var(--a1);color:var(--a1-on)}.slide.on .top{color:var(--a1-on)}.slide.on .head .title{color:var(--a1-on)}
.slide .head:not(:has(>.lead))+.body::before{content:"";position:absolute;left:-32px;right:-32px;top:0;border-top:var(--stroke) solid var(--n-6)}
.slide .foot:has(>.src:only-child){left:0;right:0;top:489px;bottom:auto;justify-content:center;text-align:center;font-size:var(--type-14);line-height:var(--afterglow-meta-line)}
.slide:has(.head>.lead) .body::before,.slide:has(.foot>.src:only-child) .body::before{content:"";position:absolute;left:-32px;right:-32px;top:321px;border-top:var(--stroke) solid var(--n-6)}
''')
print('parent furniture refreshed')
