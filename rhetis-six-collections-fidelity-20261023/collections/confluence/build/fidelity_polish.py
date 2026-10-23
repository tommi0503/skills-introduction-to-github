from pathlib import Path
import re,shutil
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
def add(path,s):
 p=C/path;t=p.read_text().split('/* fidelity-polish */')[0];p.write_text(t+'\n/* fidelity-polish */\n'+s)
add(Path('kit/css/tokens.css'),'.slide{--confluence-hero-track:.0083em;--confluence-goal-track:-.01em;--confluence-cover-copy-track:-.032em;}')
add(Path('foundation/foundation.css'),'''
.cover .title{height:253px}.cover .title small{top:-62px;line-height:1.2}.cover .lead{position:absolute;top:324px;margin:0;letter-spacing:var(--confluence-cover-copy-track)}
.rail .title{top:162px;letter-spacing:var(--confluence-hero-track);font-weight:800;min-height:126px}.rail .title b{font-weight:800}.rail .lead{font-size:var(--type-14);line-height:1.3}.rail .kicker{letter-spacing:var(--confluence-caption-track)}
.top .seat.logo{border-radius:0}.slide{background:radial-gradient(ellipse 400px 350px at 640px 160px,color-mix(in srgb,var(--page) 28%,transparent),transparent),linear-gradient(var(--a1-1-soft),var(--a2-1-soft))}
''')
q='.card[data-el="confluence-card"]'
add(Path('elements/card/element.css'),f'''{q}.tone-1:has(.fig) .name,{q}.tone-1:has(.fig) .fig,{q}.tone-1:has(.fig) .note{{width:auto}}{q}.tone-1:has(.fig) .fig{{color:var(--n-9)}}{q}.tone-1:has(.fig) .note{{color:var(--n-8)}}''')
q='.hub[data-el="confluence-hub"]'
add(Path('elements/hub/element.css'),f'''
{q} .mark{{font-size:0;line-height:0}}{q} .icon svg{{display:block}}
@container(min-width:1000px){{
{q}:has(>.spoke:nth-child(5):last-child) .core .name{{top:106px;min-height:126px;font-weight:800;letter-spacing:var(--confluence-hero-track)}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .name{{letter-spacing:var(--confluence-goal-track)}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .mark:has(.icon+.icon) .icon{{position:absolute;left:0;top:0;width:76px;height:76px}}
{q} .mark .icon[data-icon="chart-no-axes-column-increasing"]{{top:21px!important;height:55px!important}}{q} .mark .icon[data-icon="chart-no-axes-column-increasing"] svg{{stroke-width:4}}{q} .mark .icon[data-icon="trending-up"]{{top:0!important;height:34px!important}}
{q} .mark .icon[data-icon="message-square"]{{width:60px!important;height:60px!important;top:0!important;left:-2px!important;color:var(--a2)}}{q} .mark .icon[data-icon="message-square"] svg{{fill:var(--a2);stroke:var(--a2)}}
{q} .mark .icon[data-icon="message-circle-more"]{{width:64px!important;height:64px!important;top:10px!important;left:20px!important}}{q} .mark .icon[data-icon="message-circle-more"] svg{{fill:var(--a1-1-soft);stroke:var(--a1)}}
{q} .mark .icon[data-icon="file-text"]{{left:8px!important;top:0!important;width:58px!important;height:58px!important;color:var(--a2)}}{q} .mark .icon[data-icon="file-text"] svg{{fill:var(--a2);stroke:var(--a2)}}{q} .mark .icon[data-icon="file-text"] svg path:nth-child(n+2){{stroke:var(--page)}}
{q} .mark:has([data-icon="file-text"]) .icon[data-icon="mail"]{{top:26px!important;height:50px!important}}{q} .mark .icon[data-icon="mail"] svg{{stroke:var(--a1)}}
{q} .mark .icon[data-icon="arrow-big-up"]{{width:46px!important;height:76px!important;left:0!important}}{q} .mark .icon[data-icon="arrow-big-up"] svg{{fill:var(--a1);stroke:var(--a1)}}
{q} .mark .icon[data-icon="arrow-big-down"]{{width:46px!important;height:76px!important;left:34px!important;color:var(--a2)}}{q} .mark .icon[data-icon="arrow-big-down"] svg{{stroke:var(--a2)}}
}}
''')
p=R/'assets/reference-style.css';s=p.read_text();s+='\n.slide{--a1:#44cde5;--a2:#3858e3;--a1-1-soft:#effafd;--a2-1-soft:#eff2fc;--n-8:#626262;--n-9:#505050;--a1-6:#308d9e;}\n';p.write_text(s)
p=R/'reassembled/slide_04.html';s=p.read_text()
for old,new in [('chart-no-axes-combined','chart-no-axes-column-increasing'),('messages-square','message-square'),('arrow-down-up','arrow-big-up')]:s=s.replace(f'data-icon="{old}"></span>',f'data-icon="{new}"></span>')
s=s.replace('data-icon="chart-no-axes-column-increasing"></span>','data-icon="chart-no-axes-column-increasing"></span><span class="icon" data-icon="trending-up"></span>').replace('data-icon="message-square"></span>','data-icon="message-square"></span><span class="icon" data-icon="message-circle-more"></span>').replace('<span class="icon" data-icon="mail"></span>','<span class="icon" data-icon="file-text"></span><span class="icon" data-icon="mail"></span>').replace('data-icon="arrow-big-up"></span>','data-icon="arrow-big-up"></span><span class="icon" data-icon="arrow-big-down"></span>');p.write_text(s)
p=R/'reassembled/slide_03.html';s=p.read_text().replace('메인타이틀에 대한 간략한 세부 설명을 입력하는 영역입니다.<br>내용을 입력해주세요.','메인타이틀에 대한 간략한 세부 설명을<br>입력하는 영역입니다.<br>내용을 입력해주세요.');p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
