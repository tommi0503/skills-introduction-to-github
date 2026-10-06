import {createServer} from 'vite'
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
const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts']
const rendererHash=hash((await Promise.all(rendererFiles.map(f=>readFile(path.join(root,f),'utf8')))).join('\n'))
await mkdir(path.join(root,'renders',round),{recursive:true});await mkdir(path.join(root,'comparisons',round),{recursive:true})
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const url=`http://127.0.0.1:${server.httpServer.address().port}`
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage({viewport:{width:1280,height:720}}),errors=[],fontErrors=[]
 page.on('pageerror',e=>errors.push(e.message))
 page.on('requestfailed',request=>{if(/\.woff2?(?:\?|$)/.test(request.url()))fontErrors.push(request.url())})
 page.on('response',response=>{if(response.status()>=400&&/\.woff2?(?:\?|$)/.test(response.url()))fontErrors.push(response.url())})
 await page.goto(url,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.decks})
 const source=JSON.parse(await readFile(path.join(root,'public/reference/manifest.json'),'utf8'))
 const selected=decks.filter(d=>!ids.length||ids.includes(d.id))
 if(!selected.length||ids.some(id=>!selected.some(d=>d.id===id)))throw Error('Requested deck not implemented')
 for(const deck of selected){
  const original=source.find(d=>d.id===deck.id)
  if(deck.slides.length!==original.slides.length)throw Error(`Incomplete ${deck.id}: ${deck.slides.length}/${original.slides.length}`)
  const meta={id:deck.id,title:deck.title,round,definitionHash:hash(JSON.stringify(deck)),rendererHash,slides:[]}
  for(let index=0;index<deck.slides.length;index++){
   const slide=deck.slides[index]
   if(slide.id!==original.slides[index].id)throw Error(`Source order mismatch ${deck.id}/${slide.id}`)
   await page.goto(`${url}/#/slide/${deck.id}/${slide.id}`,{waitUntil:'networkidle'})
   const article=page.locator(`[data-deck="${deck.id}"] [data-slide="${slide.id}"]`)
   await article.waitFor()
   await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
   if(fontErrors.length)throw Error(`Font assets failed to load: ${fontErrors.length}`)
   const bounds=await article.boundingBox()
   if(bounds.width!==1280||bounds.height!==720)throw Error('Canvas dimensions changed')
   if(await article.locator('img').count())throw Error('Source screenshot embedded')
   const findings=await page.evaluate(()=>{
    const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d')
    const result=[]
    for(const el of document.querySelectorAll('.element-text,.element-chip')){
     const b=el.getBoundingClientRect(),style=getComputedStyle(el),range=document.createRange();range.selectNodeContents(el);const r=range.getBoundingClientRect()
     const record={text:el.textContent.slice(0,120),expectedClip:el.dataset.allowClip==='true',clipReason:el.dataset.clipReason}
     if(r.right>1281||r.bottom>721||r.left< -1||r.top< -1)result.push({...record,issue:'text outside slide'})
     else if(!style.transform.includes('matrix(0')&&r.width>b.width+3)result.push({...record,issue:'text wider than box'})
     if(el.classList.contains('element-chip')&&style.justifyContent==='center'){
      const label=el.querySelector('[data-chip-label]'),l=label.getBoundingClientRect()
      ctx.font=`${style.fontStyle} ${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;ctx.letterSpacing=style.letterSpacing
      const m=ctx.measureText(el.textContent)
      const dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2
      const dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2
      const x=l.x+l.width/2+dx-(b.x+b.width/2),y=l.y+l.height/2+dy-(b.y+b.height/2)
      if(Math.abs(x)>1.2||Math.abs(y)>1.2)result.push({...record,issue:'chip ink not centered',offset:[x,y]})
      if(l.width>b.width+1||l.height>b.height+1)result.push({...record,issue:'chip label exceeds bounds'})
     }
    }
    return result
   })
   const file=path.join(root,'renders',round,`${deck.id}-${slide.id}.png`)
   await article.screenshot({path:file})
   meta.slides.push({id:slide.id,title:slide.title,file,reference:path.join(root,'public',deck.references[index]),elementCount:slide.elements.length,chipCount:slide.elements.filter(e=>e.kind==='chip').length,findings})
  }
  if(errors.length)throw Error(errors.join('\n'))
  await writeFile(path.join(root,'comparisons',round,`${deck.id}.json`),JSON.stringify(meta,null,2))
  execFileSync('python3',[path.join(root,'scripts/compare.py'),deck.id,round],{stdio:'inherit'})
  console.log(`${deck.id}: ${meta.slides.length} slides / ${meta.slides.reduce((n,s)=>n+s.findings.length,0)} findings`)
 }
}finally{await browser.close();await server.close()}
