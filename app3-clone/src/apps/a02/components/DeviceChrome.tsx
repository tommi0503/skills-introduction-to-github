import { Wifi } from 'lucide-react'
import { Battery, DynamicIsland, HomeIndicator, SignalBars, StatusBar } from '../../../ui'

/** Status bar + dynamic island + home bar as rendered in the mockups. */
export function DeviceChrome() {
  return (
    <>
      <StatusBar className="absolute inset-x-0 top-0 font-inter" paddingX={37} paddingTop={22} fontSize={15}
        right={
          <div className="flex items-center gap-[5px] pt-[3px]">
            <SignalBars size={0.85} />
            <Wifi size={14} strokeWidth={2.8} />
            <Battery size={0.9} />
          </div>
        }
      />
      <DynamicIsland width={112} height={32} top={10} />
      <HomeIndicator width={120} bottom={10} />
    </>
  )
}
