import { cn } from '../../../ui'

export interface PillTabsProps {
  items: string[]
  active: string
  className?: string
  itemClassName?: string
}

/** Two-up segmented control: grey track with a white selected capsule. */
export function PillTabs({ items, active, className, itemClassName }: PillTabsProps) {
  return (
    <div className={cn('flex rounded-full bg-[#efefef] p-[2px]', className)}>
      {items.map((t) => (
        <div
          key={t}
          className={cn(
            'flex flex-1 items-center justify-center rounded-full',
            t === active && 'bg-white shadow-[0_1px_3px_rgba(0,0,0,0.1)]',
            itemClassName,
          )}
        >
          {t}
        </div>
      ))}
    </div>
  )
}
