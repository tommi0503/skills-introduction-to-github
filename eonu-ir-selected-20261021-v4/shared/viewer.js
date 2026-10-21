/* Local, offline review viewer. All slide, preview, PDF and font paths are relative. */
(() => {
  'use strict';
  const catalog = window.IR_CATALOG;
  const deck = catalog.concepts.find(item => item.id === 'final') || catalog.concepts[0];
  const main = document.querySelector('#main');
  const drawer = document.querySelector('#drawer');
  const count = deck.slides.length;
  const key = 'eonu-selected-unified-review-20261021-v4';
  const pad = value => String(value).padStart(2, '0');
  const esc = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[char]));
  const plain = value => String(value ?? '').replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
  const topic = page => catalog.topics?.[page - 1] || plain(deck.slides[page - 1].title);
  const source = page => {
    const selected = String(deck.slides[page - 1].source || ['D','A','A','v3','A','v3','A','v3','v3','E','A','D'][page - 1]);
    return selected.toLowerCase() === 'v3' ? 'v3' : selected.toUpperCase();
  };
  let reviews = {}, storageOK = true, drawerOpen = false, presenting = false, toastTimer;
  let state = {page: 1, mode: 'design', layout: 'focus'};
  try {
    const saved = JSON.parse(localStorage.getItem(key) || '{}');
    if (saved && typeof saved === 'object' && !Array.isArray(saved)) reviews = saved;
  } catch { storageOK = false; }
  const slide = () => deck.slides[state.page - 1];
  const reviewKey = () => `final-${pad(state.page)}`;
  const path = (mode = state.mode, page = state.page) => `concepts/final/${mode}/${pad(page)}.html`;
  const preview = (page = state.page, mode = state.mode) => `concepts/final/previews/${mode}/${pad(page)}.png`;
  function route(overrides = {}) {
    const next = {...state, ...overrides};
    return `#view=final&page=${pad(next.page)}&mode=${next.mode}&layout=${next.layout}`;
  }
  function go(overrides) {
    const hash = route(overrides);
    if (location.hash === hash) render();
    else location.hash = hash;
  }
  function readHash() {
    const params = new URLSearchParams(location.hash.slice(1));
    state = {
      page: Math.max(1, Math.min(count, parseInt(params.get('page'), 10) || 1)),
      mode: params.get('mode') === 'wireframe' ? 'wireframe' : 'design',
      layout: ['focus','overview','compare'].includes(params.get('layout')) ? params.get('layout') : 'focus'
    };
  }
  function notify(message) {
    clearTimeout(toastTimer);
    const toast = document.querySelector('#toast');
    toast.textContent = message;
    toast.classList.add('show');
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2800);
  }
  function controls() {
    return `<div class="page-controls"><button data-action="prev" aria-label="이전 슬라이드" ${state.page === 1 ? 'disabled' : ''}>‹</button><b>${pad(state.page)} <span>/ ${pad(count)}</span></b><button data-action="next" aria-label="다음 슬라이드" ${state.page === count ? 'disabled' : ''}>›</button></div>`;
  }
  function toolbar() {
    return `<div class="workspace-top"><div class="toolbar"><div class="toolbar-left"><div class="segmented" aria-label="슬라이드 종류"><button data-mode="design" class="${state.mode === 'design' ? 'active' : ''}" aria-pressed="${state.mode === 'design'}">시안</button><button data-mode="wireframe" class="${state.mode === 'wireframe' ? 'active' : ''}" aria-pressed="${state.mode === 'wireframe'}">와이어프레임</button></div><select id="pageSelect" aria-label="슬라이드 선택">${deck.slides.map((item, index) => `<option value="${index + 1}" ${state.page === index + 1 ? 'selected' : ''}>${pad(index + 1)} · ${esc(topic(index + 1))}</option>`).join('')}</select></div><div class="toolbar-right"><button data-layout="focus" class="${state.layout === 'focus' ? 'active' : ''}" aria-pressed="${state.layout === 'focus'}" title="한 장 크게 보기">한 장 보기</button><a href="concepts/final/pdfs/${state.mode}.pdf" target="_blank" rel="noopener">PDF ↗</a><button data-action="notes" aria-expanded="${drawerOpen}" aria-controls="drawer" title="발표 대본과 검수 메모 (N)">대본·메모</button><button data-action="present" title="발표 화면 (F)">발표 ⛶</button></div></div></div>`;
  }
  function renderFocus() {
    main.innerHTML = toolbar() + `<div class="focus-body"><nav class="thumb-rail" aria-label="12장 슬라이드 목록">${deck.slides.map((item, index) => `<button class="thumb" data-page="${index + 1}" aria-current="${index + 1 === state.page}" aria-label="${pad(index + 1)} ${esc(topic(index + 1))}"><img src="${preview(index + 1)}" alt="" loading="lazy"><span>${pad(index + 1)} · ${esc(topic(index + 1))}</span>${hasReview(index + 1) ? '<i class="review-dot" title="검수 메모 있음"></i>' : ''}</button>`).join('')}</nav><section class="slide-workspace" aria-label="슬라이드"><div class="slide-viewport"><iframe id="slideFrame" src="${path()}" title="${state.page}번 ${esc(topic(state.page))} ${state.mode === 'design' ? '시안' : '와이어프레임'}"></iframe></div><div class="slide-bottom"><span class="slide-caption">${esc(plain(slide().title))}</span>${controls()}</div><p class="keyboard-hint">← → 이동 <span>G 전체 보기 · C 비교 · N 메모 · F 발표</span></p></section></div>`;
    requestAnimationFrame(() => main.querySelector('.thumb[aria-current=true]')?.scrollIntoView({block:'nearest', inline:'nearest'}));
  }
  function renderOverview() {
    main.innerHTML = toolbar() + `<div class="view-intro"><div><p class="eyebrow">EONU INVESTOR PRESENTATION</p><h1>12장의 이야기</h1><p>페이지를 선택하면 크게 볼 수 있습니다.</p></div><span class="view-label">${state.mode === 'design' ? '시안' : '와이어프레임'}</span></div><section class="overview" aria-label="전체 12장">${deck.slides.map((item, index) => `<button data-page="${index + 1}" data-open="focus" aria-label="${pad(index + 1)} ${esc(topic(index + 1))} 크게 보기"><div class="overview-image"><img src="${preview(index + 1)}" alt="${esc(plain(item.title))}" loading="lazy">${hasReview(index + 1) ? '<i class="review-dot" title="검수 메모 있음"></i>' : ''}</div><span><b>${pad(index + 1)}</b>${esc(topic(index + 1))}</span></button>`).join('')}</section>`;
  }
  function renderCompare() {
    main.innerHTML = toolbar() + `<div class="view-intro comparison-intro"><div><p class="eyebrow">DESIGN & WIREFRAME</p><h1>${pad(state.page)} · ${esc(topic(state.page))}</h1><p>같은 페이지의 구성과 완성 시안을 확인하세요. 화면을 누르면 크게 열립니다.</p></div>${controls()}</div><section class="compare-grid" aria-label="같은 페이지의 시안과 와이어프레임 비교">${[{id:'design', label:'시안', detail:'통합 디자인'}, {id:'wireframe', label:'와이어프레임', detail:'콘텐츠와 배치 구조'}].map(mode => `<article class="compare-card"><div class="compare-title"><h2>${mode.label}</h2><a href="${route({mode:mode.id, layout:'focus'})}">크게 보기 ↗</a></div><div class="compare-image"><iframe src="${path(mode.id)}" title="${state.page}번 ${mode.label} 비교" tabindex="-1"></iframe><a href="${route({mode:mode.id, layout:'focus'})}" aria-label="${state.page}번 ${mode.label} 크게 보기"></a></div><p class="compare-subtitle">${mode.detail}</p></article>`).join('')}</section>`;
  }
  function hasReview(page) {
    const review = reviews[`final-${pad(page)}`];
    return Boolean(review?.verdict || review?.comment?.trim());
  }
  function renderDrawer() {
    document.querySelector('[data-action="notes"]')?.setAttribute('aria-expanded', String(drawerOpen));
    drawer.hidden = !drawerOpen;
    document.body.classList.toggle('drawer-open', drawerOpen);
    if (!drawerOpen) return;
    const item = slide(), review = reviews[reviewKey()] || {};
    drawer.innerHTML = `<div class="drawer-top"><div><p class="eyebrow">${pad(state.page)} / ${pad(count)} · EONU IR</p><h2>${esc(topic(state.page))}</h2></div><button data-action="close-notes" aria-label="대본과 메모 닫기">✕</button></div><div class="source-note"><span>선택한 구성</span><strong>${esc(source(state.page))}</strong><p>선택한 원안의 구성을 통합된 화이트·블루 디자인으로 정리한 페이지입니다.</p></div><h3>이 페이지 검수</h3><div class="verdicts">${['좋아요','수정 필요','보류'].map(verdict => `<button data-verdict="${verdict}" class="${review.verdict === verdict ? 'active' : ''}" aria-pressed="${review.verdict === verdict}">${verdict}</button>`).join('')}</div><label for="reviewNote">수정할 위치나 원하는 방향</label><textarea id="reviewNote" placeholder="예: 제목을 더 짧게, 오른쪽 이미지 영역을 더 크게…">${esc(review.comment || '')}</textarea><p class="save-status" id="saveStatus">${storageOK ? '이 브라우저에 자동 저장됩니다.' : '브라우저 저장이 제한됩니다. 메모를 내보내 주세요.'}</p><h3>발표 대본</h3><p class="script">${esc(item.talk || '별도 대본이 등록되지 않았습니다.')}</p>${item.note ? `<h3>자료·확인 범위</h3><p class="evidence">${esc(item.note)}</p>` : ''}<a href="${path()}" target="_blank" rel="noopener">이 페이지 HTML 열기 ↗</a>`;
  }
  function readyFrames() {
    for (const frame of main.querySelectorAll('iframe')) {
      const reveal = () => {
        try {
          const doc = frame.contentDocument;
          if (!doc || doc.URL === 'about:blank') return;
          doc.fonts.ready.then(() => frame.classList.add('ready'));
        } catch { frame.classList.add('ready'); }
      };
      frame.addEventListener('load', reveal, {once:true});
      try { if (frame.contentDocument?.readyState === 'complete') reveal(); } catch { /* Wait for load. */ }
    }
  }
  function render() {
    document.title = `${pad(state.page)} · ${topic(state.page)} — EONU IR`;
    document.querySelector('#overviewButton').setAttribute('aria-pressed', String(state.layout === 'overview'));
    document.querySelector('#compareButton').setAttribute('aria-pressed', String(state.layout === 'compare'));
    if (state.layout === 'overview') renderOverview();
    else if (state.layout === 'compare') renderCompare();
    else renderFocus();
    readyFrames();
    renderDrawer();
  }
  function saveReview(patch) {
    const id = reviewKey();
    reviews[id] = {...reviews[id], ...patch, concept:'final', page:state.page, source:source(state.page), title:topic(state.page), updatedAt:new Date().toISOString()};
    try { localStorage.setItem(key, JSON.stringify(reviews)); storageOK = true; }
    catch { storageOK = false; }
    const status = document.querySelector('#saveStatus');
    if (status) status.textContent = storageOK ? '저장됨 · 이 브라우저에 보관' : '임시 보관 중 · 메모 내보내기로 저장하세요';
    const thumb = main.querySelector(`.thumb[data-page="${state.page}"]`);
    if (thumb && !thumb.querySelector('.review-dot') && hasReview(state.page)) thumb.insertAdjacentHTML('beforeend', '<i class="review-dot" title="검수 메모 있음"></i>');
    if (thumb && !hasReview(state.page)) thumb.querySelector('.review-dot')?.remove();
  }
  function exportReviews() {
    const payload = {project:'EONU IR · 선택안 통합', version:'20261021-v4', exportedAt:new Date().toISOString(), composition:deck.slides.map((item,index) => ({page:index + 1, source:source(index + 1)})), reviews:Object.values(reviews).filter(item => item.verdict || item.comment?.trim())};
    const blob = new Blob([JSON.stringify(payload, null, 2)], {type:'application/json'});
    const objectURL = URL.createObjectURL(blob), link = document.createElement('a');
    link.href = objectURL;
    link.download = 'eonu-ir-selected-review.json';
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(objectURL), 2000);
    notify(`${payload.reviews.length}개 페이지의 검수 메모를 내보냈습니다.`);
  }
  function advance(delta) { go({page:Math.max(1, Math.min(count, state.page + delta))}); }
  async function present() {
    if (presenting) {
      presenting = false;
      document.body.classList.remove('presenting');
      if (document.fullscreenElement) { try { await document.exitFullscreen(); } catch {} }
      return;
    }
    if (state.layout !== 'focus') {
      state.layout = 'focus';
      history.replaceState(null, '', route());
      render();
    }
    drawerOpen = false;
    renderDrawer();
    presenting = true;
    document.body.classList.add('presenting');
    try { await document.documentElement.requestFullscreen(); }
    catch { notify('발표 화면입니다. Esc 키로 종료합니다.'); }
  }
  function action(name) {
    if (name === 'prev') advance(-1);
    else if (name === 'next') advance(1);
    else if (name === 'notes') { drawerOpen = !drawerOpen; renderDrawer(); }
    else if (name === 'close-notes') { drawerOpen = false; renderDrawer(); }
    else if (name === 'present') present();
  }
  document.addEventListener('fullscreenchange', () => {
    if (!document.fullscreenElement && presenting) {
      presenting = false;
      document.body.classList.remove('presenting');
    }
  });
  document.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button || button.disabled) return;
    if (button.id === 'overviewButton') go({layout:state.layout === 'overview' ? 'focus' : 'overview'});
    else if (button.id === 'compareButton') go({layout:state.layout === 'compare' ? 'focus' : 'compare'});
    else if (button.id === 'exportButton') exportReviews();
    else if (button.dataset.action) action(button.dataset.action);
    else if (button.dataset.mode) go({mode:button.dataset.mode});
    else if (button.dataset.layout) go({layout:button.dataset.layout});
    else if (button.dataset.page) go({page:Number(button.dataset.page), layout:button.dataset.open || state.layout});
    else if (button.dataset.verdict) {
      saveReview({verdict:reviews[reviewKey()]?.verdict === button.dataset.verdict ? '' : button.dataset.verdict});
      renderDrawer();
    }
  });
  document.addEventListener('change', event => { if (event.target.id === 'pageSelect') go({page:Number(event.target.value)}); });
  document.addEventListener('input', event => { if (event.target.id === 'reviewNote') saveReview({comment:event.target.value}); });
  function handleKey(keyValue, event) {
    if (keyValue === 'Escape') {
      if (presenting) present();
      else { drawerOpen = false; renderDrawer(); }
      return;
    }
    if (['ArrowRight','PageDown'].includes(keyValue)) { event?.preventDefault(); advance(1); }
    else if (['ArrowLeft','PageUp'].includes(keyValue)) { event?.preventDefault(); advance(-1); }
    else if (keyValue === 'Home') { event?.preventDefault(); go({page:1}); }
    else if (keyValue === 'End') { event?.preventDefault(); go({page:count}); }
    else if (keyValue.toLowerCase() === 'n') action('notes');
    else if (keyValue.toLowerCase() === 'f') present();
    else if (keyValue.toLowerCase() === 'g' && !presenting) go({layout:state.layout === 'overview' ? 'focus' : 'overview'});
    else if (keyValue.toLowerCase() === 'c' && !presenting) go({layout:state.layout === 'compare' ? 'focus' : 'compare'});
  }
  document.addEventListener('keydown', event => {
    if (event.ctrlKey || event.metaKey || event.altKey || event.target.isContentEditable || ['INPUT','TEXTAREA','SELECT'].includes(event.target.tagName)) return;
    handleKey(event.key, event);
  });
  addEventListener('message', event => {
    if (event.data?.type === 'eonu-key' && typeof event.data.key === 'string' && [...main.querySelectorAll('iframe')].some(frame => frame.contentWindow === event.source)) handleKey(event.data.key);
  });
  addEventListener('hashchange', () => { readHash(); render(); });
  readHash();
  render();
})();
