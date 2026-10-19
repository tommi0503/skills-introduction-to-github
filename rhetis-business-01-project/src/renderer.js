import{assembleNode,assembleSlide}from'./assembly.js';
const esc=s=>String(s??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const css=(el,style)=>Object.assign(el.style,style);
let icons={}; export function setIcons(v){icons=v;}
export function renderNode(n,index,assembled=false){
 const el=document.createElement('div'); el.className='node '+n.type; el.dataset.node=index;el.dataset.kind=n.type;
 css(el,{position:'absolute',left:n.x+'px',top:n.y+'px',width:n.w+'px',height:n.h+'px',boxSizing:'border-box',zIndex:n.z??'',opacity:n.opacity??1,transform:[n.rotate?`rotate(${n.rotate}deg)`:'',n.scaleX?`scaleX(${n.scaleX})`:''].filter(Boolean).join(' '),transformOrigin:n.origin??'left top',borderRadius:(n.radius??0)+'px',overflow:n.clip?'hidden':'visible'});
 if(n.type==='text'||n.type==='chip'){
  css(el,{fontFamily:n.font??'Pretendard',fontSize:n.size+'px',fontWeight:n.weight??(n.type==='chip'?700:400),color:n.color,letterSpacing:(n.letterSpacing??-.45)+'px',lineHeight:String(n.lineHeight??1.4),textAlign:n.align??(n.type==='chip'?'center':'left'),whiteSpace:'pre-wrap',wordBreak:'keep-all',display:n.type==='chip'||n.valign==='middle'?'flex':'block',alignItems:'center',justifyContent:n.align==='right'?'flex-end':n.align==='left'?'flex-start':'center',background:n.type==='chip'?n.fill:'',borderRadius:(n.radius??(n.type==='chip'?4:0))+'px',WebkitTextStroke:n.type==='text'&&n.stroke?`${n.strokeWidth??1}px ${n.stroke}`:'',textShadow:n.shadow??''});
  const span=document.createElement('span');span.className=n.type==='chip'?'name':'text-content';if(n.runs){for(const run of n.runs){const s=document.createElement('span');s.textContent=run.text;css(s,{color:run.color??n.color,fontWeight:run.weight??n.weight,fontSize:run.size?run.size+'px':'',verticalAlign:run.valign??''});span.append(s);}}else span.textContent=n.text;el.append(span);
  if(n.type==='chip'&&n.stroke)el.style.border=`${n.strokeWidth??1}px solid ${n.stroke}`;
 }else if(n.type==='rect'){css(el,{background:n.fill,border:n.stroke?`${n.strokeWidth??1}px solid ${n.stroke}`:'',boxShadow:n.shadow??''});}
 else if(n.type==='placeholder'){css(el,{background:'#e6e6e6',border:n.stroke?`${n.strokeWidth??1}px solid ${n.stroke}`:''});el.dataset.placeholder='true';}
 else if(n.type==='line'){el.style.width=Math.max(n.w,1)+'px';el.style.height=Math.max(n.h,1)+'px';el.innerHTML=`<svg width="100%" height="100%" viewBox="0 0 ${Math.max(n.w,1)} ${Math.max(n.h,1)}" overflow="visible"><line x1="0" y1="0" x2="${n.w}" y2="${n.h}" stroke="${n.color}" stroke-width="${n.stroke??1}" ${n.dash?'stroke-dasharray="'+n.dash+'"':''}/></svg>`;}
 else if(n.type==='svg'){el.innerHTML=`<svg width="100%" height="100%" viewBox="${n.viewBox??`0 0 ${n.w} ${n.h}`}" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">${n.content}</svg>`;}
 else if(n.type==='icon'){el.innerHTML=icons[n.name]??icons.CircleHelp??'';const s=el.querySelector('svg');if(s){s.setAttribute('width','100%');s.setAttribute('height','100%');s.setAttribute('stroke',n.color??'currentColor');s.setAttribute('stroke-width',n.strokeWidth??1.5);}}
 if(assembled){el.dataset.assembled='true';assembleNode(el,n);}
 return el;
}
export function renderSlide(deck,slide,mode='clone'){
 if(mode==='assembled')return assembleSlide(deck,slide,renderNode);
 const el=document.createElement('section');el.className='canvas';el.dataset.deck=deck.id;el.dataset.slide=slide.id;el.dataset.mode=mode;css(el,{background:slide.background??deck.theme?.page??'#fff','--accent':deck.theme?.accent??'#197c79'});
 for(const [i,n]of slide.elements.entries())el.append(renderNode(n,i,false));
 return el;
}
export {esc};
