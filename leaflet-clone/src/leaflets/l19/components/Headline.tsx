import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { fonts } from '../theme'

export interface HeadlineProps {
  children: ReactNode
  size: number
  lineHeight?: number
  color: string
  className?: string
}

/** Condensed display headline (Anton). */
export function Headline({ children, size, lineHeight, color, className }: HeadlineProps) {
  return (
    <h2 className={cn(fonts.headline, 'm-0 font-normal', className)} style={{ fontSize: size, lineHeight: lineHeight ? `${lineHeight}px` : 1, color }}>
      {children}
    </h2>
  )
}
