import type { CSSProperties, ReactNode } from 'react'
import { cn } from './cn'
import { FRAME } from './geometry'

export interface PageFrameProps {
  background?: string
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Fixed FRAME-size viewport for one site; content below FRAME.height is clipped. */
export function PageFrame({ background = '#fff', className, style, children }: PageFrameProps) {
  return (
    <div
      data-stage
      className={cn('relative overflow-hidden', className)}
      style={{ width: FRAME.width, height: FRAME.height, background, ...style }}
    >
      {children}
    </div>
  )
}
