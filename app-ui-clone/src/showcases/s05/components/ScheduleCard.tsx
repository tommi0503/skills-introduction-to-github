import { CalendarFold, Plus } from 'lucide-react'
import type { DayItem, ScheduleEvent } from '../data'
import { cardShadow, theme } from '../theme'
import { DayPicker } from './DayPicker'
import { EventRow } from './EventRow'

export interface ScheduleCardProps {
  date: string
  count: string
  days: DayItem[]
  activeDay: string
  events: ScheduleEvent[]
}

const actions = [Plus, CalendarFold]

export function ScheduleCard({ date, count, days, activeDay, events }: ScheduleCardProps) {
  return (
    <div className="h-[600px] w-[369px] rounded-[22px] px-[14px] pt-[20px]" style={{ background: theme.card, boxShadow: cardShadow }}>
      <div className="flex items-start justify-between pl-[5px]">
        <div>
          <p className="text-[15.5px] tracking-[-0.4px] text-[#151515]">{date}</p>
          <span className="mt-[6px] inline-block rounded-full bg-white px-[8px] py-[3px] text-[10.5px] tracking-[-0.2px]" style={{ color: theme.greenDeep }}>
            {count}
          </span>
        </div>
        <div className="mt-[16px] flex gap-[10px] pr-[6px]">
          {actions.map((Icon, i) => (
            <span key={i} className="flex h-[40px] w-[40px] items-center justify-center rounded-full bg-white">
              <Icon size={i === 0 ? 20 : 16} strokeWidth={1.5} color="#222" />
            </span>
          ))}
        </div>
      </div>

      <DayPicker days={days} active={activeDay} className="mt-[18px] px-[2px]" />

      <div className="relative mt-[18px]">
        <span className="absolute top-[22px] left-[23px] h-[300px] w-[2px] rounded-full bg-[#ececec]" />
        {events.map((e) => (
          <EventRow key={e.key} event={e} />
        ))}
      </div>
    </div>
  )
}
