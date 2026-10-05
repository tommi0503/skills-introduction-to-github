import type { CSSProperties, ElementType } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface PixelTextProps {
  lines: string[]
  size: number
  lineHeight: number
  as?: ElementType
  className?: string
  style?: CSSProperties
}

/** Thin monospace display text (stand-in for the Geist Pixel Line face). */
export function PixelText({ lines, size, lineHeight, as: Tag = 'h2', className, style }: PixelTextProps) {
  return (
    <Tag className={cn('whitespace-pre', className)} style={{ ...theme.pixel, fontSize: size, lineHeight: `${lineHeight}px`, letterSpacing: '-0.1em', ...style }}>
      {lines.map((l) => (
        <span key={l} className="block">
          {l}
        </span>
      ))}
    </Tag>
  )
}
