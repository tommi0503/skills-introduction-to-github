import { TabBar, cn } from '../../../ui'
import type { IconItem } from '../data'

/** Translucent floating capsule navigation with a soft active halo. */
export function FloatingTabBar({ items, activeKey, className }: { items: IconItem[]; activeKey: string; className?: string }) {
  return (
    <TabBar
      className={cn('h-[62px] rounded-full bg-white/65 px-[4px] shadow-[0_4px_24px_rgba(0,0,0,0.12)] backdrop-blur', className)}
      items={items.map(({ key, label, icon }) => ({ key, label, icon }))}
      activeKey={activeKey}
      renderItem={(item, active) => {
        const Icon = item.icon!
        const filled = items.find((i) => i.key === item.key)?.filled
        return (
          <div
            className={cn(
              'flex h-[56px] flex-1 flex-col items-center justify-center gap-[4px] pt-[3px] rounded-full text-[#111]',
              active && 'bg-[#ececee]/90',
            )}
          >
            <Icon size={filled ? 24 : 22} strokeWidth={filled ? 1.6 : 1.8} fill={filled ? 'currentColor' : 'none'} stroke={filled ? '#fff' : 'currentColor'} />
            <span className="text-[10.5px] font-medium">{item.label}</span>
          </div>
        )
      }}
    />
  )
}
