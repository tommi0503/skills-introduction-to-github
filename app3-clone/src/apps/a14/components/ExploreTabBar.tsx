import { ImagePlaceholder, TabBar, type TabItem } from '../../../ui'
import type { ExploreTab } from '../data'
import { explorePalette as c } from '../theme'

export function ExploreTabBar({ tabs, active }: { tabs: ExploreTab[]; active: string }) {
  const items: TabItem[] = tabs.map((t) => ({
    key: t.key,
    icon: t.icon ?? undefined,
    label: t.label,
    node: t.icon ? undefined : <ImagePlaceholder className="rounded-[6px]" style={{ width: 22, height: 24 }} label={`${t.label} logo`} />,
  }))
  return (
    <TabBar
      items={items}
      activeKey={active}
      className="absolute inset-x-0 bottom-0 h-[92px] items-start border-t border-[#ebebeb] bg-white px-[6px] pt-[8px]"
      renderItem={(item, on) => {
        const Icon = item.icon
        return (
          <div className="flex flex-1 flex-col items-center" style={{ color: on ? c.brand : c.muted }}>
            <div className="flex h-[26px] items-center">
              {item.node ?? (Icon && <Icon size={26} strokeWidth={on ? 2.4 : 1.4} />)}
            </div>
            <span className={on ? 'mt-[2px] text-[10px] font-semibold' : 'mt-[2px] text-[10px] font-medium'}>{item.label}</span>
          </div>
        )
      }}
    />
  )
}
