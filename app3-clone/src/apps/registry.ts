import type { AppDefinition } from '../ui'

/** Auto-discovers src/apps/aNN/index.tsx — adding an app needs no edit here. */
const modules = import.meta.glob<{ default: AppDefinition }>('./a*/index.tsx', { eager: true })

export const apps: AppDefinition[] = Object.values(modules)
  .map((m) => m.default)
  .sort((a, b) => a.id.localeCompare(b.id))

export const findApp = (id: string) => apps.find((a) => a.id === id)
