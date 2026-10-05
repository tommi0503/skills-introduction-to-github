import { Bell } from 'lucide-react'
import { SearchField } from '../../../ui'

interface SearchHeaderProps {
  placeholder: string
}

/** Search input with a square bell button beside it. */
export function SearchHeader({ placeholder }: SearchHeaderProps) {
  return (
    <div className="flex items-center gap-[12px]">
      <SearchField
        placeholder={placeholder}
        iconSize={19}
        iconStrokeWidth={2}
        className="h-[40px] flex-1 gap-[8px] rounded-[9px] border border-[#ececec] px-[13px] text-[#444]"
        textClassName="text-[14px] text-[#5c5c5c]"
      />
      <div className="flex h-[40px] w-[40px] items-center justify-center rounded-[9px] border border-[#ececec] text-[#111]">
        <Bell size={21} strokeWidth={2} />
      </div>
    </div>
  )
}
