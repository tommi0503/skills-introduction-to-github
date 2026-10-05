import { Waves, Wind } from 'lucide-react'

export interface CompassProps {
  cx: number
  cy: number
  size: number
  speed: string
  direction: string
  gusts: string
}

const letters = [
  { l: 'N', a: 0, c: '#5aa0f0' },
  { l: 'E', a: 90 },
  { l: 'S', a: 180 },
  { l: 'W', a: 270 },
]

/** Wind compass dial with tick marks, cardinal letters and the speed read-out. */
export function Compass({ cx, cy, size, speed, direction, gusts }: CompassProps) {
  const r = size / 2
  const ticks = Array.from({ length: 72 }, (_, i) => i * 5)
  return (
    <div className="absolute" style={{ left: cx - r, top: cy - r, width: size, height: size }}>
      <svg width={size} height={size} className="absolute inset-0">
        <circle cx={r} cy={r} r={r - 2} fill="rgba(60,72,104,0.55)" stroke="rgba(160,170,195,0.75)" strokeWidth={3.5} />
        {ticks.map((a) => {
          const rad = (a * Math.PI) / 180
          const long = a % 30 === 0
          const r1 = r - 9
          const r2 = r1 - (long ? 5 : 3)
          return (
            <line
              key={a}
              x1={r + r1 * Math.sin(rad)}
              y1={r - r1 * Math.cos(rad)}
              x2={r + r2 * Math.sin(rad)}
              y2={r - r2 * Math.cos(rad)}
              stroke="rgba(255,255,255,0.35)"
              strokeWidth={1}
            />
          )
        })}
        {letters.map(({ l, a, c }) => {
          const rad = (a * Math.PI) / 180
          return (
            <text
              key={l}
              x={r + (r - 11) * Math.sin(rad)}
              y={r - (r - 11) * Math.cos(rad)}
              textAnchor="middle"
              dominantBaseline="central"
              fontSize={9.5}
              fontWeight={700}
              fill={c ?? '#fff'}
            >
              {l}
            </text>
          )
        })}
      </svg>
      <Wind size={13} strokeWidth={2} className="absolute text-white" style={{ left: 16, top: r - 13 }} />
      <Waves size={13} strokeWidth={2} className="absolute text-white/80" style={{ left: 160, top: 128 }} />
      <div className="absolute inset-x-0 flex items-center justify-center gap-[4px] text-[11.5px] text-white/40" style={{ top: 54 }}>
        <Wind size={12} strokeWidth={2} />
        Wind Speed
      </div>
      <div className="absolute inset-x-0 flex items-baseline justify-center gap-[8px] text-white" style={{ top: 70 }}>
        <span className="text-[41px] leading-[52px] font-bold">{speed}</span>
        <span className="text-[22px] text-white/80">{direction}</span>
      </div>
      <div className="absolute inset-x-0 text-center text-[11px] text-white/55" style={{ top: 122 }}>
        {gusts}
      </div>
    </div>
  )
}
