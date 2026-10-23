a => {
 const out={stack:[],donut:[],balance:[],bullet:[],seats:[],graphics:[],polygonText:[],polygonSkipped:[]};
 const rect=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height,left:r.left,right:r.right,top:r.top,bottom:r.bottom}};
 const n=v=>Number.parseFloat(v)||0;
 const visible=e=>{const s=getComputedStyle(e),r=rect(e);return r.w>0&&r.h>0&&s.visibility!=='hidden'&&s.display!=='none'};
 function pseudoRect(e,p){
  const s=getComputedStyle(e,p);if(s.content==='none'||s.display==='none')return null;
  let cb=e;while(cb&&getComputedStyle(cb).position==='static'&&getComputedStyle(cb).transform==='none'&&getComputedStyle(cb).contain==='none')cb=cb.parentElement;
  if(!cb)cb=e;const b=rect(cb),bs=getComputedStyle(cb),cw=cb.clientWidth,ch=cb.clientHeight;
  const w=n(s.width),h=n(s.height);let x,y;
  if(s.position==='absolute'||s.position==='fixed'){
   x=b.x+n(bs.borderLeftWidth)+(s.left!=='auto'?n(s.left):cw-n(s.right)-w);
   y=b.y+n(bs.borderTopWidth)+(s.top!=='auto'?n(s.top):ch-n(s.bottom)-h);
  }else{
   // Static grid pseudo-items: resolve explicit row/column against used pixel tracks.
   const rootStyle=getComputedStyle(e),eb=rect(e),cols=rootStyle.gridTemplateColumns.split(' ').map(n),rows=rootStyle.gridTemplateRows.split(' ').map(n),col=Math.max(0,n(s.gridColumnStart)-1),row=Math.max(0,n(s.gridRowStart)-1);
   if(rootStyle.display!=='grid'||!cols.length||!rows.length)return null;
   x=eb.x+n(rootStyle.borderLeftWidth)+n(rootStyle.paddingLeft)+cols.slice(0,col).reduce((a,b)=>a+b,0)+col*n(rootStyle.columnGap);
   y=eb.y+n(rootStyle.borderTopWidth)+n(rootStyle.paddingTop)+rows.slice(0,row).reduce((a,b)=>a+b,0)+row*n(rootStyle.rowGap);
   const align=s.alignSelf==='auto'?rootStyle.alignItems:s.alignSelf;if(align==='center')y+=(rows[row]-h)/2;
   const justify=s.justifySelf==='auto'?rootStyle.justifyItems:s.justifySelf;if(justify==='center')x+=(cols[col]-w)/2;
  }
  if(s.transform!=='none'){const m=new DOMMatrix(s.transform);x+=m.e;y+=m.f;}
  if(s.translate!=='none'){const parts=s.translate.split(' ');x+=parts[0]?.includes('%')?n(parts[0])*w/100:n(parts[0]);y+=parts[1]?.includes('%')?n(parts[1])*h/100:n(parts[1]);}
  return {x,y,w,h,cx:x+w/2,cy:y+h/2,style:s};
 }
 // Default untoned segment ordinal colors must remain distinguishable.
 for(const row of a.querySelectorAll('.stacks .sbar')){
  const seg=[...row.querySelectorAll(':scope > .seg')].filter(visible);if(seg.length<2)continue;
  const paints=seg.map(e=>{const s=getComputedStyle(e);return s.backgroundColor+'|'+s.backgroundImage});
  if(new Set(paints).size<seg.length)out.stack.push({label:row.querySelector(':scope > span')?.textContent,segments:seg.length,uniquePaints:new Set(paints).size,paints});
 }
 // Measure the actual conic-painted object, including its generated pseudo.
 for(const donut of a.querySelectorAll('.donut')){
  for(const p of [null,'::before','::after']){
   const s=p?getComputedStyle(donut,p):getComputedStyle(donut);if(!s.backgroundImage.includes('conic-gradient'))continue;
   const r=p?pseudoRect(donut,p):rect(donut);if(!r||r.w<2||r.h<2)continue;
   if(Math.abs(r.w/r.h-1)>.035)out.donut.push({pseudo:p||'root',size:[r.w,r.h],ratio:r.w/r.h,value:donut.style.getPropertyValue('--v')});
  }
 }
 // Heavy left pan for a negative tilt must move down relative to its neutral state.
 for(const balance of a.querySelectorAll('.balance')){
  const pans=balance.querySelectorAll(':scope > .pan');if(pans.length!==2)continue;const old=balance.style.getPropertyValue('--tilt');
  const sample=t=>{balance.style.setProperty('--tilt',t);const l=rect(pans[0]),r=rect(pans[1]),s=getComputedStyle(balance,'::before');let angle=0;if(s.transform!=='none'){const m=new DOMMatrix(s.transform);angle=Math.atan2(m.b,m.a)*180/Math.PI;}if(s.rotate!=='none')angle+=n(s.rotate);return {delta:(l.top+l.h/2)-(r.top+r.h/2),angle}};
  const zero=sample(0),left=sample(-50),right=sample(50);balance.style.setProperty('--tilt',old);
  const dl=left.delta-zero.delta,dr=right.delta-zero.delta;let issues=[];
  if(left.angle>=-.05||right.angle<=.05)issues.push('beam-sign');
  if(dl<-.5||dr>.5)issues.push('pan-sign');else if(Math.abs(dl)<.5&&Math.abs(dr)<.5)issues.push('pans-do-not-follow-beam');
  if(issues.length)out.balance.push({issues,leftDelta:dl,rightDelta:dr,leftAngle:left.angle,rightAngle:right.angle});
 }
 // Actual/target coordinates are independent of the fixture's label text.
 for(const bullet of a.querySelectorAll('.bullet')){
  const de=bullet.getAttribute('data-el')||bullet.closest('[data-el]')?.getAttribute('data-el')||'';
  let fill,track,marker;const fig=bullet.querySelector(':scope > .fig');
  if(de.startsWith('vectorbox-')){fill=pseudoRect(bullet,'::before');marker=pseudoRect(bullet,'::after');}
  else if(de.startsWith('seedmark-')||de.startsWith('crossrail-')){track=pseudoRect(bullet,'::before');fill=pseudoRect(bullet,'::after');marker=fig?pseudoRect(fig,'::after'):null;}
  else if(de.startsWith('onboard-docket-')){fill=pseudoRect(bullet,'::before');track=fill;marker=pseudoRect(bullet,'::after');}
  else if(de.startsWith('meridian-deck-'))continue; // This design uses the caption's border as its target cue; visual review handles that variant.
  if(!fill||!marker)continue;const s=getComputedStyle(bullet),v=n(s.getPropertyValue('--v')),target=n(s.getPropertyValue('--target'));
  const range=track?.w||(v?fill.w/(v/100):0),start=(track||fill).x,expectedX=start+range*target/100,expectedY=(track||fill).cy;
  const dx=marker.cx-expectedX,dy=marker.cy-expectedY,tooTall=marker.h>Math.max(40,(track||fill).h*3.5);
  if(Math.abs(dx)>4||Math.abs(dy)>4||tooTall)out.bullet.push({value:v,target,dx,dy,marker:[marker.w,marker.h],track:[range,(track||fill).h],tooTall});
 }
 // Foundation seats that do not belong to a component must stay close to square.
 for(const seat of a.querySelectorAll('.seat:not(.back):not(.portrait)')){
  if(seat.closest('[data-el]')||!visible(seat))continue;const r=rect(seat);if(r.w/r.h<.8||r.w/r.h>1.25)out.seats.push({ph:seat.getAttribute('data-ph'),size:[r.w,r.h],ratio:r.w/r.h});
 }
 // Nontext graphic boxes: empty heat cells/units must not disappear beyond a slot.
 for(const e of a.querySelectorAll('.cell,.u,.seat:not(.back),.ring,.dot')){
  if(!visible(e))continue;let slot=e.closest('[data-el]');if(!slot){slot=e;while(slot.parentElement&&!slot.parentElement.classList.contains('body'))slot=slot.parentElement;if(!slot.parentElement?.classList.contains('body'))continue;}
  const er=rect(e),sr=rect(slot);if(e!==slot&&(er.left<sr.left-2||er.top<sr.top-2||er.right>sr.right+2||er.bottom>sr.bottom+2))out.graphics.push({class:e.className,slot:slot.className,box:[er.x-sr.x,er.y-sr.y,er.w,er.h],slotSize:[sr.w,sr.h],kind:'outside-assigned-slot'});
  for(let p=e.parentElement;p&&p!==a;p=p.parentElement){const ps=getComputedStyle(p),pr=rect(p),x=['hidden','clip','scroll','auto'].includes(ps.overflowX),y=['hidden','clip','scroll','auto'].includes(ps.overflowY);if((x&&(er.left<pr.left-2||er.right>pr.right+2))||(y&&(er.top<pr.top-2||er.bottom>pr.bottom+2))){out.graphics.push({class:e.className,clipAncestor:p.className,kind:'actual-overflow-clip'});break;}}
 }
 // Convex and concave CSS polygons: text rect corners should remain within the shape.
 function polyPoints(value,r){if(!value.startsWith('polygon('))return null;let body=value.slice(8,-1).replace(/^(?:evenodd|nonzero),\s*/,'');const pts=[];for(const pair of body.split(',')){const xy=pair.trim().split(/\s+/);if(xy.length!==2||xy.some(v=>!/^-?[\d.]+(?:px|%)?$/.test(v)))return null;pts.push(xy.map((v,i)=>v.endsWith('%')?n(v)*(i?r.h:r.w)/100:n(v)));}return pts;}
 function inside(p,poly){let yes=false;for(let i=0,j=poly.length-1;i<poly.length;j=i++){const [xi,yi]=poly[i],[xj,yj]=poly[j];if(((yi>p[1])!==(yj>p[1]))&&(p[0]<(xj-xi)*(p[1]-yi)/(yj-yi)+xi))yes=!yes;}return yes;}
 for(const shape of a.querySelectorAll('.funnel .stage,.pyramid .level')){
  if(!visible(shape))continue;const path=getComputedStyle(shape).clipPath;if(path==='none')continue;const sr=rect(shape),poly=polyPoints(path,sr);if(!poly){out.polygonSkipped.push(path);continue;}
  const w=document.createTreeWalker(shape,NodeFilter.SHOW_TEXT);let text;while(text=w.nextNode()){if(!text.textContent.trim()||getComputedStyle(text.parentElement).display==='none')continue;const range=document.createRange();range.selectNodeContents(text);for(const tr of range.getClientRects()){if(!tr.width||!tr.height)continue;const corners=[[tr.left-sr.left+2,tr.top-sr.top+2],[tr.right-sr.left-2,tr.top-sr.top+2],[tr.right-sr.left-2,tr.bottom-sr.top-2],[tr.left-sr.left+2,tr.bottom-sr.top-2]];if(corners.some(p=>!inside(p,poly))){const midY=tr.top-sr.top+tr.height*.55,leftX=tr.left-sr.left+Math.min(4,tr.width*.1),rightX=tr.right-sr.left-Math.min(4,tr.width*.1),midlineCut=!inside([leftX,midY],poly)||!inside([rightX,midY],poly),outsideRect=tr.left<sr.left-3||tr.top<sr.top-3||tr.right>sr.right+3||tr.bottom>sr.bottom+3;out.polygonText.push({text:text.textContent.trim().slice(0,90),shape:shape.className,path,severity:midlineCut||outsideRect?'probable-glyph-cut':'corner-only-review',textBox:[tr.x-sr.x,tr.y-sr.y,tr.width,tr.height],shapeSize:[sr.w,sr.h]});}}}
 }
 return out;
}
