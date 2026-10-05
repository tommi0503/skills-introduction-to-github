import { cn } from '../../../ui'

export interface CategoryTabsProps {
  items: string[]
  active: string
  className?: string
}

/** Text-only category switcher (active = bold, others dimmed). */
export function CategoryTabs({ items, active, className }: CategoryTabsProps) {
  return (
    <div className={cn('flex items-center justify-between text-[14.5px] tracking-[-0.1px]', className)}>
      {items.map((c) => (
        <span key={c} className={c === active ? 'font-semibold text-white' : 'text-white/70'}>
          {c}
        </span>
      ))}
    </div>
  )
}
