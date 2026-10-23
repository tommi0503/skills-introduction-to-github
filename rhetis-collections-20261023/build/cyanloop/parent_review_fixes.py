from pathlib import Path
import re
C=Path('/workspace/output/cyanloop');W=Path('/workspace/work/cyanloop')
def css(folder,s):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+'\n'+s)
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide::before,.slide::after,.slide *::before,.slide *::after{box-sizing:border-box;}
.slide.cover .deco::before{background:conic-gradient(var(--a1-7),var(--a1) 90deg,var(--a2) 180deg,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 180deg,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 270deg,var(--a3) 270deg,var(--a1-7));}
.slide.cover .page.at-bottom-left::before{left:1015px;top:158px;width:392px;height:375px;background:radial-gradient(circle at 196px 336px,var(--a3) 0 39px,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 40px),conic-gradient(from 180deg,var(--a3),var(--a1-7) 90deg,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 90deg);}
''')
css('agenda','''
.agenda[data-el="cyanloop-agenda"].quiet.line .entry{position:relative;}
.agenda[data-el="cyanloop-agenda"].quiet.line .entry::after{content:'';flex:1;border-top:var(--stroke) dotted var(--n-5);margin:0 var(--gap-sm);order:-1;}
.agenda[data-el="cyanloop-agenda"].quiet.line .entry>.mark{margin-left:0;order:-2;}
''')
css('image-frame','''
.frame[data-el="cyanloop-image-frame"].line:not(.quiet) .seat{border:0;}
.frame[data-el="cyanloop-image-frame"].quiet:not(.line){width:247px;height:247px;margin-top:var(--cyanloop-space-30);}
.frame[data-el="cyanloop-image-frame"].quiet:not(.line) .seat{width:100%;height:100%;margin:0;}
.frame[data-el="cyanloop-image-frame"].quiet:not(.line):nth-child(1){margin-left:calc(var(--gap-sm)/2 - var(--stroke));}
.frame[data-el="cyanloop-image-frame"].quiet:not(.line):nth-child(2){margin-left:calc(0px - var(--cyanloop-space-11));}
.frame[data-el="cyanloop-image-frame"].quiet:not(.line):nth-child(3){margin-left:calc(0px - var(--cyanloop-space-27));}
.frame[data-el="cyanloop-image-frame"].quiet:not(.line):nth-child(4){margin-left:calc(0px - var(--cyanloop-space-43));}
.frame[data-el="cyanloop-image-frame"].quiet.line .seat{margin-top:0;}
''')
css('legend','''
.legend[data-el="cyanloop-legend"].col{justify-content:flex-start;padding-top:var(--gap-lg);padding-left:var(--cyanloop-space-74);}
.legend[data-el="cyanloop-legend"].col .key{font-size:var(--type-14);font-weight:var(--body-weight);}
''')
css('chart-bar',r'''
.bars[data-el="cyanloop-chart-bar"].line::after{content:counter(cyanloop-y100) '\A' counter(cyanloop-y80) '\A' counter(cyanloop-y60) '\A' counter(cyanloop-y40) '\A' counter(cyanloop-y20) '\A0';counter-reset:cyanloop-y100 var(--max) cyanloop-y80 calc(var(--max)*.8) cyanloop-y60 calc(var(--max)*.6) cyanloop-y40 calc(var(--max)*.4) cyanloop-y20 calc(var(--max)*.2);position:absolute;right:0;top:16px;white-space:pre;font-family:var(--font-body);font-size:var(--type-14);font-weight:var(--body-weight);line-height:calc((100cqh - var(--cyanloop-space-30) - var(--cyanloop-space-14))/5);color:var(--n-9);}
''')
css('card','''
.card[data-el="cyanloop-card"].on.quiet{width:362px;}
.card[data-el="cyanloop-card"].on.quiet:nth-child(1){margin-left:calc(var(--gap) - 3*var(--stroke));}
.card[data-el="cyanloop-card"].on.quiet:nth-child(2){margin-left:calc(var(--gap-sm)/2);}
.card[data-el="cyanloop-card"].on.quiet:nth-child(3){margin-left:calc(0px - var(--cyanloop-space-9));}
.card[data-el="cyanloop-card"].on.quiet .note .list{justify-content:flex-start;gap:var(--gap-sm);}
.card[data-el="cyanloop-card"].on.quiet .note .list .item{padding-left:var(--gap);padding-bottom:var(--gap-sm);border-bottom:var(--stroke) dotted var(--n-5);}
.card[data-el="cyanloop-card"].on.quiet .note .list .item:last-child{border-bottom:0;}
.card[data-el="cyanloop-card"].on.quiet .note .list .item::before{background:var(--a2-on);left:0;top:var(--gap-sm);}
.card[data-el="cyanloop-card"].on.quiet .note .list .name{font-size:var(--type-18);font-weight:var(--body-weight);color:inherit;text-align:left;}
.card[data-el="cyanloop-card"].quiet.line .note{font-size:var(--type-16);}
.card[data-el="cyanloop-card"].quiet.line:nth-child(3),.card[data-el="cyanloop-card"].quiet.line:nth-child(4){margin-top:calc(var(--gap-sm) + 3*var(--stroke));}
.card[data-el="cyanloop-card"].on.line{width:336px;height:136px;margin-left:var(--rail-w);margin-top:var(--gap);}
.card[data-el="cyanloop-card"].on.line.tone-1{margin-top:var(--gap);}
.card[data-el="cyanloop-card"].on.line.tone-2{margin-top:calc(var(--top-h));}
.card[data-el="cyanloop-card"].on.line.tone-3{margin-top:var(--gap-lg);}
.card[data-el="cyanloop-card"].on.line.tone-4{margin-left:calc(var(--gap-lg) - var(--stroke));}
''')
s=''
for i,(ang,width) in enumerate([(42.8,202),(0,148),(-42.4,200),(137.2,202),(180,148),(222.4,200)],2):
 edge='left:100%;right:auto;' if i<5 else 'left:0;right:auto;'
 s+=f'.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child({i})::before{{{edge}top:50%;width:{width}px;height:0;background:none;border:0;border-top:var(--stroke) dotted var(--n-5);transform:rotate({ang}deg);transform-origin:left center;}}\n'
s+='''.hub[data-el="cyanloop-hub"].quiet.line .spoke::before{background:none;border:0;border-top:var(--stroke) dotted var(--n-5);height:0;}'''
css('hub',s)
css('timeline','''
.track[data-el="cyanloop-timeline"].on .stop::before{width:12px;height:12px;background:none;clip-path:none;border-top:var(--stroke) solid var(--a1);border-right:var(--stroke) solid var(--a1);transform:rotate(45deg);}
''')
css('person','''
.people[data-el="cyanloop-person"].on>.person>.seat.portrait{clip-path:polygon(40% 0,65% 0,72% 4%,75% 10%,70% 16%,92% 20%,100% 32%,93% 53%,78% 57%,80% 100%,25% 100%,24% 58%,4% 55%,0 36%,12% 21%,37% 16%,30% 10%,32% 4%);}
''')
css('roadmap','''
.roadmap[data-el="cyanloop-roadmap"].on .lane::before{content:'';position:absolute;right:100%;top:0;width:217px;height:1px;background:var(--n-3);}
.roadmap[data-el="cyanloop-roadmap"].on .lane:last-child::after{content:'';position:absolute;right:100%;bottom:0;width:217px;height:1px;background:var(--n-3);}
''')
p=W/'reassembly.py';s=p.read_text();idx=s.index('\nfor n in range(1,19):')
insert='''
# Four cards occupy overlapping grid reservations, while their visible surfaces remain separated.
q7=[('맞춤형 교육 설계','기업의 업종과 조직 문화, 교육 목표를 분석하여<br>최적의 커리큘럼을 설계합니다.','clipboard-check'),('실무 중심 커리큘럼','현업 사례와 프로젝트 기반 학습으로 교육 내용을<br>실제 업무에 바로 적용할 수 있습니다.','chart-pie'),('전문 강사진','풍부한 실무 경험과 교육 노하우를 갖춘 전문 강사진이<br>교육을 진행합니다.','users'),('교육 성과 관리','교육 만족도 조사와 성과 분석을 통해 지속적인 교육<br>개선과 효과를 지원합니다.','presentation')]
P[7]=''.join(el('card','card','<div class="parts"><span class="mark"><span class="icon" data-icon="'+ico+'"></span></span><p class="kick">Keyword '+str(i+1)+'</p><p class="name">'+a+'</p><p class="note">'+b+'</p></div>',1+(i%2)*6,2+(i//2)*2,6,3,variant='quiet line '+('tone-3' if i in (1,2) else '')) for i,(a,b,ico) in enumerate(q7))+el('callout','callout','<p>미리HRD는 기업의 목표와 구성원의 성장을 연결하는 맞춤형 교육 솔루션을 제안합니다.</p>',1,6,12,1,variant='quiet')
P[5]=P[5].replace('<p class="note">현업 최적화 직무 스킬 강화<br><br>실무 적용률을 높이는 문제 해결 훈련<br><br>직무별 핵심 역량 모델링 구축</p>','<div class="note">'+listel([('현업 최적화 직무 스킬 강화',''),('실무 적용률을 높이는 문제 해결 훈련',''),('직무별 핵심 역량 모델링 구축','')],'divided')+'</div>')
P[10]=P[10].replace('grid-row:2 / span 3','grid-row:2 / span 4')
P[16]=P[16][:P[16].index('<div class="group two"')]+''.join(el('card','card','<div class="parts"><p class="kick">Keyword '+str(i+1)+'</p><p class="name">'+a+'</p><p class="fig">'+b+'</p></div>',5 if i%2==0 else 9,[2,3,5][i//2],5 if i%2==0 else 4,[2,3,2][i//2],variant='on line tone-'+str(i//2+1)+(' tone-4' if i%2 else '')) for i,(a,b) in enumerate([('교육 만족도','4.8 / 5.0'),('교육 수료율','97%'),('업무 적용률','89%'),('교육 추천 의향','95%'),('연간 학습 운영','120H'),('키워드 입력','00%')]))
'''
s=s[:idx]+insert+s[idx:];s=s.replace("' at-bottom-left' if n in (11,13,15)","' at-bottom-left' if n in (11,12,13,15)")
s=s.replace("html='<!doctype html>","body=re.sub(r'data-ph=\"\\d+\"','data-ph=\"\"',body)\n html='<!doctype html>")
p.write_text(s)
