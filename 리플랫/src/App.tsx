import {useEffect,useState} from 'react'
import {brochures} from './registry'
import {PageCanvas,Thumbnail} from './ui'
export default function App(){
 const [route,setRoute]=useState(location.hash.slice(2));useEffect(()=>{const update=()=>setRoute(location.hash.slice(2));addEventListener('hashchange',update);return()=>removeEventListener('hashchange',update)},[])
 const [mode,id,pageId]=route.split('/'),brochure=brochures.find(b=>b.id===id)
 if(mode==='page'&&brochure){const page=brochure.panels.find(p=>p.id===pageId);if(page)return <div data-brochure={id}><PageCanvas page={page}/></div>}
 if(mode==='side'&&brochure){const page=brochure.sides.find(p=>p.id===pageId);if(page)return <div data-brochure={id}><PageCanvas page={page}/></div>}
 if(brochure)return <><header className="toolbar"><a href="#/">← 전체 목록</a><h1>{brochure.title}</h1><a href={`#/brochure/${id}`}>접지면 6페이지</a><a href={`#/unfold/${id}`}>앞·뒷면 펼치기</a><a href={`#/compare/${id}`}>원본 비교</a></header>{mode==='compare'?<div className="compare-list">{brochure.sides.map(s=><section key={s.id}><h2>{s.id==='s01'?'앞면':'뒷면'}</h2><div className="compare-row"><img src={s.reference} alt={`${brochure.title} ${s.id} 원본`}/><Thumbnail page={s} width={600}/></div></section>)}</div>:<div className="page-grid">{(mode==='unfold'?brochure.sides:brochure.panels).map(p=><a href={`#/${mode==='unfold'?'side':'page'}/${id}/${p.id}`} key={p.id}><span>{p.id}</span><Thumbnail page={p} width={600}/></a>)}</div>}</>
 return <main className="gallery"><h1>리플랫</h1><p>3단 브로셔 72종 · 접지면 432페이지 · 1280 × 720</p><div className="brochure-grid">{brochures.map(b=><a className="brochure-card" href={`#/brochure/${b.id}`} key={b.id}><header><strong>{b.id} · {b.title}</strong><span>앞·뒤 6페이지</span></header><Thumbnail page={b.sides[0]} width={400}/></a>)}</div></main>
}
