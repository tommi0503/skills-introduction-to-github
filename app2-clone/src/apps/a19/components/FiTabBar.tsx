import { Avatar, TabBar, cn } from '../../../ui'
import type { FiTab } from '../data'

/** Bottom navigation of the Fi app. */
export function FiTabBar({ items, active, className }: { items: FiTab[]; active: string; className?: string }) {
  return (
    <TabBar
      className={cn('absolute inset-x-0 bottom-0 h-[84px] items-start bg-white px-[0px] pt-[8px]', className)}
      items={items.map((t) => ({ key: t.key, label: t.label }))}
      activeKey={active}
      renderItem={(item, on) => {
        const tab = items.find((t) => t.key === item.key)!
        const Icon = tab.icon
        return (
          <div className={cn('flex w-[97px] flex-col items-center gap-[4px]', on ? 'text-black' : 'text-[#9a9a9a]')}>
            {tab.avatar ? (
              <Avatar size={24} />
            ) : Icon ? (
              <Icon size={23} strokeWidth={on ? 2.4 : 1.6} fill={on ? 'currentColor' : 'none'} className={on ? '[&>circle]:fill-white' : ''} />
            ) : null}
            <span className={cn('text-[11.5px]', on ? 'font-semibold' : 'font-normal')}>{item.label}</span>
          </div>
        )
      }}
    />
  )
}
