import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {auditSlide} from '../scripts/audit.mjs'
import {writeFile,mkdir} from 'node:fs/promises'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)))
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
const results=[];await mkdir('/tmp/b-extra-live-final-three',{recursive:true})
try{const page=await browser.newPage({viewport:{width:1280,height:720}});const url=`http://127.0.0.1:${server.httpServer.address().port}`
for(const id of ['s03-30','s04-26','s04-38']){
 await page.goto(`${url}/#/slide/p105/${id}`,{waitUntil:'load'});await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})
 const a=await auditSlide(page);let glyphGaps=[]
 if(id==='s04-38')glyphGaps=await page.evaluate(()=>{
  const labels=[...document.querySelectorAll('[data-chip-label]')].filter(e=>['79%','21%'].includes(e.textContent));const ctx=document.createElement('canvas').getContext('2d');const boxes=labels.map(e=>{const cs=getComputedStyle(e),r=e.getBoundingClientRect();ctx.font=`${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;const m=ctx.measureText(e.textContent),scale=r.width/m.width;return {text:e.textContent,left:r.left-m.actualBoundingBoxLeft*scale,right:r.left+m.actualBoundingBoxRight*scale,top:r.top,bottom:r.bottom}});return Array.from({length:5},(_,i)=>({pair:i+1,gap:boxes[i*2].left-boxes[i*2+1].right,blue:boxes[i*2],red:boxes[i*2+1]}))
 })
 await page.screenshot({path:`/tmp/b-extra-live-final-three/p105-${id}.png`});results.push({id,...a,glyphGaps})
}
await writeFile(path.join(root,'review/group-b-extra-final-three-audit.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results.map(r=>({id:r.id,findings:r.findings,gaps:r.glyphGaps.map(g=>g.gap)}))))
}finally{await browser.close();await server.close()}
