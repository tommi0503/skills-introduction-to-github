import { Wifi } from 'lucide-react'
import { Battery, HighlightChip, SignalBars, StatusBar, cn } from '../../../ui'

export interface ChromeProps {
  color?: string
  chipClassName?: string
}

/** Status bar + "Highlight" capsule over the time. */
export function Chrome({ color = '#000', chipClassName }: ChromeProps) {
  return (
    <>
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar
          color={color}
          paddingTop={17}
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
      <HighlightChip className={cn('top-[25px]! text-[17px]! px-[10px]! py-[8px]!', chipClassName)} />
    </>
  )
}
