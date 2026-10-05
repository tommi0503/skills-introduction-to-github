import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface Reaction {
  key: string
  label: string
  icon: LucideIcon
}

/** Four rating tiles; the chosen one is lifted (white, dark label). */
export function ReactionTiles({ items, activeKey, className }: { items: Reaction[]; activeKey: string; className?: string }) {
  return (
    <div className={cn('flex gap-[10px]', className)}>
      {items.map((r) => {
        const active = r.key === activeKey
        return (
          <div
            key={r.key}
            className={cn(
              'flex h-[63px] flex-1 flex-col items-center justify-center gap-[6px] rounded-[14px]',
              active ? 'bg-white text-[#111]' : 'bg-[#f2f3f5] text-[#7c7d82]',
            )}
            style={{ boxShadow: active ? '0 2px 8px rgba(0,0,0,.10)' : '0 2px 5px rgba(0,0,0,.08), inset 0 -1px 0 rgba(0,0,0,.04)' }}
          >
            <r.icon size={active ? 20 : 15} strokeWidth={active ? 1.6 : 1.3} />
            <span className={cn('text-[14px] leading-none', active && 'font-semibold')}>{r.label}</span>
          </div>
        )
      })}
    </div>
  )
}
