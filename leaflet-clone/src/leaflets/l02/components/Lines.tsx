import type { CSSProperties } from 'react'
import { cn } from '../../../ui'

interface LinesProps {
  lines: string[]
  className?: string
  style?: CSSProperties
}

/** Paragraph rendered with the reference's explicit line breaks. */
export function Lines({ lines, className, style }: LinesProps) {
  return (
    <p className={cn('m-0', className)} style={style}>
      {lines.map((l) => (
        <span key={l} className="block whitespace-nowrap">{l}</span>
      ))}
    </p>
  )
}
