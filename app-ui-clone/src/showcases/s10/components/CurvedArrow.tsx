import type { CSSProperties } from "react"

export interface CurvedArrowProps {
  /** SVG path in the box's own coordinates; the arrowhead is drawn at the path end. */
  d: string
  width: number
  height: number
  color: string
  strokeWidth?: number
  /** Arrowhead tip and direction (degrees, 0 = pointing right). */
  head: { x: number; y: number; angle: number }
  className?: string
  style?: CSSProperties
}

/** Thin curved connector with a filled triangular arrowhead. */
export function CurvedArrow({ d, width, height, color, strokeWidth = 2, head, className, style }: CurvedArrowProps) {
  return (
    <svg width={width} height={height} className={className} style={{ overflow: 'visible', ...style }}>
      <path d={d} fill="none" stroke={color} strokeWidth={strokeWidth} strokeLinecap="round" />
      <path
        d="M0 0 L-12 -7 L-12 7 Z"
        fill={color}
        transform={`translate(${head.x} ${head.y}) rotate(${head.angle})`}
      />
    </svg>
  )
}
