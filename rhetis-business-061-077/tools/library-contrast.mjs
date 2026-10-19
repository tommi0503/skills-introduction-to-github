import path from 'node:path';import{fileURLToPath}from'node:url';
import {chromium} from 'playwright';import fs from 'node:fs';
const base=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});const page=await browser.newPage({viewport:{width:1440,height:1000}});let report=[];
for(const mode of ['light','dark']){
 await page.setContent(fs.readFileSync(base+'/collection/business-prism/'+mode+'.html','utf8'));
 const result=await page.evaluate(()=>{
 function rgba(s){let a=s.match(/[\d.]+/g);if(!a)return [0,0,0,0];if(a.length===3)a.push(1);a=a.map(Number);if(s.startsWith('color(srgb'))a=a.map((v,i)=>i<3?v*255:v);return a}
 function composite(f,b){return [0,1,2].map(i=>f[i]*f[3]+b[i]*(1-f[3])).concat(1)}
 function bg(n){let p=n.parentElement;return composite(rgba(getComputedStyle(n).backgroundColor),p?bg(p):[255,255,255,1])}
 function luminance(c){return c.slice(0,3).map(v=>v/255).map(v=>v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4)).reduce((v,s,i)=>v+s*[.2126,.7152,.0722][i],0)}
 let all=[];document.querySelectorAll('article').forEach((article,index)=>{let failures=[];for(const el of article.querySelectorAll('.slide *')){const cs=getComputedStyle(el);if(!el.getClientRects().length||cs.display==='none')continue;for(const child of el.childNodes){if(child.nodeType!==Node.TEXT_NODE||!child.textContent.trim())continue;const a=luminance(composite(rgba(cs.color),bg(el))),b=luminance(bg(el));const ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);const minimum=parseFloat(cs.fontSize)>=28?3:4.5;if(ratio+0.01<minimum)failures.push({text:child.textContent,color:cs.color,bg:bg(el),size:cs.fontSize,ratio,minimum});}}all.push({index:index+1,label:article.querySelector('h2').textContent,failures})});return all;
 });report.push({mode,result});console.log(mode,JSON.stringify(result.filter(x=>x.failures.length),null,2));
}
fs.writeFileSync(base+'/review/library-contrast.json',JSON.stringify(report,null,2));await browser.close();
