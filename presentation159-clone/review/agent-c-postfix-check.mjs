// Automatic verification only; this does not create a third comparison/render round.
import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {auditSlide} from '../scripts/browser-audit.mjs'
const assignment=JSON.parse(await readFile(new URL('./assignment-c.json',import.meta.url),'utf8'))
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium'})
const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1})
const url='http://127.0.0.1:'+server.httpServer.address().port
const rows=[]
try {
 await page.goto(url,{waitUntil:'networkidle'})
 const decks=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.decks})
 for(const deck of assignment){
  const definition=decks.find(d=>d.id===deck.id)
  const definitionHash=createHash('sha256').update(JSON.stringify(definition)).digest('hex')
  for(const slide of deck.slides){
   await page.goto(url+'/#/slide/'+deck.id+'/'+slide.id,{waitUntil:'networkidle'})
   const audit=await auditSlide(page)
   rows.push({deck:deck.id,slide:slide.id,definitionHash,...audit})
  }
  console.log(deck.id,rows.filter(r=>r.deck===deck.id).reduce((n,r)=>n+r.issues.filter(i=>!i.expectedClip).length,0),'findings')
 }
 await writeFile(new URL('./agent-c-postfix-audit.json',import.meta.url),JSON.stringify({checkedAt:new Date().toISOString(),verification:'Live browser automatic audit after second visual comparison round. No PNG was captured in this check; primary final capture remains required.',pages:rows.length,unexpectedFindings:rows.reduce((n,r)=>n+r.issues.filter(i=>!i.expectedClip).length,0),rows},null,2)+'\n')
} finally {await browser.close();await server.close()}
