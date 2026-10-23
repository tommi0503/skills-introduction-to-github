from pathlib import Path
import json,re
from lxml import html
from playwright.sync_api import sync_playwright
from PIL import Image
P=Path(__file__).parent;Q=P/'qa-final-source-patch';Q.mkdir(exist_ok=True);S=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('078*'));report={}
# Keep source composition and its public fixture in parity.
a=html.fromstring((P/'reassembled/slide_16.html').read_text()).xpath('//div[contains(concat(" ",@class," ")," body ")]/div')[0];b=html.fromstring((P/'onboard-docket/elements/list/fixtures/tabs-three-source.html').read_text());assert a.get('class')==b.get('class')=='group overrides';assert [e.get('class')for e in a.xpath('./div')]==[e.get('class')for e in b.xpath('./div')]==['stack overrides']*3;report['sourceFixtureParity']=True
with sync_playwright()as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=browser.new_page(viewport={'width':1280,'height':720})
 for n in [1,4,6,8,11,13,14,15,16]:
  page.goto(f'http://127.0.0.1:8765/onboard-docket-project/reassembled/slide_{n:02}.html',wait_until='networkidle');page.evaluate('document.fonts.ready');page.screenshot(path=str(Q/f'assembly_{n:02}.png'));pair=Image.new('RGB',(2560,720));pair.paste(Image.open(S/f'slide_{n:02}.png').convert('RGB'),(0,0));pair.paste(Image.open(Q/f'assembly_{n:02}.png').convert('RGB'),(1280,0));pair.save(Q/f'slide_{n:02}.png')
  data=page.evaluate('''()=>({viewport:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],source:document.querySelector('.slide').classList.contains('src'),numberPaint:[...document.querySelectorAll('.seat')].map(e=>getComputedStyle(e,'::after').content)})''');assert data['viewport']==[1280,720];assert data['source'];assert all(x=='none'for x in data['numberPaint']);report[str(n)]=data
  if n==1:
   centers=page.evaluate('''()=>[...document.querySelectorAll('.deco svg')].map(e=>{let r=e.getBoundingClientRect(),b=e.getBBox(),s=getComputedStyle(e);return r.y+parseFloat(s.paddingTop)+parseFloat(s.height)*(b.y+b.height/2)/24})''');report['coverIconPaintCenters']=centers;assert all(abs(y-(115+83*i))<2 for i,y in enumerate(centers)),centers
  if n==16:
   rects=page.evaluate('''()=>[...document.querySelectorAll('.list.divided,.stack>.pill')].map(e=>{let r=e.getBoundingClientRect();return[e.className,r.x,r.y,r.width,r.height]})''');report['panelsAndTabs']=rects;panels=[r for r in rects if'list'in r[0]];tabs=[r for r in rects if'pill'in r[0]];assert all(abs(r[1]-(161+326*i))<.6 and abs(r[3]-306)<.6 for i,r in enumerate(panels)),panels;assert all(abs(r[3]-266)<.6 for r in tabs),tabs
 page.goto('http://127.0.0.1:8765/onboard-docket-project/replica/slide_04.html',wait_until='networkidle');page.evaluate('document.fonts.ready');page.screenshot(path=str(Q/'replica_04.png'));browser.close()
orig=Image.open(S/'slide_14.png').convert('RGB');now=Image.open(Q/'assembly_14.png').convert('RGB');report['lensColors']={'original':[(x,orig.getpixel((x,362)))for x in [466,637,808]],'assembly':[(x,now.getpixel((x,362)))for x in [466,637,808]]}
for n in ['original','assembly']:
 im=Image.open(S/'slide_06.png'if n=='original'else Q/'assembly_06.png').convert('RGB');report['bottomGap_'+n]=[x for x in range(626,654)if min(im.getpixel((x,555)))>240]
(Q/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in report.items()if k not in [str(n)for n in [1,4,6,8,11,13,14,15,16]]},ensure_ascii=False))
