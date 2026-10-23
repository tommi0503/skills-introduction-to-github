from pathlib import Path
W=Path('/workspace/work/cyanloop');C=Path('/workspace/output/cyanloop')
def css(folder,s):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+'\n'+s)
p=C/'elements/card/element.css';s=p.read_text();s=s.replace('.quiet:is(.tone-', '.quiet:not(.on):not(.line):is(.tone-').replace('.quiet.tone-', '.quiet:not(.on):not(.line).tone-');p.write_text(s)
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide.cover .page.at-center{top:0;text-align:left;align-items:stretch;}
.slide.cover .page.at-bottom-left{bottom:auto;}
.slide.cover .page.overrides .deco{clip-path:inset(0 0 27px 0);}
.slide.cover .page.overrides::before{display:block;inset:0;height:720px;background:radial-gradient(circle at 801px 247px,var(--a3) 0 35px,transparent 36px),radial-gradient(circle at 1065px 160px,var(--a2) 0 35px,transparent 36px);z-index:1;pointer-events:none;}
.slide.cover .page.at-center .title{transform:scaleX(.8);}
''')
css('card','''
.card[data-el="cyanloop-card"].on.quiet{width:100%;border-radius:var(--radius);margin:0 0 13px;}
.card[data-el="cyanloop-card"].on.quiet .parts{height:100%;}
.card[data-el="cyanloop-card"].on.quiet .note{display:block;}
.card[data-el="cyanloop-card"].on.line{position:relative;width:calc(100% + var(--gap-sm));height:136px;margin-left:calc(0px - var(--gap) + var(--gap-sm)/2);align-self:start;padding:var(--gap);border:0;background:var(--n-1);color:var(--n-9);}
.card[data-el="cyanloop-card"].on.line .parts{position:relative;height:100%;display:block;}
.card[data-el="cyanloop-card"].on.line .kick{position:absolute;left:0;top:0;font-size:var(--type-16);color:var(--n-6);}
.card[data-el="cyanloop-card"].on.line .name{position:absolute;left:0;top:30px;font-size:var(--type-22);min-height:0;}
.card[data-el="cyanloop-card"].on.line .fig{position:absolute;right:0;top:57px;font-size:var(--type-48);color:var(--a2-7);}
.card[data-el="cyanloop-card"].on.line:nth-child(-n+2){margin-top:var(--gap);}
.card[data-el="cyanloop-card"].on.line:nth-child(3),.card[data-el="cyanloop-card"].on.line:nth-child(4){margin-top:var(--gap-sm);}
''')
css('table','''
.tablebox[data-el="cyanloop-table"].on{padding-top:29px;padding-bottom:8px;}
.tablebox[data-el="cyanloop-table"].on .table{font-size:var(--type-18);}
.tablebox[data-el="cyanloop-table"].on :is(th,td){text-align:center;padding:var(--gap-sm);}
.tablebox[data-el="cyanloop-table"].on th{background:var(--a2);color:var(--a2-on);}
.tablebox[data-el="cyanloop-table"].on td{background:var(--n-1);color:var(--n-9);}
.tablebox[data-el="cyanloop-table"].on td:first-child{background:var(--a1);color:var(--a1-on);}
.tablebox[data-el="cyanloop-table"].on :is(th,td):nth-child(1){width:20%;}
.tablebox[data-el="cyanloop-table"].on :is(th,td):nth-child(2){width:15%;}
.tablebox[data-el="cyanloop-table"].on :is(th,td):nth-child(3){width:34%;}
.tablebox[data-el="cyanloop-table"].on :is(th,td):nth-child(4){width:11%;}
.tablebox[data-el="cyanloop-table"].on :is(th,td):nth-child(5){width:20%;}
''')
css('metric','''
.stat[data-el="cyanloop-metric"].on{position:relative;display:block;padding:0;}
.stat[data-el="cyanloop-metric"].on .parts{position:relative;height:100%;display:block;}
.stat[data-el="cyanloop-metric"].on .fig{position:absolute;left:154px;top:167px;font-size:var(--type-128);color:var(--a1-7);transform:scaleX(.85);transform-origin:left top;white-space:nowrap;}
.stat[data-el="cyanloop-metric"].on .name{position:absolute;left:0;top:271px;font-size:var(--type-22);color:var(--n-9);}
.stat[data-el="cyanloop-metric"].on .note{position:absolute;left:4px;top:15px;font-size:var(--type-18);color:var(--n-9);white-space:nowrap;}
''')
css('list','''
.list[data-el="cyanloop-list"].divided.quiet{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,auto);grid-auto-flow:column;align-content:center;gap:4px var(--gap);padding-top:var(--gap-lg);border-top:var(--stroke) dotted var(--n-5);}
.list[data-el="cyanloop-list"].divided.quiet .item{border:0;padding:0 0 0 var(--gap-sm);}
.list[data-el="cyanloop-list"].divided.quiet .item::before{left:0;top:10px;background:var(--n-9);width:4px;height:4px;}
.list[data-el="cyanloop-list"].divided.quiet .item .name{font-size:var(--type-18);font-weight:var(--body-weight);color:var(--n-9);white-space:nowrap;}
''')
css('person','''
.people[data-el="cyanloop-person"].on{gap:var(--gap-sm);display:flex;}
.people[data-el="cyanloop-person"].on>.person{position:relative;display:block;padding:0;text-align:left;}
.people[data-el="cyanloop-person"].on>.person::before{content:'';position:absolute;left:0;right:0;top:34.45%;bottom:0;border-radius:190px 190px 0 0;background:var(--a1);}
.people[data-el="cyanloop-person"].on>.person:nth-child(2)::before{background:var(--a2);}
.people[data-el="cyanloop-person"].on>.person:nth-child(3)::before{background:var(--a1-7);}
.people[data-el="cyanloop-person"].on>.person>.seat.portrait{position:absolute;left:49%;top:15.38%;width:51%;height:84.62%;border:0;border-radius:0;max-width:none;max-height:none;aspect-ratio:auto;}
.people[data-el="cyanloop-person"].on>.person>.name{position:absolute;left:30px;top:60%;font-size:var(--type-24);color:var(--a1-on);}
.people[data-el="cyanloop-person"].on>.person>.note{position:absolute;left:110px;top:61%;font-size:var(--type-16);color:var(--a1-on);}
.people[data-el="cyanloop-person"].on>.person:nth-child(2)>:is(.name,.note){color:var(--a2-on);}
.people[data-el="cyanloop-person"].on>.person:nth-child(3)>:is(.name,.note){color:var(--page);}
.people[data-el="cyanloop-person"].on>.person>.note .kick{position:absolute;left:-80px;top:181px;font-family:var(--font-display);font-size:var(--type-24);color:inherit;white-space:nowrap;}
.people[data-el="cyanloop-person"].on>.person>.list{position:absolute;left:30px;top:67.7%;width:190px;height:26%;display:flex;justify-content:flex-start;gap:4px;}
.people[data-el="cyanloop-person"].on>.person>.list .item{padding-left:var(--gap-sm);}
.people[data-el="cyanloop-person"].on>.person>.list .item::before{left:0;top:10px;background:var(--a1-on);width:4px;height:4px;}
.people[data-el="cyanloop-person"].on>.person>.list .name{font-size:var(--type-16);font-weight:var(--body-weight);color:var(--a1-on);white-space:nowrap;}
.people[data-el="cyanloop-person"].on>.person:nth-child(2)>.list .name{color:var(--a2-on);}
.people[data-el="cyanloop-person"].on>.person:nth-child(3)>.list .name{color:var(--page);}
''')
css('roadmap','''
.roadmap[data-el="cyanloop-roadmap"].on{padding:104px 4px 6px 0;}
.roadmap[data-el="cyanloop-roadmap"].on .heads{margin-left:217px;height:74px;min-height:74px;padding:0;align-items:center;font-size:var(--type-20);}
.roadmap[data-el="cyanloop-roadmap"].on .lane{margin-left:217px;}
.roadmap[data-el="cyanloop-roadmap"].on .lane>.name{right:calc(100% + 5px);width:188px;font-size:var(--type-20);color:var(--n-9);}
.roadmap[data-el="cyanloop-roadmap"].on .bar{top:0;bottom:0;border-radius:0;padding:var(--gap-sm);}
.roadmap[data-el="cyanloop-roadmap"].on .bar span{font-size:var(--type-18);font-weight:var(--body-weight);}
.roadmap[data-el="cyanloop-roadmap"].on .bar.on{background:var(--a2);color:var(--a2-on);}
''')
css('image-frame','''
.frame[data-el="cyanloop-image-frame"].line:not(.quiet){display:flex;padding:0;align-items:flex-start;justify-content:flex-start;background:none;}
.frame[data-el="cyanloop-image-frame"].line:not(.quiet) .seat{width:calc(100% + 26px);height:281px;max-width:none;max-height:none;border-radius:var(--radius);margin-top:-7px;aspect-ratio:auto;}
''')
css('chart-bar','''
.bars[data-el="cyanloop-chart-bar"].line{padding:30px 30px 14px 57px;background:none;border:0;gap:0;}
.bars[data-el="cyanloop-chart-bar"].line::before{content:'';position:absolute;inset:30px 30px 14px 57px;background:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 20%);}
.bars[data-el="cyanloop-chart-bar"].line .bar::before{width:65%;}
.bars[data-el="cyanloop-chart-bar"].line .bar b{font-size:var(--type-16);bottom:calc(var(--v)/var(--max)*100% + var(--gap-sm));}
.bars[data-el="cyanloop-chart-bar"].line .bar span{font-size:var(--type-14);top:calc(100% + 6px);}
''')
css('chart-line','''
.lines[data-el="cyanloop-chart-line"].on{padding:30px 30px 14px 57px;background:none;border:0;}
.lines[data-el="cyanloop-chart-line"].on::after{inset:30px 30px 14px 57px;background:var(--a2);}
.lines[data-el="cyanloop-chart-line"].on .pt::before{background:var(--a2);}
.lines[data-el="cyanloop-chart-line"].on .pt b{font-size:var(--type-14);color:var(--a2-7);}
.lines[data-el="cyanloop-chart-line"].on .pt span{display:none;}
''')
css('legend','''
.legend[data-el="cyanloop-legend"].col{display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:var(--gap-sm);padding-left:var(--gap);font-size:var(--type-14);color:var(--n-9);}
''')
css('prose','''
.prose[data-el="cyanloop-prose"].quiet.line{justify-content:flex-start;gap:var(--gap);padding-top:24px;color:var(--n-9);}
.prose[data-el="cyanloop-prose"].quiet.line p{font-size:var(--type-18);}
.prose[data-el="cyanloop-prose"].quiet.line p:first-child{font-size:var(--type-22);font-weight:var(--name-weight);}
''')
p=W/'reassembly.py';s=p.read_text();idx=s.index('\nfor n in range(1,19):')
insert='''
P[4]=el('prose','prose','<p>급변하는 경영 환경에서 지속적인 역량 개발은<br>기업 경쟁력 확보의 핵심입니다.</p><p>교육 투자가 확대될수록 조직의 성과도 함께 성장합니다.<br>지속적인 교육은 조직의 경쟁력을 높이는 장기적인 성장 전략입니다.</p>',1,2,5,2,variant='quiet line')+el('frame','image-frame',seat(1),1,4,5,3,variant='line')+el('bars','chart-bar',''.join('<div class="bar" style="--v:'+str(v)+'"><b>'+str(v)+'</b><span>'+str(2080+i)+'</span></div>' for i,v in enumerate([55,61,68,74,81])),6,2,7,5,variant='line',data='; --max:100')+el('lines','chart-line',''.join('<div class="pt" style="--v:'+str(v)+'"><b>'+str(v)+'</b></div>' for v in [16,20,24,29,34]),6,2,7,5,variant='on',data='; --max:100')+el('legend','legend','<span class="key tone-1">기업 교육 투자 비중(%)</span><span class="key tone-2">교육 도입 후 평균 조직 성과 향상(%)</span>',6,2,5,1,variant='col')
P[14]=el('tablebox','table','<table class="table"><thead><tr>'+''.join('<th>'+a+'</th>' for a in ['교육 과정','교육 대상','주요 교육 내용','교육 시간','교육 방식'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table>',1,2,12,5,variant='on')
P[15]=el('people','person',''.join('<div class="person" data-el="cyanloop-person">'+seat(i+1,'portrait')+'<p class="name">'+a+'</p><p class="note">| '+b+'<span class="kick">'+eng+'</span></p>'+listel([(v,'') for v in c])+'</div>' for i,(a,b,c,eng) in enumerate([('김미리','책임교수',['HR 컨설팅 경력 15년','리더십 교육 350회+','대기업·공공기관 교육 운영'],'LEADERSHIP EXPERT'),('박미리','수석강사',['조직 커뮤니케이션 전문','기업 교육 500회+'],'BUSINESS COMMUNICATION'),('이미리','전문강사',['현업 실무 경력 12년','리더십 교육 200회+','직무교육 전문','프로젝트 기반 교육 운영'],'JOB SKILL TRAINER')])),variant='on')
P[16]=el('stat','metric','<div class="parts"><p class="fig">1,500+</p><p class="name">사내 교육 참여자</p><p class="note">교육은 개인의 성장을 넘어 조직의 성과로 이어집니다.</p></div>',1,2,5,4,variant='on')+prose('<b>기대효과</b>',1,5,1,2)+el('list','list',''.join('<div class="item"><span class="name">'+a+'</span></div>' for a in ['업무 생산성 향상','조직 커뮤니케이션 강화','직무 전문성 향상','조직 몰입도 향상','리더십 역량 강화','키워드를 입력해주세요.']),2,5,4,2,variant='divided quiet')+group(['<div class="card on line" data-el="cyanloop-card"><div class="parts"><p class="kick">Keyword '+str(i+1)+'</p><p class="name">'+a+'</p><p class="fig">'+b+'</p></div></div>' for i,(a,b) in enumerate([('교육 만족도','4.8 / 5.0'),('교육 수료율','97%'),('업무 적용률','89%'),('교육 추천 의향','95%'),('연간 학습 운영','120H'),('키워드 입력','00%')])],6,2,7,5,'two')
P[17]=el('roadmap','roadmap','<div class="heads">'+''.join('<span>W'+str(i+1)+'</span>' for i in range(10))+'</div>'+''.join('<div class="lane"><span class="name">'+a+'</span><div class="bar'+(' on' if i%2 else '')+'" style="--from:'+str(st)+'; --to:'+str(en)+'"><span>'+b+'</span></div></div>' for i,(a,b,st,en) in enumerate([('교육 요구 분석','조직 분석 및<br>교육 니즈 조사',0,2),('교육 설계','과정 설계 및 일정 협의',1,3),('콘텐츠 개발','교안 및 실습 자료 제작',2,5),('교육 운영','과정 운영 및 학습 관리',5,10),('성과 분석','만족도 조사<br>결과 분석',9,10)])),variant='on',data='; --cols:10')
'''
s=s[:idx]+insert+s[idx:];s=s.replace("' at-bottom-left' if n in (11,13)","' at-bottom-left' if n in (11,13,15)")
s=s.replace('--n-1:#f5f5f5;', '--n-1:#fff;');s=s.replace("if n==12 else '')}","if n==12 else '직무 특성에 맞춘 맞춤형 교육으로 실무 경쟁력을 강화합니다.' if n==14 else '교육은 개인의 성장을 넘어 조직의 성과로 이어집니다.' if n==15 else '교육 도입부터 성과 분석까지 체계적으로 지원합니다.' if n==17 else '')}")
p.write_text(s)
# Compact dumbbell labels retain actual coordinates at 3 rows.
css('slope','''
.slope[data-el="cyanloop-slope"].dumbbell{gap:0;}
.slope[data-el="cyanloop-slope"].dumbbell .pair{min-height:0;}
.slope[data-el="cyanloop-slope"].dumbbell .pair .a,.slope[data-el="cyanloop-slope"].dumbbell .pair .b{font-size:var(--type-12);top:calc(50% - 18px);}
.slope[data-el="cyanloop-slope"].dumbbell .pair .b{top:calc(50% + 6px);}
.slope[data-el="cyanloop-slope"].dumbbell .pair .a::before{top:13px;}
.slope[data-el="cyanloop-slope"].dumbbell .pair .b::before{top:-11px;}
''')
p=C/'elements/tag/fixtures/expanded-tag-hl.html';p.write_text(p.read_text().replace('min: 6x2','min: 6x3'))
