export interface LineChartProps {
  /** Samples in screen points. */
  points: [number, number][]
  /** Y of the dashed reference line (previous close). */
  baselineY: number
  baselineX?: [number, number]
  color: string
  endDot?: boolean
  strokeWidth?: number
}

/** Full-screen-width SVG overlay drawing a price line and its dashed baseline. */
export function LineChart({ points, baselineY, baselineX = [15, 375], color, endDot, strokeWidth = 1.6 }: LineChartProps) {
  const d = points.map(([x, y], i) => `${i ? 'L' : 'M'}${x} ${y}`).join(' ')
  const last = points[points.length - 1]
  return (
    <svg className="pointer-events-none absolute inset-0" width={390} height={844}>
      <line x1={baselineX[0]} x2={baselineX[1]} y1={baselineY} y2={baselineY} stroke="#c9c9cc" strokeWidth={1.2} strokeDasharray="6 5" />
      <path d={d} fill="none" stroke={color} strokeWidth={strokeWidth} strokeLinejoin="round" />
      {endDot && <circle cx={last[0]} cy={last[1]} r={3} fill={color} />}
    </svg>
  )
}
