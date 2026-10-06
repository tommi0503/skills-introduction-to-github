import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {auditSlide} from '../scripts/audit.mjs'
import {writeFile} from 'node:fs/promises'
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
const page=await browser.newPage({viewport:{width:1280,height:720}}),url=`http://127.0.0.1:${server.httpServer.address().port}`
try { await page.goto(url);const decks=await page.evaluate(()=>window.__presentationDecks);const selected=decks.filter(d=>['p110','p112','p119','p127','p143','p145'].includes(d.id));await writeFile('review/group-c-definitions.json',JSON.stringify(selected,null,2));const out=[];
for(const d of decks.filter(d=>['p110','p112','p119','p127','p143','p145'].includes(d.id)))for(const s of d.slides){await page.goto(`${url}/#/slide/${d.id}/${s.id}`);await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))) });const audit=await auditSlide(page);const boxes=await page.evaluate(()=>[...document.querySelectorAll('.slide-canvas .element')].flatMap((el,index)=>{if(!el.classList.contains('element-text'))return[];const range=document.createRange();range.selectNodeContents(el);const r=range.getBoundingClientRect(),b=el.getBoundingClientRect();return r.height>b.height+3||r.width>b.width+3||r.bottom>721||r.right>1281||r.top<-1||r.left<-1?[{index,text:el.textContent,declared:[b.x,b.y,b.width,b.height],ink:[r.x,r.y,r.width,r.height],expectedClip:el.dataset.allowClip==='true'}]:[]}));out.push({deck:d.id,slide:s.id,...audit,boxes})};await writeFile('review/group-c-current-audit.json',JSON.stringify(out,null,2));console.log(JSON.stringify(out.filter(p=>p.findings.length).map(p=>({deck:p.deck,slide:p.slide,findings:p.findings,boxes:p.boxes})),null,2));}
finally {await browser.close();await server.close()}
