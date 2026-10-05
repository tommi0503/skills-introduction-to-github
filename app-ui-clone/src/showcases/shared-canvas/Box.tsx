import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../ui'

export interface Rect {
  x: number
  y: number
  w: number
  h: number
}

/** Absolutely positioned box in logical (pt) screen coordinates. */
export function Box({ rect, className, style, children }: { rect: Rect; className?: string; style?: CSSProperties; children?: ReactNode }) {
  return (
    <div className={cn('absolute', className)} style={{ left: rect.x, top: rect.y, width: rect.w, height: rect.h, ...style }}>
      {children}
    </div>
  )
}
