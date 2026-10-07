import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {mkdir,readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {execFileSync} from 'node:child_process'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
import {auditPage} from './browser-audit.mjs'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');process.chdir(root);
const args=process.argv.slice(2),round=args.find(a=>a.startsWith('--round='))?.slice(8)??'final',ids=args.filter(a=>!a.startsWith('--'));
if(!/^[a-z0-9-]+$/.test(round))throw Error('Invalid round');
const hash=s=>createHash('sha256').update(s).digest('hex');
export const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','src/fonts.ts','scripts/browser-audit.mjs'];
const rendererHash=hash((await Promise.all(rendererFiles.map(f=>readFile(f,'utf8')))).join('\n'));
await mkdir(`renders/${round}`,{recursive:true});await mkdir(`comparisons/${round}`,{recursive:true});
const server=await createServer({root,server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen();
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
try{
 const page=await browser.newPage({viewport:{width:1280,height:720}}),errors=[],failedAssets=[];
 page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>failedAssets.push(r.url()));page.on('response',r=>{if(r.status()>=400&&!r.url().endsWith('/favicon.ico'))failedAssets.push(r.url())});
 const url=`http://127.0.0.1:${server.httpServer.address().port}`;await page.goto(url,{waitUntil:'networkidle'});
 const brochures=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.brochures});
 const selected=brochures.filter(b=>!ids.length||ids.includes(b.id));
 if(!selected.length||ids.some(id=>!selected.some(b=>b.id===id)))throw Error('Requested brochure missing');
 for(const b of selected){
  if(b.sides.some(s=>!s.elements.length))throw Error(`Implementation pending ${b.id}`);
  const meta={id:b.id,title:b.title,round,definitionHash:hash(JSON.stringify(b)),rendererHash,panels:[],sides:[],notes:b.sides.flatMap(s=>s.notes),capturedAt:new Date().toISOString()};
  for(const [mode,sheets] of [['page',b.panels],['side',b.sides]])for(const sheet of sheets){
   await page.goto(`${url}/#/${mode}/${b.id}/${sheet.id}`,{waitUntil:'networkidle'});
   await page.locator('[data-page][data-fonts-ready="true"]').waitFor();await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))});
   const audit=await auditPage(page);const file=`renders/${round}/${b.id}-${sheet.id}.png`;
   await page.locator('[data-page]').screenshot({path:file});
   const reference=`public/${sheet.reference}`;
   meta[mode==='page'?'panels':'sides'].push({id:sheet.id,title:sheet.title??sheet.id,file,reference,size:sheet.size,crop:sheet.crop,canvas:audit.size,findings:audit.issues,fontChecks:audit.fontChecks,chipCount:audit.chipCount,placeholderCount:audit.placeholderCount,replacementCount:audit.replacementCount,pngSha256:hash(await readFile(file)),referenceSha256:hash(await readFile(reference))});
  }
  if(errors.length||failedAssets.length)throw Error(JSON.stringify({errors,failedAssets}));
  await writeFile(`comparisons/${round}/${b.id}.json`,JSON.stringify(meta,null,2)+'\n');
  execFileSync('python3',['scripts/compare.py',b.id,round],{stdio:'inherit'});
  const findings=[...meta.panels,...meta.sides].flatMap(s=>s.findings).filter(f=>!f.expectedClip);
  console.log(`${b.id}: ${meta.panels.length} panels + ${meta.sides.length} unfolded / ${findings.length} unexpected findings`);
 }
}finally{await browser.close();await server.close();}
