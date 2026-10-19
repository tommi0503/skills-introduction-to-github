import {chromium} from 'playwright-core';
import fs from 'node:fs/promises';
const deckArg=process.argv[2],mode='replica';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
page.on('pageerror',e=>console.error('PAGE ERROR',e.message));
await page.goto('http://localhost:5173/');
const decks=await page.evaluate(()=>window.__DECKS__); const audits=[];
for(const deck of decks.filter(d=>!deckArg||d.id===deckArg)){
 await fs.mkdir(`renders/${mode}/${deck.id}`,{recursive:true});
 for(const slide of deck.slides){
  await page.goto(`http://localhost:5173/?deck=${deck.id}&slide=${slide.id}`);
  await page.evaluate(()=>document.fonts.ready); await page.waitForTimeout(90);
  await page.locator('.slide').screenshot({path:`renders/${mode}/${deck.id}/${slide.id}.png`});
  const audit=await page.evaluate(()=>{
   const root=document.querySelector('.slide'),r=root.getBoundingClientRect();let issues=[];
   for(const el of root.querySelectorAll('[data-ui="text"],[data-ui="chip"]')){const b=el.getBoundingClientRect();if(b.left<r.left-.5||b.top<r.top-.5||b.right>r.right+.5||b.bottom>r.bottom+.5)issues.push({type:'outside',text:el.textContent.slice(0,70),rect:[b.x,b.y,b.width,b.height]});if(el.clientHeight&&el.scrollHeight>el.clientHeight+2)issues.push({type:'overflow-height',text:el.textContent.slice(0,70)});if(el.clientWidth&&el.scrollWidth>el.clientWidth+2)issues.push({type:'overflow-width',text:el.textContent.slice(0,70)});}
   return {size:[r.width,r.height],fonts:document.fonts.check('400 20px Pretendard')&&document.fonts.check('700 20px Pretendard'),issues};
  });audits.push({deck:deck.id,slide:slide.id,...audit});
 }
 console.log(`rendered ${deck.id}: ${deck.slides.length} slides (${mode})`);
}
await fs.mkdir('review',{recursive:true});await fs.writeFile(`review/audit-${deckArg||'all'}-${mode}.json`,JSON.stringify(audits,null,2));await browser.close();
