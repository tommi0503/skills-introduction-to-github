import type { CSSProperties, ReactNode } from 'react'
import type { Rect } from '../data'
import { cn } from '../../../ui'

/** Absolutely positioned box at a rect (relative to the nearest positioned ancestor, with optional offset). */
export function Box({
  rect,
  offset = { x: 0, y: 0 },
  className,
  style,
  children,
}: {
  rect: Rect
  offset?: { x: number; y: number }
  className?: string
  style?: CSSProperties
  children?: ReactNode
}) {
  return (
    <div
      className={cn('absolute', className)}
      style={{ left: rect.x - offset.x, top: rect.y - offset.y, width: rect.w, height: rect.h, ...style }}
    >
      {children}
    </div>
  )
}
