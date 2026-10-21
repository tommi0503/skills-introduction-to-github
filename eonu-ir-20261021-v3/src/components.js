(function(){
  const E=window.EONU={};
  E.esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  E.icon=(name,cls='')=>{
    const paths={
      person:'<circle cx="12" cy="8" r="4"/><path d="M4 22v-4a8 8 0 0 1 16 0v4"/>',
      people:'<circle cx="8" cy="8" r="4"/><path d="M2 22v-4a6 6 0 0 1 12 0v4M18 4a4 4 0 0 1 0 8m0 4a4 4 0 0 1 4 4v2"/>',
      doctor:'<path d="M4 2v8a6 6 0 0 0 12 0V2M2 2h4m8 0h4m-8 14v2a4 4 0 0 0 8 0v-2"/><circle cx="18" cy="12" r="4"/>',
      arrow:'<path d="M2 12h20m-8-8 8 8-8 8"/>',
      check:'<path d="m4 12 6 6L22 4"/>',
      clock:'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
      heart:'<path d="M12 22 2 12C-4 4 6-2 12 6c6-8 16-2 10 6Z"/>',
      chart:'<path d="M2 2v20h20M6 16l4-6 4 2 8-8"/>',
      message:'<path d="M4 2h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-8l-6 4v-4H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Z"/><path d="M6 8h12M6 12h8"/>',
      record:'<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 8h8M8 12h8M8 16h4"/>',
      link:'<path d="m8 8 4-4a6 6 0 0 1 8 8l-4 4M16 16l-4 4a6 6 0 0 1-8-8l4-4m0 8 8-8"/>',
      shield:'<path d="m12 2 10 4v6c0 6-10 10-10 10S2 18 2 12V6zM6 12l4 4 8-8"/>',
      hospital:'<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 8h8m-4-4v8M8 22v-6h8v6"/>',
      calendar:'<rect x="2" y="4" width="20" height="18" rx="2"/><path d="M6 2v6m12-6v6M2 10h20m-16 4h4m4 0h4m-12 4h4"/>',
      target:'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><path d="m12 12 10-10m-6 0h6v6"/>',
      code:'<path d="m8 6-6 6 6 6m8-12 6 6-6 6M14 2l-4 20"/>',
      device:'<rect x="6" y="2" width="12" height="20" rx="4"/><path d="M10 6h4M10 18h4"/>',
      mic:'<rect x="8" y="2" width="8" height="14" rx="4"/><path d="M4 10v2a8 8 0 0 0 16 0v-2M12 20v2M8 22h8"/>'
    };
    return `<svg class="icon ${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths[name]||paths.record}</svg>`;
  };
  E.ph=(label,cls='')=>`<div class="placeholder ${cls}" role="img" aria-label="${E.esc(label)} 이미지 자리"><span>${label}</span></div>`;
  E.badge=(name,cls='')=>`<span class="icon-badge ${cls}">${E.icon(name)}</span>`;
  E.chip=(text,cls='')=>`<span class="chip ${cls}">${text}</span>`;
  E.arrow=()=>`<span class="arrow">${E.icon('arrow')}</span>`;
  E.stage=()=>'<div class="stage" aria-hidden="true"></div>';
  E.miniTriangle=(active='all')=>`<div class="mini-triangle active-${active}" role="img" aria-label="의료진, 환자·보호자가 EONU로 연결되는 구조"><svg viewBox="0 0 288 96" aria-hidden="true"><path class="d-line" d="M64 48h48m-8-8 8 8-8 8"/><path class="p-line" d="m232 20-56 24 12-2m-12 2 6-10M232 76l-56-24 12 2m-12-2 6 10"/></svg><span class="mini-doctor">의료진</span><b>EONU</b><span class="mini-patient">환자</span><span class="mini-family">보호자</span></div>`;
  E.renderSlide=(s,theme='design')=>{
    const bookend=['01','12'].includes(s.id);
    return `<article class="slide ${theme} page-${s.id}${bookend?' bookend':''}" data-slide="${s.id}" aria-label="${s.id}. ${E.esc(s.title.replace(/<[^>]*>/g,' '))}">${bookend?'':`<header class="slide-header"><span class="section-label">${s.section}</span></header><div class="heading"><h1>${s.title}</h1>${s.subtitle?`<p class="subtitle">${s.subtitle}</p>`:''}</div>`}<div class="slide-body layout-${s.id}">${s.content}</div>${bookend?'':`<footer class="slide-footer"><span class="source-note">${s.caption||''}</span><span class="footer-brand">EONU</span><span class="page-number">${s.id}</span></footer>`}</article>`;
  };
})();
