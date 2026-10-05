import { Search, Sparkles } from 'lucide-react'
import { theme } from '../theme'

export function SearchBar({ placeholder, className }: { placeholder: string; className?: string }) {
  return (
    <div className={className}>
      <div className="flex gap-[9px]">
        <div className="flex h-[44px] flex-1 items-center gap-[7px] rounded-[12px] px-[14px]" style={{ background: theme.field }}>
          <Search size={17} strokeWidth={1.8} className="text-[#6f6f74]" />
          <span className="text-[16px] text-[#77777c]">{placeholder}</span>
        </div>
        <div className="flex h-[44px] w-[43px] items-center justify-center rounded-[12px]" style={{ background: theme.field }}>
          <Sparkles size={18} strokeWidth={1.8} className="text-[#111]" />
        </div>
      </div>
    </div>
  )
}
