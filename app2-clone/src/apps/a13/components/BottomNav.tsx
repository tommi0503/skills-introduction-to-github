import { cn } from '../../../ui'
import type { NavItem } from '../data'

export interface BottomNavProps {
  items: NavItem[]
  activeKey: string
  className?: string
}

/** Zip tab bar: outline icons above tiny bold labels. */
export function BottomNav({ items, activeKey, className }: BottomNavProps) {
  return (
    <nav className={cn('absolute inset-x-0 bottom-0 flex bg-white px-[1px] pt-[14px]', className)} style={{ height: 86 }}>
      {items.map(({ key, label, icon: Icon }) => (
        <div
          key={key}
          className={cn(
            'flex flex-1 flex-col items-center gap-[7px]',
            key === activeKey ? 'text-[#7b62d6]' : 'text-[#24182f]',
          )}
        >
          <Icon size={25} strokeWidth={1.4} />
          <span className="font-lexend text-[11px] leading-none font-medium tracking-[-0.3px]">{label}</span>
        </div>
      ))}
    </nav>
  )
}
