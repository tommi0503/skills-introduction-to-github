import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { ClubMark } from './Tag'

export interface FilterChipData {
  key: string
  label: string
  icon?: LucideIcon
  club?: boolean
  active?: boolean
}

/** Outlined sort/filter capsules; the active one is solid black. */
export function FilterChips({ items, className }: { items: FilterChipData[]; className?: string }) {
  return (
    <div className={cn('flex gap-[8px] whitespace-nowrap', className)}>
      {items.map((c) => (
        <span
          key={c.key}
          className={cn(
            'inline-flex h-[34px] shrink-0 items-center gap-[5px] rounded-full px-[15px] text-[13.5px] tracking-[-0.3px]',
            c.active ? 'bg-[#1c1c1f] font-semibold text-white' : 'border border-[#e2e4e7] bg-white text-[#222]',
          )}
        >
          {c.icon && <c.icon size={15} strokeWidth={2} fill={c.key === 'instant' ? '#111' : 'none'} />}
          {c.club && <ClubMark size={15} color="#5ed6f0" />}
          {c.label}
        </span>
      ))}
    </div>
  )
}
