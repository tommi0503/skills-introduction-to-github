"""Read card-row alignment without treating unnamed figures as failed headings.
Preserves raw measurements and separates explicitly documented source compositions.
"""
from pathlib import Path
import sys,json,re,importlib.util,hashlib
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE,COLLECTIONS
spec=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(spec);spec.loader.exec_module(pv)
GOLDEN={'card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone'}
if __name__=='__main__':
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1360,'height':900});page.goto('http://127.0.0.1:8765/qa/probe.html')
  for k in (sys.argv[1:] or COLLECTIONS):
   root=BASE/(k+'-project')/k
   if len(list((root/'elements').glob('*/element.css')))!=56:continue
   markup=pv.sheet(root,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),fonts_href=f'/{k}-project/assets/fonts/fonts.css')
   page.set_content(markup,wait_until='networkidle');page.evaluate('document.fonts.ready')
   result=page.evaluate('''()=>{let out=[];for(let a of document.querySelectorAll('article')){let title=a.querySelector('h2').textContent;if(!title.startsWith('card /'))continue;let cards=[...a.querySelectorAll('.card')];if(cards.length<2)continue;let ys=cards.map(c=>{let n=c.querySelector('.name');return n?n.getBoundingClientRect().y:null}).filter(y=>y!==null),relative=ys.map(y=>+(y-Math.min(...ys)).toFixed(2)),slide=a.querySelector('.slide'),scale=slide.getBoundingClientRect().width/slide.offsetWidth;out.push({fixture:title,cardCount:cards.length,namedCardCount:ys.length,nameAbsent:ys.length===0,titleOffsets:relative,drift:relative.length?Math.max(...relative):null,unscaledDrift:relative.length?+(Math.max(...relative)/scale).toFixed(2):null,status:ys.length<2?'not-applicable':Math.max(...relative)>1?'needs-review':'pass'});}return out}''')
   for item in result:
    name=item['fixture'].split(' / ',1)[1].split(' min ',1)[0];item['golden']=name in GOLDEN
    if k=='vectorbox' and name=='source-caption-pair' and item['status']!='not-applicable':
     item['status']='intentional-composition';item['intentionalComposition']={'reason':'The source page places normal and quiet caption cards at different vertical origins; quiet preserves its 58px internal source offset. Raw drift is retained, not counted as a golden-row pass.','expectedUnscaledOffset':58}
   golden=[x for x in result if x['golden']];regular=[x for x in result if not x['golden'] and x['status'] in ['pass','needs-review']];intentional=[x for x in result if x['status']=='intentional-composition'];na=[x for x in result if x['status']=='not-applicable']
   report={'collection':k,'sourceSha256':hashlib.sha256(markup.encode()).hexdigest(),'summary':{'goldenRows':len(golden),'goldenFailures':sum(x['status']=='needs-review' for x in golden),'regularRows':len(regular),'regularFailures':sum(x['status']=='needs-review' for x in regular),'intentionalCompositions':len(intentional),'notApplicable':len(na)},'checks':result,'intentionalComposition':intentional,'notApplicable':na}
   (BASE/'qa'/(k+'-alignment-audit.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n');print(k,report['summary'],flush=True)
  b.close()
