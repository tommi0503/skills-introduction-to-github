import type { CSSProperties } from 'react'
import { cn } from '../../../ui'

interface LineBlockProps {
  lines: string[]
  className?: string
  style?: CSSProperties
}

/** Paragraph rendered as explicit lines (keeps the reference line breaks). */
export function LineBlock({ lines, className, style }: LineBlockProps) {
  return (
    <p className={cn('m-0', className)} style={style}>
      {lines.map((l) => (
        <span key={l} className="block">{l}</span>
      ))}
    </p>
  )
}
