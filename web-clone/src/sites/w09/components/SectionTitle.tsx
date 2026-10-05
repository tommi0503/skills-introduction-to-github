import type { CSSProperties } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface SectionTitleProps {
  text: string
  size?: number
  lineHeight?: number
  className?: string
  style?: CSSProperties
}

/** Large tight-tracked display heading (tracking = -4% of size). */
export function SectionTitle({ text, size = 66, lineHeight = 72, className, style }: SectionTitleProps) {
  return (
    <h2
      className={cn('whitespace-nowrap font-normal', className)}
      style={{ fontSize: size, lineHeight: `${lineHeight}px`, letterSpacing: `${-size * 0.04}px`, color: theme.color.ink, ...style }}
    >
      {text}
    </h2>
  )
}
