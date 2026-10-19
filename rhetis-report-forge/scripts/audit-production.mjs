import {chromium} from 'playwright-core';
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1280,height:720}}),rows=[],errors=[];page.on('pageerror',e=>errors.push(e.message));
for(const route of ['/?deck=054&slide=18','/?deck=061&slide=02','/outputs/preview.html','/outputs/assembled.html','/outputs/light.html','/outputs/dark.html']){
 const response=await page.goto('http://127.0.0.1:5174'+route);await page.evaluate(()=>document.fonts.ready);
 rows.push({route,status:response.status(),...await page.evaluate(()=>({slides:document.querySelectorAll('.slide').length,font:document.fonts.check('400 20px Pretendard'),firstSize:[document.querySelector('.slide').offsetWidth,document.querySelector('.slide').offsetHeight]}))});
}
const pdfs=[];for(const f of await fs.readdir('pdfs')){if(!f.endsWith('.pdf'))continue;const r=await page.request.get('http://127.0.0.1:5174/pdfs/'+f),body=await r.body();pdfs.push({file:f,status:r.status(),matchesSource:crypto.createHash('sha256').update(body).digest('hex')===crypto.createHash('sha256').update(await fs.readFile('pdfs/'+f)).digest('hex')})}
const result={pass:!errors.length&&rows.every(r=>r.status===200&&r.font&&r.firstSize[0]===1280&&r.firstSize[1]===720)&&pdfs.every(r=>r.status===200&&r.matchesSource),rows,pdfs,errors};await fs.writeFile('review/production-audit.json',JSON.stringify(result,null,2));console.log(JSON.stringify(result));await browser.close();if(!result.pass)process.exit(1);
