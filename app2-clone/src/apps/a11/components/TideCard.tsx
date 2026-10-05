import type { StationCard } from '../data'
import { LevelBadge } from './LevelBadge'
import { TideCurve } from './TideCurve'

const W = 351
const H = 138

/** Station row on the home list: name, current level and today's curve over a sky gradient. */
export function TideCard({ station }: { station: StationCard }) {
  return (
    <div
      className="relative overflow-hidden rounded-[20px] border border-white/10"
      style={{ width: W, height: H, background: `linear-gradient(${station.sky[0]}, ${station.sky[1]})` }}
    >
      <div className="absolute inset-x-0 top-[9.5px] flex items-center pr-[12px] pl-[16px] text-white">
        <span className="min-w-0 flex-1 truncate pr-[14px] text-[13px] leading-[20px] font-semibold">{station.name}</span>
        <span className="text-[16.5px] font-bold">{station.level}</span>
        <LevelBadge rising={station.rising} className="ml-[6px]" />
      </div>
      <TideCurve
        className="absolute inset-0"
        extremes={station.extremes}
        width={W}
        height={H}
        x0={0}
        pxPerHour={W / 24}
        yHigh={61}
        yLow={110}
        nowHour={station.nowHour}
        labels={{ timeSize: 12.5, heightSize: 9.5, timeGap: 13, heightGap: 11 }}
        strokeWidth={3.5}
      />
    </div>
  )
}
