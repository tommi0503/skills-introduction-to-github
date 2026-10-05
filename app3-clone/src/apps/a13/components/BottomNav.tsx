import { TabBar, type TabItem } from '../../../ui'
import type { NavItem } from '../data'
import { theme } from '../theme'

export function BottomNav({ items, active }: { items: NavItem[]; active: string }) {
  const tabs: TabItem[] = items.map((i) => ({ key: i.key, icon: i.icon, label: i.label }))
  return (
    <TabBar
      items={tabs}
      activeKey={active}
      className="absolute inset-x-0 bottom-0 h-[90px] items-start bg-white px-[4px] pt-[8px] shadow-[0_-4px_10px_rgba(0,0,0,0.04)]"
      renderItem={(item, on) => {
        const src = items.find((i) => i.key === item.key)!
        const Icon = src.icon
        return (
          <div className="flex flex-1 flex-col items-center" style={{ color: on ? '#000' : theme.navInactive }}>
            <div className="relative">
              <Icon size={24} strokeWidth={on ? 2.4 : 1.8} />
              {src.badge != null && (
                <span className="absolute -top-[6px] -right-[7px] flex h-[14px] w-[14px] items-center justify-center rounded-full bg-[#0e8345] text-[9px] font-semibold text-white">
                  {src.badge}
                </span>
              )}
            </div>
            <span className={on ? 'mt-[5px] text-[10px] font-semibold' : 'mt-[5px] text-[10px]'}>{item.label}</span>
          </div>
        )
      }}
    />
  )
}
