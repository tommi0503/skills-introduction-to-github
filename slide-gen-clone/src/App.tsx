import {useEffect,useState} from 'react'
import {decks} from './registry'
import {ScaledSlide,SlideCanvas,ReferenceBoard,ScaledReferenceBoard,sourceVisibility} from './ui'
import type {Deck} from './model'
function Board({deck,width=600}:{deck:Deck;width?:number}){return <div className="deck-board" style={{gridTemplateColumns:`repeat(${deck.columns??2},${width}px)`}}>{deck.slides.map((s,index)=><ScaledSlide slide={s} width={width} visible={sourceVisibility(deck,index)} key={s.id}/>)}</div>}
export default function App(){
 const [route,setRoute]=useState(location.hash.slice(2));useEffect(()=>{const f=()=>setRoute(location.hash.slice(2));addEventListener('hashchange',f);return()=>removeEventListener('hashchange',f)},[])
 const [mode,id,sid]=route.split('/');const deck=decks.find(d=>d.id===id)
 if(mode==='slide'&&deck){const slide=deck.slides.find(s=>s.id===sid)??deck.slides[0];return <div className="slide-view"><SlideCanvas slide={slide} visible={sourceVisibility(deck,deck.slides.indexOf(slide))}/></div>}
 if(mode==='board'&&deck)return <ReferenceBoard deck={deck}/>
 if(deck)return <><header className="toolbar"><a href="#/">← 갤러리</a><h1>{deck.id} · {deck.title}</h1><a href={`#/deck/${deck.id}`}>슬라이드</a><a href={`#/compare/${deck.id}`}>원본 비교</a><span>{deck.slides.length} slides · 1280 × 720</span></header>{mode==='compare'?<div className="comparison"><img src={`/reference/${deck.id}.jpg`} alt="원본 참고 이미지"/><ScaledReferenceBoard deck={deck}/></div>:<Board deck={deck}/>}</>
 return <main className="gallery"><h1>Slide Gen Clone</h1><p className="intro">32개 참고 이미지 · {decks.reduce((n,d)=>n+d.slides.length,0)}개 슬라이드 · 1280 × 720<br/>사진과 복잡한 그래픽은 연한 회색 플레이스홀더로 표시합니다.</p><div className="deck-grid">{decks.map(d=><a className="deck-card" href={`#/deck/${d.id}`} key={d.id}><header><strong>{d.id} · {d.title}</strong><span>{d.slides.length} slides</span></header><div className="thumb"><ScaledSlide slide={d.slides[0]} width={440} visible={sourceVisibility(d,0)}/></div></a>)}</div></main>
}
