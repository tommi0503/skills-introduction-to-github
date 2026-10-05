import { Compass } from 'lucide-react'
import { TabBar, cn } from '../../../ui'
import type { NavItem } from '../data'

export interface PillNavProps {
  items: NavItem[]
  activeKey: string
  className?: string
}

/** Glyph for a nav item: compass is drawn as a disc with a needle, others are filled lucide icons. */
function NavGlyph({ item, active }: { item: NavItem; active: boolean }) {
  if (item.key === 'explore') {
    return <Compass size={21} fill={active ? '#fff' : '#000'} color={active ? '#000' : '#fff'} strokeWidth={2} />
  }
  const Icon = item.icon
  return <Icon size={20} fill={item.filled ? 'currentColor' : 'none'} strokeWidth={item.filled ? 1.4 : 2.2} />
}

/** Floating bottom navigation: white capsule, active item becomes a labelled black pill. */
export function PillNav({ items, activeKey, className }: PillNavProps) {
  return (
    <TabBar
      items={items.map((i) => ({ key: i.key }))}
      activeKey={activeKey}
      className={cn('gap-[6px] rounded-full bg-white p-[4px]', className)}
      renderItem={(tab, active) => {
        const item = items.find((i) => i.key === tab.key)!
        return (
          <div
            className={cn(
              'flex h-[56px] items-center justify-center gap-[8px] rounded-full',
              active ? 'w-[117px] bg-black text-white' : 'w-[70px] bg-[#f2f2f3] text-black',
            )}
          >
            <NavGlyph item={item} active={active} />
            {active && <span className="text-[15.5px] font-semibold">{item.label}</span>}
          </div>
        )
      }}
    />
  )
}
