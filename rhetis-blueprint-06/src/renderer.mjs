import fs from 'node:fs';
const icons=JSON.parse(fs.readFileSync(new URL('./lucide-icons.json',import.meta.url),'utf8'));
export const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const kebab=s=>s.replace(/[A-Z]/g,m=>'-'+m.toLowerCase());
function styleObj(o){return Object.entries(o).filter(([,v])=>v!==undefined&&v!==null).map(([k,v])=>`${kebab(k)}:${v}`).join(';')}
export const fontCSS=`@font-face{font-family:Oswald;src:url('../../../assets/fonts/Oswald-500.woff2');font-weight:500;font-display:block}@font-face{font-family:Montserrat;src:url('../../../assets/fonts/Montserrat-Variable.woff2');font-weight:100 900;font-display:block}@font-face{font-family:'Gmarket Sans';src:url('../../../assets/fonts/GmarketSansLight.woff');font-weight:300;font-display:block}@font-face{font-family:'Gmarket Sans';src:url('../../../assets/fonts/GmarketSansMedium.woff');font-weight:500;font-display:block}@font-face{font-family:'Gmarket Sans';src:url('../../../assets/fonts/GmarketSansBold.woff');font-weight:700;font-display:block}${[300,400,500,600,700,800,900].map((w,i)=>`@font-face{font-family:Pretendard;src:url('../../../assets/fonts/Pretendard-${['Light','Regular','Medium','SemiBold','Bold','ExtraBold','Black'][i]}.woff2') format('woff2');font-weight:${w};font-style:normal;font-display:block}`).join('')}`;
export const baseCSS=`*{box-sizing:border-box}html,body{margin:0;padding:0}body{background:#ededf0}.slide{width:1280px;height:720px;position:relative;overflow:hidden;font-family:Pretendard,sans-serif;background:white;color:#17202b}.node{position:absolute;box-sizing:border-box}.text,.chip{font-family:Pretendard,sans-serif;margin:0;white-space:pre-wrap;word-break:keep-all;overflow-wrap:normal;-webkit-font-smoothing:antialiased}.text{display:flex;flex-direction:column;justify-content:flex-start}.chip{display:flex;align-items:center;justify-content:center;white-space:nowrap}.chip-label{display:inline-block;position:relative;line-height:1}.vector svg{width:100%;height:100%;display:block}.node .parts{width:100%;height:100%;display:contents}.node .name{font:inherit;color:inherit;line-height:inherit;letter-spacing:inherit;margin:0;white-space:inherit}.node .seat{width:100%;height:100%;background:#e5e5e5;border-radius:inherit}.node .seat::after{content:none!important}@page{size:1280px 720px;margin:0}@media print{html,body{background:white}.slide{break-after:page;page-break-after:always;print-color-adjust:exact;-webkit-print-color-adjust:exact}.slide:last-child{break-after:auto}}`;
function iconSVG(n){const name=n.name?.replace(/(^|-)(\w)/g,(_,a,b)=>b.toUpperCase());return (icons[name]||icons.Circle).replace('stroke="currentColor"',`stroke="${esc(n.color)}"`).replace('stroke-width="1.7"',`stroke-width="${n.sw??1.7}"`);}

export function renderNode(n,i,mode='replica'){
 const s={left:n.x+'px',top:n.y+'px',width:n.w+'px',height:n.h+'px',zIndex:n.z,opacity:n.opacity,transform:n.rotate?`rotate(${n.rotate}deg)`:undefined,overflow:n.overflow};
 let cls='node',body='',tag='div';
 if(n.type==='text'){
  cls+=' text';Object.assign(s,{fontFamily:n.font||'Pretendard',fontSize:n.size+'px',fontWeight:n.weight,lineHeight:n.lineHeight??1.35,letterSpacing:(n.tracking??0)+'px',color:n.color,textAlign:n.align??'left',fontStyle:n.italic?'italic':undefined,justifyContent:n.valign==='center'?'center':n.valign==='bottom'?'flex-end':'flex-start'});
  body=n.runs?'<span>'+n.runs.map(r=>'<span style="color:'+esc(r.color||n.color)+';font-weight:'+(r.weight||n.weight)+'">'+esc(r.text)+'</span>').join('')+'</span>':esc(n.text);
 }else if(n.type==='pill'){
  cls+=' chip';Object.assign(s,{background:n.fill,borderRadius:(n.radius??n.h/2)+'px',color:n.color,fontSize:n.size+'px',fontWeight:n.weight??600,lineHeight:1,letterSpacing:(n.tracking??0)+'px',border:n.stroke?`${n.sw??1}px solid ${n.stroke}`:undefined});body=`<span class="chip-label" data-chip-label>${esc(n.text)}</span>`;
  
 }else if(n.type==='rect'){
  cls+=' shape';Object.assign(s,{background:n.fill,borderRadius:(n.radius??0)+'px',border:n.stroke!=='none'?`${n.sw??1}px solid ${n.stroke}`:undefined,boxShadow:n.shadow});
 }else if(n.type==='placeholder'){
  cls+=' placeholder';Object.assign(s,{background:'#e5e5e5',borderRadius:(n.radius??0)+'px',border:n.stroke?`${n.sw??1}px solid ${n.stroke}`:undefined});
 }else if(n.type==='svg'||n.type==='icon'){
  cls+=' vector';body=n.type==='svg'?n.svg:iconSVG(n);
 }else if(n.type==='line'){
  const x=Math.min(n.x,n.x+n.w),y=Math.min(n.y,n.y+n.h),w=Math.max(Math.abs(n.w),1),h=Math.max(Math.abs(n.h),1);Object.assign(s,{left:x+'px',top:y+'px',width:w+'px',height:h+'px',overflow:'visible'});cls+=' vector';body=`<svg viewBox="0 0 ${w} ${h}" overflow="visible"><line x1="${n.w>=0?0:w}" y1="${n.h>=0?0:h}" x2="${n.w>=0?w:0}" y2="${n.h>=0?h:0}" stroke="${n.color}" stroke-width="${n.width}" ${n.dash?`stroke-dasharray="${n.dash}"`:''}/></svg>`;
 }
 Object.assign(s,n.style??{});
 return `<${tag} class="${cls}" data-node="${i}" data-kind="${n.type}" style="${esc(styleObj(s))}">${body}</${tag}>`;
}
export function renderSlide(deck,slide){return `<section class="slide" data-deck="${deck.id}" data-slide="${slide.id}" style="background:${esc(slide.background)}">${slide.elements.map((n,i)=>renderNode(n,i)).join('')}</section>`}
export function documentHTML(title,body,extraCSS=''){return `<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>${esc(title)}</title><style>${fontCSS}\n${extraCSS}\n${baseCSS}</style></head><body>${body}<script>document.fonts.ready.then(()=>{for(const el of document.querySelectorAll('.chip')){const l=el.querySelector('[data-chip-label]');if(!l)continue;const s=getComputedStyle(el),c=document.createElement('canvas').getContext('2d');c.font=s.fontWeight+' '+s.fontSize+' '+s.fontFamily;const m=c.measureText(l.textContent);const dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2;const dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2;l.style.transform='translate('+(-dx)+'px,'+(-dy)+'px)'}document.body.dataset.ready='true'})</script></body></html>`}
