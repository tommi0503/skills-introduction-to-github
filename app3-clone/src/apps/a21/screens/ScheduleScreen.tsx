import { CalendarDays, Menu } from 'lucide-react'
import { ColorPlus } from '../components/ColorPlus'
import { GScreen } from '../components/GScreen'
import { MonthBanner, RangeRow, TodayRow } from '../components/ScheduleRows'
import { schedule, type ScheduleItem } from '../data'
import { theme } from '../theme'

function Row({ item }: { item: ScheduleItem }) {
  if (item.kind === 'today') return <TodayRow item={item} />
  if (item.kind === 'month') return <MonthBanner label={item.label} tone={item.tone} />
  return <RangeRow label={item.label} />
}

export function ScheduleScreen() {
  return (
    <GScreen>
      <header
        className="absolute inset-x-0 top-0 z-30 h-[105px] bg-white"
        style={{ boxShadow: '0 2px 4px rgba(0,0,0,.18)' }}
      >
        <Menu className="absolute left-[21px] top-[65px]" size={22} strokeWidth={1.8} color="#5f6368" />
        <div className="absolute left-[67px] top-[61px] flex items-center font-dm text-[20px]" style={{ color: theme.text }}>
          {schedule.month}
          <span className="ml-[8px] mt-[2px] border-x-[5px] border-t-[5px] border-x-transparent border-t-[#5f6368]" />
        </div>
        <CalendarDays className="absolute right-[18px] top-[63px]" size={22} strokeWidth={1.8} color="#5f6368" />
      </header>
      <div className="absolute inset-x-0 top-[105px]">
        {schedule.items.map((it, i) => (
          <Row key={i} item={it} />
        ))}
      </div>
      <div
        className="absolute left-[316px] top-[772px] z-40 flex size-[57px] items-center justify-center rounded-full bg-white"
        style={{ boxShadow: '0 3px 8px rgba(0,0,0,.25)' }}
      >
        <ColorPlus />
      </div>
    </GScreen>
  )
}
