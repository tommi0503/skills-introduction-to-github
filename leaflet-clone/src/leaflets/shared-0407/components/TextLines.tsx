import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface TextLinesProps {
  lines: readonly ReactNode[]
  className?: string
  lineClassName?: string
  style?: CSSProperties
}

/** Renders a list of lines (explicit line breaks from the data) as stacked block elements. */
export function TextLines({ lines, className, lineClassName, style }: TextLinesProps) {
  return (
    <div className={className} style={style}>
      {lines.map((line, i) => (
        <div key={i} className={cn('whitespace-nowrap', lineClassName)}>
          {line}
        </div>
      ))}
    </div>
  )
}
