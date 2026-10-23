from pathlib import Path
import re,json
B=Path(__file__).parent;C=B.parent/'cinder-pulse';required={'card','callout','chart-area','chart-bar','chart-donut','chart-line'};changes=[]
def convert(m):
 attrs=m.group(2);body=m.group(3)
 body=re.sub(r'<li(?:\s[^>]*)?>(.*?)</li>',lambda n:'<div class="item"><p class="name">'+n.group(1)+'</p><p class="note"></p></div>',body,flags=re.S)
 return '<div'+attrs+'>'+body+'</div>'
for p in C.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name in required:continue
 s=p.read_text();old=s
 s=re.sub(r'<(ul|ol)([^>]*class="[^"]*\blist\b[^"]*"[^>]*)>(.*?)</\1>',convert,s,flags=re.S)
 def scope(m):
  tag=m.group(0)
  if 'data-el=' in tag:return tag
  name='list' if re.search(r'class="[^"]*\blist\b',tag) else 'tag'
  return tag[:-1]+f' data-el="cinder-pulse-{name}">'
 s=re.sub(r'<(?:div|span|p|ul|ol)\b[^>]*class="[^"]*\b(?:list|tag|hl)\b[^"]*"[^>]*>',scope,s)
 if s!=old:p.write_text(s);changes.append(str(p.relative_to(C)))
for p in C.glob('elements/*/element.css'):
 s=p.read_text().replace('color:var(--a1);','color:var(--a1-8);').replace('color:var(--n-6);','color:var(--n-7);');p.write_text(s)
p=C/'elements/sparkline/element.css';p.write_text(p.read_text()+'\n.parts>.spark[data-el="cinder-pulse-sparkline"]{height:var(--gap-lg);min-height:var(--gap-lg);}\n')
(B/'normalization.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2));print('normalized',len(changes),'fixture files')
