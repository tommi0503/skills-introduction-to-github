import { Wifi } from 'lucide-react'
import { Battery, SignalBars, StatusBar } from '../../../ui'

/** Status bar tuned to this recording's glyph size/position. */
export function PhoneStatus({ color = '#000' }: { color?: string }) {
  return (
    <StatusBar
      color={color}
      paddingX={40}
      paddingTop={19}
      fontSize={17}
      right={
        <div className="flex items-center gap-[7px]" style={{ paddingTop: 2 }}>
          <SignalBars size={1.15} />
          <Wifi size={18} strokeWidth={2.8} />
          <Battery size={1.1} />
        </div>
      }
    />
  )
}
