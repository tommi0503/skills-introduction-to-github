/* Shared slide primitives. No network, raster charts or external runtime. */
(function () {
  const E = window.EONU = window.EONU || {};
  E.esc = (s) => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  E.icon = (name, cls='') => {
    const p = {
      person:'<circle cx="12" cy="7" r="3"/><path d="M5 21v-3a7 7 0 0 1 14 0v3"/>',
      family:'<circle cx="8" cy="7" r="3"/><circle cx="18" cy="9" r="2"/><path d="M2 21v-3a6 6 0 0 1 12 0v3m2-7a5 5 0 0 1 6 5v2"/>',
      doctor:'<path d="M6 3v7a5 5 0 0 0 10 0V3M4 3h4m6 0h4m-7 12v2a4 4 0 0 0 8 0v-3"/><circle cx="19" cy="11" r="3"/>',
      message:'<path d="M21 14a3 3 0 0 1-3 3H9l-6 4V6a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3zM7 8h10M7 12h7"/>',
      check:'<path d="m5 12 4 4L19 6"/><rect x="2" y="2" width="20" height="20" rx="6"/>',
      chart:'<path d="M3 3v18h18M7 16l4-5 4 2 6-8"/>',
      shield:'<path d="m12 2 9 4v6c0 5-9 10-9 10S3 17 3 12V6zM8 12l3 3 5-6"/>',
      clock:'<circle cx="12" cy="12" r="9"/><path d="M12 6v6l4 2"/>',
      arrow:'<path d="M3 12h17m-6-6 6 6-6 6"/>',
      link:'<path d="m8 8 3-3a5 5 0 0 1 7 7l-3 3M16 16l-3 3a5 5 0 0 1-7-7l3-3m-1 7 8-8"/>',
      record:'<path d="M6 3h12v18H6zM9 7h6M9 11h6M9 15h4"/>',
      building:'<path d="M4 21V4h16v17M2 21h20M8 8h2m4 0h2M8 12h2m4 0h2m-6 9v-5h4v5"/>'
    };
    return `<svg class="icon ${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${p[name]||p.message}</svg>`;
  };
  E.pill = (text, cls='') => `<span class="pill ${cls}">${text}</span>`;
  E.placeholder = (label, cls='') => `<div class="placeholder ${cls}" role="img" aria-label="${E.esc(label)} 이미지 배치 영역"><span>${label}</span></div>`;
  E.arrow = () => `<span class="flow-arrow" aria-hidden="true">${E.icon('arrow')}</span>`;
  E.card = (label, title, body, cls='') => `<div class="card ${cls}"><div class="eyebrow">${label}</div><h3>${title}</h3><p>${body}</p></div>`;
  E.triangle = (active='all', cls='') => {
    const node=(c,icon,title,small)=>`<div class="tri-node ${c}">${E.icon(icon)}<b>${title}</b><span>${small}</span></div>`;
    return `<div class="triangle ${cls} active-${active}" role="img" aria-label="의료진, 환자, 보호자가 EONU를 중심으로 연결되는 관계도. ${active==='doctor'?'의료진에서 EONU로 향하는 첫 번째 흐름 강조.':active==='patient'?'환자에서 EONU로 향하는 두 번째 흐름 강조.':'세 사람의 정보와 안내를 연결.'}">
      <svg class="tri-lines" viewBox="0 0 640 360" aria-hidden="true"><path class="outer" d="M100 180 530 62 530 298Z"/><path class="edge doctor" d="M177 180H270"/><path class="edge patient" d="M455 100 371 152"/><path class="edge guardian" d="M455 260 371 208"/><path class="arrowhead doctor" d="m257 172 13 8-13 8"/><path class="arrowhead patient" d="m376 139-5 13 14-1"/><path class="arrowhead guardian" d="m385 208-14 0 5 13"/></svg>
      ${node('node-doctor','doctor','의료진','질문 · 정보 · 관리 안내')}
      <div class="tri-center"><b>EONU</b><span>확인하고 연결</span></div>
      ${node('node-patient','person','환자','일상 경험 · 걱정')}
      ${node('node-guardian','family','보호자','관찰 · 도움')}
      <span class="edge-label label-one">① 병원의 기준</span><span class="edge-label label-two">② 일상의 정보</span>
    </div>`;
  };
  E.renderSlide = (s, theme='design') => `<article class="slide ${theme}" data-slide="${s.id}" aria-label="${s.id}. ${E.esc(s.title.replace(/<[^>]*>/g,''))}">
    <header class="slide-header"><span class="section-label">${s.id} / ${s.section}</span><span class="brand">EONU<span>이어온유</span></span></header>
    <div class="heading"><h1>${s.title}</h1><p class="subtitle">${s.subtitle}</p></div>
    <main class="slide-body layout-${s.id}">${s.content}</main>
    <footer class="slide-footer"><span>${s.note}</span><span class="page-number">${s.id}<i>/ 12</i></span></footer>
  </article>`;
})();
