import { Wifi } from 'lucide-react'
import { Battery, SignalBars, StatusBar } from '../../../ui'

/** Status bar with visible time (this recording has no Highlight chip). */
export function StatusRow() {
  return (
    <StatusBar
      paddingX={54}
      paddingTop={19}
      fontSize={17}
      className="absolute inset-x-0 top-0"
      right={
        <div className="-mr-[15px] flex items-center gap-[6px] pt-[2px]">
          <SignalBars size={1.1} />
          <Wifi size={17} strokeWidth={2.8} />
          <Battery size={1.05} />
        </div>
      }
    />
  )
}
