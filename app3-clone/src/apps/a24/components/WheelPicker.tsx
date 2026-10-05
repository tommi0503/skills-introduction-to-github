import { cn } from '../../../ui'

export interface WheelColumn {
  items: string[]
  selected: number
  x: number
  align?: 'center' | 'right'
}

export interface WheelPickerProps {
  columns: WheelColumn[]
  step: number
  radius: number
  height: number
  fontSize: number
  selectedFontSize: number
  color?: string
  dimColor?: string
  band?: { left: number; right: number; height: number; color: string }
  className?: string
}

/** Wheel picker projected on a cylinder (rows at r·sinθ, squashed by cosθ). */
export function WheelPicker({ columns, step, radius, height, fontSize, selectedFontSize, color = '#000', dimColor = '#8e8e93', band, className }: WheelPickerProps) {
  const mid = height / 2
  return (
    <div className={cn('relative overflow-hidden', className)} style={{ height }}>
      {band && (
        <div
          className="absolute rounded-full"
          style={{ left: band.left, right: band.right, top: mid - band.height / 2, height: band.height, background: band.color }}
        />
      )}
      {columns.map((col, ci) =>
        col.items.map((label, i) => {
          const k = i - col.selected
          const t = (k * step * Math.PI) / 180
          if (Math.abs(t) >= Math.PI / 2) return null
          const sel = k === 0
          const fs = sel ? selectedFontSize : fontSize
          const right = col.align === 'right'
          return (
            <span
              key={`${ci}-${i}`}
              className="absolute whitespace-nowrap leading-none"
              style={{
                left: col.x,
                top: mid + radius * Math.sin(t) - fs / 2,
                fontSize: fs,
                color: sel ? color : dimColor,
                opacity: sel ? 1 : 0.3 + 0.7 * Math.cos(t) ** 2,
                transform: `${right ? 'translateX(-100%)' : 'translateX(-50%)'} scaleY(${Math.cos(t)})`,
                transformOrigin: right ? 'right center' : 'center',
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
