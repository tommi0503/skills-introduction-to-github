from pathlib import Path
import re,json
P=Path(__file__).parent;C=P/'onboard-docket';R=P/'reassembled';K='onboard-docket'
def q(n):return '[data-el="onboard-docket-'+n+'"]'
def add(n,t):
 p=C/'elements'/n/'element.css';s=p.read_text().split('\n/* Source measured pass two */')[0];p.write_text(s+'\n/* Source measured pass two */\n'+t+'\n')
def edit(n,fn):p=R/f'slide_{n:02}.html';p.write_text(fn(p.read_text()))
p=C/'kit/css/tokens.css';s=p.read_text().replace("'Nanum Pen Script'","'Nanum Pen'");p.write_text(s)
p=P/'assets/fonts/fonts.css';s=p.read_text().replace("'Nanum Pen Script'","'Nanum Pen'");p.write_text(s)
# All copy stays intact; only placements and contract variants change.
edit(5,lambda s:s.replace('class="prose quiet"','class="prose quiet columns"'))
edit(18,lambda s:s.replace('class="list line"','class="list line quiet"'))
edit(19,lambda s:s.replace('class="body overrides"','class="body"'))
edit(13,lambda s:s.replace('이곳에 관련 내용을 텍스트로 간략하게<br>입력해주세요. 관련 내용을 이곳에 입력해주세요.','이곳에 관련 내용을 텍스트로 간략하게<br>입력해주세요. 관련 내용을 이곳에 입력해주세요.'))
# One split per KPI row supplies the label's real width independently of the three metrics.
ns={};old=(P/'build_reassembled.py').read_text();exec('def E'+old.split('def E',1)[1].split('B={}',1)[0],globals());b=''
for i,ex in enumerate(['tone-3','tone-4','on']):
 b+='<div class="split" style="'+g(1,12,1+i*2,2)+'">'+card('사업명을 입력',extra=ex)+E('metric','stats',''.join(E('metric','stat',parts('키워드 입력','전년 동기 대비 00% 상승'if j==0 else'수치에 대한 부가 설명을 입력해주세요.','000<small>'+u+'</small>'))for j,u in enumerate(['원','개','명'])),extra='bands')+'</div>'
