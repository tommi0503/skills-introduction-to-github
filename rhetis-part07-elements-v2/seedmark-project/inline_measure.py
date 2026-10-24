from pathlib import Path
from playwright.sync_api import sync_playwright
import json
P=Path(__file__).parent;m=json.loads((P/'map.json').read_text());rows=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 p=b.new_page(viewport={'width':1280,'height':720})
 for n in range(1,22):
  p.goto(f'http://127.0.0.1:8875/seedmark-project/replica/slide_{n:02}.html');p.evaluate('document.fonts.ready')
  a=p.evaluate('''()=>[...document.querySelectorAll('main > *')].flatMap((parent,j)=>[...parent.querySelectorAll('b,span,small,strong')].filter(e=>e.textContent.trim()).map((e,k)=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e),p=getComputedStyle(parent);return {parentIndex:j,childIndex:k,tag:e.tagName,classes:e.className,text:e.textContent.trim(),bbox:[r.x,r.y,r.width,r.height],fontSize:s.fontSize,fontWeight:s.fontWeight,lineHeight:s.lineHeight,letterSpacing:s.letterSpacing,fontFamily:s.fontFamily,parentFontSize:p.fontSize,parentFontWeight:p.fontWeight};}))''')
  canvas=p.locator('main').evaluate('(e)=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return {bbox:[r.x,r.y,r.width,r.height],backgroundColor:s.backgroundColor};}')
  rows.append({'page':n,'parts':a,'canvas':canvas})
 b.close()
m['instances']=[i for i in m['instances']if not i['id'].endswith('-canvas')]
for r in rows:m['instances'].append({'id':f"sm-{r['page']:02}-canvas",'page':r['page'],'leaf':None,'use':'background','bbox':r['canvas']['bbox'],'selectors':['main.slide'],'fixture':None,'paletteRole':'--page','sourceMeasurements':[r['canvas']]})
m['inlineMeasurements']=rows;(P/'map.json').write_text(json.dumps(m,ensure_ascii=False,indent=2));print('Measured',sum(len(r['parts'])for r in rows),'inline parts without editing a replica.')
for r in rows:
 for a in r['parts']:
  if a['fontSize']!=a['parentFontSize']or a['fontWeight']!=a['parentFontWeight']:print(r['page'],a['text'][:25],a['parentFontSize'],a['fontSize'],a['parentFontWeight'],a['fontWeight'])
