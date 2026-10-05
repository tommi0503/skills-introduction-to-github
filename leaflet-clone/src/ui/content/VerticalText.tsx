import type { ReactNode } from 'react'
import { cn } from '../core/cn'

export interface VerticalTextProps {
  /** 'stack' puts one character per line (upright Hangul); 'rotate' rotates the run 90°. */
  mode?: 'stack' | 'rotate'
  className?: string
  children: string | ReactNode
}

/** Vertical typesetting used for side titles (찾아오시는길 / ARTIST INTERVIEW). */
export function VerticalText({ mode = 'stack', className, children }: VerticalTextProps) {
  if (mode === 'rotate') {
    return (
      <span className={cn('inline-block whitespace-nowrap', className)} style={{ writingMode: 'vertical-rl' }}>
        {children}
      </span>
    )
  }
  return (
    <span className={cn('inline-block', className)} style={{ writingMode: 'vertical-rl', textOrientation: 'upright' }}>
      {children}
    </span>
  )
}
