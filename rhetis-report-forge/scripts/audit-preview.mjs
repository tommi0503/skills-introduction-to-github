import {chromium} from 'playwright-core';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1440,height:1000}}),results=[];
for(const name of ['preview','assembled','light','dark']){
 const failures=[];page.on('requestfailed',r=>failures.push(r.url()));
 await page.context().setOffline(true);await page.setContent(await fs.readFile(`outputs/${name}.html`,'utf8'),{waitUntil:'load'});await page.evaluate(()=>document.fonts.ready);
 const r=await page.evaluate(()=>({slides:document.querySelectorAll('.slide').length,font:document.fonts.check('400 20px Pretendard'),external:[...document.querySelectorAll('img[src],script[src],link[href]')].map(x=>x.src||x.href).filter(x=>/^https?:/.test(x))}));
 if(name==='preview'){
  await page.selectOption('select','054');r.filtered=await page.locator('.preview-item:visible').count();await page.locator('.preview-stage:visible').first().click();r.dialog=await page.locator('#viewer').evaluate(e=>e.open);await page.keyboard.press('ArrowRight');r.modalSize=await page.locator('#modal-stage>.slide').evaluate(e=>[e.offsetWidth,e.offsetHeight]);await page.keyboard.press('Escape');
 }
 results.push({name,htmlSHA256:crypto.createHash('sha256').update(await fs.readFile(`outputs/${name}.html`)).digest('hex'),method:'Standalone HTML setContent with browser network offline; managed browser blocks file scheme',...r,failures});page.removeAllListeners('requestfailed');
}
await fs.writeFile('review/preview-audit.json',JSON.stringify(results,null,2));console.log(JSON.stringify(results));await browser.close();
