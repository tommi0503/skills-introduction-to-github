import {readFile,writeFile} from 'node:fs/promises'
import path from 'node:path'
export async function loadManifest(root) {
 const input=JSON.parse(await readFile(path.join(root,'review/input-image-manifest.json'),'utf8'))
 const arrays=await Promise.all(['a','b','c'].map(async g=>{
  try{return JSON.parse(await readFile(path.join(root,`public/reference/groups/${g}.json`),'utf8'))}
  catch(e){if(e.code==='ENOENT')return [];throw e}
 }))
 const manifest=arrays.flat().sort((a,b)=>a.id.localeCompare(b.id)).map(d=>({...d,originalDeck:Number(d.id.slice(1)),sourceTitle:input.find(r=>r.id===Number(d.id.slice(1)))?.title}))
 if(new Set(manifest.map(d=>d.id)).size!==manifest.length)throw Error('Overlapping deck ownership')
 for(const d of manifest)if(new Set(d.slides.map(s=>s.id)).size!==d.slides.length)throw Error(`Duplicate slide IDs ${d.id}`)
 return manifest
}
export async function saveManifest(root) {
 const manifest=await loadManifest(root)
 await writeFile(path.join(root,'public/reference/manifest.json'),JSON.stringify(manifest,null,2)+'\n')
 return manifest
}
