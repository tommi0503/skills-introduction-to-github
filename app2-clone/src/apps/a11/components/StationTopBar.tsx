import { ChevronDown, Pause, Sailboat, Waves } from 'lucide-react'
import type { Condition } from '../data'
import { ConditionItem } from './ConditionItem'

const glass = 'absolute flex items-center justify-center rounded-full bg-[#1d2642]/55 text-white'

/** Station switcher row (menu, station picker, pause) and the conditions strip below it. */
export function StationTopBar({ station, conditions }: { station: string; conditions: Condition[] }) {
  return (
    <>
      <div className={glass} style={{ left: 16, top: 60, width: 40, height: 40 }}>
        <Waves size={20} strokeWidth={1.8} />
      </div>
      <div className={`${glass} justify-start`} style={{ left: 80, top: 64, width: 227, height: 33 }}>
        <Sailboat size={16} strokeWidth={2} className="ml-[10px]" />
        <span className="flex-1 text-center text-[12.5px] font-semibold">{station}</span>
        <span className="mr-[8px] flex h-[18px] w-[18px] items-center justify-center rounded-full bg-white/15">
          <ChevronDown size={12} strokeWidth={2.4} />
        </span>
      </div>
      <div className={glass} style={{ left: 330.5, top: 59.5, width: 41, height: 41 }}>
        <Pause size={19} strokeWidth={0} fill="#fff" />
      </div>
      <div
        className="absolute grid grid-cols-4 items-center justify-items-center rounded-full border border-white/25 bg-white/5 text-[15.5px] font-semibold text-white"
        style={{ left: 15, top: 110, width: 357, height: 38 }}
      >
        {conditions.map((c, i) => (
          <ConditionItem key={i} condition={c} tinted iconSize={17} />
        ))}
      </div>
    </>
  )
}
