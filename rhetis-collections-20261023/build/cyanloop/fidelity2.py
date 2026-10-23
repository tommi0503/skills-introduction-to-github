from pathlib import Path
C=Path('/workspace/output/cyanloop');W=Path('/workspace/work/cyanloop')
f=C/'elements/hub/element.css'
s='''
/* Connected-disc process: a diagram with explanations on either side. */
.hub[data-el="cyanloop-hub"].line{display:block;padding:0;overflow:hidden;}
.hub[data-el="cyanloop-hub"].line::before{content:'';position:absolute;left:28.7%;top:21.8%;width:450px;height:447px;background:linear-gradient(90deg,var(--a1) 0%,var(--a2) 42%,var(--a1-7) 72%);clip-path:path('M121 3C187 -4 199 79 273 67C330 58 396 35 433 98C478 175 400 211 423 278C458 367 419 443 330 443C249 442 226 361 263 287C292 227 242 189 188 199C122 215 115 254 150 292C178 327 165 358 126 355C91 353 58 330 84 290C109 246 42 257 20 218C-13 150 52 125 75 98C101 71 66 22 121 3Z');}
.hub[data-el="cyanloop-hub"].line::after{content:'';position:absolute;left:38.9%;top:44.4%;width:196px;height:210px;border-radius:43% 55% 50% 40%;background:var(--page);}
.hub[data-el="cyanloop-hub"].line .core{position:absolute;z-index:2;left:41%;top:55%;width:14%;height:auto;min-height:70px;display:flex;background:none;color:var(--ink);padding:0;border-radius:0;}
.hub[data-el="cyanloop-hub"].line .core .name{font-family:var(--font-display);font-size:var(--type-40);white-space:nowrap;}
.hub[data-el="cyanloop-hub"].line .spoke{display:contents;}
.hub[data-el="cyanloop-hub"].line .spoke::before{display:none;}
.hub[data-el="cyanloop-hub"].line .spoke>.mark{position:absolute;z-index:3;border-radius:50%;background:var(--page);border:10px solid var(--a1);display:flex;align-items:center;justify-content:center;}
.hub[data-el="cyanloop-hub"].line .spoke>.mark .icon{width:55%;height:55%;}
.hub[data-el="cyanloop-hub"].line .spoke>.name,.hub[data-el="cyanloop-hub"].line .spoke>.note{position:absolute;display:block;font-family:var(--font-body);color:var(--ink);}
.hub[data-el="cyanloop-hub"].line .spoke>.name{font-size:var(--type-20);}
.hub[data-el="cyanloop-hub"].line .spoke>.note{font-size:var(--type-18);line-height:var(--body-line);font-weight:var(--body-weight);}
.hub[data-el="cyanloop-hub"].line .spoke>.name .kick{font-size:var(--type-18);font-weight:var(--body-weight);margin-right:var(--gap-sm);}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(2)>.mark{left:37.8%;top:22.6%;width:132px;height:132px;border-color:var(--a2);color:var(--a2);}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(3)>.mark{left:29.9%;top:49.5%;width:108px;height:108px;color:var(--a1);}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(4)>.mark{left:35.2%;top:70.2%;width:80px;height:80px;border-width:8px;color:var(--a1);}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(5)>.mark{left:53%;top:30.1%;width:166px;height:166px;border-width:14px;border-color:var(--a1-7);color:var(--a1-7);}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(6)>.mark{left:50.2%;top:69%;width:192px;height:192px;border-width:16px;border-color:var(--a1-7);color:var(--a1-7);}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(2)>.name{left:0;top:29%;width:35.3%;text-align:right;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(2)>.note{left:0;top:35%;width:36.2%;text-align:right;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(3)>.name{left:0;top:52%;width:28%;text-align:right;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(3)>.note{left:0;top:58%;width:28.5%;text-align:right;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(4)>.name{left:0;top:74.5%;width:30.5%;text-align:right;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(4)>.note{left:0;top:81%;width:31.5%;text-align:right;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(5)>.name{left:69.7%;top:29%;width:30%;text-align:left;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(5)>.note{left:69.7%;top:35%;width:30%;text-align:left;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(6)>.name{left:69.7%;top:74.5%;width:30%;text-align:left;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(6)>.note{left:69.7%;top:81%;width:30%;text-align:left;}
/* Semicircular leadership diagram. The large centre surface is deliberately cropped by its own root. */
.hub[data-el="cyanloop-hub"].on{display:block;padding:0;overflow:hidden;}
.hub[data-el="cyanloop-hub"].on .core{position:absolute;left:26.2%;top:58%;width:47.6%;height:42%;background:none;border-radius:0;padding:var(--gap-lg) var(--gap) 0;display:flex;justify-content:flex-start;gap:var(--gap);color:var(--a1-on);z-index:2;font-family:var(--font-body);}
.hub[data-el="cyanloop-hub"].on .core::before{content:'';position:absolute;left:0;top:0;width:100%;aspect-ratio:1;border-radius:50%;background:var(--a1-7);border:10px solid var(--n-4);z-index:-1;}
.hub[data-el="cyanloop-hub"].on .core .name{font-size:var(--type-20);font-weight:var(--name-weight);}
.hub[data-el="cyanloop-hub"].on .core .note{font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);}
.hub[data-el="cyanloop-hub"].on .core .kick{font-size:var(--type-16);font-weight:var(--body-weight);color:inherit;}
.hub[data-el="cyanloop-hub"].on .spoke{position:absolute;width:18.3%;aspect-ratio:1;height:auto;border-radius:50%;padding:var(--gap);background:var(--a1);color:var(--a1-on);gap:var(--gap);z-index:1;}
.hub[data-el="cyanloop-hub"].on .spoke .name{font-size:var(--type-20);}
.hub[data-el="cyanloop-hub"].on .spoke .note{font-size:var(--type-18);line-height:var(--body-line);}
.hub[data-el="cyanloop-hub"].on .spoke::before{display:none;}
.hub[data-el="cyanloop-hub"].on .spoke:nth-child(2){left:1.55%;top:62.5%;}
.hub[data-el="cyanloop-hub"].on .spoke:nth-child(3){left:13.95%;top:34%;background:var(--a2);color:var(--a2-on);}
.hub[data-el="cyanloop-hub"].on .spoke:nth-child(4){left:31.3%;top:17.7%;background:var(--a3-7);color:var(--a3-on);}
.hub[data-el="cyanloop-hub"].on .spoke:nth-child(5){left:51.45%;top:17.7%;background:var(--a2);color:var(--a2-on);}
.hub[data-el="cyanloop-hub"].on .spoke:nth-child(6){left:68.8%;top:34%;}
.hub[data-el="cyanloop-hub"].on .spoke:nth-child(7){left:81.2%;top:62.5%;background:var(--a3-7);color:var(--a3-on);}
'''
f.write_text(f.read_text()+s)
# Source-specific arrangement uses foundation modifiers already in the vocabulary.
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''
.slide .page.overrides.at-bottom-left{padding-bottom:0;}
.slide .page.overrides .head:has(.label){display:block;}
.slide .page.overrides .head:has(.label) .title{display:flex;align-items:baseline;gap:var(--gap);}
.slide .page.overrides .head:has(.label) .title .label{font-size:var(--type-68);transform:scaleX(.86);transform-origin:left center;white-space:nowrap;}
.slide .page.overrides .head:has(.label) .title .lead{font-family:var(--font-body);font-size:var(--type-16);margin-left:calc(0px - var(--rail-w));}
.slide .page.overrides .head:has(.label)>.lead{position:absolute;right:0;top:var(--gap-lg);font-size:var(--type-18);text-align:right;color:var(--ink);}
''')
f=W/'reassembly.py';t=f.read_text();idx=t.index('\nfor n in range(1,19):')
insert='''
def spoke(name,note,ico=''):
 return '<div class="spoke">'+('<span class="mark"><span class="icon" data-icon="'+ico+'"></span></span>' if ico else '')+'<span class="name">'+name+'</span><span class="note">'+note+'</span></div>'
