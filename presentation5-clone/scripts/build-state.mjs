import {readFile,readdir} from 'node:fs/promises'
import {createHash} from 'node:crypto'
export const rendererFiles=['src/main.tsx','src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','scripts/audit.mjs']
const hash=value=>createHash('sha256').update(value).digest('hex')
export async function buildState(){
 async function walk(dir){const out=[];for(const e of await readdir(dir,{withFileTypes:true})){const f=`${dir}/${e.name}`;if(e.isDirectory())out.push(...await walk(f));else if(!e.name.endsWith('-seed.json'))out.push(f)}return out}
 const files=[...await walk('src'),...await walk('public/reference/groups'),'package.json','package-lock.json','index.html','tsconfig.json','vite.config.ts','scripts/audit.mjs'].sort()
 const entries=await Promise.all(files.map(async f=>[f,hash(await readFile(f))]))
 return {sourceHash:hash(JSON.stringify(entries)),rendererHash:hash((await Promise.all(rendererFiles.map(f=>readFile(f,'utf8')))).join('\n')),files:Object.fromEntries(entries)}
}
