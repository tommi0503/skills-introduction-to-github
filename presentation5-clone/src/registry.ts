import a from './decks/group-a'
import ax from './decks/group-a-extra'
import b from './decks/group-b'
import bx from './decks/group-b-extra'
import c from './decks/group-c'
import cx from './decks/group-c-extra'
import type {Deck} from './model'
export const decks:Deck[]=[...a,...ax,...b,...bx,...c,...cx].sort((a,b)=>a.id.localeCompare(b.id))
declare global {interface Window {__presentationDecks:Deck[]}}
window.__presentationDecks=decks
