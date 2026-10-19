import React from 'react';
import {createRoot} from 'react-dom/client';
import './index.css';
const modules=import.meta.glob('./decks/d*.tsx',{eager:true});
const decks=Object.values(modules).map((m:any)=>m.default).filter(Boolean).sort((a:any,b:any)=>a.id.localeCompare(b.id));
const p=new URLSearchParams(location.search),deck=p.get('deck'),slide=p.get('slide'),mode=p.get('mode')||'replica';
const chosen=deck?decks.filter((d:any)=>d.id===deck):decks;
(window as any).__DECKS__=decks.map((d:any)=>({id:d.id,title:d.title,slides:d.slides.map((s:any)=>({id:s.id,title:s.title}))}));
function App(){return <><div className="toolbar" style={{display:slide?'none':undefined}}><b>REPORT FORGE</b><a href="/">전체 112장</a>{decks.map((d:any)=><a href={`/?deck=${d.id}`} key={d.id}>{d.id}</a>)}<a href="/outputs/assembled.html">라이브러리 조립본</a></div><main className={slide?'viewer':'gallery'} data-mode={mode}>{chosen.flatMap((d:any)=>d.slides.filter((s:any)=>!slide||s.id===slide).map((s:any)=><article key={d.id+s.id} data-deck={d.id} data-slide={s.id}>{!slide&&<h2>{d.id} · {s.id} — {s.title}</h2>}{s.render()}</article>))}</main></>}
createRoot(document.getElementById('root')!).render(<App/>);