edit(17,lambda s:re.sub(r'(<div class="body[^\"]*">).*(</div></div></section>)',lambda z:z[1]+b+z[2],s,flags=re.S))
p=C/'foundation/foundation.css';s=p.read_text().split('\n/* Source measured pass two */')[0];s+='''
/* Source measured pass two */
.slide .top .deck{font-size:var(--type-14)}.slide .top .sec{font-size:var(--type-18)}
.slide .top .deck>.seat.logo{width:22px;height:22px;flex:none;border-radius:4px;font-size:var(--type-12)}
.slide.cover .lead{margin-top:calc(var(--gap-sm)*1.5)}
.slide.cover .meta{left:calc(var(--pad)*4.583);bottom:calc(var(--pad)*4.325)}
.slide .group.on{gap:0;margin-top:7px;padding-top:var(--gap)}
.slide .group.on>*{flex:0 0 calc((100% + var(--gap-lg)*3.75)/4)}
.slide .group.on>*+*{margin-left:calc(var(--gap-lg)*-1.25)}
.slide .stack.two{grid-template-columns:minmax(0,1fr);justify-content:stretch;justify-items:stretch;width:100%;min-width:0}
.slide .group:has(>.stack>.list.divided){padding:0 44px 0 64px}
.slide .stack:has(>.list.divided){padding:11px 20px 20px 0}
.slide .stack:has(>.list.divided)>.pill{margin-bottom:-8px}
.slide .group.col:has(>.headline>.kick){gap:0;justify-content:flex-start}
.slide .group.col:has(>.headline>.kick)>.headline{flex:0 0 193px}
.slide .body.overrides:has(>.headline.on.center){margin-left:-17px;margin-right:-16px}
.slide .body.overrides:has(>.split>.stats.bands){margin:0;padding-top:10px;padding-bottom:29px}
.slide .split:has(>.stats.bands){grid-template-columns:290px minmax(0,1fr);gap:5px}
.slide .body:has(>.split>.group>.stack.two){padding-top:19px;padding-bottom:48px}
.slide .split:has(>.group>.stack.two){grid-template-columns:108px minmax(0,1fr)}
.slide .body:has(>.hub){padding-bottom:0}
''';p.write_text(s)
s=q('agenda');add('agenda',s+'{padding:21px 77px 52px;grid-template-rows:repeat(4,64px);column-gap:30px;row-gap:16px}'+s+' .entry{padding:0;height:64px;min-height:64px}'+s+' .mark{width:56px;height:56px;font-size:var(--type-20);margin-left:0}'+s+' .name{font-size:var(--type-22);font-weight:var(--body-weight)}')
s=q('headline');add('headline',s+'.big.center h2{line-height:1.08;font-size:var(--type-76)}'+s+' .kick{height:35px;flex:none}'+s+'.on.center{align-self:start;margin-top:44px;margin-bottom:0}')
s=q('prose');add('prose',s+'.quiet{display:block;padding-top:0}'+s+'.quiet.columns{transform:translateY(-12px)}'+s+'.quiet.columns p{font-size:var(--type-16);line-height:1.65}'+s+'.columns:not(.quiet){padding-left:51px;padding-right:36px}'+s+'.lead.center{transform:translateY(-6px)}'+s+' p{font-size:var(--type-18)}'+s+'.lead p{font-size:var(--type-18)}')
s=q('image-frame');add('image-frame',s+'.frame{container-type:size}'+s+' .seat.portrait{width:400px;height:calc(100cqh + 208px);margin-left:4px;margin-right:auto;align-self:center;transform:translateY(-34px)}@container(min-width:350px) and (max-width:499px){'+s+' .seat:not(.portrait){width:420px;height:395px;margin-left:13px;margin-right:auto;align-self:flex-start}}@container(min-width:500px) and (max-width:650px){'+s+' .seat:not(.portrait){width:493px;height:330px;margin-left:0;margin-right:auto;align-self:flex-start;transform:translateY(15px)}}@container(max-width:300px){'+s+' .seat:not(.portrait){width:196px;height:145px;margin-left:9px;margin-right:auto;transform:translateY(-10px)}}')
s=q('list');add('list',s+'.num{padding-top:10px}'+s+'.num .item{grid-template-rows:54px}'+s+'.num .item::before{left:48px}'+s+'.num .item>.name{height:54px}'+s+'.line{padding:21px 26px 0 25px;justify-content:flex-start}'+s+'.line.quiet{padding:15px 0 0;margin-left:-41px;width:calc(100% + 41px);gap:13px}'+s+'.line.quiet .item{height:101px;min-height:101px;grid-template-columns:27% 1fr}'+s+'.divided .name{white-space:nowrap}')
s=q('callout');add('callout',s+' p{font-size:var(--type-22)}')
p=C/'elements/chart-donut/element.css';s=p.read_text();s=s.replace('50% + var(--pad)*.4','50% + var(--pad)*1.2').replace('50% - 25px','50% - 5px').replace('50% - 141px','50% - 122px');p.write_text(s)
s=q('card');css=s+':has(.parts>.mark:last-child){height:142px;transform:translateY(-24px)}'+s+':has(.parts>.mark:last-child) .mark{display:flex}'+s+'.tone-3:not(:has(.mark,.kick,.fig)):has(.name>br){height:142px;align-self:start;transform:translateY(-34px)}'+s+'.quiet:not(:has(.mark,.fig,.kick)){padding:8px 20px}'+s+'.quiet:not(:has(.mark,.fig,.kick)) .note{display:block;font-size:var(--type-14);line-height:1.5}'+s+'.quiet:not(:has(.mark,.fig,.kick)) .name{margin-bottom:4px}'+s+'.quiet:not(:has(.name,.mark,.fig,.kick)) .note{font-size:var(--type-16);line-height:1.55}'+s+':is(.tone-1,.tone-2):has(.kick):not(:has(.mark,.fig)){container-type:normal}'+s+':is(.tone-1,.tone-2):has(.kick):not(:has(.mark,.fig))::before{mix-blend-mode:multiply;opacity:.95}'+s+'.tone-1:has(.kick):not(:has(.mark,.fig))::before{background:var(--a1-5-soft)}'+s+'.tone-2:has(.kick):not(:has(.mark,.fig))::before{background:var(--a2-6)}'+s+':is(.tone-3,.tone-4):not(:has(.mark,.note,.kick,.fig)){border-radius:4px;padding:0;display:flex;align-items:center;justify-content:center;color:var(--a1-on)}'+s+':is(.tone-3,.tone-4):not(:has(.mark,.note,.kick,.fig)) .parts{display:flex;align-items:center;justify-content:center;text-align:center}'+s+':is(.tone-3,.tone-4):not(:has(.mark,.note,.kick,.fig)) .name{color:inherit;font-size:var(--type-22);font-weight:var(--body-weight)}'+s+'.tone-3:not(:has(.mark,.note,.kick,.fig)){background:var(--a1-3-soft)}'+s+'.tone-4:not(:has(.mark,.note,.kick,.fig)){background:var(--a1-4-soft)}@container(max-width:150px){'+s+'.on:not(:has(.mark,.note,.kick,.fig)) .name{font-size:var(--type-18)}}';add('card',css)
s=q('hub');add('hub','@container(min-width:900px){'+s+' .note{width:225px;margin-left:-16px;font-size:var(--type-14)}'+s+' .spoke:nth-child(3 of .spoke) .note,'+s+' .spoke:nth-child(2 of .spoke) .note{width:300px;margin-left:-54px}}')
s=q('hierarchy');add('hierarchy',s+':has(>.branch>.org){padding:68px 0 0;margin-left:-20px;width:calc(100% + 40px)}'+s+':has(>.branch>.org)>.root{top:6px}'+s+':has(>.branch>.org)>.root::after{height:21px}'+s+':has(>.branch>.org)>.branch{border-top:0}'+s+':has(>.branch>.org)>.branch>.node{display:none}'+s+':has(>.branch>.org)::before{content:"";position:absolute;left:27.05%;right:26.43%;top:68px;height:36px;border:var(--stroke) solid var(--n-4);border-bottom:0;border-radius:14px 14px 0 0}'+s+':has(>.branch>.org)::after{content:"";position:absolute;left:10%;right:9.64%;top:165px;height:35px;border:var(--stroke) solid var(--n-4);border-bottom:0;border-radius:14px 14px 0 0}'+s+' .branch>.org>.root{top:36px}'+s+' .branch>.org>.root::after{height:23px}'+s+' .branch>.org>.branch{border-top:0}'+s+':has(>.branch>.org)>.branch:first-of-type>.org>.root{left:calc(50% - 114px)}'+s+':has(>.branch>.org)>.branch:last-of-type>.org>.root{left:calc(50% - 172px)}'+s+':has(>.branch>.org)>.branch:last-of-type>.org>.branch:nth-child(2)>.node{background:var(--n-8);color:var(--page)}'+s+':has(>.branch>.org)>.branch:last-of-type>.org>.branch:nth-child(3)>.node{background:var(--a1);color:var(--a1-on)}')
s=q('metric');add('metric',s+'.stats.bands>.stat{padding:10px 22px}')
s=q('pill');add('pill',s+':has(.parts>.name:only-child) .name{font-size:var(--type-22)}')
# Source style values are palette input only, never geometry overrides.
p=P/'assets/source-palette.css';s=p.read_text();s=s.replace('--a1-3-soft:#d5e2f6','--a1-3-soft:#b4caf1').replace('--a1-4-soft:#d5e2f6','--a1-4-soft:#709fe9').replace('--a1-5-soft:#4383e6','--a1-5-soft:#5b91e8').replace('--a2-6:#4383e6','--a2-6:#55596a');p.write_text(s)
print('Pass two restored measured widths, overlap, visible notes and graph levels.')
