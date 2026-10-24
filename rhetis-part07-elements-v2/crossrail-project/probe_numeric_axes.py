from pathlib import Path
from lxml import html
import json,re
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;out=P/'axis-probes';out.mkdir(exist_ok=True);records=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for n in [20,22,0]:
  q=b.new_page(viewport={'width':1280,'height':720})
  if n:
   q.goto(f'http://127.0.0.1:8875/crossrail-project/reassembled/slide_{n:02}.html',wait_until='networkidle')
  else:
   d=html.fromstring((P/'reassembled/slide_22.html').read_text());old=d.xpath('//*[@data-el="crossrail-chart-line"]')[0];new=html.fromstring((P/'crossrail/elements/chart-line/fixtures/lines-3.html').read_text());new.set('style','grid-column:7 / span 5;grid-row:1 / span 5;--max:2.6');old.getparent().replace(old,new);f=out/'decimal.html';f.write_text('<!doctype html>'+html.tostring(d,encoding='unicode'));q.goto('http://127.0.0.1:8875/crossrail-project/axis-probes/decimal.html',wait_until='networkidle')
  q.evaluate('document.fonts.ready');q.wait_for_timeout(250)
  item=q.locator('[data-el="crossrail-chart-bar"],[data-el="crossrail-chart-line"]').first
  d=item.evaluate('''e=>{let r=e.getBoundingClientRect();let style=x=>{let s=getComputedStyle(e,x);return {content:s.content,counterSet:s.counterSet,font:s.fontSize,line:s.lineHeight,top:s.top,left:s.left,width:s.width,height:s.height,opacity:s.opacity}};return {bbox:[r.x,r.y,r.width,r.height],max:getComputedStyle(e).getPropertyValue('--max'),before:style('::before'),after:style('::after')}}''');d['case']=n;records.append(d);item.screenshot(path=str(out/f'axis-{n}.png'));q.close()
 b.close()
(P/'numeric-axis-proof.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');print(json.dumps(records,ensure_ascii=False,indent=2))
