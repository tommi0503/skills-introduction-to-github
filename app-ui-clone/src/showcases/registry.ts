import type { ShowcaseDefinition } from '../ui'

/**
 * Auto-discovers every showcase folder (src/showcases/sNN/index.tsx).
 * Adding a showcase never requires editing this file (Open/Closed).
 */
const modules = import.meta.glob<{ default: ShowcaseDefinition }>('./s*/index.tsx', { eager: true })

export const showcases: ShowcaseDefinition[] = Object.values(modules)
  .map((m) => m.default)
  .sort((a, b) => a.id.localeCompare(b.id))

export function findShowcase(id: string): ShowcaseDefinition | undefined {
  return showcases.find((s) => s.id === id)
}
