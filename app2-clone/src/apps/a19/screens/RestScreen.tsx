import { ChevronLeft, Moon, Share } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { FiStatusBar } from '../components/FiStatusBar'
import { CircleIcon } from '../components/CircleIcon'
import { Band, DateStepper, Metric, NightBar, PeriodTabs, SleepTimeline, TickAxis } from '../components/RestWidgets'
import { rest } from '../data'
import { fi } from '../theme'

const soft = 'shadow-[0_2px_12px_rgba(0,0,0,0.07)]'

export function RestScreen() {
  const { night } = rest
  return (
    <AppScreen>
      <FiStatusBar />
      <CircleIcon icon={ChevronLeft} size={44} iconSize={22} strokeWidth={2.2} className={`absolute left-[13px] top-[58px] ${soft}`} />
      <div className="absolute inset-x-0 top-[66px] flex items-center justify-center gap-[9px]">
        <span className="flex h-[16px] w-[16px] items-center justify-center bg-[#e1e8f7]">
          <Moon size={13} fill={fi.blue} strokeWidth={0} />
        </span>
        <span className="text-[20px] font-medium text-black">{rest.title}</span>
      </div>
      <CircleIcon icon={Share} size={44} iconSize={20} strokeWidth={2} className={`absolute left-[328px] top-[58px] ${soft}`} />

      <PeriodTabs items={rest.periods} active="Day" gaps={rest.periodGaps} className="absolute left-[16px] right-0 top-[135px]" />
      <DateStepper label={rest.date} className="absolute left-[18px] top-[191px] w-[352px]" />

      <div className="absolute left-[19px] top-[263px] text-[15px] font-medium text-black">{rest.label}</div>
      <div className="absolute left-[18px] top-[286px] font-condensed text-[46px] font-bold leading-[54px] tracking-[-1px] text-black">{rest.total}</div>
      <div className="absolute right-[23px] top-[289px] flex">
        {rest.split.map((s, i) => (
          <Metric
            key={s.label}
            label={s.label}
            value={s.value}
            color={s.tone === 'strong' ? fi.blue : fi.blueLight}
            align="center"
            divider={i > 0}
            className={i > 0 ? 'pl-[17px]' : 'pr-[20px]'}
            valueClassName="text-[20px] leading-[30px]"
          />
        ))}
      </div>

      <div className="absolute left-[19px] top-[368px] text-[15px] font-medium text-black">{rest.timelineTitle}</div>
      <SleepTimeline segments={rest.timeline} className="absolute left-[18px] top-[400px] h-[100px] w-[350px]" />
      <TickAxis labels={rest.axis} className="absolute left-[19px] right-[22px] top-[520px]" />

      <Band className="absolute inset-x-0 top-[561px]" />
      <div className="absolute left-[19px] right-[18px] top-[600px] flex justify-between text-[15px]">
        <span className="font-medium text-black">{night.title}</span>
        <span className="text-[#777]">{night.date}</span>
      </div>
      <NightBar start={night.start} end={night.end} marks={night.marks} className="absolute left-[18px] top-[641px] w-[350px]" />
      <div className="absolute left-[19px] top-[688px] flex">
        {night.stats.map((s, i) => (
          <Metric
            key={s.label}
            label={s.label}
            value={s.value}
            color={s.tone === 'blue' ? fi.blue : fi.red}
            divider={i > 0}
            className={i > 0 ? 'pl-[24px]' : 'pr-[22px]'}
            valueClassName="mt-[7px] text-[18.5px] font-semibold"
          />
        ))}
      </div>
      <Band className="absolute inset-x-0 top-[771px]" />
      <div className="absolute left-[19px] top-[812px] text-[16px] font-medium text-black">{rest.comparison}</div>
    </AppScreen>
  )
}
