// Final source-to-render reproducibility and 1280x720 page checks.
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),http=require('http'),crypto=require('crypto');
const {PNG}=require('pngjs');
const ROOT=path.resolve(__dirname,'..');const OUT=path.resolve(__dirname,'../checks/page-audit-renders');fs.mkdirSync(OUT,{recursive:true});
const names=process.argv.slice(2).length?process.argv.slice(2):['chalkline','undertow','cutplane','skylight','arrowtab','blockweave'];
(async()=>{
 const server=http.createServer((req,res)=>{let f=path.resolve(ROOT,'.'+decodeURIComponent(req.url.split('?')[0]));if(!f.startsWith(ROOT+'/')){res.writeHead(403);res.end();return;}fs.readFile(f,(e,d)=>{if(e){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.css':'text/css','.woff2':'font/woff2','.woff':'font/woff','.png':'image/png'})[path.extname(f)]||'application/octet-stream');res.end(d)});});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});let report=[];
 for(const name of names)for(const kind of ['replica','reassembled']){
  const dir=path.join(ROOT,'reviews',name+'-review',kind);if(!fs.existsSync(dir))continue;
  const files=fs.readdirSync(dir).filter(f=>f.endsWith('.html')&&!['index.html'].includes(f));
  const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
  for(const f of files){let failures=[];const handler=r=>failures.push({url:r.url(),error:r.failure()?.errorText});page.on('requestfailed',handler);
   await page.goto(origin+'/reviews/'+name+'-review/'+kind+'/'+f);await page.evaluate(()=>document.fonts.ready);
   const checks=await page.evaluate(()=>{
    const slide=(document.querySelector('.slide')||document.querySelector('body>section'));if(!slide)return {error:'missing slide'};
    const rect=slide.getBoundingClientRect();let issues=[];let fonts=new Set();let ranges=[];
    const walker=document.createTreeWalker(slide,NodeFilter.SHOW_TEXT);
    for(let t;t=walker.nextNode();){if(!t.textContent.trim())continue;const el=t.parentElement,st=getComputedStyle(el);if(st.visibility==='hidden'||st.display==='none')continue;const rg=document.createRange();rg.selectNodeContents(t);const rs=[...rg.getClientRects()].filter(r=>r.width&&r.height);if(!rs.length)continue;fonts.add(st.fontFamily);
     for(const r of rs){if(r.left<rect.left-1||r.right>rect.right+1||r.top<rect.top-1||r.bottom>rect.bottom+1)issues.push({type:'outside-page',text:t.textContent.trim().slice(0,80),className:el.className});
      let clipped=false;for(let anc=el;anc&&anc!==slide.parentElement;anc=anc.parentElement){let cs=getComputedStyle(anc),ar=anc.getBoundingClientRect();if(['hidden','clip'].includes(cs.overflowX)&&(r.left<ar.left-1||r.right>ar.right+1))clipped=true;if(['hidden','clip'].includes(cs.overflowY)&&(r.top<ar.top-1||r.bottom>ar.bottom+1))clipped=true;}
      if(clipped)issues.push({type:'clipped-text',text:t.textContent.trim().slice(0,80),className:el.className});
     }
    }
    const loadedFonts=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family);
    let chips=[];for(const el of slide.querySelectorAll('.pill,.tag,button,.chip')){let r=el.getBoundingClientRect();if(!r.width||!r.height)continue;let rg=document.createRange();rg.selectNodeContents(el);let tr=rg.getBoundingClientRect();if(tr.width)chips.push({text:el.textContent.slice(0,45),dx:(tr.left+tr.right-r.left-r.right)/2,dy:(tr.top+tr.bottom-r.top-r.bottom)/2});}
    const componentBoxes=[];
    for(const body of slide.querySelectorAll('.page>.body')){const br=body.getBoundingClientRect();
     for(const el of body.children){const r=el.getBoundingClientRect();const outside=r.left<br.left-2||r.right>br.right+2||r.top<br.top-2||r.bottom>br.bottom+2;
      componentBoxes.push({root:el.getAttribute('data-el')||el.className,x:+(r.left-br.left).toFixed(2),y:+(r.top-br.top).toFixed(2),width:+r.width.toFixed(2),height:+r.height.toFixed(2),outsideBody:outside});
      if(outside)issues.push({type:'component-outside-body',root:el.getAttribute('data-el')||el.className});
     }
    }
    return {size:[slide.clientWidth,slide.clientHeight],viewport:[innerWidth,innerHeight],fonts:[...fonts],loadedFonts,issues,chips,componentBoxes};
   });
   const fresh=await page.screenshot();const old=path.join(dir,f.replace(/\.html$/,'.png'));let diff=null;
   if(fs.existsSync(old)){const a=PNG.sync.read(fs.readFileSync(old)),b=PNG.sync.read(fresh);if(a.width===b.width&&a.height===b.height){let changed=0;for(let i=0;i<a.data.length;i+=4){if(a.data[i]!==b.data[i]||a.data[i+1]!==b.data[i+1]||a.data[i+2]!==b.data[i+2]||a.data[i+3]!==b.data[i+3])changed++;}diff={pixels:changed,fraction:changed/(a.width*a.height)};}else diff={error:'size mismatch',old:[a.width,a.height],new:[b.width,b.height]};}else diff={error:'PNG missing'};
   if(diff.pixels!==0)fs.writeFileSync(path.join(OUT,name+'-'+kind+'-'+f.replace(/\.html$/,'.png')),fresh);
   report.push({collection:name,kind,page:f,requestFailures:failures,...checks,sourceHash:crypto.createHash('sha256').update(fs.readFileSync(path.join(dir,f))).digest('hex'),renderComparison:diff});page.removeListener('requestfailed',handler);
  }
  await page.close();console.log(name,kind,files.length,'pages audited');
 }
 await browser.close();server.close();fs.writeFileSync(path.join(ROOT,'checks/integration-pages-audit.json'),JSON.stringify(report,null,2));
 console.log('PAGES',report.length,'ISSUE_PAGES',report.filter(r=>r.issues?.length||r.error).length,'RENDER_MISMATCH',report.filter(r=>r.renderComparison?.pixels!==0).length);
})().catch(e=>{console.error(e);process.exit(1)});
