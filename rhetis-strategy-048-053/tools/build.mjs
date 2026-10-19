import fs from 'node:fs/promises';
import path from 'node:path';
import {collectionType} from '../src/ui/collection-adapter.js';
import {renderSlide} from '../src/ui/renderer.js';
const root=path.resolve(new URL('..',import.meta.url).pathname),c=path.join(root,'strategy-blueprint');
const cssPaths=[path.join(c,'kit/css/tokens.css'),path.join(c,'foundation/foundation.css'),...(await fs.readdir(path.join(c,'elements'))).sort().map(d=>path.join(c,'elements',d,'element.css'))];
let lib=(await Promise.all(cssPaths.map(p=>fs.readFile(p,'utf8')))).join('\n');
const steps=JSON.parse(await fs.readFile(path.join(root,'contract/type-steps.json'),'utf8'));lib+='\n.slide{'+steps.map(n=>`--type-${n}:${n}px;`).join('')+'}\n';
await fs.writeFile(path.join(root,'library.css'),lib);
let base=await fs.readFile(path.join(root,'src/style.css'),'utf8');for(const [file,mime] of [['PretendardVariable.woff2','font/woff2'],['BlackHanSans-Regular.ttf','font/ttf'],['NotoSansCJKkr-Regular.woff','font/woff2'],['NotoSansCJKkr-Bold.woff','font/woff2']]){base=base.replaceAll('../public/fonts/'+file,'data:'+mime+';base64,'+(await fs.readFile(path.join(root,'public/fonts',file))).toString('base64'));}
const all=[];for(const d of ['048','049','050','051','052','053']){const {slides}=await import('../src/decks/d'+d+'.js');for(const s of slides){if(!s.id.startsWith(d+'-'))throw new Error('Invalid slide id '+s.id);all.push(s);}}
const controls=`<nav><b>Strategy Blueprint</b><select id="deck"><option value="all">전체 105장</option>${['048','049','050','051','052','053'].map(d=>'<option>'+d+'</option>').join('')}</select><button id="size">크게 보기</button><a href="light.html">라이브러리 Light</a><a href="dark.html">Dark</a><span>1280 × 720</span></nav>`;
const galleryCss=`body{background:#e8ecf2;color:#20334f}nav{position:sticky;top:0;z-index:100;display:flex;align-items:center;gap:16px;padding:18px 24px;background:#fff;border-bottom:1px solid #c8d1df;font:15px Pretendard,sans-serif}nav a{color:#3454ae}nav span{margin-left:auto;color:#64748b}nav button,nav select{font:inherit;border:1px solid #c8d1df;background:#f6f8fc;border-radius:6px;padding:7px 12px}.gallery{display:grid;grid-template-columns:repeat(auto-fit,640px);gap:24px;padding:24px}.tile{width:640px}.tile h2{font:14px Pretendard,sans-serif;margin:0 0 8px}.tile>.viewport{width:640px;height:360px;overflow:hidden;background:white;box-shadow:0 5px 16px #172d4912}.viewport>.slide{transform:scale(.5);transform-origin:0 0}body.large .gallery{grid-template-columns:1280px}body.large .tile,body.large .viewport{width:1280px}body.large .viewport{height:720px}body.large .viewport>.slide{transform:none}.tile[hidden]{display:none}@media print{nav,.tile h2{display:none}.gallery{display:block;padding:0}.tile,.tile>.viewport{width:1280px;height:720px;box-shadow:none}.viewport>.slide{transform:none}.tile{break-after:page}}`;
const galleryScript=`document.querySelector('#deck').onchange=e=>document.querySelectorAll('.tile').forEach(t=>t.hidden=e.target.value!=='all'&&t.dataset.deck!==e.target.value);document.querySelector('#size').onclick=()=>{document.body.classList.toggle('large');};window.__ready=true;`;
for(const mode of ['direct','assembled']){
const markup=all.map(s=>`<article class="tile" data-deck="${s.id.slice(0,3)}"><h2>${s.id}</h2><div class="viewport">${renderSlide(s,mode)}</div></article>`).join('');
const html=`<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rhetis 048–053 · ${mode}</title><style>${mode==='assembled'?lib:''}</style><style>${base}</style><style>${galleryCss}</style></head><body>${controls}<main class="gallery">${markup}</main><script>${galleryScript}</script></body></html>`;
await fs.writeFile(path.join(root,mode==='direct'?'preview.html':'assembled-preview.html'),html);
}
await fs.mkdir(path.join(root,'artifacts'),{recursive:true});await fs.writeFile(path.join(root,'artifacts/scene-data.json'),JSON.stringify(all));
const trace=[];function walk(nodes,prefix){nodes.forEach((n,i)=>{const loc=prefix+'/'+i,t=collectionType(n);trace.push({node:loc,kind:n.kind,contract:t.contract,source:'strategy-blueprint/elements/'+t.folder,geometry:[n.x,n.y,n.w,n.h]});if(n.children)walk(n.children,loc);});}all.forEach(s=>walk(s.nodes,s.id));await fs.writeFile(path.join(root,'artifacts/assembly-trace.json'),JSON.stringify(trace,null,2));
console.log('Build passed:',all.length,'slides;',cssPaths.length,'library CSS sources; standalone previews built.');

await fs.writeFile(path.join(root,'artifacts/build-audit.json'),JSON.stringify({success:true,slides:all.length,libraryCssSources:cssPaths.length,runtime:'native HTML/CSS/SVG; no build-time image flattening'},null,2));
