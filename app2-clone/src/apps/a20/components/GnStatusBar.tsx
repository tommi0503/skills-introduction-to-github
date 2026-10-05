import { Wifi } from 'lucide-react'
import { Battery, HighlightChip, SignalBars, StatusBar } from '../../../ui'

/** Status bar with the Highlight capsule covering the time (sized as in the recording). */
export function GnStatusBar({ color = '#000', chipClassName = '' }: { color?: string; chipClassName?: string }) {
  return (
    <>
      <div className={`absolute left-[1px] top-[1px] z-50 font-inter [&>span]:!rounded-[9px] [&>span]:!px-[10px] [&>span]:!py-[8px] [&>span]:!text-[18px] ${chipClassName}`}>
        <HighlightChip />
      </div>
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar
          color={color}
          paddingTop={17}
          right={
            <div className="flex items-center gap-[6px]" style={{ paddingTop: 2, marginRight: 8 }}>
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
