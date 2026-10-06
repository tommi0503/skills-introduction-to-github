import type {Deck} from './model'
const modules=import.meta.glob<{default?:Deck[]}>('./decks/group-*.ts',{eager:true})
export const decks=Object.entries(modules).sort(([a],[b])=>a.localeCompare(b)).flatMap(([,module])=>module.default??[])
