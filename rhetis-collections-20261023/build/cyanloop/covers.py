from pathlib import Path
W=Path('/workspace/work/cyanloop');C=Path('/workspace/output/cyanloop')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
/* Four cover families retain the source's oversized type and open-ended loop grammar. */
.slide.cover .page{padding:0;}
.slide.cover .lockup{left:60px;right:60px;top:126px;display:block;}
.slide.cover .lockup .title{font-size:var(--type-128);line-height:var(--figure-line);max-width:none;transform:scale(.86,1.04);transform-origin:left top;}
.slide.cover .lockup .title .label{font-size:inherit;color:var(--a3);}
.slide.cover .lockup .kicker{position:absolute;left:0;top:287px;width:580px;height:55px;border-radius:999px;background:linear-gradient(90deg,var(--a2),transparent);padding-left:74px;display:flex;align-items:center;font-size:var(--type-28);color:var(--page);}
.slide.cover .lockup .kicker::before{content:'';position:absolute;left:0;top:0;width:55px;height:55px;border-radius:50%;background:var(--a2);}
.slide.cover .lockup .lead{margin-top:var(--gap);font-size:var(--type-22);line-height:var(--body-line);max-width:600px;}
.slide.cover .meta{left:115px;bottom:64px;font-size:var(--type-28);font-weight:var(--name-weight);margin:0;}
.slide.cover .meta::before{content:'';position:absolute;left:-54px;top:0;width:38px;height:40px;background:radial-gradient(circle at 50% 15%,var(--page) 0 6px,transparent 7px),radial-gradient(circle at 18% 48%,var(--page) 0 6px,transparent 7px),radial-gradient(circle at 82% 48%,var(--page) 0 6px,transparent 7px),radial-gradient(circle at 50% 77%,var(--page) 0 7px,transparent 8px);}
.slide.cover .deco{position:absolute;inset:0;width:1280px;height:720px;border:0;border-radius:0;transform:none;background:linear-gradient(var(--a3),var(--a1-7)) 1152px 0/80px 461px no-repeat,linear-gradient(90deg,var(--a1-7),var(--a2)) 0 591px/1034px 83px no-repeat;pointer-events:none;}
.slide.cover .deco::before{content:'';position:absolute;left:815px;top:256px;width:418px;height:418px;border-radius:50%;background:conic-gradient(var(--a1-7),var(--a1) 90deg,var(--a2) 180deg,var(--a1-7) 220deg,var(--a3) 280deg,var(--a1-7));mask:radial-gradient(circle,transparent 0 124px,black 125px);}
.slide.cover .deco::after{content:'';position:absolute;left:815px;top:420px;width:83px;height:83px;border-radius:50%;background:var(--a3);box-shadow:335px 0 var(--a1),177px 172px var(--a2);}
.slide.cover .page.overrides{background:linear-gradient(to bottom,var(--a1-7) 0 350px,var(--page) 350px);}
.slide.cover .page.overrides .lockup{left:83px;top:177px;}
.slide.cover .page.overrides .lockup .title{font-size:var(--type-128);color:var(--a3);transform:scale(.92,1.12);}
.slide.cover .page.overrides .lockup .kicker{top:-81px;width:430px;height:54px;border:var(--stroke) solid var(--n-4);background:none;padding:0;justify-content:center;font-size:var(--type-24);}
.slide.cover .page.overrides .lockup .kicker::before{display:none;}
.slide.cover .page.overrides .body{position:absolute;left:83px;right:83px;top:430px;bottom:44px;}
.slide.cover .page.overrides .deco{left:757px;top:31px;width:346px;height:346px;background:conic-gradient(from 250deg,var(--a3),var(--a1-7) 130deg,var(--a1) 270deg,var(--a1-7));mask:radial-gradient(circle,transparent 0 103px,black 104px);border-radius:50%;}
.slide.cover .page.overrides .deco::before,.slide.cover .page.overrides .deco::after{display:none;}
.slide.cover .page.overrides::after{display:block;left:1020px;top:-70px;width:346px;height:346px;border-radius:50%;background:conic-gradient(from 250deg,var(--a2),var(--a1-7) 130deg,var(--a2) 270deg,var(--a1-7));mask:radial-gradient(circle,transparent 0 103px,black 104px);}
.slide.cover .page.at-center .lockup{left:54px;top:137px;}
.slide.cover .page.at-center .kicker{position:static;background:none;padding:0;height:auto;font-family:var(--font-display);font-size:var(--type-128);color:var(--a3);line-height:var(--figure-line);}
.slide.cover .page.at-center .kicker::before{display:none;}
.slide.cover .page.at-center .title{margin-top:20px;font-size:var(--type-104);transform:scaleX(.84);white-space:nowrap;}
.slide.cover .page.at-center .body{position:absolute;left:721px;right:60px;top:542px;bottom:75px;}
.slide.cover .page.at-center .deco{left:56px;top:300px;width:358px;height:379px;border-radius:50%;background:conic-gradient(from 90deg,var(--a1-7),var(--a2) 180deg,transparent 180deg);mask:radial-gradient(circle,transparent 0 100px,black 101px);}
.slide.cover .page.at-center .deco::before,.slide.cover .page.at-center .deco::after{display:none;}
.slide.cover .page.at-center::before{display:block;left:520px;top:78px;width:401px;height:401px;border-radius:50%;background:conic-gradient(from 330deg,var(--a1-7),var(--a3) 120deg,transparent 120deg);mask:radial-gradient(circle,transparent 0 121px,black 122px);}
.slide.cover .page.at-center::after{display:block;left:843px;top:136px;width:401px;height:362px;border-radius:50%;background:conic-gradient(from 90deg,var(--a3),var(--a1-7) 180deg,transparent 180deg);mask:radial-gradient(circle,transparent 0 121px,black 122px);}
.slide.cover .page.at-bottom-left .lockup{left:84px;top:226px;}
.slide.cover .page.at-bottom-left .title{color:var(--a3);transform:scale(1.04,1.3);font-size:var(--type-128);}
.slide.cover .page.at-bottom-left .kicker{top:-73px;left:-10px;width:548px;height:58px;padding:0;border:var(--stroke) solid var(--n-5);background:none;justify-content:center;font-size:var(--type-28);}
.slide.cover .page.at-bottom-left .kicker::before{display:none;}
.slide.cover .page.at-bottom-left .lead{margin-top:40px;font-size:var(--type-22);}
.slide.cover .page.at-bottom-left .foot{left:85px;top:544px;bottom:auto;right:auto;display:block;font-size:var(--type-18);white-space:pre-line;color:var(--page);line-height:var(--body-line);}
.slide.cover .page.at-bottom-left .foot b{font-size:var(--type-24);position:absolute;left:0;top:0;}
.slide.cover .page.at-bottom-left .foot span{display:block;margin-left:117px;}
.slide.cover .page.at-bottom-left .meta{left:1073px;bottom:69px;font-size:var(--type-24);}
.slide.cover .page.at-bottom-left .deco{left:769px;top:-82px;width:330px;height:364px;border-radius:50%;background:conic-gradient(from 90deg,var(--a3),var(--a1-7) 180deg,transparent 180deg);mask:radial-gradient(circle,transparent 0 88px,black 89px);}
.slide.cover .page.at-bottom-left .deco::before,.slide.cover .page.at-bottom-left .deco::after{display:none;}
.slide.cover .page.at-bottom-left::before{display:block;left:1015px;top:158px;width:392px;height:375px;border-radius:50%;background:conic-gradient(from 180deg,var(--a3),var(--a1-7) 180deg,transparent 180deg);mask:radial-gradient(circle,transparent 0 112px,black 113px);}
.slide.cover .page.at-bottom-left::after{display:block;left:944px;top:524px;width:382px;height:392px;border-radius:50%;background:conic-gradient(from 270deg,var(--a1-7),var(--a2) 180deg,transparent 180deg);mask:radial-gradient(circle,transparent 0 112px,black 113px);}
''')
p=C/'elements/agenda/element.css';p.write_text(p.read_text()+'''
.agenda[data-el="cyanloop-agenda"].quiet{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--gap-lg);padding:0;align-content:start;}
.agenda[data-el="cyanloop-agenda"].quiet .entry{display:grid;grid-template-columns:auto 1fr;grid-template-rows:76px auto;gap:0 var(--gap);background:none;border:0;border-radius:0;padding:0;align-items:baseline;}
.agenda[data-el="cyanloop-agenda"].quiet .entry .mark{font-family:var(--font-display);font-size:var(--type-60);background:none;color:var(--a1-7);width:auto;height:auto;border:0;line-height:var(--figure-line);}
.agenda[data-el="cyanloop-agenda"].quiet .entry>.name{font-size:var(--type-20);color:var(--a1-7);white-space:nowrap;}
.agenda[data-el="cyanloop-agenda"].quiet .entry>.note{grid-column:1/-1;border-top:var(--stroke) dotted var(--n-5);padding-top:var(--gap);font-size:var(--type-20);color:var(--n-9);line-height:1.75;}
.agenda[data-el="cyanloop-agenda"].quiet.line{display:flex;flex-direction:column;gap:var(--gap-sm);justify-content:center;}
.agenda[data-el="cyanloop-agenda"].quiet.line .entry{display:flex;flex-direction:row-reverse;gap:var(--gap-sm);align-items:center;padding:0;border:0;background:none;}
.agenda[data-el="cyanloop-agenda"].quiet.line .entry .mark{font-family:var(--font-body);font-size:var(--type-18);color:var(--page);margin-left:auto;}
.agenda[data-el="cyanloop-agenda"].quiet.line .entry .name{font-size:var(--type-20);color:var(--page);}
''')
p=W/'reassembly.py';s=p.read_text();idx=s.index('\nfor n in range(1,19):')
insert='''
P[2]=el('agenda','agenda',''.join('<div class="entry"><span class="mark">'+str(i+1).zfill(2)+'</span><span class="name">'+a+'</span><div class="note">'+b+'</div></div>' for i,(a,b) in enumerate([('교육 제안 배경','교육 목표<br>MIRI HRD 소개<br>미리HRD의 차별화'),('교육 체계','계층별 교육 체계<br>핵심 역량 모델<br>연간 교육 로드맵<br>교육 운영 프로세스'),('교육 과정','신입(Onboarding) 교육<br>직무 전문 교육<br>전문 강사진'),('운영 및 성과','기대 효과<br>실행 계획')])),variant='quiet')
P[3]=el('prose','prose','<p><b>교육 제안 배경</b></p>',1,1,4,6)+el('agenda','agenda',''.join('<div class="entry"><span class="mark">'+str(i+1).zfill(2)+'</span><span class="name">'+a+'</span></div>' for i,a in enumerate(['교육 목표','MIRI HRD 소개','미리HRD의 차별화'])),5,1,8,6,variant='quiet line')
'''
s=s[:idx]+insert+s[idx:]
a=s.index(" if P[n]=='cover':");b=s.index('\n else:',a)
s=s[:a]+''' if n in (1,2,3,18):
  variant={1:'',2:' overrides',3:' at-center',18:' at-bottom-left'}[n]
  kt={1:'직원 역량 강화 교육 프로그램 제안서',2:'직원 역량 강화 교육 프로그램 제안서',3:'01.',18:'함께 성장하는 조직을 위한 최고의 교육 파트너'}[n]
  ht={1:'<span class="label">HRD Learning</span><br>Solution',2:'CONTENTS',3:'EDUCATION PROPOSAL',18:'Thank You!'}[n]
  lead='<p class="lead">미리교육은 기업의 성장 단계와 교육 목표에 맞춘<br>최적의 교육 솔루션을 제안합니다.</p>' if n==18 else ''
  meta='<p class="meta">MIRI HRD</p>' if n in (1,18) else ''
  foot='<div class="foot"><b>Contact.</b><span>Address. 미리시 미리구 미리로 000<br>Tel.  00-0000-0000<br>E-mail. kimmiri@miridih.com<br>Web.  www.miriedu.co.kr</span></div>' if n==18 else ''
  content='<div class="body">'+P[n]+'</div>' if n in (2,3) else ''
  body='<section class="slide cover"><div class="page'+variant+'"><div class="deco"></div><div class="lockup"><p class="kicker">'+kt+'</p><h1 class="title">'+ht+'</h1>'+lead+'</div>'+content+meta+foot+'</div></section>'
'''+s[b:]
s=s.replace('--a3-7:#2bd4c8;}','--a3:#00eee2;--a3-7:#2bd4c8;}')
p.write_text(s)
