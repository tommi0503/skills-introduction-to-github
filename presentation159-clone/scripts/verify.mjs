import {createServer,preview} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile,readdir} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
import {auditSlide} from './browser-audit.mjs'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
process.chdir(root)
const hash=value=>createHash('sha256').update(value).digest('hex')
const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','scripts/browser-audit.mjs']
const rendererHash=hash((await Promise.all(rendererFiles.map(file=>readFile(file,'utf8')))).join('\n'))
const manifest=JSON.parse(await readFile('public/reference/manifest.json','utf8'))
const inventory=JSON.parse(await readFile('provenance/input-inventory.json','utf8'))
const sources=inventory.entries.filter(entry=>entry.kind==='reference-image'&&!entry.duplicatePath)
const expected=manifest.flatMap(deck=>deck.slides.map(slide=>deck.id+'-'+slide.id))
if(manifest.length!==53||expected.length!==159||sources.length!==159||new Set(expected).size!==159)throw Error('Source scope must be exactly53decks/159uniqueimages')
const finalPngs=(await readdir('renders/final')).filter(name=>name.endsWith('.png')).map(name=>name.slice(0,-4)).sort()
if(JSON.stringify(finalPngs)!==JSON.stringify(expected.slice().sort()))throw Error('Final PNG scope mismatch')
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
const production=await preview({root,preview:{host:'127.0.0.1',port:0},logLevel:'error'})
let browser
try{
 browser=await chromium.launch({executablePath:'/usr/bin/chromium'})
 const page=await browser.newPage({viewport:{width:1280,height:720}})
 const errors=[],failedAssets=[],findings=[],fontChecks=[]
 page.on('pageerror',error=>errors.push(error.message))
 page.on('requestfailed',request=>failedAssets.push(request.url()))
 page.on('response',response=>{if(response.status()>=400&&new URL(response.url()).pathname!=='/favicon.ico')failedAssets.push(response.url()+':'+response.status())})
 await page.goto('http://127.0.0.1:'+server.httpServer.address().port,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const module=await import('/src/registry.ts');return module.decks})
 if(decks.length!==53||decks.reduce((sum,deck)=>sum+deck.slides.length,0)!==159)throw Error('Incomplete source data')
 let chips=0,placeholders=0
 for(const original of manifest){
  const deck=decks.find(item=>item.id===original.id)
  if(!deck||JSON.stringify(deck.slides.map(s=>s.id))!==JSON.stringify(original.slides.map(s=>s.id)))throw Error('Source order mismatch '+original.id)
  const meta=JSON.parse(await readFile('comparisons/final/'+deck.id+'.json','utf8'))
  if(meta.definitionHash!==hash(JSON.stringify(deck))||meta.rendererHash!==rendererHash)throw Error('Stale final render '+deck.id)
  if(meta.slides.length!==deck.slides.length)throw Error('Incomplete final capture '+deck.id)
  for(const slide of meta.slides){
   if(slide.pngSha256!==hash(await readFile(slide.file)))throw Error('Final PNG bytes changed')
   if(slide.referenceHash!==hash(await readFile(slide.reference)))throw Error('Reference changed')
   chips+=slide.chipCount;placeholders+=slide.placeholderCount
   findings.push(...slide.findings.map(f=>({...f,deck:deck.id,slide:slide.id,phase:'final capture'})))
  }
 }
 const url='http://127.0.0.1:'+production.httpServer.address().port
 await page.goto(url,{waitUntil:'networkidle'})
 if(await page.locator('.deck-card').count()!==53)throw Error('Production gallery incomplete')
 await page.locator('.deck-card').first().click()
 await page.locator('.deck-board [data-slide]').first().waitFor()
 await page.getByRole('link',{name:'원본 비교'}).click()
 await page.locator('.compare-row img').first().waitFor()
 await page.waitForFunction(()=>[...document.querySelectorAll('.compare-row img')].every(img=>img.complete&&img.naturalWidth===1600&&img.naturalHeight===900))
 const productionPages=[]
 for(const deck of decks){
  for(const slide of deck.slides){
   await page.goto(url+'/#/slide/'+deck.id+'/'+slide.id,{waitUntil:'networkidle'})
   await page.locator('[data-deck="'+deck.id+'"] [data-slide="'+slide.id+'"]').waitFor()
   const audit=await auditSlide(page)
   productionPages.push({deck:deck.id,slide:slide.id,size:audit.size,issues:audit.issues})
   findings.push(...audit.issues.map(f=>({...f,deck:deck.id,slide:slide.id,phase:'production'})))
   fontChecks.push(...audit.fontChecks)
  }
 }
 const unexpected=findings.filter(f=>!f.expectedClip)
 const undocumented=findings.filter(f=>f.expectedClip&&!f.clipReason)
 const report={status:unexpected.length||undocumented.length||errors.length||failedAssets.length?'failed':'passed',
  decks:53,slides:159,canvas:[1280,720],sourceImages:159,sourceBytesPreserved:true,
  latestDefinitionHashesMatch:true,latestSharedRendererHash:rendererHash,
  pngHashesMatch:true,productionGallery:true,productionComparisonNavigation:true,
  productionPagesValidated:productionPages.length,chipCount:chips,placeholderCount:placeholders,
  unexpectedFindings:unexpected,expectedClipping:findings.filter(f=>f.expectedClip),pageErrors:errors,
  failedAssets,fontChecks,productionPages,checkedAt:new Date().toISOString()}
 await writeFile('review/verification.json',JSON.stringify(report,null,2)+'\n')
 console.log(JSON.stringify({...report,fontChecks:fontChecks.length,productionPages:productionPages.length},null,2))
 if(report.status!=='passed')throw Error('Required verification failed; see review/verification.json')
}finally{
 if(browser)await browser.close()
 await server.close()
 await new Promise(resolve=>production.httpServer.close(resolve))
}

