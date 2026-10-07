import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {mkdir,readFile,writeFile,readdir} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
const args=process.argv.slice(2),round=args.find(a=>a.startsWith('--round='))?.slice(8)??'final',ids=args.filter(a=>!a.startsWith('--'))
if(!/^[a-z0-9-]+$/.test(round))throw Error('Invalid round')
const hash=s=>createHash('sha256').update(s).digest('hex')
const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','src/fonts.ts']
const rendererHash=hash((await Promise.all(rendererFiles.map(f=>readFile(path.join(root,f),'utf8')))).join('\n'))
const files=[...rendererFiles,...(await readdir(path.join(root,'src/data'))).filter(f=>f.endsWith('.ts')).map(f=>`src/data/${f}`)]
const sourceHash=hash((await Promise.all(files.map(f=>readFile(path.join(root,f),'utf8')))).join('\n'))
await mkdir(path.join(root,'renders',round),{recursive:true});await mkdir(path.join(root,'comparisons',`round-${round}`),{recursive:true})
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const url=`http://127.0.0.1:${server.httpServer.address().port}`
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']})
try{
 const page=await browser.newPage({viewport:{width:1280,height:910},deviceScaleFactor:1}),errors=[],fontErrors=[]
 page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400&&/woff/.test(r.url()))fontErrors.push(r.url())});page.on('requestfailed',r=>{if(/woff/.test(r.url()))fontErrors.push(r.url())})
 await page.goto(url,{waitUntil:'networkidle'})
 const available=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.pages})
 const selected=available.filter(p=>!ids.length||ids.includes(p.id))
 if(!selected.length||ids.some(id=>!selected.some(p=>p.id===id)))throw Error('Requested page missing')
 for(const sheet of selected){
  await page.goto(`${url}/#/page/${sheet.id}`,{waitUntil:'networkidle'})
  await page.waitForFunction(()=>document.querySelector('[data-page]')?.dataset.fontsReady==='true')
  await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
  const article=page.locator(`[data-page="${sheet.id}"]`),b=await article.boundingBox()
  if(b.width!==1280||b.height!==910)throw Error('Canvas dimensions changed')
  if(await article.locator('img').count())throw Error('Raster image embedded in UI')
  const audit=await article.evaluate((article,elements)=>{
   const findings=[],paper=article.querySelector('[data-paper]'),pb=paper.getBoundingClientRect(),scale=pb.height/parseFloat(getComputedStyle(paper).height),ctx=document.createElement('canvas').getContext('2d')
   const fontFaces=[...document.fonts].map(f=>({family:f.family.replaceAll('"',''),weight:f.weight,style:f.style,status:f.status}))
   const textData=elements.filter(e=>e.kind==='text')
   for(const [i,el] of [...paper.querySelectorAll('.element-text')].entries()){
    const e=textData[i],s=getComputedStyle(el),rect=el.getBoundingClientRect(),range=document.createRange();range.selectNodeContents(el)
    const record={index:elements.indexOf(e),text:el.textContent.slice(0,100),elementId:e.id}
    const family=s.fontFamily.split(',')[0].replaceAll('"','').trim(),weight=Number(s.fontWeight)
    const declared=fontFaces.filter(f=>f.family===family&&f.style===s.fontStyle)
    if(!declared.some(f=>{const range=f.weight.split(' ').map(Number);return range.length===2?weight>=range[0]&&weight<=range[1]:weight===range[0]}))findings.push({...record,issue:'font weight/style unavailable',family,weight,style:s.fontStyle})
    ctx.font=`${s.fontStyle} ${s.fontWeight} ${s.fontSize} ${s.fontFamily}`;ctx.letterSpacing=s.letterSpacing==='normal'?'0px':s.letterSpacing
    const lines=el.textContent.split('\n'),m=ctx.measureText(lines.at(-1)),r=range.getBoundingClientRect()
    const paintedBottom=r.bottom-(m.fontBoundingBoxDescent-m.actualBoundingBoxDescent)*scale
    if(!e.rotate&&r.width>rect.width+3*scale)findings.push({...record,issue:'text wider than box',excess:(r.width-rect.width)/scale})
    if(!e.rotate&&paintedBottom>rect.bottom+3*scale)findings.push({...record,issue:'text taller than box',excess:(paintedBottom-rect.bottom)/scale})
    if(!e.rotate&&(r.left<pb.left-2||r.right>pb.right+2||paintedBottom>pb.bottom+2))findings.push({...record,issue:'text outside paper'})
    if(el.dataset.chip==='true'){
     const l=el.querySelector('[data-chip-label]').getBoundingClientRect(),m=ctx.measureText(lines.sort((a,b)=>b.length-a.length)[0])
     const x=l.x+l.width/2+(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2*scale-(rect.x+rect.width/2)
     const y=l.y+l.height/2+(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2*scale-(rect.y+rect.height/2)
     if((e.align??'center')==='center'&&(Math.abs(x)>1.25||Math.abs(y)>1.25))findings.push({...record,issue:'chip ink not centered',offset:[x,y]})
     if(l.width>rect.width+scale||l.height>rect.height+scale)findings.push({...record,issue:'chip label exceeds bounds'})
    }
   }
   const usedFonts=[...new Set([...paper.querySelectorAll('.element-text')].map(el=>getComputedStyle(el).fontFamily.split(',')[0].replaceAll('"','').trim()))]
   const faces=[...document.fonts].map(f=>({family:f.family.replaceAll('"',''),weight:f.weight,status:f.status}))
   const missingFonts=usedFonts.filter(f=>!faces.some(face=>face.family===f&&face.status==='loaded'))
   return {findings,usedFonts,missingFonts,loadedFaces:faces.filter(f=>f.status==='loaded'),paperBounds:{x:pb.x,y:pb.y,width:pb.width,height:pb.height},canvas:{width:article.offsetWidth,height:article.offsetHeight},elementCount:elements.length,chipCount:elements.filter(e=>e.chip).length,imageCount:elements.filter(e=>e.kind==='image').length}
  },sheet.elements)
  const file=path.join(root,'renders',round,`${sheet.id}.png`);await article.screenshot({path:file})
  const meta={id:sheet.id,round,sourceHash,rendererHash,definitionHash:hash(JSON.stringify(sheet)),pngHash:hash(await readFile(file)),reference:sheet.reference,size:sheet.size,notes:sheet.notes,...audit,fontErrors:[...fontErrors],browserErrors:[...errors]}
  await writeFile(path.join(root,'comparisons',`round-${round}`,`${sheet.id}.json`),JSON.stringify(meta,null,2))
  console.log(`${sheet.id}: ${audit.elementCount} elements, ${audit.findings.length} findings, ${audit.missingFonts.length} missing fonts`)
 }
 if(errors.length||fontErrors.length)throw Error([...errors,...fontErrors].join('\n'))
}finally{await browser.close();await server.close()}
