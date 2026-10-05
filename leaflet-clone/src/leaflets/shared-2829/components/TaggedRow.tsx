import type { CSSProperties, ReactNode } from 'react'
import { Pill, cn } from '../../../ui'

export interface TaggedRowProps {
  tag: string
  lines: readonly ReactNode[]
  /** Tag fill colour. */
  color: string
  className?: string
  pillClassName?: string
  textClassName?: string
  style?: CSSProperties
}

/** A rounded label tag followed by one or more lines of text (일시 / 장소 / 셔틀버스 …). */
export function TaggedRow({ tag, lines, color, className, pillClassName, textClassName, style }: TaggedRowProps) {
  return (
    <div className={cn('flex', className)} style={style}>
      <span className={cn('inline-flex h-[38px] w-[77px] shrink-0 rounded-[12px]', pillClassName)} style={{ background: color }}>
        <Pill className="h-full w-full rounded-none text-[14.5px] font-medium text-white">{tag}</Pill>
      </span>
      <div className={textClassName}>
        {lines.map((l, i) => (
          <p key={i} className="m-0">
            {l}
          </p>
        ))}
      </div>
    </div>
  )
}
