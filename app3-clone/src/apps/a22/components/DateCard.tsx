import { cn } from '../../../ui'
import type { DayCard } from '../data'
import { theme } from '../theme'

export function DateCard({ day, active }: { day: DayCard; active: boolean }) {
  return (
    <div
      className={cn(
        'flex h-[68px] w-[67px] shrink-0 flex-col items-center justify-center gap-[8px] rounded-[6px] border text-[12px] leading-none',
        active ? 'border-black bg-black text-white' : 'bg-white text-black',
      )}
      style={active ? undefined : { borderColor: theme.border }}
    >
      <span>{day.weekday}</span>
      <span>{day.day}</span>
    </div>
  )
}
