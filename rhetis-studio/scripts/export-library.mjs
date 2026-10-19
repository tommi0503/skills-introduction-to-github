import {chromium} from 'playwright-core';import fs from 'node:fs/promises';
const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});const p=await b.newPage({viewport:{width:1280,height:720}});
for(const mode of ['light','dark']){
 await fs.mkdir(`exports/library/${mode}`,{recursive:true});await p.goto(`http://127.0.0.1:5173/sheets/${mode}.html`,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
 const labels=await p.locator('article>h2').allTextContents();await p.evaluate(()=>{const slides=[...document.querySelectorAll('.frame>.slide')];document.body.replaceChildren(...slides)});
 await p.addStyleTag({content:'html,body{margin:0!important;padding:0!important;background:white!important;display:block!important}.slide{width:1280px!important;height:720px!important;transform:none!important;position:relative!important;break-after:page}@page{size:1280px 720px;margin:0}'});
 const slides=p.locator('section.slide');for(let i=0;i<await slides.count();i++){await slides.nth(i).screenshot({path:`exports/library/${mode}/${String(i+1).padStart(3,'0')}.png`});}
 await p.pdf({path:`exports/library-${mode}-97-fixtures.pdf`,width:'1280px',height:'720px',printBackground:true,preferCSSPageSize:true});await fs.writeFile(`exports/library/${mode}/index.json`,JSON.stringify(labels,null,2));console.log(mode,labels.length);
}
await b.close();
