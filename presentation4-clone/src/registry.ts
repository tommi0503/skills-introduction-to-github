import a from './decks/group-a'
import b from './decks/group-b'
import c from './decks/group-c'
export const decks=[...a,...b,...c]

declare global { interface Window { __presentationDecks: typeof decks } }
window.__presentationDecks=decks
