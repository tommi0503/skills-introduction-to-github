import { Atom, ChartNoAxesColumn, Inbox, Search, SquareActivity, type LucideIcon } from 'lucide-react'
import { TabBar } from '../../../ui'
import { navItems, type NavKey } from '../data'

const icons: Record<NavKey, LucideIcon> = {
  portfolio: SquareActivity,
  markets: ChartNoAxesColumn,
  search: Search,
  inbox: Inbox,
  agents: Atom,
}

/** Frosted floating pill navigation with a grey disc behind the active tab. */
export function FloatingNav({ active, top = 766 }: { active: NavKey; top?: number }) {
  return (
    <div
      className="absolute rounded-full bg-white/80 shadow-[0_2px_16px_rgba(0,0,0,0.08)] backdrop-blur-md"
      style={{ left: 18, right: 18, top, height: 60 }}
    >
      <TabBar
        items={navItems}
        activeKey={active}
        className="h-full px-[4px]"
        renderItem={(item, on) => {
          const Icon = icons[item.key as NavKey]
          return (
            <div
              className="flex h-[52px] flex-1 flex-col items-center justify-center gap-[4px] rounded-full"
              style={{ background: on ? '#ececee' : undefined }}
            >
              <Icon size={20} strokeWidth={2.1} />
              <span className="text-[10.5px] leading-none font-medium">{item.label}</span>
            </div>
          )
        }}
      />
    </div>
  )
}
