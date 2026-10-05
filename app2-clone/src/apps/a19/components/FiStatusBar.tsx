import { Wifi } from 'lucide-react'
import { Battery, HighlightChip, SignalBars, StatusBar } from '../../../ui'

/** Status bar with the Highlight capsule covering the time (sized as in the recording). */
export function FiStatusBar({ color = '#000' }: { color?: string }) {
  return (
    <>
      <div className="absolute left-[1px] top-[3px] z-50 [&>span]:!rounded-[9px] [&>span]:!px-[10px] [&>span]:!py-[8px] [&>span]:!text-[18px]">
        <HighlightChip />
      </div>
      <div className="absolute inset-x-0 top-0">
        <StatusBar
          color={color}
          paddingTop={18}
          right={
            <div className="flex items-center gap-[6px] pr-[0px]" style={{ paddingTop: 2, marginRight: 8 }}>
              <SignalBars size={1.15} />
              <Wifi size={18} strokeWidth={2.8} />
              <Battery size={1.04} />
            </div>
          }
        />
      </div>
    </>
  )
}
