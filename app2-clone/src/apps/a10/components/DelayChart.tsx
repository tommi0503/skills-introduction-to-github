import { theme } from '../theme'

export interface DelayChartProps {
  bars: number[]
  pastFrom: number
  now: number
  peakLabel: string
  gridlines: { minutes: number; label: string }[]
  width?: number
  height?: number
  /** x of the first bar centre and bar pitch */
  x0?: number
  pitch?: number
  barWidth?: number
  /** y of the 2h gridline and pixels per minute */
  top?: number
  pxPerMinute?: number
}

/** Bar chart of runway delays with gridlines on the right and the current-slot marker. */
export function DelayChart({
  bars,
  pastFrom,
  now,
  peakLabel,
  gridlines,
  width = 390,
  height = 160,
  x0 = 17.5,
  pitch = 13.25,
  barWidth = 8,
  top = 20,
  pxPerMinute = 1.375,
}: DelayChartProps) {
  const maxMinutes = gridlines[0].minutes
  const y = (m: number) => top + (maxMinutes - m) * pxPerMinute
  const nowX = x0 + now * pitch
  return (
    <svg width={width} height={height} className="block overflow-visible">
      <defs>
        <linearGradient id="a10-dark" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor={theme.red} />
          <stop offset="1" stopColor={theme.red} stopOpacity="0.35" />
        </linearGradient>
        <linearGradient id="a10-light" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor={theme.redLight} />
          <stop offset="1" stopColor={theme.redLight} stopOpacity="0.45" />
        </linearGradient>
      </defs>
      {gridlines.map((g) => (
        <g key={g.label}>
          <line x1={18} x2={318} y1={y(g.minutes)} y2={y(g.minutes)} stroke="#ececee" />
          <text x={330} y={y(g.minutes) + 4} fontSize={11} fill="#8e8e93">
            {g.label}
          </text>
        </g>
      ))}
      <line x1={nowX} x2={nowX} y1={top - 6} y2={y(bars[now])} stroke="#d9d9dc" />
      {bars.map((m, i) => (
        <rect
          key={i}
          x={x0 + i * pitch - barWidth / 2}
          y={y(m)}
          width={barWidth}
          height={height - y(m)}
          rx={1.5}
          fill={i >= pastFrom && i <= now ? 'url(#a10-dark)' : 'url(#a10-light)'}
        />
      ))}
      <circle cx={nowX - 22} cy={top - 12} r={2.5} fill={theme.red} />
      <text x={nowX - 14} y={top - 8} fontSize={12} fontWeight={600} fill={theme.red}>
        {peakLabel}
      </text>
    </svg>
  )
}
