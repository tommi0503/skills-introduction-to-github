import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {writeFile,readFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
try{
 const page=await browser.newPage();await page.goto(`http://127.0.0.1:${server.httpServer.address().port}`,{waitUntil:'networkidle'})
 const audit=await page.evaluate(async()=>{
  const {brochures}=await import('/src/registry.ts'),{resolveFont}=await import('/src/fonts.ts'),requests=new Map(),findings=[]
  for(const b of brochures)for(const side of b.sides)for(const e of side.elements){
   if(e.kind!=='text'||!e.text?.trim())continue
   const glyphs=new Set([e.text.match(/[가-힣]/)?.[0],e.text.match(/[A-Za-z0-9]/)?.[0]].filter(Boolean))
   if(!glyphs.size)glyphs.add(e.text.trim()[0])
   for(const glyph of glyphs){
    const family=resolveFont(e.font),weight=e.weight??400,style=e.fontStyle??'normal',key=JSON.stringify([family,weight,style,glyph])
    const r=requests.get(key)??{family,weight,style,glyph,uses:[],text:e.text.slice(0,80)}
    r.uses.push(`${b.id}/${side.id}`);requests.set(key,r)
   }
  }
  for(const r of requests.values()){
   const faces=await document.fonts.load(`${r.style} ${r.weight} 20px ${r.family}`,r.glyph)
   const loaded=faces.filter(f=>f.status==='loaded')
   const coversWeight=f=>{const weights=f.weight.split(' ').map(Number);return weights.length===2?r.weight>=weights[0]&&r.weight<=weights[1]:r.weight===weights[0]}
   const reasons=[]
   if(!loaded.length)reasons.push('declared family does not cover sample glyph')
   if(loaded.length&&!loaded.some(coversWeight))reasons.push('declared weight uses a different font face')
   if(loaded.length&&!loaded.some(f=>f.style===r.style||f.style.includes(r.style)))reasons.push('declared style uses a different font face')
   if(reasons.length)findings.push({...r,uses:[...new Set(r.uses)],reasons,loadedFaces:loaded.map(f=>({family:f.family,weight:f.weight,style:f.style}))})
  }
  const digest=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(JSON.stringify(brochures)))
  return{definitionHash:[...new Uint8Array(digest)].map(x=>x.toString(16).padStart(2,'0')).join(''),requests:requests.size,findings}
 })
 const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','src/fonts.ts']
 audit.rendererHash=createHash('sha256').update((await Promise.all(rendererFiles.map(f=>readFile(f,'utf8')))).join('\n')).digest('hex')
 audit.status=audit.findings.length?'failed':'passed'
 await writeFile('review/font-verification.json',JSON.stringify(audit,null,2));console.log(JSON.stringify(audit,null,2))
 if(audit.findings.length)throw Error('Actual font face coverage/weight/style validation failed')
}finally{await browser.close();await server.close()}
