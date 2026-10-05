import type { MonthSpec } from '../data'
import { DayCell } from './DayCell'

interface MonthCalendarProps {
  month: MonthSpec
  weekdays: string[]
  /** Rows at or beyond this index render faded (content scrolling under the CTA). */
  fadeFromRow?: number
}

/** Month card: title, weekday header and a 7-column grid of day circles. */
export function MonthCalendar({ month, weekdays, fadeFromRow }: MonthCalendarProps) {
  const cells: Array<number | null> = [
    ...Array.from({ length: month.offset }, () => null),
    ...Array.from({ length: month.days }, (_, i) => i + 1),
  ]
  return (
    <div className="rounded-[18px] border border-[#efefef] bg-white px-[11.5px] pt-[15px] pb-[16px]">
      <div className="pl-[4.5px] text-[15.5px] font-semibold tracking-[-0.2px]">{month.title}</div>
      <div className="mt-[14px] grid grid-cols-7 justify-items-center gap-y-[7px] text-[13px] text-[#9a9a9a]">
        {weekdays.map((w) => (
          <span key={w} className="mb-[1px] leading-[16px]">
            {w}
          </span>
        ))}
        {cells.map((d, i) =>
          d === null ? (
            <span key={`e${i}`} />
          ) : (
            <DayCell
              key={d}
              day={d}
              state={month.states[d] ?? (fadeFromRow !== undefined && Math.floor(i / 7) >= fadeFromRow ? 'faded' : 'default')}
            />
          ),
        )}
      </div>
    </div>
  )
}
