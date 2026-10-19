import {chromium} from 'playwright-core';import fs from 'node:fs/promises';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});const page=await browser.newPage({viewport:{width:1280,height:720}});page.on('pageerror',console.error);
for(let n=9;n<=14;n++){await page.goto(`http://127.0.0.1:5173/?deck=009&slide=slide_${n.toString().padStart(2,'0')}&mode=single`,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:`renders/review1/009-slide_${n.toString().padStart(2,'0')}.png`});}await browser.close();
