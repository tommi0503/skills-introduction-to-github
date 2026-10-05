import { cn } from '../core/cn'
import type { ChipItem } from './ChipGroup'

export interface SegmentedControlProps {
  items: ChipItem[]
  activeKey: string
  className?: string
  segmentClassName?: string
  activeClassName?: string
  inactiveClassName?: string
}

/** Equal-width segmented tabs inside a track. */
export function SegmentedControl({
  items,
  activeKey,
  className,
  segmentClassName,
  activeClassName,
  inactiveClassName,
}: SegmentedControlProps) {
  return (
    <div className={cn('flex items-center', className)}>
      {items.map((item) => (
        <div
          key={item.key}
          className={cn(
            'flex flex-1 items-center justify-center',
            segmentClassName,
            item.key === activeKey ? activeClassName : inactiveClassName,
          )}
        >
          {item.label}
        </div>
      ))}
    </div>
  )
}
