import { ArrowDown, ArrowUp } from 'lucide-react'
import type { Strategy } from '../data'
import { theme } from '../theme'

const W = 170
const H = 84

/** Option-strategy card: payoff diagram (line vs. zero, area between filled) + name and sentiment. */
export function PayoffCard({ strategy, zeroY }: { strategy: Strategy; zeroY: number }) {
  const pts = strategy.points
  const line = pts.map(([x, y]) => `${x},${y}`).join(' ')
  const area = `${pts[0][0]},${zeroY} ${line} ${pts[pts.length - 1][0]},${zeroY}`
  const bullish = strategy.sentiment === 'Bullish'
  const Arrow = bullish ? ArrowUp : ArrowDown
  return (
    <div className="h-[145px] w-[170px] overflow-hidden rounded-[8px] bg-white shadow-[0_0_0_1px_#e8e8ea]">
      <svg width={W} height={H} className="block" style={{ background: theme.chartBg }}>
        <polygon points={area} fill={theme.payoffFill} />
        <line x1={0} x2={W} y1={zeroY} y2={zeroY} stroke="#c9c9d6" strokeDasharray="4 3" />
        <polyline points={line} fill="none" stroke={theme.payoffLine} strokeWidth={1.6} />
        <circle cx={strategy.dot[0]} cy={strategy.dot[1]} r={4} fill={theme.payoffLine} />
      </svg>
      <div className="px-[12px] pt-[14px]">
        <div className="text-[14.5px] leading-[18px] font-medium">{strategy.name}</div>
        <div className="mt-[3px] flex items-center gap-[3px] text-[12.5px] font-semibold" style={{ color: bullish ? theme.green : theme.red }}>
          {strategy.sentiment}
          <Arrow size={13} strokeWidth={2.4} />
        </div>
      </div>
    </div>
  )
}
