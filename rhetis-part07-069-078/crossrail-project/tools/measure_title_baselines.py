from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
import json
P=Path(__file__).parent
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for n in range(1,31):
  for stage in ['replica','reassembled']:
   g.goto(f'http://127.0.0.1:8765/crossrail-project/{stage}/slide_{n:02}.html');g.evaluate('document.fonts.ready');g.wait_for_timeout(30);g.screenshot(path=str(P/f'qa/baseline-{stage}-{n:02}.png'))
 b.close()
def bounds(im,dark):
 im=im.convert('RGB');pts=[]
 for y in range(125,220):
  for x in range(96,450):
   r,g,b=im.getpixel((x,y))
   keep=(r>205 and g>205 and b>205 and max(r,g,b)-min(r,g,b)<35) if dark else (r<100 and g<125 and b<170 and b>r+10)
   if keep:pts.append((x,y))
 if not pts:return None
 # Require five actual glyph pixels in a row to reject isolated compression dots.
 ys={y:sum(yy==y for xx,yy in pts) for y in range(125,220)};valid=[y for y,v in ys.items() if v>=5]
 return [min(valid),max(valid)] if valid else None
out=[]
for n in range(1,31):
 if n in [25,30]:continue
 orig=Image.open(P/f'compare-replica/slide_{n:02}.png').crop((0,0,1280,720));dark=n in [1,2,9,13,17,21]
 # Only first title line is within this ROI; source05/sidebar is white here.
 bs=[bounds(orig,dark)]+[bounds(Image.open(P/f'qa/baseline-{stage}-{n:02}.png'),dark) for stage in ['replica','reassembled']]
 out.append({'page':n,'dark':dark,'original':bs[0],'replica':bs[1],'reassembled':bs[2]})
(P/'qa/title-baselines-before.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out))
