import { Info, MoreHorizontal, PlaneLanding, PlaneTakeoff, Share, Star, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { DelayChart } from '../components/DelayChart'
import { IssueCard } from '../components/IssueCard'
import { Sheet } from '../components/Sheet'
import { StatBreakdown } from '../components/StatBreakdown'
import { StatusOverlay } from '../components/StatusOverlay'
import { airport, delayTrend, departureStats, issues } from '../data'
import { theme } from '../theme'

function SectionTitle({ title, subtitle, info }: { title: string; subtitle: string; info?: boolean }) {
  return (
    <div className="px-[19px]">
      <h2 className="text-[16px] leading-[20px] font-semibold tracking-[-0.2px] text-black">{title}</h2>
      <p className="flex items-center gap-[4px] text-[13px] leading-[16px] text-[#8e8e93]">
        {subtitle}
        {info && <Info size={11} strokeWidth={2} />}
      </p>
    </div>
  )
}

const toolbar = [PlaneTakeoff, PlaneLanding, Star, MoreHorizontal]

export function AirportDetail() {
  return (
    <AppScreen>
      <ImagePlaceholder tone={theme.satellite} label="satellite map" className="absolute inset-x-0 top-0 h-[120px]" />
      <StatusOverlay chipClassName="bg-[#6f6f6f]!" />
      <Sheet className="inset-x-0 top-[68px] bottom-0 rounded-t-[38px] font-inter">
        <div className="absolute top-[21px] right-[22px]">
          <CircleButton icon={X} size={46} iconSize={23} />
        </div>
        <div className="mt-[20px] flex gap-[4px] pl-[19px]">
          {airport.tags.map((t) => (
            <span key={t} className="rounded-[4px] border border-[#ececee] px-[5px] font-plexmono text-[10px] leading-[15px] text-[#8e8e93]">
              {t}
            </span>
          ))}
        </div>
        <h1 className="mt-[1px] pl-[18.5px] text-[19.5px] leading-[26px] font-semibold tracking-[-0.3px] text-black">{airport.name}</h1>
        <div className="mt-[1.5px] flex items-center pl-[18px] text-[13px] leading-[16px] font-medium tracking-[0.3px] text-[#8e8e93]">
          <ImagePlaceholder tone="#d63a2a" label="flag" className="mr-[8px] h-[14px] w-[14px] rounded-full" />
          {airport.city}
        </div>
        <IssueCard className="mx-[18px] mt-[16px]" title="Major Issues" issues={issues} linkLabel="View Full Operational Report" />
        <div className="mt-[24.5px]">
          <SectionTitle title="Departure Performance" subtitle="Current performance and future trend" />
        </div>
        <StatBreakdown className="mt-[14.5px] px-[19px]" stats={departureStats} columnWidths={[125, 162]} />
        <div className="mt-[15.5px]">
          <SectionTitle title="Takeoff Delay Trend" subtitle="Actual and estimated runway delays" info />
        </div>
        <div className="mt-[10px]">
          <DelayChart {...delayTrend} />
        </div>
      </Sheet>
      <div className="absolute bottom-[25px] left-[28px] flex h-[47px] w-[227px] items-center justify-around rounded-full bg-white/80 px-[10px] shadow-[0_4px_20px_rgba(0,0,0,0.10)] backdrop-blur-md">
        {toolbar.map((Icon, i) => (
          <Icon key={i} size={24} strokeWidth={i < 2 ? 2.2 : 1.8} />
        ))}
      </div>
      <div className="absolute right-[31px] bottom-[26px] flex h-[46px] w-[46px] items-center justify-center rounded-full text-white" style={{ background: theme.blue }}>
        <Share size={21} strokeWidth={2} />
      </div>
    </AppScreen>
  )
}
