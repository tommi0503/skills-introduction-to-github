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
            <Icon size={filled ? 18 : 17} strokeWidth={filled ? 1.8 : 2.4} fill={filled ? 'currentColor' : 'none'} stroke={filled ? '#f2f2f3' : 'currentColor'} />
            {label}
          </>
        ),
      }))}
      chipClassName="h-[35px] gap-[6px] rounded-full px-[16px] text-[15.5px]"
      activeClassName="bg-[#1d1d1f] text-white"
      inactiveClassName="bg-[#f2f2f3] text-[#111]"
    />
  )
}
