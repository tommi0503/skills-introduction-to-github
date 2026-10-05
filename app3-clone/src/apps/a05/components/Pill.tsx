import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface PillProps {
  children: ReactNode
  leading?: ReactNode
  className?: string
  style?: CSSProperties
}

/** Rounded capsule used for chips, filters, segmented options and small CTAs. */
export function Pill({ children, leading, className, style }: PillProps) {
  return (
    <span
      className={cn('inline-flex shrink-0 items-center justify-center rounded-full whitespace-nowrap', className)}
      style={style}
    >
      {leading}
      {children}
    </span>
  )
}
