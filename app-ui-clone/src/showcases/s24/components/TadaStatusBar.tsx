import { Navigation, Wifi } from 'lucide-react'
import { Battery, SignalBars, StatusBar } from '../../../ui'

export interface TadaStatusBarProps {
  time: string
  /** 'badge' = blue location bubble (splash), 'arrow' = plain location arrow. */
  location?: 'badge' | 'arrow'
  battery?: { level: number; fill?: string; charging?: boolean }
  paddingX?: number
  paddingTop?: number
}

function LocationBadge() {
  return (
    <span className="flex h-[19px] w-[19px] items-center justify-center rounded-full bg-[#3b82f6]">
      <Navigation size={10} strokeWidth={0} fill="#fff" />
    </span>
  )
}

/** iOS status bar used across the TADA captures. */
export function TadaStatusBar({ time, location = 'arrow', battery = { level: 0.4 }, paddingX = 25, paddingTop = 20 }: TadaStatusBarProps) {
  return (
    <StatusBar
      time={time}
      color="#000"
      paddingX={paddingX}
      paddingTop={paddingTop}
      fontSize={17.5}
      timeClassName="font-pretendard font-bold gap-[6px] tracking-[-0.3px]"
      timeAddon={location === 'badge' ? <LocationBadge /> : <Navigation size={15} strokeWidth={1} fill="#000" />}
      right={
        <div className="flex items-center gap-[6px] pt-[3px] pr-0">
          <SignalBars size={1.2} />
          <Wifi size={19} strokeWidth={2.8} />
          <Battery size={1.05} level={battery.level} fill={battery.fill} charging={battery.charging} />
        </div>
      }
    />
  )
}
