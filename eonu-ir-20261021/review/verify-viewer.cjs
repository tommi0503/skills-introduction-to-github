const {chromium}=require('playwright');
const http=require('node:http'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..');
(async()=>{
const server=http.createServer((req,res)=>{let pathname=decodeURIComponent(req.url.split('?')[0]);if(pathname==='/')pathname='/index.html';const file=path.join(root,pathname);const ext=path.extname(file);res.setHeader('Content-Type',({'.html':'text/html','.js':'application/javascript','.css':'text/css','.woff2':'font/woff2','.json':'application/json'})[ext]||'application/octet-stream');fs.createReadStream(file).on('error',()=>{res.statusCode=404;res.end()}).pipe(res)});await new Promise(r=>server.listen(0,'127.0.0.1',r));
const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
const page=await b.newPage({viewport:{width:1440,height:900}});const errors=[],failed=[],checks=[];const origin=`http://127.0.0.1:${server.address().port}`;
page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>failed.push(r.url()));
const check=async(v,m)=>{if(!await v)throw Error(m);checks.push(m)};
try{
await page.goto(origin+'/index.html');await page.locator('.slide').waitFor();await page.evaluate(()=>document.fonts.ready);
await check((await page.locator('#slide-host .slide').getAttribute('data-slide'))==='01','default design page 01');
await check(page.locator('#previous').isDisabled(),'previous disabled at start');
for(const theme of ['design','wireframe']){
for(let i=1;i<=12;i++){
const id=String(i).padStart(2,'0');await page.goto(origin+`/index.html#/${theme}/${id}`);await page.waitForFunction(({id,theme})=>document.querySelector('#slide-host .slide')?.dataset.slide===id&&document.querySelector('#slide-host .slide')?.classList.contains(theme),{id,theme});await page.evaluate(()=>document.fonts.ready);
const size=await page.locator('#slide-host .slide').evaluate(el=>({w:el.offsetWidth,h:el.offsetHeight}));await check(size.w===1280&&size.h===720,`viewer ${theme}/${id} canvas`);
await check((await page.locator('#single-link').getAttribute('href'))===`${theme}/${id}.html`,`viewer ${theme}/${id} source link`);
}
}
await page.goto(origin+'/index.html#/design/01');await page.waitForFunction(()=>document.querySelector('#slide-host .slide').dataset.slide==='01');
await page.keyboard.press('ArrowRight');await page.waitForFunction(()=>location.hash==='#/design/02'&&document.querySelector('#slide-host .slide').dataset.slide==='02');checks.push('keyboard right');
await page.getByRole('button',{name:'와이어프레임',exact:true}).click();await page.waitForFunction(()=>location.hash==='#/wireframe/02'&&document.querySelector('#slide-host .slide').classList.contains('wireframe'));checks.push('mode switch retains page');
await page.keyboard.press('End');await page.waitForFunction(()=>location.hash.endsWith('/12')&&document.getElementById('next').disabled);checks.push('End and next disabled');
await page.keyboard.press('Home');await page.waitForFunction(()=>location.hash.endsWith('/01')&&document.getElementById('previous').disabled);checks.push('Home and previous disabled');
await page.locator('#page-select').selectOption('5');await page.waitForFunction(()=>location.hash.endsWith('/06'));checks.push('page dropdown');
await page.locator('#grid-toggle').click();await check((await page.locator('.viewer-grid-card').count())===12,'grid has 12 actual slide previews');
await page.locator('.viewer-grid-card').nth(6).click();await page.waitForFunction(()=>location.hash==='#/wireframe/07'&&document.querySelector('#slide-host .slide').dataset.slide==='07');checks.push('grid card opens page');
await page.locator('#notes-toggle').click();await check(page.locator('#notes').isVisible(),'notes open');
await check(page.evaluate(()=>document.getElementById('notes-text').textContent===window.EONU.slides[6].talk),'notes match current slide');
await page.keyboard.press('Escape');await check(page.locator('#notes').isHidden(),'Escape closes notes');
await check((await page.locator('#print-link').getAttribute('href'))==='wireframe/print.html','print link retains mode');
await check((await page.locator('#pdf-link').getAttribute('href'))==='previews/eonu-wireframe.pdf','PDF link retains mode');
await check((await page.locator('#planning-link').getAttribute('href'))==='docs/planning.html','planning link');
await page.setViewportSize({width:390,height:844});await page.waitForTimeout(100);
const mobile=await page.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth,slide:document.getElementById('slide-wrap').getBoundingClientRect().toJSON()}));await check(mobile.width<=mobile.viewport,'390px viewer no horizontal overflow');
await page.screenshot({path:path.join(root,'review/viewer-mobile.png'),fullPage:true});
await page.keyboard.press('g');await page.waitForTimeout(100);await check(page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'390px grid no horizontal overflow');
await page.keyboard.press('Escape');
await page.setViewportSize({width:1280,height:800});
await page.goto(origin+'/index.html#/design/01');await page.waitForFunction(()=>document.querySelector('#slide-host .slide').dataset.slide==='01');await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(root,'review/viewer-desktop.png'),fullPage:true});
const standalone=[];
for(const theme of ['design','wireframe']){
for(let i=1;i<=12;i++){
const id=String(i).padStart(2,'0');await page.goto(origin+`/${theme}/${id}.html`);await page.locator('.slide').waitFor();await page.evaluate(()=>document.fonts.ready);await check((await page.locator('.slide').count())===1&&await page.locator('.slide').getAttribute('data-slide')===id,`standalone ${theme}/${id}`);
const fontLoaded=await page.evaluate(()=>document.fonts.check('20px Pretendard'));await check(fontLoaded,`font ${theme}/${id}`);
standalone.push({theme,id,html:true,fontLoaded});
}
await page.goto(origin+`/${theme}/print.html`);await check((await page.locator('.print-deck>.slide').count())===12,`print ${theme} has 12 slides`);
}
await page.setViewportSize({width:390,height:844});await page.goto(origin+'/design/01.html');await page.waitForTimeout(100);const standaloneMobile=await page.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth}));await check(standaloneMobile.width<=standaloneMobile.viewport,'390px standalone no horizontal overflow');
await check(errors.length===0,'no browser page errors');await check(failed.length===0,'no failed resource requests');
const report={status:'passed',testedAt:new Date().toISOString(),browser:'Chromium /usr/bin/chromium',transport:'localhost HTTP',fileProtocol:{status:'environment-blocked',error:'ERR_BLOCKED_BY_ADMINISTRATOR',offlineCompatibility:'Static relative HTML/CSS/classic JS and local fonts; no fetch/CDN/module runtime.'},desktop:[1440,900],mobile:[390,844],canvas:[1280,720],checks,standalone,mobileGeometry:mobile,standaloneMobile,pageErrors:errors,failedRequests:failed,sourceHashes:Object.fromEntries(['index.html','src/viewer.js','src/viewer.css','scripts/build-pages.mjs'].map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')]))};
fs.mkdirSync(path.join(root,'review'),{recursive:true});fs.writeFileSync(path.join(root,'review/viewer-check.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,checks:checks.length,standalone:standalone.length,mobile:standaloneMobile}));
}finally{await b.close();server.close()}
})().catch(e=>{console.error(e);process.exit(1)});
