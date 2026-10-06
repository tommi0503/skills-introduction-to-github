import {useEffect,useState,useRef} from 'react'
import {pages,decks,pageTitle} from './registry'
import {PageCanvas,Thumbnail} from './ui'
import type {Side} from './model'
function GalleryPreview({page}:{page:Side}){
 const ref=useRef<HTMLDivElement>(null),[visible,setVisible]=useState(false)
 useEffect(()=>{const observer=new IntersectionObserver(entries=>{if(entries.some(e=>e.isIntersecting)){setVisible(true);observer.disconnect()}},{rootMargin:'400px'});if(ref.current)observer.observe(ref.current);return()=>observer.disconnect()},[])
 return <div ref={ref} style={{width:200,height:142.1875,background:'#eef0f3'}}>{visible&&<Thumbnail page={page} width={200}/>}</div>
}
export default function App(){
 const [hash,setHash]=useState(location.hash)
 useEffect(()=>{const change=()=>setHash(location.hash);addEventListener('hashchange',change);return()=>removeEventListener('hashchange',change)},[])
 const id=hash.match(/^#\/page\/(\d{3})/)?.[1],page=pages.find(p=>p.id===id)
 if(page)return <PageCanvas page={page}/>
 return <main className="gallery"><h1>리플렛 UI · 102개 화면</h1><p>51개 양면 리플렛 · 1280 × 910 · 사진과 복잡한 그래픽은 연회색으로 표시합니다.</p><div className="brochure-grid">{decks.map(d=><section className="brochure-card" key={d.id}><header>{d.id} · {d.title}</header><div style={{display:'flex',gap:10}}>{d.pages.map(p=><a href={`#/page/${p.id}`} key={p.id} style={{color:'inherit',textDecoration:'none'}}><GalleryPreview page={p}/><div style={{fontSize:12,marginTop:8}}>{p.id} · {Number(p.id)%2?'앞면':'뒷면'}</div></a>)}</div></section>)}</div></main>
}
