import type { ReactNode } from 'react'
import type { CalendarDay } from '../data'
import { DayCell } from './DayCell'
import { Triangle } from './Triangle'

export interface CalendarCardProps {
  month: string
  weekdays: string[]
  highlightedWeekday: string
  days: CalendarDay[]
  /** Extra content rendered under the grid (time slot picker, actions...). */
  footer?: ReactNode
}

/** Frosted month calendar: navigation header, weekday row and 7-column day grid. */
export function CalendarCard({ month, weekdays, highlightedWeekday, days, footer }: CalendarCardProps) {
  return (
    <div className="rounded-[18px] border border-white/60 bg-white/25 px-[6px] pb-[9px] pt-[3px]">
      <div className="flex h-[32px] items-center justify-between px-[1px]">
        <span className="flex h-[29px] w-[29px] items-center justify-center rounded-full bg-[#dcdbd7] text-[#6f6e6b]">
          <Triangle dir="left" className="mr-[2px]" />
        </span>
        <span className="text-[13px] font-semibold">{month}</span>
        <span className="flex h-[29px] w-[29px] items-center justify-center rounded-full bg-white text-black">
          <Triangle dir="right" className="ml-[2px]" />
        </span>
      </div>
      <div className="mt-[5px] grid grid-cols-7 gap-x-[3px] text-center text-[10.5px] leading-[14px]">
        {weekdays.map((w) => (
          <span key={w} className={w === highlightedWeekday ? 'font-semibold text-black' : 'text-[#8d8c88]'}>
            {w}
          </span>
        ))}
      </div>
      <div className="mt-[5px] grid grid-cols-7 gap-[3.5px]">
        {days.map((d) => (
          <DayCell key={d.day} {...d} />
        ))}
      </div>
      {footer}
    </div>
  )
}
