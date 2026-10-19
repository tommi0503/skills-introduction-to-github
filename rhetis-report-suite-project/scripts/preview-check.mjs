import {createServer} from 'node:http';
import {readFile, stat, writeFile} from 'node:fs/promises';
import {resolve, extname, sep} from 'node:path';
import {fileURLToPath} from 'node:url';
import {chromium} from 'playwright-core';

const root=fileURLToPath(new URL('../',import.meta.url));
const mime={'.html':'text/html; charset=utf-8','.jpg':'image/jpeg','.png':'image/png','.pdf':'application/pdf'};
const server=createServer(async(req,res)=>{
  try {
    const path=resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://local').pathname));
    if(!path.startsWith(root.replace(/\/$/,'')+sep))throw Error('Outside project');
    const bytes=await readFile(path);res.writeHead(200,{'Content-Type':mime[extname(path)]||'application/octet-stream'});res.end(bytes);
  } catch {res.writeHead(404);res.end('Not found');}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
const origin=`http://127.0.0.1:${server.address().port}`;
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
page.on('pageerror',e=>errors.push(e.message));
page.on('requestfailed',r=>errors.push(r.url()+': '+r.failure()?.errorText));
try {
  await page.goto(origin+'/artifacts/preview.html',{waitUntil:'load'});
  const cards=await page.locator('.slide-card').count();
  const links=await page.locator('a').evaluateAll(a=>a.map(x=>new URL(x.href).pathname));
  const missing=[];for(const path of new Set(links)){try{await stat(resolve(root,'.'+path));}catch{missing.push(path)}}
  const images=await page.locator('img').count();
  const imageFailures=await page.locator('img').evaluateAll(async images=>{
    await Promise.all(images.map(img=>new Promise(r=>{img.loading='eager';if(img.complete)return r();img.onload=r;img.onerror=r;})));
    return images.filter(img=>!img.naturalWidth||img.naturalWidth!==1280||img.naturalHeight!==720).map(img=>img.getAttribute('src'));
  });
  await page.locator('#search').fill('005 slide_08');
  const searchCount=await page.locator('.slide-card:not(.hidden)').count();
  await page.locator('#search').fill('');await page.locator('button[data-view="assembled"]').click();
  const mode=await page.locator('body').getAttribute('data-view');
  await page.screenshot({path:resolve(root,'work/offline-preview-check.png')});
  const report={status:cards===121&&images===242&&searchCount===1&&mode==='assembled'&&!missing.length&&!errors.length&&!imageFailures.length?'passed':'failed',method:'Static HTML served locally; file:// navigation is disabled by the managed browser policy.',cards,images,uniqueLinks:new Set(links).size,missing,imageFailures,errors,searchCount,mode};
  await writeFile(resolve(root,'review/static-preview-verification.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));if(report.status!=='passed')process.exitCode=1;
} finally {await browser.close();await new Promise(r=>server.close(r));}
