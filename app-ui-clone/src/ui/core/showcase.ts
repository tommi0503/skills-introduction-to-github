import type { ComponentType } from 'react'

/**
 * Contract every showcase (one reference image) fulfils.
 * The gallery only depends on this shape (Dependency Inversion).
 */
export interface ShowcaseDefinition {
  /** Two digit id matching reference/<id>.jpg */
  id: string
  title: string
  /** Pixel size of the reference image — the Stage renders at exactly this size. */
  width: number
  height: number
  Component: ComponentType
}
