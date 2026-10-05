import { cn } from '../../../ui'

/** A line of text, optionally emphasised. */
export interface RichLine {
  text: string
  strong?: boolean
}

export interface RichLinesProps {
  lines: readonly RichLine[]
  className?: string
  strongClassName?: string
}

/** Paragraph rendered line by line (fixed line breaks), bold lines styled via `strongClassName`. */
export function RichLines({ lines, className, strongClassName }: RichLinesProps) {
  return (
    <div className={className}>
      {lines.map((l, i) => (
        <p key={i} className={cn('m-0 whitespace-nowrap', l.strong && strongClassName)}>
          {l.text}
        </p>
      ))}
    </div>
  )
}
