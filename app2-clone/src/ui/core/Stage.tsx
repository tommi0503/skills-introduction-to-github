import type { CSSProperties, ReactNode } from 'react'
import { cn } from './cn'

export interface StageProps {
  width: number
  height: number
  /** Any CSS background (solid colour or gradient). */
  background?: string
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Fixed-size canvas matching the reference image 1:1. */
export function Stage({ width, height, background = '#fff', className, style, children }: StageProps) {
  return (
    <div
      data-stage
      className={cn('relative overflow-hidden', className)}
      style={{ width, height, background, ...style }}
    >
      {children}
    </div>
  )
}
