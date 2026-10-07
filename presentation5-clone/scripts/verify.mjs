import {loadManifest} from './manifest.mjs'
import * as Icons from 'lucide-react'
import {preview} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile,readdir} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {auditSlide} from './audit.mjs'
import {validateDefinitions} from './validate-definitions.mjs'
import {buildState,rendererHashFor} from './build-state.mjs'
const hash=s=>createHash('sha256').update(s).digest('hex')
const rendererHash=await rendererHashFor()
const stamp=JSON.parse(await readFile('dist/build-state.json','utf8'))
const current=await buildState()
if(!stamp.sourceStableDuringBuild||!stamp.rendererStableDuringBuild||stamp.sourceHash!==current.sourceHash||stamp.rendererHash!==rendererHash)throw Error('Production build does not match the final source/dependencies; rebuild after all edits finish')
const buildHistory=JSON.parse(await readFile('review/quality/production-builds.json','utf8')).builds
const frozenProductionBuilds=new Set(buildHistory.filter(b=>b.sourceStableDuringBuild&&b.rendererStableDuringBuild&&b.rendererHash===rendererHash).map(b=>b.sourceHash))
if(!frozenProductionBuilds.has(stamp.sourceHash))throw Error('Current production build is missing its stable capture provenance')
const manifest=await loadManifest(process.cwd())
const expectedCount=manifest.reduce((n,d)=>n+d.slides.length,0)
const pngs=(await readdir('renders/final')).filter(n=>n.endsWith('.png'))
if(pngs.length!==expectedCount||manifest.length!==47||expectedCount!==1057)throw Error('Incomplete split-slide inventory')
const server=await preview({preview:{host:'127.0.0.1',port:0},logLevel:'error'})
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try {
 const page=await browser.newPage({viewport:{width:1440,height:900}}),errors=[],badRequests=[]
 page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>badRequests.push(r.url()))
 page.on('console',message=>{if(message.type()==='error'&&/attribute .*Expected|attribute .*Unexpected|attribute .*invalid|<path> attribute d/i.test(message.text()))errors.push(message.text())})
 page.on('response',r=>{if(r.status()>=400)badRequests.push(`${r.status()} ${r.url()}`)})
 const url=`http://127.0.0.1:${server.httpServer.address().port}`
 await page.goto(url,{waitUntil:'load'})
 await page.waitForFunction(()=>Array.isArray(window.__presentationDecks))
 const decks=await page.evaluate(()=>window.__presentationDecks)
 validateDefinitions(decks,await page.evaluate(()=>window.__presentationGraphics))
 if(decks.length!==manifest.length)throw Error('Incomplete production gallery')
 const missingIcons=[...new Set(decks.flatMap(d=>d.slides.flatMap(s=>s.elements.filter(e=>e.kind==='icon'&&!(e.icon in Icons)).map(e=>e.icon))))]
 if(missingIcons.length)throw Error(`Unavailable Lucide icons: ${missingIcons.join(',')}`)
 if(await page.locator('.deck-card').count()!==manifest.length)throw Error('Production gallery card mismatch')
 await page.locator('.deck-card').first().click();await page.locator('.deck-board [data-slide]').first().waitFor()
 await page.getByRole('link',{name:'원본 비교'}).click();await page.locator('.compare-row img').first().waitFor()
 await page.waitForFunction(()=>[...document.querySelectorAll('.compare-row img')].every(img=>img.complete&&img.naturalWidth>0))
 let findings=[],chips=0,fontUsage=[],verified=0,vectorScenes=0,typographyWidthApproximations=[]
 for(const original of manifest){
  const deck=decks.find(d=>d.id===original.id)
  if(!deck||JSON.stringify(deck.slides.map(s=>s.id))!==JSON.stringify(original.slides.map(s=>s.id)))throw Error(`Missing/incorrect order ${original.id}`)
  if(deck.slides.some(s=>s.sourceAspect||s.elements.some(e=>e.kind!=='text'&&e.scaleX&&e.scaleX!==1)))throw Error(`Distorted canvas/reference/non-text proportions in ${deck.id}`)
  // The user prohibits changing the stage or reference aspect ratio. Some
  // individually reviewed text elements approximate an unavailable typeface's
  // glyph width. Keep these explicit, rather than claiming exact font identity.
  for(const slide of deck.slides)for(const element of slide.elements){
   if(element.kind==='text'&&element.scaleX&&element.scaleX!==1){
    if(!Number.isFinite(element.scaleX)||element.scaleX<=0)throw Error('Invalid glyph width adjustment')
    typographyWidthApproximations.push({deck:deck.id,slide:slide.id,text:element.text,font:element.font,scaleX:element.scaleX})
   }
  }
  const meta=JSON.parse(await readFile(`comparisons/final/${deck.id}.json`,'utf8'))
  if(meta.production!==true)throw Error(`Final capture was not produced from production build ${deck.id}`)
  if(!frozenProductionBuilds.has(meta.productionSourceHash))throw Error(`Unrecorded or unstable production capture build ${deck.id}`)
  if(hash(JSON.stringify(deck))!==meta.definitionHash||rendererHash!==meta.rendererHash)throw Error(`Stale final output ${deck.id}`)
  for(let i=0;i<deck.slides.length;i++){
   const slide=deck.slides[i],capture=meta.slides[i]
   const png=await readFile(`renders/final/${deck.id}-${slide.id}.png`)
   if(hash(png)!==capture.pngSha256)throw Error(`Final PNG hash mismatch ${deck.id}/${slide.id}`)
   if(png.readUInt32BE(16)!==1280||png.readUInt32BE(20)!==720)throw Error('Incorrect PNG dimensions')
   if(!(await readFile(`comparisons/final/${deck.id}-${slide.id}.jpg`)).length)throw Error('Missing comparison')
   await page.goto(`${url}/#/slide/${deck.id}/${slide.id}`,{waitUntil:'load'})
   await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
   const stageGeometry=await page.locator('.slide-canvas').evaluate(el=>{
    const style=getComputedStyle(el),box=el.getBoundingClientRect()
    return {width:box.width,height:box.height,transform:style.transform,rotate:style.rotate,scale:style.scale,zoom:style.zoom}
   })
   if(stageGeometry.width!==1280||stageGeometry.height!==720||stageGeometry.transform!=='none'||stageGeometry.rotate!=='none'||stageGeometry.scale!=='none'||Number(stageGeometry.zoom)!==1)throw Error(`Transformed stage ${deck.id}/${slide.id}: ${JSON.stringify(stageGeometry)}`)
   const audit=await auditSlide(page)
   if(audit.canvas[0]!==1280||audit.canvas[1]!==720||audit.embeddedImages||!audit.placeholderRule||audit.fontStatus!=='loaded')throw Error(`Canvas/assets validation failed ${deck.id}/${slide.id}`)
   findings.push(...audit.findings.map(f=>({...f,deck:deck.id,slide:slide.id})))
   fontUsage.push(...audit.fontUsage);chips+=slide.elements.filter(e=>e.kind==='chip'&&e.text).length;vectorScenes+=audit.vectorScenes;verified++
  }
 }
 const unexpected=findings.filter(f=>!f.expectedClip)
 if(unexpected.length)throw Error(`Unresolved layout findings: ${JSON.stringify(unexpected)}`)
 if(errors.length||badRequests.length)throw Error(JSON.stringify({errors,badRequests}))
 const report={status:'passed',decks:manifest.length,slides:verified,canvas:[1280,720],sourceDataHashesMatch:true,sharedRendererHashesMatch:true,pngHashesMatch:true,productionGallery:true,productionNavigation:true,allProductionSlidesAudited:true,referenceImagesLoad:true,fonts:[...new Map(fontUsage.map(f=>[`${f.family}/${f.weight}/${f.style}`,f])).values()],chipCount:chips,chipCenterIssues:findings.filter(f=>f.issue==='chip ink not centered').length,placeholderRule:true,noEmbeddedSourceScreenshots:true,noCanvasOrReferenceAspectDistortion:true,noStageRotationOrScaling:true,allLucideIconsAvailable:true,pageErrors:errors,failedRequests:badRequests,layoutFindings:findings,typographyWidthApproximations}
 report.vectorSceneInstances=vectorScenes;report.allVectorSceneNamesRegistered=true;report.noRasterContentInVectorScenes=true
 report.frozenProductionBuilds=[...frozenProductionBuilds];report.allFinalDeckDefinitionsMatchCurrentSource=true
 await writeFile('review/verification.json',JSON.stringify(report,null,2));console.log(JSON.stringify({...report,fonts:report.fonts.length,layoutFindings:findings.length},null,2))
}finally {await browser.close();await new Promise(r=>server.httpServer.close(r))}
