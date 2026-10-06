import type { DeckDefinition } from '../ui'
/** Auto-discovers src/decks/dNN/index.tsx. */
const modules = import.meta.glob<{ default: DeckDefinition }>('./d*/index.tsx', { eager: true })
export const decks: DeckDefinition[] = Object.values(modules).map((m) => m.default).sort((a, b) => a.id.localeCompare(b.id))
export const findDeck = (id: string) => decks.find((d) => d.id === id)
