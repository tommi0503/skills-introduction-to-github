import { cn } from '../../../ui'
import type { DayItem } from '../data'
import { theme } from '../theme'

export interface DayPickerProps {
  days: DayItem[]
  active: string
  className?: string
}

/** Row of weekday tiles; the active day is a filled green tile. */
export function DayPicker({ days, active, className }: DayPickerProps) {
  return (
    <div className={cn('flex justify-between', className)}>
      {days.map((d) => {
        const on = d.day === active
        return (
          <div
            key={d.key}
            className={cn('flex h-[60px] w-[52px] flex-col items-center justify-center rounded-[13px]', on ? 'text-white' : '')}
            style={{ background: on ? `linear-gradient(180deg, #6fe39c, ${theme.green})` : '#fdfdfd' }}
          >
            <span className={cn('text-[10px]', !on && 'text-[#777]')}>{d.weekday}</span>
            <span className={cn('mt-[7px] text-[14.5px]', !on && 'text-[#222]')}>{d.day}</span>
          </div>
        )
      })}
    </div>
  )
}
