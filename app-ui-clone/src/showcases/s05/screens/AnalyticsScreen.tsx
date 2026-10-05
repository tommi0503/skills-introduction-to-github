import { SlidersVertical } from 'lucide-react'
import { FloatingNav } from '../components/FloatingNav'
import { ScreenHeader } from '../components/ScreenHeader'
import { SelectField } from '../components/SelectField'
import { VehicleCard } from '../components/VehicleCard'
import { analytics, metrics, navEntries } from '../data'
import { cardShadow, theme } from '../theme'

export function AnalyticsScreen() {
  return (
    <div className="absolute inset-0 font-inter">
      <ScreenHeader title={analytics.title} subtitle={analytics.subtitle} action={SlidersVertical} className="absolute left-[17px] right-[22px] top-[63px]" />
      <SelectField value={analytics.vehicle} className="absolute left-[10px] right-[10px] top-[139px]" />

      <div className="absolute left-[10px] top-[203px]">
        <VehicleCard status={analytics.status} nextService={analytics.nextService} metrics={metrics} />
      </div>

      <div className="absolute left-[10px] top-[718px] h-[200px] w-[373px] rounded-[22px] px-[32px] pt-[20px]" style={{ background: theme.card, boxShadow: cardShadow }}>
        <p className="text-[16px] tracking-[-0.3px] text-[#9a9a9a]">{analytics.breakdown}</p>
      </div>

      <div className="absolute inset-x-0 bottom-0 h-[140px] bg-gradient-to-b from-[#fafafa]/0 via-[#fafafa]/85 to-[#fafafa]" />
      <FloatingNav items={navEntries} activeKey="analytics" className="absolute left-[50px] top-[744px]" />
    </div>
  )
}
