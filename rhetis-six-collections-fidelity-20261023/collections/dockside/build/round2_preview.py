import sys
from pathlib import Path
sys.path.insert(0,'/workspace/work/tools')
from render_review import load,browser,pdf_from_pngs
from playwright.sync_api import sync_playwright
from PIL import Image
R=Path('/workspace/work/deliverables/dockside');D=Path('/workspace/work/deck/miricanvas_기업_selected/016_1j5ap_파랑_깔끔_아이디어_피칭_기획서')
with sync_playwright() as p:
 b=browser(p);page=b.new_page(viewport={'width':1280,'height':720})
 for n in [int(x) for x in sys.argv[1:]] or [5]:
  f=R/f'review/reassembled/slide_{n:02}.html';load(page,f);page.wait_for_timeout(600);out=R/f'review/round2/after-{n:02}.png';page.screenshot(path=str(out));im=Image.new('RGB',(2560,720));im.paste(Image.open(D/f'slide_{n:02}.png'),(0,0));im.paste(Image.open(out),(1280,0));im.save(R/f'review/round2/compare-{n:02}.png')
 b.close()
