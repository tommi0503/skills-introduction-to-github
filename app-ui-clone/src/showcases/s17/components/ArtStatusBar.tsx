import { Wifi } from 'lucide-react'
import { SignalBars, StatusBar } from '../../../ui'

/** iOS status bar with the numeric battery pill seen in the reference. */
export function ArtStatusBar({ level = 67 }: { level?: number }) {
  return (
    <StatusBar
      color="#111"
      paddingX={36}
      paddingTop={18}
      fontSize={17}
      height={44}
      className="font-inter"
      timeClassName="pl-[21px]"
      right={
        <div className="flex items-center gap-[5px] pt-[1px]">
          <SignalBars size={1.1} />
          <Wifi size={18} strokeWidth={2.8} />
          <span className="flex h-[14px] w-[27px] items-center justify-center rounded-[5px] bg-[#111] text-[10px] leading-none font-bold text-white">
            {level}
          </span>
          <span className="-ml-[4px] h-[5px] w-[2px] rounded-r-sm bg-[#111]" />
        </div>
      }
    />
  )
}
