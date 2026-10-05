import type { CSSProperties } from 'react'

export interface NotchedFrameProps {
  width: number
  height: number
  /** Radius of the concave (inward) corner cut. */
  notch?: number
  color?: string
  strokeWidth?: number
  className?: string
  style?: CSSProperties
}

/** Rectangular line frame whose corners are cut by inward quarter circles (classic certificate frame). */
export function NotchedFrame({ width, height, notch = 12, color = 'currentColor', strokeWidth = 2, className, style }: NotchedFrameProps) {
  const h = strokeWidth / 2
  const [l, t, r, b] = [h, h, width - h, height - h]
  const n = notch
  const d = [
    `M ${l + n} ${t}`,
    `H ${r - n}`,
    `A ${n} ${n} 0 0 0 ${r} ${t + n}`,
    `V ${b - n}`,
    `A ${n} ${n} 0 0 0 ${r - n} ${b}`,
    `H ${l + n}`,
    `A ${n} ${n} 0 0 0 ${l} ${b - n}`,
    `V ${t + n}`,
    `A ${n} ${n} 0 0 0 ${l + n} ${t}`,
    'Z',
  ].join(' ')
  return (
    <svg width={width} height={height} className={className} style={{ display: 'block', overflow: 'visible', ...style }}>
      <path d={d} fill="none" stroke={color} strokeWidth={strokeWidth} />
    </svg>
  )
}
