import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../core/cn'
import { PANEL } from '../core/geometry'

export interface PanelProps {
  background?: string
  /** Inner padding in px (number) or any CSS padding string. */
  padding?: number | string
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** One fold of the leaflet — always exactly PANEL.width × PANEL.height. */
export function Panel({ background, padding, className, style, children }: PanelProps) {
  return (
    <section
      className={cn('relative shrink-0 overflow-hidden', className)}
      style={{ width: PANEL.width, height: PANEL.height, background, padding, ...style }}
    >
      {children}
    </section>
  )
}
