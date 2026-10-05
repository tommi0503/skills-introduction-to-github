import { TabBar, type TabItem } from '../../../ui'
import type { NavTab } from '../data'

export function RevolutTabBar({ tabs, active }: { tabs: NavTab[]; active: string }) {
  const items: TabItem[] = tabs.map((t) => ({
    key: t.key,
    label: t.label,
    icon: t.icon,
    node: t.mark ? <span className="text-[21px] leading-none font-black">{t.mark}</span> : undefined,
  }))
  return (
    <div className="absolute inset-x-0 bottom-0 h-[84px] bg-[#16161c]/95 backdrop-blur">
      <TabBar
        className="px-[8px] pt-[13px]"
        items={items}
        activeKey={active}
        renderItem={(item, on) => {
          const Icon = item.icon
          return (
            <div className="flex flex-1 flex-col items-center" style={{ color: on ? '#fff' : 'rgba(255,255,255,0.6)' }}>
              <div className="flex h-[22px] items-center">{item.node ?? (Icon && <Icon size={20} strokeWidth={2} />)}</div>
              <span className="mt-[4px] text-[10.5px] font-medium">{item.label}</span>
            </div>
          )
        }}
      />
    </div>
  )
}
