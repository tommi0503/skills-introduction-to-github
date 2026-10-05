import { Plus } from 'lucide-react'
import { AppScreen, cn } from '../../../ui'
import { FixtureCard } from '../components/FixtureCard'
import { FloatingTabBar } from '../components/FloatingTabBar'
import { PhoneStatus } from '../components/PhoneStatus'
import { TeamLogo } from '../components/TeamLogo'
import { days, favourites, fixtures } from '../data'
import { theme } from '../theme'

export function CalendarScreen() {
  return (
    <AppScreen className="font-jakarta">
      <PhoneStatus />
      <div className="absolute top-[61px] left-[10px] flex gap-[6px]">
        <div className="mr-[5px] flex h-[43px] w-[43px] items-center justify-center rounded-full text-white" style={{ background: theme.ink }}>
          <Plus size={22} strokeWidth={2.2} />
        </div>
        {favourites.map((f) => (
          <div key={f} className="flex h-[43px] w-[43px] shrink-0 items-center justify-center rounded-full border border-[#ececf0] bg-white">
            <TeamLogo size={24} className="rounded-[6px]" />
          </div>
        ))}
      </div>
      {days.map((d) => (
        <div key={d.key} className="absolute left-[17px] flex w-[30px] flex-col items-center" style={{ top: d.y }}>
          <span className="text-[10.5px] leading-[14px] font-semibold text-[#333]">{d.dow}</span>
          <span
            className={cn(
              'mt-[6px] flex h-[30px] w-[30px] items-center justify-center rounded-full text-[12px]',
              d.today ? 'text-white' : 'border border-[#e2e3e8] text-[#333]',
            )}
            style={d.today ? { background: theme.ink } : undefined}
          >
            {d.date}
          </span>
        </div>
      ))}
      {fixtures.map((f) => (
        <FixtureCard key={f.key} fixture={f} className="absolute" style={{ left: f.x, top: f.y, width: f.w, height: f.h }} />
      ))}
      <div className="absolute top-[353px] left-0 h-[2px] w-[385px]" style={{ background: theme.nowLine }} />
      <div className="absolute top-[350px] left-[54px] h-[8px] w-[8px] rounded-full" style={{ background: theme.nowLine }} />
      <div className="absolute top-[756px] left-[65px] h-px w-[310px] bg-[#e6e6ea]" />
      <FloatingTabBar />
    </AppScreen>
  )
}
