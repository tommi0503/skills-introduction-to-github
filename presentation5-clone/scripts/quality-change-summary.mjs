// Report observable definition changes, independently of visual pass/fail.
import {createServer} from 'vite'
import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
const baseline=JSON.parse(await readFile('review/history/2026-10-06/baseline-deck-definitions.json','utf8'))
globalThis.window={}
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'})
const hash=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex')
const textStyle=e=>Object.fromEntries(['kind','text','runs','x','y','w','h','font','fontStyle','weight','size','letterSpacing','wordSpacing','lineHeight','align','valign'].map(k=>[k,e[k]]))
try{
 const {decks}=await server.ssrLoadModule('/src/registry.ts')
 const pages=decks.flatMap(deck=>deck.slides.map(slide=>{
  const old=baseline.find(d=>d.id===deck.id).slides.find(s=>s.id===slide.id)
  const beforeImages=old.elements.filter(e=>e.kind==='image').length,afterImages=slide.elements.filter(e=>e.kind==='image').length
  const typographyChanged=hash(old.elements.filter(e=>['text','chip'].includes(e.kind)).map(textStyle))!==hash(slide.elements.filter(e=>['text','chip'].includes(e.kind)).map(textStyle))
  return {deck:deck.id,slide:slide.id,definitionChanged:hash(old)!==hash(slide),typographyOrTextGeometryChanged:typographyChanged,
   beforePlaceholderCount:beforeImages,afterPlaceholderCount:afterImages,vectorSceneInstances:slide.elements.filter(e=>e.kind==='graphic').length,
   vectorScenes:slide.elements.filter(e=>e.kind==='graphic').map(e=>({scene:e.graphic,variant:e.variant})),beforeDefinitionSha256:hash(old),afterDefinitionSha256:hash(slide)}
 }))
 if(pages.length!==1057)throw Error('Incomplete quality scope')
 const report={qualityRevision:'2026-10-07-v2',baselineCommit:'773dda8',decks:decks.length,pages:pages.length,
  changedPages:pages.filter(p=>p.definitionChanged).length,typographyOrTextGeometryChangedPages:pages.filter(p=>p.typographyOrTextGeometryChanged).length,
  vectorSceneInstances:pages.reduce((n,p)=>n+p.vectorSceneInstances,0),pagesWithVectorScenes:pages.filter(p=>p.vectorSceneInstances).length,
  beforePlaceholderCount:pages.reduce((n,p)=>n+p.beforePlaceholderCount,0),afterPlaceholderCount:pages.reduce((n,p)=>n+p.afterPlaceholderCount,0),
  method:'Compares serialized slide definitions and text/chip geometry/style. Counts changes, not similarity or visual correctness.',slideChanges:pages}
 await writeFile('review/quality/change-summary.json',JSON.stringify(report,null,2)+'\n')
 console.log(JSON.stringify({...report,slideChanges:undefined},null,2))
}finally{await server.close()}
