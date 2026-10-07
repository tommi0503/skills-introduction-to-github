import {readFile,readdir} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'
export const rendererFiles=['src/main.tsx','src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','scripts/audit.mjs']
const hash=value=>createHash('sha256').update(value).digest('hex')
export async function rendererHashFor(root='.'){
 async function graphics(dir){const out=[];for(const e of await readdir(path.join(root,dir),{withFileTypes:true})){const f=`${dir}/${e.name}`;if(e.isDirectory())out.push(...await graphics(f));else out.push(f)}return out}
 const files=[...rendererFiles,...await graphics('src/graphics')].sort()
 return hash((await Promise.all(files.map(f=>readFile(path.join(root,f),'utf8')))).join('\n'))
}
export async function buildState(){
 async function walk(dir){const out=[];for(const e of await readdir(dir,{withFileTypes:true})){const f=`${dir}/${e.name}`;if(e.isDirectory())out.push(...await walk(f));else if(!e.name.endsWith('-seed.json'))out.push(f)}return out}
 const files=[...await walk('src'),...await walk('public/reference/groups'),'package.json','package-lock.json','index.html','tsconfig.json','vite.config.ts','scripts/audit.mjs'].sort()
 const entries=await Promise.all(files.map(async f=>[f,hash(await readFile(f))]))
 return {sourceHash:hash(JSON.stringify(entries)),rendererHash:await rendererHashFor(),files:Object.fromEntries(entries)}
}
