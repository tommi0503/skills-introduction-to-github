import fs from 'node:fs/promises';
import crypto from 'node:crypto';
const hash=x=>crypto.createHash('sha256').update(x).digest('hex');
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {renderSlide,documentHTML} from '../src/renderer.mjs';
import {renderAssembly,assemblyDocument} from '../src/assembly-renderer.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');process.chdir(root);
const args=process.argv.slice(2),selected=args.includes('--deck')?args[args.indexOf('--deck')+1]:null;
const files=(await fs.readdir('src/decks')).filter(f=>f.endsWith('.mjs')&&(!selected||f===selected+'.mjs'));
let manifest=[],css='',libraryReady=false;
try{
 const c='collection/blueprint-06';css=await fs.readFile(c+'/kit/css/tokens.css','utf8');css+='\n'+await fs.readFile(c+'/foundation/foundation.css','utf8');
 const defaults={};for(const folder of await fs.readdir(c+'/elements')){css+='\n'+await fs.readFile(c+'/elements/'+folder+'/element.css','utf8');Object.assign(defaults,JSON.parse(await fs.readFile(c+'/elements/'+folder+'/element.json','utf8')).tokenDefaults)}
 const steps=JSON.parse(await fs.readFile('contract/type-steps.json'));css+='\n.slide{'+steps.map(n=>`--type-${n}:${n}px`).join(';')+';'+Object.entries(defaults).map(([k,v])=>`${k}:${v}`).join(';')+'}';libraryReady=true;
}catch(e){if(!selected)console.log('Library assembly not yet ready:',e.message)}
for(const file of files){
 const deck=(await import(path.resolve('src/decks/'+file)+'?t='+Date.now())).default;
 if(!deck.slides?.length)throw Error('Empty deck '+file);
 const dir=`build/replica/${deck.id}`;await fs.mkdir(dir,{recursive:true});
 for(const s of deck.slides){if(s.elements.some(n=>!Number.isFinite(n.x)||!Number.isFinite(n.y)))throw Error('Invalid coordinate '+deck.id+'/'+s.id);await fs.writeFile(`${dir}/${s.id}.html`,documentHTML(`${deck.title} — ${s.title}`,renderSlide(deck,s)))}
 await fs.writeFile(`${dir}/all.html`,documentHTML(deck.title,deck.slides.map(s=>renderSlide(deck,s)).join('')));
 let assembled=0;
 if(libraryReady){
  let data;try{data=(await import(path.resolve('src/assembly/'+file)+'?t='+Date.now())).default}catch(e){if(e.code!=='ERR_MODULE_NOT_FOUND')throw e;}
  if(data){
   if(data.length!==deck.slides.length)throw Error('Assembly count mismatch '+deck.id);
   const out=`build/assembly/${deck.id}`;await fs.mkdir(out,{recursive:true});
   for(const s of data)await fs.writeFile(`${out}/${s.id}.html`,assemblyDocument(`${deck.title} — ${s.title}`,renderAssembly(deck,s),css));
   await fs.writeFile(`${out}/all.html`,assemblyDocument(deck.title,data.map(s=>renderAssembly(deck,s)).join(''),css));assembled=data.length;
  }
 }
 manifest.push({id:deck.id,title:deck.title,assemblyCount:assembled,builtSourceHash:hash(await fs.readFile('src/decks/'+file)),builtAssemblySourceHash:assembled?hash(await fs.readFile('src/assembly/'+file)):null,slides:deck.slides.map(s=>({id:s.id,title:s.title,nodes:s.elements.length}))});console.log(deck.id,deck.slides.length,'replica;',assembled,'semantic assembly');
}
if(!selected)await fs.writeFile('build/manifest.json',JSON.stringify(manifest,null,2));
