import { ShoppingBag } from 'lucide-react'
import { TabBar, cn } from '../../../ui'
import type { NavItem } from '../data'
import { theme } from '../theme'

export interface BottomNavProps {
  items: NavItem[]
  activeKey: string
  /** Key of the raised centre action. */
  fabKey: string
}

/** White tab bar with a raised orange cart button in a bump. */
export function BottomNav({ items, activeKey, fabKey }: BottomNavProps) {
  return (
    <div className="absolute inset-x-0 bottom-0 h-[92px]">
      <div className="absolute inset-0 bg-white shadow-[0_-4px_14px_rgba(0,0,0,0.05)]" />
      <div className="absolute left-1/2 top-[-22px] h-[60px] w-[72px] -translate-x-1/2 rounded-full bg-white shadow-[0_-4px_14px_rgba(0,0,0,0.05)]" />
      <div className="absolute inset-x-0 top-0 h-[40px] bg-white" />
      <TabBar
        className="relative h-full items-start px-[14px] pt-[17px]"
        items={items.map((i) => ({ key: i.key, icon: i.icon, label: i.label }))}
        activeKey={activeKey}
        renderItem={(item, active) => {
          const isFab = item.key === fabKey
          const Icon = item.icon
          return (
            <div
              className={cn('flex flex-1 flex-col items-center text-[13.5px]', active ? 'font-medium' : 'text-[#666]')}
              style={active ? { color: theme.accent } : undefined}
            >
              {isFab ? (
                <>
                  <span
                    className="-mt-[34px] flex h-[48px] w-[48px] items-center justify-center rounded-full text-white"
                    style={{ background: theme.accent }}
                  >
                    <ShoppingBag size={22} strokeWidth={1.8} />
                  </span>
                  <span className="mt-[5px] text-[#666]">{item.label}</span>
                </>
              ) : (
                <>
                  {Icon && <Icon size={23} strokeWidth={1.5} />}
                  <span className="mt-[2px]">{item.label}</span>
                </>
              )}
            </div>
          )
        }}
      />
    </div>
  )
}
