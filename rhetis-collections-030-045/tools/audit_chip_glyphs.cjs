// Measure the painted glyph bounds, rather than the font line box, in pure-text capsules.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const ROOT=path.resolve(__dirname,'..');
const names=process.argv.slice(2).length?process.argv.slice(2):['chalkline','undertow','cutplane','skylight','arrowtab','blockweave'];
(async()=>{
 const server=http.createServer((req,res)=>{const f=path.resolve(ROOT,'.'+decodeURIComponent(req.url.split('?')[0]));if(!f.startsWith(ROOT+'/')){res.writeHead(403);res.end();return;}fs.readFile(f,(e,d)=>{if(e){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.css':'text/css','.woff2':'font/woff2','.woff':'font/woff'})[path.extname(f)]||'application/octet-stream');res.end(d);});});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});const report=[];
 const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
 for(const name of names){let records=[];
  for(const kind of ['replica','reassembled','library']){
   const dir=path.join(ROOT,'reviews',name+'-review',kind);const files=fs.readdirSync(dir).filter(f=>f.endsWith('.html')&&(kind==='library'?['light.html','dark.html'].includes(f):f!=='index.html'));
   for(const file of files){await page.goto(origin+'/reviews/'+name+'-review/'+kind+'/'+file);await page.evaluate(()=>document.fonts.ready);
    const glyphs=await page.evaluate(()=>{
     const ctx=document.createElement('canvas').getContext('2d');let result=[];
     for(const chip of document.querySelectorAll('.slide .pill,.slide .tag,.slide .chip,.slide button')){
      if(chip.closest('button')!==chip&&chip.closest('button'))continue;
      if(chip.querySelector('.icon,[data-icon],.mark,svg,img,.seat'))continue;
      const box=chip.getBoundingClientRect(),cs=getComputedStyle(chip);if(box.width<1||box.height<1||cs.display==='contents')continue;
      let bounds=[],walker=document.createTreeWalker(chip,NodeFilter.SHOW_TEXT),lines=0;
      for(let t;t=walker.nextNode();){if(!t.textContent.trim())continue;const el=t.parentElement,st=getComputedStyle(el);if(st.visibility==='hidden')continue;
       const rg=document.createRange();rg.selectNodeContents(t);const rs=[...rg.getClientRects()].filter(r=>r.width&&r.height);if(rs.length!==1){lines+=rs.length;continue;}lines++;
       ctx.font=[st.fontStyle,st.fontWeight,st.fontSize,st.fontFamily].join(' ');ctx.letterSpacing=st.letterSpacing;const m=ctx.measureText(t.textContent),r=rs[0];
       const scale=r.height/((m.fontBoundingBoxAscent||0)+(m.fontBoundingBoxDescent||0));if(!Number.isFinite(scale)||scale<=0)continue;
       bounds.push({l:r.left-m.actualBoundingBoxLeft*scale,r:r.left+m.actualBoundingBoxRight*scale,t:r.top+(m.fontBoundingBoxAscent-m.actualBoundingBoxAscent)*scale,b:r.top+(m.fontBoundingBoxAscent+m.actualBoundingBoxDescent)*scale});
      }
      if(!bounds.length||lines!==1)continue;
      const l=Math.min(...bounds.map(b=>b.l)),r=Math.max(...bounds.map(b=>b.r)),t=Math.min(...bounds.map(b=>b.t)),b=Math.max(...bounds.map(b=>b.b));
      const dx=((l+r-box.left-box.right)/2),dy=((t+b-box.top-box.bottom)/2);
      // Inline labels use their text box as a marker. Capsules with a visible face/border are centred.
      const visibleFace=cs.backgroundColor!=='rgba(0, 0, 0, 0)'||parseFloat(cs.borderTopWidth)>0||cs.backgroundImage!=='none';
      result.push({text:chip.textContent.trim().slice(0,70),className:chip.className,box:[+box.width.toFixed(2),+box.height.toFixed(2)],dx:+dx.toFixed(2),dy:+dy.toFixed(2),visibleFace,candidate:visibleFace&&(Math.abs(dx)>3.5||Math.abs(dy)>3.5)});
     }return result;
    });records.push({kind,page:file,glyphs});
   }
  }
  report.push({collection:name,records});console.log(name,'capsules',records.reduce((n,x)=>n+x.glyphs.length,0),'candidates',records.reduce((n,x)=>n+x.glyphs.filter(g=>g.candidate).length,0));
 }
 await page.close();await browser.close();server.close();fs.writeFileSync(path.join(ROOT,'checks/integration-chip-glyphs-audit.json'),JSON.stringify(report,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
