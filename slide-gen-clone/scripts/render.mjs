import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {mkdir,writeFile,copyFile,readFile} from 'node:fs/promises'
import {execFileSync} from 'node:child_process'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
import {createHash} from 'node:crypto'

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
const rendererHash=createHash('sha256').update((await Promise.all(['src/ui.tsx','src/model.ts','src/index.css','src/App.tsx','src/registry.ts'].map(name=>readFile(path.join(root,name),'utf8')))).join('\n')).digest('hex')
const args=process.argv.slice(2)
const round=args.find(a=>a.startsWith('--round='))?.split('=')[1]??'final'
if(!/^[a-z0-9-]+$/.test(round))throw new Error('Invalid round name')
const requested=args.filter(a=>!a.startsWith('--'))
await mkdir(path.join(root,'renders'),{recursive:true})
await mkdir(path.join(root,'comparisons'),{recursive:true})
await mkdir(path.join(root,'renders',round),{recursive:true})
await mkdir(path.join(root,'comparisons',round),{recursive:true})
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
const url=`http://127.0.0.1:${server.httpServer.address().port}`
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
const results=[]
try {
 const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1})
 const boardPage=await browser.newPage({viewport:{width:1280,height:900},deviceScaleFactor:2})
 const pageErrors=[]
 page.on('pageerror',e=>pageErrors.push(e.message))
 boardPage.on('pageerror',e=>pageErrors.push(e.message))
 await page.goto(url,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const module=await import('/src/registry.ts');return module.decks})
 const selected=decks.filter(d=>!requested.length||requested.includes(d.id))
 if(!selected.length)throw new Error('No matching decks registered')
 const missing=requested.filter(id=>!selected.some(d=>d.id===id))
 if(missing.length)throw new Error(`Missing deck modules: ${missing.join(', ')}`)
 for(const deck of selected){
  if(!deck.referenceSize)throw new Error(`Missing measured reference dimensions: ${deck.id}`)
  if(deck.slides.length!==deck.referenceRegions.length)throw new Error(`Missing source regions: ${deck.id}`)
  const metadata={id:deck.id,title:deck.title,round,rendererHash,definitionHash:createHash('sha256').update(JSON.stringify(deck)).digest('hex'),referenceRegions:deck.referenceRegions,referenceSize:deck.referenceSize,referenceBackground:deck.referenceBackground,boardFile:path.join(root,'renders',`${deck.id}-board.png`),slides:[]}
  for(const slide of deck.slides){
   await page.goto(`${url}/#/slide/${deck.id}/${slide.id}`,{waitUntil:'networkidle'})
   await page.evaluate(()=>document.fonts.ready)
   const canvas=page.locator('[data-slide]')
   await canvas.waitFor()
   const filepath=path.join(root,'renders',`${deck.id}-${slide.id}.png`)
   await canvas.screenshot({path:filepath})
   await copyFile(filepath,path.join(root,'renders',round,`${deck.id}-${slide.id}.png`))
   const findings=await page.evaluate(()=>{
    return [...document.querySelectorAll('.element-text')].flatMap(el=>{
     const range=document.createRange();range.selectNodeContents(el)
     const r=range.getBoundingClientRect(),b=el.getBoundingClientRect()
     const extra={expectedClip:el.dataset.allowClip==='true',clipReason:el.dataset.clipReason}
     return r.right>1281||r.bottom>721||r.left < -1||r.top < -1 ? [{text:el.textContent.slice(0,100),issue:'text outside slide',...extra}] : r.width>b.width+3 ? [{text:el.textContent.slice(0,100),issue:'text wider than its box',...extra}] : []
    })
   })
   metadata.slides.push({id:slide.id,title:slide.title,file:filepath,elementCount:slide.elements.length,findings})
  }
  await boardPage.setViewportSize(deck.referenceSize)
  await boardPage.goto(`${url}/#/board/${deck.id}`,{waitUntil:'networkidle'})
  await boardPage.evaluate(()=>document.fonts.ready)
  await boardPage.locator('[data-reference-board]').screenshot({path:metadata.boardFile})
  await copyFile(metadata.boardFile,path.join(root,'renders',round,`${deck.id}-board.png`))
  if(pageErrors.length)throw new Error(pageErrors.join('\n'))
  await writeFile(path.join(root,'comparisons',`${deck.id}.json`),JSON.stringify(metadata,null,2))
  await writeFile(path.join(root,'comparisons',round,`${deck.id}.json`),JSON.stringify(metadata,null,2))
  execFileSync('python3',[path.join(root,'scripts/compare.py'),deck.id,round],{stdio:'inherit'})
  results.push(metadata)
  console.log(`${deck.id}: ${deck.slides.length} slides rendered, ${metadata.slides.reduce((n,s)=>n+s.findings.length,0)} layout findings`)
 }
 await writeFile(path.join(root,'comparisons',`render-result${requested.length?'-'+requested[0]:''}.json`),JSON.stringify(results,null,2))
}finally{await browser.close();await server.close()}
