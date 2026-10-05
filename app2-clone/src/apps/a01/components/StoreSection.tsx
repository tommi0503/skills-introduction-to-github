import { ImagePlaceholder } from '../../../ui'
import type { StoreTile } from '../data'

export interface StoreSectionProps {
  title: string
  action: string
  tiles: StoreTile[]
  nextRow: StoreTile[]
  top: number
}

/** "Triple Cash Back stores" header with logo tiles (logos → placeholders). */
export function StoreSection({ title, action, tiles, nextRow, top }: StoreSectionProps) {
  const row = (items: StoreTile[], y: number) => (
    <div className="absolute flex gap-[17px]" style={{ left: 20, top: y }}>
      {items.map((t) => (
        <ImagePlaceholder key={t.key} className="h-[67px] w-[121px] rounded-[12px]" label="store logo" />
      ))}
    </div>
  )
  return (
    <>
      <div className="absolute inset-x-[20px] flex items-center justify-between" style={{ top }}>
        <span className="text-[17px] font-semibold tracking-[-0.2px] text-[#222]">{title}</span>
        <span className="text-[15px] font-semibold text-[#222]">{action}</span>
      </div>
      {row(tiles, top + 34)}
      <div className="absolute flex gap-[17px] text-[12px] font-semibold text-[#c9a3ee]" style={{ left: 20, top: top + 112 }}>
        {tiles.map((t) => (
          <span key={t.key} className="w-[121px]">
            1% Cash Back
          </span>
        ))}
      </div>
      {row(nextRow, top + 175)}
    </>
  )
}
