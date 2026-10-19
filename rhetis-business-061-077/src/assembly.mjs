// Public-contract composition adapter. Source data stays independent of both DOM renderers.
// The page supplies placement and typography; the collection supplies surfaces and parts.
import {esc,fontCSS,styleObj,renderNode} from './renderer.mjs';
const key='business-prism';
function placed(n){return {position:'absolute',left:n.x+'px',top:n.y+'px',width:n.w+'px',height:n.h+'px',zIndex:n.z,opacity:n.opacity,transform:n.rotate?`rotate(${n.rotate}deg)`:undefined,overflow:n.overflow};}
function typography(n){return {fontFamily:n.font||'Pretendard',fontSize:n.size+'px',fontWeight:n.weight,lineHeight:n.lineHeight??1.35,letterSpacing:(n.tracking??0)+'px',color:n.color,textAlign:n.align??'left',fontStyle:n.italic?'italic':undefined};}
const styles=s=>esc(styleObj(s));
function text(n){return n.runs?'<span>'+n.runs.map(r=>`<span style="${styles({color:r.color,fontWeight:r.weight,fontSize:r.size?r.size+'px':undefined})}">${esc(r.text)}</span>`).join('')+'</span>':esc(n.text);}
function component(n,i){
 const s=placed(n),meta=`data-node="${i}" data-kind="${n.type}"`;
 if(n.type==='rect'){
  const own={'--surface':n.fill,'--radius':(n.radius??0)+'px','--stroke':n.stroke==='none'?'0px':(n.sw??1)+'px','--line':n.stroke==='none'?'transparent':n.stroke,padding:0,boxShadow:n.shadow};
  return `<div class="node card" data-el="${key}-card" ${meta} style="${styles({...s,...own,...n.style})}"><div class="parts"></div></div>`;
 }
 if(n.type==='pill'){
  const own={...typography({...n,lineHeight:1}),fontWeight:n.weight??600,'--surface':n.fill,'--stroke':n.stroke?(n.sw??1)+'px':'0px','--line':n.stroke||'transparent',padding:0,borderRadius:(n.radius??n.h/2)+'px',whiteSpace:'nowrap'};
  return `<div class="node pill" data-el="${key}-pill" ${meta} style="${styles({...s,...own,...n.style})}"><div class="parts"><span class="name" data-chip-label style="font:inherit;line-height:inherit;letter-spacing:inherit;color:inherit;white-space:inherit;position:relative;display:inline-block">${esc(n.text)}</span></div></div>`;
 }
 if(n.type==='placeholder'){
  const own={'--surface-2':'#e5e5e5','--radius':(n.radius??0)+'px','--radius-sm':(n.radius??0)+'px','--stroke':n.stroke?(n.sw??1)+'px':'0px','--line':n.stroke||'transparent',padding:0,borderRadius:(n.radius??0)+'px'};
  return `<div class="node frame" data-el="${key}-image-frame" ${meta} style="${styles({...s,...own,...n.style})}"><div class="seat" data-ph="1"></div></div>`;
 }
 if(n.type==='text'){
  const role=n.size>=36?'title':'lead';
  const own={...typography(n),display:'flex',flexDirection:'column',justifyContent:n.valign==='center'?'center':n.valign==='bottom'?'flex-end':'flex-start',whiteSpace:'pre-wrap',wordBreak:'keep-all',overflowWrap:'normal',margin:0};
  return `<div class="node ${role}" ${meta} style="${styles({...s,...own,...n.style})}">${text(n)}</div>`;
 }
 // Rules, simple vector backgrounds, chart paths and Lucide icons stay editable SVG.
 return renderNode(n,i,'replica');
}
export function renderAssembly(deck,slide){
 return `<section class="slide" data-deck="${deck.id}" data-slide="${slide.id}" style="--page:${esc(slide.background)}"><div class="page overrides" style="inset:0;gap:0"><div class="body" style="gap:0"><div class="group" style="grid-column:1 / span 12; grid-row:1 / span 6">${slide.elements.map(component).join('')}</div></div></div></section>`;
}
export function assemblyDocument(title,body,css){
 const host=`html,body{margin:0;padding:0;background:#ededf0}.slide .overrides .group{position:relative;gap:0}.overrides .node{position:absolute;box-sizing:border-box;-webkit-font-smoothing:antialiased}.overrides .vector svg{display:block;width:100%;height:100%}.overrides .frame>.seat{width:100%;height:100%}.overrides .seat[data-ph]::after{content:none}.overrides .pill>.parts{gap:0}.overrides .pill>.parts>.name{transform-origin:center}.overrides .node.title{text-wrap:initial}.overrides .node.lead{text-wrap:initial}@page{size:1280px 720px;margin:0}@media print{.slide{break-after:page;print-color-adjust:exact;-webkit-print-color-adjust:exact}.slide:last-child{break-after:auto}}`;
 const ready=`document.fonts.ready.then(()=>{for(const el of document.querySelectorAll('[data-kind="pill"]')){const l=el.querySelector('[data-chip-label]'),s=getComputedStyle(el),c=document.createElement('canvas').getContext('2d');c.font=s.fontWeight+' '+s.fontSize+' '+s.fontFamily;const m=c.measureText(l.textContent),dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2,dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2;l.style.transform='translate('+(-dx)+'px,'+(-dy)+'px)'}document.body.dataset.ready='true'})`;
 return `<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>${esc(title)}</title><style>${fontCSS}\n${css}\n${host}</style></head><body>${body}<script>${ready}</script></body></html>`;
}
