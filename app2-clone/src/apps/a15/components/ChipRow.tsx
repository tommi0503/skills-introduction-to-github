import { CalendarDays, CircleUserRound } from 'lucide-react'
import { cn } from '../../../ui'
import type { Chip } from '../data'
import { lyft } from '../theme'

const icons = { calendar: CalendarDays, rider: CircleUserRound }

/** "Schedule ahead" / "Change rider" capsules. */
export function ChipRow({ items, className, height }: { items: Chip[]; className?: string; height: number }) {
  return (
    <div className={cn('absolute flex gap-[10px]', className)}>
      {items.map((c) => {
        const Icon = icons[c.icon]
        return (
          <div
            key={c.key}
            className="flex items-center gap-[5px] rounded-full pr-[16px] pl-[16px] text-[14px] font-medium"
            style={{ background: lyft.chip, height }}
          >
            <Icon size={15} strokeWidth={2.2} fill={c.icon === 'calendar' ? 'currentColor' : 'none'} />
            {c.label}
          </div>
        )
      })}
    </div>
  )
}
