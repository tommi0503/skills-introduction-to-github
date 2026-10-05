import { cn } from '../../../ui'

interface LineBlockProps {
  lines: string[]
  className?: string
}

/** Paragraph rendered as explicit lines (keeps the reference line breaks). */
export function LineBlock({ lines, className }: LineBlockProps) {
  return (
    <p className={cn('m-0', className)}>
      {lines.map((l) => (
        <span key={l} className="block">{l}</span>
      ))}
    </p>
  )
}
