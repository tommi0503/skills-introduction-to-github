import { SlidersHorizontal } from 'lucide-react'
import { cn } from '../../../ui'
import type { FilterChip } from '../data'

export function FilterChips({ items, className }: { items: FilterChip[]; className?: string }) {
  return (
    <div className={cn('flex gap-[11px] whitespace-nowrap', className)}>
      {items.map((c) => (
        <span
          key={c.label}
          className={cn(
            'flex h-[34px] items-center gap-[10px] rounded-full bg-white px-[14px] text-[15px] font-medium text-[#222325]',
            c.selected ? 'border-2 border-[#111]' : 'border border-[#dadbdd]',
          )}
        >
          {c.withIcon && <SlidersHorizontal size={15} strokeWidth={2} />}
          {c.label}
        </span>
      ))}
    </div>
  )
}
