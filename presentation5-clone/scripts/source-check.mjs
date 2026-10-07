import {preview} from 'vite'
import {chromium} from 'playwright-core'
import * as Icons from 'lucide-react'
import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {buildState} from './build-state.mjs'
import {validateDefinitions} from './validate-definitions.mjs'
import {auditSlide} from './audit.mjs'
const stamp=JSON.parse(await readFile('dist/build-state.json','utf8'))
const current=await buildState()
if(!stamp.sourceStableDuringBuild||stamp.sourceHash!==current.sourceHash)throw Error('Build is stale')
const server=await preview({preview:{host:'127.0.0.1',port:0},logLevel:'error'})
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage({viewport:{width:1440,height:900}}),errors=[],failures=[],findings=[]
 page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>failures.push(r.url()))
 page.on('response',r=>{if(r.status()>=400)failures.push(`${r.status()} ${r.url()}`)})
 const base=`http://127.0.0.1:${server.httpServer.address().port}`
 await page.goto(base);await page.waitForFunction(()=>Array.isArray(window.__presentationDecks))
 const decks=await page.evaluate(()=>window.__presentationDecks)
 validateDefinitions(decks,await page.evaluate(()=>window.__presentationGraphics))
 if(decks.length!==47||decks.reduce((n,d)=>n+d.slides.length,0)!==1057)throw Error('Missing pages')
 if(await page.locator('.deck-card').count()!==47)throw Error('Missing gallery links')
 await page.locator('.deck-card').first().click();await page.locator('.deck-board [data-slide]').first().waitFor()
 let count=0,chipCount=0
 for(const deck of decks)for(const slide of deck.slides){
  if(slide.elements.some(e=>e.kind==='icon'&&!(e.icon in Icons)))throw Error('Unavailable icon')
  await page.goto(`${base}/#/slide/${deck.id}/${slide.id}`,{waitUntil:'load'})
  await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
  if(await page.locator('img,svg image').count())throw Error('Image requested by source-only UI')
  const audit=await auditSlide(page)
  if(audit.canvas[0]!==1280||audit.canvas[1]!==720||audit.fontStatus!=='loaded'||!audit.placeholderRule)throw Error(`Layout/assets failed: ${deck.id}/${slide.id}`)
  findings.push(...audit.findings.map(f=>({...f,deck:deck.id,slide:slide.id})))
  chipCount+=slide.elements.filter(e=>e.kind==='chip'&&e.text).length;count++
  if(count%100===0)console.log(`Audited ${count}/1057 pages`)
 }
 if(findings.some(f=>!f.expectedClip)||errors.length||failures.length)throw Error(JSON.stringify({findings:findings.filter(f=>!f.expectedClip),errors,failures}))
 const report={status:'passed',decks:47,slides:count,pageSize:[1280,720],productionSourceHash:stamp.sourceHash,sourceStableDuringBuild:true,imageElementsRequested:0,chipCount,unexpectedLayoutFindings:0,expectedSourceCrops:findings,pageErrors:errors,failedRequests:failures}
 await mkdir('review',{recursive:true});await writeFile('review/source-only-verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2))
}finally{await browser.close();await new Promise(resolve=>server.httpServer.close(resolve))}
