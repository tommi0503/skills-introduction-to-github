import { useId } from 'react'
import { theme } from '../theme'

export interface ScoreRingProps {
  /** 0..100 */
  value: number
  label: string
  size?: number
  thickness?: number
  /** Visual gap at 12 o'clock, in degrees. */
  gapDeg?: number
}

/** Point on a circle (0deg = 12 o'clock, clockwise). */
function polar(c: number, r: number, deg: number) {
  const a = ((deg - 90) * Math.PI) / 180
  return `${c + r * Math.cos(a)} ${c + r * Math.sin(a)}`
}

function arc(c: number, r: number, from: number, to: number) {
  const large = to - from > 180 ? 1 : 0
  return `M ${polar(c, r, from)} A ${r} ${r} 0 ${large} 1 ${polar(c, r, to)}`
}

/** Gradient progress ring with round caps around a bordered dial. */
export function ScoreRing({ value, label, size = 292, thickness = 18, gapDeg = 18 }: ScoreRingProps) {
  const id = useId()
  const c = size / 2
  const r = c - thickness / 2 - 2
  const start = gapDeg / 2 - 4
  const end = 360 - gapDeg / 2 - 4
  const dial = 217
  const dc = dial / 2
  return (
    <div className="relative" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="absolute inset-0 overflow-visible">
        <defs>
          <linearGradient id={`${id}g`} x1="0" y1="0" x2="1" y2="0">
            <stop offset="0" stopColor="#5cc2fd" />
            <stop offset="0.45" stopColor="#64c0ee" />
            <stop offset="1" stopColor="#6cb8cf" />
          </linearGradient>
          <filter id={`${id}b`}>
            <feGaussianBlur stdDeviation="1" />
          </filter>
        </defs>
        <path d={arc(c, r, start, end)} fill="none" stroke={`url(#${id}g)`} strokeWidth={thickness} strokeLinecap="round" filter={`url(#${id}b)`} />
      </svg>

      <div
        className="absolute rounded-full border-[12px] border-[#f1f1ef] bg-white"
        style={{ width: dial, height: dial, left: c - dc, top: c - dc, boxShadow: 'inset 0 0 6px rgba(0,0,0,0.04), 0 1px 6px rgba(0,0,0,0.04)' }}
      >
        <svg width={dial - 24} height={dial - 24} className="absolute inset-0">
          {[
            { r: 64, from: 290, to: 20 },
            { r: 76, from: 300, to: 10 },
            { r: 66, from: 110, to: 200 },
            { r: 78, from: 120, to: 190 },
          ].map((a, i) => (
            <path
              key={i}
              d={arc(dc - 12, a.r, a.from, a.to < a.from ? a.to + 360 : a.to)}
              fill="none"
              stroke="#bfe0fb"
              strokeWidth={1}
            />
          ))}
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="mt-[6px] text-[42px] leading-none font-medium tracking-[-0.5px]" style={{ color: theme.blueText }}>
            {value}%
          </span>
          <span className="mt-[11px] text-[11px] text-[#b5b5b5]">{label}</span>
        </div>
      </div>
    </div>
  )
}
