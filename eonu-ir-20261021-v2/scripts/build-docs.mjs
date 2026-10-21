import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
const require=createRequire(import.meta.url);
const {marked}=await import(require.resolve('marked'));
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const files=[['planning-review.md','기획 검토와 개선'],['revised-script.md','12장 개선 기획·발표 대본'],['evidence-register.md','근거·미확정 항목']];
let sections='';
for(let i=0;i<files.length;i++)sections+=`<section id="doc-${i}">${marked.parse(await fs.readFile(path.join(root,'docs',files[i][0]),'utf8'))}</section>`;
const html=`<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>EONU · IR 기획 검토와 개선본</title><style>
@font-face{font-family:Pretendard;src:url('../assets/fonts/PretendardVariable.woff2');font-weight:100 900}*{box-sizing:border-box}body{margin:0;background:#f6f5f7;color:#292a31;font:16px/28px Pretendard,sans-serif}nav{position:sticky;top:0;background:#fff;border-bottom:2px solid #e3e3e9;padding:18px 5vw;display:flex;gap:26px;z-index:2}a{color:#6377db;text-decoration:none}main{max-width:1120px;padding:50px 50px 80px;background:#fff;margin:36px auto}section+section{border-top:4px solid #dfe4ff;margin-top:70px;padding-top:36px}h1{font-size:34px;line-height:48px}h2{margin-top:42px;font-size:24px}h3{font-size:20px}p{margin:12px 0}strong{font-weight:700}table{border-collapse:collapse;width:100%;font-size:14px;line-height:24px;margin:22px 0}th{text-align:left;background:#edf0ff;color:#4c5990}th,td{border:2px solid #e2e3e8;padding:12px;vertical-align:top}code{font-family:inherit;font-size:14px;background:#f0f1f5;padding:2px 4px;border-radius:4px}li{margin:6px 0}section{scroll-margin-top:86px}@media(max-width:700px){main{padding:26px 18px}nav{gap:12px;font-size:12px;flex-wrap:wrap}table{font-size:12px}td,th{padding:6px}}@page{size:A4;margin:18mm 15mm}@media print{body{font-size:10px;line-height:20px;background:#fff}nav{display:none}main{margin:0;padding:0;max-width:none}h1{font-size:24px}h2{font-size:16px;margin-top:24px;break-after:avoid}h3{font-size:14px;break-after:avoid}table{font-size:8px}tr{break-inside:avoid}th,td{padding:6px}section+section{break-before:page;margin-top:0;padding-top:0;border:0}p,li{orphans:3;widows:3}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
</style></head><body><nav><a href="../index.html">← 슬라이드 뷰어</a>${files.map((f,i)=>`<a href="#doc-${i}">${f[1]}</a>`).join('')}<a href="../previews/eonu-planning.pdf">PDF 다운로드</a></nav><main>${sections}</main></body></html>`;
await fs.writeFile(path.join(root,'docs/planning.html'),html);
console.log('Built docs/planning.html from three Markdown documents.');
