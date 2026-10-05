import type { ReactNode } from 'react'
import { Wifi } from 'lucide-react'
import { cn } from '../core/cn'
import { Battery, SignalBars, type BatteryProps } from './StatusGlyphs'

export interface StatusBarProps {
  time?: string
  /** Text/icon colour. */
  color?: string
  /** Glyph after the time (e.g. a location arrow or a "Highlight" chip). */
  timeAddon?: ReactNode
  /** Replace the default right cluster entirely. */
  right?: ReactNode
  battery?: BatteryProps
  height?: number
  /** Horizontal padding of the two clusters. */
  paddingX?: number
  /** Vertical offset of the content row from the top. */
  paddingTop?: number
  fontSize?: number
  className?: string
  timeClassName?: string
}

/** iOS status bar (logical units). Purely presentational and fully overridable. */
export function StatusBar({
  time = '9:41',
  color = '#000',
  timeAddon,
  right,
  battery,
  height = 50,
  paddingX = 32,
  paddingTop = 18,
  fontSize = 16,
  className,
  timeClassName,
}: StatusBarProps) {
  return (
    <div
      className={cn('relative z-40 flex items-start justify-between', className)}
      style={{ height, color, paddingLeft: paddingX, paddingRight: paddingX - 6, paddingTop }}
    >
      <div className={cn('flex items-center gap-1 font-semibold', timeClassName)} style={{ fontSize, lineHeight: 1.2 }}>
        <span>{time}</span>
        {timeAddon}
      </div>
      {right ?? (
        <div className="flex items-center gap-[6px]" style={{ paddingTop: 2 }}>
          <SignalBars />
          <Wifi size={16} strokeWidth={2.8} />
          <Battery {...battery} />
        </div>
      )}
    </div>
  )
}
