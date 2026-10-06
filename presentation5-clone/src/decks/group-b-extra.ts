import type {Deck, Slide} from '../model'
import {D} from '../primitives'
import manifest from '../../public/reference/groups/b.json'
import data from './group-b-extra-data.json'
// Per-page data uses reusable semantic charts, shapes, tables and actual DOM text.
const owned = new Set(['p055','p060','p100','p105'])
const pages = data as unknown as Record<string,Slide>
const decks:Deck[] = manifest.filter(d => owned.has(d.id)).map(d => D(d.id,d.title,d.slides.map(s => pages[d.id+'/'+s.id])))
export default decks
