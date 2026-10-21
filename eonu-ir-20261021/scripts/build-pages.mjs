import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const context = {window:{}, console};
context.globalThis = context.window;
vm.createContext(context);
for (const source of ['components.js', 'slides.js']) {
  vm.runInContext(await fs.readFile(path.join(root, 'src', source), 'utf8'), context, {filename:source});
}
const EONU = context.window.EONU;
if (!EONU || !Array.isArray(EONU.slides) || EONU.slides.length !== 12 || typeof EONU.renderSlide !== 'function') throw new Error('Expected window.EONU with 12 slides and renderSlide().');
const escape = text => String(text ?? '').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const plain = text => String(text ?? '').replace(/<[^>]+>/g,'');
const baseStyle = `
  html,body{margin:0;padding:0;background:#eeedf1}
  body{font-family:Pretendard,sans-serif}
  .standalone-shell{width:1280px;height:720px;position:relative;margin:0 auto;transform-origin:0 0}
  .standalone-shell>.slide{margin:0!important;box-shadow:none!important}
  .standalone-wrap{width:1280px;height:720px;margin:0 auto}
  .standalone-navigation{padding:14px;display:flex;justify-content:center;gap:24px;font-size:13px;font-family:sans-serif}
  .standalone-navigation a{color:#626cab;text-decoration:none}
  @page{size:1280px 720px;margin:0}
  @media print{html,body{width:1280px!important;background:white;margin:0!important;padding:0!important}.standalone-wrap,.standalone-shell{width:1280px!important;height:720px!important;transform:none!important;margin:0!important}.standalone-navigation{display:none!important}.slide{break-inside:avoid;page-break-inside:avoid;break-after:page;page-break-after:always;margin:0!important;box-shadow:none!important}.slide:last-child{break-after:auto;page-break-after:auto}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
`;
const head = (title, extra='') => `<!doctype html>\n<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(title)}</title><link rel="stylesheet" href="../src/slides.css"><style>${baseStyle}${extra}</style></head>`;
const fitScript = `<script>(()=>{const shell=document.querySelector('.standalone-shell'),wrap=document.querySelector('.standalone-wrap');function fit(){const scale=Math.min(1,innerWidth/1280);shell.style.transform='scale('+scale+')';wrap.style.width=(1280*scale)+'px';wrap.style.height=(720*scale)+'px';}addEventListener('resize',fit);fit();})();</script>`;
const manifest = [];
for (const theme of ['wireframe','design']) {
  const label = theme === 'design' ? '디자인 시안' : '와이어프레임';
  const folder = path.join(root,theme);
  await fs.mkdir(folder,{recursive:true});
  for (const [index, slide] of EONU.slides.entries()) {
    const id = String(slide.id || index + 1).padStart(2,'0');
    const previous = index ? `${String(EONU.slides[index-1].id || index).padStart(2,'0')}.html` : null;
    const next = index < 11 ? `${String(EONU.slides[index+1].id || index+2).padStart(2,'0')}.html` : null;
    const navigation = `<nav class="standalone-navigation" aria-label="페이지 이동">${previous?`<a href="${previous}">← 이전</a>`:'<span>첫 페이지</span>'}<a href="../index.html#/${theme}/${id}">뷰어로 돌아가기 · ${index+1} / 12</a>${next?`<a href="${next}">다음 →</a>`:'<span>마지막 페이지</span>'}</nav>`;
    const html = `${head(`EONU · ${label} ${id} · ${plain(slide.title)}`)}<body class="standalone-page"><main class="standalone-wrap"><div class="standalone-shell">${EONU.renderSlide(slide,theme)}</div></main>${navigation}${fitScript}</body></html>\n`;
    await fs.writeFile(path.join(folder,`${id}.html`),html);
    manifest.push({theme,id,title:plain(slide.title),path:`${theme}/${id}.html`,width:1280,height:720});
  }
  const print = `${head(`EONU · ${label} · 전체 12장`,'.print-deck{width:1280px;margin:0 auto}.print-deck>.slide{margin:0!important;box-shadow:none!important}@media screen{.print-deck>.slide{margin-bottom:24px!important}}@media print{.print-deck{margin:0;width:1280px}}')}<body class="print-page"><main class="print-deck">${EONU.slides.map(slide=>EONU.renderSlide(slide,theme)).join('\n')}</main></body></html>\n`;
  await fs.writeFile(path.join(folder,'print.html'),print);
}
await fs.writeFile(path.join(root,'slide-manifest.json'),JSON.stringify({canvas:[1280,720],slides:12,variants:2,files:manifest},null,2)+'\n');
console.log('Generated 24 standalone slide HTML files, 2 print HTML files, and slide-manifest.json.');