P[11]=el('hub','hub','<div class="core"><span class="name">Miri HRD</span></div>'+''.join(spoke(a,b,k) for a,b,k in [('<span class="kick">Step 3.</span>교육 운영','온·오프라인 교육 진행 학습 참여 관리','network'),('<span class="kick">Step 2.</span>교육 설계','맞춤형 커리큘럼 구성 교육 일정 및 방식 설계','clipboard-check'),('<span class="kick">Step 1.</span>교육 니즈 분석','조직 및 직무 요구사항 분석 현황 진단 및 요구 조사<br>직무 요구사항 분석 현황 진단 및 요구 조사','pencil-line'),('<span class="kick">Step 4.</span>성과 평가','만족도 및 학습 성취도 평가를 통해 교육 참여자의<br>전반적인 교육 경험과 이해도를 확인하고,<br>교육 전·후 역량 향상 결과를 분석하여 실질적인<br>성장 효과를 검증<br>이를 바탕으로 교육 효과를 종합적으로 측정하고,<br>향후 교육 과정 및 콘텐츠 개선에 반영','timer'),('<span class="kick">Step 5.</span>사후 관리','교육 결과와 참여자 피드백을 바탕으로 개선안을<br>도출하고 이를 반영하여 교육 품질을 높일 수 있는<br>차기 교육 계획을 수립합니다.','clipboard-pen')]),variant='line')
P[13]=el('hub','hub','<div class="core"><span class="kick">Effective Leadership</span><span class="name">조직의 성과를 이끄는 핵심 리더 역량</span><span class="note">대상과 조직에 맞춰 핵심 역량을 중심으로<br>맞춤형 리더십 교육 프로그램을 설계합니다.</span></div>'+''.join(spoke(a,b) for a,b in [('전략적 사고','조직 목표를 이해하고<br>장기적인 방향을<br>설정하는 역량'),('성과관리','목표 수립과 성과 점검으로<br>지속적인 개선을<br>이끄는 역량'),('코칭 & 피드백','구성원의 성장을 지원하고<br>동기를 부여하는<br>코칭 및 피드백 역량'),('커뮤니케이션','신뢰를 기반으로<br>원활하게 소통하고<br>협업을 이끄는 역량'),('변화관리','환경에 유연하게 대응하고<br>조직의 변화를<br>주도하는 역량'),('문제 해결','상황 분석과 합리적인<br>의사결정을 통해<br>문제를 해결하는 역량')]),variant='on')
'''
t=t[:idx]+insert+t[idx:];t=t.replace("(' overrides' if n in (6,) else '')","(' overrides'+(' at-bottom-left' if n==13 else '') if n in (6,11,13) else '')")
t=t.replace("{titles[n-1]}</h1><p class=\"lead\">{subs[n-1]}","{('<span class=\"label\">'+titles[n-1]+'</span><span class=\"lead\">'+subs[n-1]+'</span>') if n in (11,13) else titles[n-1]}</h1><p class=\"lead\">{('교육 설계부터 성과 분석까지 체계적으로 운영합니다.<br>전 과정을 체계적으로 관리하여 교육 효과를 극대화합니다.' if n==11 else '효과적인 리더는 다양한 역량의 균형 있는 성장을 통해<br>조직과 구성원의 성과를 이끌어냅니다.' if n==13 else subs[n-1])}")
t=t.replace('--a1-7:#d8f9ff;--a2-7:#d8e4ff;--a3-7:#b5fff3;', '--a1-7:#f5f5f5;--a1-on:#001134;--a2-7:#d8e4ff;--a3-7:#2bd4c8;--a3-on:#f5f5f5;')
f.write_text(t)
