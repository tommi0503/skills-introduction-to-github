import {chromium} from 'playwright-core';
import fs from 'node:fs/promises';
const base='collection/report-forge';
const css=await fs.readFile(`${base}/kit/css/tokens.css`,'utf8')+await fs.readFile(`${base}/foundation/foundation.css`,'utf8')+await fs.readFile(`${base}/elements/chart-line/element.css`,'utf8');
const steps=JSON.parse(await fs.readFile('contract/type-steps.json','utf8'));
const files=await fs.readdir(`${base}/elements/chart-line/fixtures`);
const b=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:1280,height:720}});
for(const f of files){const fixture=await fs.readFile(`${base}/elements/chart-line/fixtures/${f}`,'utf8');const n=(fixture.match(/class="pt/g)||[]).length;
 await p.setContent(`<style>${css}.slide{${steps.map(x=>`--type-${x}:${x}px;`).join('')}}body{margin:0}</style><section class="slide"><div class="page"><div class="body">${fixture}</div></div></section>`);
 await p.screenshot({path:`review/chart-line-final-${n}.png`});
 console.log(n,await p.locator('.pt').evaluateAll(ps=>ps.map(el=>{const b=el.querySelector('b').getBoundingClientRect();const c=getComputedStyle(el,'::before'),a=getComputedStyle(el,'::after');return {value:el.style.getPropertyValue('--v'),point:[b.x+b.width/2,b.bottom],before:[c.left,c.top,c.width,c.height],after:[a.left,a.top,a.width,a.height]}})));
}
await b.close();
