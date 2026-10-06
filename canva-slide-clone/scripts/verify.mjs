import {createServer,preview} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
const hash=s=>createHash('sha256').update(s).digest('hex')
const files=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts']
const rendererHash=hash((await Promise.all(files.map(f=>readFile(f,'utf8')))).join('\n'))
const manifest=JSON.parse(await readFile('public/reference/manifest.json','utf8'))
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const production=await preview({preview:{host:'127.0.0.1',port:0}})
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage({viewport:{width:1440,height:900}}),errors=[]
 page.on('pageerror',e=>errors.push(e.message))
 await page.goto(`http://127.0.0.1:${server.httpServer.address().port}`,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.decks})
 if(decks.length!==17||decks.reduce((n,d)=>n+d.slides.length,0)!==190)throw Error('Missing templates or pages')
 let chips=0,findings=[]
 for(const original of manifest){
  const deck=decks.find(d=>d.id===original.id)
  if(!deck||deck.slides.length!==original.slides.length)throw Error(`Missing source pages ${original.id}`)
  const meta=JSON.parse(await readFile(`comparisons/final/${deck.id}.json`,'utf8'))
  if(hash(JSON.stringify(deck))!==meta.definitionHash||rendererHash!==meta.rendererHash)throw Error(`Stale final output ${deck.id}`)
  if(meta.slides.length!==deck.slides.length)throw Error('Missing captured slides')
  for(const slide of meta.slides){chips+=slide.chipCount;findings.push(...slide.findings.map(f=>({...f,deck:deck.id,slide:slide.id})))}
 }
 const unexpected=findings.filter(f=>!f.expectedClip)
 if(unexpected.length)throw Error(`Unresolved layout findings: ${JSON.stringify(unexpected)}`)
 const url=`http://127.0.0.1:${production.httpServer.address().port}`
 await page.goto(url,{waitUntil:'networkidle'})
 if(await page.locator('.deck-card').count()!==17)throw Error('Incomplete production gallery')
 await page.locator('.deck-card').first().click();await page.locator('.deck-board [data-slide]').first().waitFor()
 await page.getByRole('link',{name:'원본 비교'}).click();await page.locator('.compare-row img').first().waitFor()
 await page.waitForFunction(()=>[...document.querySelectorAll('.compare-row img')].every(img=>img.complete&&img.naturalWidth===1600))
 await page.goto(`${url}/#/slide/c01/s04`,{waitUntil:'networkidle'})
 await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
 const bounds=await page.locator('[data-slide]').boundingBox()
 if(bounds.width!==1280||bounds.height!==720)throw Error('Uniform canvas changed')
 if(!(await page.locator('[data-slide]').innerText()).includes('좋아'))throw Error('Korean slide missing')
 if(!(await page.locator('[data-chip-label]').count()))throw Error('Reusable centered chips not rendered')
 if(await page.locator('article img').count())throw Error('Reference screenshot embedded')
 const realWeights=await page.evaluate(async()=>{
  const normal=await document.fonts.load('400 24px "Noto Sans KR"','한글')
  const bold=await document.fonts.load('700 24px "Noto Sans KR"','한글')
  return normal.some(f=>f.status==='loaded'&&f.weight==='400')&&bold.some(f=>f.status==='loaded'&&f.weight==='700')
 })
 if(!realWeights)throw Error('Actual Korean normal and bold font files missing')
 const placeholders=await page.locator('.element-image').evaluateAll(els=>els.every(el=>getComputedStyle(el).backgroundColor==='rgb(229, 229, 229)'))
 if(!placeholders)throw Error('Placeholder rule changed')
 if(errors.length)throw Error(errors.join('\n'))
 const report={status:'passed',templates:17,slides:190,canvas:[1280,720],sourceDataHashesMatch:true,sharedRendererHashesMatch:true,productionGallery:true,productionNavigation:true,referenceImagesLoad:true,koreanSlideRenders:true,actualKoreanNormalAndBoldFiles:true,sharedChipsRender:true,chipCount:chips,chipCenterIssues:findings.filter(f=>f.issue==='chip ink not centered').length,placeholderRule:true,noEmbeddedSourceScreenshots:true,pageErrors:errors,layoutFindings:findings}
 await writeFile('review/verification.json',JSON.stringify(report,null,2));console.log(JSON.stringify({...report,layoutFindings:findings.length},null,2))
}finally{await browser.close();await server.close();await new Promise(r=>production.httpServer.close(r))}
