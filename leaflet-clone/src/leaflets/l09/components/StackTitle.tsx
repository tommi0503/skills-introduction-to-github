import { VerticalText, cn } from '../../../ui'

export interface StackTitleProps {
  text: string
  /** Extra space (px) inserted where the heading has a word break. */
  wordGap?: number
  className?: string
}

/** Upright vertical serif heading (one glyph per line); word spaces become small gaps. */
export function StackTitle({ text, wordGap = 8, className }: StackTitleProps) {
  return (
    <div className="flex flex-col items-center" style={{ gap: wordGap }}>
      {text.split(' ').map((word) => (
        <VerticalText key={word} className={cn('text-[31px] leading-none tracking-[7px] text-[#2b2b2b]', className)}>
          {word}
        </VerticalText>
      ))}
    </div>
  )
}
