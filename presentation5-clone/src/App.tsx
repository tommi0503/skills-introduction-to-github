import {useEffect,useState} from 'react'
import {decks} from './registry'
import {ScaledSlide,SlideCanvas} from './ui'
import type {Deck} from './model'
function Board({deck}:{deck:Deck}) {return <div className="deck-board" style={{gridTemplateColumns:'repeat(2,600px)'}}>{deck.slides.map(s=><section key={s.id}><p className="reference-label"><a href={`#/slide/${deck.id}/${s.id}`}>{s.id} · {s.title} ↗</a></p><ScaledSlide slide={s} width={600}/></section>)}</div>}
export default function App(){
 const [route,setRoute]=useState(location.hash.slice(2));useEffect(()=>{const f=()=>setRoute(location.hash.slice(2));addEventListener('hashchange',f);return()=>removeEventListener('hashchange',f)},[])
 const [mode,id,sid]=route.split('/'),deck=decks.find(d=>d.id===id)
 if(mode==='slide'&&deck){const slide=deck.slides.find(s=>s.id===sid)??deck.slides[0];return <div className="slide-view" data-deck={deck.id}><SlideCanvas slide={slide}/></div>}
 if(deck)return <><header className="toolbar"><a href="#/">← 갤러리</a><h1>{deck.id} · {deck.title}</h1><a href={`#/deck/${deck.id}`}>슬라이드</a><a href={`#/compare/${deck.id}`}>원본 비교</a><span>{deck.slides.length} slides · 1280 × 720</span></header>{mode==='compare'?<div className="compare-list">{deck.slides.map((s,i)=><section key={s.id}><p className="reference-label"><a href={`#/slide/${deck.id}/${s.id}`}>{deck.id}/{s.id} · {s.title} ↗</a> · 원본 / 구현</p><div className="compare-row"><img src={deck.references?.[i]} alt={`${s.title} 원본`}/><ScaledSlide slide={s} width={600}/></div></section>)}</div>:<Board deck={deck}/>}</>
 return <main className="gallery"><h1>Presentation 5 Clone</h1><p className="intro">{decks.length}개 덱 · {decks.reduce((n,d)=>n+d.slides.length,0)}개 슬라이드 · 1280 × 720<br/>사진과 복잡한 그래픽은 연한 회색 플레이스홀더로 표시합니다.</p><div className="deck-grid">{decks.map(d=><a className="deck-card" href={`#/deck/${d.id}`} key={d.id}><header><strong>{d.id} · {d.title}</strong><span>{d.slides.length} slides</span></header><div className="thumb"><ScaledSlide slide={d.slides[0]} width={440}/></div></a>)}</div></main>
}
