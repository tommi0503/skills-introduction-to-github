import { CircleUserRound, Gift, House, MapPin, Search, type LucideIcon } from 'lucide-react'
import { TabBar } from '../../../ui'
import type { NavItem } from '../data'
import { theme } from '../theme'

const icons: Record<string, LucideIcon> = {
  home: House,
  explore: Search,
  rewards: Gift,
  instore: MapPin,
  account: CircleUserRound,
}

/** Frosted floating pill navigation. */
export function FloatingTabBar({ items, activeKey }: { items: NavItem[]; activeKey: string }) {
  return (
    <div
      className="absolute rounded-full bg-white/85 shadow-[0_2px_14px_rgba(0,0,0,0.08)] backdrop-blur"
      style={{ left: 22, top: 769, width: 346, height: 58 }}
    >
      <TabBar
        items={items.map((i) => ({ key: i.key, label: i.label, icon: icons[i.key] }))}
        activeKey={activeKey}
        className="h-full px-[3px]"
        renderItem={(item, active) => {
          const Icon = item.icon!
          return (
            <div
              className="flex h-[52px] flex-1 flex-col items-center justify-center gap-[3px] rounded-full"
              style={{ background: active ? '#ececf0' : undefined, color: active ? theme.purpleDeep : '#2a2a2e' }}
            >
              <Icon size={21} strokeWidth={1.7} fill={active ? theme.purpleDeep : 'none'} />
              <span className="text-[10px] leading-none font-medium">{item.label}</span>
            </div>
          )
        }}
      />
    </div>
  )
}
