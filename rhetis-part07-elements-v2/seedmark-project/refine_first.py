"""Edit the new full-source generator, then emit complete element files."""
from pathlib import Path
P=Path(__file__).parent;p=P/'new_library.py';s=p.read_text()
s=s.replace('$ {display:flex;align-items:stretch;justify-content:center;padding:min(var(--pad),8cqw);isolation:isolate;}','$ {display:flex;align-items:stretch;justify-content:center;padding:0;isolation:isolate;}')
s=s.replace('$ .parts{width:100%;min-width:0;min-height:0;display:grid;grid-auto-rows:auto;align-content:center;gap:var(--gap-sm);}', '$ .parts{width:100%;height:100%;min-width:0;min-height:0;padding:min(var(--pad),8cqw);display:grid;grid-auto-rows:auto;align-content:center;gap:var(--gap-sm);}')
s=s.replace('$.on .note{color:var(--a1-on)}','$.on .parts>.note{color:var(--a1-on)}')
s=s.replace('$:has(>.parts>.mark):has(>.parts>.kick){padding:min(calc(var(--pad)*2.15625),21.77cqh) min(calc(var(--pad)*1.3125),11.8cqw) min(var(--gap),8cqh);}', '$:has(>.parts>.mark):has(>.parts>.kick){padding:0;}')
s=s.replace('$ .parts:has(>.mark):has(>.kick){grid-template-rows:26px minmax(0,21cqh) minmax(0,1fr);align-content:stretch;gap:var(--gap-sm);}', '$ .parts:has(>.mark):has(>.kick){padding:min(calc(var(--pad)*3.9),21.77cqh) min(calc(var(--pad)*3.9),11.8cqw) min(var(--gap),8cqh);grid-template-rows:min(7.9cqh,44px) minmax(0,21cqh) minmax(0,1fr);align-content:stretch;gap:var(--gap-sm);}')
s=s.replace('font-size:var(--type-32);text-align:center;', 'font-size:clamp(var(--type-24),min(9cqw,10cqh),var(--type-60));text-align:center;')
s=s.replace('$ .parts:has(>.mark):has(>.kick)>.kick{text-align:center;}', '$ .parts:has(>.mark):has(>.kick)>.kick{text-align:center;font-size:clamp(var(--type-12),min(4cqw,4.4cqh),var(--type-24));}\n$ .parts:has(>.mark):has(>.kick)>.note{font-size:clamp(var(--type-16),min(5.06cqw,5.68cqh),var(--type-28));}')
start=s.index("CSS['pill']=");end=s.index("CSS['headline']=",start)
s=s[:start]+'''CSS['pill']=\'\'\'
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
\'\'\'
''' +s[end:]
s=s.replace('$.cols{display:block;columns:2;column-gap:var(--gap-lg)}$.cols p{break-inside:avoid;margin-bottom:var(--gap)}', '$.cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--gap-lg);align-content:center;}$.cols p{grid-column:auto;}')
s=s.replace('$.cols{columns:1}', '$.cols p{grid-column:span 2}')
start=s.index("CSS['metric']=");end=s.index("CSS['tag']=",start)
s=s[:start]+'''CSS['metric']=\'\'\'
$.stat{padding:var(--gap-sm) 0;border-bottom:var(--stroke) solid var(--n-3);display:flex;align-items:center;}
$ .parts{display:grid;width:100%;grid-template-columns:28% minmax(0,1fr);grid-template-rows:auto auto;gap:calc(var(--gap-sm)/2) var(--gap-sm);align-content:center;}
$ .fig{grid-column:1;grid-row:1;font-size:clamp(var(--type-28),min(12cqw,33.33cqh),var(--type-40));line-height:var(--name-line);font-weight:var(--figure-weight);letter-spacing:var(--figure-track);}
$ .name{grid-column:1;grid-row:2;font-size:var(--type-16);line-height:var(--name-line);}
$ .note{grid-column:2;grid-row:1/span 2;font-size:clamp(var(--type-14),min(5cqw,18cqh),var(--type-18));line-height:var(--body-line);}
$.stats{display:flex;align-items:stretch;gap:var(--gap)}$.stats>.stat{flex:1;min-width:0;container-type:size;display:flex;align-items:center;padding:var(--gap);border-right:var(--stroke) solid var(--n-3);}
$.stats>.stat:last-child{border-right:0}
@container(max-aspect-ratio:3/1){$ .parts{grid-template-columns:28% minmax(0,1fr);grid-template-rows:auto auto;}$ .name{grid-column:2;grid-row:1;align-self:center;}$ .note{grid-column:1/span 2;grid-row:2;}}
@container(max-width:300px){$ .name{font-size:var(--type-14)}}
\'\'\'
'''+s[end:]
s=s.replace('$.tag{display:flex;align-items:center;justify-content:center;align-self:center;justify-self:center;width:max-content;max-width:100%;min-height:26px;height:max-content;', '$.tag{display:inline-flex;align-items:center;justify-content:center;align-self:center;justify-self:center;width:min(100%,96px);max-width:100%;min-height:26px;height:26px;')
s=s.replace('$ .key.tone-2:before', '@container(max-height:100px){$ .key{font-size:var(--type-10);}}\n$ .key.tone-2:before')
s=s.replace('gap:calc(var(--gap-sm)/3);padding:calc(var(--gap-sm)/2);', 'gap:calc(var(--gap-sm)/6);padding:calc(var(--gap-sm)/2);')
s=s.replace('@container(max-height:220px){$ .name{font-size:var(--type-16)}$ .note{font-size:var(--type-14)}}', '@container(max-height:350px){$ .item{padding-top:calc(var(--gap-sm)/6);padding-bottom:calc(var(--gap-sm)/6);gap:calc(var(--gap-sm)/4);}$ .name{font-size:var(--type-16)}$ .note{font-size:var(--type-14)}}')
# Equal tracks in figure cards preserve title starts despite variable note/name lengths.
s=s.replace('$ .parts>.list{min-height:0;}', '''$ .parts>.list{min-height:0;}
$ .parts:has(>.fig){height:min(100%,calc(var(--pad)*9));align-self:center;grid-template-rows:24px 52px 80px minmax(0,1fr);padding:0;gap:var(--gap-sm);}
$ .parts:has(>.fig)>.kick{grid-row:1;}$ .parts:has(>.fig)>.fig{grid-row:2;}$ .parts:has(>.fig)>.name{grid-row:3;}$ .parts:has(>.fig)>.note{grid-row:4;}
@container(max-height:350px){$ .parts:has(>.fig){height:100%;grid-template-rows:18px 34px 56px minmax(0,1fr);gap:calc(var(--gap-sm)/2);}$ .parts:has(>.fig)>.name{font-size:var(--type-20);}$ .parts:has(>.fig)>.fig{font-size:var(--type-28);}$ .parts:has(>.fig)>.note{font-size:var(--type-16);}}
''')
p.write_text(s)
