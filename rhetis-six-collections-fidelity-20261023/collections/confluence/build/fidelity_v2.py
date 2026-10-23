from pathlib import Path
import shutil,re
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
B=D/'build/fidelity-before';B.mkdir(exist_ok=True)
for p in (R/'reassembled').glob('*.png'):
 if not (B/p.name).exists():shutil.copy2(p,B/p.name)
def add(path,s):
 p=C/path;t=p.read_text();t=t.split('/* fidelity-v2 */')[0];p.write_text(t+'\n/* fidelity-v2 */\n'+s)
add(Path('kit/css/tokens.css'),'''.slide{--weight-display:900;--title-track:-.0625em;--name-track:-.05em;--confluence-column-gap:20px;--confluence-row-gap:23px;--confluence-agenda-gap:47px;--confluence-agenda-column:27px;--confluence-card-inset:11px;--confluence-caption-line:1.35;--confluence-cover-line:.92;--confluence-caption-track:.3em;--confluence-rail-copy:190px;}''')
add(Path('foundation/foundation.css'),'''
.title b,.cover .title b{color:var(--a1)}.title b~b,.cover .title b~b{color:var(--a2)}
.cover .page{inset:0}.cover .seat.back{left:108px;top:111px;width:510px;height:520px;transform:none;border-radius:0}
.cover:has(.seat.back) .at-left{left:701px;top:166px;width:525px;max-width:none;transform:none}
.cover .kicker{font-size:var(--type-8);line-height:var(--label-line);letter-spacing:var(--confluence-caption-track);color:var(--a1-3)}
.cover .title{position:relative;margin-top:71px;font-size:var(--type-128);line-height:var(--confluence-cover-line);font-weight:var(--weight-display);letter-spacing:var(--title-track)}
.cover .title b{font-weight:var(--weight-display)}.cover .title small{position:absolute;left:0;top:-58px;margin:0;white-space:nowrap;font-size:var(--type-48);line-height:1.05;letter-spacing:var(--title-track);font-weight:var(--lead-weight);color:var(--n-7)}
.cover .lead{margin-top:16px;font-size:var(--type-16);line-height:var(--lead-line);letter-spacing:var(--name-track);white-space:nowrap;color:var(--ink)}
.cover .lead small{display:block;font-size:var(--type-8);line-height:1.1;color:var(--n-3);letter-spacing:var(--body-track);margin-top:8px;white-space:normal}
.top .seat.logo{width:35px;height:36px}.top{top:22px;right:23px}
.page:has(>.head.center){inset:0;display:block}.head.center{position:absolute;left:94px;top:151px;width:1092px;padding:0;gap:7px}.head.center .title{font-size:var(--type-64);line-height:1.2}.head.center .kicker{font-size:var(--type-9);line-height:var(--label-line);letter-spacing:var(--confluence-caption-track);color:var(--n-5)}
.head.center .title::before,.head.center .title::after{top:40px;background:var(--n-2);width:396px}.head.center .title::after{width:402px}
.page:has(>.head.center)>.body{position:absolute;left:94px;top:295px;width:1092px;height:351px}
.top .seat.icon{top:2px;left:50%;width:160px;height:126px;border-radius:0}
.rail{left:94px;top:75px;width:280px;height:569px}.rail::after{height:568px;right:0;top:1px;background:var(--n-2)}.rail .seat{width:130px;height:145px;margin:0;border-radius:0}.rail .title{position:absolute;top:162px;left:0;line-height:1;letter-spacing:var(--title-track)}.rail .kicker{position:absolute;top:292px;margin:0;font-size:var(--type-9);letter-spacing:var(--label-track-latin);color:var(--n-5)}.rail .lead{position:absolute;left:0;top:328px;margin:0;max-width:var(--confluence-rail-copy);font-size:var(--type-13);line-height:1.3;color:var(--n-6)}
.slide:has(>.rail) .page{left:420px;right:94px;top:75px;bottom:74px;display:block}.slide:has(>.rail) .body{height:571px;column-gap:var(--confluence-column-gap);row-gap:var(--confluence-row-gap);grid-template-rows:115px repeat(5,minmax(0,1fr))}
.page:not(:has(>.head)){inset:0;display:block}.page:not(:has(>.head))>.body{height:100%}.slide:has(>.rail) .page{left:420px;right:94px;top:75px;bottom:74px}.slide:has(>.rail) .body{height:571px}
''')
q='.card[data-el="confluence-card"]'
add(Path('elements/card/element.css'),f'''
{q}.line:has(.kick):not(:has(.fig)){{padding:0;border:0;border-radius:10px;background:var(--page)}}
{q}.line:has(.kick):not(:has(.fig)) .parts{{position:relative;display:block;width:100%;height:100%}}
{q}.line:has(.kick):not(:has(.fig)) .kick{{position:absolute;left:10px;top:8px;width:220px;height:98px;padding:0;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:var(--type-26);font-weight:var(--name-weight);letter-spacing:var(--name-track);background:var(--a2);color:var(--a2-on)}}
{q}.line:has(.kick):not(:has(.fig)) .name{{position:absolute;left:262px;top:38px;display:block;white-space:nowrap;font-size:var(--type-28);line-height:var(--name-line);color:var(--ink)}}
{q}.tone-1:has(.fig){{padding:0;border:0;border-radius:17px;background:var(--page)}}
{q}.tone-1:has(.fig) .parts{{display:block;position:relative;width:100%;height:100%;padding:0}}
{q}.tone-1:has(.fig) .kick{{position:absolute;left:11px;right:11px;top:12px;height:68px;padding:0;display:flex;align-items:center;justify-content:center;border-radius:6px;background:var(--a1);color:var(--a1-on);font-size:var(--type-26);font-weight:var(--name-weight);letter-spacing:var(--name-track)}}
{q}.tone-1:has(.fig) .name{{position:absolute;left:22px;right:18px;top:119px;padding:0;border:0;font-size:var(--type-20);line-height:var(--name-line);font-weight:var(--label-weight);color:var(--a1)}}
{q}.tone-1:has(.fig) .fig{{position:absolute;left:22px;right:18px;top:151px;padding:0;font-size:var(--type-52);font-weight:800;line-height:1.05;letter-spacing:var(--figure-track);color:var(--n-8)}}
{q}.tone-1:has(.fig) .fig:has(br){{font-size:var(--type-24);font-weight:var(--body-weight);letter-spacing:var(--name-track)}}
{q}.tone-1:has(.fig) .parts::after{{content:"";position:absolute;left:22px;right:18px;top:238px;border-top:1px dotted var(--a1-2)}}
{q}.tone-1:has(.fig) .note{{position:absolute;left:22px;right:18px;top:272px;padding:0;margin:0;font-size:var(--type-15);line-height:1.55;font-weight:var(--body-weight);color:var(--n-6)}}
{q}.tone-1:has(.fig) .note>b{{position:absolute;left:0;top:0;font-size:var(--type-20);line-height:var(--name-line);font-weight:var(--label-weight);color:var(--a1)}}
{q}.tone-1:has(.fig) .note>span{{position:absolute;left:0;top:31px;white-space:nowrap}}{q}.tone-1:has(.fig) .note>b:nth-child(3){{top:66px}}{q}.tone-1:has(.fig) .note>span:nth-child(4){{top:97px}}
''')
# Host palette: original visual values, independent from library preview palette.
p=R/'assets/reference-style.css';s=p.read_text();s += '\n.slide{--ink:#090b0e;--a1:#41c6db;--a1-on:#fff;--a2:#3a54df;--a2-on:#fff;--a1-3:#a8d8e8;--n-2:#d5ddea;--n-3:#c3c9ce;--n-5:#9cabb0;--n-6:#979fa4;--n-7:#7b8183;--n-8:#505050;--a1-1-soft:#effbfc;--a2-1-soft:#f0f2fd;}\n';p.write_text(s)
p=R/'reassembled/slide_03.html';s=p.read_text();s=s.replace('class="card "','class="card line"',1).replace('class="card "','class="card tone-1"')
s=s.replace('<b>1차 프로젝트</b><br>2060년 4월 26일~ 5월 17일<br><br><b>2차 프로젝트</b><br>2060년 5월 18일~ 6월 18일','<b>1차 프로젝트</b><span>2060년 4월 26일~ 5월 17일</span><b>2차 프로젝트</b><span>2060년 5월 18일~ 6월 18일</span>')
s=s.replace('<b>사업관리비</b><br>127,500,600원<br><br><b>연계지원비</b><br>130,640,100원','<b>사업관리비</b><span>127,500,600원</span><b>연계지원비</b><span>130,640,100원</span>')
s=s.replace('<b>연구원</b><br>이미리 / 과제 진행<br>김미리 / 과제 진행<br>박미리 / 모델 개발<br>신미리 / 모델 개발','<b>연구원</b><span>이미리 / 과제 진행<br>김미리 / 과제 진행<br>박미리 / 모델 개발<br>신미리 / 모델 개발</span>');p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
print('fidelity-v2 applied: foundation + card original geometry/palette')
