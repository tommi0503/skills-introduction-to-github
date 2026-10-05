import { cn } from '../../../ui'

export interface JustifiedLinesProps {
  lines: string[]
  className?: string
}

/** Paragraph with fixed (printed) line breaks; every line but the last is justified edge to edge. */
export function JustifiedLines({ lines, className }: JustifiedLinesProps) {
  return (
    <div className={className}>
      {lines.map((line, i) => (
        <p
          key={line}
          className={cn('m-0 whitespace-nowrap', i < lines.length - 1 && 'text-justify [text-align-last:justify]')}
        >
          {line}
        </p>
      ))}
    </div>
  )
}
