from pathlib import Path
import shutil,re
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
def add(path,s):
 p=C/path;t=p.read_text().split('/* fidelity-complete */')[0];p.write_text(t+'\n/* fidelity-complete */\n'+s)
add(Path('foundation/foundation.css'),'''
.cover .title{margin-top:71px;line-height:.92}.cover .title small{letter-spacing:var(--title-track);top:-58px;line-height:1.05}.cover .title{height:235.5px}
.rail .title{top:158px}.rail .kicker{font-size:var(--type-8);color:var(--a1-3)}.rail .lead{font-size:var(--type-12);line-height:var(--lead-line)}
.head.center .kicker{font-size:var(--type-8);line-height:var(--label-line)}
''')
q='.card[data-el="confluence-card"]'
add(Path('elements/card/element.css'),f'''
{q}.tone-1:has(.fig) .kick{{width:auto;font-weight:var(--label-weight)}}
{q}.tone-1:has(.fig) .note{{font-size:var(--type-14);text-align:center;color:var(--n-7)}}
{q}.tone-1:has(.fig) .note>b,{q}.tone-1:has(.fig) .note>span{{left:0;right:0;width:100%;text-align:center}}
{q}.tone-1:has(.fig) .fig:has(br){{font-weight:var(--name-weight)}}
''')
q='.agenda[data-el="confluence-agenda"]'
add(Path('elements/agenda/element.css'),f'''
{q}{{padding:0;column-gap:var(--confluence-agenda-column);row-gap:var(--confluence-agenda-gap)}}
{q} .entry{{padding:0;border-radius:17px;box-shadow:0 7px 8px color-mix(in srgb,var(--n-2) 25%,transparent);display:block}}
{q} .entry .mark{{top:-23px;left:50%;transform:translateX(-50%);width:53px;height:53px;border:7px solid var(--page);background:var(--a2);color:var(--a1);font-size:var(--type-18);font-weight:var(--name-weight)}}
{q} .entry:nth-child(even) .mark{{background:var(--a1);color:var(--a1-on)}}
{q} .entry .name{{position:absolute;left:0;right:0;top:29px;display:block;padding:0;border:0;font-size:var(--type-32);line-height:var(--name-line)}}
{q} .entry::after{{content:"";position:absolute;left:22px;right:22px;top:81px;height:1px;background:var(--n-2)}}
{q} .entry .note{{position:absolute;left:0;right:0;top:98px;font-size:var(--type-14);line-height:1.2;color:var(--n-6);letter-spacing:var(--body-track)}}
@container(max-width:650px){{{q}{{column-gap:var(--gap-sm);row-gap:var(--gap)}}{q} .entry .name{{font-size:var(--type-18)}}{q} .entry .note{{font-size:var(--type-12)}}}}
''')
q='.hub[data-el="confluence-hub"]';s=f'''
@container(min-width:1000px){{
{q}:has(>.spoke:nth-child(5):last-child){{display:block}}
{q}:has(>.spoke:nth-child(5):last-child)::before{{left:100px;right:100px;top:360px;height:1px;background:var(--n-2)}}
{q}:has(>.spoke:nth-child(5):last-child)::after{{left:640px;top:76px;bottom:76px;width:1px;background:var(--n-2)}}
{q}:has(>.spoke:nth-child(5):last-child) .core{{position:absolute;left:456px;top:175px;width:367px;height:367px;aspect-ratio:1;display:block;padding:0;border:17px solid var(--page);border-radius:50%;background:var(--a1);box-shadow:0 8px 12px color-mix(in srgb,var(--n-2) 35%,transparent)}}
{q}:has(>.spoke:nth-child(5):last-child) .core>.seat{{position:absolute;left:104px;top:-49px;width:131px;height:128px;transform:none;border-radius:0}}
{q}:has(>.spoke:nth-child(5):last-child) .core .name{{position:absolute;left:0;right:0;top:100px;padding:0;font-size:var(--type-60);font-weight:var(--title-weight);line-height:1;letter-spacing:var(--name-track);color:var(--a1-on)}}
{q}:has(>.spoke:nth-child(5):last-child) .core .name b{{font-weight:inherit;color:var(--a2)}}
{q}:has(>.spoke:nth-child(5):last-child) .core .kick{{position:absolute;top:233px;left:0;right:0;font-size:var(--type-8);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track-latin);color:var(--a2)}}
{q}:has(>.spoke:nth-child(5):last-child) .core .note{{position:absolute;left:0;right:0;top:251px;padding:0;font-size:var(--type-14);line-height:1.25;color:var(--a1-6)}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke{{position:absolute;left:148px;top:165px;width:335px;height:145px;display:block;align-items:initial;justify-content:initial;padding:0;text-align:left}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(3),{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(5){{left:830px;text-align:right}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(4),{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(5){{top:489px;padding:0}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .name{{position:absolute;left:0;right:0;top:0;font-size:var(--type-40);line-height:1.1;font-weight:800;letter-spacing:var(--name-track);white-space:nowrap}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .name u{{text-underline-offset:4px;text-decoration-thickness:3px}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .name b{{color:var(--a2)}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(3) .name b,{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(4) .name b{{color:var(--a1)}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .note{{position:absolute;left:0;right:0;top:64px;font-size:var(--type-14);line-height:1.35;color:var(--n-6)}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .mark{{position:absolute;left:0;top:-77px;width:76px;height:76px;color:var(--a1)}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(3) .mark,{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(5) .mark{{left:auto;right:0}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(4) .mark,{q}:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(5) .mark{{top:-79px}}
{q}:has(>.spoke:nth-child(5):last-child) .spoke .mark .icon{{width:76px;height:76px}}
{q} .spoke .mark svg path:nth-child(even),{q} .spoke .mark svg rect:nth-child(even){{stroke:var(--a2)}}
}}
''';add(Path('elements/hub/element.css'),s)
p=R/'reassembled/slide_01.html';s=p.read_text();needle='산학 협력 프로젝트 제안 프레젠테이션</b></p>';s=s.replace(needle,'산학 협력 프로젝트 제안 프레젠테이션</b><small>산업과 교육의 만남으로 함께 성장하는 산학협력 프로젝트를 제안합니다.<br>미래의 인재와 기업의 새로운 가능성을 연결하고 지속 가능한 성과를 만듭니다.<br>다양한 기관에서 활용할 수 있는 협력 모델을 소개합니다.</small></p>');p.write_text(s)
p=R/'reassembled/slide_02.html';s=p.read_text().replace('정도의 설명글이 들어가는','정도의 설명글이<br>들어가는');p.write_text(s)
p=R/'reassembled/slide_04.html';s=p.read_text();s=s.replace('<b class="name">프로젝트<br>목표</b><p class="note">PROJECT GOAL<br><br>메인타이틀에 대한 간략한 설명을 입력하는 영역입니다.</p>','<b class="name">프로젝트<br><b>목표</b></b><p class="kick">PROJECT GOAL</p><p class="note">메인타이틀에 대한 간략한 설명을<br>입력하는 영역입니다.</p>')
s=s.replace('프로젝트 목표 <b>','<u>프로젝트 목표</u> <b>').replace('프로젝트 목표를 입력하세요.<br>','<u>프로젝트 목표를 입력하세요.</u><br>').replace('프로젝트의 상세 목표를 입력하세요.<br>','<u>프로젝트의 상세 목표를 입력하세요.</u><br>');p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
print('all four geometry fidelity applied')
