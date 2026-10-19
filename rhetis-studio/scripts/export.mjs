import {chromium} from 'playwright-core';import fs from 'node:fs/promises';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1280,height:720}});await page.goto('http://127.0.0.1:5173/',{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);const registry=await page.evaluate(()=>window.registry);await fs.mkdir('exports/pdf',{recursive:true});
const ids=process.argv.slice(2).filter(x=>/^\d\d$/.test(x));for(const mode of ['replica','assembled'])for(const id of Object.keys(registry).filter(x=>!ids.length||ids.includes(x))){
 await page.goto(`http://127.0.0.1:5173/?deck=${id}&mode=${mode}&all=1`,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);await page.pdf({path:`exports/pdf/${mode}-${id}.pdf`,width:'1280px',height:'720px',printBackground:true,preferCSSPageSize:true});console.log(`PDF ${mode} ${id}`);
}
await browser.close();
