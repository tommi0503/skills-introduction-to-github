import {createServer,preview} from 'vite'
import {chromium} from 'playwright-core'
import {mkdir,readFile,writeFile,readdir} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {execFileSync} from 'node:child_process'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');process.chdir(root)
const output=path.resolve(process.argv[2]??path.join(root,'shots','review'))
const hash=data=>createHash('sha256').update(data).digest('hex')
const sourceHashes={}
async function collect(dir){for(const ent of await readdir(dir,{withFileTypes:true})){const f=path.join(dir,ent.name);if(ent.isDirectory())await collect(f);else sourceHashes[path.relative(root,f)]=hash(await readFile(f))}}
await collect(path.join(root,'src'));for(const f of ['package.json','package-lock.json','vite.config.ts','index.html'])sourceHashes[f]=hash(await readFile(f))
const sourceCommit=execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'}).trim()
await mkdir(path.join(output,'native'),{recursive:true})
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH??'/usr/bin/chromium',args:['--no-sandbox']})
const dev=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'});await dev.listen()
const page=await browser.newPage({viewport:{width:2200,height:1200},deviceScaleFactor:1})
let production
try{
 await page.goto(`http://127.0.0.1:${dev.httpServer.address().port}`,{waitUntil:'networkidle'})
 const definitions=await page.evaluate(async()=>{const {leaflets}=await import('/src/leaflets/registry.ts');return leaflets.map(({Component,...metadata})=>metadata)})
 await dev.close()
 if(definitions.length!==35)throw Error(`Expected 35 screens, found ${definitions.length}`)
 production=await preview({root,preview:{host:'127.0.0.1',port:0},logLevel:'error'})
 const base=`http://127.0.0.1:${production.httpServer.address().port}`,runtimeErrors=[],failedAssets=[],pages=[]
 page.on('pageerror',e=>runtimeErrors.push(e.message));page.on('requestfailed',r=>failedAssets.push(r.url()));page.on('response',r=>{if(r.status()>=400&&!r.url().endsWith('/favicon.ico'))failedAssets.push(r.url())})
 for(const def of definitions){
  await page.goto(`${base}/#/sheet/${def.id}`,{waitUntil:'networkidle'})
  const stage=page.locator('[data-stage]');if(await stage.count()!==1)throw Error(`${def.id}: stage count`)
  await page.evaluate(async()=>{
   await document.fonts.ready
   const stage=document.querySelector('[data-stage]'),used=new Map()
   const walker=document.createTreeWalker(stage,NodeFilter.SHOW_TEXT);let node
   while(node=walker.nextNode()){const text=node.textContent.trim();if(!text)continue;const style=getComputedStyle(node.parentElement),key=`${style.fontStyle} ${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;used.set(key,(used.get(key)??'')+text)}
   await Promise.all([...used].map(([font,text])=>document.fonts.load(font,text)));await document.fonts.ready
   await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))
  })
  const metrics=await stage.evaluate(el=>{const r=el.getBoundingClientRect();return {width:r.width,height:r.height,loadedFontFaces:[...document.fonts].filter(f=>f.status==='loaded').length,failedFontFaces:[...document.fonts].filter(f=>f.status==='error').map(f=>({family:f.family,weight:f.weight})),fontStatus:document.fonts.status}})
  const expected=[480*def.panels,1018];if(metrics.width!==expected[0]||metrics.height!==expected[1]||metrics.failedFontFaces.length)throw Error(`${def.id}: ${JSON.stringify(metrics)}`)
  const file=`native/${def.id}.png`;await stage.screenshot({path:path.join(output,file),animations:'disabled'})
  const bytes=await readFile(path.join(output,file));if(bytes.readUInt32BE(16)!==expected[0]||bytes.readUInt32BE(20)!==expected[1])throw Error(`${def.id}: PNG dimensions`)
  pages.push({...def,file,size:expected,sha256:hash(bytes),metrics});console.log(`${def.id}: ${expected.join('x')} captured`)
 }
 if(runtimeErrors.length||failedAssets.length)throw Error(JSON.stringify({runtimeErrors,failedAssets}))
 for(const [f,sha] of Object.entries(sourceHashes))if(hash(await readFile(path.join(root,f)))!==sha)throw Error(`Source changed during capture: ${f}`)
 const report={status:'passed',capturedAt:new Date().toISOString(),sourceCommit,environment:'Built production app in Chromium, device scale factor 1',scope:'Render existing screens without layout or text changes',screenCount:pages.length,sourceHashes,sourceUnchangedDuringCapture:true,runtimeErrors,failedAssets,pages}
 await writeFile(path.join(output,'render-verification.json'),JSON.stringify(report,null,2)+'\n');console.log('PASS: 35 production screens, original geometry, fonts settled and no browser/asset errors')
}finally{
 await browser.close();await dev.close();if(production)await new Promise(resolve=>production.httpServer.close(resolve))
}
