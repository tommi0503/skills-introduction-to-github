import type { WeekDay } from '../data'
import { theme } from '../theme'

function Letter({ d }: { d: WeekDay }) {
  if (d.state === 'future') return <span className="flex size-[31px] items-center justify-center text-[13px] text-[#a5a5a5]">{d.letter}</span>
  return (
    <span className="relative flex size-[31px] items-center justify-center text-[13px] font-medium">
      <svg className="absolute inset-0" viewBox="0 0 31 31">
        {d.state === 'done' ? (
          <circle cx="15.5" cy="15.5" r="14.5" fill="none" stroke="#9a9a9a" strokeWidth="1" strokeDasharray="2.6 2.4" />
        ) : (
          <path d="M 19 2 A 14 14 0 0 1 19 29" fill="none" stroke={theme.ink} strokeWidth="1.4" />
        )}
      </svg>
      {d.letter}
    </span>
  )
}

export function WeekStrip({ days }: { days: WeekDay[] }) {
  return (
    <div className="flex justify-between">
      {days.map((d, i) => (
        <div key={i} className="flex w-[31px] flex-col items-center gap-[6px]">
          <Letter d={d} />
          <span className="text-[14px]" style={{ color: d.state === 'future' ? '#a5a5a5' : '#333' }}>{d.day}</span>
        </div>
      ))}
    </div>
  )
}
