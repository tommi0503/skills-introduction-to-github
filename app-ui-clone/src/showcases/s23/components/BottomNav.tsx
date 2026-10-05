import { HomeIndicator, ImagePlaceholder, TabBar, cn } from '../../../ui'
import { navItems, type NavItem } from '../data'

export interface BottomNavProps {
  activeKey?: string
  className?: string
}

function NavTab({ item, active }: { item: NavItem; active: boolean }) {
  const Icon = item.icon
  return (
    <div className="flex flex-1 flex-col items-center pt-[8px]">
      <div className="flex h-[25px] w-[25px] items-center justify-center">
        {item.logo ? (
          <ImagePlaceholder label="수거요청 로고" className="h-[24px] w-[24px] rounded-full" />
        ) : (
          Icon && (
            <Icon
              size={active ? 25 : 24}
              strokeWidth={active ? 2 : 1.3}
              color={active ? '#111' : '#555'}
              fill={active ? '#111' : 'none'}
            />
          )
        )}
      </div>
      <span
        className={cn('mt-[3.5px] text-[10.5px] leading-[13px] tracking-[-0.3px]', active ? 'font-semibold' : 'font-normal')}
        style={{ color: active ? '#111' : '#444' }}
      >
        {item.label}
      </span>
    </div>
  )
}

/** Laundrygo bottom tab bar with home indicator. */
export function BottomNav({ activeKey = 'home', className }: BottomNavProps) {
  return (
    <div
      className={cn('absolute inset-x-0 bottom-0 z-30 h-[88px] border-t bg-white font-pretendard', className)}
      style={{ borderColor: '#e8e8e8' }}
    >
      <TabBar
        items={navItems.map((n) => ({ key: n.key }))}
        activeKey={activeKey}
        className="items-start"
        renderItem={(tab, active) => <NavTab item={navItems.find((n) => n.key === tab.key)!} active={active} />}
      />
      <HomeIndicator width={138} bottom={8} />
    </div>
  )
}
