import { ImagePlaceholder, TabBar } from '../../../ui'
import type { NavItem } from '../data'
import { cn } from '../../../ui'

export interface NavDockProps {
  items: NavItem[]
  activeKey: string
}

/** Floating pill tab bar with a separate brand bubble on its right. */
export function NavDock({ items, activeKey }: NavDockProps) {
  return (
    <div className="flex items-center gap-[5px]">
      <TabBar
        className="h-[52px] gap-[3px] rounded-[18px] bg-white px-[5px] shadow-[0_4px_14px_rgba(0,0,0,0.08)]"
        items={items.map((i) => ({ key: i.key, icon: i.icon }))}
        activeKey={activeKey}
        renderItem={(item, active) => {
          const Icon = item.icon!
          return (
            <div
              className={cn(
                'flex h-[42px] w-[42px] items-center justify-center rounded-[13px]',
                active ? 'bg-[#ececea] text-black' : 'text-[#a3a29e]',
              )}
            >
              <Icon size={20} strokeWidth={1.5} fill={active ? 'currentColor' : 'none'} />
            </div>
          )
        }}
      />
      <div className="flex h-[52px] w-[52px] items-center justify-center rounded-[18px] bg-white shadow-[0_4px_14px_rgba(0,0,0,0.08)]">
        <ImagePlaceholder label="Bj monogram" className="h-[22px] w-[24px] rounded-[3px]" />
      </div>
    </div>
  )
}
