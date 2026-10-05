import { Wifi } from 'lucide-react'
import { Battery, SignalBars, StatusBar } from '../../../ui'

export function AppStatusBar() {
  return (
    <StatusBar
      paddingX={52}
      paddingTop={15}
      fontSize={16}
      className="font-inter"
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
