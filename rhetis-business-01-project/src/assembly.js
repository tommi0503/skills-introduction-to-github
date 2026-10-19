// Reconstruct meaningful library components from the editable reference model.
// Page geometry lives inside 12 × 6 slots; collection contracts own component parts.
const KIT='rhetis-business-01-';
const WIDTH=1280,HEIGHT=720,CW=WIDTH/12,RH=HEIGHT/6;
const set=(el,style)=>Object.assign(el.style,style);
const box=n=>({x:n.x,y:n.y,w:Math.max(n.w,1),h:Math.max(n.h,1)});
const contains=(a,b,p=3)=>b.x>=a.x-p&&b.y>=a.y-p&&b.x+b.w<=a.x+a.w+p&&b.y+b.h<=a.y+a.h+p;
const normalize=s=>String(s??'').replace(/\s/g,'').toLowerCase();
const inkKey=s=>String(s??'').toLowerCase().replace(/\s/g,'');
const common=values=>{const counts=new Map();for(const v of values.filter(Boolean))counts.set(v,(counts.get(v)||0)+1);return [...counts].sort((a,b)=>b[1]-a[1])[0]?.[0];};
const steps=[8,10,12,14,16,18,20,22,24,26,28,30,32,...Array.from({length:24},(_,i)=>36+i*4)];
function ensurePageRules(){
 if(document.getElementById('semantic-assembly-rules'))return;
 const style=document.createElement('style');style.id='semantic-assembly-rules';style.textContent=`
 .canvas[data-assembly="semantic-v2"]>.page{position:absolute;inset:0;width:100%;height:100%;padding:0;margin:0;border:0;gap:0;display:block}
 .canvas[data-assembly="semantic-v2"]>.page>.head{position:absolute;inset:0;display:block;width:100%;height:100%;margin:0;padding:0;pointer-events:none;z-index:10000}
 .canvas[data-assembly="semantic-v2"]>.page>.body{position:absolute;inset:0;width:100%;height:100%;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));gap:0;padding:0;margin:0}
 .canvas[data-assembly="semantic-v2"]>.page>.body>.group{min-width:0;min-height:0;gap:0;overflow:visible}
 .canvas[data-assembly="semantic-v2"] .reference-slot{position:relative;width:100%;height:100%;flex:none;overflow:visible;min-width:0;min-height:0}
 .canvas[data-assembly="semantic-v2"] .reference-component{display:block;padding:0;margin:0;min-width:0;min-height:0;gap:0;container-type:size}
 .canvas[data-assembly="semantic-v2"] .reference-component>.parts{position:relative;display:block;width:100%;height:100%;padding:0;margin:0;gap:0;text-align:inherit;min-width:0;min-height:0}
 .canvas[data-assembly="semantic-v2"] .reference-component>.parts>.node{margin:0;padding:0;min-width:0;min-height:0;max-width:none}
 .canvas[data-assembly="semantic-v2"] .reference-component>.parts>.mark{border:0;border-radius:0;box-shadow:none;display:block;background:transparent}
 .canvas[data-assembly="semantic-v2"] .frame>.seat::before,.canvas[data-assembly="semantic-v2"] .frame>.seat::after{content:none!important}
 .canvas[data-assembly="semantic-v2"] .reference-component>.parts::before,.canvas[data-assembly="semantic-v2"] .reference-component>.parts::after{content:none!important}
 `;document.head.append(style);
}
function context(section,deck,slide){
 const ns=slide.elements;
 const palette={page:slide.background??deck.theme?.page??'#fff',accent:deck.theme?.accent??'#197c79',ink:common(ns.filter(n=>n.type==='text').map(n=>n.color))??'#222',surface:common(ns.filter(n=>n.type==='rect'&&n.w>=120&&n.h>=60&&n.w*n.h<WIDTH*HEIGHT*.65).map(n=>n.fill))??'#fff',line:common(ns.filter(n=>n.stroke).map(n=>n.stroke))??'#ccc'};
 const vars=new Map();for(const [key,color]of Object.entries(palette)){section.style.setProperty('--'+key,color);if(!vars.has(inkKey(color)))vars.set(inkKey(color),'--'+key);}
 section.style.setProperty('--font-body',`"${common(ns.filter(n=>n.type==='text').map(n=>n.font??'Pretendard'))??'Pretendard'}",sans-serif`);
 section.style.setProperty('--font-display',`"${common(ns.filter(n=>n.type==='text'&&n.size>=32).map(n=>n.font??'Pretendard'))??'Pretendard'}",sans-serif`);
 let serial=0;
 const color=value=>{if(!value||value==='transparent'||String(value).includes('gradient('))return value;if(!vars.has(inkKey(value))){const name='--reference-color-'+(++serial);vars.set(inkKey(value),name);section.style.setProperty(name,value);}return `var(${vars.get(inkKey(value))})`;};
 const fontCache=new Map();const font=name=>{if(!name)return 'var(--font-body)';const main=(section.style.getPropertyValue('--font-body')||'').includes('"'+name+'"');if(main)return 'var(--font-body)';if(!fontCache.has(name)){const key='--reference-font-'+fontCache.size;fontCache.set(name,key);section.style.setProperty(key,`"${name}",sans-serif`);}return `var(${fontCache.get(name)})`;};
 const surface=value=>inkKey(value)===inkKey(palette.surface)?'var(--surface)':color(value);
 return {color,font,surface,counts:{cards:0,pills:0,frames:0,headings:0,freeText:0,decorations:0},groups:[],palette};
}
const roleBase={title:{weight:700,line:1.15,track:-.035},lead:{weight:400,line:1.6,track:-.02},kicker:{weight:600,line:1.3,track:-.01},meta:{weight:600,line:1.3,track:-.01},name:{weight:700,line:1.35,track:-.025},note:{weight:400,line:1.65,track:-.015},kick:{weight:600,line:1.3,track:-.01},fig:{weight:700,line:1.05,track:-.04}};
const roleToken={title:'title',lead:'lead',kicker:'label',meta:'label',name:'name',note:'body',kick:'label',fig:'figure'};
function tokenText(el,n,role,ctx){
 const base=roleBase[role]||roleBase.note,token=roleToken[role]||'body',size=n.size??20,nearest=steps.reduce((a,b)=>Math.abs(b-size)<Math.abs(a-size)?b:a,steps[0]);
 const font=ctx.font(n.font);set(el,{fontFamily:font,fontSize:`calc(var(--type-${nearest}) + ${size-nearest}px)`,fontWeight:`calc(var(--${token}-weight) + ${(n.weight??(n.type==='chip'?700:400))-base.weight})`,lineHeight:`calc(var(--${token}-line) + ${(n.lineHeight??1.4)-base.line})`,letterSpacing:`calc(var(--${token}-track) + ${n.letterSpacing??-.45}px + ${-base.track}em)`,color:ctx.color(n.color),textAlign:n.align??(n.type==='chip'?'center':'left')});
 // The text wrapper remains inline; actual part positions are preserved locally.
 const content=el.querySelector('.text-content,.name,.fig');if(content){set(content,{font:'inherit',color:'inherit',letterSpacing:'inherit',lineHeight:'inherit',whiteSpace:'inherit',margin:'0',padding:'0'});if(n.runs)for(const [i,run]of n.runs.entries()){const child=content.children[i];if(child)set(child,{color:ctx.color(run.color??n.color),fontWeight:`calc(var(--${token}-weight) + ${(run.weight??n.weight??400)-base.weight})`});}}
}
function paint(el,n,ctx){
 if(n.type==='text'||n.type==='chip')return;
 if(n.type==='rect'){el.style.background=el.classList.contains('card')?ctx.surface(n.fill):ctx.color(n.fill);el.style.border=n.stroke?`${n.strokeWidth??1}px solid ${ctx.color(n.stroke)}`:'0';}
 if(n.type==='icon'){const s=el.querySelector('svg');if(s)s.style.stroke=ctx.color(n.color);}
}
function createParts(){const p=document.createElement('div');p.className='parts';return p;}
// Kept as a standalone fallback API. Free text is foundation prose; plain geometry
// is decoration, never a fabricated empty card or an unrelated metric.
export function assembleNode(el,n){
 if(n.type==='chip'){
  el.dataset.el=KIT+'pill';el.classList.add('pill','reference-component');const p=createParts(),span=el.firstElementChild;span.className='name';p.style.cssText='width:100%;height:100%;display:flex;align-items:inherit;justify-content:inherit;text-align:inherit;';span.style.cssText='font:inherit;color:inherit;letter-spacing:inherit;line-height:inherit;margin:0;padding:0;';p.append(span);el.append(p);el.style.padding='0';el.style.gap='0';el.style.display='flex';
 }else if(n.type==='placeholder'){
  el.dataset.el=KIT+'image-frame';el.classList.add('frame','reference-component');const seat=document.createElement('div');seat.className='seat';seat.dataset.ph='1';seat.style.cssText='position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:inherit;background:var(--reference-placeholder,#e6e6e6);';el.append(seat);el.style.padding='0';el.style.border=n.stroke?`${n.strokeWidth??1}px solid ${n.stroke}`:'0';
 }else if(n.type==='text')el.classList.add('lead');else el.classList.add('page-vector');
 el.dataset.assembled='true';return el;
}
function candidateGroups(nodes){
 const surface=nodes.map((n,i)=>({n,i})).filter(({n})=>n.type==='rect'&&!n.rotate&&n.w>=120&&n.h>=60&&n.w*n.h<WIDTH*HEIGHT*.65);
 const content=n=>n.type==='text'||n.type==='icon'||n.type==='placeholder'||n.type==='chip'||(n.type==='svg'&&n.w<=120&&n.h<=120);
 const used=new Set(),groups=[];
 for(const {n,i}of surface.sort((a,b)=>a.n.w*a.n.h-b.n.w*b.n.h)){
  const members=nodes.map((child,j)=>({n:child,i:j})).filter(o=>o.i!==i&&!used.has(o.i)&&content(o.n)&&!o.n.rotate&&contains(n,o.n));
  const texts=members.filter(o=>o.n.type==='text');if(texts.length<2&&!(texts.length&&members.some(o=>o.n.type==='icon')))continue;
  // A large backdrop with scattered headers is furniture rather than one card.
  if(n.w*n.h>WIDTH*HEIGHT*.46&&texts.length>8)continue;
  used.add(i);for(const m of members)used.add(m.i);groups.push({n,i,members});
 }
 // Retain local paint order: a header strip must remain before its title,
 // rather than being painted over a completed card as an unrelated slot.
 for(const [i,n]of nodes.entries())if(!used.has(i)&&['rect','line','svg'].includes(n.type)&&!n.rotate){
  const owner=groups.filter(g=>contains(g.n,n)&&n.w*n.h<g.n.w*g.n.h*.98).sort((a,b)=>a.n.w*a.n.h-b.n.w*b.n.h)[0];
  if(owner){owner.members.push({n,i,decoration:true});used.add(i);}
 }
 return {groups,used};
}
function classifyParts(members){
 const text=members.filter(o=>o.n.type==='text'),roles=new Map();
 const numeric=text.filter(o=>/^\s*[-+−]?\d[\d.,%\s]*(?:명|억|원|만원|억원|점|배|회|%|천|만|건|개월|분)?\s*$/.test(o.n.text??'')&&o.n.size>=24);
 for(const o of numeric)roles.set(o.i,'fig');
 const remaining=text.filter(o=>!roles.has(o.i));const name=remaining.filter(o=>!String(o.n.text).includes('\n')&&String(o.n.text).length<70).sort((a,b)=>(b.n.weight??400)-(a.n.weight??400)||(b.n.size??20)-(a.n.size??20)||a.n.y-b.n.y)[0]??remaining[0];
 if(name)roles.set(name.i,'name');for(const o of remaining)if(!roles.has(o.i))roles.set(o.i,o.n.y<(name?.n.y??0)&&o.n.size<=(name?.n.size??20)?'kick':'note');
 return roles;
}
function slot(body,bounds){
 const col=Math.max(0,Math.min(11,Math.floor(bounds.x/CW))),row=Math.max(0,Math.min(5,Math.floor(bounds.y/RH)));
 const endCol=Math.max(col+1,Math.min(12,Math.ceil((bounds.x+bounds.w)/CW))),endRow=Math.max(row+1,Math.min(6,Math.ceil((bounds.y+bounds.h)/RH)));
 const group=document.createElement('div');group.className='group';group.style.gridColumn=`${col+1} / span ${endCol-col}`;group.style.gridRow=`${row+1} / span ${endRow-row}`;
 const local=document.createElement('div');local.className='reference-slot';group.append(local);body.append(group);return {el:local,x:col*CW,y:row*RH};
}
function freeRole(n,slide){
 const text=normalize(n.text),title=normalize(slide.title);
 if(n.y<280&&((n.size??20)>=32||(title.length>2&&text.includes(title)&&n.size>=20)))return 'title';
 if(n.y<110&&(n.size??20)<=26)return 'kicker';
 if(n.y>=620||(n.y>=520&&(n.size??20)<=16))return 'meta';return 'lead';
}
function foundationText(node,role){
 const semantic=document.createElement(role==='title'?'h1':'p');
 for(const attr of [...node.attributes])semantic.setAttribute(attr.name,attr.value);
 while(node.firstChild)semantic.append(node.firstChild);semantic.classList.add(role);return semantic;
}
export function assembleSlide(deck,slide,renderNode){
 ensurePageRules();const section=document.createElement('section');section.className='canvas slide overrides';section.dataset.assembly='semantic-v2';section.dataset.deck=deck.id;section.dataset.slide=slide.id;section.dataset.mode='assembled';
 const ctx=context(section,deck,slide);section.style.background='var(--page)';section.style.setProperty('--reference-placeholder','#e6e6e6');
 const page=document.createElement('div');page.className='page';const head=document.createElement('header');head.className='head';const body=document.createElement('div');body.className='body';page.append(head,body);section.append(page);
 const {groups,used}=candidateGroups(slide.elements),at=new Map(groups.map(g=>[g.i,g]));
 for(const [i,n]of slide.elements.entries()){
  const group=at.get(i);
  if(group){
   const s=slot(body,box(n)),card=renderNode({...n,x:n.x-s.x,y:n.y-s.y},i,false);card.dataset.el=KIT+'card';card.dataset.assembled='true';card.classList.add('card','reference-component');card.style.padding='0';card.style.gap='0';card.style.display='block';paint(card,n,ctx);const parts=createParts();card.append(parts);s.el.append(card);const roles=classifyParts(group.members);const borderX=n.stroke?Math.max(1,Math.floor(n.strokeWidth??1)):0,borderY=borderX;
   for(const m of group.members.sort((a,b)=>a.i-b.i)){
    const local={...m.n,x:m.n.x-n.x-borderX,y:m.n.y-n.y-borderY};let child=renderNode(local,m.i,false);child.dataset.assembled='true';
    if(local.type==='text'){const role=roles.get(m.i);child.classList.add(role);tokenText(child,local,role,ctx);}
    else if(local.type==='chip'){assembleNode(child,local);ctx.counts.pills++;tokenText(child,local,'name',ctx);child.style.background=ctx.color(local.fill);}
    else if(local.type==='placeholder'){assembleNode(child,local);ctx.counts.frames++;}
    else{child.classList.add(m.decoration?'page-vector':'mark');paint(child,local,ctx);if(m.decoration)ctx.counts.decorations++;}
    parts.append(child);
   }
   ctx.counts.cards++;ctx.groups.push({source:i,members:group.members.map(m=>m.i),parts:[...roles.values()]});continue;
  }
  if(used.has(i))continue;
  if(n.type==='text'){
   const role=freeRole(n,slide),node=foundationText(renderNode(n,i,false),role);node.dataset.assembled='true';tokenText(node,n,role,ctx);
   if(role==='title'||role==='kicker'){head.append(node);ctx.counts.headings++;}else{const s=slot(body,box(n));node.style.left=(n.x-s.x)+'px';node.style.top=(n.y-s.y)+'px';s.el.append(node);ctx.counts.freeText++;}continue;
  }
  const s=slot(body,box(n)),local={...n,x:n.x-s.x,y:n.y-s.y},node=assembleNode(renderNode(local,i,false),local);paint(node,local,ctx);
  if(n.type==='chip'){tokenText(node,local,'name',ctx);node.style.background=ctx.color(n.fill);node.style.border=n.stroke?`${n.strokeWidth??1}px solid ${ctx.color(n.stroke)}`:'0';ctx.counts.pills++;}
  else if(n.type==='placeholder')ctx.counts.frames++;else ctx.counts.decorations++;
  s.el.append(node);
 }
 // Keep title/foundation structure honest even on pages whose source heading is
 // inseparable from a vector composition. It is accessibility text, not a duplicate.
 if(!head.querySelector('.title')){const title=document.createElement('h1');title.className='title';title.textContent=slide.title;title.style.cssText='position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap;';head.append(title);}
 section.dataset.assemblySummary=JSON.stringify(ctx.counts);section.assemblyReport={...ctx.counts,groups:ctx.groups,palette:ctx.palette};return section;
}
