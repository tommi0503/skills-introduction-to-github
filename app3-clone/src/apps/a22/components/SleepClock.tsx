import { BedDouble, Bell, Sparkles, Sun } from 'lucide-react'
import type { ClockLabel } from '../data'
import { theme } from '../theme'

export interface SleepClockProps {
  size: number
  labels: ClockLabel[]
  start: number
  end: number
}

const deg = (hour: number) => (hour / 24) * 360
const polar = (c: number, r: number, a: number) => {
  const t = (a * Math.PI) / 180
  return { x: c + r * Math.sin(t), y: c - r * Math.cos(t) }
}

/** 24h sleep-schedule dial: grey ring, white bedtime→wake arc with hatching, clock face with hour labels. */
export function SleepClock({ size, labels, start, end }: SleepClockProps) {
  const c = size / 2
  const outer = c
  const band = { r: c - 18, w: 29 }
  const dial = c - 53
  let a0 = deg(start)
  const a1 = deg(end)
  if (a0 > a1) a0 -= 360
  const p0 = polar(c, band.r, a0)
  const p1 = polar(c, band.r, a1)
  const large = a1 - a0 > 180 ? 1 : 0
  const hatch = Array.from({ length: Math.floor((a1 - a0 - 16) / 1.7) }, (_, i) => a0 + 9 + i * 1.7)
  const ticks = Array.from({ length: 96 }, (_, i) => i * 3.75)
  const iconAt = (a: number) => polar(c, band.r, a)
  return (
    <div className="relative" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="absolute inset-0">
        <circle cx={c} cy={c} r={outer} fill={theme.ring} />
        <circle cx={c} cy={c} r={band.r + band.w / 2 + 3} fill="#d5d5d8" opacity={0} />
        <path
          d={`M ${p0.x} ${p0.y} A ${band.r} ${band.r} 0 ${large} 1 ${p1.x} ${p1.y}`}
          stroke="#fff"
          strokeWidth={band.w}
          strokeLinecap="round"
          fill="none"
          style={{ filter: 'drop-shadow(0 1px 1.5px rgba(0,0,0,.12))' }}
        />
        {hatch.map((a) => {
          const i = polar(c, band.r - 7, a)
          const o = polar(c, band.r + 7, a)
          return <line key={a} x1={i.x} y1={i.y} x2={o.x} y2={o.y} stroke="#e6e6e8" strokeWidth={1} />
        })}
        <circle cx={c} cy={c} r={dial} fill="#fff" />
        {ticks.map((a) => {
          const major = a % 15 === 0
          const i = polar(c, dial - (major ? 7 : 5), a)
          const o = polar(c, dial - 2, a)
          return <line key={a} x1={i.x} y1={i.y} x2={o.x} y2={o.y} stroke={major ? '#c4c4c6' : '#dedee0'} strokeWidth={1} />
        })}
      </svg>
      {labels.map((l) => {
        const p = polar(c, dial - 25, deg(l.hour))
        return (
          <span
            key={l.hour}
            className="absolute -translate-x-1/2 -translate-y-1/2 whitespace-nowrap leading-none"
            style={{ left: p.x, top: p.y }}
          >
            {l.suffix ? (
              <span className="text-[15px] font-semibold text-black">
                {l.text}
                <span className="text-[11.5px]">{l.suffix}</span>
              </span>
            ) : (
              <span className="text-[15px]" style={{ color: theme.label }}>{l.text}</span>
            )}
          </span>
        )
      })}
      <Sparkles className="absolute -translate-x-1/2" style={{ left: c, top: c - 66 }} size={17} strokeWidth={1.6} color="#3fb8b0" />
      <Sun className="absolute -translate-x-1/2" style={{ left: c, top: c + 46 }} size={18} color="#f2c230" fill="#f2c230" />
      <BedDouble strokeWidth={2} className="absolute -translate-x-1/2 -translate-y-1/2" style={{ left: iconAt(a0).x, top: iconAt(a0).y }} size={16} color="#a5a5a8" />
      <Bell className="absolute -translate-x-1/2 -translate-y-1/2" style={{ left: iconAt(a1).x, top: iconAt(a1).y }} size={15} color="#a5a5a8" fill="#a5a5a8" />
    </div>
  )
}
