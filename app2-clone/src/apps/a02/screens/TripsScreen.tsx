import { ChevronDown, Ellipsis, Info, Plus } from 'lucide-react'
import { AppScreen, Toggle } from '../../../ui'
import { BottomPanel } from '../components/BottomPanel'
import { PhotoTile } from '../components/PhotoTile'
import { TopBar } from '../components/TopBar'
import { trips } from '../data'

const MoreButton = (
  <span className="absolute top-[18px] right-[12px] flex h-[32px] w-[32px] items-center justify-center rounded-full bg-white">
    <Ellipsis size={16} strokeWidth={2.6} />
  </span>
)

export function TripsScreen() {
  const sectionTop = [181, 521]
  return (
    <AppScreen className="font-inter">
      <TopBar />
      <h1 className="absolute text-[28px] font-bold tracking-[-0.4px]" style={{ left: 22, top: 71 }}>
        {trips.title}
      </h1>
      <span className="absolute flex items-center gap-[5px] rounded-full bg-black px-[13px] text-[12.5px] font-semibold text-white" style={{ left: 266, top: 76, height: 30 }}>
        <Plus size={14} strokeWidth={2.2} />
        {trips.newTrip}
      </span>
      <span className="absolute text-[16px]" style={{ left: 22, top: 130 }}>
        {trips.bookedOnly}
      </span>
      <Toggle on={false} width={50} className="!absolute left-[128px] top-[124px] shadow-[inset_0_0_0_1px_#e2e2e2]" />
      <span className="absolute flex items-center gap-[4px] text-[16px]" style={{ right: 22, top: 130 }}>
        {trips.filter}
        <ChevronDown size={16} strokeWidth={1.6} />
      </span>
      {trips.sections.map((s, i) => (
        <div key={s.key} className="absolute inset-x-[22px]" style={{ top: sectionTop[i] }}>
          <h2 className="text-[19px] font-semibold tracking-[-0.2px]">{s.title}</h2>
          <PhotoTile width={346} height={260} radius={12} className="mt-[21px]" corner={MoreButton}>
            <div className="flex items-end justify-between pb-[7px] pl-[3px]">
              <div className="flex max-w-[290px] flex-col gap-[14px]">
                <span className="text-[17px] leading-[20px] font-semibold">{s.card.title}</span>
                {s.card.subtitle && <span className="text-[13px] leading-none">{s.card.subtitle}</span>}
              </div>
              {s.card.subtitle && <Info size={18} strokeWidth={1.6} />}
            </div>
          </PhotoTile>
        </div>
      ))}
      <BottomPanel active="trips" composer={false} top={762} />
    </AppScreen>
  )
}
