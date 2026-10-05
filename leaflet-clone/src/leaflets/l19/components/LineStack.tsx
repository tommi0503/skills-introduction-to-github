import { cn } from '../../../ui'

export interface LineStackProps {
  lines: string[]
  /** Justify every line but the last edge to edge. */
  justify?: boolean
  className?: string
  lineClassName?: string
}

/** Text block with fixed printed line breaks. */
export function LineStack({ lines, justify, className, lineClassName }: LineStackProps) {
  return (
    <div className={className}>
      {lines.map((line, i) => (
        <p
          key={line}
          className={cn(
            'm-0 whitespace-nowrap',
            justify && i < lines.length - 1 && 'text-justify [text-align-last:justify]',
            lineClassName,
          )}
        >
          {line}
        </p>
      ))}
    </div>
  )
}
