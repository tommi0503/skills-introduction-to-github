from pathlib import Path
import re
B=Path('/workspace/output/roundrise');p=B/'foundation/foundation.css';s=p.read_text();a=[];c=[]
def move(m):
 sel,body=m[1],m[2]
 if sel.endswith('.body:has(>.agenda)>.agenda'):
  a.append('.agenda[data-el="roundrise-agenda"]{'+body+'}');return ''
 if re.search(r'>\.card\.line\+\.card\.line(?::before)?$',sel):
  r='.card.line[data-el="roundrise-card"]:is(.group.two>.card.line+.card.line)'
  if sel.endswith(':before'):r+=':before'
  if '.slide.dark' in sel:r='.slide.dark '+r
  c.append(r+'{'+body+'}');return ''
 return m[0]
s=re.sub(r'([^{}]+)\{([^{}]*)\}',move,s);p.write_text(s)
for name,rules in [('agenda',a),('card',c)]:
 p=B/'elements'/name/'element.css';p.write_text(p.read_text()+''.join(rules))
p=B/'kit/css/tokens.css';s=p.read_text().replace('.slide{--roundrise-split-title-line:1.33;}','');p.write_text(s)
p=B/'elements/headline/element.css';s=p.read_text().replace('var(--roundrise-split-title-line)','calc(var(--name-line) + .03)');p.write_text(s)
