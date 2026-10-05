import { cn } from '../../../ui'

export interface UnderlineTabsProps {
  items: string[]
  active: number
  /** Equal-width cells (package selector) vs. content-width (profile tabs). */
  equal?: boolean
  className?: string
  itemClassName?: string
  barClassName?: string
}

export function UnderlineTabs({ items, active, equal, className, itemClassName, barClassName }: UnderlineTabsProps) {
  return (
    <div className={cn('flex', className)}>
      {items.map((t, i) => (
        <div
          key={t}
          className={cn('relative flex items-center justify-center whitespace-nowrap', equal && 'flex-1', itemClassName)}
          style={{ color: i === active ? '#222325' : '#95979d', fontWeight: i === active ? 600 : 500 }}
        >
          {t}
          {i === active && <span className={cn('absolute inset-x-0 bottom-0 h-[3px] bg-[#111]', barClassName)} />}
        </div>
      ))}
    </div>
  )
}
