import { Share } from 'lucide-react'
import { AppScreen, Avatar, ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { FloatingNav } from '../components/FloatingNav'
import { FlightRow } from '../components/FlightRow'
import { MapControls } from '../components/MapControls'
import { ProBanner } from '../components/ProBanner'
import { BottomFade } from '../components/BottomFade'
import { Sheet } from '../components/Sheet'
import { StatusOverlay } from '../components/StatusOverlay'
import { layover, myFlights } from '../data'
import { navTabs } from '../nav'
import { theme } from '../theme'

export function MyFlights() {
  const [first, ...rest] = myFlights
  return (
    <AppScreen background={theme.space}>
      <ImagePlaceholder tone={theme.globe} label="globe" className="absolute top-[112px] -left-[190px] h-[770px] w-[770px] rounded-full" />
      <StatusOverlay chipClassName="bg-[#454545]!" />
      <MapControls className="top-[60px]" />
      <Sheet className="inset-x-[7px] top-[360px] bottom-[8px] rounded-[36px] font-inter">
        <div className="flex h-[79px] items-center pt-[4px] pr-[25px] pl-[18px]">
          <h1 className="text-[31px] font-bold tracking-[-0.3px] text-black">My Flights</h1>
          <CircleButton icon={Share} size={40} iconSize={21} plain className="ml-auto" />
          <Avatar size={40} className="ml-[14px]" />
        </div>
        <ProBanner
          className="mx-[19px] -mt-[1px]"
          badge="PRO"
          title="Complete Your Map & Stats"
          text="Upgrade to add flights older than 12 months."
        />
        <div className="mt-[6.5px]">
          <FlightRow flight={first} tone="scheduled" height={109} dividerClassName="left-[88px] right-0" />
          <div className="flex h-[23px] items-center pr-[22px] pl-[95px] text-[13.5px] font-semibold text-black">
            {layover.duration}
            <span className="ml-[4px] font-normal text-[#9a9a9f]">{layover.where}</span>
            <span className="ml-auto">{layover.label}</span>
          </div>
          {rest.map((f) => (
            <FlightRow key={f.id} flight={f} tone="scheduled" height={109.5} dividerClassName="left-[88px] right-0" />
          ))}
        </div>
        <BottomFade className="h-[110px]" />
      </Sheet>
      <FloatingNav items={navTabs} activeKey="flights" width={260} className="bottom-[22px] left-[30px] right-[31px]" />
    </AppScreen>
  )
}
