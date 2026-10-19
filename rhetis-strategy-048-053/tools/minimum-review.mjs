const {chromium}=await import('playwright-core').catch(()=>import('/workspace/skills-introduction-to-github/presentation3-clone/node_modules/playwright-core/index.mjs'));
import fs from 'node:fs/promises';
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});const page=await browser.newPage({viewport:{width:1300,height:750}});const result=[];
for(const mode of ['light','dark']){
 await page.goto(`http://127.0.0.1:4173/${mode}.html`);await page.addStyleTag({content:'@font-face{font-family:Pretendard;src:url(/public/fonts/PretendardVariable.woff2);font-weight:100 900}body{display:block;padding:0}article{display:none}article.active{display:block}article.active>.frame{width:1280px;height:720px}article.active>.frame>.slide{transform:none}'});await page.evaluate(()=>document.fonts.ready);
 const count=await page.locator('article').count();
 for(let i=2;i<count;i++){
  const a=page.locator('article').nth(i);const title=await a.locator('h2').innerText();const mins=(title.match(/min (.*)/)||[])[1]||'8x4';
  for(const min of mins.split('|').map(s=>s.trim())){
   const [cols,rows]=min.split('x').map(Number);
   await page.evaluate(({i,cols,rows})=>{document.querySelectorAll('article').forEach((e,j)=>e.classList.toggle('active',j===i));const body=document.querySelector('article.active .body');body.firstElementChild.style.gridColumn=`1 / span ${cols}`;body.firstElementChild.style.gridRow=`1 / span ${rows}`;},{i,cols,rows});
   const issues=await a.evaluate(a=>{const root=a.querySelector('.body').firstElementChild,rb=root.getBoundingClientRect();return [...root.querySelectorAll('.name,.note,.fig,.chip,th,td,.node,.leaf,.root,.tag,.hl')].flatMap(e=>{if(!e.getClientRects().length)return[];const r=document.createRange();r.selectNodeContents(e);const b=r.getBoundingClientRect();if(!b.width||!b.height)return[];return b.left<rb.left-2||b.top<rb.top-2||b.right>rb.right+2||b.bottom>rb.bottom+2?[{text:e.textContent,position:[b.left-rb.left,b.top-rb.top,b.width,b.height],root:[rb.width,rb.height]}]:[];})});result.push({mode,title,min,issues});
  }
 }
}await fs.writeFile('artifacts/library/minimum-audit.json',JSON.stringify(result,null,2));console.log(result.length,'minimum checks;',result.reduce((n,x)=>n+x.issues.length,0),'issues');await browser.close();
