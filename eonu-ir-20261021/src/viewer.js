(() => {
  'use strict';
  const {slides, renderSlide} = window.EONU;
  if (!Array.isArray(slides) || !slides.length || typeof renderSlide !== 'function') throw new Error('EONU 슬라이드 데이터가 없습니다.');
  const $ = id => document.getElementById(id);
  const state = {mode:'design', index:0, grid:false, notes:false};
  const labels = {design:'디자인 시안', wireframe:'와이어프레임'};
  const cleanText = value => String(value || '').replace(/<[^>]*>/g, '').replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ');
  const idFor = index => String(slides[index].id || index + 1).padStart(2, '0');

  slides.forEach((slide, index) => {
    const option = document.createElement('option');
    option.value = index;
    option.textContent = String(index+1).padStart(2,'0');
    $('page-select').append(option);
  });
  $('total-count').textContent = slides.length;

  function setHash(mode, index) {
    const next = `#/${mode}/${idFor(Math.max(0, Math.min(slides.length - 1, index)))}`;
    if (location.hash === next) readHash(); else location.hash = next;
  }
  function readHash() {
    const match = location.hash.match(/^#\/?(design|wireframe)\/(\d{1,2})$/);
    if (match) {
      state.mode = match[1];
      const requested = slides.findIndex((slide, index) => idFor(index) === match[2].padStart(2,'0'));
      state.index = requested >= 0 ? requested : 0;
    } else {
      state.mode = 'design';
      state.index = 0;
    }
    render();
  }
  function fitSlides() {
    const main = document.querySelector('.viewer-main');
    const style = getComputedStyle(main);
    const availableWidth = main.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
    const headerHeight = document.querySelector('.viewer-topbar').offsetHeight;
    const footerHeight = document.querySelector('.viewer-footer').offsetHeight;
    const availableHeight = Math.max(150, window.innerHeight - headerHeight - footerHeight - parseFloat(style.paddingTop) - parseFloat(style.paddingBottom));
    const scale = Math.min(1, availableWidth / 1280, state.notes ? availableWidth / 1280 : availableHeight / 720);
    $('slide-wrap').style.width = `${1280 * scale}px`;
    $('slide-wrap').style.height = `${720 * scale}px`;
    $('slide-host').style.transform = `scale(${scale})`;
    document.querySelectorAll('.viewer-grid-frame').forEach(frame => {
      frame.firstElementChild.style.transform = `scale(${frame.clientWidth / 1280})`;
    });
  }
  function renderGrid() {
    $('grid').replaceChildren();
    slides.forEach((slide, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'viewer-grid-card';
      button.setAttribute('aria-label', `${index+1}장: ${cleanText(slide.title)}`);
      button.setAttribute('aria-current', String(index === state.index));
      const frame = document.createElement('div');
      frame.className = 'viewer-grid-frame';
      frame.setAttribute('aria-hidden', 'true');
      const host = document.createElement('div');
      host.className = 'viewer-grid-host';
      host.innerHTML = renderSlide(slide, state.mode);
      frame.append(host);
      const caption = document.createElement('div');
      caption.className = 'viewer-grid-caption';
      const number = document.createElement('span');
      number.className = 'viewer-grid-number';
      number.textContent = String(index+1).padStart(2,'0');
      const title = document.createElement('span');
      title.className = 'viewer-grid-title';
      title.textContent = cleanText(slide.title);
      caption.append(number, title);
      button.append(frame, caption);
      button.addEventListener('click', () => {state.grid = false; setHash(state.mode, index); window.scrollTo(0,0);});
      $('grid').append(button);
    });
  }
  function render() {
    const slide = slides[state.index];
    document.documentElement.dataset.viewerMode = state.mode;
    $('slide-host').innerHTML = renderSlide(slide, state.mode);
    $('presentation').hidden = state.grid;
    $('grid').hidden = !state.grid;
    $('notes').hidden = !state.notes || state.grid;
    $('grid-toggle').setAttribute('aria-pressed', String(state.grid));
    $('notes-toggle').setAttribute('aria-pressed', String(state.notes));
    document.querySelectorAll('[data-mode]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.mode === state.mode)));
    $('page-select').value = String(state.index);
    $('previous').disabled = state.index === 0;
    $('next').disabled = state.index === slides.length - 1;
    $('section-label').textContent = cleanText(slide.section);
    $('mode-label').textContent = labels[state.mode];
    $('single-link').href = `${state.mode}/${idFor(state.index)}.html`;
    $('print-link').href = `${state.mode}/print.html`;
    $('pdf-link').href = `previews/eonu-${state.mode}.pdf`;
    $('notes-title').textContent = `${String(state.index+1).padStart(2,'0')} · ${cleanText(slide.title)}`;
    $('notes-text').textContent = slide.talk || '발표 대본은 docs/revised-script.md에서 확인할 수 있습니다.';
    $('notes-source').textContent = cleanText(slide.note);
    document.title = `EONU · ${labels[state.mode]} · ${state.index+1}/${slides.length}`;
    $('announcement').textContent = `${labels[state.mode]}, ${state.index+1}장, ${cleanText(slide.title)}`;
    if (state.grid) renderGrid();
    requestAnimationFrame(fitSlides);
  }
  function move(delta) {setHash(state.mode, Math.max(0, Math.min(slides.length - 1, state.index + delta)));}
  $('previous').addEventListener('click', () => move(-1));
  $('next').addEventListener('click', () => move(1));
  $('page-select').addEventListener('change', event => setHash(state.mode, Number(event.target.value)));
  document.querySelectorAll('[data-mode]').forEach(button => button.addEventListener('click', () => setHash(button.dataset.mode, state.index)));
  $('grid-toggle').addEventListener('click', () => {state.grid = !state.grid; render();});
  $('notes-toggle').addEventListener('click', () => {state.notes = !state.notes; state.grid = false; render();});
  $('notes-close').addEventListener('click', () => {state.notes = false; render(); $('notes-toggle').focus();});
  window.addEventListener('hashchange', readHash);
  window.addEventListener('resize', fitSlides);
  document.addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey || /INPUT|SELECT|TEXTAREA/.test(event.target.tagName) || event.target.isContentEditable) return;
    if (event.key === 'ArrowLeft' || event.key === 'PageUp') {event.preventDefault(); move(-1);}
    else if (event.key === 'ArrowRight' || event.key === 'PageDown') {event.preventDefault(); move(1);}
    else if (event.key === 'Home') {event.preventDefault(); setHash(state.mode, 0);}
    else if (event.key === 'End') {event.preventDefault(); setHash(state.mode, slides.length-1);}
    else if (event.key.toLowerCase() === 'g') {state.grid = !state.grid; render();}
    else if (event.key.toLowerCase() === 'n') {state.notes = !state.notes; state.grid = false; render();}
    else if (event.key === 'Escape') {state.grid = false; state.notes = false; render();}
  });
  let touchStart = null;
  $('slide-wrap').addEventListener('touchstart', event => {if (event.touches.length === 1) touchStart = {x:event.touches[0].clientX,y:event.touches[0].clientY};}, {passive:true});
  $('slide-wrap').addEventListener('touchend', event => {
    if (!touchStart || !event.changedTouches.length) return;
    const dx = event.changedTouches[0].clientX - touchStart.x;
    const dy = event.changedTouches[0].clientY - touchStart.y;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy)*1.5) move(dx > 0 ? -1 : 1);
    touchStart = null;
  }, {passive:true});
  readHash();
  document.fonts.ready.then(fitSlides);
})();
