import { Navigation, Wifi } from 'lucide-react'
import { Battery, SignalBars, StatusBar } from '../../../ui'

export interface LaundryStatusBarProps {
  time: string
  tone?: 'dark' | 'light'
}

/** iOS status bar as captured in the Laundrygo screenshots (location arrow + charging battery). */
export function LaundryStatusBar({ time, tone = 'dark' }: LaundryStatusBarProps) {
  const color = tone === 'dark' ? '#000' : '#fff'
  return (
    <StatusBar
      time={time}
      color={color}
      paddingX={25}
      paddingTop={19}
      fontSize={17}
      timeClassName="font-pretendard font-bold gap-[5px] tracking-[-0.3px]"
      timeAddon={<Navigation size={14} strokeWidth={2.4} />}
      right={
        <div className="flex items-center gap-[6px] pt-[3px] pr-[2px]">
          <SignalBars size={1.1} />
          <Wifi size={18} strokeWidth={2.8} />
          <Battery size={1.05} level={0.62} fill="#4cd964" charging />
        </div>
      }
    />
  )
}
