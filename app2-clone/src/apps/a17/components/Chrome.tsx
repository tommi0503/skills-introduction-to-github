import { Wifi } from 'lucide-react'
import { Battery, HighlightChip, SignalBars, StatusBar } from '../../../ui'

/** Status bar + "Highlight" capsule over the time. */
export function Chrome({ color = '#000' }: { color?: string }) {
  return (
    <>
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar
          color={color}
          paddingTop={21}
          paddingX={41}
          right={
            <div className="flex items-center gap-[6px]">
              <SignalBars size={1.12} />
              <Wifi size={18} strokeWidth={2.8} />
              <Battery size={1.04} />
            </div>
          }
        />
      </div>
      <HighlightChip className="top-[25px]! text-[17px]! px-[10px]! py-[8px]! bg-[#a5a5a5]/95!" />
    </>
  )
}
