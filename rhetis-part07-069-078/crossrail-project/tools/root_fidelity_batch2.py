from pathlib import Path
import re
P=Path(__file__).parent;E=P/'crossrail/elements'
f=E/'steps/element.css';s=f.read_text()
# A container query reads content height after root padding; the source col root has 341px content.
# Restrict compact column rules to <=300px content while preserving 380px horizontal rich-step rules.
pat=r'\[data-el="crossrail-steps"\]\.col:has\(\.mark>\.icon\)[^{]*\{[^{}]*\}'
last=s.rfind('@container(max-height:380px)')
head=s[:last];tail=s[last:];cols=re.findall(pat,tail);tail=re.sub(pat,'',tail);s=head+tail+'\n@container(max-height:300px){'+''.join(cols)+'}\n'
s+='''\n[data-el="crossrail-steps"].col:has(.mark>.icon){padding-top:calc(var(--gap-lg) + var(--gap-sm)*5/6)}[data-el="crossrail-steps"].col:has(.mark>.icon)::before{top:calc(var(--gap-lg) + var(--gap-sm)*5/6)}[data-el="crossrail-steps"].col:has(.mark>.icon) .step::before{top:calc(var(--gap-sm)/6);bottom:calc(var(--gap-sm)/6)}[data-el="crossrail-steps"]:not(.col):not(:has(.name>.icon)) .mark{clip-path:polygon(0 0,calc(100% - var(--gap-sm)*11/6) 0,100% 50%,calc(100% - var(--gap-sm)*11/6) 100%,0 100%,calc(var(--gap-sm)*11/6) 50%)}[data-el="crossrail-steps"]:not(.col):not(:has(.name>.icon))[dir="rtl"] .mark{clip-path:polygon(calc(var(--gap-sm)*11/6) 0,100% 0,calc(100% - var(--gap-sm)*11/6) 50%,100% 100%,calc(var(--gap-sm)*11/6) 100%,0 50%)}\n'''
f.write_text(s)
f=P/'crossrail/foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide .body:has(>[data-el="crossrail-image-frame"]>.seat.avatar)::before{content:"";position:absolute;left:calc(var(--margin-x)*-1);right:calc(var(--margin-x)*-1);top:calc((100% - var(--gap-sm)*5)/4 + var(--gap-sm)*2/3);height:1px;background:var(--n-3);pointer-events:none;z-index:0}\n''')
f=E/'image-frame/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-image-frame"]:has(>.seat.avatar){background:var(--page)}\n')
