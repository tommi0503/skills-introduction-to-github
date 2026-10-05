import { TabBar, cn } from '../../../ui'
import { navTabs } from '../data'
import { gh } from '../theme'

/** Floating capsule tab bar; the active tab sits on a grey lozenge. */
export function FloatingTabBar({ active = 'home', className }: { active?: string; className?: string }) {
  return (
    <div
      className={cn('absolute top-[765px] left-[19px] z-40 h-[63px] w-[350px] rounded-full bg-white/95 py-[4px] pl-[12px]', className)}
      style={{ boxShadow: gh.halo }}
    >
      <TabBar
        items={navTabs.map((t) => ({ key: t.key, icon: t.icon, label: t.label }))}
        activeKey={active}
        className="h-full"
        renderItem={(item, isActive) => {
          const Icon = item.icon!
          const filled = navTabs.find((t) => t.key === item.key)?.filled
          return (
            <div
              className={cn(
                'relative flex h-full w-[81.5px] flex-col items-center justify-center gap-[3px] pt-[2px]',
                isActive ? 'text-[#2f6fdb]' : 'text-[#1f2328]',
              )}
            >
              {isActive && <span className="absolute inset-y-0 -inset-x-[6px] rounded-full bg-[#ececee]" />}
              <Icon className="relative" size={22} strokeWidth={2.2} fill={filled ? 'currentColor' : 'none'} />
              <span className="relative text-[10.5px] leading-[13px] font-semibold">{item.label}</span>
            </div>
          )
        }}
      />
    </div>
  )
}
