import type { ComponentType } from 'react'
/** Contract each cloned site fulfils; the gallery depends only on this. */
export interface SiteDefinition {
  id: string
  title: string
  url: string
  Component: ComponentType
}
