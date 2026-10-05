import { Search } from 'lucide-react'
import { TabBar, cn } from '../../../ui'
import type { NavItem } from '../data'

/** Floating pill navigation with a separate search FAB. */
export function FloatingNav({ items, activeKey, widths }: { items: NavItem[]; activeKey: string; widths: Record<string, number> }) {
  const shadow = 'shadow-[0_2px_10px_rgba(0,0,0,0.15)]'
  return (
    <div className="absolute inset-x-[24px] top-[753px] flex items-center gap-[11px]">
      <TabBar
        className={cn('h-[53px] w-[276px] rounded-full bg-white/95 px-[8px] font-dm', shadow)}
        items={items}
        activeKey={activeKey}
        renderItem={(item, active) => {
          const Icon = item.icon!
          return (
            <span
              style={{ width: widths[item.key] }}
              className={cn(
                'flex h-[38px] items-center gap-[6px] rounded-full text-[15px]',
                'justify-center',
                active ? 'bg-[#d3e3fd] text-[#0b57d0]' : 'text-[#444746]',
              )}
            >
              {active && <Icon size={17} strokeWidth={2} fill="currentColor" stroke="#d3e3fd" />}
              <span className={active ? 'text-[#0b57d0]' : undefined}>{item.label}</span>
            </span>
          )
        }}
      />
      <span className={cn('flex size-[53px] items-center justify-center rounded-full bg-white text-[#1f1f1f]', shadow)}>
        <Search size={20} strokeWidth={2} />
      </span>
    </div>
  )
}
