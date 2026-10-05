import { ChartNoAxesColumn, Feather, LayoutGrid, Shield, Sunrise, Users, type LucideIcon } from 'lucide-react'
import { HomeIndicator, TabBar } from '../../../ui'
import { navOrder, type NavKey } from '../data'

const icons: Record<NavKey, LucideIcon> = {
  home: Sunrise,
  stats: ChartNoAxesColumn,
  journal: Feather,
  season: Shield,
  friends: Users,
  more: LayoutGrid,
}

/** White bottom bar with six glyph tabs and the home indicator. */
export function BottomNav({ active }: { active: NavKey }) {
  return (
    <div className="absolute inset-x-0 top-[774px] bottom-0 rounded-t-[26px] bg-white shadow-[0_-2px_10px_rgba(0,0,0,0.05)]">
      <TabBar
        items={navOrder.map((k) => ({ key: k, icon: icons[k] }))}
        activeKey={active}
        className="h-[64px] px-[30px]"
        renderItem={(item, on) => {
          const Icon = item.icon!
          const filled = item.key !== 'home' && item.key !== 'stats'
          return (
            <div className="flex flex-1 items-center justify-center" style={{ color: on ? '#111' : '#dedede' }}>
              <Icon size={26} strokeWidth={item.key === 'stats' ? 3.4 : 2.2} fill={filled ? 'currentColor' : 'none'} />
            </div>
          )
        }}
      />
      <HomeIndicator width={138} bottom={8} />
    </div>
  )
}
