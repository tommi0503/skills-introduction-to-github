import type { CSSProperties } from 'react'
import { cn } from '../../../ui'
import { seoul } from '../theme'

interface TextCardProps {
  lines: string[]
  /** Draw the soft grey card behind the text. */
  card?: boolean
  className?: string
  style?: CSSProperties
}

/** Paragraph (pre-broken into printed lines) on a soft grey card. */
export function TextCard({ lines, card = true, className, style }: TextCardProps) {
  return (
    <div
      className={cn('absolute box-border px-[16px] font-nanum-gothic text-[14.5px] font-bold leading-[27.5px]', className)}
      style={{ background: card ? seoul.card : undefined, color: seoul.body, ...style }}
    >
      {lines.map((l) => (
        <p key={l} className="m-0 whitespace-nowrap">
          {l}
        </p>
      ))}
    </div>
  )
}
