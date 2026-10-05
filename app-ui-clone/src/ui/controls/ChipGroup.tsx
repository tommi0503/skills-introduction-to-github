import type { ReactNode } from 'react'
import { cn } from '../core/cn'

export interface ChipItem {
  key: string
  label: ReactNode
}

export interface ChipGroupProps {
  items: ChipItem[]
  activeKey?: string
  /** Classes shared by every chip. */
  chipClassName?: string
  activeClassName?: string
  inactiveClassName?: string
  className?: string
  gap?: number
  onSelect?: (key: string) => void
}

/** Horizontal filter-chip row. Styling is injected so it fits any app. */
export function ChipGroup({
  items,
  activeKey,
  chipClassName,
  activeClassName,
  inactiveClassName,
  className,
  gap = 8,
  onSelect,
}: ChipGroupProps) {
  return (
    <div className={cn('flex items-center whitespace-nowrap', className)} style={{ gap }}>
      {items.map((item) => {
        const active = item.key === activeKey
        return (
          <button
            key={item.key}
            type="button"
            onClick={() => onSelect?.(item.key)}
            className={cn('inline-flex shrink-0 items-center justify-center', chipClassName, active ? activeClassName : inactiveClassName)}
          >
            {item.label}
          </button>
        )
      })}
    </div>
  )
}
