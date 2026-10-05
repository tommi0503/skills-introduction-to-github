import { TabBar, cn } from '../../../ui'
import type { NavItem } from '../data'
import { theme } from '../theme'

/** Floating frosted tab pill; the active tab sits on a soft grey disc. */
export function BottomNav({ items, activeKey, className }: { items: NavItem[]; activeKey: string; className?: string }) {
  return (
    <div
      className={cn('absolute left-[22px] right-[20px] h-[60px] rounded-[30px] px-[4px]', className)}
      style={{ background: theme.navGlass, boxShadow: '0 4px 18px rgba(0,0,0,0.12)', backdropFilter: 'blur(12px)' }}
    >
      <TabBar
        items={items}
        activeKey={activeKey}
        className="h-full"
        renderItem={(item, active) => {
          const Icon = item.icon!
          return (
            <div className="relative flex h-full flex-1 flex-col items-center justify-center gap-[4px]">
              {active && <span className="absolute h-[58px] w-[70px] rounded-[30px] bg-[#e7e5e3]" />}
              <Icon size={23} strokeWidth={active ? 2 : 1.9} fill={active ? '#111' : 'none'} className="relative" />
              <span className="relative text-[10px] leading-none tracking-[-0.3px] text-[#222]">{item.label}</span>
            </div>
          )
        }}
      />
    </div>
  )
}
