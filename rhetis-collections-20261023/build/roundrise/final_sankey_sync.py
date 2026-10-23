from pathlib import Path
import importlib.util,json,fitz
from PIL import Image
from playwright.sync_api import sync_playwright
R=Path('/workspace/output/roundrise-review');r=Path('/workspace/work/reference');spec=importlib.util.spec_from_file_location('prev',r/'tools/preview.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
for mode in ['light','dark']:
 (R/'library'/f'{mode}.html').write_text(m.sheet('/workspace/output/roundrise',json.loads((r/'contract/type-steps.json').read_text()),json.loads((r/'contract/palette.json').read_text()),dark=mode=='dark',fonts_href='../replica/assets/fonts/fonts.css'))
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1328,'height':900},device_scale_factor=1)
 for mode in ['light','dark']:
  pg.goto('http://127.0.0.1:8767/library/'+mode+'.html');pg.evaluate('document.fonts.ready');group=[];targets=[]
  for i,a in enumerate(pg.locator('article').all()):
   title=a.locator(':scope>h2').inner_text()
   if title.startswith('sankey / '):
    f=R/'library/fixtures'/mode/f'{i:03}.png';f.parent.mkdir(parents=True,exist_ok=True);a.screenshot(path=str(f));group.append(f)
    targets.append((i,a))
  board=Image.new('RGB',(1280,((len(group)+1)//2)*400),'#e8e8ec')
  for j,f in enumerate(group):
   im=Image.open(f).convert('RGB');im.thumbnail((632,390));board.paste(im,((j%2)*640,(j//2)*400))
  board.save(R/'library/sankey'/f'{mode}.png')
  assert targets
  pg.add_style_tag(content='body{display:block;padding:0;margin:0}article{width:1280px;height:720px;overflow:hidden}article>h2{display:none}.frame{width:1280px;height:720px;border-radius:0;overflow:hidden}.frame>.slide{transform:none;width:1280px;height:720px}')
  path=R/'library'/f'library-{mode}.pdf';doc=fitz.open(path)
  for idx,a in targets:
   raw=a.locator('.slide').screenshot();page=doc.new_page(pno=idx,width=1280,height=720);page.insert_image(page.rect,stream=raw);doc.delete_page(idx+1)
  tmp=path.with_suffix('.tmp.pdf');doc.save(tmp,deflate=True,deflate_images=True);doc.close();tmp.replace(path);print(mode,'sankey pages synced',flush=True)
 b.close()
