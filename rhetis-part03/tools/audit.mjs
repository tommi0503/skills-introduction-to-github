export async function audit(page){return page.evaluate(()=>{
const findings=[],stage=document.querySelector('.slide-canvas'),sr=stage.getBoundingClientRect();
for(const [i,el] of [...stage.querySelectorAll('.element')].entries()){
 const r=el.getBoundingClientRect(),cs=getComputedStyle(el),text=el.textContent?.trim();
 if(el.classList.contains('element-text')&&text){const range=document.createRange();range.selectNodeContents(el);const tr=range.getBoundingClientRect();if(tr.right>sr.right+2||tr.bottom>sr.bottom+2||tr.left<sr.left-2||tr.top<sr.top-2)findings.push({i,type:'text-stage-overflow',text:text.slice(0,90),rect:[tr.x,tr.y,tr.width,tr.height]});
 if(tr.right>r.right+2||tr.bottom>r.bottom+3)findings.push({i,type:'text-frame-overflow',text:text.slice(0,90),excess:[Math.round(tr.right-r.right),Math.round(tr.bottom-r.bottom)],rect:[r.x,r.y,r.width,r.height]});
 }
 if(el.classList.contains('element-chip')&&text){const t=el.querySelector('span'),tr=t.getBoundingClientRect();if(tr.width>r.width+1||tr.height>r.height+3)findings.push({i,type:'chip-overflow',text,excess:[tr.width-r.width,tr.height-r.height]});}
}
return{width:sr.width,height:sr.height,fontStatus:document.fonts.status,pretendard:document.fonts.check('400 16px "Pretendard Variable"'),findings};
})}
