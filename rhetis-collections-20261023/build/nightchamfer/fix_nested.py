from pathlib import Path
import re
C=Path('/workspace/output/nightchamfer')
for n in ['versus','person','matrix','pricing']:
 for p in (C/'elements'/n/'fixtures').glob('*.html'):
  s=p.read_text()
  def lst(m):
   inner=re.sub(r'<li>(.*?)</li>',r'<div class="item"><b class="name">\1</b></div>',m.group(1),flags=re.S)
   return '<div class="list'+(' check'if n=='pricing'else '')+'" data-el="nightchamfer-list">'+inner+'</div>'
  s=re.sub(r'<ul class="list">(.*?)</ul>',lst,s,flags=re.S)
  s=s.replace('<span class="tag">','<span class="tag" data-el="nightchamfer-tag">')
  p.write_text(s)
p=C/'elements/tag/element.css';p.write_text(p.read_text()+'\n[data-el="nightchamfer-tag"].tag,[data-el="nightchamfer-tag"].hl{container-type:normal}\n')
p=C/'elements/pricing/element.css';p.write_text(p.read_text()+'\n[data-el="nightchamfer-pricing"] .list .item{padding-top:calc(var(--gap-sm)/3);padding-bottom:calc(var(--gap-sm)/3)}\n')
