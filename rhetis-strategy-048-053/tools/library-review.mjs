const {chromium}=await import('playwright-core').catch(()=>import('/workspace/skills-introduction-to-github/presentation3-clone/node_modules/playwright-core/index.mjs'));
import fs from 'node:fs/promises';
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1400,height:1000},deviceScaleFactor:1});const audit=[];await fs.mkdir('artifacts/library',{recursive:true});
for(const mode of ['light','dark']){
 await page.goto(`http://127.0.0.1:4173/${mode}.html`);await page.addStyleTag({content:'@font-face{font-family:Pretendard;src:url(/public/fonts/PretendardVariable.woff2);font-weight:100 900;font-display:block}'});await page.addStyleTag({content:'body{grid-template-columns:1280px}.frame{width:1280px;height:720px}.frame>.slide{transform:none}'});await page.evaluate(()=>document.fonts.ready);
 const count=await page.locator('article').count();
 for(let i=0;i<count;i++){
  const a=page.locator('article').nth(i);const title=await a.locator('h2').innerText();const slug=title.split('min')[0].trim().replace(/[^a-zA-Z0-9-]+/g,'-');
  await a.locator(':scope > .frame').screenshot({path:`artifacts/library/${mode}-${slug}.png`});
  const issues=await a.evaluate(a=>{const slide=a.querySelector('.slide'),sb=slide.getBoundingClientRect();return [...a.querySelectorAll('.name,.note,.fig,.chip,td,th,.node,.leaf,.root,.tag,.hl')].flatMap(e=>{if(!e.getClientRects().length)return[];const b=e.getBoundingClientRect(),r=document.createRange();r.selectNodeContents(e);const t=r.getBoundingClientRect();return t.right>sb.right+1||t.bottom>sb.bottom+1||t.right>b.right+2||t.bottom>b.bottom+2?[{text:e.textContent,box:[b.x-sb.x,b.y-sb.y,b.width,b.height],actual:[t.width,t.height]}]:[]})});audit.push({mode,title,issues});
 }
 console.log(mode,count,'fixtures');
 await page.pdf({path:`artifacts/library/${mode}-sheet.pdf`,width:'1400px',height:'1000px',printBackground:true});
}await fs.writeFile('artifacts/library/audit.json',JSON.stringify(audit,null,2));await browser.close();console.log('Issues',audit.reduce((n,a)=>n+a.issues.length,0));
