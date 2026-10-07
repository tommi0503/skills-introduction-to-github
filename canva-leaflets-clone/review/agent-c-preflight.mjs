import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {auditPage} from '../scripts/browser-audit.mjs'
import {writeFile} from 'node:fs/promises'
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage({viewport:{width:1280,height:720}}),url=`http://127.0.0.1:${server.httpServer.address().port}`
 await page.goto(url,{waitUntil:'networkidle'});const bs=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.brochures.filter(b=>['l11','l12','l13','l14'].includes(b.id))}),out=[]
 for(const b of bs)for(const [mode,sheets] of [['side',b.sides],['page',b.panels]])for(const sheet of sheets){await page.goto(`${url}/#/${mode}/${b.id}/${sheet.id}`,{waitUntil:'networkidle'});await page.locator('[data-page][data-fonts-ready="true"]').waitFor();await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))});const a=await auditPage(page);out.push({id:b.id+'-'+sheet.id,findings:a.issues.filter(f=>!f.expectedClip)});if(out.at(-1).findings.length)console.log(JSON.stringify(out.at(-1)))}
 await writeFile('review/agent-c-preflight.json',JSON.stringify(out,null,2)+'\n');console.log('Unexpected findings: '+out.reduce((n,p)=>n+p.findings.length,0))
}finally{await browser.close();await server.close()}
