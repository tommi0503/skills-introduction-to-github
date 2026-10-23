const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const ROOT=path.resolve(__dirname,'../collections');
const names=process.argv.slice(2).length?process.argv.slice(2):['chalkline','undertow','cutplane','skylight','arrowtab','blockweave'];
(async()=>{const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',args:['--no-sandbox']});const page=await browser.newPage();const report=[];
 for(const name of names){const base=path.join(ROOT,name),fixtures=[];
  for(const folder of fs.readdirSync(path.join(base,'elements')))for(const f of fs.readdirSync(path.join(base,'elements',folder,'fixtures')))if(f.endsWith('.html'))fixtures.push({folder,file:f,html:fs.readFileSync(path.join(base,'elements',folder,'fixtures',f),'utf8')});
  const css=fs.readFileSync(path.join(base,'foundation/foundation.css'),'utf8');
  const issues=await page.evaluate(({fixtures,css})=>{
   document.head.innerHTML='';document.body.innerHTML='';const style=document.createElement('style');style.textContent=css;document.head.append(style);const rules=[];
   function walk(rs){for(const r of rs)if(r.selectorText)rules.push(r);else if(r.cssRules)walk(r.cssRules);}walk(style.sheet.cssRules);
   const layoutOnly=new Set(['box-sizing','min-width','min-height','flex','flex-grow','flex-shrink','flex-basis','container-type','container-name','grid-column','grid-row']);const out=[];
   for(const f of fixtures){document.body.innerHTML='<section class="slide"><div class="page"><div class="body">'+f.html+'</div></div></section>';
    for(const root of document.querySelectorAll('[data-el]'))for(const rule of rules){try{if(!root.matches(rule.selectorText))continue;}catch{continue;}const props=[...rule.style].filter(p=>!layoutOnly.has(p));if(props.length)out.push({folder:f.folder,fixture:f.file,root:root.getAttribute('data-el'),selector:rule.selectorText,properties:props});}
   }return [...new Map(out.map(x=>[JSON.stringify(x),x])).values()];
  },{fixtures,css});report.push({collection:name,fixtureCount:fixtures.length,issues});console.log(name,issues.length,'foundation root scope candidates');
 }
 await browser.close();fs.writeFileSync(path.resolve(__dirname,'../checks/integration-foundation-audit.json'),JSON.stringify(report,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
