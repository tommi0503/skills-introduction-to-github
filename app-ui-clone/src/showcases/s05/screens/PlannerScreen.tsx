import { Bell } from 'lucide-react'
import { FloatingNav } from '../components/FloatingNav'
import { ScheduleCard } from '../components/ScheduleCard'
import { ScreenHeader } from '../components/ScreenHeader'
import { StatCard } from '../components/StatCard'
import { days, events, navEntries, planner, statCards } from '../data'

export function PlannerScreen() {
  return (
    <div className="absolute inset-0 font-inter">
      <ScreenHeader title={planner.title} subtitle={planner.subtitle} action={Bell} dot className="absolute left-[17px] right-[22px] top-[63px]" />

      <div className="absolute left-[14px] top-[137px] flex gap-[13px]">
        {statCards.map((c) => (
          <StatCard key={c.key} data={c} />
        ))}
        <div className="h-[160px] w-[174px] shrink-0 rounded-[22px] bg-[#f9f9f9]" />
      </div>

      <div className="absolute left-[14px] top-[307px]">
        <ScheduleCard date={planner.date} count={planner.count} days={days} activeDay={planner.activeDay} events={events} />
      </div>

      <div className="absolute inset-x-0 bottom-0 h-[150px] bg-gradient-to-b from-transparent via-[#fafafa]/80 to-[#fafafa]" />
      <FloatingNav items={navEntries} activeKey="service" className="absolute left-[50px] top-[740px]" />
    </div>
  )
}
