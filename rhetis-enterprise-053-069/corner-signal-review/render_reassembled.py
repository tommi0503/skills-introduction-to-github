from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import json
R=Path(__file__).parent;D=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('067*'));checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for f in sorted((R/'reassembled').glob('slide*.html')):
  page.goto('http://127.0.0.1:8765/corner-signal-review/reassembled/'+f.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(f.with_suffix('.png')))
  a=page.evaluate("""()=>{let s=document.querySelector('.slide'),b=s.getBoundingClientRect(),outside=[],clipped=[];s.querySelectorAll('[data-el]').forEach(e=>{let r=e.getBoundingClientRect();if(r.width&&r.height&&(r.left<b.left-1||r.top<b.top-1||r.right>b.right+1||r.bottom>b.bottom+1))outside.push(e.dataset.el);if(e.scrollHeight>e.clientHeight+2||e.scrollWidth>e.clientWidth+2)clipped.push({el:e.dataset.el,client:[e.clientWidth,e.clientHeight],scroll:[e.scrollWidth,e.scrollHeight]})});return{size:[b.width,b.height],font:document.fonts.check('16px "Pretendard Variable"'),outside:outside,clipped:clipped}}""")
  checks.append(dict(page=f.name,**a));c=Image.new('RGB',(2560,720),'white');c.paste(Image.open(D/f.with_suffix('.png').name),(0,0));c.paste(Image.open(f.with_suffix('.png')),(1280,0));c.save(R/'compare-reassembled'/f.with_suffix('.png').name)
 b.close()
ims=[Image.open(f).convert('RGB') for f in sorted((R/'reassembled').glob('slide*.png'))];ims[0].save(R/'reassembled/reassembled.pdf',save_all=True,append_images=ims[1:],resolution=96)
(R/'reassembled-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print(json.dumps(checks,ensure_ascii=False))
