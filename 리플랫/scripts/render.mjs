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
 page.on('requestfailed',r=>{if(/\.woff2?(?:\?|$)/.test(r.url()))fontErrors.push(r.url())})
 page.on('response',r=>{if(r.status()>=400&&/\.woff2?(?:\?|$)/.test(r.url()))fontErrors.push(r.url())})
 await page.goto(url,{waitUntil:'networkidle'})
 const brochures=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.brochures})
 const selected=brochures.filter(d=>!ids.length||ids.includes(d.id))
 if(!selected.length||ids.some(id=>!selected.some(d=>d.id===id)))throw Error('Requested brochure missing')
 for(const brochure of selected){
  if(brochure.panels.length!==6||brochure.sides.length!==2)throw Error('Incomplete brochure')
  const meta={id:brochure.id,title:brochure.title,round,definitionHash:hash(JSON.stringify(brochure)),rendererHash,panels:[],sides:[],notes:brochure.sides.flatMap(s=>s.notes)}
  for(const [mode,pages] of [['page',brochure.panels],['side',brochure.sides]])for(const sheet of pages){
   await page.goto(`${url}/#/${mode}/${brochure.id}/${sheet.id}`,{waitUntil:'networkidle'})
   const article=page.locator(`[data-brochure="${brochure.id}"] [data-page="${sheet.id}"]`);await article.waitFor()
   await article.getAttribute('data-fonts-ready');await page.waitForFunction(()=>document.querySelector('[data-page]')?.dataset.fontsReady==='true')
   await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
   const b=await article.boundingBox();if(b.width!==1280||b.height!==720)throw Error('Canvas dimensions changed')
   if(fontErrors.length)throw Error(`Font loading failed: ${fontErrors.length}`)
   if(await article.locator('img').count())throw Error('Source image embedded in UI')
   const findings=await article.evaluate((article,elements)=>{
    const result=[],paper=article.querySelector('[data-paper]'),paperBounds=paper.getBoundingClientRect(),scale=paperBounds.height/parseFloat(getComputedStyle(paper).height)
    const ctx=document.createElement('canvas').getContext('2d')
    const declaredText=elements.filter(e=>e.kind==='text')
    for(const [i,el] of [...paper.querySelectorAll('.element-text')].entries()){
     const b=el.getBoundingClientRect(),s=getComputedStyle(el),range=document.createRange();range.selectNodeContents(el);const r=range.getBoundingClientRect()
     const record={text:el.textContent.slice(0,100),elementId:el.dataset.elementId}
     ctx.font=`${s.fontStyle} ${s.fontWeight} ${s.fontSize} ${s.fontFamily}`;ctx.letterSpacing=s.letterSpacing==='normal'?'0px':s.letterSpacing
     const bottomMetrics=ctx.measureText(el.textContent.split('\n').at(-1))
     // An ink-fitted title uses the visible glyph bounds, while a DOM Range includes side bearings.
     const width=el.style.transform.startsWith('scaleX(')&&!el.textContent.includes('\n')
      ?r.width*(bottomMetrics.actualBoundingBoxLeft+bottomMetrics.actualBoundingBoxRight)/Math.max(1,bottomMetrics.width):r.width
     if(width>b.width+3*scale)result.push({...record,issue:'text wider than box',excess:(width-b.width)/scale})
     const paintedBottom=r.bottom-(bottomMetrics.fontBoundingBoxDescent-bottomMetrics.actualBoundingBoxDescent)*scale
     const intendedBottom=declaredText[i]?.inkFit?paperBounds.y+(declaredText[i].y+declaredText[i].h)*scale:b.bottom
     if(paintedBottom>intendedBottom+3*scale)result.push({...record,issue:'text taller than box',excess:(paintedBottom-intendedBottom)/scale})
     if(el.dataset.chip==='true'){
      const label=el.querySelector('[data-chip-label]'),l=label.getBoundingClientRect()
      ctx.font=`${s.fontStyle} ${s.fontWeight} ${s.fontSize} ${s.fontFamily}`;ctx.letterSpacing=s.letterSpacing==='normal'?'0px':s.letterSpacing
      const m=ctx.measureText(el.textContent.split('\n').sort((a,b)=>b.length-a.length)[0])
      const x=l.x+l.width/2+(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2*scale-(b.x+b.width/2)
      const y=l.y+l.height/2+(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2*scale-(b.y+b.height/2)
      if(Math.abs(x)>1.2||Math.abs(y)>1.2)result.push({...record,issue:'chip ink not centered',offset:[x,y]})
      if(l.width>b.width+scale||l.height>b.height+scale)result.push({...record,issue:'chip label exceeds bounds'})
     }
    }
    return result
   },sheet.elements)
   const file=path.join(root,'renders',round,`${brochure.id}-${sheet.id}.png`);await article.screenshot({path:file})
   const record={id:sheet.id,title:sheet.title??sheet.id,file,reference:path.join(root,'public',sheet.reference),size:sheet.size,crop:sheet.crop,findings,elementCount:sheet.elements.length,chipCount:sheet.elements.filter(e=>e.chip).length,replacementCount:sheet.elements.filter(e=>e.replacement).length}
   meta[mode==='page'?'panels':'sides'].push(record)
  }
  if(errors.length)throw Error(errors.join('\n'))
  await writeFile(path.join(root,'comparisons',round,`${brochure.id}.json`),JSON.stringify(meta,null,2))
  execFileSync('python3',[path.join(root,'scripts/compare.py'),brochure.id,round],{stdio:'inherit'})
  console.log(`${brochure.id}: 6 panels / 2 unfolded sheets / ${meta.panels.reduce((n,p)=>n+p.findings.length,0)} findings`)
 }
}finally{await browser.close();await server.close()}
