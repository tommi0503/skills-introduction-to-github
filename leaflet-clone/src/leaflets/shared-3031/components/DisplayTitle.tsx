import { cn } from '../../../ui'
import { fonts } from '../theme'

export interface DisplayTitleProps {
  lines: readonly string[]
  color: string
  className?: string
  /** Per-line colours override `color` (e.g. sky / white title). */
  lineColors?: readonly string[]
}

/** Centered multi-line rounded display title. */
export function DisplayTitle({ lines, color, className, lineColors }: DisplayTitleProps) {
  return (
    <h1 className={cn('m-0 text-center font-normal', fonts.display, className)}>
      {lines.map((l, i) => (
        <span key={i} className="block whitespace-pre" style={{ color: lineColors?.[i] ?? color }}>
          {l}
        </span>
      ))}
    </h1>
  )
}
