import {createServer,preview} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,readdir,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
const hash=s=>createHash('sha256').update(s).digest('hex')
const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts']
const rendererHash=hash((await Promise.all(rendererFiles.map(f=>readFile(f,'utf8')))).join('\n'))
const manifest=JSON.parse(await readFile('public/reference/manifest.json','utf8'))
const ids=Array.from({length:72},(_,i)=>`l${String(i+1).padStart(2,'0')}`)
if(JSON.stringify(manifest.map(d=>d.id))!==JSON.stringify(ids))throw Error('Incorrect source inventory')
const metas=(await readdir('comparisons/final')).filter(n=>/^l\d{2}\.json$/.test(n))
if(metas.length!==72)throw Error('Missing final brochure captures')
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const production=await preview({preview:{host:'127.0.0.1',port:0},logLevel:'error'})
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage({viewport:{width:1440,height:900}}),errors=[]
 page.on('pageerror',e=>errors.push(e.message))
 await page.goto(`http://127.0.0.1:${server.httpServer.address().port}`,{waitUntil:'networkidle'})
 const brochures=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.brochures})
 if(brochures.length!==72||brochures.reduce((n,b)=>n+b.panels.length,0)!==432)throw Error('Incomplete independent pages')
 let chips=0,replacements=0,findings=[],uniform=true
 for(const b of brochures){
  const meta=JSON.parse(await readFile(`comparisons/final/${b.id}.json`,'utf8'))
  if(hash(JSON.stringify(b))!==meta.definitionHash||rendererHash!==meta.rendererHash)throw Error(`Stale final output ${b.id}`)
  if(meta.panels.length!==6||meta.sides.length!==2)throw Error('Missing panel or unfolded sheet')
  for(const p of meta.panels){chips+=p.chipCount;replacements+=p.replacementCount;findings.push(...p.findings.map(f=>({...f,brochure:b.id,page:p.id})))}
  for(const side of meta.sides)findings.push(...side.findings.map(f=>({...f,brochure:b.id,page:side.id})))
  for(const side of b.sides){
   const panels=b.panels.filter(p=>p.sideId===side.id)
   if(panels.reduce((n,p)=>n+p.size[0],0)!==side.size[0]||panels.some(p=>p.size[1]!==side.size[1]))throw Error('Fold boundaries distort source proportions')
  }
 }
 if(findings.length)throw Error(`Unresolved typography findings: ${JSON.stringify(findings.slice(0,50))}`)
 const url=`http://127.0.0.1:${production.httpServer.address().port}`
 await page.goto(url,{waitUntil:'networkidle'})
 if(await page.locator('.brochure-card').count()!==72)throw Error('Production gallery incomplete')
 await page.locator('.brochure-card').first().click();await page.waitForFunction(()=>document.querySelectorAll('.page-grid a').length===6);if(await page.locator('.page-grid a').count()!==6)throw Error('Independent six-page navigation missing')
 await page.getByRole('link',{name:'앞·뒷면 펼치기'}).click();await page.waitForFunction(()=>document.querySelectorAll('.page-grid a').length===2);if(await page.locator('.page-grid a').count()!==2)throw Error('Unfolded navigation missing')
 await page.getByRole('link',{name:'원본 비교'}).click();await page.waitForFunction(()=>document.querySelectorAll('.compare-row img').length===2&&[...document.querySelectorAll('.compare-row img')].every(i=>i.complete&&i.naturalWidth>0))
 for(const [id,panel] of [['l01','s01-p1'],['l41','s02-p3'],['l72','s02-p3']]){
  await page.goto(`${url}/#/page/${id}/${panel}`,{waitUntil:'networkidle'});await page.locator('[data-fonts-ready="true"]').waitFor()
  const bounds=await page.locator('[data-page]').boundingBox();uniform&&=bounds.width===1280&&bounds.height===720
  if(await page.locator('article img').count())throw Error('Source screenshot embedded')
  const s=await page.locator('[data-paper]').evaluate(el=>{const b=el.getBoundingClientRect(),c=getComputedStyle(el);return {scaleX:b.width/parseFloat(c.width),scaleY:b.height/parseFloat(c.height)}})
  if(Math.abs(s.scaleX-s.scaleY)>.0001)throw Error('Page stretched instead of contained')
 }
 if(!uniform)throw Error('Canvas size mismatch')
 const actualFonts=await page.evaluate(async()=>{await document.fonts.ready;return (await document.fonts.load('700 20px "Noto Sans KR"','한글')).some(f=>f.status==='loaded'&&f.weight==='700')&&(await document.fonts.load('400 20px "Tinos"','Sample')).some(f=>f.status==='loaded')})
 if(!actualFonts)throw Error('Actual declared font files missing')
 const gray=await page.locator('.element-image').evaluateAll(els=>els.every(el=>getComputedStyle(el).backgroundColor==='rgb(229, 229, 229)'))
 if(!gray||errors.length)throw Error('Placeholder or browser verification failed')
 const report={status:'passed',brochures:72,sourceSheets:144,pages:432,unfoldedSheets:144,canvas:[1280,720],uniformScale:true,sixIndependentPages:true,exactSourceFoldWidths:true,sourceAndRendererHashesMatch:true,productionGallery:true,productionNavigation:true,referenceImagesLoad:true,actualFontFiles:true,chipCount:chips,chipCenterIssues:0,replacementCount:replacements,grayPlaceholders:true,noEmbeddedSourceScreenshots:true,layoutFindings:findings,pageErrors:errors}
 await writeFile('review/verification.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2))
}finally{await browser.close();await server.close();await new Promise(r=>production.httpServer.close(r))}
