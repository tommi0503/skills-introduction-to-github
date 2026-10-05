import type { CSSProperties, ElementType } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface Segment {
  t: string
  em?: boolean
}

export interface SerifTitleProps {
  lines: Segment[][]
  as?: ElementType
  size: number
  lineHeight: number
  letterSpacing?: number
  className?: string
  style?: CSSProperties
}

/** Light serif display heading; `em` segments render in italic (Lyon Display stand-in). */
export function SerifTitle({ lines, as: Tag = 'h2', size, lineHeight, letterSpacing = 0, className, style }: SerifTitleProps) {
  return (
    <Tag
      className={cn(theme.fonts.serif, 'm-0 text-center font-normal', className)}
      style={{ fontSize: size, lineHeight: `${lineHeight}px`, letterSpacing: letterSpacing + size * theme.serifTracking, ...style }}
    >
      {lines.map((line, i) => (
        <span key={i} className="block whitespace-nowrap">
          {line.map((s, j) => (s.em ? <em key={j}>{s.t}</em> : <span key={j}>{s.t}</span>))}
        </span>
      ))}
    </Tag>
  )
}
