import { ChevronLeft, CircleX, Focus, Search } from 'lucide-react'
import { cn } from '../../../ui'

export interface SearchHeaderProps {
  placeholder?: string
  query?: string
}

/** Back chevron, rounded search field and the lens (image search) button. */
export function SearchHeader({ placeholder, query }: SearchHeaderProps) {
  return (
    <div className="absolute top-[54px] left-0 flex h-[32px] w-full items-center pr-[14px] pl-[16px]">
      <ChevronLeft size={26} strokeWidth={1.6} className="mr-[10px] -ml-[3px]" />
      <div className="flex h-[32px] flex-1 items-center rounded-full bg-[#f3f3f5] pr-[10px] pl-[16px]">
        <span className={cn('flex-1 text-[13.5px]', query ? 'font-medium text-[#222]' : 'text-[#b0b0b4]')}>{query ?? placeholder}</span>
        {query ? <CircleX size={20} fill="#bfc0c4" color="#fff" strokeWidth={2} /> : <Search size={19} strokeWidth={2} />}
      </div>
      <Focus size={23} strokeWidth={1.8} className="ml-[13px]" />
    </div>
  )
}
