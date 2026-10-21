(function(){
 const E=window.EONU={};
 E.esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 E.icon=(name)=>{
  const paths={person:'<circle cx="12" cy="7" r="3"/><path d="M5 22v-4a7 7 0 0 1 14 0v4"/>',family:'<circle cx="8" cy="7" r="3"/><circle cx="18" cy="9" r="2"/><path d="M2 22v-4a6 6 0 0 1 12 0v4m2-8a5 5 0 0 1 6 5v3"/>',doctor:'<path d="M6 2v8a5 5 0 0 0 10 0V2M4 2h4m6 0h4m-7 13v2a4 4 0 0 0 8 0v-3"/><circle cx="19" cy="11" r="3"/>',arrow:'<path d="M2 12h20m-8-8 8 8-8 8"/>',check:'<path d="m4 12 5 5L20 5"/>',clock:'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',chart:'<path d="M2 2v20h20M6 16l4-6 4 2 8-8"/>',link:'<path d="m8 8 3-3a5 5 0 0 1 7 7l-3 3M16 16l-3 3a5 5 0 0 1-7-7l3-3m-1 7 8-8"/>',shield:'<path d="m12 2 10 4v6c0 5-10 10-10 10S2 17 2 12V6zM7 12l4 4 6-8"/>'};
  return `<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths[name]||paths.arrow}</svg>`;
 };
 E.ph=(label,cls='')=>`<div class="placeholder ${cls}" role="img" aria-label="${E.esc(label)} 이미지 영역"><span class="image-label">${label}</span></div>`;
 E.tag=(text,cls='')=>`<span class="tag ${cls}">${text}</span>`;
 E.arrow=()=>`<span class="connector">${E.icon('arrow')}</span>`;
 E.relation=(active='all',compact=false)=>{
  const node=(role,icon,title,desc)=>`<div class="relation-node ${role}">${E.icon(icon)}<strong>${title}</strong>${compact?'':`<span>${desc}</span>`}</div>`;
  const path=compact?'<path class="edge doctor" d="M112 112H232"/><path class="edge patient" d="M432 48 320 92"/><path class="edge guardian" d="M432 176 320 132"/><path class="head doctor" d="m220 104 12 8-12 8"/><path class="head patient" d="m326 80-6 12 14 2"/><path class="head guardian" d="m334 130-14 2 6 12"/>':'<path class="edge doctor" d="M176 176H304"/><path class="edge patient" d="M544 64 432 144"/><path class="edge guardian" d="M544 288 432 208"/><path class="head doctor" d="m292 168 12 8-12 8"/><path class="head patient" d="m436 130-4 14 14-2"/><path class="head guardian" d="m446 208-14 0 4 14"/>';
  return `<div class="relation active-${active}${compact?' compact':''}" role="img" aria-label="의료진·환자·보호자가 EONU를 중심으로 연결됩니다. ${active==='doctor'?'의료진에서 EONU로 향하는 흐름 강조':active==='patient'?'환자에서 EONU로 향하는 흐름 강조':'세 사람의 정보 연결'}"><svg class="relation-lines" viewBox="${compact?'0 0 576 224':'0 0 736 352'}" aria-hidden="true">${path}</svg>${node('doctor','doctor','의료진','질문 · 정보 · 안내')}<div class="relation-center"><strong>EONU</strong><span>확인하고 연결</span></div>${node('patient','person','환자','일상 경험 · 걱정')}${node('guardian','family','보호자','관찰 · 도움')}${compact?'':`<span class="relation-label doctor-label">① 병원의 기준</span><span class="relation-label patient-label">② 일상의 정보</span>`}</div>`;
 };
 E.renderSlide=(s,theme='design')=>{
  const bookend=s.id==='01'||s.id==='12';
  return `<article class="slide ${theme} page-${s.id}${bookend?' bookend':''}" data-slide="${s.id}" aria-label="${s.id}. ${E.esc(s.title.replace(/<[^>]*>/g,''))}">${bookend?'':`<header class="slide-header"><span class="section-label">${s.section}</span><span class="brand">EONU</span></header><div class="heading"><h1>${s.title}</h1><p class="subtitle">${s.subtitle}</p></div>`}<div class="slide-body layout-${s.id}">${s.content}</div>${bookend?'':`<footer class="slide-footer"><span class="source-note">${s.note}</span><span class="page-number">${s.id}<span> / 12</span></span></footer>`}</article>`;
 };
})();
