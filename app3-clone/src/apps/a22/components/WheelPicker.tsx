import type { CSSProperties } from 'react'
import { cn } from '../../../ui'

export interface WheelColumn {
  items: string[]
  selected: number
  /** Column centre (or right edge when align = 'right') in px from the picker's left. */
  x: number
  align?: 'center' | 'right'
}

export interface WheelPickerProps {
  columns: WheelColumn[]
  /** Angle between rows in degrees. */
  step: number
  /** Cylinder radius in px. */
  radius: number
  /** Visible height (content is clipped). The selected row sits in the middle. */
  height: number
  fontSize: number
  selectedFontSize: number
  color?: string
  dimColor?: string
  band?: { left: number; right: number; height: number; color: string; radius?: number }
  className?: string
  style?: CSSProperties
}

/** iOS wheel picker drawn as a projected cylinder: rows are placed at r·sin(θ) and squashed by cos(θ). */
export function WheelPicker({
  columns,
  step,
  radius,
  height,
  fontSize,
  selectedFontSize,
  color = '#000',
  dimColor = '#a8a8a8',
  band,
  className,
  style,
}: WheelPickerProps) {
  const mid = height / 2
  return (
    <div className={cn('relative overflow-hidden', className)} style={{ height, ...style }}>
      {band && (
        <div
          className="absolute"
          style={{
            left: band.left,
            right: band.right,
            top: mid - band.height / 2,
            height: band.height,
            background: band.color,
            borderRadius: band.radius ?? 6,
          }}
        />
      )}
      {columns.map((col, ci) =>
        col.items.map((label, i) => {
          const k = i - col.selected
          const theta = (k * step * Math.PI) / 180
          if (Math.abs(theta) >= Math.PI / 2) return null
          const y = mid + radius * Math.sin(theta)
          const sel = k === 0
          const fs = sel ? selectedFontSize : fontSize
          return (
            <span
              key={`${ci}-${i}`}
              className="absolute whitespace-nowrap leading-none"
              style={{
                top: y - fs / 2,
                fontSize: fs,
                color: sel ? color : dimColor,
                opacity: sel ? 1 : 0.35 + 0.65 * Math.cos(theta) ** 2,
                transform: `${col.align === 'right' ? 'translateX(-100%)' : 'translateX(-50%)'} scaleY(${Math.cos(theta)})`,
                transformOrigin: col.align === 'right' ? 'right center' : 'center',
                left: col.x,
              }}
            >
              {label}
            </span>
          )
        }),
      )}
    </div>
  )
}
