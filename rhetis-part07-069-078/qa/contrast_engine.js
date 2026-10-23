() => {
 const canvas=document.createElement('canvas');canvas.width=canvas.height=1;const ctx=canvas.getContext('2d',{willReadFrequently:true});
 const rgb=c=>{ctx.clearRect(0,0,1,1);ctx.fillStyle=c;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data].map((v,i)=>i===3?v/255:v)};
 const lum=c=>c.slice(0,3).map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4}).reduce((v,x,i)=>v+x*[.2126,.7152,.0722][i],0);

 const inPoly=(x,y,path,w,h)=>{if(!path.startsWith('polygon('))return true;const pts=path.slice(8,-1).split(',').map(p=>p.trim().split(/\s+/).map((v,i)=>v.endsWith('%')?parseFloat(v)*(i?h:w)/100:parseFloat(v)));if(pts.some(p=>p.length!==2||p.some(v=>!Number.isFinite(v))))return false;let hit=false;for(let i=0,j=pts.length-1;i<pts.length;j=i++){let[a,b]=pts[i],[c,d]=pts[j];if((b>y)!==(d>y)&&x<(c-a)*(y-b)/(d-b)+a)hit=!hit;}return hit;};
 const pseudoPaint=(a,p,cx,cy)=>{const ps=getComputedStyle(a,p);if(ps.content==='none'||ps.display==='none'||ps.position!=='absolute')return null;let cb=a;while(cb&&getComputedStyle(cb).position==='static'&&getComputedStyle(cb).transform==='none'&&getComputedStyle(cb).contain==='none')cb=cb.parentElement;if(!cb)return null;const br=cb.getBoundingClientRect(),bs=getComputedStyle(cb),num=v=>parseFloat(v)||0,sx=br.width/(cb.offsetWidth||br.width),sy=br.height/(cb.offsetHeight||br.height),uw=num(ps.width),uh=num(ps.height),w=uw*sx,h=uh*sy;let x=br.left+(num(bs.borderLeftWidth)+(ps.left!=='auto'?num(ps.left):cb.clientWidth-num(ps.right)-uw))*sx,y=br.top+(num(bs.borderTopWidth)+(ps.top!=='auto'?num(ps.top):cb.clientHeight-num(ps.bottom)-uh))*sy;if(ps.transform!=='none'){const m=new DOMMatrix(ps.transform);if(Math.abs(m.b)>.001||Math.abs(m.c)>.001)return null;x+=m.e*sx;y+=m.f*sy;}if(cx<x||cx>x+w||cy<y||cy>y+h||!inPoly(cx-x,cy-y,ps.clipPath,w,h))return null;return ps;};
 const candidates=[],skipped=[];
 for(const e of document.querySelectorAll('.slide *')){
  if(e.children.length||!e.textContent.trim())continue;const s=getComputedStyle(e),r=e.getBoundingClientRect();if(!r.width||!r.height||s.display==='none'||s.visibility==='hidden')continue;
  let chain=[],a=e,hasGradient=false;
  while(a){const st=getComputedStyle(a),ar=a.getBoundingClientRect(),cx=r.x+r.width/2,cy=r.y+r.height/2,hit=cx>=ar.left&&cx<=ar.right&&cy>=ar.top&&cy<=ar.bottom;if(hit){for(const pseudo of ['::after','::before']){const ps=pseudoPaint(a,pseudo,cx,cy);if(ps){chain.push(rgb(ps.backgroundColor));if(ps.backgroundImage!=='none')hasGradient=true;}}chain.push(rgb(st.backgroundColor));if(st.backgroundImage!=='none')hasGradient=true;}if(a.matches('.slide'))break;a=a.parentElement;}
  if(hasGradient){skipped.push(e.textContent.slice(0,50));continue}
  let bg=[255,255,255];for(const c of chain.reverse())bg=bg.map((v,i)=>c[i]*c[3]+v*(1-c[3]));const fg=rgb(s.color);const solid=fg.map((v,i)=>i===3?1:v*fg[3]+bg[i]*(1-fg[3]));
  let l1=lum(solid),l2=lum(bg),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05),threshold=(parseFloat(s.fontSize)>=24||(parseFloat(s.fontSize)>=18.6667&&parseFloat(s.fontWeight)>=700))?3:4.5;
  if(ratio+0.04<threshold)candidates.push({text:e.textContent.trim().slice(0,90),class:e.className,ratio:+ratio.toFixed(2),threshold,size:s.fontSize,fg:s.color,bg:bg.map(Math.round),fixture:e.closest('article')?.querySelector('h2')?.textContent||''});
 }
 return {candidates,gradientSkipped:skipped.length};
}
