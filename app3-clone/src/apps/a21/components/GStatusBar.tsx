import { Wifi } from 'lucide-react'
import { Battery, StatusBar } from '../../../ui'
import { statusTime } from '../data'

/** Status bar with the "no service" dotted signal shown in the recordings. */
export function GStatusBar({ color = '#000' }: { color?: string }) {
  return (
    <StatusBar
      time={statusTime}
      color={color}
      paddingX={28}
      paddingTop={15}
      fontSize={14.5}
      right={
        <div className="flex items-center gap-[6px]" style={{ paddingTop: 2 }}>
          <div className="flex items-end gap-[2px] opacity-30">
            {[0, 1, 2, 3].map((i) => (
              <span key={i} className="size-[2.5px] rounded-full bg-current" />
            ))}
          </div>
          <Wifi size={14} strokeWidth={3} />
          <Battery />
        </div>
      }
    />
  )
}
