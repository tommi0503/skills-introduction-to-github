import { TabBar } from '../../../ui'
import { tabs } from '../data'
import { kr } from '../theme'

/** Five-tab bottom navigation with filled glyphs; active tab in black. */
export function HomeTabBar({ activeKey }: { activeKey: string }) {
  return (
    <TabBar
      items={tabs}
      activeKey={activeKey}
      className="absolute inset-x-0 bottom-0 h-[82px] items-start border-t border-[#eaebee] bg-white px-[1px] pt-[6px]"
      renderItem={(item, active) => {
        const Icon = item.icon!
        const color = active ? '#111' : kr.faint
        return (
          <div className="flex flex-1 flex-col items-center" style={{ color }}>
            <Icon size={27} strokeWidth={1.6} fill={color} stroke="#fff" />
            <span className="mt-[3px] text-[10.5px] tracking-[-0.3px]" style={{ color: active ? '#111' : kr.sub }}>
              {item.label}
            </span>
          </div>
        )
      }}
    />
  )
}
