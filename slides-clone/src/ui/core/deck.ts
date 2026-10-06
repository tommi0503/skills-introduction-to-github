import type { ComponentType } from 'react'
/** One reference image = one deck (one or more slides). */
export interface DeckDefinition {
  id: string
  title: string
  slides: ComponentType[]
}
