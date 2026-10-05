import { ChipGroup } from '../../../ui'
import type { IconItem } from '../data'

/** "For you / Following / Recents" icon chips. */
export function FilterChips({ items, activeKey }: { items: IconItem[]; activeKey: string }) {
  return (
    <ChipGroup
      gap={9}
      activeKey={activeKey}
      items={items.map(({ key, label, icon: Icon, filled }) => ({
        key,
        label: (
          <>
            <Icon size={17} strokeWidth={2.4} fill={filled ? 'currentColor' : 'none'} />
            {label}
          </>
        ),
      }))}
      chipClassName="h-[35px] gap-[6px] rounded-full px-[17px] text-[16px]"
      activeClassName="bg-[#1d1d1f] text-white"
      inactiveClassName="bg-[#f2f2f3] text-[#111]"
    />
  )
}
