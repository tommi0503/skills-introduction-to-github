from pathlib import Path
import sys,re,json,importlib.util
B=Path(__file__).parent;C=B.parent/'cinder-pulse';R=Path('/workspace/work/ref');L=B/'library';L.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('preview',R/'tools/preview.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
steps=json.loads((R/'contract/type-steps.json').read_text());pal=json.loads((R/'contract/palette.json').read_text())
for dark in [False,True]:
 mode='dark' if dark else 'light';source=m.sheet(C,steps,pal,dark,'../fonts/fonts.css');(L/f'{mode}.html').write_text(source)
 # per-element sheets contain every fixture, plus its most compact declared layout.
 css=source.split('<style>',1)[1].split('</style>',1)[0]
 for folder in [C/'foundation',*sorted((C/'elements').iterdir())]:
  fixtures=sorted((folder/'fixtures').glob('*.html'));cards=[]
  for f in fixtures:
   text=f.read_text();minimum=re.search(r'min:\s*(\d+)x(\d+)',text);body=re.sub(r'^<!--.*?-->\s*','',text,flags=re.S)
   for compact in [False,True]:
    label=f.stem+(' · min' if compact else ' · 12×6')
    if '<section' in body:slide=body.replace('class="slide','class="slide'+(' dark' if dark else ''),1)
    else:
     if compact and minimum:
      w,h=map(int,minimum.groups());body2=re.sub(r'grid-column:\s*1\s*/\s*span\s*12;\s*grid-row:\s*1\s*/\s*span\s*6',f'grid-column:1 / span {w}; grid-row:1 / span {h}',body,count=1)
     else:body2=body
     slide=f'<section class="slide'+(' dark' if dark else '')+f'"><div class="page"><div class="body">{body2}</div></div></section>'
    cards.append(f'<div class="tile"><div class="scaled">{slide}</div><div class="caption">{label}</div></div>')
  n=len(cards);cols=4 if n>9 else 3 if n>4 else 2;rows=(n+cols-1)//cols;scale=min(1/cols,1/rows)
  # fit all cards in one 1280×720 review page; every internal slide retains 1280×720.
  extra=f'''html,body{{margin:0;width:1280px;height:720px;overflow:hidden;background:#ddd}}body{{display:grid;grid-template-columns:repeat({cols},1fr);grid-template-rows:repeat({rows},1fr)}}.tile{{position:relative;overflow:hidden;border:1px solid #bbb}}.scaled{{position:absolute;left:0;top:0;transform:scale({scale});transform-origin:top left;width:1280px;height:720px}}.caption{{position:absolute;left:4px;bottom:2px;font:11px sans-serif;background:#fff;color:#222;padding:2px 4px}}'''
  (L/f'{folder.name}-{mode}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><style>{css}</style><style>{extra}</style><body>'+''.join(cards)+'</body></html>')
print('library sheets generated')
