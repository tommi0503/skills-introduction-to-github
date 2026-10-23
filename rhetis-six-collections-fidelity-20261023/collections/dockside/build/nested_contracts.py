exec(open('/workspace/work/deliverables/dockside/build/refine_collection.py').read().split("f='chart-area'")[0])
from bs4 import BeautifulSoup
for p in C.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name not in ['pricing','person','matrix','versus']:continue
 b=BeautifulSoup(p.read_text(),'html.parser')
 for u in b.select('ul.list'):
  items=[li.get_text(' ',strip=True) for li in u.find_all('li',recursive=False)];q=b.new_tag('div');q['class']=['list']+(['check'] if p.parent.parent.name=='pricing' else []);q['data-el']='dockside-list'
  for t in items:
   item=b.new_tag('div');item['class']=['item'];name=b.new_tag('b');name['class']=['name'];name.string=t;item.append(name);q.append(item)
  u.replace_with(q)
 for q in b.select('.tag'):q['data-el']='dockside-tag'
 p.write_text(str(b))
# Decrease the specificity of inherited typography so nested owned elements keep their own styles.
for p in C.glob('elements/*/element.css'):
 f=p.parent.name;r=root(f);s=p.read_text();end=s.find(r+' p{margin:0}')
 if end>=0:
  end+=len(r+' p{margin:0}');s=s[:end].replace(r,':where('+r+')')+s[end:]
 if f=='person':s=s.replace(r+' .name{display:flex',r+'>.name,'+r+' .person>.name{display:flex')
 p.write_text(s)
f='list';r=root(f);append(f,f':is(.plan,.person,.side,.cell)>{r}{{container-type:normal;flex:none;width:100%;gap:var(--gap-sm)}}:is(.plan,.person,.side,.cell)>{r} .name{{font-size:var(--type-16);font-weight:var(--body-weight);text-align:left}}:is(.plan,.person,.side,.cell)>{r} .item{{padding-left:var(--pad)}}:is(.plan,.person,.side,.cell)>{r}.check .item{{padding:calc(var(--gap-sm)/2) var(--gap-sm) calc(var(--gap-sm)/2) calc(var(--pad)*1.5);box-shadow:none;background:none;border:0}}:is(.plan,.person,.side,.cell)>{r}.check .item::before{{left:var(--gap-sm)}}:is(.plan,.person,.side,.cell)>{r}.check .item::after{{left:calc(var(--gap-sm) + 5px)}}')
f='code';r=root(f);append(f,f'{r} .c{{color:var(--n-8)}}')
f='chart-scatter';r=root(f);append(f,f'{r} .dot span{{background:var(--page);color:var(--ink);padding:calc(var(--gap-sm)/4);border-radius:var(--radius-sm)}}')
