import { ArrowLeft, Plus } from 'lucide-react'
import { AppHeader, SquareAction } from '../components/AppHeader'
import { BarberPhone } from '../components/BarberPhone'
import { CalendarCard } from '../components/CalendarCard'
import { Headline } from '../components/Headline'
import { RangeTabs } from '../components/RangeTabs'
import { ScheduleCard } from '../components/ScheduleCard'
import { TimeSlotPicker } from '../components/TimeSlotPicker'
import {
  activeRange,
  copy,
  highlightedWeekday,
  rangeTabs,
  schedule,
  scheduleTimes,
  septemberDays,
  timeSlot,
  weekdays,
} from '../data'
import { theme } from '../theme'

/** Stagger of the schedule tiles along the timeline. */
const scheduleSlots = [
  { left: 50, top: 708 },
  { left: 199, top: 728 },
]

/** Booking: range tabs, month calendar, time slot and today's schedule. */
export function BookingScreen() {
  return (
    <BarberPhone background={theme.screenBooking}>
      <AppHeader
        left={
          <SquareAction>
            <ArrowLeft size={15} strokeWidth={1.8} />
          </SquareAction>
        }
      />
      <Headline lines={copy.bookingTitle} className="absolute left-[22px] top-[113px] text-[28.5px] font-medium leading-[36px] tracking-[-0.2px]" />
      <div className="absolute left-[22px] top-[195px] w-[335px]">
        <RangeTabs options={rangeTabs} active={activeRange} />
      </div>
      <div className="absolute left-[23px] top-[243px] w-[333px]">
        <CalendarCard
          month={copy.month}
          weekdays={weekdays}
          highlightedWeekday={highlightedWeekday}
          days={septemberDays}
          footer={<TimeSlotPicker slot={timeSlot} saveLabel={copy.save} />}
        />
      </div>

      <div className="absolute left-[22px] top-[677px] text-[16px] font-semibold">{copy.scheduleTitle}</div>
      {scheduleTimes.map((t, i) => (
        <div key={t.time} className="absolute left-[21px] text-[9.5px] leading-[12px] text-[#55544f]" style={{ top: 707 + i * 60 }}>
          {t.time}
          <div className="text-[#9a9994]">{t.meridiem}</div>
        </div>
      ))}
      <div className="absolute left-[52px] right-0 top-[718px] border-t border-dashed border-[#c9c8c3]" />
      {scheduleSlots.map((slot, i) => (
        <div key={schedule[i].name} className="absolute" style={{ left: slot.left, top: slot.top }}>
          <ScheduleCard entry={schedule[i]} className="h-[120px]" />
        </div>
      ))}

      <span className="absolute left-[311px] top-[694px] flex h-[49px] w-[49px] items-center justify-center rounded-full bg-black text-white shadow-[0_4px_12px_rgba(0,0,0,0.3)]">
        <Plus size={20} strokeWidth={1.8} />
      </span>
    </BarberPhone>
  )
}
