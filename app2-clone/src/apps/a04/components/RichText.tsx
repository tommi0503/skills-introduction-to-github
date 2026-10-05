import { cn } from '../../../ui'
import type { TextRun } from '../data'
import { theme } from '../theme'

export interface RichTextProps {
  runs: TextRun[]
  className?: string
}

/** Paragraph built from plain / link / underlined runs. */
export function RichText({ runs, className }: RichTextProps) {
  return (
    <p className={cn('text-center', className)}>
      {runs.map((r, i) => (
        <span
          key={i}
          className={r.kind === 'underline' ? 'underline underline-offset-2' : undefined}
          style={r.kind === 'link' ? { color: theme.link } : undefined}
        >
          {r.text}
        </span>
      ))}
    </p>
  )
}
