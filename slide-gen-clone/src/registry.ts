import type {Deck} from './model'
const modules=import.meta.glob<{default:Deck|Deck[]}>('./decks/*.ts',{eager:true})
export const decks=Object.values(modules).flatMap(m=>Array.isArray(m.default)?m.default:[m.default]).filter((deck):deck is Deck=>Boolean(deck)).sort((a,b)=>a.id.localeCompare(b.id))
