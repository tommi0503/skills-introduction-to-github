import { cn } from '../../../ui'
import type { LabeledValue } from '../data'

export interface LabeledLineProps {
  items: LabeledValue[]
  /** Separator between label and value (e.g. " | "). */
  separator?: string
  gap?: number
  className?: string
  labelClassName?: string
  valueClassName?: string
}

/** One line of "라벨 | 값" pairs (일시 | …, 장소 | … 문의 | …). */
export function LabeledLine({ items, separator = ' | ', gap = 12, className, labelClassName, valueClassName }: LabeledLineProps) {
  return (
    <p className={cn('m-0 flex whitespace-pre', className)} style={{ gap }}>
      {items.map((item) => (
        <span key={item.label}>
          <span className={labelClassName}>{item.label}</span>
          <span className={valueClassName}>
            {separator}
            {item.value}
          </span>
        </span>
      ))}
    </p>
  )
}
