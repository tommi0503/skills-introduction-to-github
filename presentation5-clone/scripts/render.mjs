import {loadManifest} from './manifest.mjs'
import {auditSlide} from './audit.mjs'
import {validateDefinitions} from './validate-definitions.mjs'
import {buildState,rendererHashFor} from './build-state.mjs'
import {createServer,preview} from 'vite'
import {chromium} from 'playwright-core'
import {mkdir,readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {execFileSync} from 'node:child_process'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
const args=process.argv.slice(2),round=args.find(a=>a.startsWith('--round='))?.slice(8)??'final',ids=args.filter(a=>!a.startsWith('--'))
if(!/^[a-z0-9-]+$/.test(round))throw Error('Invalid round')
const hash=s=>createHash('sha256').update(s).digest('hex')
const rendererHash=await rendererHashFor(root)
await mkdir(path.join(root,'renders',round),{recursive:true});await mkdir(path.join(root,'comparisons',round),{recursive:true})
const production=args.includes('--production')
let productionSourceHash
if(production){
 const stamp=JSON.parse(await readFile(path.join(root,'dist/build-state.json'),'utf8'))
 const current=await buildState()
 if(!stamp.sourceStableDuringBuild||!stamp.rendererStableDuringBuild||stamp.rendererHash!==rendererHash||stamp.sourceHash!==current.sourceHash)throw Error('Production build differs from current source/dependencies; rebuild first')
 productionSourceHash=current.sourceHash
}
const server=production?await preview({root,preview:{host:'127.0.0.1',port:0},logLevel:'error'}):await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'})
if(!production)await server.listen()
const url=`http://127.0.0.1:${server.httpServer.address().port}`
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage({viewport:{width:1280,height:720}}),errors=[],fontErrors=[]
 page.on('pageerror',e=>errors.push(e.message))
 page.on('console',message=>{if(message.type()==='error'&&/attribute .*Expected|attribute .*Unexpected|attribute .*invalid|<path> attribute d/i.test(message.text()))errors.push(message.text())})
 page.on('requestfailed',request=>{if(/\.woff2?(?:\?|$)/.test(request.url()))fontErrors.push(request.url())})
 page.on('response',response=>{if(response.status()>=400&&/\.woff2?(?:\?|$)/.test(response.url()))fontErrors.push(response.url())})
 await page.goto(url,{waitUntil:'load'})
 await page.waitForFunction(()=>Array.isArray(window.__presentationDecks))
 const decks=await page.evaluate(()=>window.__presentationDecks)
 const source=await loadManifest(root)
 const selected=decks.filter(d=>!ids.length||ids.includes(d.id))
 validateDefinitions(selected,await page.evaluate(()=>window.__presentationGraphics))
 if(!selected.length||ids.some(id=>!selected.some(d=>d.id===id)))throw Error('Requested deck not implemented')
 for(const deck of selected){
  const original=source.find(d=>d.id===deck.id)
  if(deck.slides.length!==original.slides.length)throw Error(`Incomplete ${deck.id}: ${deck.slides.length}/${original.slides.length}`)
  const meta={id:deck.id,title:deck.title,round,production,productionSourceHash,definitionHash:hash(JSON.stringify(deck)),rendererHash,slides:[]}
  for(let index=0;index<deck.slides.length;index++){
   const slide=deck.slides[index]
   if(slide.id!==original.slides[index].id)throw Error(`Source order mismatch ${deck.id}/${slide.id}`)
   await page.goto(`${url}/#/slide/${deck.id}/${slide.id}`,{waitUntil:'load'})
   const article=page.locator(`[data-deck="${deck.id}"] [data-slide="${slide.id}"]`)
   await article.waitFor()
   await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
   if(fontErrors.length)throw Error(`Font assets failed to load: ${fontErrors.length}`)
   const bounds=await article.boundingBox()
   if(bounds.width!==1280||bounds.height!==720)throw Error('Canvas dimensions changed')
   if(await article.locator('img').count())throw Error('Source screenshot embedded')
   const audit=await auditSlide(page)
   const findings=audit.findings
   const file=path.join(root,'renders',round,`${deck.id}-${slide.id}.png`)
   await article.screenshot({path:file})
   meta.slides.push({pngSha256:hash(await readFile(file)),id:slide.id,title:slide.title,file,reference:path.join(root,'public',deck.references[index]),elementCount:slide.elements.length,chipCount:slide.elements.filter(e=>e.kind==='chip').length,...audit,findings})
  }
  if(errors.length)throw Error(errors.join('\n'))
  if(production&&(await buildState()).sourceHash!==productionSourceHash)throw Error('Source changed during production capture; keep it frozen and recapture')
  await writeFile(path.join(root,'comparisons',round,`${deck.id}.json`),JSON.stringify(meta,null,2))
  execFileSync('python3',[path.join(root,'scripts/compare.py'),deck.id,round],{stdio:'inherit'})
  console.log(`${deck.id}: ${meta.slides.length} slides / ${meta.slides.reduce((n,s)=>n+s.findings.length,0)} findings`)
 }
}finally{await browser.close();if(production)await new Promise(r=>server.httpServer.close(r));else await server.close()}
