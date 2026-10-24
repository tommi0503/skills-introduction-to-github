from pathlib import Path
import asyncio,json
from playwright.async_api import async_playwright
P=Path('/workspace/work/publish/rhetis-component-rebuild-20261024')
async def main():
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await b.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));await page.goto('http://127.0.0.1:8768/preview.html');rows=[]
  async def ready():
   await page.wait_for_function("document.querySelector('#artifact').complete && document.querySelector('#artifact').naturalWidth>0");await page.wait_for_timeout(30)
  for n in ['nocturne','inflexion','diecut','afterglow','dockside','confluence']:
   await page.select_option('#collection',n)
   for tab in ['sizes','replica','pages']:
    await page.click('[data-tab="'+tab+'"]')
    if tab=='replica':
     candidates=await page.evaluate("Object.entries(RhetisReview.data.collections.find(c=>c.name===RhetisReview.state.collection).leaves).filter(([k,v])=>v.hasComparison).map(([k,v])=>k)")
     await page.select_option('#leaf',candidates[0])
    for mode in (['light','dark']if tab=='sizes'else['light']):
     if tab=='sizes':await page.click('[data-mode="'+mode+'"]')
     await ready();rows.append(await page.evaluate("({state:RhetisReview.state,url:RhetisReview.imageURL,width:document.querySelector('#artifact').naturalWidth,height:document.querySelector('#artifact').naturalHeight})"))
   await page.click('#actual');await page.click('#fit')
  await page.screenshot(path=str(P/'preview-desktop.png'),full_page=True)
  await page.set_viewport_size({'width':390,'height':844});await page.screenshot(path=str(P/'preview-mobile.png'),full_page=True)
  assert not errors,errors
  assert len(rows)==24
  (P/'preview-validation.json').write_text(json.dumps({'browser':'Chromium','screenChecks':rows,'scriptErrors':errors,'desktop':[1440,1000],'mobile':[390,844]},ensure_ascii=False,indent=2));print('preview24views scriptErrors0');await b.close()
asyncio.run(main())
