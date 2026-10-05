import { Search, SlidersHorizontal } from 'lucide-react'
import { IconButton } from '../../../ui'
import { explorePalette as c } from '../theme'

export function ExploreSearch({ title, sub }: { title: string; sub: string }) {
  return (
    <div
      className="mx-[26px] flex h-[57px] items-center rounded-full bg-white pr-[10px] pl-[20px]"
      style={{ boxShadow: '0 2px 12px rgba(0,0,0,0.12)', border: '0.5px solid #eee' }}
    >
      <Search size={18} strokeWidth={2.6} color={c.text} />
      <div className="ml-[16px] flex-1 leading-none">
        <div className="text-[13.5px] font-semibold" style={{ color: c.text }}>
          {title}
        </div>
        <div className="mt-[4px] text-[11.5px]" style={{ color: c.muted }}>
          {sub}
        </div>
      </div>
      <IconButton icon={SlidersHorizontal} size={36} iconSize={14} strokeWidth={2.2} className="border border-[#ddd] text-[#222]" />
    </div>
  )
}
