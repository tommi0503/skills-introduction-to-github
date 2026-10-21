import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const {marked}=await import(require.resolve('marked'));
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
// Resolve grayscale as colors, not a CSS filter, so printed PDFs retain vector text.
const gray=s=>s.replace(/#([0-9a-f]{8}|[0-9a-f]{6}|[0-9a-f]{4}|[0-9a-f]{3})\b/gi,(_,h)=>{if(h.length<5)h=[...h].map(x=>x+x).join('');const n=Math.round(.2126*parseInt(h.slice(0,2),16)+.7152*parseInt(h.slice(2,4),16)+.0722*parseInt(h.slice(4,6),16)).toString(16).padStart(2,'0');return '#'+n+n+n+h.slice(6)});
const catalog={date:'2026-10-21',canvas:[1280,720],topics:['커버','소통의 공백','세 사람의 필요','병원 도입 가설','병원에서 시작하는 연결','데모 진행 흐름','사업 모델','시장 산정','환자에서 시작하는 확장','현재의 근거와 다음 검증','팀과 1억 원의 계획','클로징'],concepts:[]};
const fontCSS='../../../shared/base.css';
const printCSS='@page{size:1280px 720px;margin:0}html,body{margin:0;padding:0;background:#fff}.slide{break-after:page;break-inside:avoid;margin:0!important;box-shadow:none!important}.slide:last-child{break-after:auto}@media print{*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}';
const fitJS=`(()=>{const el=document.querySelector('.canvas-host');function fit(){const z=Math.min(innerWidth/1280,innerHeight/720);el.style.transform='scale('+z+')';el.style.left=((innerWidth-1280*z)/2)+'px';el.style.top=((innerHeight-720*z)/2)+'px';}addEventListener('resize',fit);fit();addEventListener('keydown',e=>{if(parent!==window){parent.postMessage({type:'eonu-key',key:e.key},'*');if(['ArrowLeft','ArrowRight','PageUp','PageDown','Home','End'].includes(e.key))e.preventDefault()}})})();`;
for(const id of 'abcdef'){
 const dir=path.join(root,'concepts',id);try{await fs.access(path.join(dir,'deck.js'))}catch{if(process.argv.includes('--partial'))continue;throw Error('Missing concept '+id)}
 const context={window:{},console};vm.createContext(context);vm.runInContext(await fs.readFile(path.join(root,'shared/content.js'),'utf8'),context);vm.runInContext(await fs.readFile(path.join(dir,'deck.js'),'utf8'),context);
 const C=context.window.CONCEPT;const meta=JSON.parse(await fs.readFile(path.join(dir,'concept.json'),'utf8'));
 if(C.slides.length!==12||typeof C.renderSlide!=='function')throw Error(id+' invalid contract');
 const slides=C.slides.map(s=>({id:s.id,title:s.title,section:s.section,talk:s.talk,note:s.note}));
 if(slides.some((s,i)=>s.id!==String(i+1).padStart(2,'0')||s.talk!==context.window.IR_CONTENT[i].talk||s.note!==context.window.IR_CONTENT[i].note))throw Error(id+' altered source notes/talk or IDs');
 catalog.concepts.push({...meta,id,slides});
 for(const mode of ['design','wireframe']){
  const theme=mode==='wireframe'?'<style>'+gray(await fs.readFile(path.join(dir,'style.css'),'utf8'))+'.slide.wireframe,.slide.wireframe *{filter:none!important}</style>':'';
  await fs.mkdir(path.join(dir,mode),{recursive:true});
  let articles=[];
  for(const s of C.slides){let html=C.renderSlide(s,mode);if(mode==='wireframe')html=gray(html);if(!html.includes('class="slide ')&&!html.includes("class='slide "))throw Error(id+' article missing');articles.push(html);
   await fs.writeFile(path.join(dir,mode,s.id+'.html'),`<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>EONU ${esc(meta.name)} · ${s.id}</title><link rel="stylesheet" href="${fontCSS}"><link rel="stylesheet" href="../style.css">${theme}<style>html,body{width:100%;height:100%;overflow:hidden;background:#fff}.canvas-host{width:1280px;height:720px;position:absolute;transform-origin:0 0}@media print{.canvas-host{transform:none!important;left:0!important;top:0!important}}${printCSS}</style></head><body><main class="canvas-host">${html}</main><script>${fitJS}</script></body></html>`);
  }
  await fs.writeFile(path.join(dir,mode,'print.html'),`<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>EONU ${esc(meta.name)} ${mode}</title><link rel="stylesheet" href="${fontCSS}"><link rel="stylesheet" href="../style.css">${theme}<style>${printCSS}</style></head><body>${articles.join('\n')}</body></html>`);
 }
 await fs.writeFile(path.join(dir,'index.html'),`<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(meta.name)} — EONU</title><script>location.replace('../../index.html#view=${id}&page=01&mode=design&layout=focus')</script><a href="../../index.html#view=${id}&page=01&mode=design&layout=focus">${esc(meta.name)} 열기</a></html>`);
}
await fs.writeFile(path.join(root,'shared/catalog.js'),'window.IR_CATALOG = '+JSON.stringify(catalog,null,2)+';\n');
await fs.writeFile(path.join(root,'review/slide-manifest.json'),JSON.stringify(catalog,null,2)+'\n');
const docs=[];for(const f of ['planning-review','revised-script','evidence-register'])docs.push(await marked.parse(await fs.readFile(path.join(root,'docs',f+'.md'),'utf8')));
await fs.writeFile(path.join(root,'docs/planning.html'),`<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>EONU 기획과 대본</title><link rel="stylesheet" href="../shared/base.css"><style>body{max-width:960px;padding:48px;margin:auto;color:#253140;font-size:16px;line-height:28px}h1{font-size:32px;line-height:44px;margin:48px 0 24px}h2{font-size:24px;line-height:36px;margin:40px 0 20px}h3{font-size:20px;line-height:28px}table{border-collapse:collapse;font-size:14px;line-height:24px}td,th{border:2px solid #e4e6eb;padding:12px;text-align:left}pre{white-space:pre-wrap}section+section{break-before:page;border-top:2px solid #e4e6eb;margin-top:64px}a{color:#476ce6}@page{size:A4;margin:18mm}@media print{body{padding:0;max-width:none;font-size:12px;line-height:20px}table{font-size:10px;line-height:16px}h1{font-size:24px;line-height:32px}h2{font-size:20px;line-height:28px}td,th{padding:8px}}</style></head><body><a href="../index.html">← 6개 시안</a><p>내용 근거와 발표 대본은 기존 기획 검토를 이어받았습니다. 이번 6개 안은 같은 12장 구조를 서로 다른 디자인으로 비교합니다.</p>${docs.map(d=>'<section>'+d+'</section>').join('')}</body></html>`);
console.log(`Built ${catalog.concepts.length} concepts, ${catalog.concepts.length*24} standalone slides.`);
