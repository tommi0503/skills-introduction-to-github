import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {mkdir,readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {execFileSync} from 'node:child_process'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
import {auditSlide} from './browser-audit.mjs'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
const args=process.argv.slice(2),round=args.find(a=>a.startsWith('--round='))?.slice(8)??'final',ids=args.filter(a=>!a.startsWith('--'))
if(!/^[a-z0-9-]+$/.test(round))throw Error('Invalid round')
const hash=value=>createHash('sha256').update(value).digest('hex')
const rendererFiles=['src/ui.tsx','src/graphics.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','scripts/browser-audit.mjs']
const rendererHash=hash((await Promise.all(rendererFiles.map(file=>readFile(path.join(root,file),'utf8')))).join('\n'))
await mkdir(path.join(root,'renders',round),{recursive:true})
await mkdir(path.join(root,'comparisons',round),{recursive:true})
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
const url='http://127.0.0.1:'+server.httpServer.address().port
let browser
try{
 browser=await chromium.launch({executablePath:'/usr/bin/chromium'})
 const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1})
 const errors=[],fontErrors=[]
 page.on('pageerror',error=>errors.push(error.message))
 page.on('requestfailed',request=>{if(/\.woff2?(?:\?|$)/.test(request.url()))fontErrors.push(request.url())})
 page.on('response',response=>{if(response.status()>=400&&/\.woff2?(?:\?|$)/.test(response.url()))fontErrors.push(response.url())})
 await page.goto(url,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const module=await import('/src/registry.ts');return module.decks})
 const source=JSON.parse(await readFile(path.join(root,'public/reference/manifest.json'),'utf8'))
 const selected=decks.filter(deck=>!ids.length||ids.includes(deck.id))
 if(!selected.length||ids.some(id=>!selected.some(deck=>deck.id===id)))throw Error('Requested deck not implemented')
 for(const deck of selected){
  const original=source.find(item=>item.id===deck.id)
  if(!original||deck.slides.length!==original.slides.length)throw Error('Incomplete deck '+deck.id)
  const meta={id:deck.id,title:deck.title,round,definitionHash:hash(JSON.stringify(deck)),rendererHash,
   capturedAt:new Date().toISOString(),slides:[]}
  for(let index=0;index<deck.slides.length;index++){
   const slide=deck.slides[index]
   if(slide.id!==original.slides[index].id)throw Error('Source order mismatch '+deck.id+'/'+slide.id)
   await page.goto(url+'/#/slide/'+deck.id+'/'+slide.id,{waitUntil:'networkidle'})
   const article=page.locator('[data-deck="'+deck.id+'"] [data-slide="'+slide.id+'"]')
   await article.waitFor()
   const audit=await auditSlide(page)
   if(fontErrors.length)throw Error('Font assets failed: '+fontErrors.join(', '))
   if(audit.size[0]!==1280||audit.size[1]!==720)throw Error('Canvas dimensions changed')
   const file='renders/'+round+'/'+deck.id+'-'+slide.id+'.png'
   await article.screenshot({path:path.join(root,file)})
   const reference='public'+deck.references[index]
   const referenceHash=hash(await readFile(path.join(root,reference)))
   if(referenceHash!==original.slides[index].sha256)throw Error('Reference bytes changed')
   meta.slides.push({id:slide.id,title:slide.title,file,reference,referenceHash,
    pngSha256:hash(await readFile(path.join(root,file))),elementCount:slide.elements.length,
    chipCount:audit.chipCount,placeholderCount:audit.placeholderCount,graphicCount:audit.graphicCount,gradientCount:audit.gradientCount,fadeMaskCount:audit.fadeMaskCount,fontChecks:audit.fontChecks,findings:audit.issues})
  }
  if(errors.length)throw Error(errors.join('\n'))
  await writeFile(path.join(root,'comparisons',round,deck.id+'.json'),JSON.stringify(meta,null,2)+'\n')
  execFileSync('python3',[path.join(root,'scripts/compare.py'),deck.id,round],{stdio:'inherit'})
  console.log(deck.id+': '+meta.slides.length+' slides / '+meta.slides.reduce((count,slide)=>count+slide.findings.filter(f=>!f.expectedClip).length,0)+' findings')
 }
}finally{
 if(browser)await browser.close()
 await server.close()
}
