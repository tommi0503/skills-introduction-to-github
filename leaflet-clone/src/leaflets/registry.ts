import type { LeafletDefinition } from '../ui'

/** Auto-discovers src/leaflets/lNN/index.tsx — no edits needed to add a leaflet. */
const modules = import.meta.glob<{ default: LeafletDefinition }>('./l*/index.tsx', { eager: true })

export const leaflets: LeafletDefinition[] = Object.values(modules)
  .map((m) => m.default)
  .sort((a, b) => a.id.localeCompare(b.id))

export const findLeaflet = (id: string) => leaflets.find((l) => l.id === id)
