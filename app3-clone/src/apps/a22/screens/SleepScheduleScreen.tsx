import type { ReactNode } from 'react'
import { Bell, BedDouble } from 'lucide-react'
import { Shell } from '../components/Shell'
import { SleepClock } from '../components/SleepClock'
import { sleep } from '../data'
import { theme } from '../theme'

function TimeHeading({ x, icon, label, value }: { x: number; icon: ReactNode; label: string; value: string }) {
  return (
    <div className="absolute flex -translate-x-1/2 flex-col items-center" style={{ left: x }}>
      <span className="flex items-center gap-[3px] text-[13px] font-semibold leading-none" style={{ color: theme.label }}>
        {icon}
        {label}
      </span>
      <span className="mt-[5px] text-[22.5px] font-bold leading-none">{value}</span>
    </div>
  )
}

export function SleepScheduleScreen() {
  return (
    <Shell background="#000" statusColor="#fff">
      <div className="absolute left-[18px] right-[18px] top-[46px] h-[30px] rounded-t-[10px] bg-[#e4e4e6]" />
      <div className="absolute inset-x-0 bottom-0 top-[57px] rounded-t-[12px] bg-white">
        <span className="absolute left-[16px] top-[17px] text-[16.5px]" style={{ color: theme.iosBlue }}>{sleep.cancel}</span>
        <span className="absolute right-[17px] top-[17px] text-[16.5px] font-medium" style={{ color: theme.iosBlue }}>{sleep.add}</span>
        <h1 className="absolute inset-x-0 top-[76px] text-center text-[32px] font-bold leading-[43px]">
          {sleep.title.map((l) => (
            <span key={l} className="block">{l}</span>
          ))}
        </h1>
        <h2 className="absolute left-[18px] top-[196px] text-[19px] font-bold">{sleep.daysTitle}</h2>
        <div
          className="absolute left-[16px] right-[17px] top-[229px] flex h-[76px] items-center justify-between rounded-[10px] px-[15px]"
          style={{ background: theme.groupBg }}
        >
          {sleep.days.map((d, i) => (
            <span
              key={i}
              className="flex size-[36px] items-center justify-center rounded-full text-[15px] font-medium text-white"
              style={{ background: theme.dayBlue }}
            >
              {d}
            </span>
          ))}
        </div>
        <h2 className="absolute left-[18px] top-[338px] text-[19px] font-bold">{sleep.bedTitle}</h2>
        <div className="absolute left-[16px] right-[17px] top-[371px] h-[460px] rounded-[10px]" style={{ background: theme.groupBg }}>
          <div className="absolute inset-x-0 top-[22px]">
            <TimeHeading x={107} icon={<BedDouble size={14} fill="currentColor" />} label={sleep.bedtime.label} value={sleep.bedtime.value} />
            <TimeHeading x={250} icon={<Bell size={12} fill="currentColor" />} label={sleep.wakeup.label} value={sleep.wakeup.value} />
          </div>
          <div className="absolute left-[12px] top-[78px]">
            <SleepClock size={332} labels={sleep.labels} start={sleep.bedtime.hour} end={sleep.wakeup.hour} />
          </div>
        </div>
      </div>
    </Shell>
  )
}
