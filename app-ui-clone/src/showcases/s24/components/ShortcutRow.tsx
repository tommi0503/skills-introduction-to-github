import { Settings } from 'lucide-react'
import { cn } from '../../../ui'
import type { IconLabel } from '../data'
import { theme } from '../theme'

export function ShortcutRow({ items, className }: { items: IconLabel[]; className?: string }) {
  return (
    <div className={cn('flex h-[30px] items-center pr-[38px] pl-[39px] font-pretendard', className)}>
      {items.map(({ icon: Icon, label }) => (
        <div key={label} className="mr-[41px] flex items-center gap-[11px]">
          <Icon size={16} strokeWidth={2} color={theme.navy} />
          <span className="text-[13.5px] tracking-[-0.2px]" style={{ color: theme.ink }}>
            {label}
          </span>
        </div>
      ))}
      <span className="ml-auto h-[14px] w-px bg-[#e3e3e8]" />
      <Settings size={15} strokeWidth={0} fill="#9aa0b4" className="ml-[25px]" />
    </div>
  )
}
