import type { CSSProperties } from 'react'
import { cn } from '../../../ui'
import type { ScheduleItem } from '../data'

export interface ScheduleListProps {
  items: ScheduleItem[]
  color: string
  ruleColor: string
  rowHeight: number
  className?: string
  style?: CSSProperties
}

/** "10:00 | 프로그램" rows, each underlined by a hairline. */
export function ScheduleList({ items, color, ruleColor, rowHeight, className, style }: ScheduleListProps) {
  return (
    <ul className={cn('m-0 list-none p-0', className)} style={{ color, ...style }}>
      {items.map((item) => (
        <li
          key={item.time}
          className="flex items-center"
          style={{ height: rowHeight, borderBottom: `2px solid ${ruleColor}` }}
        >
          {item.time} | {item.label}
        </li>
      ))}
    </ul>
  )
}
