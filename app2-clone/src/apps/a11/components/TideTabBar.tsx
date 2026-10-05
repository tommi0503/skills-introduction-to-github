import { CalendarDays, ChartLine, History, MoonStar, type LucideIcon } from 'lucide-react'
import { cn, TabBar } from '../../../ui'
import { tabs, type TabKey } from '../data'

const icons: Record<TabKey, LucideIcon> = { today: History, charts: ChartLine, tables: CalendarDays, solunar: MoonStar }

/** Glassy four-tab bar at the bottom of the station screens. */
export function TideTabBar({ active, className }: { active: TabKey; className?: string }) {
  return (
    <TabBar
      items={tabs.map((t) => ({ key: t.key, icon: icons[t.key], label: t.label }))}
      activeKey={active}
      className={cn('absolute h-[60px] rounded-full border border-white/30 bg-white/10 px-[4px]', className)}
      renderItem={(item, on) => {
        const Icon = item.icon!
        return (
          <div
            className={cn(
              'flex h-[52px] flex-1 flex-col items-center justify-center rounded-full',
              on ? 'bg-white/25 text-[#8ad3ff]' : 'text-white',
            )}
          >
            <Icon size={24} strokeWidth={1.8} fill={item.key === 'solunar' ? '#fff' : 'none'} />
            <span className="mt-[3px] text-[10.5px] leading-[12px] font-semibold">{item.label}</span>
          </div>
        )
      }}
    />
  )
}
