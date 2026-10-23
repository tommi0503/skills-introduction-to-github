from pathlib import Path
W=Path('/workspace/work/cyanloop');C=Path('/workspace/output/cyanloop')
def css(folder,s):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+'\n'+s)
css('card','''
.card[data-el="cyanloop-card"].on.quiet{height:306px;align-self:end;padding:var(--pad);background:var(--a1);color:var(--a1-on);border:0;}
.card[data-el="cyanloop-card"].on.quiet .parts{display:flex;flex-direction:column;align-items:center;justify-content:flex-start;gap:var(--gap);text-align:center;}
.card[data-el="cyanloop-card"].on.quiet .kick{font-size:var(--type-18);color:inherit;margin-top:var(--gap-sm);}
.card[data-el="cyanloop-card"].on.quiet .name{font-size:var(--type-22);min-height:0;}
.card[data-el="cyanloop-card"].on.quiet .note{font-size:var(--type-18);min-height:0;line-height:var(--body-line);}
.card[data-el="cyanloop-card"].on.quiet.tone-2{background:var(--a2);color:var(--a2-on);}
.card[data-el="cyanloop-card"].on.quiet.tone-3{background:var(--n-2);color:var(--n-9);}
.card[data-el="cyanloop-card"].on.quiet.tone-3 .note{margin-top:var(--gap-lg);}
.card[data-el="cyanloop-card"].quiet.line{border:0;background:var(--n-1);padding:var(--gap) var(--gap-lg);}
.card[data-el="cyanloop-card"].quiet.line .parts{display:grid;grid-template-columns:138px 1fr;grid-template-rows:auto auto auto;gap:var(--gap-sm) var(--gap);align-content:center;align-items:center;}
.card[data-el="cyanloop-card"].quiet.line .mark{grid-column:1;grid-row:1/4;width:138px;height:138px;border-radius:50%;background:var(--a1);color:var(--a1-on);margin:0;}
.card[data-el="cyanloop-card"].quiet.line .mark .icon{width:52px;height:52px;}
.card[data-el="cyanloop-card"].quiet.line .kick{grid-column:2;font-size:var(--type-16);color:var(--n-6);}
.card[data-el="cyanloop-card"].quiet.line .name{grid-column:2;font-size:var(--type-22);min-height:0;color:var(--n-9);}
.card[data-el="cyanloop-card"].quiet.line .note{grid-column:2;font-size:var(--type-18);min-height:0;color:var(--n-9);}
.card[data-el="cyanloop-card"].quiet.line.tone-3 .mark{background:var(--a3-7);color:var(--page);}
''')
css('callout','''
.callout[data-el="cyanloop-callout"].on{display:flex;align-items:flex-start;justify-content:center;background:none;padding:30px 0 0;border:0;position:relative;}
.callout[data-el="cyanloop-callout"].on p{position:relative;background:var(--a1-7);color:var(--page);height:54px;border-radius:999px;display:flex;align-items:center;justify-content:center;padding:0 var(--gap-lg);font-size:var(--type-22);z-index:1;}
.callout[data-el="cyanloop-callout"].on::before{content:'';position:absolute;width:65%;height:28px;top:113px;left:17.5%;border:var(--stroke) solid var(--n-5);border-bottom:0;}
.callout[data-el="cyanloop-callout"].on::after{content:'';position:absolute;width:1px;height:58px;top:84px;left:50%;background:var(--n-5);}
.callout[data-el="cyanloop-callout"].quiet{height:70px;padding:0 var(--gap);align-self:end;margin-bottom:calc(0px - var(--gap-sm)/2);background:var(--a1-7);color:var(--page);border:0;border-radius:999px;display:flex;align-items:center;justify-content:center;}
.callout[data-el="cyanloop-callout"].quiet p{font-size:var(--type-24);font-weight:var(--name-weight);}
''')
css('pyramid','''
.pyramid[data-el="cyanloop-pyramid"].on{display:block;padding:0;position:relative;}
.pyramid[data-el="cyanloop-pyramid"].on .level{position:absolute;left:0;top:116px;width:100%;height:77px;display:block;flex:none;background:none;padding:0;border-radius:0;}
.pyramid[data-el="cyanloop-pyramid"].on .level>.name{position:absolute;left:348px;top:0;width:318px;height:77px;border-radius:999px;background:var(--n-1);color:var(--n-9);font-size:var(--type-22);padding:0 29px 0 46px;display:flex;align-items:center;justify-content:space-between;}
.pyramid[data-el="cyanloop-pyramid"].on .level>.name small{font-size:var(--type-18);font-weight:var(--body-weight);}
.pyramid[data-el="cyanloop-pyramid"].on .level>.note{position:absolute;left:686px;top:24px;font-size:var(--type-18);color:var(--n-9);white-space:nowrap;}
.pyramid[data-el="cyanloop-pyramid"].on .level:nth-child(2){top:211px;}
.pyramid[data-el="cyanloop-pyramid"].on .level:nth-child(2)>.name{left:238px;width:428px;background:var(--a3-7);color:var(--page);}
.pyramid[data-el="cyanloop-pyramid"].on .level:nth-child(3){top:302px;}
.pyramid[data-el="cyanloop-pyramid"].on .level:nth-child(3)>.name{left:150px;width:516px;background:var(--a1);color:var(--a1-on);}
.pyramid[data-el="cyanloop-pyramid"].on .level:nth-child(4){top:393px;}
.pyramid[data-el="cyanloop-pyramid"].on .level:nth-child(4)>.name{left:64px;width:602px;background:var(--a2);color:var(--a2-on);}
''')
css('hub','''
.hub[data-el="cyanloop-hub"].quiet:not(.line){display:block;padding:0;}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .core{position:absolute;left:449px;top:195px;width:262px;height:262px;border-radius:50%;background:var(--a1-7);color:var(--page);gap:var(--gap);padding:var(--gap);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .core .name{font-family:var(--font-display);font-size:var(--type-36);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .core .note{font-family:var(--font-body);font-size:var(--type-18);line-height:var(--body-line);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke{position:absolute;left:2px;top:131px;width:430px;height:116px;border-radius:999px;background:var(--a1);color:var(--a1-on);display:flex;flex-direction:row;gap:0;text-align:left;padding:0;}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke .name{position:absolute;left:45px;top:32px;font-size:var(--type-20);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke .name small{display:block;font-size:var(--type-14);font-weight:var(--body-weight);margin-top:var(--stroke);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke .note{position:absolute;left:192px;top:32px;font-size:var(--type-16);line-height:var(--body-line);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke::before{left:100%;right:auto;top:50%;width:90px;border-top:var(--stroke) dotted var(--n-5);height:0;background:none;}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child(3){top:267px;background:var(--a2);color:var(--a2-on);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child(4){top:403px;}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child(n+5){left:728px;}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child(n+5)::before{left:auto;right:100%;}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child(5){top:131px;background:var(--a2);color:var(--a2-on);}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child(6){top:267px;}
.hub[data-el="cyanloop-hub"].quiet:not(.line) .spoke:nth-child(7){top:403px;background:var(--a2);color:var(--a2-on);}
.hub[data-el="cyanloop-hub"].quiet.line{display:block;padding:0;overflow:hidden;}
.hub[data-el="cyanloop-hub"].quiet.line::before,.hub[data-el="cyanloop-hub"].quiet.line::after{display:none;}
.hub[data-el="cyanloop-hub"].quiet.line .core{position:absolute;left:92px;top:184px;width:299px;height:299px;display:flex;background:var(--a1-7);color:var(--page);border-radius:50%;padding:var(--gap);gap:var(--gap);text-align:center;}
.hub[data-el="cyanloop-hub"].quiet.line .core .mark .icon{width:52px;height:52px;}
.hub[data-el="cyanloop-hub"].quiet.line .core .name{font-family:var(--font-body);font-size:var(--type-22);white-space:normal;}
.hub[data-el="cyanloop-hub"].quiet.line .core .note{font-size:var(--type-18);}
.hub[data-el="cyanloop-hub"].quiet.line .spoke{position:absolute;left:517px;top:128px;width:633px;height:89px;background:var(--a1);color:var(--a1-on);border-radius:999px;display:block;padding:0;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke>.name{position:absolute;left:36px;top:31px;width:auto;color:inherit;font-size:var(--type-22);text-align:left;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke>.name .kick{font-size:var(--type-14);color:inherit;margin-right:var(--gap-sm);}
.hub[data-el="cyanloop-hub"].quiet.line .spoke>.note{position:absolute;left:257px;top:33px;width:auto;color:inherit;font-size:var(--type-16);text-align:left;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke>.mark{position:absolute;right:40px;left:auto;top:20px;width:52px;height:52px;border:0;background:none;color:inherit;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke::before{content:'';display:block;position:absolute;left:-120px;right:auto;top:50%;width:120px;border-top:var(--stroke) dotted var(--n-5);height:0;background:none;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(2){left:479px;}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(3){top:234px;background:var(--a2);color:var(--a2-on);}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(4){top:340px;background:var(--a3-7);color:var(--page);}
.hub[data-el="cyanloop-hub"].quiet.line .spoke:nth-child(5){top:446px;}
''')
css('image-frame','''
.frame[data-el="cyanloop-image-frame"].quiet{display:flex;align-items:flex-start;justify-content:flex-start;padding:0;background:none;border:0;}
.frame[data-el="cyanloop-image-frame"].quiet .seat{width:247px;height:247px;max-width:none;max-height:none;border-radius:50%;aspect-ratio:1;margin-top:30px;border:5px solid var(--a1);}
.frame[data-el="cyanloop-image-frame"].quiet:nth-child(1) .seat{margin-left:5px;border-color:var(--a3-7);}
.frame[data-el="cyanloop-image-frame"].quiet:nth-child(2) .seat{margin-left:-11px;}
.frame[data-el="cyanloop-image-frame"].quiet:nth-child(3) .seat{margin-left:-27px;border-color:var(--a2);}
.frame[data-el="cyanloop-image-frame"].quiet:nth-child(4) .seat{margin-left:-43px;border-color:var(--a1-7);}
.frame[data-el="cyanloop-image-frame"].quiet.line .seat{width:460px;height:460px;border:0;margin:8px 0 0 10px;}
''')
css('timeline','''
.track[data-el="cyanloop-timeline"].on{display:block;padding:0;}
.track[data-el="cyanloop-timeline"].on::before{display:none;}
.track[data-el="cyanloop-timeline"].on .stop{position:absolute;left:65px;top:302px;width:249px;height:249px;border:0;border-radius:50%;background:var(--a3-7);color:var(--page);display:flex;justify-content:center;align-items:center;text-align:center;padding:var(--gap);gap:var(--gap-sm);}
.track[data-el="cyanloop-timeline"].on .stop .kick{font-size:var(--type-24);color:inherit;}
.track[data-el="cyanloop-timeline"].on .stop .name{font-size:var(--type-24);}
.track[data-el="cyanloop-timeline"].on .stop .note{font-size:var(--type-18);}
.track[data-el="cyanloop-timeline"].on .stop::before{left:calc(100% + var(--gap-sm));top:40%;width:12px;height:18px;border-radius:0;clip-path:polygon(0 0,100% 50%,0 100%);background:var(--a1);}
.track[data-el="cyanloop-timeline"].on .stop:last-child::before{display:none;}
.track[data-el="cyanloop-timeline"].on .stop:nth-child(2){left:345px;background:var(--a1);color:var(--a1-on);}
.track[data-el="cyanloop-timeline"].on .stop:nth-child(3){left:625px;background:var(--a2);color:var(--a2-on);}
.track[data-el="cyanloop-timeline"].on .stop:nth-child(4){left:905px;background:var(--a1-7);color:var(--page);}
''')
p=W/'reassembly.py';s=p.read_text();idx=s.index('\nfor n in range(1,19):')
insert='''
P[5]=el('callout','callout','<p>조직과 개인이 함께 성장하는 교육 체계를 구축합니다.</p>',1,2,12,2,variant='on')+group(['<div class="card on quiet tone-'+str(i+1)+'" data-el="cyanloop-card"><div class="parts"><p class="kick">Goal '+str(i+1)+'</p><p class="name">'+a+'</p><p class="note">'+b+'</p></div></div>' for i,(a,b) in enumerate([('조직 경쟁력 강화','기업 비즈니스 방향과 연계된 전략적 교육을<br>통해 실질적인 성과 향상을 도모합니다.<br>교육이 단순히 학습에 머무르지 않고,<br>조직의 경쟁력을 실질적으로 견인하는<br>비즈니스 임팩트를 창출하도록 설계합니다.'),('직무 전문성 향상','현업 최적화 직무 스킬 강화<br><br>실무 적용률을 높이는 문제 해결 훈련<br><br>직무별 핵심 역량 모델링 구축'),('미래 인재 육성','신입부터 리더까지, 개인의 성장이 조직의<br>미래가 되는 맞춤형 로드맵을 운영합니다.')])],1,3,12,4)
P[7]=group(['<div class="card quiet line '+('tone-3' if i in(1,2) else '')+'" data-el="cyanloop-card"><div class="parts"><span class="mark"><span class="icon" data-icon="'+ico+'"></span></span><p class="kick">Keyword '+str(i+1)+'</p><p class="name">'+a+'</p><p class="note">'+b+'</p></div></div>' for i,(a,b,ico) in enumerate([('맞춤형 교육 설계','기업의 업종과 조직 문화, 교육 목표를 분석하여<br>최적의 커리큘럼을 설계합니다.','clipboard-check'),('실무 중심 커리큘럼','현업 사례와 프로젝트 기반 학습으로 교육 내용을<br>실제 업무에 바로 적용할 수 있습니다.','chart-pie'),('전문 강사진','풍부한 실무 경험과 교육 노하우를 갖춘 전문 강사진이<br>교육을 진행합니다.','users'),('교육 성과 관리','교육 만족도 조사와 성과 분석을 통해 지속적인 교육<br>개선과 효과를 지원합니다.','presentation')])],1,2,12,4,'two')+el('callout','callout','<p>미리HRD는 기업의 목표와 구성원의 성장을 연결하는 맞춤형 교육 솔루션을 제안합니다.</p>',1,6,12,1,variant='quiet')
P[8]=el('pyramid','pyramid',''.join('<div class="level"><span class="name">'+a+'<small>'+b+'</small></span><span class="note">'+c+'</span></div>' for a,b,c in [('Executive','임원리더십','조직 전략 수립 · 의사결정 · 조직문화 구축'),('Manager','관리자 리더십','성과관리 · 코칭 및 피드백 · 팀 운영 · 문제 해결'),('Staff','실무 역량','직무 전문성 · 커뮤니케이션 · 업무 개선'),('New Employee','신입 온보딩','조직 적응 · 업무 기본기 · 기업문화 이해 · 비즈니스 매너')]),variant='on')+prose('신입부터 관리자, 리더까지 각 계층에서<br>요구되는 핵심 역량을 중심으로<br>단계별 교육 과정을 제공합니다.',1,2,4,1)+el('callout','callout','<p>미리HRD는 단계별 성장에 맞춘 교육으로 개인의 역량을 조직의 성과로 연결합니다.</p>',1,6,12,1,variant='quiet')
P[9]=el('hub','hub','<div class="core"><span class="name">Miri HRD</span><span class="note">기업의 목표와 특성에 맞춰<br>다양한 교육 분야를<br>맞춤형으로 제공합니다.</span></div>'+''.join(spoke(a+'<small>| '+e+'</small>',b) for a,e,b in [('리더십 교육','Leadership','리더의 역할과 성과 관리<br>의사결정 및 팀 운영 역량 강화'),('커뮤니케이션','Communication','효과적인 소통과 협업을 통해<br>원활한 업무 환경을 구축'),('디지털 역량','Digital Skills','AI · 데이터 활용 등 변화하는<br>업무 환경에 필요한 역량 개발'),('직무 전문 교육','Job Skills','직무별 역량과 전문성을 높여<br>업무 효율과 성과 향상을 지원'),('조직문화','Organization','기업의 핵심 가치와 비전공유<br>긍정적인 조직문화 조성'),('문제 해결','Problem Solving','분석력과 창의적 문제 해결<br>능력을 향상')]),variant='quiet')
P[10]=el('track','timeline',''.join('<div class="stop"><span class="kick">'+str(i+1)+'Q</span><span class="name">'+a+'</span><span class="note">'+b+'</span></div>' for i,(a,b) in enumerate([('조직 적응','신입 온보딩 · 기업문화<br>비즈니스 매너'),('직무 역량 강화','직무 전문교육<br>업무 프로세스'),('리더십 강화','성과관리<br>조직관리'),('성과 공유','우수사례 발표 · 성과 리뷰<br>차년도 계획')])),variant='on')+group(['<div class="frame quiet" data-el="cyanloop-image-frame">'+seat(i+1)+'</div>' for i in range(4)],1,2,12,3)
P[12]=el('frame','image-frame',seat(1),1,2,5,5,variant='quiet line')+el('hub','hub','<div class="core"><span class="mark"><span class="icon" data-icon="target"></span></span><span class="name">교육 목표</span><span class="note">기업문화와 업무 기본기를<br>이해하고 조직에 빠르게<br>적응할 수 있도록 지원</span></div>'+''.join(spoke('<span class="kick">Module '+str(i+1)+'.</span>'+a,b,ico) for i,(a,b,ico) in enumerate([('기업문화 이해','기업 비전 · 조직문화','book-open'),('비즈니스 기본기','업무 프로세스 · 문서 작성 · 비즈니스 매너','mail'),('커뮤니케이션','협업 · 피드백','messages-square'),('실무 적응','직무 이해 · 업무 실습 · 사례 학습','presentation')])),variant='quiet line')
'''
s=s[:idx]+insert+s[idx:];s=s.replace("if n in (6,11,13) else", "if n not in (1,2,3,18) else")
s=s.replace("if n in (11,13) else titles[n-1]", "if n not in (1,2,3,6,18) else titles[n-1]")
s=s.replace("if n==13 else subs[n-1])}", "if n==13 else '기업의 목표와 직무에 맞춰 다양한 교육 분야를 맞춤형으로 제공합니다.' if n==9 else '빠른 조직 적응과 안정적인 업무 시작을 지원합니다.' if n==12 else '')}")
p.write_text(s)
