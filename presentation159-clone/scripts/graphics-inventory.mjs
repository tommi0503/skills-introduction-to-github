import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'
import {fileURLToPath} from 'node:url'

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
process.chdir(root)
const hash=bytes=>createHash('sha256').update(bytes).digest('hex')
const baseline=JSON.parse(await readFile('review/pre-graphics-revision/baseline-pages.json','utf8')).pages
const previous=new Map(baseline.map(page=>[page.key,page]))
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
let browser
try{
 browser=await chromium.launch({executablePath:'/usr/bin/chromium'})
 const page=await browser.newPage()
 await page.goto('http://127.0.0.1:'+server.httpServer.address().port,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const module=await import('/src/registry.ts');return module.decks})
 const pages=[],graphicKinds={}
 for(const deck of decks){
  const meta=JSON.parse(await readFile('comparisons/final/'+deck.id+'.json','utf8'))
  if(meta.definitionHash!==hash(JSON.stringify(deck)))throw Error('Stale capture '+deck.id)
  for(const slide of deck.slides){
   const key=deck.id+'-'+slide.id,old=previous.get(key),capture=meta.slides.find(item=>item.id===slide.id)
   if(!old||!capture)throw Error('Missing page '+key)
   const placeholders=slide.elements.filter(element=>element.kind==='image').map((element,index)=>({index,label:element.text??'Unlabelled photo',region:[element.x,element.y,element.w,element.h]}))
   const graphics=slide.elements.filter(element=>element.kind==='graphic')
   for(const graphic of graphics)graphicKinds[graphic.graphic]=(graphicKinds[graphic.graphic]??0)+1
   pages.push({key,previousPlaceholderCount:old.placeholderCount,placeholderCount:placeholders.length,
    placeholders,svgGraphicCount:graphics.length,svgGradientCount:graphics.reduce((sum,element)=>sum+(element.graphicOptions?.gradients?.length??0),0),
    cssGradientCount:capture.gradientCount??0,fadeMaskCount:capture.fadeMaskCount??0,
    vectorPathCount:slide.elements.filter(element=>element.kind==='path').length,
    pngChanged:old.pngSha256!==capture.pngSha256,definitionHash:meta.definitionHash,finalPngSha256:capture.pngSha256})
  }
 }
 if(pages.length!==159||decks.length!==53)throw Error('Incomplete inventory')
 const sum=field=>pages.reduce((total,page)=>total+page[field],0)
 const report={revision:'SVG and gradient restoration',decks:53,pages:159,comparisonCycles:2,
  previousPlaceholderCount:sum('previousPlaceholderCount'),remainingPlaceholderCount:sum('placeholderCount'),
  removedPlaceholderCount:sum('previousPlaceholderCount')-sum('placeholderCount'),
  svgGraphicCount:sum('svgGraphicCount'),svgGradientCount:sum('svgGradientCount'),cssGradientCount:sum('cssGradientCount'),fadeMaskCount:sum('fadeMaskCount'),vectorPathCount:sum('vectorPathCount'),
  changedPageCount:pages.filter(page=>page.pngChanged).length,graphicKinds,
  limitations:['Photos and photographic device screens retain light gray placeholders.','SVG illustration outlines, texture and exact font glyphs can differ from the raster reference; individual differences are recorded in main-review.json.'],
  checkedAt:new Date().toISOString(),pageInventory:pages}
 await writeFile('review/graphics-revision.json',JSON.stringify(report,null,2)+'\n')
 console.log(JSON.stringify({...report,pageInventory:report.pageInventory.length},null,2))
}finally{if(browser)await browser.close();await server.close()}
