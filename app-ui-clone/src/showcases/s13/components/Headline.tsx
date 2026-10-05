import { cn } from '../../../ui'

export interface HeadlineProps {
  lines: string[]
  className?: string
}

/** Multi-line title with explicit line breaks taken from data. */
export function Headline({ lines, className }: HeadlineProps) {
  return (
    <h1 className={cn('m-0', className)}>
      {lines.map((line) => (
        <span key={line} className="block">
          {line}
        </span>
      ))}
    </h1>
  )
}
