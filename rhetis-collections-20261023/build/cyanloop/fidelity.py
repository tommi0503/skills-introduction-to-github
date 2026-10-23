from pathlib import Path
import json
C=Path('/workspace/output/cyanloop')
def app(name,s):p=C/'elements'/name/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
p=C/'foundation/foundation.css';s=p.read_text();s+='''
/* Image-led pages share the same contract grid while the heading occupies only its own region. */
.slide .page.overrides .head{position:absolute;left:var(--margin-x);right:var(--margin-x);top:calc(var(--top-h) + var(--margin-y) + 5 * var(--stroke));z-index:2;}
.slide .page.overrides .head>.kicker{position:fixed;}
.slide .page.overrides .body{flex:1;}
.slide .head>.kicker{left:calc(var(--margin-x) + var(--gap) + 5 * var(--stroke));top:calc(var(--furn-edge) + 2 * var(--stroke));font-size:var(--type-18);}
.slide .head>.kicker::before{content:'';position:absolute;left:calc(0px - var(--gap));top:calc(50% - 6px);width:12px;height:12px;border-radius:50%;background:var(--page);}
.slide .page::after{left:calc(var(--margin-x) + var(--rail-w) + var(--gap-lg) + var(--gap));}
.slide .title>.label{font-size:var(--type-56);}
'''
# Fixed is unsuitable in multi-slide sheets; anchor furniture to the slide instead.
s=s.replace('.slide .page.overrides .head>.kicker{position:fixed;}','.slide .page.overrides .head>.kicker{position:absolute;left:var(--gap);top:calc(0px - var(--top-h) - var(--gap-sm) - 3 * var(--stroke));}')
p.write_text(s)
app('card','''
.card[data-el="cyanloop-card"].quiet:is(.tone-1,.tone-2,.tone-3){width:180px;height:180px;max-width:none;max-height:none;border-radius:50%;background:var(--a1);color:var(--a1-on);padding:var(--gap);align-self:end;margin-bottom:calc(var(--gap-sm) / 2);}
.card[data-el="cyanloop-card"].quiet.tone-1{margin-left:calc(var(--gap-sm) / 2);}
.card[data-el="cyanloop-card"].quiet.tone-2{margin-left:var(--gap-sm);background:var(--a3-7);color:var(--page);}
.card[data-el="cyanloop-card"].quiet.tone-3{margin-left:calc(var(--gap-sm) * 1.5);}
.card[data-el="cyanloop-card"].quiet:is(.tone-1,.tone-2,.tone-3) .parts{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);text-align:center;}
.card[data-el="cyanloop-card"].quiet:is(.tone-1,.tone-2,.tone-3) .parts>.mark{width:52px;height:52px;background:none;color:inherit;border-radius:0;}
.card[data-el="cyanloop-card"].quiet:is(.tone-1,.tone-2,.tone-3) .mark .icon{width:52px;height:52px;}
.card[data-el="cyanloop-card"].quiet:is(.tone-1,.tone-2,.tone-3) .parts>.name{min-height:0;font-size:var(--type-18);font-weight:var(--name-weight);}
.card[data-el="cyanloop-card"].quiet:is(.tone-1,.tone-2,.tone-3) .parts>.note{display:none;min-height:0;}
''')
app('pill','''
.pill[data-el="cyanloop-pill"].on.line{width:calc(var(--rail-w) * 4);height:calc(var(--furn-edge) + var(--gap-sm));align-self:start;margin-top:calc(var(--stroke) * 5);padding:0 var(--gap);background:var(--a1-7);color:var(--page);border:0;}
.pill[data-el="cyanloop-pill"].on.line .mark,.pill[data-el="cyanloop-pill"].on.line .note{display:none;}
.pill[data-el="cyanloop-pill"].on.line .name{font-size:var(--type-20);}
''')
app('prose','''
.prose[data-el="cyanloop-prose"]{padding:0;}
.prose[data-el="cyanloop-prose"].lead.quiet{justify-content:flex-end;padding-bottom:calc(var(--pad) + 3 * var(--stroke));color:var(--ink);}
.prose[data-el="cyanloop-prose"].lead.quiet p{font-size:var(--type-18);}
''')
app('image-frame','''
.frame[data-el="cyanloop-image-frame"].on{padding:0;background:none;isolation:isolate;}
.frame[data-el="cyanloop-image-frame"].on .seat{width:min(95cqw,95cqh);height:min(95cqw,95cqh);border:0;transform:translateX(var(--pad));}
.frame[data-el="cyanloop-image-frame"].on::before{content:'';position:absolute;left:calc(50% + var(--pad));top:50%;width:min(100cqw,100cqh);height:min(100cqw,100cqh);transform:translate(-50%,-50%);border:18px solid var(--a3);border-radius:50%;clip-path:inset(0 50% 0 0);z-index:-1;}
''')
# Demonstrate each new allowed modifier combination in the library itself.
(C/'elements/card/fixtures/features-3-circles.html').write_text('<!-- min: 7x3 -->\n<div class="group" style="grid-column:1 / span 12; grid-row:1 / span 6">'+''.join(f'<div class="card quiet tone-{i+1}" data-el="cyanloop-card"><div class="parts"><span class="mark"><span class="icon" data-icon="{ico}"></span></span><p class="name">{name}</p></div></div>' for i,(name,ico) in enumerate([('Professional','badge-check'),('Practical','presentation'),('Partnership','network')]))+'</div>\n')
(C/'elements/pill/fixtures/pill-deep-capsule.html').write_text('<!-- min: 4x1 -->\n<div class="pill on line" data-el="cyanloop-pill" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="parts"><span class="name">기업과 함께 성장하는 교육 전문기관</span></div></div>\n')
(C/'elements/image-frame/fixtures/frame-image-led.html').write_text('<!-- min: 6x6 -->\n<div class="frame on" data-el="cyanloop-image-frame" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="seat" data-ph="1"></div></div>\n')
# Generate the 06 markup from contract elements; the original deck positions guide its spans.
p=Path('/workspace/work/cyanloop/reassembly.py');s=p.read_text()
insert='''
P[6]=prose('기업과 사람의 성장을 만드는 교육 파트너, MIRI HRD는 산업별 맞춤형 교육과<br>체계적인 운영 시스템으로 기업의 지속 가능한 성장을 지원합니다.',1,2,6,1)+el('pill','pill','<div class="parts"><span class="name">기업과 함께 성장하는 교육 전문기관</span></div>',1,3,4,1,variant='on line')+el('prose','prose','<p>MIRI HRD는 다양한 산업 분야의 기업 교육 경험을 바탕으로 조직의 목표와 직무에<br>맞는 맞춤형 교육 프로그램을 제공합니다. 교육 기획부터 운영, 성과 분석까지<br>전 과정을 체계적으로 지원하며, 기업의 인재 경쟁력 향상에 기여하고 있습니다.</p>',1,3,6,2,variant='lead quiet')+group(['<div class="card quiet tone-'+str(i+1)+'" data-el="cyanloop-card"><div class="parts"><span class="mark"><span class="icon" data-icon="'+ico+'"></span></span><p class="name">'+name+'</p></div></div>' for i,(name,ico) in enumerate([('Professional','badge-check'),('Practical','presentation'),('Partnership','network')])],1,4,6,3)+el('frame','image-frame',seat(1),7,1,6,6,variant='on')
'''
s=s.replace('for n in range(1,19):',insert+'\nfor n in range(1,19):')
s=s.replace("f'\"><div class=\"page\"><header class=\"head\">'", "f'\"><div class=\"page'+(' overrides' if n in (6,) else '')+'\"><header class=\"head\">'") if False else s
# Exact existing string in the builder.
s=s.replace("+f'\"><div class=\"page\"><header class=\"head\"><p class=\"kicker\">'", "+f'\"><div class=\"page'+(' overrides' if n in (6,) else '')+'\"><header class=\"head\"><p class=\"kicker\">'")
s=s.replace("orig+='--a1-7:#001134;--a2-7:#0753d6;--a3-7:#006c68;}","orig+='--a1-on:#f5f5f5;--a1-7:#001134;--a2-7:#0753d6;--a3-7:#2bd4c8;}")
p.write_text(s)
print('fidelity variants written')
