import { Badge, ChevronRight, Plus, Search } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { ServiceTile } from '../data'
import { cu } from '../theme'

/** Pill search field with a gradient ring showing a trending keyword. */
export function TrendingSearch({ rank, keyword, trend }: { rank: string; keyword: string; trend: string }) {
  return (
    <div className="rounded-full p-[1.5px]" style={{ background: cu.searchRing }}>
      <div className="flex h-[37px] items-center rounded-full bg-white pr-[17px] pl-[18px] text-[16px]">
        <span className="font-semibold text-[#7a5cf0]">{rank}</span>
        <span className="ml-[10px] text-[#333]">{keyword}</span>
        <span className="ml-[10px] text-[#999]">{trend}</span>
        <Search size={21} strokeWidth={1.8} className="ml-auto text-[#222]" />
      </div>
    </div>
  )
}

/** Scalloped "혜택" badge icon. */
export function BenefitBadge({ label }: { label: string }) {
  return (
    <span className="relative inline-flex items-center justify-center">
      <Badge size={28} strokeWidth={1.4} className="text-[#222]" />
      <span className="absolute text-[7px] font-bold text-[#222]">{label}</span>
    </span>
  )
}

export function SectionHeading({ children, className }: { children: string; className?: string }) {
  return <h3 className={cn('text-[16px] font-bold text-[#1a1a1a]', className)}>{children}</h3>
}

export function OutlinePill({ label }: { label: string }) {
  return (
    <div className="flex h-[33.5px] w-[130px] items-center justify-center gap-[5px] rounded-full bg-white text-[12.3px] text-[#444]">
      <Plus size={15} strokeWidth={1.4} className="text-[#888]" />
      {label}
    </div>
  )
}

const tileSurface = 'rounded-[16px] bg-[#f8f8f9] shadow-[0_0_0_1px_rgba(0,0,0,0.03)]'

/** Square-ish service tile; the illustration is a placeholder. */
export function ServiceTileView({ tile, className }: { tile: ServiceTile; className?: string }) {
  if (tile.size === 'large') {
    return (
      <div className={cn('relative h-[82px] overflow-hidden', tileSurface, className)}>
        <span className="absolute top-[13px] left-[14px] text-[15px] font-bold text-[#1a1a1a]">{tile.label}</span>
        <ImagePlaceholder label={`${tile.label} illustration`} className="absolute right-[10px] bottom-0 h-[42px] w-[48px] rounded-t-[6px]" />
      </div>
    )
  }
  return (
    <div className={cn('flex flex-col items-center', className)}>
      <div className={cn('flex h-[52px] w-full items-center justify-center', tileSurface)}>
        <ImagePlaceholder label={`${tile.label} icon`} className="h-[30px] w-[30px] rounded-[6px]" />
      </div>
      <span className={cn('mt-[5px] text-[11.5px] text-[#777]', tile.bold && 'font-bold tracking-[0.3px] text-[#888]')}>{tile.label}</span>
    </div>
  )
}

export function KeepingTileView({ title, caption }: { title: string; caption: string }) {
  return (
    <div className={cn('relative h-[162px] overflow-hidden', tileSurface)}>
      <div className="absolute top-[14px] left-[15px] flex items-center text-[15.5px] font-bold text-[#1a1a1a]">
        {title}
        <ChevronRight size={15} strokeWidth={2} className="ml-[2px]" />
      </div>
      <span className="absolute top-[36px] left-[15px] text-[12.5px] text-[#aaa]">{caption}</span>
      <ImagePlaceholder label="empty box illustration" tone="#efedf7" className="absolute right-[12px] bottom-[12px] h-[70px] w-[110px] rounded-[10px]" />
    </div>
  )
}
