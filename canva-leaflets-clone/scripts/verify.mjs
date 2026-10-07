import {createServer,preview} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile,readdir} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {auditPage} from './browser-audit.mjs'
const hash=s=>createHash('sha256').update(s).digest('hex')
const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','src/fonts.ts','scripts/browser-audit.mjs']
const rendererHash=hash((await Promise.all(rendererFiles.map(f=>readFile(f,'utf8')))).join('\n'))
const manifest=JSON.parse(await readFile('public/reference/manifest.json','utf8'))
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
const dev=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'});await dev.listen()
const page=await browser.newPage({viewport:{width:1280,height:720}})
await page.goto(`http://127.0.0.1:${dev.httpServer.address().port}`,{waitUntil:'networkidle'})
const source=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return {brochures:m.brochures,missing:m.missingImplementations}})
await dev.close()
const prod=await preview({preview:{host:'127.0.0.1',port:0},logLevel:'error'})
const errors=[],failedAssets=[],issues=[],screens=[],fonts=new Map(),bounds=[]
page.on('pageerror',e=>errors.push(e.message))
page.on('requestfailed',r=>failedAssets.push(r.url()))
page.on('response',r=>{if(r.status()>=400&&!r.url().endsWith('/favicon.ico'))failedAssets.push(r.url())})
const base=`http://127.0.0.1:${prod.httpServer.address().port}`
const expect=(condition,message)=>{if(!condition)issues.push(message)}
try{
 expect(source.missing.length===0,`Missing implementations: ${source.missing}`)
 expect(source.brochures.length===26,'Expected 26 brochures')
 await page.goto(base,{waitUntil:'networkidle'});expect(await page.locator('.brochure-card').count()===26,'Gallery card count')
 for(const b of source.brochures){
  const m=JSON.parse(await readFile(`comparisons/final/${b.id}.json`,'utf8'))
  expect(m.rendererHash===rendererHash,`${b.id}: final render does not match current renderer`)
  expect(m.definitionHash===hash(JSON.stringify(b)),`${b.id}: final render does not match current definition`)
  expect(b.sides.length===2,`${b.id}: side count`)
  expect(b.panels.length===manifest.find(x=>x.id===b.id).foldCount*2,`${b.id}: native fold count`)
  for(const [mode,list] of [['page',b.panels],['side',b.sides]])for(const s of list){
   const capture=[...m.panels,...m.sides].find(x=>x.id===s.id),key=`${b.id}-${s.id}`
   expect(!!capture,`${key}: missing capture`)
   const png=await readFile(capture.file);expect(png.readUInt32BE(16)===1280&&png.readUInt32BE(20)===720,`${key}: PNG size`)
   expect(hash(png)===capture.pngSha256,`${key}: PNG changed after capture`)
   expect(hash(await readFile(capture.reference))===capture.referenceSha256,`${key}: reference changed after capture`)
   await page.goto(`${base}/#/${mode}/${b.id}/${s.id}`,{waitUntil:'networkidle'})
   await page.locator('[data-fonts-ready="true"]').waitFor();await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
   const audit=await auditPage(page),unexpected=audit.issues.filter(x=>!x.expectedClip)
   const occlusions=await page.evaluate(()=>[...document.querySelectorAll('[data-paper] .element-text')].flatMap(el=>{
    const range=document.createRange();range.selectNodeContents(el);const paper=el.parentElement.getBoundingClientRect(),hidden=[];
    // A rotated Range exposes an axis-aligned bounding box, whose corners may
    // lie outside the glyph. Sample unrotated text, then map points back through
    // the element's actual rotation (all native transforms use top-left origin).
    const saved=el.style.transform,transform=getComputedStyle(el).transform,matrix=transform==='none'?new DOMMatrix():new DOMMatrix(transform);
    el.style.transform='none';const origin=el.getBoundingClientRect(),rects=[...range.getClientRects()];el.style.transform=saved;
    for(const r of rects)for(const f of [.15,.5,.85,.97]){
     const dx=r.x+r.width*f-origin.x,dy=r.y+r.height*.5-origin.y;
     const x=origin.x+matrix.a*dx+matrix.c*dy,y=origin.y+matrix.b*dx+matrix.d*dy;
     if(x<paper.left||x>paper.right||y<paper.top||y>paper.bottom||x<0||x>=1280||y<0||y>=720)continue;
     const cover=document.elementFromPoint(x,y)?.closest('.element');
     if(cover?.dataset.elementKind==='image')hidden.push({x,y,cover:cover.dataset.label});
    }
    return hidden.length?[{text:el.textContent,hiddenSamples:hidden}]:[];
   }))
   expect(occlusions.length===0,`${key}: text occluded by placeholder ${JSON.stringify(occlusions)}`)
   expect(unexpected.length===0,`${key}: ${JSON.stringify(unexpected)}`)
   const canvasBounds=await page.evaluate(()=>[...document.querySelectorAll('[data-paper] .element')].filter(e=>e.dataset.elementKind!=='text').map(e=>{const s=getComputedStyle(e),p=e.parentElement,x=parseFloat(s.left),y=parseFloat(s.top),w=parseFloat(s.width),h=parseFloat(s.height);return{kind:e.dataset.elementKind,x,y,w,h,clipReason:e.dataset.clipReason,foldClip:e.dataset.foldClip==='true',outside:x<0||y<0||x+w>parseFloat(p.style.width)||y+h>parseFloat(p.style.height)}}).filter(x=>x.outside))
   if(canvasBounds.length)bounds.push({key,elements:canvasBounds,note:mode==='page'?'Native fold boundary crops shared geometry; reviewed in individual pairs':'Paper-edge geometry is clipped by the native paper; reviewed in individual pairs'})
   for(const f of audit.fontChecks)fonts.set(JSON.stringify(f),f)
   screens.push({key,canvas:audit.size,pngSha256:capture.pngSha256,unexpectedFindings:unexpected,expectedFoldTextClips:audit.issues.filter(x=>x.expectedClip).length,chipCount:audit.chipCount,placeholderCount:audit.placeholderCount})
  }
  console.log(`${b.id}: production font/geometry and final-source hash checked`)
 }
 const pngs=(await readdir('renders/final')).filter(f=>f.endsWith('.png'))
 expect(screens.length===202&&pngs.length===202,'Expected 202 final PNGs')
 expect(screens.filter(x=>/-p[123]$/.test(x.key)).length===150,'Expected 150 folded panels')
 expect(screens.filter(x=>!/-p[123]$/.test(x.key)).length===52,'Expected 52 unfolded sides')
 expect(errors.length===0,`Browser errors ${errors}`);expect(failedAssets.length===0,`Failed assets ${failedAssets}`)
 const report={status:issues.length?'failed':'passed',checkedAt:new Date().toISOString(),environment:'Built production app in Chromium',brochures:26,unfoldedSides:52,panels:150,totalPNGs:202,pngSize:[1280,720],rendererHash,sourceAndFinalRenderHashesMatch:!issues.some(x=>x.includes('match current')),runtimeErrors:errors,failedAssets,issues,fontFaces:[...fonts.values()],nontextCanvasBoundaryChecks:bounds,screens}
 await writeFile('review/verification.json',JSON.stringify(report,null,2)+'\n')
 if(issues.length)throw Error(JSON.stringify(issues))
 console.log('PASS: all 202 production pages; fonts, text bounds, ink-centered chips, size and final source hashes')
}finally{await browser.close();await new Promise(r=>prod.httpServer.close(r))}
