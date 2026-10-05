import { cn } from '../../../ui'

export interface DottedTextProps {
  text: string
  /** Character indices that get an emphasis dot (방점) above them. */
  dotted: readonly number[]
  dotSize?: number
  /** Distance of the dot above the glyph box, px. */
  dotOffset?: number
  className?: string
}

/** Text with Korean-style emphasis dots above selected characters. */
export function DottedText({ text, dotted, dotSize = 4, dotOffset = 2, className }: DottedTextProps) {
  return (
    <span className={cn('inline-flex whitespace-pre', className)}>
      {[...text].map((ch, i) => (
        <span key={i} className="relative">
          {dotted.includes(i) && (
            <span
              className="absolute left-1/2 -translate-x-1/2 rounded-full bg-current"
              style={{ width: dotSize, height: dotSize, top: -dotOffset - dotSize }}
            />
          )}
          {ch}
        </span>
      ))}
    </span>
  )
}
