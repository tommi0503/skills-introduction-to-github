import { Search } from 'lucide-react'
import { ChipGroup } from '../../../ui'

/** Editor tool categories with a trailing search button. */
export function ToolTabs({ tools, active }: { tools: string[]; active: string }) {
  return (
    <div className="absolute inset-x-[16px] top-[748px] flex items-center">
      <ChipGroup
        gap={9}
        activeKey={active}
        items={tools.map((t) => ({ key: t, label: t }))}
        chipClassName="h-[44px] rounded-full text-[14px] text-[#e3e3e3]"
        activeClassName="w-[63px] border-[1.5px] border-[#e3e3e3]"
        inactiveClassName="px-[10px]"
      />
      <span className="flex-1" />
      <span className="flex size-[44px] items-center justify-center rounded-full bg-[#262626] text-[#e3e3e3]">
        <Search size={19} strokeWidth={2} />
      </span>
    </div>
  )
}
