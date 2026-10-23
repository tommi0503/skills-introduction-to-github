from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import sys,json,re,importlib.util,html
R=Path(__file__).parent; C=R.parent/'scanline-rise'; REF=Path('/workspace/work/ref'); OUT=R/'library';OUT.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('preview',REF/'tools/preview.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
steps=json.loads((REF/'contract/type-steps.json').read_text());palette=json.loads((REF/'contract/palette.json').read_text())
font='../assets/fonts/fonts.css'
for dark in [False,True]:
 text=m.sheet(C,steps,palette,dark=dark,fonts_href=font);(OUT/('dark.html' if dark else 'light.html')).write_text(text)
css=''.join(p.read_text() for p in [C/'kit/css/tokens.css',C/'foundation/foundation.css']+sorted((C/'elements').glob('*/element.css')))
css+=''.join(('.slide.dark' if mode=='dark' else '.slide')+'{'+''.join(k+':'+v+';' for k,v in vals.items())+'}' for mode,vals in palette.items())
css+='.slide{'+''.join(f'--type-{x}:{x}px;' for x in steps)+'--scanline-rise-angle:-90deg;--scanline-rise-i:0;--scanline-rise-c:var(--a1);}'
css+='[data-icon]:empty::after{content:"";width:100%;height:100%;border:1px dashed currentColor;border-radius:50%;box-sizing:border-box;display:block}'
folders=[C/'foundation']+sorted((C/'elements').iterdir());audit=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for dark in [False,True]:
  mode='dark' if dark else 'light';imgs=[]
  for folder in folders:
   name=folder.name;cells=[]
   for f in sorted((folder/'fixtures').glob('*.html')):
    txt=f.read_text();match=re.search(r'<!-- min:\s*(\d+)x(\d+)',txt);mini=(int(match[1]),int(match[2])) if match else (8,4);txt=re.sub(r'<!--.*?-->','',txt,flags=re.S).strip()
    if txt.startswith('<section'):full=txt.replace('class="slide',f'class="slide {mode if dark else ""}',1)
    else:full=f'<section class="slide {mode if dark else ""}"><div class="page"><div class="body">{txt}</div></div></section>'
    for size in [(12,6),mini]:
     doc='<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="'+font+'"><style>html,body{margin:0;padding:0;width:1280px;height:720px}'+css+'</style><body>'+full+'</body></html>'
     if size!=(12,6):doc=re.sub(r'grid-column:\s*1 / span 12;\s*grid-row:\s*1 / span 6',f'grid-column:1 / span {size[0]}; grid-row:1 / span {size[1]}',doc)
     (OUT/'audit-current.html').write_text(doc);page.goto('http://127.0.0.1:8765/scanline-rise-review/library/audit-current.html?n='+str(len(audit)));page.evaluate('document.fonts.ready')
     found=page.evaluate('''() => ({font:document.fonts.check('16px "Pretendard Variable"'),overflow:[...document.querySelectorAll('[data-el], [data-el] .parts, [data-el] .name,[data-el] .note,[data-el] .fig,[data-el] .chip')].filter(e=>e.clientWidth&&e.clientHeight&&(e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+3)).map(e=>({class:e.className,text:e.textContent.slice(0,70),w:e.clientWidth,sw:e.scrollWidth,h:e.clientHeight,sh:e.scrollHeight}))})''')
     audit.append({'element':name,'fixture':f.stem,'mode':mode,'size':size,**found})
    cells.append((f.stem,full))
   # All fixtures of one element remain visible on a single 1280x720 review sheet.
   cols=3 if len(cells)>4 else 2;rows=(len(cells)+cols-1)//cols;cw=1280/cols;ch=720/max(rows,2);scale=min(cw/1280,(ch-24)/720)
   blocks=''.join(f'<article><h2>{html.escape(label)}</h2><div class="frame">{slide}</div></article>' for label,slide in cells)
   sheet=f'<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../{font}"><style>{css}</style><style>html,body{{margin:0;width:1280px;height:720px;background:#dedee2;font:12px sans-serif}}body{{display:grid;grid-template-columns:repeat({cols},1fr);grid-auto-rows:{ch}px}}article{{padding:6px;overflow:hidden}}h2{{font:12px sans-serif;margin:0 0 6px;height:14px}}.frame{{height:{720*scale}px;width:{1280*scale}px}}.frame>.slide{{transform:scale({scale});transform-origin:0 0}}</style><body>{blocks}</body></html>'
   dest=OUT/name;dest.mkdir(exist_ok=True);(dest/f'{mode}.html').write_text(sheet);page.goto(f'http://127.0.0.1:8765/scanline-rise-review/library/{name}/{mode}.html');page.evaluate('document.fonts.ready');page.screenshot(path=str(dest/f'{mode}.png'));imgs.append(Image.open(dest/f'{mode}.png').convert('RGB'))
  imgs[0].save(OUT/f'library-{mode}.pdf',save_all=True,append_images=imgs[1:],resolution=96)
 b.close()
(OUT/'audit-current.html').unlink(missing_ok=True)
(R/'library-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
print('audit',len(audit),'overflow',sum(bool(x['overflow']) for x in audit))
