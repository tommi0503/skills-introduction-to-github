import type { Point } from '../data'

/** Smooth Catmull-Rom → cubic Bézier path through the given points. */
function smoothLine(points: Point[]): string {
  return points.reduce((d, [x, y], i) => {
    if (i === 0) return `M${x},${y}`
    const [x0, y0] = points[i - 2] ?? points[i - 1]
    const [x1, y1] = points[i - 1]
    const [x3, y3] = points[i + 1] ?? [x, y]
    const c1 = [x1 + (x - x0) / 6, y1 + (y - y0) / 6]
    const c2 = [x - (x3 - x1) / 6, y - (y3 - y1) / 6]
    return `${d} C${c1[0]},${c1[1]} ${c2[0]},${c2[1]} ${x},${y}`
  }, '')
}

export interface AreaChartProps {
  layers: Point[][]
  grid: { rows: number[]; markerX: number; markerY: number; bottom: number }
  fill: string
  width: number
  height: number
}

/** Stacked translucent areas fading into the screen, dashed guides and a hover marker. */
export function AreaChart({ layers, grid, fill, width, height }: AreaChartProps) {
  return (
    <svg className="absolute left-0 top-0" width={width} height={height} viewBox={`0 0 ${width} ${height}`}>
      <defs>
        <linearGradient id="s15-mask-grad" x1="0" x2="0" y1={380} y2={grid.bottom} gradientUnits="userSpaceOnUse">
          <stop offset="0.55" stopColor="#fff" stopOpacity="1" />
          <stop offset="1" stopColor="#fff" stopOpacity="0" />
        </linearGradient>
        <mask id="s15-mask">
          <rect x="0" y="0" width={width} height={height} fill="url(#s15-mask-grad)" />
        </mask>
      </defs>
      <g mask="url(#s15-mask)">
        {layers.map((pts, i) => (
          <path
            key={i}
            d={`${smoothLine(pts)} L${pts[pts.length - 1][0]},${grid.bottom} L${pts[0][0]},${grid.bottom} Z`}
            fill={fill}
            fillOpacity={0.5}
          />
        ))}
      </g>
      {grid.rows.map((y) => (
        <line key={y} x1={14} x2={width} y1={y} y2={y} stroke="#b9b6c8" strokeWidth={1} strokeDasharray="4 4" />
      ))}
      <line x1={grid.markerX} x2={grid.markerX} y1={grid.markerY} y2={grid.bottom} stroke="#b9b6c8" strokeDasharray="4 4" />
      <circle cx={grid.markerX} cy={grid.markerY} r={6} fill="#fff" stroke="#9a96a8" strokeWidth={3} />
    </svg>
  )
}
