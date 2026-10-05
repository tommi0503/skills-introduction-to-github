import type { WeekDay } from '../data'
import { DayDot } from './DayDot'
import { SectionHeader } from './SectionHeader'
import { SoftCard } from './SoftCard'

interface WeekTrackerProps {
  title: string
  count: string
  days: WeekDay[]
  /** Card height so both trackers can match their reference spacing. */
  height: number
  headerTop: number
  labelsTop: number
}

/** Seven-day streak card: header + labelled day dots. */
export function WeekTracker({ title, count, days, height, headerTop, labelsTop }: WeekTrackerProps) {
  return (
    <SoftCard className="relative" style={{ height }}>
      <div className="absolute inset-x-[17px]" style={{ top: headerTop }}>
        <SectionHeader title={title} aside={count} titleClassName="text-[12.5px] font-bold" />
      </div>
      <div className="absolute inset-x-[13px] grid grid-cols-7 justify-items-center" style={{ top: labelsTop }}>
        {days.map((d, i) => (
          <div key={i} className="flex flex-col items-center gap-[6px]">
            <span className={d.current ? 'text-[10px] font-bold text-[#151518]' : 'text-[10px] font-medium text-[#9c9ca1]'}>
              {d.label}
            </span>
            <DayDot status={d.status} />
          </div>
        ))}
      </div>
    </SoftCard>
  )
}
