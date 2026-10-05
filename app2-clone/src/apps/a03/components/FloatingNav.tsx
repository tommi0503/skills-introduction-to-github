import { Activity, Atom, ChartNoAxesColumn, Inbox, Search, type LucideIcon } from 'lucide-react'
import { TabBar } from '../../../ui'
import { navItems, type NavKey } from '../data'

/** Portfolio glyph: white pulse line inside a solid rounded square. */
function PortfolioGlyph() {
  return (
    <span className="flex h-[19px] w-[19px] items-center justify-center rounded-[4px] bg-[#111] text-white">
      <Activity size={12} strokeWidth={2.6} />
    </span>
  )
}

const icons: Record<Exclude<NavKey, 'portfolio'>, LucideIcon> = {
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
          const key = item.key as NavKey
          const Icon = key === 'portfolio' ? null : icons[key]
          return (
            <div
              className="flex h-[52px] flex-1 flex-col items-center justify-center gap-[5px] rounded-full"
              style={{ background: on ? '#ececee' : undefined }}
            >
              <span className="flex h-[21px] items-center">{Icon ? <Icon size={21} strokeWidth={2.4} /> : <PortfolioGlyph />}</span>
              <span className="text-[10.5px] leading-none font-semibold">{item.label}</span>
            </div>
          )
        }}
      />
    </div>
  )
}
