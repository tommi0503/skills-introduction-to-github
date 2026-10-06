import {createServer,preview} from 'vite'
import {chromium} from 'playwright-core'
import {createHash} from 'node:crypto'
import {readFileSync,writeFileSync} from 'node:fs'
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
const production=await preview({preview:{host:'127.0.0.1',port:0}})
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try {
 const page=await browser.newPage({viewport:{width:1440,height:900}})
 const errors=[];page.on('pageerror',e=>errors.push(e.message))
 await page.goto(`http://127.0.0.1:${server.httpServer.address().port}`,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.decks})
 if(decks.length!==32)throw Error('Missing decks')
 if(decks.reduce((n,d)=>n+d.slides.length,0)!==113)throw Error('Missing observed source panels')
 const rendererHash=createHash('sha256').update(['src/ui.tsx','src/model.ts','src/index.css','src/App.tsx','src/registry.ts'].map(name=>readFileSync(name,'utf8')).join('\n')).digest('hex')
 for(const d of decks){
  const hash=createHash('sha256').update(JSON.stringify(d)).digest('hex')
  const meta=JSON.parse(readFileSync(`comparisons/${d.id}.json`))
  if(hash!==meta.definitionHash)throw Error(`Stale render ${d.id}`)
  if(meta.rendererHash!==rendererHash)throw Error(`Stale renderer ${d.id}`)
  if(d.slides.length!==d.referenceRegions.length)throw Error(`Missing source crop ${d.id}`)
 }
 const url=`http://127.0.0.1:${production.httpServer.address().port}`
 await page.goto(url,{waitUntil:'networkidle'})
 if(await page.locator('.deck-card').count()!==32)throw Error('Missing gallery cards')
 await page.locator('.deck-card').first().click()
 await page.locator('.toolbar').waitFor()
 await page.locator('.deck-board [data-slide]').first().waitFor()
 await page.getByRole('link',{name:'원본 비교'}).click()
 await page.locator('.comparison img').waitFor()
 await page.waitForFunction(()=>document.querySelector('.comparison img').naturalWidth>0)
 await page.goto(`${url}/#/slide/r26/s01`,{waitUntil:'networkidle'})
 const bounds=await page.locator('[data-slide]').boundingBox()
 if(bounds.width!==1280||bounds.height!==720)throw Error('Incorrect canvas dimensions')
 if(!(await page.locator('[data-slide]').innerText()).includes('상담교사의'))throw Error('Korean screen missing')
 if(await page.locator('article img').count())throw Error('Reference screenshot embedded in slide')
 if(errors.length)throw Error(errors.join('\n'))
 await page.goto(`${url}/#/board/r11`,{waitUntil:'networkidle'})
 if(await page.locator('[data-reference-board] [data-slide]').count()!==5)throw Error('Financial partial panel missing')
 const report={status:'passed',decks:32,slides:decks.reduce((n,d)=>n+d.slides.length,0),sourceHashesMatchRenders:true,rendererHashesMatch:true,productionGallery:true,productionNavigation:true,referenceComparisonImageLoads:true,koreanSlideRenders:true,financialMissingPanelRestored:true,canvasSize:[1280,720],pageErrors:errors}
 writeFileSync('verification.json',JSON.stringify(report,null,2))
 console.log(JSON.stringify(report,null,2))
}finally{
 await browser.close();await server.close()
 await new Promise(resolve=>production.httpServer.close(resolve))
}
