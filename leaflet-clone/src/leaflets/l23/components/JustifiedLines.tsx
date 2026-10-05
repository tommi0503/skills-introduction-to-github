import { cn } from '../../../ui'

export interface JustifiedLinesProps {
  lines: string[]
  className?: string
}

/** Body copy set line by line, each line justified edge to edge except the last (as printed). */
export function JustifiedLines({ lines, className }: JustifiedLinesProps) {
  return (
    <div className={cn('flex flex-col', className)}>
      {lines.map((l, i) => (
        <span key={l} style={i < lines.length - 1 ? { textAlign: 'justify', textAlignLast: 'justify' } : undefined}>
          {l}
        </span>
      ))}
    </div>
  )
}
