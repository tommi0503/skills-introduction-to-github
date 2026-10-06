import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {auditSlide} from '../scripts/audit.mjs'
import {writeFile} from 'node:fs/promises'
import {fileURLToPath} from 'node:url'
import path from 'node:path'
const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)))
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage({viewport:{width:1280,height:720}})
 const url=`http://127.0.0.1:${server.httpServer.address().port}`
 await page.goto(url,{waitUntil:'load'});await page.waitForFunction(()=>window.__presentationDecks)
 const decks=await page.evaluate(()=>window.__presentationDecks.filter(d=>['p055','p060','p100','p105'].includes(d.id)))
 const results=[]
 for(const d of decks)for(const s of d.slides){
  await page.goto(`${url}/#/slide/${d.id}/${s.id}`,{waitUntil:'load'})
  await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
  const audit=await auditSlide(page);results.push({deck:d.id,id:s.id,...audit})
 }
 await writeFile(path.join(root,'review/group-b-extra-final-audit.json'),JSON.stringify(results,null,2))
 console.log(results.length,results.flatMap(s=>s.findings).length)
 for(const s of results)if(s.findings.length)console.log(s.deck,s.id,JSON.stringify(s.findings))
}finally{await browser.close();await server.close()}
