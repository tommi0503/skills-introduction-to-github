import { Search, X } from 'lucide-react'
import { SearchField, cn } from '../../../ui'

/** Black search capsule with the current query and a clear button. */
export function SearchBar({ value, className }: { value: string; className?: string }) {
  return (
    <SearchField
      value={value}
      iconSize={20}
      icon={Search}
      className={cn('h-[47px] rounded-full bg-black px-[17px] text-white', className)}
      textClassName="pl-[4px] text-[16.5px] tracking-[0.1px]"
      trailing={<X size={20} strokeWidth={2} />}
    />
  )
}
