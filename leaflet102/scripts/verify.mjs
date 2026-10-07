import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),hash=s=>createHash('sha256').update(s).digest('hex')
const files=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','src/fonts.ts']
const rendererHash=hash((await Promise.all(files.map(f=>readFile(path.join(root,f),'utf8')))).join('\n'))
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage();await page.goto(`http://127.0.0.1:${server.httpServer.address().port}`,{waitUntil:'networkidle'})
 const pages=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.pages})
 const ids=pages.map(p=>p.id),expected=Array.from({length:102},(_,i)=>String(i+1).padStart(3,'0'))
 if(JSON.stringify(ids)!==JSON.stringify(expected))throw Error('Expected exactly 001–102 once each')
 const failures=[]
 for(const sheet of pages){
  const meta=JSON.parse(await readFile(path.join(root,'comparisons/round-final',`${sheet.id}.json`),'utf8'))
  const png=await readFile(path.join(root,'renders/final',`${sheet.id}.png`))
  if(png.readUInt32BE(16)!==1280||png.readUInt32BE(20)!==910)failures.push(`${sheet.id}: invalid PNG size`)
  if(meta.definitionHash!==hash(JSON.stringify(sheet)))failures.push(`${sheet.id}: last data edit not rendered`)
  if(meta.rendererHash!==rendererHash)failures.push(`${sheet.id}: last renderer edit not rendered`)
  if(meta.pngHash!==hash(png))failures.push(`${sheet.id}: PNG hash mismatch`)
  if(meta.findings.length)failures.push(`${sheet.id}: ${meta.findings.length} overflow or chip findings`)
  if(meta.missingFonts.length||meta.fontErrors.length||meta.browserErrors.length)failures.push(`${sheet.id}: font/browser failures`)
 }
 const report={pages:102,size:[1280,910],rendererHash,finalDataReflected:true,failures,passed:!failures.length}
 await writeFile(path.join(root,'review/final-verification.json'),JSON.stringify(report,null,2))
 console.log(JSON.stringify(report,null,2));if(failures.length)process.exitCode=1
}finally{await browser.close();await server.close()}
