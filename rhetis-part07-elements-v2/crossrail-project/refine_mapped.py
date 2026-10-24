from pathlib import Path
import re,json
P=Path(__file__).parent;E=P/'crossrail/elements'
# These are complete declaration edits, not a cascade of appended page patches.
p=E/'hub/element.css';s=p.read_text();s=s.replace('--crossrail-hub-radius:min(40cqw,58cqh)','--crossrail-hub-radius:min(40cqw,58cqh)')
s=s.replace('left:50%;top:calc(100% + var(--gap-sm)/2);transform:translateX(-50%);width:150%','left:calc((var(--crossrail-spoke-index) - 1)*100cqw/var(--crossrail-hub-count));top:84cqh;transform:none;width:calc(100cqw/var(--crossrail-hub-count) - var(--gap-sm))')
s=s.replace('.spoke .note{position:absolute;','.spoke .note{position:fixed;')
# Spoke transform is removed and converted into negative margins so note's fixed CB is the root.
s=s.replace('transform:translate(-50%,-50%);box-sizing:border-box;border-radius:50%;background:var(--a1-7)','margin-left:calc(min(19cqw,26cqh)/-2);margin-top:calc(min(19cqw,26cqh)/-2);box-sizing:border-box;border-radius:50%;background:var(--a1-7)')
s=s.replace('position:relative;min-width:0;min-height:0;','position:relative;min-width:0;min-height:0;transform:translate(0);')
# Generic count rules own their member geometry; source has four short names and no note parts.
for i in range(1,7):s+=f' .hub[data-el="crossrail-hub"]>.spoke:nth-child({i} of .spoke){{--crossrail-spoke-index:{i}}}'
s+=' .hub[data-el="crossrail-hub"]:has(>.spoke:nth-child(6 of .spoke):last-child)>.spoke{width:min(13cqw,17cqh);height:min(13cqw,17cqh);margin-left:calc(min(13cqw,17cqh)/-2);margin-top:calc(min(13cqw,17cqh)/-2)} .hub[data-el="crossrail-hub"]:not(:has(>.spoke>.note)){--crossrail-hub-radius:min(45.5cqw,84cqh)} .hub[data-el="crossrail-hub"]:not(:has(>.spoke>.note))>.spoke{width:min(20cqw,38cqh);height:min(20cqw,38cqh);margin-left:calc(min(20cqw,38cqh)/-2);margin-top:calc(min(20cqw,38cqh)/-2)}'
p.write_text(s)
# In long-copy pyramid examples, notes form a readable aligned column beside the actual triangular levels.
p=E/'pyramid/element.css';s=p.read_text().replace('position:relative;min-width:0;min-height:0;','position:relative;min-width:0;min-height:0;transform:translate(0);').replace('font-size:var(--type-26)','font-size:var(--type-18)')
s+=' .pyramid[data-el="crossrail-pyramid"]:has(>.level>.note)>.level{width:calc(var(--crossrail-level-index)/var(--crossrail-levels)*50%);margin-right:50%} .pyramid[data-el="crossrail-pyramid"] .level>.note{position:fixed;left:55cqw;top:calc((var(--crossrail-level-index) - .5)*100cqh/var(--crossrail-levels));width:43cqw;transform:translateY(-50%);text-align:left;margin:0;color:var(--ink)}'
p.write_text(s)
# Preserve natural one-line pill sizing instead of stretching a label into a page-sized ellipse.
p=E/'pill/element.css';s=p.read_text();s=s.replace('border:2px solid var(--n-3);border-radius:999px;background:var(--page);color:var(--ink);padding:var(--gap-sm) var(--gap)','color:var(--ink)')
s=s.replace('.parts{display:flex;','.parts{box-sizing:border-box;border:2px solid var(--n-3);border-radius:999px;background:var(--page);padding:var(--gap-sm) var(--gap);display:flex;')
s=s.replace('].on{background:','].on .parts{background:').replace('].quiet{background:','].quiet .parts{background:').replace('].line{background:','].line .parts{background:')
p.write_text(s)
# Exact source-edge partition follows the same weighted branch layout using positive anchor rectangles.
p=E/'sankey/element.css';s=p.read_text();start='0 calc(100% - 50cqh - 30cqh*var(--v)/100)';end='0 calc(100% - 50cqh + 30cqh*var(--v)/100)';sourceY='100% - 80cqh + (200cqh - 100% - var(--crossrail-flow-index)*var(--gap-sm))*60cqh/(100cqh - var(--gap-sm)*(var(--crossrail-flow-count) - 1))';s=s.replace(start,'0 calc('+sourceY+')').replace(end,'0 calc('+sourceY+' + 60cqh*var(--v)/100)')
s=re.sub(r'(@|\.sankey\[data-el="crossrail-sankey"\]) \.branch>\.branch:nth-child\([234] of \.branch\)\{[^}]*\}','',s)
s=s.replace('top:0;width:18cqw;height:calc(var(--v)*1%)','top:anchor(var(--crossrail-nested-prev) bottom,0px);width:18cqw;height:calc(var(--v)*1%)')
s=s.replace('right:100%;top:50%;width:10cqw;border-top:1px solid var(--n-4)','right:100%;top:0;bottom:0;width:10cqw;background:inherit')
for i in range(1,7):s=s.replace(f'--crossrail-branch-anchor:--crossrail-branch-{i}',f'--crossrail-branch-anchor:--crossrail-branch-{i};--crossrail-flow-index:{i-1}')
for i in range(1,5):s+=f' .sankey[data-el="crossrail-sankey"]>.branch>.branch:nth-child({i} of .branch){{anchor-name:--crossrail-nested-{i};--crossrail-nested-prev:--crossrail-nested-{max(i-1,1)}}}'
s+=' .sankey[data-el="crossrail-sankey"]>.branch{anchor-scope:--crossrail-nested-1,--crossrail-nested-2,--crossrail-nested-3,--crossrail-nested-4} .sankey[data-el="crossrail-sankey"]>.branch>.branch:first-child{top:0}'
p.write_text(s)
# Copy prohibition outranks the golden copy requirement, while markup and quantitative data remain unchanged.
for p in (E/'card/fixtures').glob('replica-05*.html'):p.write_text(p.read_text().replace('SERVICE','DEPOT'))
for p in (E/'table/fixtures').glob('replica-16*.html'):p.write_text(p.read_text().replace('1500mm','1540mm').replace('1200mm','1260mm'))
# Honest minima for complex long-copy unreferenced examples.
for leaf,fn,minimum in [('hub','base-b.html','10x6'),('pyramid','base-a.html','8x4'),('pyramid','base-b.html','10x6')]:
 p=E/leaf/'fixtures'/fn;s=p.read_text();s=re.sub(r'<!-- min:[^>]*-->',f'<!-- min:{minimum} -->',s);p.write_text(s)
