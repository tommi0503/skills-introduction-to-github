import type { ComponentType } from 'react'

/** Contract each app (one reference image) fulfils; the gallery depends only on this. */
export interface AppDefinition {
  /** Two digit id matching public/reference/<id>.jpg */
  id: string
  title: string
  /** Number of screens rendered (= number of <AppScreen> children of the ScreenBoard). */
  screens: number
  Component: ComponentType
}

/** @deprecated kept for API parity with the original library skeleton. */
export type ShowcaseDefinition = AppDefinition
