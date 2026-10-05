import { Wifi } from 'lucide-react'
import { Battery, SignalBars, StatusBar } from '../../../ui'

/** Status bar tuned to this mockup's horizontal insets. */
export function AppStatusBar() {
  return (
    <StatusBar
      paddingX={38}
      fontSize={16.5}
      right={
        <div className="mr-[8px] flex items-center gap-[6px]" style={{ paddingTop: 3 }}>
          <SignalBars />
          <Wifi size={16} strokeWidth={2.8} />
          <Battery />
        </div>
      }
    />
  )
}
