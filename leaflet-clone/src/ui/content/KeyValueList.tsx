import type { ReactNode } from 'react'
import { cn } from '../core/cn'

export interface KeyValueItem {
  key: string
  label: ReactNode
  value: ReactNode
}

export interface KeyValueListProps {
  items: KeyValueItem[]
  /** Label column width (px or CSS). */
  labelWidth?: number | string
  className?: string
  rowClassName?: string
  labelClassName?: string
  valueClassName?: string
  /** Custom label renderer (e.g. render label as a pill). */
  renderLabel?: (item: KeyValueItem) => ReactNode
}

/** "label  value" rows (주소 / 웹사이트 / 전화 …). */
export function KeyValueList({
  items,
  labelWidth,
  className,
  rowClassName,
  labelClassName,
  valueClassName,
  renderLabel,
}: KeyValueListProps) {
  return (
    <dl className={cn('flex flex-col', className)}>
      {items.map((item) => (
        <div key={item.key} className={cn('flex items-start', rowClassName)}>
          <dt className={cn('shrink-0', labelClassName)} style={{ width: labelWidth }}>
            {renderLabel ? renderLabel(item) : item.label}
          </dt>
          <dd className={cn('m-0 min-w-0 flex-1', valueClassName)}>{item.value}</dd>
        </div>
      ))}
    </dl>
  )
}
