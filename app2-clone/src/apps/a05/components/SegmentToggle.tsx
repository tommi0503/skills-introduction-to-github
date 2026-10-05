import { Check, type LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface Segment {
  key: string
  label: string
  icon?: LucideIcon
}

/** Two-state pill switch ("want to try" | "visited"); the active side is a black capsule. */
export function SegmentToggle({ items, activeKey, className }: { items: Segment[]; activeKey: string; className?: string }) {
  return (
    <div className={cn('flex rounded-full border border-[#dedee2] bg-[#f4f5f7]', className)}>
      {items.map((s) => {
        const active = s.key === activeKey
        const Icon = active ? Check : s.icon
        return (
          <div
            key={s.key}
            className={cn(
              'a05-wide flex items-center justify-center gap-[6px] rounded-full text-[16px] font-bold tracking-[-0.6px]',
              active ? 'bg-black text-white' : 'text-[#8f9095]',
            )}
            style={{ fontStretch: '110%', flex: active ? 1.17 : 1 }}
          >
            {Icon && <Icon size={active ? 15 : 13} strokeWidth={active ? 2 : 1.5} fill={active ? 'none' : '#8f9095'} />}
            {s.label}
          </div>
        )
      })}
    </div>
  )
}
