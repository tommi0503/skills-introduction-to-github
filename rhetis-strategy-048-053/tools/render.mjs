const {chromium}=await import('playwright-core').catch(()=>import('/workspace/skills-introduction-to-github/presentation3-clone/node_modules/playwright-core/index.mjs'));
import fs from 'node:fs/promises';
const deck=process.argv[2]||'all',mode=process.argv[3]||'direct';
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
for(const d of deck==='all'?['048','049','050','051','052','053']:[deck]){
 await page.goto(`http://127.0.0.1:4173/?deck=${d}&mode=${mode}`);await page.waitForFunction(()=>window.__ready||window.__error);if(await page.evaluate(()=>window.__error))throw new Error(await page.evaluate(()=>window.__error));await page.evaluate(()=>document.fonts.ready);
 const slides=await page.evaluate(()=>window.__slides.map(s=>s.id));await fs.mkdir(`artifacts/${mode}/${d}`,{recursive:true});const audit=[];
 for(const id of slides){await page.goto(`http://127.0.0.1:4173/?deck=${d}&slide=${id}&mode=${mode}`);await page.waitForFunction(()=>window.__ready);await page.evaluate(()=>document.fonts.ready);await page.locator('.scene-slide').screenshot({path:`artifacts/${mode}/${d}/${id}.png`});
 const issues=await page.evaluate(()=>[...document.querySelectorAll('.node.text')].flatMap(e=>{const b=e.getBoundingClientRect(),r=document.createRange();r.selectNodeContents(e.querySelector('.bridge-text')||e);const t=r.getBoundingClientRect();let i=[];if(b.x<-.5||b.y<-.5||b.right>1280.5||b.bottom>720.5)i.push('bounds');if(t.right>b.right+2||t.bottom>b.bottom+3)i.push('text-overflow');return i.length?[{text:e.textContent,issues:i,box:[b.x,b.y,b.width,b.height],actual:[t.width,t.height]}]:[]}));audit.push({id,issues});}
 await page.goto(`http://127.0.0.1:4173/?deck=${d}&mode=${mode}`);await page.waitForFunction(()=>window.__ready);await page.evaluate(()=>document.fonts.ready);await page.pdf({path:`artifacts/${mode}/${d}.pdf`,width:'1280px',height:'720px',printBackground:true,preferCSSPageSize:true});await fs.writeFile(`artifacts/${mode}/${d}-audit.json`,JSON.stringify(audit,null,2));console.log(d,mode,slides.length,'slides',audit.reduce((n,a)=>n+a.issues.length,0),'issues');
}await browser.close();
