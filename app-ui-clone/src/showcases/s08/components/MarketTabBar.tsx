import { TabBar } from '../../../ui'
import { tabs } from '../data'
import { theme } from '../theme'

/** Bottom navigation: five icons, the active one filled/dark with a terracotta tick below. */
export function MarketTabBar({ active, fillActive = false }: { active: string; fillActive?: boolean }) {
  return (
    <div className="absolute inset-x-0 bottom-0 h-[56px] border-t" style={{ background: theme.bg, borderColor: theme.hairline }}>
      <TabBar
        items={tabs}
        activeKey={active}
        className="h-[54px] px-[21px]"
        renderItem={(item, isActive) => {
          const Icon = item.icon!
          return (
            <div className="relative flex h-full flex-1 items-center justify-center" style={{ color: isActive ? theme.ink : '#5f5952' }}>
              <Icon size={22} strokeWidth={isActive ? 2.4 : 1.8} fill={isActive && fillActive ? theme.ink : 'none'} />
              {isActive && <span className="absolute bottom-[-3px] h-[4px] w-[15px]" style={{ background: theme.accent }} />}
            </div>
          )
        }}
      />
    </div>
  )
}
