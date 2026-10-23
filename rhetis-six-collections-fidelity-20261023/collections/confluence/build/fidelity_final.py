from pathlib import Path
import shutil,json,re
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
p=C/'kit/css/tokens.css';s=p.read_text();s+='\n.slide{--confluence-hero-track:.035em;--confluence-goal-track:-.0225em;}\n';p.write_text(s)
p=C/'foundation/foundation.css';s=p.read_text();s+='\n.cover .lockup{height:400px}\n';p.write_text(s)
p=C/'elements/hub/element.css';s=p.read_text();s+='''\n@container(min-width:1000px){
.hub[data-el="confluence-hub"]:has(>.spoke:nth-child(5):last-child) .core .name{transform:translateX(3px)}
.hub[data-el="confluence-hub"]:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(3) .mark{right:31px;width:84px}
.hub[data-el="confluence-hub"]:has(>.spoke:nth-child(5):last-child) .spoke:nth-child(5) .mark{right:3px;width:120px;height:84px}
.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-up"]{width:84px!important;height:84px!important;left:0!important;top:-6px!important;overflow:visible}
.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-down"]{width:76px!important;height:84px!important;left:44px!important;top:-6px!important;overflow:visible}
.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-up"] svg,.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-down"] svg{left:0;top:0;width:100%;height:100%}
}
''';p.write_text(s)
# Port the same geometric/family corrections to replicas; replicas retain free source CSS.
p=R/'replica/replica.css';s=p.read_text().replace('#41c6db','#44cde5').replace('#3a54df','#3858e3').replace('#effbfc','#effafd').replace('#f0f2fd','#eff2fc');s+='\n.goal h2{letter-spacing:-.9px}.goal h2 span{font-weight:800}\n';p.write_text(s)
for p in (R/'replica').glob('*.html'):
 s=p.read_text().replace('#41c6db','#44cde5').replace('#3a54df','#3858e3')
 if p.stem=='slide_03':s=s.replace('font-size:60px;line-height:1;letter-spacing:-4px;font-weight:850','font-size:60px;line-height:1;letter-spacing:2.1px;font-weight:800')
 if p.stem=='slide_04':s=s.replace('padding-top:100px','padding-top:106px').replace('font-size:60px;line-height:1;letter-spacing:-3px;font-weight:850','font-size:60px;line-height:1;letter-spacing:2.1px;font-weight:800').replace('<h2>프로젝트 목표 <span','<h2><u>프로젝트 목표</u> <span')
 p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
