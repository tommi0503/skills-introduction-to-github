import { cn } from '../../../ui'
import type { CalendarDay } from '../data'
import { theme } from '../theme'

const hatch = `repeating-linear-gradient(135deg, ${theme.cellHatchA} 0 2.4px, ${theme.cellHatchB} 2.4px 4.8px)`

/** One calendar day; its look is driven purely by `state`. */
export function DayCell({ day, state }: CalendarDay) {
  return (
    <div
      className={cn(
        'relative flex h-[43px] items-center justify-center rounded-[9px] text-[14px] font-bold',
        state === 'open' && 'bg-white text-black',
        state === 'selected' && 'bg-black text-white',
        state !== 'open' && state !== 'selected' && 'text-[#2b2b2b]',
      )}
      style={
        state === 'blocked' ? { background: theme.cellBlocked } : state === 'hatched' ? { background: hatch } : undefined
      }
    >
      {state === 'selected' && <span className="absolute left-[5px] top-[4px] h-[4px] w-[4px] rounded-full bg-white" />}
      {day}
    </div>
  )
}
