import { Search } from 'lucide-react'
import { theme } from '../theme'

export function HomeSearch({ placeholder }: { placeholder: string }) {
  return (
    <div
      className="absolute flex items-center gap-[9px] rounded-full pl-[15px]"
      style={{ left: 20, top: 59, width: 350, height: 43, background: theme.soft }}
    >
      <Search size={18} strokeWidth={2} color="#3a3a40" />
      <span className="text-[14px] text-[#4b4b52]">{placeholder}</span>
    </div>
  )
}
