import type { CSSProperties } from 'react'
import { cn } from '../../../ui'

export interface LinesProps {
  lines: string[]
  className?: string
  style?: CSSProperties
  /** Keep the wrapped-line trailing space (as in right-aligned, naturally wrapped text). */
  hangingSpace?: boolean
}

/** Renders pre-broken copy lines as stacked blocks (keeps the reference's exact line breaks). */
export function Lines({ lines, className, style, hangingSpace }: LinesProps) {
  return (
    <p className={cn('whitespace-pre', className)} style={style}>
      {lines.map((l, i) => (
        <span key={l} className="block">
          {hangingSpace && i < lines.length - 1 ? `${l} ` : l}
        </span>
      ))}
    </p>
  )
}
