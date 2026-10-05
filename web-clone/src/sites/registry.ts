import type { SiteDefinition } from '../ui'

/** Auto-discovers src/sites/wNN/index.tsx. */
const modules = import.meta.glob<{ default: SiteDefinition }>('./w*/index.tsx', { eager: true })
export const sites: SiteDefinition[] = Object.values(modules).map((m) => m.default).sort((a, b) => a.id.localeCompare(b.id))
export const findSite = (id: string) => sites.find((s) => s.id === id)
