import { ImagePlaceholder, TabBar, type TabItem } from '../../../ui'
import type { NavTab } from '../data'
import { palette as c } from '../theme'

export function NavBar({ tabs, active }: { tabs: NavTab[]; active: string }) {
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
      className="absolute inset-x-0 bottom-0 z-10 h-[90px] items-start border-t border-[#ebebeb] bg-white px-[6px] pt-[7px]"
      renderItem={(item, on) => {
        const Icon = item.icon
        const dot = tabs.find((t) => t.key === item.key)?.dot
        return (
          <div className="flex flex-1 flex-col items-center" style={{ color: on ? c.brand : c.muted }}>
            <div className="relative flex h-[26px] items-center">
              {item.node ?? (Icon && <Icon size={25} strokeWidth={on ? 2.4 : 1.4} />)}
              {dot && <span className="absolute -top-[1px] -right-[4px] h-[7px] w-[7px] rounded-full" style={{ background: c.brand }} />}
            </div>
            <span className={on ? 'mt-[1px] text-[10px] font-semibold' : 'mt-[1px] text-[10px] font-medium'}>{item.label}</span>
          </div>
        )
      }}
    />
  )
}
