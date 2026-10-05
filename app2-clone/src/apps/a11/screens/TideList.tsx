import { Map, Settings } from 'lucide-react'
import { AppScreen, SearchField } from '../../../ui'
import { StatusOverlay } from '../components/StatusOverlay'
import { TideCard } from '../components/TideCard'
import { stations } from '../data'

export function TideList() {
  return (
    <AppScreen background="#000" className="font-inter text-white">
      <StatusOverlay />
      <h1 className="absolute top-[60px] left-[16px] text-[34px] leading-[40px] font-bold tracking-[-0.5px]">Tide Guide</h1>
      <div className="absolute top-[58px] right-[16px] flex h-[44px] w-[44px] items-center justify-center rounded-full bg-[#1c1c1e]">
        <Settings size={22} strokeWidth={1.8} />
      </div>
      <div className="absolute top-[125px] left-[19px] flex flex-col gap-[13px]">
        {stations.map((s) => (
          <TideCard key={s.id} station={s} />
        ))}
      </div>
      <SearchField
        placeholder="Stations & Locations"
        iconSize={19}
        iconStrokeWidth={2.2}
        className="absolute top-[772px] left-[26px] h-[47px] w-[276px] gap-[10px] rounded-full bg-[#1c1c1e] pl-[20px] text-white"
        textClassName="text-[16.5px] text-[#9a9aa0]"
      />
      <div className="absolute top-[771px] left-[314px] flex h-[48px] w-[48px] items-center justify-center rounded-full bg-[#1c1c1e]">
        <Map size={21} strokeWidth={2} fill="#fff" stroke="#1c1c1e" />
      </div>
    </AppScreen>
  )
}
