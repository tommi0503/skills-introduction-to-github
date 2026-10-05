import { TabBar, cn } from '../../../ui'
import { tabs } from '../data'
import { fv } from '../theme'

/** Floating capsule bar; the active tab sits on a grey disc. */
export function FiverrTabBar({ active }: { active: string }) {
  return (
    <div
      className="absolute top-[764px] left-[21px] z-40 h-[62px] w-[347px] rounded-full bg-white/95 px-[4px]"
      style={{ boxShadow: fv.halo }}
    >
      <TabBar
        items={tabs}
        activeKey={active}
        className="h-full justify-between"
        renderItem={(item, isActive) => {
          const Icon = item.icon!
          const badge = tabs.find((t) => t.key === item.key)?.badge
          return (
            <span className={cn('relative flex h-[54px] w-[71px] items-center justify-center rounded-full', isActive && 'bg-[#efefef]')}>
              <Icon size={24} strokeWidth={isActive ? 2.6 : 1.9} fill={isActive && item.key === 'home' ? 'currentColor' : 'none'} className="text-[#1b1b1b]" />
              {badge && (
                <span
                  className="absolute top-[2px] right-[8px] flex h-[16px] w-[16px] items-center justify-center rounded-full text-[10px] text-white"
                  style={{ background: fv.badgePink }}
                >
                  {badge}
                </span>
              )}
            </span>
          )
        }}
      />
    </div>
  )
}
