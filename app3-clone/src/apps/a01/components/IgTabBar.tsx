import { TabBar, cn } from '../../../ui'
import { navTabs } from '../data'

export interface IgTabBarProps {
  activeKey: string
  className?: string
}

/** Instagram bottom navigation: five icon-only tabs, active one drawn filled. */
export function IgTabBar({ activeKey, className }: IgTabBarProps) {
  return (
    <TabBar
      items={navTabs}
      activeKey={activeKey}
      className={cn('absolute inset-x-0 bottom-0 h-[82px] items-start bg-white px-[2px] pt-[15px]', className)}
      renderItem={(item, active) => {
        const Icon = item.icon!
        return (
          <div className="flex flex-1 justify-center text-black">
            <Icon size={25} strokeWidth={active ? 2 : 1.9} fill={active ? 'currentColor' : 'none'} />
          </div>
        )
      }}
    />
  )
}
