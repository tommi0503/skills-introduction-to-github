import type { CSSProperties } from 'react'
import { cn } from '../../ui'

export interface LinesProps {
  /** Each entry is rendered on its own line — keeps the printed line breaks. */
  lines: readonly string[]
  className?: string
  lineClassName?: string
  style?: CSSProperties
}

/** Multi-line text block with explicit (print-faithful) line breaks. */
export function Lines({ lines, className, lineClassName, style }: LinesProps) {
  return (
    <div className={className} style={style}>
      {lines.map((line, i) => (
        <div key={i} className={cn('whitespace-pre', lineClassName)}>
          {line || ' '}
        </div>
      ))}
    </div>
  )
}
