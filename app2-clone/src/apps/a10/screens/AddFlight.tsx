import { ChevronDown, Eye, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { FloatingNav } from '../components/FloatingNav'
import { FlightRow } from '../components/FlightRow'
import { BottomFade } from '../components/BottomFade'
import { Sheet } from '../components/Sheet'
import { StatusOverlay } from '../components/StatusOverlay'
import { addFlightDate, addFlightTabs, searchResults } from '../data'
import { navTabs } from '../nav'
import { theme } from '../theme'

function FieldChip({ label, className }: { label: string; className?: string }) {
  return (
    <div className={`flex h-[46px] items-center rounded-[14px] bg-[#f3f3f5] px-[16px] text-[16.5px] tracking-[-0.2px] ${className ?? ''}`}>{label}</div>
  )
}

function FilterPill({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-[34px] items-center gap-[7px] rounded-full border border-[#e6e6e9] bg-white px-[12px] text-[14.5px] tracking-[-0.2px] text-black">
      {children}
    </div>
  )
}

export function AddFlight() {
  return (
    <AppScreen background={theme.space}>
      <ImagePlaceholder tone="#3c4a3e" label="globe" className="absolute top-[12px] -left-[30px] h-[260px] w-[450px] rounded-[50%]" />
      <StatusOverlay />
      <Sheet className="inset-x-0 top-[58px] bottom-0 rounded-t-[38px] font-inter">
        <div className="absolute top-[20px] right-[23.5px]">
          <CircleButton icon={X} size={46} iconSize={23} strokeWidth={2} />
        </div>
        <h1 className="mt-[23px] ml-[19.5px] text-[32.5px] leading-[36px] font-bold tracking-[-0.5px] text-black">Add Flight</h1>
        <p className="mt-[2px] ml-[21px] flex items-center text-[16px] leading-[20px] text-[#8e8e93]">
          Tap flight to add to <span className="ml-[4px] font-semibold text-black">My Flights</span>
          <ChevronDown size={16} strokeWidth={2.6} className="ml-[2px] text-black" />
        </p>
        <div className="mt-[16px] flex gap-[10px] px-[17px]">
          {addFlightTabs.map((t) => (
            <FieldChip key={t} label={t} className="w-[66px]" />
          ))}
          <FieldChip label={addFlightDate} className="flex-1" />
        </div>
        <div className="mt-[20.5px] flex gap-[7px] px-[15px]">
          <FilterPill>
            <Eye size={20} strokeWidth={2.8} />
            Codeshares
          </FilterPill>
          <FilterPill>
            All Airlines <ChevronDown size={16} strokeWidth={2.2} />
          </FilterPill>
        </div>
        <div className="mt-[17px]">
          {searchResults.map((f) => (
            <FlightRow key={f.id} flight={f} dividerClassName="left-[96px] right-[18px]" />
          ))}
        </div>
        <BottomFade className="h-[120px]" />
      </Sheet>
      <FloatingNav items={navTabs} width={278} searchClassName="relative text-[#2f7cf6]" className="bottom-[20px] left-[22px] right-[23px]" />
    </AppScreen>
  )
}
