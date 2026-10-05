import { Sailboat, X } from 'lucide-react'
import { cn } from '../../../ui'
import type { Condition, Extreme } from '../data'
import { ConditionItem } from './ConditionItem'
import { TideCurve } from './TideCurve'

export interface StationSummaryCardProps {
  name: string
  place: string
  nowHour: number
  extremes: Extreme[]
  conditions: Condition[]
  className?: string
}

const W = 343
const H = 189

/** Selected-station card floating over the map. */
export function StationSummaryCard({ name, place, nowHour, extremes, conditions, className }: StationSummaryCardProps) {
  const last = extremes[extremes.length - 1].hour
  return (
    <div
      className={cn('absolute overflow-hidden rounded-[22px] border border-white/20 bg-[#0e1736]/85 backdrop-blur-md', className)}
      style={{ width: W, height: H }}
    >
      <div className="absolute top-[10px] left-[18px] w-[214px] overflow-hidden whitespace-nowrap">
        <div className="text-[15.5px] leading-[19px] font-medium text-white">{name}</div>
        <div className="text-[15px] leading-[18px] text-white/45">{place}</div>
      </div>
      <div className="absolute top-[15px] left-[264px] flex h-[34px] w-[34px] items-center justify-center rounded-full bg-[#3d86e8] text-white/40">
        <Sailboat size={16} strokeWidth={2} />
      </div>
      <div className="absolute top-[11px] left-[297px] flex h-[34px] w-[34px] items-center justify-center rounded-full bg-[#2c3448] text-white/60">
        <X size={18} strokeWidth={2.4} />
      </div>
      <TideCurve
        className="absolute top-0 left-0"
        extremes={extremes}
        width={W}
        height={145}
        x0={35.6}
        pxPerHour={14.4}
        yHigh={74}
        yLow={114}
        nowHour={nowHour}
        toHour={last}
        strokeWidth={3}
        fillTop="rgba(70,130,210,0.35)"
        fillBottom="rgba(70,130,210,0)"
        labels={{ timeSize: 10.5, heightSize: 8, timeGap: 11, heightGap: 11, unit: 'm' }}
        dotRadius={2.5}
      />
      <div className="absolute top-[153px] left-[28px] flex w-[290px] items-center justify-between text-[15.5px] text-white">
        {conditions.map((c, i) => (
          <ConditionItem key={i} condition={c} iconSize={19} />
        ))}
      </div>
    </div>
  )
}
