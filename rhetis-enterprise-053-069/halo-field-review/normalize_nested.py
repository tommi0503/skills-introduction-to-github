from pathlib import Path
import re
R=Path(__file__).parent;C=R.parent/'halo-field';mandatory={'card','callout','chart-area','chart-bar','chart-donut','chart-line'}
for d in (C/'elements').iterdir():
 if d.name in mandatory:continue
 for p in (d/'fixtures').glob('*.html'):
  s=p.read_text()
  s=re.sub(r'<ul class="(list[^"]*)"[^>]*>',lambda m:'<div class="'+m[1]+'" data-el="halo-field-list">',s).replace('</ul>','</div>')
  s=re.sub(r'<li[^>]*>(.*?)</li>',lambda m:'<div class="item"><p class="name">'+m[1]+'</p><p class="note">목표에 맞춰 실행 범위를 조정합니다.</p></div>',s,flags=re.S)
  s=re.sub(r'<(div|span|b) class="(list(?: [^"]*)?|tag|hl)"(?![^>]*data-el=)',lambda m:'<'+m[1]+' class="'+m[2]+'" data-el="halo-field-'+('list' if m[2].startswith('list') else 'tag')+'"',s)
  p.write_text(s)
p=C/'elements/list/element.css';p.write_text(p.read_text()+'''\n@container(max-height:240px){[data-el="halo-field-list"][data-el="halo-field-list"][data-el="halo-field-list"] .note{display:none}}''')
print('nested contract normalization complete')
