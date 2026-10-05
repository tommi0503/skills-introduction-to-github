import { useId } from 'react'
import type { Extreme } from '../data'

export interface TideLabelStyle {
  timeSize: number
  heightSize: number
  /** distance from the dot to the time / height label centres */
  timeGap: number
  heightGap: number
  unit?: string
  timeColor?: string
  heightColor?: string
}

export interface TideCurveProps {
  extremes: Extreme[]
  width: number
  height: number
  /** x of hour 0 and horizontal scale */
  x0: number
  pxPerHour: number
  /** y for the highest / lowest labelled extreme */
  yHigh: number
  yLow: number
  nowHour?: number
  /** clamp the drawn curve to this hour range */
  fromHour?: number
  toHour?: number
  labels?: TideLabelStyle
  strokeWidth?: number
  pastColor?: string
  futureColor?: string
  fillTop?: string
  fillBottom?: string
  dotRadius?: number
  className?: string
}

/** Smooth (cosine-interpolated) tide curve with filled area, extremes, labels and the "now" marker. */
export function TideCurve({
  extremes,
  width,
  height,
  x0,
  pxPerHour,
  yHigh,
  yLow,
  nowHour,
  fromHour,
  toHour,
  labels,
  strokeWidth = 4,
  pastColor = '#e6eef9',
  futureColor = '#4b8fdf',
  fillTop = 'rgba(80,145,220,0.45)',
  fillBottom = 'rgba(80,145,220,0.04)',
  dotRadius = 3,
  className,
}: TideCurveProps) {
  const gid = useId()
  const labelled = extremes.filter((e) => e.time)
  const hs = labelled.map((e) => e.height)
  const max = Math.max(...hs)
  const min = Math.min(...hs)
  const x = (h: number) => x0 + h * pxPerHour
  const y = (m: number) => (max === min ? yHigh : yLow - ((m - min) / (max - min)) * (yLow - yHigh))

  const level = (h: number) => {
    let i = extremes.findIndex((e) => e.hour > h)
    if (i <= 0) i = i === 0 ? 1 : extremes.length - 1
    const a = extremes[i - 1]
    const b = extremes[i]
    const f = Math.min(1, Math.max(0, (h - a.hour) / (b.hour - a.hour)))
    return a.height + (b.height - a.height) * (1 - Math.cos(Math.PI * f)) / 2
  }

  const start = fromHour ?? -x0 / pxPerHour
  const end = toHour ?? (width - x0) / pxPerHour
  const pts = (a: number, b: number) => {
    const out: string[] = []
    const step = 0.1
    for (let h = a; h < b; h += step) out.push(`${x(h).toFixed(1)},${y(level(h)).toFixed(1)}`)
    out.push(`${x(b).toFixed(1)},${y(level(b)).toFixed(1)}`)
    return out
  }
  const all = pts(start, end)
  const now = nowHour !== undefined ? Math.min(Math.max(nowHour, start), end) : start
  const area = `M${all[0]} L${all.join(' L')} L${x(end)},${height} L${x(start)},${height} Z`

  return (
    <svg width={width} height={height} className={className} style={{ overflow: 'visible' }}>
      <defs>
        <linearGradient id={gid} x1="0" y1="0" x2="0" y2={height} gradientUnits="userSpaceOnUse">
          <stop offset={yHigh / height} stopColor={fillTop} />
          <stop offset="1" stopColor={fillBottom} />
        </linearGradient>
      </defs>
      <path d={area} fill={`url(#${gid})`} />
      {now > start && (
        <polyline points={pts(start, now).join(' ')} fill="none" stroke={pastColor} strokeWidth={strokeWidth} strokeLinecap="round" />
      )}
      <polyline points={pts(now, end).join(' ')} fill="none" stroke={futureColor} strokeWidth={strokeWidth} strokeLinecap="round" />
      {labelled.map((e, i) => {
        const cx = x(e.hour)
        const cy = y(e.height)
        const prev = extremes[extremes.indexOf(e) - 1] ?? extremes[extremes.indexOf(e) + 1]
        const high = prev ? e.height >= prev.height : true
        const unit = labels?.unit ?? ''
        return (
          <g key={i}>
            <circle cx={cx} cy={cy} r={dotRadius} fill="#fff" />
            {labels && (
              <>
                <text
                  x={cx}
                  y={cy + (high ? -labels.timeGap : labels.timeGap)}
                  textAnchor="middle"
                  dominantBaseline="central"
                  fontSize={labels.timeSize}
                  fontWeight={600}
                  fill={labels.timeColor ?? '#fff'}
                >
                  {e.time}
                </text>
                <text
                  x={cx}
                  y={cy + (high ? labels.heightGap : -labels.heightGap)}
                  textAnchor="middle"
                  dominantBaseline="central"
                  fontSize={labels.heightSize}
                  fill={labels.heightColor ?? 'rgba(255,255,255,0.45)'}
                >
                  {e.height}
                  {unit}
                </text>
              </>
            )}
          </g>
        )
      })}
      {nowHour !== undefined && (
        <circle cx={x(nowHour)} cy={y(level(nowHour))} r={dotRadius + 1.2} fill="#e5413a" stroke="#fff" strokeWidth={1.6} />
      )}
    </svg>
  )
}
