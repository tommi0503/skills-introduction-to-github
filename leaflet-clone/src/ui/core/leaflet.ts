import type { ComponentType } from 'react'
import type { PanelCount } from './geometry'

/** Contract each leaflet (one reference image) fulfils; the gallery depends only on this. */
export interface LeafletDefinition {
  /** Two digit id matching public/reference/<id>.jpg */
  id: string
  title: string
  panels: PanelCount
  Component: ComponentType
}
