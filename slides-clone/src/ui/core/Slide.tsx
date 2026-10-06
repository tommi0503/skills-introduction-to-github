import type { CSSProperties, ReactNode } from 'react'
import { cn } from './cn'
import { SLIDE } from './geometry'

export interface SlideProps {
  background?: string
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** A single slide canvas — always SLIDE.width × SLIDE.height, content clipped. */
export function Slide({ background = '#fff', className, style, children }: SlideProps) {
  return (
    <section
      className={cn('relative shrink-0 overflow-hidden', className)}
      style={{ width: SLIDE.width, height: SLIDE.height, background, ...style }}
    >
      {children}
    </section>
  )
}
