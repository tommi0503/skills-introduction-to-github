import { Bell } from 'lucide-react'
import { Avatar } from '../../../ui'
import { FoodFan } from '../components/FoodFan'
import { HintBox } from '../components/HintBox'
import { PickCard } from '../components/PickCard'
import { RoundButton } from '../components/RoundButton'
import { FoodTabBar } from '../components/TabBar'
import { homeScreen as d } from '../data'
import { theme } from '../theme'

/** Side cards peek in at 94% scale, anchored to the gap beside the main card. */
const pickLayout = [
  { left: 41.7, top: 445, origin: 'top right', shift: '-100%', scale: 0.94 },
  { left: 54.8, top: 415.3, origin: 'top left', shift: '0', scale: 1 },
  { left: 349.7, top: 445, origin: 'top left', shift: '0', scale: 0.94 },
]

export function HomeScreen() {
  return (
    <div className="absolute inset-0">
      <div className="absolute top-[70px] left-[15px]">
        <div className="text-[14px] leading-[18px]" style={{ color: theme.muted }}>
          {d.greeting}
        </div>
        <div className="mt-[3px] font-condensed text-[19px] leading-[22px] font-bold text-[#111]">{d.name}</div>
      </div>
      <div className="absolute top-[67px] right-[10px] flex gap-[11px]">
        <RoundButton icon={Bell} size={52} iconSize={19} strokeWidth={2} />
        <Avatar size={52} tone="#cddff8" />
      </div>

      <div className="absolute top-[142px] left-[16px] font-condensed text-[28px] leading-[34px] font-bold text-[#111]">
        {d.headline.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>

      <div className="absolute top-[233px] left-[162px]">
        <FoodFan angles={d.fan} width={66} height={92} />
      </div>
      <div className="absolute top-[315px] right-[15px] left-[16px] z-20">
        <HintBox text={d.hint} />
      </div>

      {d.picks.map((p, i) => {
        const l = pickLayout[i]
        return (
          <div
            key={p.key}
            className="absolute"
            style={{ left: l.left, top: l.top, transform: `translateX(${l.shift}) scale(${l.scale})`, transformOrigin: l.origin }}
          >
            <PickCard pick={p} />
          </div>
        )
      })}

      <div className="absolute right-0 bottom-0 left-0 h-[110px]" style={{ background: 'linear-gradient(180deg, rgba(255,255,255,0), #fff 30%)' }} />
      <FoodTabBar activeKey="home" top={748} />
    </div>
  )
}
