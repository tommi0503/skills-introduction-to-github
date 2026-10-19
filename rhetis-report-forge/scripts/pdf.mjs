import {chromium} from 'playwright-core';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});const page=await browser.newPage({viewport:{width:1280,height:720}});
for(const kind of process.argv.slice(2).length?process.argv.slice(2):['assembled','light','dark']){
 await page.goto(`http://localhost:5173/outputs/${kind==='assembled'?'assembled':kind}.html`);await page.evaluate(()=>document.fonts.ready);
 if(kind!=='assembled')await page.addStyleTag({content:'@media print{body{display:block;margin:0;padding:0;background:white}article{margin:0;break-after:page}article:last-child{break-after:auto}h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none!important}@page{size:1280px 720px;margin:0}}'});
 await page.pdf({path:`pdfs/${kind==='assembled'?'assembled-slides':'library-'+kind}.pdf`,printBackground:true,preferCSSPageSize:true,timeout:0});console.log('PDF',kind);
}await browser.close();
