import type { CSSProperties, ReactNode } from 'react'
import { cn } from './cn'

export interface AbsProps {
  x: number
  y: number
  w?: number
  h?: number
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Absolutely positioned box in slide coordinates. */
export function Abs({ x, y, w, h, className, style, children }: AbsProps) {
  return (
    <div className={cn('absolute', className)} style={{ left: x, top: y, width: w, height: h, ...style }}>
      {children}
    </div>
  )
}
