from pathlib import Path
import importlib.util,json,sys
from playwright.sync_api import sync_playwright
from PIL import Image
MERGED='--merged' in sys.argv
BASE=Path('/workspace/work/rhetis-part07');P=BASE/'meridian-deck-project';s=importlib.util.spec_from_file_location('tail',P/'fidelity_tail_patch.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
original=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('074_*'))
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720});report={}
 for n in ([27] if '--badge' in sys.argv else [27,29] if '--targeted' in sys.argv else range(25,30)):
  q.goto(f'http://127.0.0.1:8765/meridian-deck-project/reassembled/slide_{n}.html',wait_until='networkidle');q.evaluate('document.fonts.ready');
  if not MERGED:q.add_style_tag(content=m.FOUNDATION_PATCH+'\n'+'\n'.join(m.ELEMENT_PATCHES.values()));
  q.wait_for_timeout(100)
  out=BASE/'qa'/f'meridian-tail-{n}{"-merged" if MERGED else ""}.png';q.screenshot(path=str(out));a=Image.open(original/f'slide_{n}.png').convert('RGB').resize((1280,720));c=Image.open(out);combo=Image.new('RGB',(2560,720));combo.paste(a,(0,0));combo.paste(c,(1280,0));combo.save(BASE/'qa'/f'meridian-tail-{n}{"-merged" if MERGED else ""}-compare.png')
  report[n]=q.evaluate('''()=>[...document.querySelectorAll('.body > *, .body [data-el],.body .group,.body .stack')].map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return {el:e.className,kind:e.dataset.el,box:[r.x,r.y,r.width,r.height],font:s.fontSize,text:e.textContent.trim().slice(0,60)}})''')
 (BASE/('qa/meridian-tail-merged-boxes.json' if MERGED else 'qa/meridian-tail-boxes.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2));b.close()
