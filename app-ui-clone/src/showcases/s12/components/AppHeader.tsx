import { Equal, Wifi } from 'lucide-react'
import { Battery, ImagePlaceholder, SignalBars, StatusBar } from '../../../ui'
import { brand } from '../data'

/** iOS status bar with this mockup's insets. */
export function AppStatusBar() {
  return (
    <StatusBar
      time={brand.time}
      paddingX={46}
      paddingTop={19}
      fontSize={16}
      right={
        <div className="mr-[-6px] flex items-center gap-[6px]" style={{ paddingTop: 3 }}>
          <SignalBars />
          <Wifi size={16} strokeWidth={2.8} />
          <Battery />
        </div>
      }
    />
  )
}

/** Menu capsule on the left, blastup wordmark on the right. */
export function NavHeader() {
  return (
    <div className="absolute top-[52px] right-[18px] left-[15px] flex items-center justify-between">
      <span className="flex h-[41px] w-[61px] items-center justify-center rounded-full bg-[#efefef] text-[#8a8a8a]">
        <Equal size={18} strokeWidth={2} />
      </span>
      <span className="flex items-center gap-[5px]">
        <ImagePlaceholder label="blastup logo mark" className="h-[15px] w-[30px] rounded-[3px]" />
        <span className="text-[22px] leading-none font-bold tracking-[-0.04em] text-black">{brand.name}</span>
        <span className="mt-[10px] size-[3px] rounded-full bg-black" />
      </span>
    </div>
  )
}
