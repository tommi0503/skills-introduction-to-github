import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import type { Rect } from '../data'

/** Absolutely positioned box at a frame rect. */
export function Box({ rect, className, style, children }: { rect: Rect; className?: string; style?: CSSProperties; children?: ReactNode }) {
  return (
    <div className={cn('absolute', className)} style={{ left: rect.x, top: rect.y, width: rect.w, height: rect.h, ...style }}>
      {children}
    </div>
  )
}
