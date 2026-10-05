import type { ReactNode } from 'react'

export interface RingProps {
  size: number
  stroke: number
  progress: number
  color: string
  track: string
  children?: ReactNode
}

/** Circular progress ring starting at 12 o'clock, clockwise. */
export function Ring({ size, stroke, progress, color, track, children }: RingProps) {
  const r = (size - stroke) / 2
  const len = 2 * Math.PI * r
  return (
    <div className="relative flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="absolute inset-0 -rotate-90">
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={track} strokeWidth={stroke} />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke={color}
          strokeWidth={stroke}
          strokeDasharray={`${len * progress} ${len}`}
        />
      </svg>
      {children}
    </div>
  )
}
