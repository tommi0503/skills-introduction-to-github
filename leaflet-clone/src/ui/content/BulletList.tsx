import type { ReactNode } from 'react'
import { cn } from '../core/cn'

export interface BulletListProps {
  items: ReactNode[]
  /** Marker node, or a function of the index (e.g. numbers, check icons). */
  marker?: ReactNode | ((index: number) => ReactNode)
  className?: string
  itemClassName?: string
  markerClassName?: string
}

export function BulletList({ items, marker = '•', className, itemClassName, markerClassName }: BulletListProps) {
  return (
    <ul className={cn('m-0 flex list-none flex-col p-0', className)}>
      {items.map((item, i) => (
        <li key={i} className={cn('flex items-start', itemClassName)}>
          <span className={cn('shrink-0', markerClassName)}>{typeof marker === 'function' ? marker(i) : marker}</span>
          <span className="min-w-0 flex-1">{item}</span>
        </li>
      ))}
    </ul>
  )
}
