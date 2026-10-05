import { ChevronDown, Search, Share, X } from 'lucide-react'
import { AppScreen, cn, ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { MapControls } from '../components/MapControls'
import { Sheet } from '../components/Sheet'
import { SkeletonRow } from '../components/SkeletonRow'
import { StatusOverlay } from '../components/StatusOverlay'
import { airportFilters } from '../data'
import { theme } from '../theme'

export function Airports() {
  return (
    <AppScreen background={theme.satellite}>
      <ImagePlaceholder tone={theme.satellite} label="satellite map" className="absolute inset-0" />
      <StatusOverlay chipClassName="bg-[#6f6f6f]!" />
      <MapControls variant="light" className="top-[60px]" />
      <Sheet className="inset-x-[7px] top-[357px] bottom-[8px] rounded-[36px] font-inter">
        <div className="flex h-[78px] items-center pt-[4px] pr-[21px] pl-[19.5px]">
          <h1 className="text-[31px] font-bold tracking-[-0.3px] text-black">Airports</h1>
          <CircleButton icon={Share} size={40} iconSize={21} plain className="ml-auto" />
          <CircleButton icon={X} size={44} iconSize={22} className="ml-[14px]" />
        </div>
        <div className="mt-[6px] flex h-[36px] items-center pl-[21px] text-[15.5px] tracking-[-0.2px] whitespace-nowrap">
          <span className="flex items-center gap-[4px] text-[#e2e2e4] blur-[0.6px]">
            Now <ChevronDown size={14} strokeWidth={2.4} />
          </span>
          <span className="mx-[18px] h-[22px] w-px bg-[#e3e3e5]" />
          {airportFilters.map((f, i) => (
            <span
              key={f}
              className={cn(
                'flex h-[36px] items-center rounded-full',
                i === 0 ? 'mr-[14px] -ml-[12px] bg-white px-[12px] font-semibold text-black shadow-[0_0_14px_rgba(0,0,0,0.07)]' : 'mr-[31px] text-[#555]',
              )}
            >
              {f}
            </span>
          ))}
        </div>
        <h2 className="mt-[9px] ml-[16px] text-[15px] leading-[18px] font-semibold text-black">For You</h2>
        <p className="mt-[1px] ml-[16px] text-[12.5px] leading-[16px] text-[#9a9a9f]">Favorites and airports from your active flights</p>
        <div className="mt-[22px]">
          {[0, 1, 2].map((i) => (
            <SkeletonRow key={i} />
          ))}
        </div>
      </Sheet>
      <div className="absolute right-[30px] bottom-[29px]">
        <CircleButton icon={Search} size={56} iconSize={23} strokeWidth={2.2} />
      </div>
    </AppScreen>
  )
}
