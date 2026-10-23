from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json,sys
R=Path(__file__).parent
ORIG=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('056*'))
kind=sys.argv[1] if len(sys.argv)>1 else 'replica'
folder=R/kind; compare=R/('compare-'+kind);compare.mkdir(exist_ok=True)
audit=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for i in range(1,19):
  src=folder/f'slide-{i:02}.html';page.goto('http://127.0.0.1:8765/scanline-rise-review/'+kind+'/'+src.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(folder/f'slide-{i:02}.png'))
  a=page.evaluate('''() => ({font:document.fonts.check('16px "Pretendard Variable"'),width:document.querySelector('.slide').getBoundingClientRect().width,height:document.querySelector('.slide').getBoundingClientRect().height,overflow:[...document.querySelectorAll('p,li,.note,.name,.fig,.cap')].filter(e=>e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2).map(e=>({text:e.textContent.slice(0,80),class:e.className,sw:e.scrollWidth,cw:e.clientWidth,sh:e.scrollHeight,ch:e.clientHeight}))})''');a['page']=i;audit.append(a)
  left=Image.open(ORIG/f'slide_{i:02}.png').convert('RGB');right=Image.open(folder/f'slide-{i:02}.png').convert('RGB');im=Image.new('RGB',(2560,720));im.paste(left,(0,0));im.paste(right,(1280,0));im.save(compare/f'slide-{i:02}.png')
 b.close()
(R/(kind+'-audit.json')).write_text(json.dumps(audit,ensure_ascii=False,indent=2))
ims=[Image.open(folder/f'slide-{i:02}.png').convert('RGB') for i in range(1,19)];ims[0].save(folder/(kind+'.pdf'),save_all=True,append_images=ims[1:],resolution=96)
print(kind,len(audit),'overflow',sum(bool(a['overflow']) for a in audit))
